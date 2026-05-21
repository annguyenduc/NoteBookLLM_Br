"""
gap_check.py — Local Model Gap-Check (Phase 2, Wiki 2.0)

Vai trò: "Second opinion" sau khi Gemini extract atoms từ 1 chunk markdown.
Gọi qwen3:4b via Ollama REST API để phát hiện candidates bị bỏ sót.

Luồng gọi (Scout Analysis):
  atoms = gemini_extract(chunk)
  python gap_check.py --chunk <file> --atoms <json_list> --source <name> --chunk-num <n>
  save_atoms(atoms)           ← luôn chạy, không bị block

Flags:
  --skip-gap-check            Bypass hoàn toàn (không gọi Ollama)

Output:
  00_Inbox/gap_candidates/<source>_gap_<n>.md

Non-blocking: exit code luôn 0 kể cả khi Ollama offline / timeout.
"""

import os
import re
import sys
import json
import argparse
import logging
import urllib.request
import urllib.error
import yaml
import shutil
from datetime import datetime, timezone

# --- Cấu hình ---
OLLAMA_URL    = "http://localhost:11434/api/generate"
GAP_MODEL     = os.getenv("GAP_CHECK_MODEL", "gemma3:4b")  # Optimized for Atomic Extraction & Source Metadata
TIMEOUT_SEC   = 60
SCRIPT_ROOT   = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
CANONICAL_ROOT = r"D:\NoteBookLLM_Br"
ROOT_DIR      = os.getenv(
    "NOTEBOOKLLM_ROOT",
    CANONICAL_ROOT if os.path.exists(CANONICAL_ROOT) else SCRIPT_ROOT
)
OUTPUT_DIR    = os.path.join(ROOT_DIR, "00_Inbox", "gap_candidates")
FAILED_DIR    = os.path.join(ROOT_DIR, "00_Inbox", "failed_queue")

# --- Logger --- stdout UTF-8 để tránh cp1252 trên Windows terminal
logging.basicConfig(
    level=logging.INFO,
    format="[gap_check] %(levelname)s: %(message)s",
    handlers=[logging.StreamHandler(
        open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1, closefd=False)
    )]
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------------

PROMPT_TEMPLATE = """\
You are a knowledge gap detector for a personal knowledge vault designed to accelerate learning.
Priority atom types: Concept, Entity, Method, Principle, Mental Model, Relationship.
Your goal is to find missing information.

A human assistant already extracted {atom_count} concepts/entities from this text chunk.

=== CHUNK (chunk #{chunk_num} of source: {source}) ===
{chunk_text}
=== END CHUNK ===

Atoms already extracted:
{atoms_list}

TASK: List important concepts, entities, or relationships in the chunk NOT mentioned above.
STRICT RULES:
1. Respond ONLY with bullet points starting with "- [Type] Name: Description".
2. No preamble, no "Here are the gaps", no thinking out loud.
3. If nothing is missed, write exactly: NONE.
4. If the chunk is in Vietnamese, respond in Vietnamese. If English, respond in English.
5. A valid gap must be source-specific knowledge that a learner should preserve as a Wiki atom.
6. IGNORE generic illustrative examples, analogies, metaphors, and everyday nouns used only to explain another concept (e.g., digestive system, football team, school, city).
7. IGNORE broad/common terms that are already represented by the extracted atoms list, even if the exact wording appears again in the chunk.
8. When uncertain whether a candidate is core knowledge or just an example, omit it. Prefer NONE over false positives.

Format (STRICTLY follow this):
- [Concept] <name>: <1 sentence value>
- [Entity] <name>: <1 sentence role>
- [Mental Model] <name>: <1 sentence application>
- [Relationship] <name>: <1 sentence connection>
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_chunk_file(path: str) -> str:
    """Đọc chunk text từ file tạm hoặc trực tiếp."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def validate_yaml_gate(content: str) -> tuple[bool, str | None]:
    """
    Kiểm tra tính hợp lệ của YAML Frontmatter.
    Trả về (True, None) nếu hợp lệ hoặc không có frontmatter.
    Trả về (False, error_msg) nếu YAML lỗi.
    """
    if not content.startswith("---"):
        return True, None # Không có frontmatter thì bỏ qua validation này

    parts = content.split("---", 2)
    if len(parts) < 3:
        return True, None # Không đủ cặp --- thì không phải frontmatter chuẩn

    yaml_text = parts[1]
    try:
        yaml.safe_load(yaml_text)
        return True, None
    except Exception as e:
        return False, str(e)


def call_ollama(prompt: str) -> str | None:
    """
    Gọi Ollama REST API, timeout 60s.
    Trả về response text hoặc None nếu offline/timeout.
    """
    payload = json.dumps({
        "model": GAP_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 1024,
            "num_ctx": 4096,
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("response", "").strip()
    except urllib.error.URLError as e:
        log.warning(f"Ollama offline hoặc không kết nối được: {e}. Pipeline tiếp tục bình thường.")
        return None
    except TimeoutError:
        log.warning(f"Ollama timeout sau {TIMEOUT_SEC}s. Pipeline tiếp tục bình thường.")
        return None
    except Exception as e:
        log.warning(f"Lỗi không xác định khi gọi Ollama: {e}. Pipeline tiếp tục bình thường.")
        return None


def save_to_failed_queue(source: str, chunk_num: int, error_msg: str, atoms_json: str, chunk_path: str = None, chunk_text: str = None):
    """Ghi nhận lỗi vào Dead-Letter Queue (DLQ) để xử lý sau."""
    os.makedirs(FAILED_DIR, exist_ok=True)
    safe_source = "".join(c if c.isalnum() or c in "-_" else "_" for c in os.path.basename(source))
    fail_file = os.path.join(FAILED_DIR, f"{safe_source}_chunk_{chunk_num:03d}.failed")

    # Xây dựng command retry
    retry_cmd = f"python .agent/skills/wiki-ingest/scripts/gap_check.py --source \"{source}\" --chunk-num {chunk_num} --atoms '{atoms_json}'"

    temp_text_path = None
    if chunk_path:
        retry_cmd += f" --chunk \"{chunk_path}\""
    elif chunk_text:
        # Lưu text trực tiếp vào file tạm để retry
        temp_text_path = os.path.join(FAILED_DIR, f"{safe_source}_chunk_{chunk_num:03d}.txt")
        with open(temp_text_path, "w", encoding="utf-8") as f:
            f.write(chunk_text)
        retry_cmd += f" --chunk \"{temp_text_path}\""

    error_data = {
        "timestamp": datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "source": source,
        "chunk_num": chunk_num,
        "error": error_msg,
        "status": "REQUIRES_RETRY",
        "retry_command": retry_cmd
    }
    if temp_text_path:
        error_data["chunk_text_saved_to"] = temp_text_path

    with open(fail_file, "w", encoding="utf-8") as f:
        json.dump(error_data, f, indent=2, ensure_ascii=False)
    log.warning(f"[DLQ] Gap-check failed. Logged to: {fail_file}")


CANONICAL_TYPES = {
    "concept": "Concept", "khái niệm": "Concept", "khai niem": "Concept",
    "entity": "Entity", "thực thể": "Entity", "thuc the": "Entity",
    "method": "Method", "phương pháp": "Method", "phuong phap": "Method",
    "principle": "Principle", "nguyên lý": "Principle", "nguyen ly": "Principle", "nguyên tắc": "Principle", "nguyen tac": "Principle",
    "mental model": "Mental Model", "mô hình tư duy": "Mental Model", "mo hinh tu duy": "Mental Model",
    "relationship": "Relationship", "quan hệ": "Relationship", "quan he": "Relationship", "mối quan hệ": "Relationship", "moi quan he": "Relationship"
}

ILLUSTRATIVE_BLACKLIST = {
    "digestive system", "football team", "school", "city", "solar system",
    "clock", "car", "bicycle", "family", "team", "classroom", "human body",
    "organism", "corporation", "computer", "traffic system"
}

def parse_gap_line(line: str) -> tuple[str, str, str] | None:
    """
    Parse một dòng gap candidate.
    Trả về (canonical_type, name, description) nếu hợp lệ, ngược lại trả về None.
    """
    line = line.strip()
    if not line:
        return None

    # Loại bỏ bullet prefix ở đầu dòng: -, *, +, 1., 2.
    line = re.sub(r'^[-*+\s]+|^\d+\.\s*', '', line).strip()
    if not line:
        return None

    # Regex nhận diện [Type] ở đầu
    match_type = re.match(r'^[\[{(]([^\]})]+)[\]})]\s*(.*)', line)
    if not match_type:
        return None

    raw_type = match_type.group(1).strip().lower()
    rest = match_type.group(2).strip()

    # Chuẩn hóa Type
    canonical_type = None
    for key, val in CANONICAL_TYPES.items():
        if raw_type == key or raw_type.startswith(key) or key.startswith(raw_type):
            canonical_type = val
            break

    if not canonical_type:
        return None

    # Phân tách Name và Description. Dấu gạch ngang chỉ là delimiter khi có khoảng trắng hai bên,
    # để không cắt sai các tên hợp lệ như "First-Order" hoặc "Model-Based".
    parts = re.split(r':\s*|\s+(?:—|–|-)\s+', rest, maxsplit=1)
    if len(parts) < 2:
        return None

    name = parts[0].strip()
    description = parts[1].strip()

    if not name or not description:
        return None

    # Loại bỏ dấu ngoặc nhọn hoặc ký tự rác quanh name
    name = re.sub(r'^["\'<>\s]+|["\'<>\s]+$', '', name).strip()

    # Đảm bảo description có ít nhất 1 câu và không quá ngắn
    if len(description) < 5:
        return None

    return canonical_type, name, description


def is_illustrative_example(name: str) -> bool:
    """
    Kiểm tra xem tên atom có phải là một ví dụ minh họa chung chung (illustrative example)
    thường dùng trong lý thuyết hệ thống hay không.
    """
    name_lower = name.lower().strip()
    if name_lower in ILLUSTRATIVE_BLACKLIST:
        return True
    for item in ILLUSTRATIVE_BLACKLIST:
        if item in name_lower:
            if len(name_lower.split()) <= 4:
                return True
    return False


def is_duplicate_of_extracted(name: str, extracted_atoms: list[str]) -> bool:
    """
    Kiểm tra xem tên atom có trùng với bất kỳ atom nào đã được trích xuất trong chunk hiện tại không.
    """
    name_normalized = name.lower().strip()
    for atom in extracted_atoms:
        if name_normalized == atom.lower().strip():
            return True
    return False


def check_vault_duplicate(canonical_type: str, name: str) -> bool:
    """
    Kiểm tra xem một atom có tên `name` và loại `canonical_type` đã tồn tại trong Vault hay chưa.
    """
    normalized_name = name.strip().lower().replace(" ", "_").replace("-", "_")

    type_folder = ""
    if canonical_type == "Concept":
        type_folder = "concepts"
    elif canonical_type == "Entity":
        type_folder = "entities"
    elif canonical_type == "Method":
        type_folder = "methods"
    elif canonical_type == "Principle":
        type_folder = "principles"
    elif canonical_type == "Mental Model":
        type_folder = "mental_models"
    elif canonical_type == "Relationship":
        type_folder = "relationships"

    folders_to_scan = []
    if type_folder:
        folders_to_scan.append(os.path.join(ROOT_DIR, "3-resources", "wiki", type_folder))
    folders_to_scan.append(os.path.join(ROOT_DIR, "3-resources", "wiki", "review_queue"))

    for folder in folders_to_scan:
        if not os.path.exists(folder):
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                if not file.endswith(".md"):
                    continue
                file_name_normalized = file.lower().replace(" ", "_").replace("-", "_")[:-3]
                parts = file_name_normalized.split("_")
                if normalized_name == file_name_normalized or normalized_name in parts:
                    return True
    return False


def process_and_validate_gaps(response_text: str, extracted_atoms: list[str]) -> tuple[str | None, list[str]]:
    """
    Xử lý và validate các candidates trả về từ AI.
    Trả về (validated_markdown_text, list_of_ignored_reasons).
    """
    if not response_text:
        return None, ["Response rỗng từ Ollama"]

    lines = response_text.splitlines()
    valid_candidates = []
    ignored_reasons = []

    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            continue

        parsed = parse_gap_line(line_stripped)
        if not parsed:
            if line_stripped.startswith(("-", "*", "+")) or re.match(r'^\d+\.', line_stripped):
                ignored_reasons.append(f"Format không đúng chuẩn: {line_stripped}")
            continue

        canonical_type, name, description = parsed

        # 1. Check ví dụ minh họa chung chung
        if is_illustrative_example(name):
            ignored_reasons.append(f"Bỏ qua ví dụ minh họa chung chung: [{canonical_type}] {name}")
            continue

        # 2. Check trùng với atoms đã được trích xuất ở chunk này
        if is_duplicate_of_extracted(name, extracted_atoms):
            ignored_reasons.append(f"Trùng với atom đã trích xuất ở chunk này: [{canonical_type}] {name}")
            continue

        # 3. Check trùng với atoms đã có sẵn trong Vault
        if check_vault_duplicate(canonical_type, name):
            ignored_reasons.append(f"Đã tồn tại trong Vault: [{canonical_type}] {name}")
            continue

        valid_candidates.append(f"- [{canonical_type}] {name}: {description}")

    if not valid_candidates:
        return None, ignored_reasons

    return "\n".join(valid_candidates), ignored_reasons


def write_gap_candidates(source: str, chunk_num: int, response: str) -> str:
    """
    Ghi kết quả gap-check ra file markdown.
    Trả về đường dẫn file đã ghi.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Tên file: <source>_gap_<chunk_num>.md
    safe_source = os.path.splitext(os.path.basename(source))[0]
    # Loại bỏ ký tự không hợp lệ trong tên file
    safe_source = "".join(c if c.isalnum() or c in "-_" else "_" for c in safe_source)
    filename = f"{safe_source}_gap_{chunk_num:03d}.md"
    output_path = os.path.join(OUTPUT_DIR, filename)

    content = f"""---
source: {source}
chunk: {chunk_num}
date: {datetime.now().strftime('%Y-%m-%d')}
model: {GAP_MODEL}
status: PENDING_REVIEW
audit_stamp: true
audit_timestamp: {datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
---

## Candidates bị bỏ sót

{response}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Gap-check: phát hiện atoms bị bỏ sót sau khi Gemini extract."
    )
    parser.add_argument("--chunk", required=False, help="Path đến file chứa chunk text")
    parser.add_argument("--chunk-text", required=False, help="Chunk text trực tiếp (thay thế --chunk)")
    parser.add_argument("--atoms", required=False, default="[]",
                        help="JSON array tên atoms đã extract, ví dụ: '[\"A\",\"B\"]'")
    parser.add_argument("--source", required=True, help="Tên file nguồn (để đặt tên output)")
    parser.add_argument("--chunk-num", type=int, default=1, help="Số thứ tự chunk (mặc định: 1)")
    parser.add_argument("--skip-gap-check", action="store_true",
                        help="Bypass hoàn toàn, không gọi Ollama")
    args = parser.parse_args()

    # --- Bypass flag ---
    if args.skip_gap_check:
        log.info("--skip-gap-check active. Skipping gap-check.")
        sys.exit(0)

    # --- Đọc chunk text ---
    source_file_path = None
    if args.chunk_text:
        chunk_text = args.chunk_text
    elif args.chunk:
        source_file_path = os.path.normpath(args.chunk)
        if not os.path.exists(source_file_path):
            log.warning(f"Chunk file not found: {source_file_path}. Skipping gap-check.")
            sys.exit(0)
        chunk_text = read_chunk_file(source_file_path)
    else:
        log.warning("Need --chunk or --chunk-text. Skipping gap-check.")
        sys.exit(0)

    # --- YAML Validation Gate (Kernel Bridge Hardening) ---
    is_valid, yaml_error = validate_yaml_gate(chunk_text)
    if not is_valid:
        log.error(f"[BLOCKED] File bị từ chối do YAML không hợp lệ: {source_file_path if source_file_path else 'direct input'}")

        if source_file_path:
            # DLQ Logic: Move file to failed_queue and log error
            os.makedirs(FAILED_DIR, exist_ok=True)
            filename = os.path.basename(source_file_path)
            error_log_path = os.path.join(FAILED_DIR, f"{filename}.error.log")

            with open(error_log_path, "w", encoding="utf-8") as f:
                f.write(f"Timestamp: {datetime.now(timezone.utc).isoformat()}\n")
                f.write(f"File: {source_file_path}\n")
                f.write(f"YAML Error:\n{yaml_error}\n")

            dest_path = os.path.join(FAILED_DIR, filename)
            try:
                shutil.move(source_file_path, dest_path)
                log.error(f"[DLQ] Đã chuyển file lỗi vào failed_queue/: {dest_path}")
            except Exception as move_err:
                log.error(f"Failed to move file to DLQ: {move_err}")

        sys.exit(0) # Non-blocking for the batch process

    # --- Parse atoms list ---
    try:
        atoms = json.loads(args.atoms)
        if not isinstance(atoms, list):
            atoms = []
    except json.JSONDecodeError:
        log.warning(f"--atoms is not valid JSON: {args.atoms!r}. Using empty list.")
        atoms = []

    atom_count = len(atoms)
    atoms_list = "\n".join(f"  - {a}" for a in atoms) if atoms else "  (chưa có atoms nào)"

    # Giới hạn chunk text để tránh prompt quá dài — tăng lên 6000 để bắt được nhiều ngữ cảnh hơn
    chunk_preview = chunk_text[:6000]
    if len(chunk_text) > 6000:
        chunk_preview += "\n... [truncated for context]"

    # --- Xây dựng prompt ---
    prompt = PROMPT_TEMPLATE.format(
        atom_count=atom_count,
        chunk_num=args.chunk_num,
        source=args.source,
        chunk_text=chunk_preview,
        atoms_list=atoms_list,
    )

    # --- Gọi Ollama (non-blocking) ---
    log.info(f"Calling {GAP_MODEL} for gap-check on chunk #{args.chunk_num} ({atom_count} atoms already extracted)...")
    response = call_ollama(prompt)

    if response is None:
        # Ollama offline hoặc lỗi — Ghi vào DLQ
        save_to_failed_queue(
            source=args.source,
            chunk_num=args.chunk_num,
            error_msg="Ollama offline or Connection Timeout",
            atoms_json=args.atoms,
            chunk_path=args.chunk,
            chunk_text=args.chunk_text if not args.chunk else None
        )
        sys.exit(0)

    if response.upper() == "NONE":
        log.info(f"Chunk #{args.chunk_num}: No gap detected. No file created.")
        sys.exit(0)

    # --- Post-process + Ghi output ---
    clean_response, ignored_reasons = process_and_validate_gaps(response, atoms)

    if ignored_reasons:
        for reason in ignored_reasons:
            log.info(f"[Validation Filter] {reason}")

    if not clean_response:
        log.info(f"Chunk #{args.chunk_num}: No valid gap candidates found after strict validation and filtering. No file created.")
        sys.exit(0)

    output_path = write_gap_candidates(args.source, args.chunk_num, clean_response)
    log.info(f"Gap candidates saved: {output_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()

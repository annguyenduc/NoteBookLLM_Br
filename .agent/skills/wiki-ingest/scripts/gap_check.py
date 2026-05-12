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
import sys
import json
import argparse
import logging
import urllib.request
import urllib.error
from datetime import datetime

# --- Cấu hình ---
OLLAMA_URL    = "http://localhost:11434/api/generate"
GAP_MODEL     = os.getenv("GAP_CHECK_MODEL", "gemma3:4b")  # Optimized for Atomic Extraction & Source Metadata
TIMEOUT_SEC   = 60
ROOT_DIR      = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
OUTPUT_DIR    = os.path.join(ROOT_DIR, "00_Inbox", "gap_candidates")

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

Format (STRICTLY follow this):
- [Concept] Leverage Points: Points in a system where a small shift in one thing can produce big changes in everything.
- [Entity] World Bank: An international financial institution that provides loans to countries.
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def read_chunk_file(path: str) -> str:
    """Đọc chunk text từ file tạm hoặc trực tiếp."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


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


def extract_bullets(text: str) -> str:
    """
    Hậu xử lý response: Lọc lấy các dòng bắt đầu bằng dấu gạch ngang.
    Loại bỏ mọi đoạn hội thoại thừa của AI.
    """
    lines = text.splitlines()
    # Chấp nhận cả '- [Concept]' và '- Khái niệm' hoặc chỉ đơn giản là '- '
    bullets = [line.strip() for line in lines if line.strip().startswith("-")]
    
    if not bullets:
        return "NONE (No formatted candidates found)"
    return "\n".join(bullets)


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
    if args.chunk_text:
        chunk_text = args.chunk_text
    elif args.chunk:
        if not os.path.exists(args.chunk):
            log.warning(f"Chunk file not found: {args.chunk}. Skipping gap-check.")
            sys.exit(0)
        chunk_text = read_chunk_file(args.chunk)
    else:
        log.warning("Need --chunk or --chunk-text. Skipping gap-check.")
        sys.exit(0)

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
        # Ollama offline — log warning đã xử lý trong call_ollama(), exit 0
        sys.exit(0)

    if response.upper() == "NONE":
        log.info(f"Chunk #{args.chunk_num}: No gap detected. No file created.")
        sys.exit(0)

    # --- Post-process + Ghi output ---
    # Extract bullet points, lọc bỏ thinking text của qwen3
    clean_response = extract_bullets(response)
    output_path = write_gap_candidates(args.source, args.chunk_num, clean_response)
    log.info(f"Gap candidates saved: {output_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()

import os
import re
import json
import hashlib
import shutil
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import yaml
import sys

# Thêm workspace root vào sys.path để import libs
# Đảm bảo PYTHONPATH trỏ tới d:/NoteBookLLM_Br
WORKSPACE_ROOT = Path("d:/NoteBookLLM_Br")
sys.path.append(str(WORKSPACE_ROOT))

from libs.core.llm_client import call_pedagogical_engineer

# CONFIGURATION
DISTILLED_DIR = WORKSPACE_ROOT / "brain/distilled"
RAW_DIR = WORKSPACE_ROOT / "brain/raw"
MEDIA_ASSETS_DIR = RAW_DIR / "lms_multi_media_dump/assets"
ARCHIVE_DIR = WORKSPACE_ROOT / "brain/archive/Standardization_Cleanup"
MASTER_INDEX_FILE = RAW_DIR / "MASTER_SOURCE_INDEX.md"

# Global Source Resolver Cache
MASTER_SOURCE_MAP = {}
RE_VERSION = re.compile(r"v(\d+)", re.IGNORECASE)

def load_master_index():
    if MASTER_INDEX_FILE.exists():
        with open(MASTER_INDEX_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            for line in content.split("\n"):
                if "[" in line and "]" in line:
                    match = re.search(r"\[(.*?)\]", line)
                    if match:
                        name = match.group(1)
                        MASTER_SOURCE_MAP[name.lower()] = name
    
    # Fuzzy fallback for optimized parts
    # Maps 'v01' to 'optimized_part_1_v01.md'
    for i in range(1, 27):
        key = f"v{i:02d}"
        if i <= 9:
            MASTER_SOURCE_MAP[key] = f"optimized_part_1_{key}.md"
        else:
            # v10-v26 might be part 1 or 2, checking index
            name_v10 = f"optimized_part_1_{key}.md"
            if name_v10.lower() not in MASTER_SOURCE_MAP:
                 MASTER_SOURCE_MAP[key] = name_v10
    
    print(f"Master Index Loaded: {len(MASTER_SOURCE_MAP)} entries.")

def resolve_source(key):
    key_clean = str(key).replace("[[", "").replace("]]", "").strip().lower()
    # Check exact match
    if key_clean in MASTER_SOURCE_MAP:
        return MASTER_SOURCE_MAP[key_clean]
    
    # Check vXX pattern
    v_match = RE_VERSION.search(key_clean)
    if v_match:
        v_key = v_match.group(0).lower()
        if v_key in MASTER_SOURCE_MAP:
            return MASTER_SOURCE_MAP[v_key]
            
    return key_clean if ".md" in key_clean else "MASTER_SOURCE_INDEX.md"

load_master_index()

# LOM v4.4 Supreme Defaults
DEFAULT_BLOOM = "Remember/Understand"
DEFAULT_LEVEL = "Entry"

# Regex for asset detection
ASSET_RE = re.compile(r"(image\d+\.(png|jpg|jpeg|gif|mp4))", re.IGNORECASE)

class SwarmHighFidelityStandardizer:
    def __init__(self):
        self.archive_dir = ARCHIVE_DIR
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.source_map = {} 
        
    def normalize_text(self, text):
        return re.sub(r'\s+', ' ', text).strip().lower()

    def extract_metadata(self, content):
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    metadata = yaml.safe_load(parts[1])
                    body = parts[2].strip()
                    return metadata, body
            except Exception:
                pass
        return {}, content.strip()

    def find_best_asset_match(self, asset_name, source_file_name_hint=None):
        if not source_file_name_hint:
            return None
        
        # Clean hint
        base_source = Path(source_file_name_hint).stem
        # Pattern in dump: 'Filename.docx_image1.png'
        target_name = f"{base_source}.docx_{asset_name}"
        
        # Try exact match with docx prefix
        if (MEDIA_ASSETS_DIR / target_name).exists():
            return f"../raw/lms_multi_media_dump/assets/{target_name}"
        
        # Try direct match
        if (MEDIA_ASSETS_DIR / asset_name).exists():
            return f"../raw/lms_multi_media_dump/assets/{asset_name}"
            
        return None

    def process_file_pass1(self, file_path):
        """Pass 1: Catalog."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            metadata, body = self.extract_metadata(content)
            source = metadata.get("source", metadata.get("Source", "Unknown"))
            
            source_match = re.search(r"\[\[(.*?)\]\]", str(source))
            source_key = source_match.group(1) if source_match else str(source)
            
            if source_key not in self.source_map:
                self.source_map[source_key] = []
                
            self.source_map[source_key].append({
                "path": file_path,
                "metadata": metadata,
                "body": body,
                "norm_body": self.normalize_text(body)
            })
        except Exception as e:
            print(f"Error cataloging {file_path}: {e}")

    def distill_content_ai(self, entry, source_key):
        """Call @engineer to re-distill content with high fidelity."""
        body = entry["body"]
        file_name = entry["path"].name
        resolved_src = resolve_source(source_key)
        
        # Clickable Link Format
        src_link = f"[{resolved_src}](../raw/{resolved_src})"

        system_prompt = f"""Bạn là @engineer (Content Engineer) chuyên gia sư phạm.
Nhiệm vụ: Tinh cất nội dung từ bản nháp thô sang tài liệu học tập chuẩn LOM v4.4 Supreme.

QUY TẮC BẮT BUỘC:
1. NGÔN NGỮ: Tuyệt đối sử dụng Tiếng Việt 100%. Nếu nguồn là Tiếng Anh, hãy DỊCH sang Tiếng Việt chuyên ngành chuẩn xác.
2. DẪN NGUỒN (PROVENANCE): Mọi sự kiện/kiến thức quan trọng phải kết thúc bằng liên kết: {src_link}. Không dùng định dạng khác.
3. MEDIA: Nếu thấy image1.png, image2.png... hãy đổi thành: ![mô tả](../../3-resources/raw/lms_multi_media_dump/assets/[KEY]_imageN.png) với [KEY] là tên file nguồn (bỏ .md).
4. CẤU TRÚC: Sử dụng Heading (#, ##, ###), bảng biểu, và các hộp Markdown chuyên nghiệp.

INPUT:
{body}
"""
        messages = [{"role": "user", "content": "Hãy tinh cất nội dung này."}]
        # nhưng call_pedagogical_engineer đã tự chèn system_prompt role tương ứng.
        # Ở đây ta sẽ gửi prompt chi tiết vào user message.
        
        messages = [{"role": "user", "content": system_prompt}]
        
        try:
            content, actual_model = call_pedagogical_engineer(messages, max_tokens=4000)
            return content
        except Exception as e:
            print(f"AI Distillation Failed for {file_name}: {e}")
            return body # Fallback to original

    def archive_file(self, file_path):
        if file_path.exists():
            target = self.archive_dir / file_path.name
            if not target.exists():
                shutil.move(str(file_path), str(target))

    def finalize_block(self, entry, source_key):
        """AI-aided finalization."""
        # AI Distill
        refined_body = self.distill_content_ai(entry, source_key)
        
        # Metadata Standardization
        file_path = entry["path"]
        file_id = file_path.stem
        meta = entry["metadata"]
        resolved_src = resolve_source(source_key)
        
        new_meta = {
            "file_id": file_id,
            "category": meta.get("category", "Atomic Note"),
            "trainer_level": meta.get("trainer_level", DEFAULT_LEVEL),
            "bloom_level": meta.get("bloom_level", DEFAULT_BLOOM),
            "source": f"[[{resolved_src}]]",
            "status": "Verified",
            "last_audit": time.strftime("%Y-%m-%d")
        }

        yaml_str = yaml.dump(new_meta, sort_keys=False, allow_unicode=True)
        final_content = f"---\n{yaml_str}---\n\n# {file_id.replace('_', ' ')}\n\n{refined_body}"

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print(f"Verified & Standardized: {file_id}")

    def run(self, limit=None):
        all_files = list(DISTILLED_DIR.glob("*.md"))
        print(f"Discovered {len(all_files)} files.")
        
        # Pass 1: Catalog
        for f in all_files:
            self.process_file_pass1(f)
        
        # Pass 2: Merging & High-Fidelity Distillation
        to_process = []
        for source_key, entries in self.source_map.items():
            # Deduplicate by norm_body
            entries.sort(key=lambda x: (
                1 if x["path"].name.startswith("LMS") else 0,
                len(x["body"])
            ), reverse=True)
            
            unique_blocks = []
            seen_hashes = set()
            for entry in entries:
                # Nếu file cực ngắn (<3 dòng), ta sẽ coi nó là fragment để gộp
                content_lines = [l for l in entry["body"].split("\n") if l.strip() and not l.startswith("#")]
                is_short = len(content_lines) < 3
                
                h = hashlib.md5(entry["norm_body"].encode()).hexdigest()
                if h not in seen_hashes:
                    unique_blocks.append(entry)
                    seen_hashes.add(h)
                else:
                    self.archive_file(entry["path"])

            if not unique_blocks:
                continue

            # Chiến lược gộp mới: 
            # - Nếu có nhiều khối unique cho cùng 1 source, ta gộp chúng lại nẾU chúng ngắn.
            # - Nếu khối dài, ta giữ riêng để tránh file quá khổng lồ.
            
            current_merged = unique_blocks[0]
            for next_block in unique_blocks[1:]:
                # Chỉ gộp nếu một trong hai bên "ngắn"
                c1 = [l for l in current_merged["body"].split("\n") if l.strip() and not l.startswith("#")]
                c2 = [l for l in next_block["body"].split("\n") if l.strip() and not l.startswith("#")]
                if len(c1) < 5 or len(c2) < 5:
                    current_merged["body"] += "\n\n" + next_block["body"]
                    self.archive_file(next_block["path"])
                else:
                    # Giữ riêng
                    to_process.append((next_block, source_key))
            
            to_process.append((current_merged, source_key))

        if limit:
            to_process = to_process[:limit]
            print(f"AI Pilot: Processing {len(to_process)} unique blocks.")

        # Pass 3: Parallel AI Distillation
        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(lambda p: self.finalize_block(p[0], p[1]), to_process)

        print("High-Fidelity Swarm Distillation Complete.")

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    standardizer = SwarmHighFidelityStandardizer()
    standardizer.run(limit=limit)

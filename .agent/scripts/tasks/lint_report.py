# -*- coding: utf-8 -*-
import os
import sys
import hashlib
import json
import re
from pathlib import Path

# Thêm project root
REPO_ROOT = Path("D:/NoteBookLLM_Br")
sys.path.append(str(REPO_ROOT))

# Định nghĩa các thư mục tài nguyên và cache
WIKI_DIR = REPO_ROOT / "3-resources" / "wiki"
SCAN_FOLDERS = ["concepts", "entities", "sources", "synthesis", "comparisons"]
CACHE_PATH = REPO_ROOT / "scripts" / "maintenance" / "process" / "storage" / "cache" / "brain_lint_manifest.json"

def get_wiki_files():
    """Lấy danh sách tất cả các file markdown trong các thư mục wiki chính."""
    files = []
    for folder in SCAN_FOLDERS:
        folder_path = WIKI_DIR / folder
        if folder_path.exists():
            files.extend(list(folder_path.glob("*.md")))
    return sorted(files, key=lambda path: path.name.lower())

def read_file_content(path):
    return path.read_text(encoding="utf-8")

def file_sha256(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()

def check_broken_links(content, all_filenames):
    """Tìm tất cả các liên kết wikilink hỏng."""
    links = re.findall(r"\[\[(.*?)\]\]", content)
    broken = []
    for link in links:
        link_name = link.split("|")[0].strip()
        # Kiểm tra xem link_name có tồn tại trong danh sách file (name hoặc stem) không
        if link_name not in all_filenames:
            broken.append(link_name)
    return broken

def load_cache():
    """Load thông tin cache đã lưu."""
    if not CACHE_PATH.exists():
        return {"files": {}}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"files": {}}

def main():
    print("--- 🩺 ĐANG CHẠY DRY-RUN WIKI LINT & BROKEN LINKS ---")
    
    files = [path for path in get_wiki_files() if not path.name.startswith("_")]
    # Hỗ trợ cả file name, file stem và các system stems để đối chiếu wikilinks
    all_filenames = set()
    for f in files:
        all_filenames.add(f.name)
        all_filenames.add(f.stem)
    all_filenames.update(["log", "index", "overview", "WIKI_INDEX"])
    
    cache = load_cache()
    cache_files = cache.get("files", {})
    
    stale_files = []
    broken_links_report = {}
    
    for file_path in files:
        try:
            content = read_file_content(file_path)
            file_hash = file_sha256(content)
            
            # So sánh hash với cache để xem file có bị thay đổi không
            cache_entry = cache_files.get(file_path.name)
            if not cache_entry or cache_entry.get("sha256") != file_hash:
                stale_files.append(file_path.name)
                
            # Kiểm tra liên kết hỏng
            broken = check_broken_links(content, all_filenames)
            if broken:
                broken_links_report[file_path.name] = broken
        except Exception as e:
            print(f"[!] Lỗi đọc file {file_path.name}: {e}")
            
    print(f"Tổng số file Wiki đã quét: {len(files)}")
    print(f"Số file bị thay đổi (cần Lint lại): {len(stale_files)}")
    if stale_files:
        print("Danh sách các file thay đổi:")
        for sf in stale_files[:10]:
            print(f"  - {sf}")
        if len(stale_files) > 10:
            print(f"  - ... và {len(stale_files) - 10} file khác.")
            
    print(f"\nSố file phát hiện liên kết hỏng (Broken Links): {len(broken_links_report)}")
    if broken_links_report:
        print("Chi tiết liên kết hỏng:")
        for fname, blinks in broken_links_report.items():
            print(f"  - {fname}: {', '.join(blinks)}")
            
    # Output contract
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"lint_report.py\"")
    print("  command: \"python scripts/tasks/lint_report.py --dry-run\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"PASS\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NONE\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"Quet {len(files)} files, phat hien {len(stale_files)} files stale va {len(broken_links_report)} files co broken links\"")

if __name__ == "__main__":
    main()

import os
import re
import sqlite3
import argparse
import sys
from datetime import datetime

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

ROOT_DIR = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")

WIKI_LINK_RE = re.compile(r"\[\[(.*?)\]\]")

def get_existing_file_ids():
    """Lấy danh sách tất cả các file_id hiện có từ Database."""
    ids = set()
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        rows = cursor.execute("SELECT file_id FROM atoms").fetchall()
        for r in rows:
            if r[0]:
                ids.add(r[0].lower())
        conn.close()
    except Exception as e:
        print(f"Error reading DB: {e}")
    return ids

def scan_broken_links():
    """Quét các file markdown để tìm các liên kết chưa có tệp tin tương ứng."""
    existing_ids = get_existing_file_ids()
    gaps = {} # {term: count}
    
    scan_folders = ["concepts", "entities", "sources", "synthesis"]
    for folder in scan_folders:
        folder_path = os.path.join(WIKI_DIR, folder)
        if not os.path.exists(folder_path): continue
        
        for file in os.listdir(folder_path):
            if not file.endswith(".md"): continue
            
            file_path = os.path.join(folder_path, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    matches = WIKI_LINK_RE.findall(content)
                    for match in matches:
                        term = match.split("|")[0].strip()
                        if term.lower() not in existing_ids:
                            gaps[term] = gaps.get(term, 0) + 1
            except:
                pass
    return gaps

def create_stub(term):
    """Tạo một file CONCEPT stub cho thuật ngữ chưa có."""
    file_id = f"CONCEPT_{term.replace(' ', '_')}"
    file_path = os.path.join(WIKI_DIR, "concepts", f"{file_id}.md")
    
    if os.path.exists(file_path):
        return False
        
    template = f"""---
file_id: {file_id}
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@scout"
status: "STUB"
confidence: 0.10
---

# {term}

> [!NOTE]
> Đây là trang tri thức tạm thời (STUB) được tạo tự động vì có nhiều liên kết trỏ đến thuật ngữ này.

## Core Principle
Chưa có định nghĩa chính thức. Cần được bổ sung từ nguồn RAW.

## 4F Reflection
- **Facts**: Được phát hiện qua phân tích lỗ hổng tri thức (Breakdown).
- **Feelings**: 
- **Findings**: 
- **Futures**: 
"""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template)
            
        # Add to DB
        conn = sqlite3.connect(DB_PATH)
        conn.execute("INSERT OR IGNORE INTO atoms (file_id, title, type, status, confidence) VALUES (?, ?, ?, ?, ?)",
                    (file_id, term, "Concept", "STUB", 0.10))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error creating stub for {term}: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wiki Breakdown / Noun Miner")
    parser.add_argument("--source", choices=["broken-links"], default="broken-links")
    parser.add_argument("--create-stubs", action="store_true", help="Create .md files for common gaps")
    parser.add_argument("--min-occurrence", type=int, default=2, help="Minimum mentions to create stub")
    args = parser.parse_args()

    print(f"Starting wiki-breakdown scan (min={args.min_occurrence}) at {datetime.now()}...")
    gaps = scan_broken_links()
    
    sorted_gaps = sorted(gaps.items(), key=lambda x: x[1], reverse=True)
    
    created_count = 0
    for term, count in sorted_gaps:
        if count >= args.min_occurrence:
            print(f"  - {term} ({count} mentions)")
            if args.create_stubs:
                if create_stub(term):
                    created_count += 1
                    print(f"    [STUB CREATED]")
        
    print(f"\nScan completed. Found {len(gaps)} gaps. Created {created_count} stubs.")

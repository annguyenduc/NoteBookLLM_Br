# -*- coding: utf-8 -*-
"""
Asset Sync & Standardize v1.1 - NoteBookLLM_Br
Di chuyển và đổi tên các Asset hình ảnh (ASCII only in logs).
"""

import os
import sys
import re
from pathlib import Path

# Đảm bảo UTF-8 cho stdout trên Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAW_ASSETS_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\raw\assets")
WIKI_ASSETS_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki\assets")
WIKI_CONCEPTS_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki\concepts")

def main():
    # 1. Danh sách các file cần xử lý
    mapping = {} # Old name -> New name
    
    asset_files = list(RAW_ASSETS_DIR.glob("WIKI_IMG_THINK_*.png"))
    
    print(f"Standardizing {len(asset_files)} assets...")
    
    for src_path in asset_files:
        old_name = src_path.name
        new_name = old_name.replace("WIKI_IMG_", "")
        dest_path = WIKI_ASSETS_DIR / new_name
        
        try:
            # Di chuyển và đổi tên
            if src_path.exists():
                src_path.replace(dest_path)
                mapping[old_name] = new_name
                print(f"  [MOVED] {old_name} -> {new_name}")
        except Exception as e:
            print(f"  [ERROR] Move {old_name}: {e}")

    # 2. Cập nhật link trong Markdown
    md_files = list(WIKI_CONCEPTS_DIR.glob("*.md"))
    updated_md_count = 0
    
    for md_path in md_files:
        try:
            content = md_path.read_text(encoding="utf-8")
            new_content = content
            
            for old_n, new_n in mapping.items():
                new_content = new_content.replace(old_n, new_n)
            
            if new_content != content:
                md_path.write_text(new_content, encoding="utf-8")
                updated_md_count += 1
                print(f"  [UPDATED LINK] {md_path.name}")
        except Exception as e:
            print(f"  [ERROR] Update {md_path.name}: {e}")

    print(f"\n[DONE] Processed {len(mapping)} assets and updated {updated_md_count} files.")

if __name__ == "__main__":
    main()

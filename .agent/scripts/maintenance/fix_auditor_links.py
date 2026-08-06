# -*- coding: utf-8 -*-
"""
Auditor Link Fixer v1.0 - NoteBookLLM_Br
Cập nhật đường dẫn raw trong các comment [AUDITOR] Rule 14.
"""

import os
import sys
import re
from pathlib import Path

# Đảm bảo UTF-8 cho stdout
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")

# Tìm các đường dẫn raw cũ: 3-resources/raw/FILENAME.md
# Thay bằng: 3-resources/raw/sources/FILENAME.md
# Lưu ý: Không thay nếu đã có /sources/ hoặc /assets/
RAW_PATH_RE = re.compile(r'3-resources/raw/(?!sources/|assets/)([^`\s,]+)')

def fix_auditor_line(content):
    # Thay thế đường dẫn file .md thành /sources/
    # Thay thế đường dẫn file .png/.jpg/.gif thành /assets/
    
    def replacer(match):
        filename = match.group(1)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            return f"3-resources/raw/assets/{filename}"
        else:
            return f"3-resources/raw/sources/{filename}"

    return RAW_PATH_RE.sub(replacer, content)

def main():
    print("🛠️ Đang cập nhật tọa độ Auditor trong Wiki...")
    
    files = list(WIKI_DIR.rglob("*.md"))
    updated_count = 0
    
    for fpath in files:
        try:
            content = fpath.read_text(encoding="utf-8")
            new_text = fix_auditor_line(content)
            
            if new_text != content:
                fpath.write_text(new_text, encoding="utf-8")
                updated_count += 1
                print(f"  [UPDATED] {fpath.name}")
        except Exception as e:
            print(f"  [ERROR] {fpath.name}: {e}")

    print(f"\n✅ HOÀN TẤT! Đã cập nhật {updated_count} file.")

if __name__ == "__main__":
    main()

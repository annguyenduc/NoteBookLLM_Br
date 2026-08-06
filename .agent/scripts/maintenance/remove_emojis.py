# -*- coding: utf-8 -*-
"""
De-Emoji v1.0 - NoteBookLLM_Br
Gỡ bỏ toàn bộ Emoji và biểu tượng trang trí để tối ưu hóa độ ổn định encoding.
"""

import os
import sys
import re
from pathlib import Path

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")

# Regex tìm các ký tự Emoji và biểu tượng đặc biệt (Unicode ranges cho Emoji)
# Range này bao gồm hầu hết các biểu tượng mặt cười, phương tiện, biểu tượng kỹ thuật...
EMOJI_RE = re.compile(
    r'[\U00010000-\U0010ffff]' # Emojis (4-byte)
    r'|[\u2600-\u26FF]'        # Miscellaneous Symbols
    r'|[\u2700-\u27BF]'        # Dingbats
    r'|[\u2300-\u23FF]'        # Miscellaneous Technical
    r'|[\u2B50]'               # Star
    r'|[\u2190-\u21FF]'        # Arrows (Keep if technical, but user asked for simple)
)

def clean_content(text):
    # 1. Xóa Emojis
    text = EMOJI_RE.sub('', text)
    
    # 2. Chuẩn hóa các label hệ thống
    text = text.replace('Nguồn:', 'Nguồn:') # Nếu đã có
    text = re.sub(r'\n\s*📖\s*Nguồn:', '\nNguồn:', text) # Thay thế icon sách
    text = re.sub(r'#\s*⚙️', '#', text) # Thay thế icon bánh răng trong tiêu đề
    
    # 3. Dọn dẹp khoảng trắng thừa do xóa icon sinh ra
    text = re.sub(r'#\s+', '# ', text)
    
    return text

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🧹 Bắt đầu quy trình làm sạch biểu tượng (De-Emoji)...")
    
    files = list(WIKI_DIR.rglob("*.md"))
    changed_count = 0
    
    for fpath in files:
        try:
            content = fpath.read_text(encoding="utf-8")
            new_text = clean_content(content)
            
            if new_text != content:
                fpath.write_text(new_text, encoding="utf-8")
                changed_count += 1
                print(f"  [CLEANED] {fpath.name}")
        except Exception as e:
            print(f"  [ERROR] {fpath.name}: {e}")

    print(f"\n✅ HOÀN TẤT! Đã làm sạch {changed_count} file.")

if __name__ == "__main__":
    main()

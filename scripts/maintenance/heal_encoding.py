# -*- coding: utf-8 -*-
"""
Heal Encoding v7.0 - NoteBookLLM_Br
Surgical healing using sliding window buffer analysis to handle partial Mojibake.
"""

import os
import sys
from pathlib import Path

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")

CP1252_MAP = {
    '\u20ac': 0x80, '\u201a': 0x82, '\u0192': 0x83, '\u201e': 0x84, '\u2026': 0x85,
    '\u2020': 0x86, '\u2021': 0x87, '\u02c6': 0x88, '\u2030': 0x89, '\u0160': 0x8a,
    '\u2039': 0x8b, '\u0152': 0x8c, '\u017d': 0x8e, '\u2018': 0x91, '\u2019': 0x92,
    '\u201c': 0x93, '\u201d': 0x94, '\u2022': 0x95, '\u2013': 0x96, '\u2014': 0x97,
    '\u02dc': 0x98, '\u2122': 0x99, '\u0161': 0x9a, '\u203a': 0x9b, '\u0153': 0x9c,
    '\u017e': 0x9e, '\u0178': 0x9f
}

def fix_buffer(buffer):
    res = []
    while buffer:
        found = False
        # Thử các độ dài từ 4 xuống 2 (UTF-8 Việt Nam thường 2-3 bytes)
        for length in range(min(len(buffer), 4), 1, -1):
            sub = buffer[:length]
            try:
                b_sub = bytes([CP1252_MAP.get(c, ord(c)) for c in sub])
                fixed = b_sub.decode('utf-8')
                res.append(fixed)
                buffer = buffer[length:]
                found = True
                break
            except:
                continue
        if not found:
            res.append(buffer[0])
            buffer = buffer[1:]
    return "".join(res)

def fix_text_robust(text):
    output = []
    buffer = []
    for char in text:
        code = ord(char)
        if 0x80 <= code <= 0xFF or char in CP1252_MAP:
            buffer.append(char)
        else:
            if buffer:
                output.append(fix_buffer(buffer))
                buffer = []
            output.append(char)
    if buffer:
        output.append(fix_buffer(buffer))
    return "".join(output)

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🚀 Bắt đầu quy trình Hàn gắn tri thức v7.0 (Sliding Window Heal)...")
    
    files = list(WIKI_DIR.rglob("*.md"))
    fixed_count = 0
    
    for fpath in files:
        try:
            content = fpath.read_text(encoding="utf-8", errors="replace")
            new_text = fix_text_robust(content)
            # Không cần loop nhiều lần vì Sliding Window đã xử lý triệt để
            
            if new_text != content:
                fpath.write_text(new_text, encoding="utf-8")
                fixed_count += 1
                print(f"  [FIXED] {fpath.name}")
        except Exception as e:
            print(f"  [ERROR] {fpath.name}: {e}")

    print(f"\n✅ HOÀN TẤT! Đã sửa {fixed_count} file.")

if __name__ == "__main__":
    main()

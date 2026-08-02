# -*- coding: utf-8 -*-
"""
Full System Clean v1.0 - NoteBookLLM_Br
Làm sạch Emoji khỏi các file hướng dẫn hệ thống (CLAUDE.md, AGENTS.md, task_plan.md).
"""

import os
import sys
import re
from pathlib import Path

ROOT_DIR = Path(r"d:\NoteBookLLM_Br")
SYSTEM_FILES = ["CLAUDE.md", "AGENTS.md", "task_plan.md", "CONTINUITY.md", "3-resources/WIKI_AGENT_GUIDE.md"]

EMOJI_RE = re.compile(r'[\U00010000-\U0010ffff]|[\u2600-\u27BF]|[\u2300-\u23FF]')

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    print("🧹 Bắt đầu làm sạch hệ thống file CORE...")
    
    for rel_path in SYSTEM_FILES:
        fpath = ROOT_DIR / rel_path
        if not fpath.exists(): continue
        
        try:
            content = fpath.read_text(encoding="utf-8")
            # Xóa Emoji
            new_text = EMOJI_RE.sub('', content)
            
            # Fix các text markers đặc biệt
            new_text = new_text.replace('✅', '[DONE]')
            new_text = new_text.replace('🔴', '[TODO]')
            new_text = new_text.replace('⚠️', '[IMPORTANT]')
            new_text = new_text.replace('📐', '[RULE]')
            new_text = new_text.replace('📏', '[STD]')
            new_text = new_text.replace('🐍', '[PY]')
            new_text = new_text.replace('📐', '[SQL]')
            
            if new_text != content:
                fpath.write_text(new_text, encoding="utf-8")
                print(f"  [CLEANED] {rel_path}")
        except Exception as e:
            print(f"  [ERROR] {rel_path}: {e}")

if __name__ == "__main__":
    main()

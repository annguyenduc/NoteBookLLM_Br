# -*- coding: utf-8 -*-
"""
Brain Lint v2.2 - NoteBookLLM_Br
Kiểm tra sức khỏe Wiki: Orphan pages, Broken wikilinks và Encoding integrity (No Emojis).
"""

import re
import sys
import os
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT_DIR = Path(
    os.getenv(
        "NOTEBOOKLLM_ROOT",
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
    )
)
WIKI_DIR = ROOT_DIR / "3-resources" / "wiki"
SYSTEM_STEMS = {"log", "index", "overview", "WIKI_INDEX"}

def _read_safe(file_path: Path) -> tuple[str | None, str | None]:
    try:
        return file_path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError:
        return None, "Encoding error (Not UTF-8)"

# Regex phát hiện Mojibake (giữ lại để cảnh báo sớm)
MOJIBAKE_RE = re.compile(
    chr(195) + r'[\u0082\u008a\u0094\u009b]' + '|' +
    chr(225) + chr(186) + r'[\u00a9\u00ae\u00af]' + '|' +
    chr(225) + chr(187) + r'[\u0099\u009a]' + '|' +
    chr(196) + chr(8216)
)

def lint():
    if not WIKI_DIR.exists():
        print(f"Error: {WIKI_DIR} not found.")
        return

    all_files = list(WIKI_DIR.rglob("*.md"))
    target_files = {f.stem: f for f in all_files if f.stem not in SYSTEM_STEMS}
    inbound = {stem: 0 for stem in target_files}
    broken = []
    errors = []

    for fpath in all_files:
        content, err = _read_safe(fpath)
        if err:
            errors.append((fpath.name, err))
            continue
            
        m = MOJIBAKE_RE.search(content)
        if m:
            errors.append((fpath.name, f"Mojibake detected: {m.group(0)!r}"))

        links = re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]', content)
        for link in links:
            link_stem = link.strip()
            if link_stem in target_files:
                inbound[link_stem] += 1
            elif link_stem not in SYSTEM_STEMS:
                broken.append((fpath.name, link_stem))

    print("\n" + "="*50)
    print("  BRAIN LINT REPORT v2.2 (ASCII Edition)")
    print("="*50)
    
    print(f"\n[1/3] ORPHAN PAGES")
    orphans = [s for s, count in inbound.items() if count == 0]
    if not orphans: print("  [OK] None")
    else:
        for s in sorted(orphans): print(f"  - {s}")
        
    print(f"\n[2/3] BROKEN LINKS")
    if not broken: print("  [OK] None")
    else:
        for src, dest in sorted(set(broken)): print(f"  - {src} -> {dest}")
        
    print(f"\n[3/3] ENCODING ERRORS")
    if not errors: print("  [OK] None")
    else:
        for f, msg in errors: print(f"  [ERROR] {f}: {msg}")

    print("\n" + "="*50)
    print(f"  Status: {'OK' if not (broken or errors) else 'NEEDS ATTENTION'}")
    print("="*50)

if __name__ == "__main__":
    lint()

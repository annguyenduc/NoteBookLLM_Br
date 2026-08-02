# -*- coding: utf-8 -*-
"""
Pressure Chain v1.0 - NoteBookLLM_Br
Audit tính tuân thủ các quy tắc lõi:
- Rule 20: Preamble '## For future Claude'
- Rule 17: Double Examples (Original + Pedagogical)
- Rule 14: Source Tracing (Evidence)
"""

import re
import sys
import os
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")
CONCEPTS_DIR = WIKI_DIR / "concepts"
LOG_FILE = WIKI_DIR / "log.md"

def _read_safe(file_path: Path) -> str:
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception:
        return ""

def audit():
    if not CONCEPTS_DIR.exists():
        print(f"Error: {CONCEPTS_DIR} not found.")
        return

    files = list(CONCEPTS_DIR.glob("*.md"))
    report = []
    
    total = len(files)
    r20_fail = []
    r17_fail = []
    r14_fail = []
    stubs = []

    for fpath in files:
        content = _read_safe(fpath)
        if not content: continue

        # Rule 20 Check (Preamble)
        if not re.search(r"##\s*For\s*future\s*Claude", content, re.I):
            r20_fail.append(fpath.name)

        # Rule 17 Check (Double Examples)
        # Tìm các section liên quan đến Ví dụ hoặc Rule 17
        if not re.search(r"(Ví\s*dụ\s*đối\s*chiếu|Rule\s*17)", content, re.I):
            r17_fail.append(fpath.name)

        # Rule 14 Check (Source Tracing)
        if not re.search(r"(Source\s*Tracing|Nguồn:)", content, re.I):
            r14_fail.append(fpath.name)
            
        # Stub check
        if "status: \"stub\"" in content or "status: 'stub'" in content:
            stubs.append(fpath.name)

    # Print Summary to Terminal
    print("\n" + "="*50)
    print("  WIKI PRESSURE CHAIN REPORT v1.0")
    print("="*50)
    print(f"Tổng số Concept checked: {total}")
    print(f"- Thiếu Rule 20 (Preamble): {len(r20_fail)}")
    print(f"- Thiếu Rule 17 (Examples): {len(r17_fail)}")
    print(f"- Thiếu Rule 14 (Tracing):  {len(r14_fail)}")
    print(f"- Số lượng Stubs:           {len(stubs)}")
    print("="*50)

    # Chi tiết 10 file tệ nhất (fail nhiều rule nhất)
    all_fails = {}
    for f in r20_fail: all_fails[f] = all_fails.get(f, 0) + 1
    for f in r17_fail: all_fails[f] = all_fails.get(f, 0) + 1
    for f in r14_fail: all_fails[f] = all_fails.get(f, 0) + 1
    
    sorted_fails = sorted(all_fails.items(), key=lambda x: x[1], reverse=True)
    
    print("\n[TOP GAPS - CẦN ƯU TIÊN HEALING]")
    for f, count in sorted_fails[:15]:
        status = " (STUB)" if f in stubs else ""
        print(f"  - {f}: Fail {count} rules{status}")

    # Append to Wiki Log
    import datetime
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = f"\n## [{now}] AUDIT | @auditor | Pressure Chain Report\n"
    log_entry += f"- **Stats:** Total: {total} | R20 Fail: {len(r20_fail)} | R17 Fail: {len(r17_fail)} | R14 Fail: {len(r14_fail)}\n"
    log_entry += f"- **Status:** {total - len(all_fails)}/{total} nodes compliant.\n"
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

if __name__ == "__main__":
    audit()

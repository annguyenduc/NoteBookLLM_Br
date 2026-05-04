import os
import sys
from pathlib import Path

# Đảm bảo in được tiếng Việt
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

RAW_LMS_ROOT = Path(r"D:\NoteBookLLM_Br\brain\raw\Tổng hợp đề kiểm tra LMS")
RAW_OUTPUT_DIR = Path(r"d:\NoteBookLLM_Br\brain\raw")
WIKI_DIR = Path(r"d:\NoteBookLLM_Br\brain\wiki")

def final_audit():
    all_docx = list(RAW_LMS_ROOT.rglob("*.docx"))
    
    cited_sources = set()
    import re
    
    for wf in WIKI_DIR.glob("*.md"):
        try:
            with open(wf, "r", encoding="utf-8") as f:
                match = re.search(r'source:\s*"\[\[(.*?)\]\]"', f.read())
                if match: cited_sources.add(match.group(1))
        except: pass

    for rf in RAW_OUTPUT_DIR.glob("EXAM_*.md"):
        try:
            with open(rf, "r", encoding="utf-8") as f:
                match = re.search(r'source:\s*"\[\[(.*?)\]\]"', f.read())
                if match: cited_sources.add(match.group(1))
        except: pass

    missing = []
    found_count = 0
    raw_md_files = [f.name for f in RAW_OUTPUT_DIR.glob("*.md")]

    for doc in all_docx:
        if doc.name in cited_sources:
            found_count += 1
            continue
        
        matched = False
        # Check if there is a raw .md file that contains the name
        for md_name in raw_md_files:
            if doc.stem[:20].lower() in md_name.lower():
                matched = True
                break
        
        if matched:
            found_count += 1
        else:
            missing.append(doc)

    print(f"--- FINAL AUDIT RESULT ---")
    print(f"Total .docx files: {len(all_docx)}")
    print(f"Fully converted/cited: {found_count}")
    print(f"Missing conversion: {len(missing)}")
    
    if missing:
        print("\n[MISSING FILES]:")
        for m in missing:
            print(f"- {m.relative_to(RAW_LMS_ROOT)}")
    else:
        print("\n[SUCCESS] ALL FILES CONVERTED!")

if __name__ == "__main__":
    final_audit()

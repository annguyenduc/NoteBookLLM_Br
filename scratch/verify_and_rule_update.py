import sqlite3
import os
import sys

# Ensure UTF-8 output for Windows console
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"
AGENTS_MD = r"d:\NoteBookLLM_Br\AGENTS.md"

def verify_and_update_rules():
    conn = sqlite3.connect(DB_PATH)
    
    # 1. Verify Status
    print("--- 10 Most Recent Concept Atoms ---")
    atoms = conn.execute("""
        SELECT file_id, status, confidence
        FROM atoms
        WHERE file_id LIKE 'CONCEPT_%'
        ORDER BY last_modified DESC
        LIMIT 10
    """).fetchall()
    print(f"Found: {len(atoms)} atoms")
    for a in atoms:
        print(a)
    conn.close()

    # 2. Add Rule to AGENTS.md
    print("\n--- Updating AGENTS.md ---")
    with open(AGENTS_MD, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rule = """
## RULE: Atom Status Creation
- Mọi atom tạo mới phải có status = DRAFT
- KHÔNG set status = VERIFIED/SYNTHESIZED khi tạo atom
- Chỉ ingest.py và reconciler.py được set VERIFIED
- Chỉ HUMAN được set SYNTHESIZED
"""
    if 'RULE: Atom Status Creation' not in content:
        with open(AGENTS_MD, 'a', encoding='utf-8') as f:
            f.write(rule)
        print("Rule added to AGENTS.md.")
    else:
        print("Rule already exists.")

if __name__ == "__main__":
    verify_and_update_rules()

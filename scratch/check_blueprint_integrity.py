import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r"d:\NoteBookLLM_Br"
sources = [
    'SOURCE_META_KARPATHY_LLM_WIKI',
    'SOURCE_META_NASHUS_LLMWIKI',
    'SOURCE_META_KARPATHY_CLAUDE_SKILLS',
    'SOURCE_META_WIKI_GEN_CLONE',
    'SOURCE_META_LLM_WIKI_V2' # Added this one as I saw it in the preview
]

print("--- 2. Sources Physical Check ---")
for s in sources:
    found = False
    for root, dirs, files in os.walk(ROOT):
        for f in files:
            if s in f:
                print(f"OK: {os.path.join(root,f)}")
                found = True
                break # Only need to find it once
        if found: break
    if not found:
        print(f"MISSING: {s}")

import sqlite3
DB_PATH = os.path.join(ROOT, "3-resources", "wiki", "wiki_brain.db")

print("\n--- 3. Relationships in DB ---")
try:
    conn = sqlite3.connect(DB_PATH)
    edges = conn.execute("""
        SELECT edge_type, target_id FROM edges
        WHERE source_id = 'SYNTHESIS_MASTER_SECOND_BRAIN_BLUEPRINT'
    """).fetchall()
    print(f"Edges in DB: {len(edges)}")
    for e in edges:
        print(f"  {e[0]} → {e[1]}")
    conn.close()
except Exception as e:
    print(f"Error: {e}")

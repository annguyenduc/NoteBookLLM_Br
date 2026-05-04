import sqlite3
import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def check_synthesis():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT file_id, title, status, confidence,
               SUBSTR(content, 1, 150) as preview
        FROM atoms
        WHERE category = 'Rooms (Synthesis)'
        ORDER BY confidence DESC
    """).fetchall()
    
    print(f"--- 17 Synthesis Atoms (Tầng tri thức tổng hợp) ---")
    print(f"Total: {len(rows)}")
    for r in rows:
        print(f"\n[{r[2]}] {r[1]} (ID: {r[0]}) | Conf: {r[3]}")
        if r[4]:
            preview = r[4].replace('\n', ' ').strip()
            print(f"  > {preview}...")
        else:
            print("  > [NO CONTENT IN DB]")
    conn.close()

if __name__ == "__main__":
    check_synthesis()

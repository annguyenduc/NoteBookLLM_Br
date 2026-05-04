import sqlite3
import sys
import io

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def filter_meta():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute('''
        SELECT file_id, title, confidence,
               LENGTH(content) as content_len
        FROM atoms
        WHERE file_id LIKE 'CONCEPT_META%'
        AND status != 'DEPRECATED'
        AND content IS NOT NULL
        AND LENGTH(content) > 200
        ORDER BY content_len DESC
        LIMIT 20
    ''').fetchall()
    
    print(f'CONCEPT_META có content thật: {len(rows)}')
    for r in rows:
        # Avoid potential None title
        title = r[1] if r[1] else "None"
        print(f'  {r[0]} | {title} | {r[2]} conf | {r[3]} chars')
    conn.close()

if __name__ == "__main__":
    filter_meta()

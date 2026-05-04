import sqlite3
import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def run_audit():
    if not os.path.exists(DB_PATH):
        print("Error: DB not found.")
        return
        
    conn = sqlite3.connect(DB_PATH)
    
    print('=== STATUS DISTRIBUTION ===')
    rows = conn.execute('''
        SELECT status, COUNT(*) as count
        FROM atoms
        GROUP BY status
        ORDER BY count DESC
    ''').fetchall()
    for r in rows: print(f'  {r[0]}: {r[1]}')

    print('\n=== CATEGORY DISTRIBUTION ===')
    rows = conn.execute('''
        SELECT category, COUNT(*) as count
        FROM atoms
        GROUP BY category
        ORDER BY count DESC
        LIMIT 10
    ''').fetchall()
    for r in rows: print(f'  {r[0]}: {r[1]}')

    print('\n=== CONFIDENCE DISTRIBUTION ===')
    rows = conn.execute('''
        SELECT
            CASE
                WHEN confidence >= 0.75 THEN 'HIGH (>=0.75)'
                WHEN confidence >= 0.50 THEN 'MID (0.50-0.74)'
                WHEN confidence >= 0.30 THEN 'LOW (0.30-0.49)'
                ELSE 'VERY LOW (<0.30)'
            END as tier,
            COUNT(*) as count
        FROM atoms
        GROUP BY tier
        ORDER BY count DESC
    ''').fetchall()
    for r in rows: print(f'  {r[0]}: {r[1]}')

    print('\n=== LEGACY ATOMS (no content, no title) ===')
    count = conn.execute('''
        SELECT COUNT(*) FROM atoms
        WHERE (content IS NULL OR content = '')
        AND (title IS NULL OR title = '')
    ''').fetchone()[0]
    print(f'  Empty atoms: {count}')

    print('\n=== WIKI FOLDERS IN USE ===')
    # Using a slightly different approach for path split to be robust
    rows = conn.execute("SELECT path FROM atoms WHERE path IS NOT NULL").fetchall()
    folders = {}
    for r in rows:
        path = r[0]
        # Get first two parts of relative path if possible
        # e.g. d:\NoteBookLLM_Br\3-resources\wiki\concepts -> 3-resources\wiki
        rel_path = path.replace(r"d:\NoteBookLLM_Br\\", "").replace(r"d:\NoteBookLLM_Br\\", "")
        parts = rel_path.split(os.sep)
        if len(parts) > 1:
            folder = os.path.join(parts[0], parts[1])
            folders[folder] = folders.get(folder, 0) + 1
    
    sorted_folders = sorted(folders.items(), key=lambda x: x[1], reverse=True)
    for f, c in sorted_folders[:15]:
        print(f'  {f}: {c}')

    print('\n=== EDGES BY TYPE ===')
    rows = conn.execute('''
        SELECT edge_type, COUNT(*) as count
        FROM edges
        GROUP BY edge_type
        ORDER BY count DESC
    ''').fetchall()
    for r in rows: print(f'  {r[0]}: {r[1]}')

    conn.close()

if __name__ == "__main__":
    run_audit()

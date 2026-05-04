import sqlite3
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

db_path = r'3-resources\wiki\wiki_brain.db'
source_id = 'SOURCE_AIMET_AGENTIC_ROADMAP_2026'

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT path, title FROM nodes_fts WHERE metadata LIKE ?", ('%' + source_id + '%',))
    results = cursor.fetchall()
    
    print(f"\n[+] Tổng số Atoms từ nguồn {source_id}: {len(results)}\n")
    for i, (path, title) in enumerate(results, 1):
        fname = os.path.basename(path)
        print(f"{i}. {fname} | {title}")
    
    conn.close()
else:
    print(f"Không tìm thấy database Smart Spine.")

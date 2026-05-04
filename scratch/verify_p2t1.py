import os
import sqlite3

print("--- 2. SKILL.md Content Check ---")
try:
    content = open(r'd:\NoteBookLLM_Br\.agent\skills\wiki-ingest\SKILL.md', encoding='utf-8').read()
    checks = ['Gate', 'magika', 'DRAFT', 'confidence', 'IMMUTABLE']
    for c in checks:
        print(f'  {c}: {"OK" if c in content else "MISSING"}')
    print(f'  Length: {len(content)} chars')
except Exception as e:
    print(f"Error: {e}")

print("\n--- 3. Scripts Existence & Size ---")
for f in ['ingest.py', 'magika_router.py']:
    path = rf'd:\NoteBookLLM_Br\.agent\skills\wiki-ingest\scripts\{f}'
    if os.path.exists(path):
        size = os.path.getsize(path)
        lines = len(open(path, encoding='utf-8').readlines())
        print(f'  {f}: {size} bytes, {lines} lines')
    else:
        print(f'  {f}: MISSING')

print("\n--- 4. Task Logs Verification ---")
try:
    conn = sqlite3.connect(r'd:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db')
    logs = conn.execute("SELECT action, status, details FROM task_logs ORDER BY timestamp DESC LIMIT 10").fetchall()
    for l in logs:
        print(l)
    conn.close()
except Exception as e:
    print(f"Error: {e}")

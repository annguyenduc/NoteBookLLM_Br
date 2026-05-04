import sqlite3
import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r"d:\NoteBookLLM_Br"
WIKI_BASE = os.path.join(ROOT, "3-resources", "wiki")
DB = os.path.join(WIKI_BASE, "wiki_brain.db")

def find_file(rel_path):
    # Try 1: ROOT + rel_path
    p1 = os.path.join(ROOT, rel_path)
    if os.path.isfile(p1): return p1
    
    # Try 2: WIKI_BASE + rel_path
    p2 = os.path.join(WIKI_BASE, rel_path)
    if os.path.isfile(p2): return p2
    
    # Try 3: Recursive search for basename in WIKI_BASE
    basename = os.path.basename(rel_path)
    for root, dirs, files in os.walk(WIKI_BASE):
        if basename in files:
            return os.path.join(root, basename)
            
    return None

def populate_content():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    # Rollback DEPRECATED status from previous failed attempt
    cursor.execute("UPDATE atoms SET status='DRAFT' WHERE status='DEPRECATED'")
    
    populated = 0
    not_found = 0
    
    # Get atoms with no content or no title
    atoms = cursor.execute("""
        SELECT path, file_id FROM atoms
        WHERE (content IS NULL OR content = '')
        OR (title IS NULL OR title = '')
    """).fetchall()
    
    print(f"Total atoms to process: {len(atoms)}")
    
    for rel_path, file_id in atoms:
        if not rel_path:
            continue
            
        full_path = find_file(rel_path)
            
        if full_path:
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title from H1 or filename
                title = ""
                for line in content.split('\n'):
                    if line.startswith('# '):
                        title = line[2:].strip()
                        break
                if not title:
                    title = file_id or os.path.basename(full_path).replace('.md', '')
                
                # Normalize the path in DB to the found relative path if it's different
                new_rel_path = os.path.relpath(full_path, ROOT)
                
                cursor.execute("""
                    UPDATE atoms 
                    SET content=?, title=?, status='DRAFT', path=?
                    WHERE path=? OR file_id=?
                """, (content[:10000], title, new_rel_path, rel_path, file_id))
                populated += 1
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
        else:
            not_found += 1
            cursor.execute("UPDATE atoms SET status='DEPRECATED' WHERE path=? OR file_id=?", (rel_path, file_id))
            
    conn.commit()
    conn.close()
    print(f"Populated: {populated}")
    print(f"Deprecated (not found): {not_found}")

if __name__ == "__main__":
    populate_content()

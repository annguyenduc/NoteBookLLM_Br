import sqlite3
import os
import sys

# Ensure UTF-8 output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r"d:\NoteBookLLM_Br"
DB = os.path.join(ROOT, "3-resources", "wiki", "wiki_brain.db")

def populate_content():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    
    populated = 0
    deprecated = 0
    
    # Get atoms with no content or no title
    atoms = cursor.execute("""
        SELECT path, file_id, status FROM atoms
        WHERE (content IS NULL OR content = '')
        OR (title IS NULL OR title = '')
    """).fetchall()
    
    for path, file_id, current_status in atoms:
        if not path:
            continue
            
        # Build absolute path
        if os.path.isabs(path):
            full_path = path
        else:
            # Handle potential relative path formats
            full_path = os.path.join(ROOT, path)
            
        if os.path.isfile(full_path):
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
                    title = file_id or os.path.basename(path).replace('.md', '')
                
                # Update status to DRAFT for these empty ones, populate content and title
                cursor.execute("""
                    UPDATE atoms 
                    SET content=?, title=?, status='DRAFT'
                    WHERE path=?
                """, (content[:10000], title, path))
                populated += 1
            except Exception as e:
                print(f"Error reading {full_path}: {e}")
        else:
            # If no file found, mark as DEPRECATED
            cursor.execute("""
                UPDATE atoms SET status='DEPRECATED'
                WHERE path=?
            """, (path,))
            deprecated += 1
            
    conn.commit()
    conn.close()
    print(f"Populated: {populated}")
    print(f"Deprecated (no file found): {deprecated}")

if __name__ == "__main__":
    populate_content()

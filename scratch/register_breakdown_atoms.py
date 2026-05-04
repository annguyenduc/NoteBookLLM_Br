import sqlite3
import os
from datetime import datetime

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"
CONCEPTS_DIR = r"d:\NoteBookLLM_Br\3-resources\wiki\concepts"

new_atoms = [
    "CONCEPT_Karpathy_Idea_File.md",
    "CONCEPT_Wiki_vs_RAG.md",
    "CONCEPT_Three_Layer_Architecture.md",
    "CONCEPT_Wiki_Operations.md",
    "CONCEPT_Tooling_Stack.md"
]

def register_atoms():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    registered_count = 0
    for filename in new_atoms:
        path = os.path.join(CONCEPTS_DIR, filename)
        file_id = filename.replace(".md", "")
        
        # Insert if not exists
        cursor.execute("""
            INSERT OR IGNORE INTO atoms (file_id, title, path, status, confidence, last_modified, agent_id, category)
            VALUES (?, ?, ?, 'DRAFT', 0.7, ?, '@engineer', 'Wiki Page')
        """, (file_id, filename, path, datetime.now().isoformat()))
        
        if cursor.rowcount > 0:
            # Also add to review_queue
            cursor.execute("""
                INSERT OR IGNORE INTO review_queue (item_id, reason)
                VALUES (?, 'Manual breakdown from Karpathy Guide')
            """, (file_id, ))
            registered_count += 1
            
    conn.commit()
    conn.close()
    print(f"Registered {registered_count} new DRAFT atoms in DB and review_queue.")

if __name__ == "__main__":
    register_atoms()

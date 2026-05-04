import sqlite3

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def fix_status():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check current status
    cursor.execute("""
        SELECT file_id, status FROM atoms
        WHERE file_id LIKE 'CONCEPT_Karpathy%'
        OR file_id LIKE 'CONCEPT_Wiki%'
        OR file_id LIKE 'CONCEPT_Three%'
        OR file_id LIKE 'CONCEPT_Tooling%'
    """)
    rows = cursor.fetchall()
    print("Current state:")
    for row in rows:
        print(row)
        
    # Update to DRAFT
    cursor.execute("""
        UPDATE atoms SET status='DRAFT'
        WHERE (file_id LIKE 'CONCEPT_Karpathy%'
        OR file_id LIKE 'CONCEPT_Wiki%'
        OR file_id LIKE 'CONCEPT_Three%'
        OR file_id LIKE 'CONCEPT_Tooling%')
        AND status != 'DRAFT'
    """)
    fixed = cursor.rowcount
    conn.commit()
    conn.close()
    print(f"Fixed: {fixed} atoms -> DRAFT")

if __name__ == "__main__":
    fix_status()

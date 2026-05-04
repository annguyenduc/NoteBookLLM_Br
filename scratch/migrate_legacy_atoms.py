import sqlite3
import os

db_path = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def migrate_legacy_atoms():
    if not os.path.exists(db_path):
        print(f"Error: DB not found at {db_path}")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # SQL query to update status for legacy atoms
        # Atoms that have null status or status that is NOT in the standard set
        query = """
            UPDATE atoms 
            SET status = 'VERIFIED', 
                confidence = 0.70 
            WHERE status IS NULL 
               OR status NOT IN ('DRAFT', 'VERIFIED', 'REVIEWED', 'SYNTHESIZED', 'DEPRECATED')
        """
        
        cursor.execute(query)
        updated_count = cursor.rowcount
        conn.commit()
        
        print(f"Migration Success: Updated {updated_count} legacy atoms to VERIFIED status.")
        
        # Log to task_logs
        cursor.execute("""
            INSERT INTO task_logs (agent_id, action, status, details)
            VALUES (?, ?, ?, ?)
        """, ("@pm", "migration", "success", f"Standardized {updated_count} legacy atoms to VERIFIED"))
        conn.commit()
        
        conn.close()
    except Exception as e:
        print(f"Migration Error: {e}")

if __name__ == "__main__":
    migrate_legacy_atoms()

import sqlite3

db_path = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def record_note():
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("""
            INSERT OR REPLACE INTO structure (key, value)
            VALUES ('legacy_migration_note', 
            '289 atoms migrated to VERIFIED on 2026-05-04 with confidence=0.70 - not human-reviewed')
        """)
        conn.commit()
        conn.close()
        print("Legacy migration note recorded successfully.")
    except Exception as e:
        print(f"Error recording note: {e}")

if __name__ == "__main__":
    record_note()

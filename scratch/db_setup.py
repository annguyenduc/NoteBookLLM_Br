import sqlite3
import os

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"
SQL_PATH = r"d:\NoteBookLLM_Br\scratch\init_db.sql"

def init_db():
    print(f"Initializing database at: {DB_PATH}")
    
    # Ensure directory exists (already done, but safe)
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        with open(SQL_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()
            
        cursor.executescript(sql_script)
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    init_db()

import sqlite3
import os

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def migrate_v3_1():
    print(f"Migrating database to V3.1: {DB_PATH}")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 1. Clean up my previous dummy 'atoms' and 'links' tables if they exist
        cursor.execute("DROP TABLE IF EXISTS atoms;")
        cursor.execute("DROP TABLE IF EXISTS links;")
        cursor.execute("DROP TABLE IF EXISTS sources;")
        cursor.execute("DROP TABLE IF EXISTS task_logs;")
        cursor.execute("DROP TABLE IF EXISTS atom_search;")
        
        # 2. Rename nodes_meta to atoms
        cursor.execute("ALTER TABLE nodes_meta RENAME TO atoms;")
        print("Renamed nodes_meta to atoms.")
        
        # 3. Add new columns to atoms
        # SQLite doesn't support adding multiple columns in one ALTER TABLE
        new_columns = [
            ("confidence", "REAL DEFAULT 0.9"),
            ("learning_source", "INTEGER DEFAULT 0"),
            ("metadata", "JSON"),
            ("file_hash", "TEXT")
        ]
        
        for col_name, col_def in new_columns:
            try:
                cursor.execute(f"ALTER TABLE atoms ADD COLUMN {col_name} {col_def};")
                print(f"Added column {col_name} to atoms.")
            except sqlite3.OperationalError:
                print(f"Column {col_name} already exists.")

        # 4. Create review_queue
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS review_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id TEXT NOT NULL,
            reason TEXT,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (item_id) REFERENCES atoms(file_id)
        );
        """)
        print("Created review_queue table.")

        # 5. Create structure (Meta table)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS structure (
            key TEXT PRIMARY KEY,
            value TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        # Set version
        cursor.execute("INSERT OR REPLACE INTO structure (key, value) VALUES ('version', '3.1');")
        print("Created structure table.")

        # 6. Ensure session_insights exists (might have been created by my previous script)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS session_insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            tags TEXT
        );
        """)
        print("Ensured session_insights table exists.")

        # 7. Setup FTS5
        cursor.execute("DROP TABLE IF EXISTS atom_search;")
        cursor.execute("""
        CREATE VIRTUAL TABLE atom_search USING fts5(
            file_id UNINDEXED,
            title,
            content,
            tokenize='porter unicode61'
        );
        """)
        print("Setup FTS5 atom_search table.")

        # 8. Re-check edges (User might want to rename columns later, but keeping as is for now)
        # Existing columns: source_id, target_id, edge_type, confidence, created_at
        
        conn.commit()
        print("Migration to V3.1 completed successfully.")
        
    except Exception as e:
        print(f"Error during migration: {e}")
        conn.rollback()
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    migrate_v3_1()

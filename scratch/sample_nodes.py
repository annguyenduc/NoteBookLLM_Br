import sqlite3

DB_PATH = "3-resources/wiki/wiki_brain.db"

def sample_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(nodes_meta);")
        columns = cursor.fetchall()
        print("Columns in nodes_meta:", [c[1] for c in columns])
        
        cursor.execute("SELECT * FROM nodes_meta LIMIT 2;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sample_data()

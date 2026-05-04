import sqlite3

DB_PATH = "3-resources/wiki/wiki_brain.db"

def check_edges_schema():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(edges);")
        columns = cursor.fetchall()
        print("Columns in edges:", [c[1] for c in columns])
        
        cursor.execute("SELECT * FROM edges LIMIT 1;")
        print("Sample row:", cursor.fetchone())
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_edges_schema()

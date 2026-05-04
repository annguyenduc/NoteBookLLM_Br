import sqlite3

DB_PATH = "3-resources/wiki/wiki_brain.db"

def count_rows():
    try:
        conn = sqlite3.connect(DB_PATH)
        for table in ['nodes_meta', 'edges']:
            count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
            print(f"{table}: {count} rows")
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    count_rows()

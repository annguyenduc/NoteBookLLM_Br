import sqlite3

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def test_query():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("--- 1. Testing atom_search (FTS5) ---")
    try:
        # Sync FTS
        cursor.execute("DELETE FROM atom_search")
        cursor.execute("INSERT INTO atom_search (file_id, title, metadata) SELECT file_id, title, metadata FROM atoms")
        conn.commit()
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='atom_search'")
        if cursor.fetchone():
            print("  atom_search table exists.")
            # Search for 'Concept'
            results = cursor.execute("SELECT file_id, title FROM atom_search WHERE atom_search MATCH 'Concept'").fetchall()
            print(f"  Found {len(results)} matches for 'Concept'.")
            for r in results[:3]: print(f"    - {r}")
        else:
            print("  atom_search table MISSING.")
    except Exception as e:
        print(f"  FTS5 Error: {e}")

    print("\n--- 2. Testing Graph Query ---")
    try:
        # Look for the SUPERSEDES edge from Test 3 of Task 2
        cursor.execute("SELECT source_id, target_id FROM edges WHERE edge_type='SUPERSEDES'")
        edges = cursor.fetchall()
        print(f"  Found {len(edges)} SUPERSEDES edges.")
        for e in edges: print(f"    - {e}")
    except Exception as e:
        print(f"  Graph Error: {e}")

    conn.close()

if __name__ == "__main__":
    test_query()

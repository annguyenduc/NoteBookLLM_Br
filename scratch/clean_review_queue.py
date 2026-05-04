import sqlite3
import os

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"

def clean_queue():
    if not os.path.exists(DB_PATH):
        print("DB not found.")
        return
        
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete test items
    cursor.execute("""
        DELETE FROM review_queue
        WHERE item_id LIKE '%test_%'
        OR item_id LIKE '%empty%'
        OR item_id LIKE '%scratch%'
    """)
    
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    print(f"Cleaned: {deleted} test items from review_queue.")

if __name__ == "__main__":
    clean_queue()

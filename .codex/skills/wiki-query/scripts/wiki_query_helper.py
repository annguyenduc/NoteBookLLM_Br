import sqlite3
import os
import sys
import argparse

# Path Configuration
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
DB_PATH = os.path.join(REPO_ROOT, "3-resources", "wiki", "wiki_brain.db")

def query_spine(query_text, limit=5):
    if not os.path.exists(DB_PATH):
        print(f"[!] Lỗi: Không tìm thấy cơ sở dữ liệu tại {DB_PATH}")
        return

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Tìm kiếm bằng FTS5 (BM25 ranking)
        search_query = """
        SELECT path, title, snippet(nodes_fts, 2, '<b>', '</b>', '...', 10) 
        FROM nodes_fts 
        WHERE nodes_fts MATCH ? 
        ORDER BY rank 
        LIMIT ?
        """
        
        cursor.execute(search_query, (query_text, limit))
        results = cursor.fetchall()
        
        if not results:
            print(f"[*] Không tìm thấy kết quả cho: '{query_text}'")
        else:
            print(f"--- 🧠 SMART SPINE SEARCH RESULTS ({len(results)}) ---")
            for path, title, snippet in results:
                print(f"\n📄 {title} ({path})")
                print(f"   Snippet: {snippet}")
        
        conn.close()
    except Exception as e:
        print(f"[!] Lỗi truy vấn: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", required=True, help="Câu hỏi hoặc từ khóa cần tìm")
    parser.add_argument("--limit", type=int, default=5, help="Số lượng kết quả tối đa")
    args = parser.parse_args()
    
    query_spine(args.query, args.limit)

# -*- coding: utf-8 -*-
import sqlite3
import os
import sys

# Trỏ về repo chính
REPO_ROOT = "D:/NoteBookLLM_Br"
DB_PATH = os.path.join(REPO_ROOT, "3-resources", "wiki", "wiki_brain.db")

def query_spine(query_text, limit=5):
    """Tìm kiếm Atom dựa trên FTS5 trên bảng atom_search join với atoms."""
    if not os.path.exists(DB_PATH):
        print(f"[!] Lỗi: Không tìm thấy cơ sở dữ liệu tại {DB_PATH}")
        return False

    try:
        # Kết nối database ở chế độ read-only
        db_uri = f"file:{DB_PATH}?mode=ro"
        conn = sqlite3.connect(db_uri, uri=True)
        cursor = conn.cursor()
        
        # Tìm kiếm bằng FTS5 (BM25 ranking) trên bảng atom_search join với atoms
        search_query = """
        SELECT a.file_id, a.title, snippet(atom_search, 1, '<b>', '</b>', '...', 10) 
        FROM atom_search 
        JOIN atoms a ON atom_search.file_id = a.file_id
        WHERE atom_search MATCH ? 
        ORDER BY rank 
        LIMIT ?
        """
        
        cursor.execute(search_query, (query_text, limit))
        results = cursor.fetchall()
        
        if not results:
            print(f"[*] Không tìm thấy kết quả cho: '{query_text}'")
        else:
            print(f"--- 🧠 SMART SPINE SEARCH RESULTS ({len(results)}) ---")
            for file_id, title, snippet in results:
                print(f"\n📄 {title} ({file_id})")
                print(f"   Snippet: {snippet}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"[!] Lỗi truy vấn: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("[!] Lỗi: Bạn cần cung cấp từ khóa tìm kiếm.")
        print("Ví dụ: python query_wiki.py \"feedback loop\"")
        sys.exit(1)
        
    query_text = sys.argv[1]
    
    limit = 5
    if len(sys.argv) >= 3:
        try:
            limit = int(sys.argv[2])
        except ValueError:
            pass
            
    success = query_spine(query_text, limit=limit)
    
    # Output contract
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"query_wiki.py\"")
    print(f"  command: \"python scripts/tasks/query_wiki.py \\\"{query_text}\\\"\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"PASS\"" if success else "  result: \"FAIL\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NONE\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"Tim kiem tu khoa '{query_text}' trong wiki spine. Ket qua: {'Thanh cong' if success else 'That bai'}\"")
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

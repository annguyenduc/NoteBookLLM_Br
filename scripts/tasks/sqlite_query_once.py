# -*- coding: utf-8 -*-
import os
import sys
import sqlite3
import argparse

# Trỏ về repo chính
REPO_ROOT = "D:/NoteBookLLM_Br"
DB_PATH = os.path.join(REPO_ROOT, "3-resources", "wiki", "wiki_brain.db")

def is_safe_select(query):
    """Kiểm tra xem câu lệnh SQL có phải là câu lệnh SELECT an toàn hay không."""
    q = query.strip().lower()
    
    # Bắt buộc phải bắt đầu bằng SELECT
    if not q.startswith("select"):
        return False
        
    # Các từ khóa sửa đổi dữ liệu bị cấm tuyệt đối
    forbidden = ["insert", "update", "delete", "drop", "alter", "create", "replace", "vacuum", "attach", "detach"]
    for word in forbidden:
        if f" {word} " in f" {q} " or f"\n{word} " in f" {q} " or f"\t{word} " in f" {q} ":
            return False
            
    return True

def print_markdown_table(headers, rows):
    """In danh sách kết quả ra bảng Markdown."""
    if not headers:
        return
    # In header
    header_line = " | ".join(str(h) for h in headers)
    print(f"| {header_line} |")
    # In separator
    sep_line = " | ".join("---" for _ in headers)
    print(f"| {sep_line} |")
    # In rows
    for row in rows:
        row_line = " | ".join(str(val) if val is not None else "NULL" for val in row)
        print(f"| {row_line} |")

def main():
    parser = argparse.ArgumentParser(description="Chạy một câu lệnh SELECT SQLite duy nhất ở chế độ chỉ đọc.")
    parser.add_argument("query", nargs="?", help="Câu lệnh SQL SELECT cần thực thi")
    parser.add_argument("--query", dest="query_opt", help="Câu lệnh SQL SELECT cần thực thi (tùy chọn)")
    args = parser.parse_args()
    
    query = args.query or args.query_opt
    
    if not query:
        print("[!] Lỗi: Bạn cần cung cấp câu lệnh SQL SELECT.")
        print("Ví dụ: python sqlite_query_once.py \"SELECT count(*) FROM nodes\"")
        sys.exit(1)
        
    if not is_safe_select(query):
        print("[!] Lỗi bảo mật: Chỉ cho phép các câu lệnh SELECT chỉ đọc (Read-only SELECT).")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"sqlite_query_once.py\"")
        print(f"  command: \"python scripts/tasks/sqlite_query_once.py\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NONE\"")
        print("  stayed_resident: \"NO\"")
        print("  summary: \"Vi pham bao mat: cau lenh khong phai SELECT hoac chua tu khoa cam\"")
        sys.exit(1)
        
    if not os.path.exists(DB_PATH):
        print(f"[!] Lỗi: Không tìm thấy database tại {DB_PATH}")
        sys.exit(1)
        
    try:
        # Kết nối database ở chế độ read-only qua URI
        db_uri = f"file:{DB_PATH}?mode=ro"
        conn = sqlite3.connect(db_uri, uri=True)
        cursor = conn.cursor()
        
        cursor.execute(query)
        rows = cursor.fetchall()
        headers = [desc[0] for desc in cursor.description] if cursor.description else []
        
        print(f"--- 📊 KẾT QUẢ TRUY VẤN SQLITE ({len(rows)} hàng) ---")
        if len(rows) == 0:
            print("Truy vấn thành công nhưng không có kết quả trả về.")
        else:
            print_markdown_table(headers, rows)
            
        conn.close()
        
        # Output contract
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"sqlite_query_once.py\"")
        print(f"  command: \"python scripts/tasks/sqlite_query_once.py \\\"{query}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"PASS\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NONE\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Truy van thanh cong, tra ve {len(rows)} hang\"")
        
    except Exception as e:
        print(f"[!] Lỗi khi chạy truy vấn: {e}")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"sqlite_query_once.py\"")
        print(f"  command: \"python scripts/tasks/sqlite_query_once.py \\\"{query}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NONE\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Loi SQL: {str(e)}\"")
        sys.exit(1)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
import os
import sys
import site
import argparse
from pathlib import Path

# Bootstrap project venv site-packages
REPO_ROOT = Path("D:/NoteBookLLM_Br")
sys.path.append(str(REPO_ROOT))
site_packages = REPO_ROOT / ".venv" / "Lib" / "site-packages"
if site_packages.exists():
    site.addsitedir(str(site_packages))

try:
    from notebooklm_mcp.auth import load_cached_tokens
    from notebooklm_mcp.api_client import NotebookLMClient
except ImportError as e:
    print(f"[!] Lỗi import notebooklm_mcp: {e}")
    # Output contract khi lỗi import
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"notebooklm_query_once.py\"")
    print("  command: \"python scripts/tasks/notebooklm_query_once.py\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"FAIL\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NotebookLM\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"Loi import notebooklm_mcp: {str(e)}\"")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Gửi truy vấn đến NotebookLM bằng cached token.")
    parser.add_argument("query", nargs="?", help="Câu hỏi cần gửi đến NotebookLM")
    parser.add_argument("--notebook-id", help="ID của notebook (nếu không có, dùng notebook đầu tiên tìm thấy)")
    args = parser.parse_args()
    
    query_text = args.query
    if not query_text:
        print("[!] Lỗi: Bạn cần cung cấp câu hỏi.")
        print("Ví dụ: python notebooklm_query_once.py \"Tóm tắt dự án\"")
        sys.exit(1)
        
    print("--- 🧠 ĐANG KẾT NỐI TỚI NOTEBOOKLM ---")
    
    tokens = load_cached_tokens()
    if not tokens:
        print("[!] Lỗi: Không tìm thấy cached tokens. Vui lòng chạy 'switch_mcp_profile.ps1' hoặc refresh_auth để đăng nhập.")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"notebooklm_query_once.py\"")
        print("  command: \"python scripts/tasks/notebooklm_query_once.py\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NotebookLM\"")
        print("  stayed_resident: \"NO\"")
        print("  summary: \"Thieu cached tokens NotebookLM\"")
        sys.exit(1)
        
    try:
        client = NotebookLMClient(
            cookies=tokens.cookies,
            csrf_token=tokens.csrf_token,
            session_id=tokens.session_id
        )
        
        notebook_id = args.notebook_id
        if not notebook_id:
            print("Đang lấy danh sách các notebook...")
            notebooks = client.list_notebooks()
            if not notebooks:
                print("[!] Lỗi: Không tìm thấy notebook nào trong tài khoản.")
                client.close()
                sys.exit(1)
            # Dùng notebook đầu tiên
            target_notebook = notebooks[0]
            notebook_id = target_notebook.id
            print(f"Sử dụng notebook mặc định (đầu tiên): '{target_notebook.title}' (ID: {notebook_id})")
        else:
            print(f"Sử dụng notebook ID chỉ định: {notebook_id}")
            
        print(f"Đang gửi truy vấn: '{query_text}'...")
        response = client.query(notebook_id, query_text)
        
        print("\n--- 📝 PHẢN HỒI TỪ NOTEBOOKLM ---")
        if isinstance(response, dict):
            answer = response.get("answer", "")
            print(answer)
            sources = response.get("sources", [])
            if sources:
                print("\nNguồn tham khảo:")
                for src in sources:
                    print(f"- {src.get('title')} ({src.get('url', 'N/A')})")
        else:
            print(response)
            
        client.close()
        
        # External Call Policy Report
        print("\nEXTERNAL_CALL_REPORT:")
        print("  service_called: \"NotebookLM\"")
        print(f"  query_sent: \"{query_text}\"")
        print("  result_saved_or_displayed: \"displayed\"")
        print("  file_uploaded: \"no\"")
        
        # Output contract
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"notebooklm_query_once.py\"")
        print(f"  command: \"python scripts/tasks/notebooklm_query_once.py \\\"{query_text}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"PASS\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NotebookLM\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Truy van thanh cong toi notebook: {notebook_id}\"")
        
    except Exception as e:
        print(f"[!] Lỗi khi làm việc với NotebookLM API: {e}")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"notebooklm_query_once.py\"")
        print(f"  command: \"python scripts/tasks/notebooklm_query_once.py \\\"{query_text}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"NotebookLM\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Loi NotebookLM API: {str(e)}\"")
        sys.exit(1)

if __name__ == "__main__":
    main()

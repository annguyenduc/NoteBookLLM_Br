# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error

# Trỏ về repo chính
REPO_ROOT = "D:/NoteBookLLM_Br"
ENV_PATH = os.path.join(REPO_ROOT, ".env")

def get_tavily_api_key():
    """Đọc TAVILY_API_KEY từ biến môi trường hoặc file .env."""
    key = os.environ.get("TAVILY_API_KEY")
    if key:
        return key
        
    if os.path.exists(ENV_PATH):
        try:
            with open(ENV_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        if k.strip() == "TAVILY_API_KEY":
                            val = v.strip()
                            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                                val = val[1:-1]
                            return val
        except Exception:
            pass
    return None

def main():
    if len(sys.argv) < 2:
        print("[!] Lỗi: Bạn cần cung cấp câu truy vấn tìm kiếm.")
        print("Ví dụ: python tavily_search_once.py \"agentic workflow design\"")
        sys.exit(1)
        
    query_text = sys.argv[1]
    
    api_key = get_tavily_api_key()
    if not api_key:
        print("[!] Lỗi: Không tìm thấy TAVILY_API_KEY trong file .env hoặc biến môi trường.")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"tavily_search_once.py\"")
        print("  command: \"python scripts/tasks/tavily_search_once.py\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"Tavily\"")
        print("  stayed_resident: \"NO\"")
        print("  summary: \"Thieu TAVILY_API_KEY trong .env\"")
        sys.exit(1)
        
    print(f"--- 🌐 ĐANG TÌM KIẾM WEB QUA TAVILY: '{query_text}' ---")
    
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    data = {
        "api_key": api_key,
        "query": query_text,
        "search_depth": "basic",
        "include_answer": False
    }
    
    try:
        req_data = json.dumps(data).encode("utf-8")
        req = urllib.request.Request(url, data=req_data, headers=headers, method="POST")
        
        with urllib.request.urlopen(req, timeout=15) as response:
            res_body = response.read().decode("utf-8")
            res_json = json.loads(res_body)
            
        results = res_json.get("results", [])
        print(f"Tìm thấy {len(results)} kết quả:")
        for i, res in enumerate(results[:5], 1):
            print(f"\n[{i}] 📄 {res.get('title')}")
            print(f"    URL: {res.get('url')}")
            print(f"    Nội dung: {res.get('content')[:200]}...")
            
        # External Call Policy Report
        print("\nEXTERNAL_CALL_REPORT:")
        print("  service_called: \"Tavily\"")
        print(f"  query_sent: \"{query_text}\"")
        print("  result_saved_or_displayed: \"displayed\"")
        print("  file_uploaded: \"no\"")
        
        # Output contract
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"tavily_search_once.py\"")
        print(f"  command: \"python scripts/tasks/tavily_search_once.py \\\"{query_text}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"PASS\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"Tavily\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Tim kiem web thanh cong, tra ve {len(results)} ket qua\"")
        
    except Exception as e:
        print(f"[!] Lỗi khi kết nối tới Tavily API: {e}")
        print("\nSCRIPT_RUN_REPORT:")
        print("  script: \"tavily_search_once.py\"")
        print(f"  command: \"python scripts/tasks/tavily_search_once.py \\\"{query_text}\\\"\"")
        print("  mode: \"safe_auto\"")
        print("  result: \"FAIL\"")
        print("  files_written: []")
        print("  files_modified: []")
        print("  external_service_called: \"Tavily\"")
        print("  stayed_resident: \"NO\"")
        print(f"  summary: \"Loi ket noi Tavily API: {str(e)}\"")
        sys.exit(1)

if __name__ == "__main__":
    main()

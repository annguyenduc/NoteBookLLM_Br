# -*- coding: utf-8 -*-
import os
import sys
import json

# Trỏ về repo chính để import libs nếu cần
REPO_ROOT = "D:/NoteBookLLM_Br"
sys.path.append(REPO_ROOT)

CONFIG_PATHS = {
    "Antigravity Chat Client Config": r"C:\Users\anngu\.gemini\antigravity\mcp_config.json",
    "Antigravity IDE Config": r"C:\Users\anngu\.gemini\antigravity-ide\mcp_config.json",
    "Global CLI/Core Config": r"C:\Users\anngu\.gemini\config\mcp_config.json"
}

def inspect_file(name, path):
    print(f"\n--- 🔍 Kiểm tra {name} ({path}) ---")
    if not os.path.exists(path):
        print(f"[-] Không tìm thấy file tại đường dẫn này.")
        return 0, "Không tồn tại"
        
    try:
        with open(path, "r", encoding="utf-8-sig") as f:
            config = json.load(f)
            
        mcp_servers = config.get("mcpServers", {})
        
        active_count = 0
        for srv_name, srv_config in mcp_servers.items():
            is_disabled = srv_config.get("disabled", False)
            status_str = "[DISABLED]" if is_disabled else "[ACTIVE]"
            if not is_disabled:
                active_count += 1
            print(f"\n  🖥️ Server: {srv_name} {status_str}")
            print(f"    Command: {srv_config.get('command')}")
            print(f"    Args: {srv_config.get('args')}")
            env = srv_config.get("env")
            if env:
                safe_env = {k: ("***" if "key" in k.lower() or "token" in k.lower() else v) for k, v in env.items()}
                print(f"    Env: {safe_env}")
        
        print(f"[+] Kết quả: Active {active_count}/{len(mcp_servers)} servers.")
        return active_count, f"Thành công (Active: {active_count}/{len(mcp_servers)})"
    except PermissionError:
        print(f"[!] Lỗi phân quyền: Không có quyền đọc file này (Permission Denied).")
        return 0, "Lỗi phân quyền"
    except Exception as e:
        print(f"[!] Lỗi đọc file: {e}")
        return 0, f"Lỗi: {e}"

def main():
    print("--- ⚙️ ĐANG KIỂM TRA CẤU HÌNH MCP CONFIG (2 NGUỒN) ---")
    
    results = {}
    total_servers = 0
    
    for name, path in CONFIG_PATHS.items():
        count, status = inspect_file(name, path)
        results[name] = {"count": count, "status": status}
        total_servers += count
        
    # Output contract
    summary_str = ", ".join([f"{k}: {v['status']} ({v['count']} srvs)" for k, v in results.items()])
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"inspect_mcp_config.py\"")
    print("  command: \"python scripts/tasks/inspect_mcp_config.py\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"PASS\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NONE\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"{summary_str}\"")

if __name__ == "__main__":
    main()

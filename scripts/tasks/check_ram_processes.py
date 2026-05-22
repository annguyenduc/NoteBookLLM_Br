# -*- coding: utf-8 -*-
import os
import sys
import psutil

# Trỏ về repo chính để import libs nếu cần
REPO_ROOT = "D:/NoteBookLLM_Br"
sys.path.append(REPO_ROOT)

def format_ram(bytes_val):
    """Định dạng số bytes sang MB để hiển thị."""
    return f"{bytes_val / 1024 / 1024:.2f} MB"

def get_related_processes():
    """Lấy danh sách các tiến trình liên quan đến dự án và tính tổng RAM."""
    process_list = []
    total_ram = 0
    
    # Các từ khóa nhận diện tiến trình liên quan đến dự án
    keywords = ["notebookllm_br", "mcp", "tavily", "sqlite", "fastmcp"]
    
    for proc in psutil.process_iter(['pid', 'name', 'cmdline', 'memory_info']):
        try:
            info = proc.info
            cmdline = info.get('cmdline') or []
            cmdline_str = " ".join(cmdline).lower()
            name = (info.get('name') or "").lower()
            
            is_related = False
            # Kiểm tra xem command line hoặc tên tiến trình có liên quan không
            if any("notebookllm_br" in p.lower() for p in cmdline):
                is_related = True
            elif any(kw in cmdline_str for kw in keywords):
                is_related = True
            elif any(kw in name for kw in keywords):
                is_related = True
                
            if is_related:
                mem = info.get('memory_info')
                rss = mem.rss if mem else 0
                total_ram += rss
                process_list.append({
                    "pid": info['pid'],
                    "name": info['name'],
                    "ram": format_ram(rss),
                    "cmd": " ".join(cmdline)
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
            
    return process_list, total_ram

def main():
    print("--- 🔍 ĐANG KIỂM TRA RAM TIẾN TRÌNH LIÊN QUAN ---")
    procs, total_ram_bytes = get_related_processes()
    
    if not procs:
        print("Không tìm thấy tiến trình liên quan nào đang chạy ngầm.")
    else:
        print(f"Tìm thấy {len(procs)} tiến trình liên quan:")
        for p in procs:
            print(f"- PID: {p['pid']} | Tên: {p['name']} | RAM: {p['ram']}")
            print(f"  Lệnh: {p['cmd'][:120]}")
            
    print(f"\nTổng dung lượng RAM Idle tiêu tốn: {format_ram(total_ram_bytes)}")
    
    # Output Contract theo spec
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"check_ram_processes.py\"")
    print("  command: \"python scripts/tasks/check_ram_processes.py\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"PASS\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NONE\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"Tim thay {len(procs)} tien trinh, tong RAM su dung: {format_ram(total_ram_bytes)}\"")

if __name__ == "__main__":
    main()

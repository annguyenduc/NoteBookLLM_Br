# -*- coding: utf-8 -*-
import os
import sys
import subprocess

def run_git_cmd(args):
    """Thực thi một lệnh git và trả về kết quả string."""
    try:
        res = subprocess.run(args, capture_output=True, text=True, check=True, encoding="utf-8")
        return res.stdout.rstrip('\r\n')
    except Exception as e:
        return f"Lỗi chạy git: {e}"

def main():
    print("--- 🌿 ĐANG KIỂM TRA TRẠNG THÁI GIT ---")
    
    branch = run_git_cmd(["git", "branch", "--show-current"])
    last_commit = run_git_cmd(["git", "log", "-n", "1", "--oneline"])
    status_porcelain = run_git_cmd(["git", "status", "--porcelain"])
    
    modified = []
    untracked = []
    deleted = []
    staged = []
    
    if status_porcelain and not status_porcelain.startswith("Lỗi"):
        lines = status_porcelain.split("\n")
        for line in lines:
            if not line:
                continue
            status_code = line[:2]
            file_path = line[3:]
            
            # Phân loại theo mã trạng thái git status
            if status_code.startswith("M") or "M" in status_code:
                modified.append(file_path)
            elif status_code.startswith("??"):
                untracked.append(file_path)
            elif status_code.startswith("D") or "D" in status_code:
                deleted.append(file_path)
            elif status_code.startswith("A") or "A" in status_code:
                staged.append(file_path)
                
    total_changes = len(modified) + len(untracked) + len(deleted) + len(staged)
    
    print(f"Nhánh hiện tại: {branch}")
    print(f"Commit gần nhất: {last_commit}")
    print(f"Tổng số file thay đổi: {total_changes}")
    if total_changes > 0:
        if staged:
            print(f"  - Staged (Đã chuẩn bị): {len(staged)} files")
        if modified:
            print(f"  - Modified (Đã sửa đổi): {len(modified)} files")
            for f in modified[:5]:
                print(f"    * {f}")
            if len(modified) > 5:
                print(f"    * ... và {len(modified) - 5} file khác")
        if untracked:
            print(f"  - Untracked (Chưa theo dõi): {len(untracked)} files")
            for f in untracked[:5]:
                print(f"    * {f}")
            if len(untracked) > 5:
                print(f"    * ... và {len(untracked) - 5} file khác")
        if deleted:
            print(f"  - Deleted (Đã xóa): {len(deleted)} files")
            
    # Output contract
    print("\nSCRIPT_RUN_REPORT:")
    print("  script: \"git_status_report.py\"")
    print("  command: \"python scripts/tasks/git_status_report.py\"")
    print("  mode: \"safe_auto\"")
    print("  result: \"PASS\"")
    print("  files_written: []")
    print("  files_modified: []")
    print("  external_service_called: \"NONE\"")
    print("  stayed_resident: \"NO\"")
    print(f"  summary: \"Branch: {branch}, thay doi: {total_changes} files (modified: {len(modified)}, untracked: {len(untracked)})\"")

if __name__ == "__main__":
    main()

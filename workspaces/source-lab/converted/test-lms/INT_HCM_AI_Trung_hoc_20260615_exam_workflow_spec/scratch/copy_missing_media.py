import os
import shutil

def main():
    src_dir = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\output_ban_giao_20260622_01\1_Media\GV-HO-AI-KT-INT_HCM_Tri_tue_nhan_tao_Trung_hoc_1_v2-Media"
    dest_dir = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học-Media"
    
    missing_files = [
        # (File nguon, File dich)
        ("cau_3.png", "cau_03.png"),
        ("cau_3.png", "cau_3.png"),
        ("cau_17.png", "cau_17.png"),
        ("cau_17.sb3", "cau_17.sb3")
    ]
    
    print("Copying missing media files...")
    for src_file, dest_file in missing_files:
        src_path = os.path.join(src_dir, src_file)
        dest_path = os.path.join(dest_dir, dest_file)
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dest_path)
            print(f"  Copied: {src_file} -> {dest_file}")
        else:
            print(f"  Error: {src_file} not found in source directory!")

if __name__ == "__main__":
    main()

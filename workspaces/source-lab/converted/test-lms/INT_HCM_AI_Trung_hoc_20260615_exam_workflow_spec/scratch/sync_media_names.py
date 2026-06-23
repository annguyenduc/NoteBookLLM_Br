import os
import glob
import shutil

def rename_files(media_dir):
    # Dinh nghia cac quy tac doi ten: (tu_khoa_cu, tu_khoa_moi)
    # De tranh trung lap khi doi ten, ta se lam theo thu tu nguoc hoac di chuyen tam thoi
    rules = [
        # (Ten file nguon, Ten file dich)
        ("cau_08_1.png", "cau_10_1.png"),
        ("cau_08_source.sb3", "cau_10_source.sb3"),
        ("cau_06_1.png", "cau_09_1.png"),
        ("cau_06_source.sb3", "cau_09_source.sb3"),
        ("cau_04_1.png", "cau_06_1.png"),
        ("cau_04_source.sb3", "cau_06_source.sb3"),
        ("cau_03_1.png", "cau_04_1.png"),
        ("cau_03_2.png", "cau_04_2.png"),
        ("cau_03_3.png", "cau_04_3.png"),
        ("cau_03_4.png", "cau_04_4.png"),
        ("cau_03_source_pack.sb3", "cau_04_source_pack.sb3")
    ]
    
    print(f"Renaming mismatched media in {media_dir}...")
    for old_name, new_name in rules:
        old_path = os.path.join(media_dir, old_name)
        new_path = os.path.join(media_dir, new_name)
        if os.path.exists(old_path):
            shutil.move(old_path, new_path)
            print(f"  Renamed: {old_name} -> {new_name}")
        else:
            print(f"  Warning: {old_name} not found, skipped.")

def main():
    media_dir = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học-Media"
    rename_files(media_dir)
    
    # Kiem tra va sao luu file cau_13 mồ côi (do Word da doi sang ly thuyet)
    cau13_files = glob.glob(os.path.join(media_dir, "cau_13*"))
    if cau13_files:
        archive_dir = os.path.join(media_dir, "archive")
        os.makedirs(archive_dir, exist_ok=True)
        for f in cau13_files:
            shutil.move(f, os.path.join(archive_dir, os.path.basename(f)))
            print(f"  Archived orphaned file: {os.path.basename(f)}")

if __name__ == "__main__":
    main()

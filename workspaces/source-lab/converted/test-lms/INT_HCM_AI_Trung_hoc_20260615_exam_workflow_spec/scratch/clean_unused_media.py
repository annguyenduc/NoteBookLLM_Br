import os
import glob
import shutil

def main():
    media_dir = r"D:\_agent_worktrees\20260615_exam_workflow_spec\workspaces\source-lab\converted\test-lms\INT_HCM_AI_Trung_hoc\_GV-HO-AI-KT-Trí tuệ nhân tạo Trung học-Media"
    archive_dir = os.path.join(media_dir, "archive")
    os.makedirs(archive_dir, exist_ok=True)
    
    # Danh sach cac file media duoc dung thuc te trong DOCX (viet dang pattern or ten chinh xac)
    used_patterns = [
        # Cau 2
        "cau_02_*.png", "cau_02_*.sb3",
        # Cau 3
        "cau_03.png", "cau_3.png",
        # Cau 4 (da duoc doi ten tu cau_03)
        "cau_04_*.png", "cau_04_source_pack.sb3",
        # Cau 6 (da duoc doi ten tu cau_04)
        "cau_06_*.png", "cau_06_source.sb3",
        # Cau 9 (da duoc doi ten tu cau_06)
        "cau_09_*.png", "cau_09_source.sb3",
        # Cau 10 (da duoc doi ten tu cau_08)
        "cau_10_*.png", "cau_10_source.sb3",
        # Cau 11
        "cau_11_*.png", "cau_11_source_pack.sb3",
        # Cau 12
        "cau_12_*.png", "cau_12_source_pack.sb3",
        # Cau 14
        "cau_14_*.png", "cau_14_source_pack.sb3",
        # Cau 17
        "cau_17.png", "cau_17.sb3",
        # Cau 19
        "cau_19_*.png", "cau_19_source.sb3",
        # Cau 21
        "cau_21_*.png", "cau_21_source_pack.sb3",
        # Cau 22
        "cau_22_*.png", "cau_22_*.sb3",
        # Cau 23
        "cau_23_*.png", "cau_23_*.sb3",
        # Cau 24
        "cau_24_*.png", "cau_24_*.sb3",
        # Cau 25
        "cau_25_*.png", "cau_25_*.sb3",
        # Cau 26
        "cau_26_*.png", "cau_26_*.sb3", "cau_26_source.sb3",
        # Cau 27
        "cau_27_*.png", "cau_27_*.sb3",
        # Cau 28
        "cau_28_*.png", "cau_28_*.sb3",
        # Cau 29
        "cau_29_*.png", "cau_29_*.sb3",
        # Cau 30
        "cau_30_*.png", "cau_30_*.sb3"
    ]
    
    # Expand patterns to get a set of used filenames
    used_files = set()
    for pattern in used_patterns:
        full_pattern = os.path.join(media_dir, pattern)
        for filepath in glob.glob(full_pattern):
            used_files.add(os.path.basename(filepath))
            
    print(f"Found {len(used_files)} active media files currently referenced by the exam.")
    
    # Scan all files in media_dir
    all_items = os.listdir(media_dir)
    archived_count = 0
    
    for item in all_items:
        item_path = os.path.join(media_dir, item)
        # Skip directories like archive
        if os.path.isdir(item_path):
            continue
            
        if item not in used_files:
            # Move to archive instead of deleting (Safety First Rule)
            shutil.move(item_path, os.path.join(archive_dir, item))
            print(f"  Archived unused file: {item}")
            archived_count += 1
            
    print(f"\nCleanup complete. Archived {archived_count} unused files to: {archive_dir}")

if __name__ == "__main__":
    main()

import os
import re
import shutil
from datetime import datetime, timedelta

WIKI_DIR = r"d:\NoteBookLLM_Br\3-resources\wiki"
ARCHIVE_DIR = r"d:\NoteBookLLM_Br\4-archive"
RETENTION_DAYS = 30

def extract_date(content, field):
    """Trích xuất ngày từ YAML frontmatter (vd: last_accessed: '2026-05-01')."""
    match = re.search(rf"{field}:\s*['\"]?(\d{{4}}-\d{{2}}-\d{{2}})['\"]?", content)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d")
    return None

def run_retention(apply_changes=False):
    print(f"--- STARTING RETENTION CHECK (Threshold: {RETENTION_DAYS} days) ---")
    today = datetime.now()
    archived_count = 0
    
    # Chỉ quét thư mục queries và synthesis (Tri thức mang tính thời điểm)
    TARGET_DIRS = [os.path.join(WIKI_DIR, "queries"), os.path.join(WIKI_DIR, "synthesis")]
    
    for target_dir in TARGET_DIRS:
        if not os.path.exists(target_dir): continue
        
        for file in os.listdir(target_dir):
            if not file.endswith(".md"): continue
            
            file_path = os.path.join(target_dir, file)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Ưu tiên last_accessed, nếu không có dùng last_updated
            access_date = extract_date(content, "last_accessed") or extract_date(content, "last_updated")
            
            if access_date:
                days_diff = (today - access_date).days
                if days_diff > RETENTION_DAYS:
                    print(f"[EXPIRED] {file} (Old: {days_diff} days)")
                    if apply_changes:
                        dest_path = os.path.join(ARCHIVE_DIR, file)
                        # Đảm bảo thư mục archive tồn tại
                        if not os.path.exists(ARCHIVE_DIR): os.makedirs(ARCHIVE_DIR)
                        shutil.move(file_path, dest_path)
                        archived_count += 1
            else:
                print(f"[SKIP] {file} (No date metadata)")

    if apply_changes:
        print(f"--- SUCCESSFULLY ARCHIVED {archived_count} FILES ---")
    else:
        print("--- DRY RUN COMPLETE. Use --apply to archive. ---")

if __name__ == "__main__":
    import sys
    apply_mode = "--apply" in sys.argv
    run_retention(apply_changes=apply_mode)

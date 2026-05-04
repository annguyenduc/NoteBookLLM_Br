import os
import sqlite3
import subprocess
import sys
import argparse
from datetime import datetime

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

ROOT_DIR = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH  = os.path.join(WIKI_DIR, "wiki_brain.db")
SCRIPTS_DIR = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-rebuild", "scripts")

def sync_db_from_files():
    print("Syncing Database with File System...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    files_on_disk = set()
    scan_folders = ["concepts", "entities", "sources", "synthesis", "decisions"]
    for folder in scan_folders:
        path = os.path.join(WIKI_DIR, folder)
        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith(".md"):
                    file_path = os.path.join(path, f)
                    
                    # [V2.0] RULE R11: No auto-stub creation (< 200 bytes)
                    if os.path.getsize(file_path) < 200:
                        continue
                    
                    # [V2.0] RULE R11: Skip files without valid frontmatter
                    try:
                        with open(file_path, "r", encoding="utf-8") as file_obj:
                            content = file_obj.read()
                            if not content.startswith("---") or "---" not in content[3:]:
                                continue
                    except:
                        continue
                        
                    files_on_disk.add(f[:-3])
                    
    cursor.execute("SELECT file_id FROM atoms")
    db_files = {r[0] for r in cursor.fetchall()}
    
    missing_in_db = files_on_disk - db_files
    if missing_in_db:
        print(f"  Found {len(missing_in_db)} files missing in DB.")
        for fid in missing_in_db:
             cursor.execute("INSERT OR IGNORE INTO atoms (file_id, title, status) VALUES (?, ?, ?)", 
                          (fid, fid.replace("_", " "), "DRAFT"))
    
    conn.commit()
    conn.close()

def heal_orphans():
    """Tự động hàn gắn các Orphan Atoms bằng cách tìm kiếm đề cập trong các atoms khác."""
    print("Healing Orphan Atoms...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. Tìm các atoms mồ côi (không có liên kết đến)
    orphans = cursor.execute("""
        SELECT a.file_id, a.title FROM atoms a
        LEFT JOIN edges e ON a.file_id = e.target_id
        WHERE e.target_id IS NULL AND a.status != 'DEPRECATED'
    """).fetchall()
    
    print(f"  Found {len(orphans)} initial orphans.")
    healed_count = 0
    
    for fid, title in orphans:
        # 2. Tìm kiếm file_id này trong nội dung các atoms khác qua FTS5
        # Bao bọc fid trong dấu ngoặc kép để tránh lỗi cú pháp FTS5 với dấu gạch ngang
        matches = cursor.execute("""
            SELECT file_id FROM atom_search 
            WHERE content MATCH '"' || ? || '"' AND file_id != ?
        """, (fid, fid)).fetchall()
        
        for (source_id,) in matches:
            # 3. Tạo cạnh MENTIONS
            cursor.execute("""
                INSERT OR IGNORE INTO edges (source_id, target_id, edge_type, confidence)
                VALUES (?, ?, 'MENTIONS', 0.5)
            """, (source_id, fid))
            healed_count += 1
            
    conn.commit()
    conn.close()
    print(f"  Healed {healed_count} orphan connections.")
    return healed_count

def run_indexer():
    indexer_path = os.path.join(SCRIPTS_DIR, "indexer.py")
    try:
        result = subprocess.run([sys.executable, indexer_path], capture_output=True, text=True)
        if result.returncode == 0:
            print("  Indexer completed successfully.")
        else:
            print(f"  Error running indexer: {result.stderr}")
    except Exception as e:
        print(f"  Failed to execute indexer: {e}")

def log_rebuild(action_detail):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("""
            INSERT INTO task_logs (agent_id, action, status, details)
            VALUES (?, ?, ?, ?)
        """, ("@engineer", "rebuild", "success", action_detail))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Logging error: {e}")

def refresh_search_index():
    """Cập nhật bảng FTS5 atom_search từ nội dung tệp tin thực tế."""
    print("Refreshing FTS5 Search Index...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Xóa dữ liệu cũ
    cursor.execute("DELETE FROM atom_search")
    
    # Duyệt qua các file và nạp vào FTS5
    scan_folders = ["concepts", "entities", "sources", "synthesis"]
    for folder in scan_folders:
        folder_path = os.path.join(WIKI_DIR, folder)
        if not os.path.exists(folder_path): continue
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                file_id = file[:-3]
                path = os.path.join(folder_path, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        content = f.read()
                    cursor.execute("INSERT INTO atom_search (file_id, content) VALUES (?, ?)", (file_id, content))
                except:
                    pass
    
    conn.commit()
    conn.close()
    print("  Search index refreshed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wiki Rebuild Utility")
    parser.add_argument("--heal-orphans", action="store_true", help="Auto-heal orphan atoms")
    args = parser.parse_args()

    print(f"--- Wiki Rebuild Start ---")
    sync_db_from_files()
    
    msg = f"Full rebuild completed at {datetime.now()}"
    if args.heal_orphans:
        refresh_search_index()
        healed = heal_orphans()
        msg += f" (Healed {healed} orphans)"
        
    run_indexer()
    log_rebuild(msg)
    print(f"--- Wiki Rebuild Completed ---")

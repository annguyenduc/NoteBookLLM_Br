import os
import sqlite3
import subprocess
import sys
import argparse
from datetime import datetime
import re
import hashlib

# Fix encoding for Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.getenv("WIKI_ROOT_PATH", os.path.join(ROOT_DIR, "3-resources", "wiki"))
DB_PATH  = os.getenv("WIKI_DB_PATH", os.path.join(WIKI_DIR, "wiki_brain.db"))
SCRIPTS_DIR = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-rebuild", "scripts")

def sync_db_from_files():
    print("Syncing Database with File System...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    files_on_disk = set()
    scan_folders = ["concepts", "entities", "sources", "synthesis", "decisions", "review_queue", "session_insights"]
    for folder in scan_folders:
        path = os.path.join(WIKI_DIR, folder)
        if os.path.exists(path):
            for f in os.listdir(path):
                if f.endswith(".md"):
                    file_path = os.path.join(path, f)
                    
                    # [V2.0] R11: No auto-stub creation (< 200 bytes)
                    if os.path.getsize(file_path) < 200:
                        continue
                    
                    # [V2.0] R11: Skip files without valid frontmatter
                    try:
                        with open(file_path, "r", encoding="utf-8-sig") as file_obj:
                            content = file_obj.read().lstrip()
                            if not content.startswith("---") or "---" not in content[3:]:
                                continue
                            
                            # [V2.1] Chỉ trích xuất từ khối Frontmatter thực sự
                            file_id_from_fm = None
                            title = f[:-3].replace("_", " ")
                            status = "DRAFT"
                            
                            fm_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)
                            if fm_match:
                                fm_content = fm_match.group(1)
                                fid_m = re.search(r"^file_id:\s*(.*)$", fm_content, re.MULTILINE)
                                if fid_m: file_id_from_fm = fid_m.group(1).strip().strip('"\'')
                                
                                title_m = re.search(r"^title:\s*(.*)$", fm_content, re.MULTILINE)
                                if title_m: title = title_m.group(1).strip().strip('"\'')
                                
                                status_m = re.search(r"^status:\s*(.*)$", fm_content, re.MULTILINE)
                                if status_m: status = status_m.group(1).strip().strip('"\'')
                            
                            # [V2.2] Determine type from folder name
                            type_map = {
                                "concepts": "Concept",
                                "entities": "Entity",
                                "sources": "Source",
                                "synthesis": "Synthesis",
                                "decisions": "Decision",
                                "review_queue": "Review",
                                "session_insights": "Insight"
                            }
                            atom_type = type_map.get(folder, folder.capitalize())
                            
                            actual_fid = file_id_from_fm if file_id_from_fm else f[:-3]
                                
                            # Tính toán File Hash
                            file_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
                            
                            # Cập nhật hoặc Thêm mới (Case-insensitive check)
                            cursor.execute("SELECT file_id FROM atoms WHERE UPPER(file_id) = UPPER(?)", (actual_fid,))
                            existing = cursor.fetchone()
                            if existing:
                                db_fid = existing[0]
                                # [V2.0] Reset human_review_flag if human has verified/synthesized in Obsidian
                                new_flag = 0 if status.upper() in ['VERIFIED', 'SYNTHESIZED'] else None
                                if new_flag == 0:
                                    cursor.execute("UPDATE atoms SET title = ?, status = ?, type = ?, file_hash = ?, human_review_flag = 0 WHERE file_id = ?", (title, status, atom_type, file_hash, db_fid))
                                else:
                                    cursor.execute("UPDATE atoms SET title = ?, status = ?, type = ?, file_hash = ? WHERE file_id = ?", (title, status, atom_type, file_hash, db_fid))
                                files_on_disk.add(db_fid)
                            else:
                                cursor.execute("INSERT INTO atoms (file_id, title, type, status, file_hash) VALUES (?, ?, ?, ?, ?)", (actual_fid, title, atom_type, status, file_hash))
                                files_on_disk.add(actual_fid)
                    except Exception as e:
                        print(f"Error indexing {f}: {e}")
                        continue
    
    cursor.execute("SELECT file_id FROM atoms")
    db_files = {r[0] for r in cursor.fetchall()}
    
    # [V2.0] Handle Deletions: Files in DB but missing on disk
    deleted_from_disk = db_files - files_on_disk
    if deleted_from_disk:
        # Filter out DEPRECATED atoms that are truly deleted
        to_deprecate = []
        for fid in deleted_from_disk:
            # Check if it's already DEPRECATED
            cursor.execute("SELECT status FROM atoms WHERE file_id = ?", (fid,))
            res = cursor.fetchone()
            if res and res[0] != 'DEPRECATED':
                to_deprecate.append(fid)
        
        if to_deprecate:
            print(f"  Found {len(to_deprecate)} atoms whose files are missing on disk. Marking as DEPRECATED.")
            for fid in to_deprecate:
                cursor.execute("UPDATE atoms SET status = 'DEPRECATED' WHERE file_id = ?", (fid,))
    
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
        # Bao bọc fid trong dấu ngoặc kép để tránh lỗi cú pháp FTS5
        quoted_fid = f'"{fid}"'
        try:
            matches = cursor.execute("""
                SELECT file_id FROM atom_search 
                WHERE content MATCH ? AND file_id != ?
            """, (quoted_fid, fid)).fetchall()
            
            for (source_id,) in matches:
                # 3. Tạo cạnh MENTIONS
                cursor.execute("""
                    INSERT OR IGNORE INTO edges (source_id, target_id, edge_type, confidence)
                    VALUES (?, ?, 'MENTIONS', 0.5)
                """, (source_id, fid))
                healed_count += 1
        except Exception as e:
            # print(f"Error healing {fid}: {e}")
            pass
            
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
    scan_folders = ["concepts", "entities", "sources", "synthesis", "decisions", "review_queue", "session_insights"]
    for folder in scan_folders:
        folder_path = os.path.join(WIKI_DIR, folder)
        if not os.path.exists(folder_path): continue
        for file in os.listdir(folder_path):
            if file.endswith(".md"):
                file_id = file[:-3]
                path = os.path.join(folder_path, file)
                try:
                    with open(path, "r", encoding="utf-8-sig") as f:
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

    # R8 Compliance: Auto-scan sau rebuild
    print("\n[REBUILD] Running R8 Compliance scan...")
    subprocess.run(
        [sys.executable,
         os.path.join(ROOT_DIR, "scripts", "maintenance", "synthesis_guard.py"),
         "scan"],
        capture_output=False
    )

    print(f"--- Wiki Rebuild Completed ---")

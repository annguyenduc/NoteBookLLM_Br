import sys
import os
import json
import sqlite3
import subprocess
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
HEALTH_SCRIPT = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-status", "scripts", "vault_health.py")

def get_db_stats():
    stats = {}
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 1. Status distribution
        cursor.execute("SELECT status, COUNT(*) FROM atoms GROUP BY status")
        stats["status_dist"] = dict(cursor.fetchall())
        
        # 2. Total atoms & edges
        stats["total_atoms"] = conn.execute("SELECT COUNT(*) FROM atoms").fetchone()[0]
        stats["total_edges"] = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        
        # 3. Latest logs
        cursor.execute("SELECT action, status, details, timestamp FROM task_logs ORDER BY timestamp DESC LIMIT 5")
        stats["recent_logs"] = cursor.fetchall()
        
        conn.close()
    except Exception as e:
        stats["error"] = str(e)
    return stats

def get_health_stats():
    try:
        result = subprocess.run(
            [sys.executable, HEALTH_SCRIPT, "--path", ROOT_DIR, "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
        else:
            return {"error": result.stderr}
    except Exception as e:
        return {"error": str(e)}

def print_dashboard():
    print(f"\n" + "="*70)
    print(f"  WIKI 2.0 STATUS DASHBOARD — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    db = get_db_stats()
    health = get_health_stats()
    
    if "error" in db or "error" in health:
        print(f"  [ERROR] Database: {db.get('error', 'OK')}")
        print(f"  [ERROR] Health: {health.get('error', 'OK')}")
        return

    # --- Section 1: Quantitative Infrastructure ---
    print(f"\n  [1] Hạ tầng tri thức")
    print(f"  - Tổng số Atoms:     {db['total_atoms']} (Scanned: {health['total_notes']})")
    print(f"  - Tổng số Liên kết:  {db['total_edges']} (FS Links: {health['total_links']})")
    print(f"  - Mật độ đồ thị:     {health['link_density']} (Mục tiêu: > 3.0)")
    
    # --- Section 2: Quality & Verification ---
    print(f"\n  [2] Chất lượng & Xác thực")
    dist = db["status_dist"]
    verified = dist.get("VERIFIED", 0) + dist.get("SYNTHESIZED", 0)
    total = db["total_atoms"]
    v_rate = (verified / total * 100) if total > 0 else 0
    
    print(f"  - Tỷ lệ xác thực:    {v_rate:.1f}%")
    for status, count in dist.items():
        icon = "✅" if status in ["VERIFIED", "SYNTHESIZED"] else "📝"
        print(f"    {icon} {status:<12}: {count}")
    
    # --- Section 3: Issues & Maintenance ---
    print(f"\n  [3] Vấn đề tồn đọng (Structural)")
    for label, count in health["counts"].items():
        icon = "⚠️" if count > 0 else "✨"
        print(f"    {icon} {label:<12}: {count}")
        
    # --- Section 4: Activity Feed ---
    print(f"\n  [4] Hoạt động gần đây")
    for act, status, det, ts in db["recent_logs"]:
        icon = "🟢" if status == "success" else "🔴"
        print(f"    {ts[11:16]} | {icon} {act:<10} | {det[:45]}...")

    print("\n" + "="*70)

if __name__ == "__main__":
    print_dashboard()

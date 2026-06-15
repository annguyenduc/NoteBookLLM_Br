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

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.getenv("WIKI_ROOT_PATH", os.path.join(ROOT_DIR, "3-resources", "wiki"))
DB_PATH  = os.getenv("WIKI_DB_PATH", os.path.join(WIKI_DIR, "wiki_brain.db"))
HEALTH_SCRIPT = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-status", "scripts", "vault_health.py")
LINT_SCRIPT = os.path.join(ROOT_DIR, ".agent", "skills", "wiki-cleanup", "scripts", "lint_engine.py")


def get_db_stats():
    stats = {}
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("SELECT status, COUNT(*) FROM atoms GROUP BY status")
        stats["status_dist"] = dict(cursor.fetchall())

        stats["total_atoms"] = conn.execute("SELECT COUNT(*) FROM atoms").fetchone()[0]
        stats["total_edges"] = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]

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
        return {"error": result.stderr}
    except Exception as e:
        return {"error": str(e)}


def get_cleanup_broken_links():
    try:
        result = subprocess.run(
            [sys.executable, LINT_SCRIPT, "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return data.get("broken_links")
    except Exception:
        pass
    return None


def print_dashboard():
    print("\n" + "=" * 70)
    print(f"  WIKI 2.0 STATUS DASHBOARD - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    db = get_db_stats()
    health = get_health_stats()
    cleanup_broken = get_cleanup_broken_links()

    if "error" in db or "error" in health:
        print(f"  [ERROR] Database: {db.get('error', 'OK')}")
        print(f"  [ERROR] Health: {health.get('error', 'OK')}")
        return

    print("\n  [1] Ha tang tri thuc")
    print(f"  - Tong so Atoms:     {db['total_atoms']} (Scanned: {health['total_notes']})")
    print(f"  - Tong so Lien ket:  {db['total_edges']} (FS Links: {health['total_links']})")
    print(f"  - Mat do do thi:     {health['link_density']} (Muc tieu: > 3.0)")

    print("\n  [2] Chat luong & Xac thuc")
    dist = db["status_dist"]
    verified = dist.get("VERIFIED", 0) + dist.get("SYNTHESIZED", 0)
    total = db["total_atoms"]
    v_rate = (verified / total * 100) if total > 0 else 0

    print(f"  - Ty le xac thuc:    {v_rate:.1f}%")
    for status, count in dist.items():
        icon = "OK" if status in ["VERIFIED", "SYNTHESIZED"] else "--"
        print(f"    {icon} {status:<12}: {count}")

    print("\n  [3] Van de ton dong (Structural)")
    if cleanup_broken is not None:
        health["counts"]["Broken links"] = cleanup_broken
    for label, count in health["counts"].items():
        icon = "WARN" if count > 0 else "CLEAN"
        print(f"    {icon} {label:<12}: {count}")

    print("\n  [4] Hoat dong gan day")
    for act, status, det, ts in db["recent_logs"]:
        icon = "OK" if status == "success" else "ERR"
        print(f"    {ts[11:16]} | {icon} {act:<10} | {det[:45]}...")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    print_dashboard()

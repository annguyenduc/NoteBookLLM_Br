import os
import sys
import hashlib
import sqlite3
import json
import subprocess
import argparse
from datetime import datetime
ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
DB_PATH = os.getenv("WIKI_DB_PATH", os.path.join(ROOT_DIR, "3-resources", "wiki", "wiki_brain.db"))
RAW_DIR = os.path.join(ROOT_DIR, "3-resources", "raw")
def has_audit_stamp(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="replace") as f:
            header = f.read(1024)
            return "audit_stamp: true" in header and "audit:" in header
    except Exception:
        return False


def validate_package_dir(package_path):
    package_path = os.path.normpath(os.path.abspath(package_path))
    if not os.path.isdir(package_path):
        return False, "Package path is not a directory."

    manifest_path = os.path.join(package_path, "manifest.md")
    chunks_dir = os.path.join(package_path, "chunks")
    if not os.path.exists(manifest_path):
        return False, "Package manifest.md is missing."
    if not os.path.isdir(chunks_dir):
        return False, "Package chunks/ directory is missing."

    chunk_files = sorted(
        os.path.join(chunks_dir, name)
        for name in os.listdir(chunks_dir)
        if name.startswith("RAW_") and name.lower().endswith(".md")
    )
    if not chunk_files:
        return False, "Package chunks/ contains no RAW_*.md files."

    missing_chunk_audit = [path for path in chunk_files if not has_audit_stamp(path)]
    if missing_chunk_audit:
        return False, f"Chunk missing valid audit block: {os.path.basename(missing_chunk_audit[0])}"

    return True, {"manifest_path": manifest_path, "chunks_dir": chunks_dir, "chunk_files": chunk_files}

def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def get_routing_info(file_path): 
    router_script = os.path.join(os.path.dirname(__file__), "magika_router.py")
    result = subprocess.run(
        [sys.executable, router_script, file_path],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        return json.loads(result.stdout)
    return None

def ingest_file(file_path, learning=False, audit_required=True):
    print(f"--- Ingesting: {file_path} ---")
    
    # [Task 2B] Security Gate: audit_stamp check for Markdown files
    if audit_required and file_path.lower().endswith(".md"):
        try:
            if not has_audit_stamp(file_path):
                print(f"WARNING: [Security Violation] Missing valid audit block in {file_path}. Skipping.")
                return False
            print("SUCCESS: Audit stamp verified.")
        except Exception as e:
            print(f"ERROR: Failed to read audit stamp: {e}")
            return False

    # Normalize path for comparison
    file_path = os.path.normpath(os.path.abspath(file_path))
    raw_dir_norm = os.path.normpath(os.path.abspath(RAW_DIR))
    
    if not os.path.exists(file_path):
        print(f"ERROR: File not found {file_path}")
        return False

    # 1. Gate -1: Routing
    routing = get_routing_info(file_path)
    if not routing or "error" in routing:
        print(f"ERROR: Routing failed: {routing}")
        return False
    
    print(f"MIME: {routing['mime_type']} | Parser: {routing['parser']}")

    # [V2.0] R11: No auto-stub creation (< 200 bytes)
    # Stub files in 00_Inbox/ are processed weekly, not indexed immediately.
    if os.path.getsize(file_path) < 200:
        print(f"Info: Skipping stub file {file_path} (< 200 bytes) per R11.")
        return True

    # 1. Calculate Hash
    file_hash = calculate_hash(file_path)
    print(f"Hash: {file_hash}")

    # 2. Check Database for duplicates or modified raw
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute("PRAGMA busy_timeout = 30000")
    # Lock early so duplicate checks and insert become one atomic write window.
    conn.execute("BEGIN IMMEDIATE")
    cursor = conn.cursor()
    
    # Check if this exact path is already in atoms (normalize stored paths if possible, but here we assume stored paths were normalized)
    cursor.execute("SELECT file_hash, status FROM atoms WHERE file_id = ?", (file_path,))
    existing_atom = cursor.fetchone()
    
    # R1 & R9: Check if file in raw/ has been modified
    # Case-insensitive check for Windows
    is_in_raw = file_path.lower().startswith(raw_dir_norm.lower())
    
    if is_in_raw and existing_atom:
        if existing_atom[0] != file_hash:
            msg = f"WARNING: [R1 Violation] Raw file modified! Expected {existing_atom[0]}, got {file_hash}"
            print(msg)
            print("Action: Rejected ingestion to protect IMMUTABLE raw source.")
            cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                           ('@engineer', 'ingest', file_path, 'rejected', msg))
            conn.commit()
            conn.close()
            return False
        else:
            print("Info: File already ingested and matches hash. Skipping.")
            cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                           ('@engineer', 'ingest', file_path, 'skipped', 'Hash matches existing atom'))
            conn.commit()
            conn.close()
            return True

    # Check for duplicates by hash across all files
    cursor.execute("SELECT file_id FROM atoms WHERE file_hash = ?", (file_hash,))
    duplicate = cursor.fetchone()
    if duplicate:
        print(f"Info: Duplicate content detected (same hash as {duplicate[0]}). Skipping.")
        cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                       ('@engineer', 'ingest', file_path, 'skipped', f"Duplicate of {duplicate[0]}"))
        conn.commit()
        conn.close()
        return True

    # 3. Gate -1: Routing
    routing = get_routing_info(file_path)
    if not routing or "error" in routing:
        print(f"ERROR: Routing failed: {routing}")
        conn.close()
        return False
    
    print(f"MIME: {routing['mime_type']} | Parser: {routing['parser']}")
    if routing.get("mime_type") == "unknown" or routing.get("parser") == "unknown":
        msg = "Routing unresolved (unknown mime/parser). Rejected for safety."
        print(f"ERROR: {msg}")
        cursor.execute(
            "INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
            ('@engineer', 'ingest', file_path, 'rejected', msg)
        )
        conn.commit()
        conn.close()
        return False

    # 4. Gate 0: Atomic Creation
    # Confidence logic via score_engine
    from score_engine import compute_confidence
    
    # Infer some metadata for scoring
    source_type = "web_scrape" if "web" in file_path.lower() else "official_doc"
    if is_in_raw:
        source_type = "personal_note" if "personal" in file_path.lower() else "official_doc"
    
    domain = "default"
    if "ai" in file_path.lower() or "ml" in file_path.lower():
        domain = "AI_ML"
    
    # Read content for semantic scoring
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(2000) # Sample content
    except:
        content = ""

    atom_data = {
        "file_id": file_path,
        "source_type": source_type,
        "domain": domain,
        "content": content,
        "created_at": datetime.now().isoformat()
    }
    
    confidence = compute_confidence(atom_data, conn)
    print(f"Confidence (Score Engine): {confidence}")

    title = os.path.basename(file_path)
    file_type = "source" # Default for ingestion
    
    try:
        learning_flag = 1 if learning else 0
        # Insert into atoms
        cursor.execute("""
            INSERT INTO atoms (file_id, title, type, status, confidence, learning_source, file_hash, agent_id)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (file_path, title, file_type, 'DRAFT', confidence, learning_flag, file_hash, '@engineer'))
        
        # Insert into review_queue
        cursor.execute("INSERT INTO review_queue (item_id, reason) VALUES (?, ?)", 
                       (file_path, f"New ingest: {routing['mime_type']}"))
        
        # Log the task
        cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                       ('@engineer', 'ingest', file_path, 'success', f"MIME: {routing['mime_type']}"))
        
        # 5. [V2.0] Post-Ingest Gate: Automatic Audit for raw_ingest promotion
        if "3-resources" in file_path and "raw_ingest" in file_path:
            audit_script = os.path.join(ROOT_DIR, "scripts", "maintenance", "audit_raw_ingest.py")
            print(f"--- Running Post-Ingest Audit for: {title} ---")
            result = subprocess.run(
                [sys.executable, audit_script, "--file", file_path],
                capture_output=True,
                text=True
            )
            print(result.stdout)
            if result.returncode != 0:
                print("WARNING: Post-Ingest Audit FAILED. Content needs remediation.")
            else:
                print("SUCCESS: Post-Ingest Audit PASSED.")

        conn.commit()
        print(f"SUCCESS: Atom created in DRAFT status. Added to review_queue.")
        
    except Exception as e:

        print(f"ERROR: Database update failed: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest a file or package into the Wiki.")
    parser.add_argument("file_path", nargs="?", help="Path to the file to ingest")
    parser.add_argument("--package", help="Path to the package directory to ingest")
    parser.add_argument("--learning", action="store_true", default=False, help="Mark as learning source")
    args = parser.parse_args()

    if args.package:
        ok, payload = validate_package_dir(args.package)
        if not ok:
            print(f"ERROR: Invalid package: {payload}")
            sys.exit(1)
        print(f"SUCCESS: Package manifest resolved: {payload['manifest_path']}")
        print(f"SUCCESS: Package chunks resolved: {len(payload['chunk_files'])}")
        success = ingest_file(payload["manifest_path"], learning=args.learning, audit_required=False)
        sys.exit(0 if success else 1)

    if not args.file_path:
        parser.error("file_path is required when --package is not used")

    success = ingest_file(args.file_path, learning=args.learning)
    sys.exit(0 if success else 1)

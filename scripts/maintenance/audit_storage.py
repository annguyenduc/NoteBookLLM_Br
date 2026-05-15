"""
audit_storage.py — Wiki Storage Integrity Auditor
=================================================
Scans raw directories for unauthorized or malformed files.

Rules:
1. Every Markdown in raw_ingest must have a valid 'PASSED' audit stamp.
2. Every file in raw_* should (ideally) be referenced in a promote log (Future enhancement).
3. Files failing audit are moved to 00_Inbox/Rejected/<date>/.

Usage:
  python scripts/maintenance/audit_storage.py [--fix]
"""

import os
import re
import shutil
import pathlib
from datetime import datetime

# --- CONFIGURATION ---
REPO_ROOT = pathlib.Path(__file__).parent.parent.parent
RAW_INGEST = REPO_ROOT / "3-resources" / "raw_ingest"
RAW_SOURCES = REPO_ROOT / "3-resources" / "raw_sources"
RAW_ASSETS = REPO_ROOT / "3-resources" / "raw_assets"
ARCHIVE_ROOT = REPO_ROOT / "4-archive"
REJECTED_DIR = ARCHIVE_ROOT / "rejected" / datetime.now().strftime("%Y-%m-%d")

def check_audit_stamp(md_path):
    """Verifies if the MD file has a PASSED audit stamp."""
    try:
        content = md_path.read_text(encoding="utf-8")
        # Look for the audit block in YAML
        if "status: \"PASSED\"" in content or "status: PASSED" in content:
            return True
        return False
    except Exception:
        return False

def audit_directory():
    print(f"--- Storage Audit Started: {datetime.now().isoformat()} ---")
    
    unauthorized_files = []

    # 1. Audit raw_ingest (Markdown files)
    if RAW_INGEST.exists():
        for md_file in RAW_INGEST.glob("*.md"):
            if not check_audit_stamp(md_file):
                print(f"[AUDIT] FAILED: {md_file.name} (Missing/Invalid Audit Stamp)")
                unauthorized_files.append(md_file)
            else:
                print(f"[AUDIT] VALID: {md_file.name}")

    # 2. Results
    if not unauthorized_files:
        print("\n[RESULT] Integrity Check: GREEN. All files in raw_ingest are verified.")
        return True
    
    print(f"\n[RESULT] Integrity Check: RED. Found {len(unauthorized_files)} unauthorized files.")
    
    # 3. Auto-fix (Move to Rejected)
    REJECTED_DIR.mkdir(parents=True, exist_ok=True)
    for f in unauthorized_files:
        dest = REJECTED_DIR / f.name
        print(f"[FIX] Moving {f.name} -> {dest.relative_to(REPO_ROOT)}")
        shutil.move(str(f), str(dest))
    
    return False

if __name__ == "__main__":
    audit_directory()

import os
import subprocess
import sqlite3
import shutil

# Paths
BASE_DIR = r"d:\NoteBookLLM_Br"
INGEST_SCRIPT = os.path.join(BASE_DIR, ".agent/skills/wiki-ingest/scripts/ingest.py")
RAW_DIR = os.path.join(BASE_DIR, "3-resources/raw/sources")
SCRATCH_DIR = os.path.join(BASE_DIR, "scratch/test_ingest")
DB_PATH = os.path.join(BASE_DIR, "3-resources/wiki/wiki_brain.db")

def setup():
    if os.path.exists(SCRATCH_DIR):
        shutil.rmtree(SCRATCH_DIR)
    os.makedirs(SCRATCH_DIR)
    
    # Clean DB
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM atoms WHERE file_id LIKE '%test_ingest%' OR file_id LIKE '%test_immutable%'")
    cursor.execute("DELETE FROM task_logs WHERE target_file LIKE '%test_ingest%' OR target_file LIKE '%test_immutable%'")
    conn.commit()
    conn.close()
    print("Database cleaned for test.")

import sys

def run_ingest(file_path):
    result = subprocess.run(
        [sys.executable, INGEST_SCRIPT, file_path],
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr

def test_pressure():
    print("=== STARTING PRESSURE TEST FOR WIKI-INGEST ===")
    
    # 1. File .pdf không có text (Empty PDF)
    pdf_path = os.path.join(SCRATCH_DIR, "empty.pdf")
    with open(pdf_path, "wb") as f:
        f.write(b"%PDF-1.4\n%EOF") # Minimal PDF
    
    print("\n[Test 1] Image-only/Empty PDF")
    out, err = run_ingest(pdf_path)
    print(out)
    if "MIME: application/pdf" in out and "Parser: docling" in out:
        print("PASS: Correctly routed to docling.")
    else:
        print("FAIL: Incorrect routing.")

    # 2. File .md với source unknown (Outside raw/)
    md_path = os.path.join(SCRATCH_DIR, "outside.md")
    with open(md_path, "w") as f:
        f.write("# Unknown Source Content")
    
    print("\n[Test 2] Unknown source (Outside raw/)")
    out, err = run_ingest(md_path)
    print(out)
    if "Setting confidence to 0.20" in out:
        print("PASS: Confidence lowered for unknown source.")
    else:
        print("FAIL: Confidence logic error.")

    # 3. File duplicate (Hash trùng)
    print("\n[Test 3] Duplicate content detection")
    out, err = run_ingest(md_path) # Ingest same file again
    print(out)
    if "Duplicate content detected" in out or "Skipping" in out:
        print("PASS: Duplicate ignored.")
    else:
        print("FAIL: Duplicate ingested.")

    # 4. File trong raw/ bị modify
    # First, ingest a clean file in raw/
    raw_file = os.path.join(RAW_DIR, "test_immutable.md")
    with open(raw_file, "w") as f:
        f.write("Original content")
    
    print("\n[Test 4] R1 Violation (Modified Raw)")
    run_ingest(raw_file) # Initial ingest
    
    # Modify it
    with open(raw_file, "w") as f:
        f.write("Modified content")
    
    out, err = run_ingest(raw_file)
    print(out)
    if "R1 Violation" in out and "Rejected ingestion" in out:
        print("PASS: Blocked modification of raw source.")
    else:
        print("FAIL: Allowed modification of raw source.")
        
    # Cleanup
    if os.path.exists(raw_file):
        os.remove(raw_file)

if __name__ == "__main__":
    setup()
    test_pressure()

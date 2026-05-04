import sqlite3
import os
import subprocess
import sys
import shutil

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"
RECONCILER_SCRIPT = r"d:\NoteBookLLM_Br\.agent\skills\wiki-absorb\scripts\reconciler.py"

def setup_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Clean up test data
    cursor.execute("DELETE FROM atoms WHERE file_id LIKE '%test_absorb%'")
    cursor.execute("DELETE FROM edges WHERE source_id LIKE '%test_absorb%' OR target_id LIKE '%test_absorb%'")
    cursor.execute("DELETE FROM review_queue WHERE item_id LIKE '%test_absorb%'")
    cursor.execute("DELETE FROM task_logs WHERE agent_id = 'wiki-absorb'")
    
    # 1. Existing atom for comparison
    cursor.execute("""
        INSERT INTO atoms (file_id, title, type, status, confidence, file_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("test_absorb_existing_1", "Concept Conflict", "concept", "VERIFIED", 0.95, "hash_original"))

    # 2. Additive DRAFT
    cursor.execute("""
        INSERT INTO atoms (file_id, title, type, status, confidence, file_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("test_absorb_draft_additive", "New Unique Concept", "concept", "DRAFT", 0.90, "hash_unique"))

    # 3. Duplicate DRAFT
    cursor.execute("""
        INSERT INTO atoms (file_id, title, type, status, confidence, file_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("test_absorb_draft_duplicate", "Concept Conflict", "concept", "DRAFT", 0.95, "hash_original"))

    # 4. Conflict High Confidence (LLM Resolve)
    cursor.execute("""
        INSERT INTO atoms (file_id, title, type, status, confidence, file_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("test_absorb_draft_conflict_high", "Concept Conflict", "concept", "DRAFT", 0.90, "hash_diff_high"))

    # 5. Conflict Low Confidence (Human Gate)
    cursor.execute("""
        INSERT INTO atoms (file_id, title, type, status, confidence, file_hash)
        VALUES (?, ?, ?, ?, ?, ?)
    """, ("test_absorb_draft_conflict_low", "Concept Conflict", "concept", "DRAFT", 0.60, "hash_diff_low"))

    conn.commit()
    conn.close()
    print("Test database setup complete.")

def run_reconcile():
    result = subprocess.run(
        [sys.executable, RECONCILER_SCRIPT],
        capture_output=True,
        text=True
    )
    return result.stdout, result.stderr

def verify():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    print("\n=== VERIFICATION RESULTS ===")
    
    # 1. Test ADDITIVE
    cursor.execute("SELECT status FROM atoms WHERE file_id = 'test_absorb_draft_additive'")
    status = cursor.fetchone()[0]
    print(f"[Test 1] ADDITIVE -> {status} (Expected: VERIFIED) -> {'PASS' if status == 'VERIFIED' else 'FAIL'}")

    # 2. Test DUPLICATE
    cursor.execute("SELECT COUNT(*) FROM atoms WHERE file_id = 'test_absorb_draft_duplicate'")
    count = cursor.fetchone()[0]
    print(f"[Test 2] DUPLICATE deleted -> {count} (Expected: 0) -> {'PASS' if count == 0 else 'FAIL'}")

    # 3. Test LLM Resolve (High Confidence)
    cursor.execute("SELECT status FROM atoms WHERE file_id = 'test_absorb_draft_conflict_high'")
    status = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM edges WHERE source_id = 'test_absorb_draft_conflict_high' AND edge_type = 'SUPERSEDES'")
    edge_count = cursor.fetchone()[0]
    print(f"[Test 3] LLM RESOLVE -> {status}, Edge: {edge_count} (Expected: VERIFIED, 1) -> {'PASS' if status == 'VERIFIED' and edge_count > 0 else 'FAIL'}")

    # 4. Test Human Gate (Low Confidence)
    cursor.execute("SELECT human_review_flag FROM atoms WHERE file_id = 'test_absorb_draft_conflict_low'")
    flag = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM review_queue WHERE item_id = 'test_absorb_draft_conflict_low'")
    queue_count = cursor.fetchone()[0]
    print(f"[Test 4] HUMAN GATE -> Flag: {flag}, Queue: {queue_count} (Expected: 1, 1) -> {'PASS' if flag == 1 and queue_count == 1 else 'FAIL'}")

    # 5. Guard Test (No SYNTHESIZED)
    cursor.execute("SELECT COUNT(*) FROM atoms WHERE status = 'SYNTHESIZED' AND file_id LIKE '%test_absorb%'")
    synth_count = cursor.fetchone()[0]
    print(f"[Test 5] Status Guard -> SYNTHESIZED: {synth_count} (Expected: 0) -> {'PASS' if synth_count == 0 else 'FAIL'}")

    conn.close()

if __name__ == "__main__":
    setup_db()
    out, err = run_reconcile()
    print(out)
    if err: print("Errors:", err)
    verify()

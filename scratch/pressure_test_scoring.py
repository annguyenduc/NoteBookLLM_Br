import sys
import os
import sqlite3
from datetime import datetime, timedelta

# Add script path to sys.path
sys.path.append(os.path.join(os.getcwd(), ".agent", "skills", "wiki-ingest", "scripts"))
from score_engine import compute_confidence

def run_pressure_tests():
    # Setup mock DB or temporary DB
    db_path = "scratch/test_scoring.db"
    if os.path.exists(db_path): os.remove(db_path)
    conn = sqlite3.connect(db_path)
    conn.execute("CREATE TABLE edges (target_id TEXT, type TEXT)")
    
    print("--- Pressure Test: score_engine ---")
    
    # 1. personal_note + age=0 days -> score gần 1.0
    atom1 = {
        "file_id": "note_1.md",
        "source_type": "personal_note",
        "created_at": datetime.now().isoformat(),
        "domain": "concept",
        "content": "A very detailed personal note about something important."
    }
    score1 = compute_confidence(atom1, conn)
    print(f"Test 1 (Personal Fresh): {score1} (Target: ~1.0)")
    
    # 2. web_scrape + age=400 days (domain=AI_ML) -> score thấp < 0.4
    created_at_2 = (datetime.now() - timedelta(days=400)).isoformat()
    atom2 = {
        "file_id": "web_old.md",
        "source_type": "web_scrape",
        "created_at": created_at_2,
        "domain": "AI_ML",
        "content": "Outdated AI news from a year ago."
    }
    score2 = compute_confidence(atom2, conn)
    print(f"Test 2 (Web Old AI_ML): {score2} (Target: < 0.4)")
    
    # 3. unknown source + 2 contradictions -> score < 0.3 -> auto flag
    atom3 = {
        "file_id": "unknown_conflict.md",
        "source_type": "unknown",
        "created_at": datetime.now().isoformat(),
        "domain": "default",
        "content": "Highly suspicious and unverified claim."
    }
    # Add 2 contradictions in DB
    conn.execute("INSERT INTO edges (target_id, type) VALUES (?, ?)", ("unknown_conflict.md", "CONTRADICTS"))
    conn.execute("INSERT INTO edges (target_id, type) VALUES (?, ?)", ("unknown_conflict.md", "CONTRADICTS"))
    conn.commit()
    
    score3 = compute_confidence(atom3, conn)
    print(f"Test 3 (Unknown Conflict): {score3} (Target: < 0.3)")
    
    conn.close()
    if os.path.exists(db_path): os.remove(db_path)

if __name__ == "__main__":
    run_pressure_tests()

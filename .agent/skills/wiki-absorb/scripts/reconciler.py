import os
import sqlite3
import json
from datetime import datetime

DB_PATH = r"d:\NoteBookLLM_Br\3-resources\wiki\wiki_brain.db"
DECISIONS_DIR = r"d:\NoteBookLLM_Br\3-resources\wiki\decisions"
LOG_FILE = r"d:\NoteBookLLM_Br\3-resources\wiki\log.md"

def log_wiki(agent, action, file_path, reason):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = f"\n## [{now}] {action.upper()} | {agent} | {reason}\n- File: {file_path}\n- Lý do: {reason}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def log_task(cursor, action, target_file, status, details):
    cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                   ('wiki-absorb', action, target_file, status, details))

def reconcile():
    if not os.path.exists(DECISIONS_DIR):
        os.makedirs(DECISIONS_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Get DRAFT atoms
    cursor.execute("SELECT file_id, title, file_hash, confidence, metadata FROM atoms WHERE status='DRAFT'")
    drafts = cursor.fetchall()
    
    if not drafts:
        print("No DRAFT atoms found.")
        conn.close()
        return

    for draft_id, title, draft_hash, confidence, metadata_json in drafts:
        print(f"\n--- Reconciling: {title} ({draft_id}) ---")
        
        # Check for existing atoms with same title (excluding itself)
        cursor.execute("SELECT file_id, file_hash, status, confidence FROM atoms WHERE title = ? AND file_id != ?", (title, draft_id))
        existing = cursor.fetchall()
        
        if not existing:
            # TIER 1: ADDITIVE
            print(f"Status: ADDITIVE. Upgrading to VERIFIED.")
            cursor.execute("UPDATE atoms SET status = 'VERIFIED' WHERE file_id = ?", (draft_id,))
            log_task(cursor, 'reconcile', draft_id, 'success', 'ADDITIVE: No existing atom with same title.')
            log_wiki('@engineer', 'UPDATE', draft_id, 'Auto-merged as ADDITIVE.')
            continue

        # Check for DUPLICATE/EXACT
        is_duplicate = False
        for ext_id, ext_hash, ext_status, ext_conf in existing:
            if ext_hash == draft_hash:
                print(f"Status: DUPLICATE of {ext_id}. Skipping.")
                cursor.execute("DELETE FROM atoms WHERE file_id = ?", (draft_id,))
                log_task(cursor, 'reconcile', draft_id, 'skipped', f'DUPLICATE: Same hash as {ext_id}')
                is_duplicate = True
                break
        
        if is_duplicate:
            continue

        # TIER 2 & 3: CONTRADICTS (Same title, different content)
        print(f"Status: CONTRADICTS found ({len(existing)} candidates).")
        
        if confidence >= 0.85:
            # TIER 2: LLM Resolve (Heuristic: Newest with high confidence supersedes)
            # In a real system, we'd call LLM here. For now, we follow instructions to set status = VERIFIED
            # and create SUPERSEDES edge.
            print("Action: LLM Resolve (Confidence >= 0.85). Superseding old versions.")
            cursor.execute("UPDATE atoms SET status = 'VERIFIED' WHERE file_id = ?", (draft_id,))
            
            for ext_id, _, _, _ in existing:
                # Create edge: draft SUPERSEDES existing
                cursor.execute("INSERT OR IGNORE INTO edges (source_id, target_id, edge_type) VALUES (?, ?, ?)",
                               (draft_id, ext_id, 'SUPERSEDES'))
                print(f"Edge created: {draft_id} SUPERSEDES {ext_id}")

            log_task(cursor, 'reconcile', draft_id, 'success', f'LLM_RESOLVED: Superseded {len(existing)} atoms.')
            log_wiki('@engineer', 'UPDATE', draft_id, f'LLM Resolve: Superseded {len(existing)} older versions.')

        else:
            # TIER 3: Human Gate (Confidence < 0.85)
            print("Action: Flagging for Human Review (Confidence < 0.85).")
            cursor.execute("UPDATE atoms SET human_review_flag = 1 WHERE file_id = ?", (draft_id,))
            
            # Create decision file
            decision_id = f"DECISION_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.path.basename(draft_id)}"
            decision_path = os.path.join(DECISIONS_DIR, decision_id + ".md")
            
            with open(decision_path, "w", encoding="utf-8") as f:
                f.write(f"# Conflict Decision Required: {title}\n\n")
                f.write(f"- **Draft Atom**: [{draft_id}]({draft_id})\n")
                f.write(f"- **Confidence**: {confidence}\n")
                f.write(f"- **Conflicts with**:\n")
                for ext_id, _, status, conf in existing:
                    f.write(f"  - [{ext_id}]({ext_id}) (Status: {status}, Confidence: {conf})\n")
                f.write("\n## Reason\nConflict detected with low confidence source. Manual reconciliation required.\n")

            # Add to review_queue
            cursor.execute("INSERT INTO review_queue (item_id, reason) VALUES (?, ?)",
                           (draft_id, f"Conflict with {len(existing)} existing atoms. See {decision_id}.md"))
            
            log_task(cursor, 'reconcile', draft_id, 'flagged', f'HUMAN_GATE: Decision file {decision_id}.md created.')
            log_wiki('@engineer', 'FLAG', draft_id, 'Conflict detected, moved to review_queue.')

    conn.commit()
    conn.close()
    print("\nReconciliation complete.")

if __name__ == "__main__":
    reconcile()

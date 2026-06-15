import os
import sys
import sqlite3
import json
from datetime import datetime

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.getenv(
    "NOTEBOOKLLM_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
)
WIKI_DIR = os.path.join(ROOT_DIR, "3-resources", "wiki")
DB_PATH = os.path.join(WIKI_DIR, "wiki_brain.db")
DECISIONS_DIR = os.path.join(WIKI_DIR, "decisions")
LOG_FILE = os.path.join(WIKI_DIR, "log.md")

def log_wiki(agent, action, file_path, reason):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_entry = f"\n## [{now}] {action.upper()} | {agent} | {reason}\n- File: {file_path}\n- Lý do: {reason}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)

def log_task(cursor, action, target_file, status, details):
    cursor.execute("INSERT INTO task_logs (agent_id, action, target_file, status, details) VALUES (?, ?, ?, ?, ?)",
                   ('wiki-absorb', action, target_file, status, details))

def get_related_context(cursor, title, exclude_ids):
    """Stage 0: Tìm các Atom liên quan để làm bằng chứng ngoại phạm."""
    print(f"  [~] Stage 0: Đang truy vấn tri thức liên quan cho '{title}'...")
    
    # Tìm theo Title tương đồng (LIKE)
    cursor.execute("""
        SELECT file_id, title, summary, content 
        FROM atoms 
        WHERE (title LIKE ? OR title LIKE ?) AND file_id NOT IN ({}) 
        LIMIT 3
    """.format(','.join(['?']*len(exclude_ids))), (f"%{title}%", f"%{title.split('_')[-1]}%", *exclude_ids))
    
    rows = cursor.fetchall()
    context = []
    for row in rows:
        context.append({
            "file_id": row[0],
            "title": row[1],
            "summary": row[2],
            "content": row[3]
        })
    return context

def reconcile():
    if not os.path.exists(DECISIONS_DIR):
        os.makedirs(DECISIONS_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Get DRAFT atoms
    cursor.execute("SELECT file_id, title, file_hash, confidence, metadata FROM atoms WHERE status LIKE '%DRAFT%'")
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
        
        # Lấy file hiện tại để so sánh (Lấy file đầu tiên nếu có nhiều)
        ext_id = existing[0][0]
        ext_status = existing[0][2]
        ext_conf = existing[0][3]
        
        import sys
        council_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "wiki-council", "scripts"))
        if council_path not in sys.path:
            sys.path.append(council_path)
        import council_engine
        
        try:
            draft_path = draft_id if os.path.isabs(draft_id) else os.path.join(WIKI_DIR, "review_queue", os.path.basename(draft_id))
            if not draft_path.endswith(".md"):
                draft_path += ".md"
            
            if not os.path.exists(draft_path):
                 # Try directly in review_queue
                 draft_path = os.path.join(WIKI_DIR, "review_queue", draft_id + (".md" if not draft_id.endswith(".md") else ""))
                
            with open(draft_path, 'r', encoding='utf-8') as f:
                draft_content = f.read()
                
            # Determine existing file path
            prefix = ext_id.split("_")[0].lower() + "s" # CONCEPT_ -> concepts
            if "entity" in prefix: prefix = "entities"
            elif "source" in prefix: prefix = "sources"
            
            ext_path = os.path.join(WIKI_DIR, prefix, ext_id)
            if not os.path.exists(ext_path) and ext_id.endswith(".md"):
                 # Check if it was without .md
                 pass
            elif not os.path.exists(ext_path) and not ext_id.endswith(".md"):
                 ext_path += ".md"
            
            with open(ext_path, 'r', encoding='utf-8') as f:
                ext_content = f.read()
            
            # Stage 0: Scouting for witnesses
            supporting_context = get_related_context(cursor, title, [draft_id, ext_id])
            if supporting_context:
                print(f"  [+] Tìm thấy {len(supporting_context)} nhân chứng (Atom liên quan).")
                
            print(f"  [+] Triệu tập Hội đồng Wiki xử lý mâu thuẫn:\n      - ATOM A (Hiện tại): {os.path.basename(ext_id)}\n      - ATOM B (Draft Mới): {os.path.basename(draft_id)}")
            
            council_res = council_engine.run_council(
                case_description=f"Xung đột nội dung trên khái niệm: {title}",
                atom_a_content=ext_content,
                atom_b_content=draft_content,
                supporting_context=supporting_context
            )
            decision = council_res['final_decision']
            print(f"  [>] Quyết định từ Hội đồng: {decision}")
            
            if decision == "SUPERSEDES B":
                print("  [>] Bị bác bỏ: ATOM A (hiện tại) ưu việt hơn.")
                cursor.execute("DELETE FROM atoms WHERE file_id = ?", (draft_id,))
                log_task(cursor, 'reconcile', draft_id, 'rejected', f'COUNCIL_DECISION: {ext_id} supersedes draft.')
                log_wiki('@auditor', 'DELETE', draft_id, f'Hội đồng phán quyết: Bị {ext_id} thay thế (SUPERSEDES B).')
                
            elif decision == "SUPERSEDES A":
                print("  [>] Chấp thuận: Draft mới ưu việt hơn, thay thế ATOM A.")
                cursor.execute("UPDATE atoms SET status = 'VERIFIED' WHERE file_id = ?", (draft_id,))
                cursor.execute("INSERT OR IGNORE INTO edges (source_id, target_id, edge_type) VALUES (?, ?, ?)", (draft_id, ext_id, 'SUPERSEDES'))
                log_task(cursor, 'reconcile', draft_id, 'success', f'COUNCIL_DECISION: Draft supersedes {ext_id}.')
                log_wiki('@engineer', 'UPDATE', draft_id, f'Hội đồng phán quyết: Draft thay thế bản cũ (SUPERSEDES A).')
                
            else:
                # Các case phức tạp: MERGE, KEEP BOTH, REJECT BOTH -> Human Review
                print(f"  [>] Quyết định phức tạp ({decision}). Flagging cho Human Review...")
                cursor.execute("UPDATE atoms SET human_review_flag = 1 WHERE file_id = ?", (draft_id,))
                
                decision_id = f"DECISION_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{os.path.basename(draft_id)}"
                decision_path = os.path.join(DECISIONS_DIR, decision_id + ".md")
                
                with open(decision_path, "w", encoding="utf-8") as f:
                    f.write(f"# Conflict Decision Required: {title}\n\n")
                    f.write(f"**Council Decision**: {decision}\n\n")
                    f.write(f"- **Atom A (Existing)**: [{ext_id}]({ext_id})\n")
                    f.write(f"- **Atom B (Draft)**: [{draft_id}]({draft_id})\n\n")
                    f.write(f"## Raw Council Logs\n```json\n{json.dumps(council_res['raw_responses'], indent=2, ensure_ascii=False)}\n```\n")

                cursor.execute("INSERT INTO review_queue (item_id, reason) VALUES (?, ?)",
                               (draft_id, f"Council ruled {decision}. See {decision_id}.md"))
                
                log_task(cursor, 'reconcile', draft_id, 'flagged', f'COUNCIL_DECISION: {decision}.')
                log_wiki('@auditor', 'FLAG', draft_id, f'Hội đồng phán quyết: {decision}. Cần Human can thiệp.')

        except Exception as e:
            print(f"  [!] Lỗi khi chạy Council: {e}")
            cursor.execute("UPDATE atoms SET human_review_flag = 1 WHERE file_id = ?", (draft_id,))
            log_task(cursor, 'reconcile', draft_id, 'error', f'COUNCIL_ERROR: {str(e)}')

    conn.commit()
    conn.close()
    print("\nReconciliation complete.")

if __name__ == "__main__":
    reconcile()

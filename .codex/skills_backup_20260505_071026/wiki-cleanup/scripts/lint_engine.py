import os
import re
import sqlite3
import sys
import argparse
import json
from datetime import datetime, timedelta

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

WIKI_LINK_RE = re.compile(r"\[\[(.*?)\]\]")

def get_all_atoms():
    atoms = {}
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        rows = cursor.execute("SELECT file_id, title FROM atoms").fetchall()
        for r in rows:
            atoms[r[0]] = {"title": r[1]}
        conn.close()
    except Exception as e:
        print(f"Error reading DB: {e}")
    return atoms

def normalize(name):
    """Chuẩn hóa tên để so khớp (lowercase, bỏ gạch dưới, bỏ prefix)."""
    n = name.lower().replace("_", "").replace("-", "")
    prefixes = ["concept", "entity", "source", "query", "synthesis"]
    for p in prefixes:
        if n.startswith(p):
            n = n[len(p):]
    return n

def find_best_match(target, all_file_ids):
    """Tìm file_id tốt nhất cho một broken link target."""
    norm_target = normalize(target)
    
    # 1. Exact case-insensitive match (with common prefixes)
    for fid in all_file_ids:
        if fid.lower() == target.lower():
            return fid
            
    # 2. Normalized match
    matches = []
    for fid in all_file_ids:
        if normalize(fid) == norm_target:
            matches.append(fid)
    
    if len(matches) == 1:
        return matches[0]
        
    # 3. Special case: SOURCE_AIMET_AgenticAI_Roadmap_2026 -> SOURCE_AIMET_AGENTIC_ROADMAP_2026
    if "aimet" in norm_target and "roadmap" in norm_target:
        for fid in all_file_ids:
            if "aimet" in fid.lower() and "roadmap" in fid.lower():
                return fid
                
    return None

def lint_wiki(fix=False):
    atoms = get_all_atoms()
    all_file_ids = list(atoms.keys())
    
    issues = []
    scan_folders = ["concepts", "entities", "sources", "synthesis"]
    
    stats = {"scanned": 0, "fixed": 0}
    
    for folder in scan_folders:
        folder_path = os.path.join(WIKI_DIR, folder)
        if not os.path.exists(folder_path): continue
        
        for file in os.listdir(folder_path):
            if not file.endswith(".md"): continue
            
            file_path = os.path.join(folder_path, file)
            stats["scanned"] += 1
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Broken Links
                matches = WIKI_LINK_RE.findall(content)
                for match in matches:
                    target_part = match.split("|")[0].strip()
                    if target_part and target_part not in all_file_ids:
                        best_match = find_best_match(target_part, all_file_ids)
                        if fix and best_match:
                            new_match = match.replace(target_part, best_match)
                            content = content.replace(f"[[{match}]]", f"[[{new_match}]]")
                            stats["fixed"] += 1
                            print(f"  [FIXED] {file}: [[{target_part}]] -> [[{best_match}]]")
                        else:
                            issues.append({
                                "file": file,
                                "type": "BROKEN_LINK",
                                "details": f"Target: {target_part} (Best guess: {best_match or 'None'})"
                            })
                
                # 2. Template Violation
                if "## 4F Reflection" not in content:
                    if fix:
                        content += "\n\n## 4F Reflection\n- **Facts**: \n- **Feelings**: \n- **Findings**: \n- **Futures**: \n"
                        stats["fixed"] += 1
                        print(f"  [FIXED] {file}: Added 4F Reflection stub")
                    else:
                        issues.append({
                            "file": file,
                            "type": "TEMPLATE_VIOLATION",
                            "details": "Missing 4F Reflection section"
                        })
                
                if fix and content != original_content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                        
            except Exception as e:
                print(f"Error processing {file}: {e}")

    return issues, stats

def report_issues(issues, stats, fix=False):
    if not issues and stats["fixed"] == 0:
        print("No issues found. Steve Jobs is proud!")
        return

    print(f"\n--- LINT REPORT ---")
    print(f"Scanned: {stats['scanned']} files")
    print(f"Fixed:   {stats['fixed']} items")
    print(f"Pending: {len(issues)} issues")
    print("-" * 20)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    for issue in issues:
        print(f"  [{issue['type']}] {issue['file']}: {issue['details']}")
        cursor.execute("""
            INSERT INTO task_logs (agent_id, action, status, details)
            VALUES (?, ?, ?, ?)
        """, ("@auditor", "cleanup", "lint_error", f"{issue['type']}: {issue['file']} - {issue['details']}"))
        
    if stats["fixed"] > 0:
        cursor.execute("""
            INSERT INTO task_logs (agent_id, action, status, details)
            VALUES (?, ?, ?, ?)
        """, ("@auditor", "cleanup", "success", f"Auto-fixed {stats['fixed']} items in Wiki"))
        
    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wiki Cleanup Lint Engine")
    parser.add_argument("--fix", action="store_true", help="Auto-fix issues")
    parser.add_argument("--json", action="store_true", help="Output lint summary as JSON")
    args = parser.parse_args()

    all_issues, stats = lint_wiki(fix=args.fix)
    if args.json:
        broken_links = sum(1 for i in all_issues if i.get("type") == "BROKEN_LINK")
        payload = {
            "scanned": stats["scanned"],
            "fixed": stats["fixed"],
            "pending": len(all_issues),
            "broken_links": broken_links,
        }
        print(json.dumps(payload, ensure_ascii=False))
    else:
        print(f"Starting wiki-cleanup linting (fix={args.fix}) at {datetime.now()}...")
        report_issues(all_issues, stats, fix=args.fix)
        print("Linting completed.")

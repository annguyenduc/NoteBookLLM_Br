import os
import sys
import datetime
import re

# Standard paths
LOG_DIR = r"d:\NoteBookLLM_Br\3-resources\wiki\logs"
WORKSPACE_ROOT = r"d:\NoteBookLLM_Br"

def get_current_log_path():
    today = datetime.date.today().strftime("%Y_%m_%d")
    return os.path.join(LOG_DIR, f"log_{today}.md")

def get_recently_modified_files(minutes=60):
    modified_files = []
    now = datetime.datetime.now()
    delta = datetime.timedelta(minutes=minutes)
    
    # Files to ignore
    today_log = f"log_{datetime.date.today().strftime('%Y_%m_%d')}.md"
    ignore_list = [".agent_busy", ".git", "wiki_brain.db", "session_seal.py", "__pycache__", ".venv", ".obsidian", ".codex", today_log]

    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        # Prune ignored directories
        dirs[:] = [d for d in dirs if not any(ignore in d for ignore in ignore_list)]
        
        for file in files:
            if any(ignore in file for ignore in ignore_list):
                continue
                
            path = os.path.join(root, file)
            try:
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
                if now - mtime < delta:
                    modified_files.append(os.path.relpath(path, WORKSPACE_ROOT))
            except Exception:
                continue
    return modified_files

def check_log_coverage(log_path, modified_files):
    if not os.path.exists(log_path):
        return False, "Daily log file missing!"
        
    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    unlogged_files = []
    for file in modified_files:
        basename = os.path.basename(file)
        rel_dir = os.path.dirname(file).replace("\\", "/")
        
        # Check for specific filename OR batch directory mention
        batch_pattern = f"Normalized all files in {rel_dir}"
        is_logged = basename in content or file in content
        if rel_dir and batch_pattern in content:
            is_logged = True
            
        if not is_logged:
            unlogged_files.append(file)
            
    return unlogged_files

def main():
    print("--- SESSION SEAL: Hard Stop Logging Verification ---")
    log_path = get_current_log_path()
    modified_files = get_recently_modified_files(minutes=120) # Check last 2 hours
    
    if not modified_files:
        print("SUCCESS: No significant changes detected in the last 2 hours.")
        sys.exit(0)
        
    print(f"Detected {len(modified_files)} modified files.")
    unlogged = check_log_coverage(log_path, modified_files)
    
    if unlogged is True: # Header missing case
        print(f"FAILED: {unlogged}")
        sys.exit(1)
    elif unlogged:
        print("FAILED: The following files have been modified but are NOT mentioned in the daily log:")
        for f in unlogged:
            print(f"  - {f}")
        print("\nACTION REQUIRED: Update your daily log with these files before finishing.")
        sys.exit(1)
    else:
        print("SUCCESS: All modified files are documented in the daily log.")
        sys.exit(0)

if __name__ == "__main__":
    main()

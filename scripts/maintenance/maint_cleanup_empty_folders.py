import os
import shutil

def cleanup_deep_structures(root_path, max_depth=3):
    count = 0
    root_path = os.path.abspath(root_path)
    
    # Sweep 1: Delete System Junk in Archive regardless of being empty
    for root, dirs, files in os.walk(root_path, topdown=True):
        rel_path = os.path.relpath(root, root_path)
        if rel_path == ".":
            continue
            
        parts = rel_path.split(os.sep)
        depth = len(parts)
        
        # Managed skip
        if any(part in ['.git', '.venv', 'node_modules'] for part in parts):
            continue
            
        # Archive specifically: Zap anything starting with _git, _pytest, _memory if deep
        if len(parts) >= 2 and parts[0] == '3-resources' and parts[1] == 'archive':
            if any('_git' in p or '_pytest' in p or '_.memory' in p for p in parts):
                if depth >= max_depth:
                    try:
                        shutil.rmtree(root)
                        count += 1
                        dirs[:] = []
                        continue
                    except Exception:
                        pass
        
    # Sweep 2: Cleanup empty folders bottom-up
    for root, dirs, files in os.walk(root_path, topdown=False):
        rel_path = os.path.relpath(root, root_path)
        if rel_path == ".":
            continue
            
        parts = rel_path.split(os.sep)
        depth = len(parts)
        
        if any(part.startswith('.') or part in ['node_modules', 'venv', '.venv'] for part in parts):
            continue
            
        if not os.listdir(root):
            if depth > max_depth:
                try:
                    os.rmdir(root)
                    count += 1
                except Exception:
                    pass
    return count

if __name__ == "__main__":
    current_dir = os.getcwd()
    total = cleanup_deep_structures(current_dir)
    print(f"Deep cleanup complete. Removed/Cleaned {total} path objects.")

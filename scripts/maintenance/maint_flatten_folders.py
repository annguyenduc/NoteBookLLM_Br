import os
import shutil

def recursive_flatten_to_level3(root_path, max_depth=3):
    print(f"Executing Deep Flattening for: {root_path}")
    root_path = os.path.abspath(root_path)
    
    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        if rel_path == ".":
            continue
            
        parts = rel_path.split(os.sep)
        depth = len(parts)
        
        # We only care about things deeper than max_depth
        if depth <= max_depth:
            continue
            
        # Target bucket is the Level 3 folder
        bucket_dir = os.path.join(root_path, parts[0], parts[1], parts[2])
        
        # 1. Handle System Junk in Archive
        if any(p.startswith('.') or '_git' in p or 'cache' in p for p in parts):
            # Deleting system junk folders to save depth
            # (Git folders in archive are usually broken/cloned junk)
            continue # We'll handle deletion in cleanup script
            
        # 2. Move Files to Bucket
        for f in files:
            old_file_path = os.path.join(root, f)
            # Create a very flat name
            sub_parts = parts[3:]
            prefix = "_".join(sub_parts)
            new_name = f"{prefix}_{f}".replace(" ", "_")
            
            target_path = os.path.join(bucket_dir, new_name)
            
            if not os.path.exists(bucket_dir):
                os.makedirs(bucket_dir, exist_ok=True)
                
            try:
                if not os.path.exists(target_path):
                    shutil.move(old_file_path, target_path)
            except Exception:
                pass

if __name__ == "__main__":
    current_dir = os.getcwd()
    # Execute on brain/archive primarily as that's where the violations are
    archive_path = os.path.join(current_dir, "brain", "archive")
    if os.path.exists(archive_path):
        recursive_flatten_to_level3(current_dir)

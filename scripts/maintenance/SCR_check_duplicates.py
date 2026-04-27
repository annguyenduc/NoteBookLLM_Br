import os
import hashlib
import sys

# Ensure UTF-8 output for Vietnamese characters in console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_file_hash(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def check_duplicates(target_dir):
    file_map = {} # filename -> list of paths
    hash_map = {} # hash -> list of paths
    
    for root, dirs, files in os.walk(target_dir):
        for name in files:
            path = os.path.join(root, name)
            
            # Check by name
            if name not in file_map:
                file_map[name] = []
            file_map[name].append(path)
            
            # Check by hash
            try:
                f_hash = get_file_hash(path)
                if f_hash not in hash_map:
                    hash_map[f_hash] = []
                hash_map[f_hash].append(path)
            except Exception as e:
                print(f"Error hashing {path}: {e}")

    print("--- DUPLICATES BY FILENAME ---")
    found_name_dup = False
    for name, paths in file_map.items():
        if len(paths) > 1:
            found_name_dup = True
            print(f"File: {name}")
            for p in paths:
                print(f"  - {p}")
    if not found_name_dup:
        print("No duplicate filenames found.")

    print("\n--- DUPLICATES BY CONTENT (HASH) ---")
    found_hash_dup = False
    for f_hash, paths in hash_map.items():
        if len(paths) > 1:
            found_hash_dup = True
            print(f"Hash: {f_hash}")
            for p in paths:
                print(f"  - {p}")
    if not found_hash_dup:
        print("No duplicate content found.")

if __name__ == "__main__":
    check_duplicates(r"d:\NoteBookLLM_Br\brain")

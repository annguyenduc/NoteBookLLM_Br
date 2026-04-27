import os
import hashlib
import re

assets_dir = r"d:\NoteBookLLM_Br\3-resources\assets"
test_bank_dir = r"d:\NoteBookLLM_Br\3-resources\test-bank"

def get_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# 1. Map hashes to files
hashes = {}
for file in os.listdir(assets_dir):
    path = os.path.join(assets_dir, file)
    if os.path.isfile(path):
        h = get_hash(path)
        if h not in hashes:
            hashes[h] = []
        hashes[h].append(file)

# 2. Identify duplicates
duplicates = {} # keep_file -> list of files to delete
for h, files in hashes.items():
    if len(files) > 1:
        # Keep the first one (usually the one with the best name or just the first)
        keep = files[0]
        others = files[1:]
        duplicates[keep] = others

if not duplicates:
    print("No duplicates found.")
    exit()

print(f"Found {len(duplicates)} sets of duplicates.")

# 3. Update markdown files
# Pre-compile mapping for speed: to_delete -> keep
remap = {}
for keep, others in duplicates.items():
    for other in others:
        remap[other] = keep

md_files = [f for f in os.listdir(test_bank_dir) if f.endswith(".md")]
total_updates = 0

for md_file in md_files:
    path = os.path.join(test_bank_dir, md_file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = content
    for other, keep in remap.items():
        # Match ![anything](../assets/other)
        pattern = r'(\.\./assets/)' + re.escape(other)
        replacement = r'\1' + keep
        updated_content = re.sub(pattern, replacement, updated_content)
    
    if updated_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        total_updates += 1

print(f"Updated {total_updates} markdown files.")

# 4. Delete duplicates
total_deleted = 0
for keep, others in duplicates.items():
    for other in others:
        path = os.path.join(assets_dir, other)
        os.remove(path)
        total_deleted += 1

print(f"Deleted {total_deleted} duplicate asset files.")

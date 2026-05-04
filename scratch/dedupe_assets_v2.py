import os
import hashlib
import re

assets_dir = r"d:\NoteBookLLM_Br\3-resources\assets"
test_bank_dir = r"d:\NoteBookLLM_Br\3-resources\test-bank"

def get_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except:
        return None

# 1. Map hashes to files
print("Scanning assets...")
hashes = {}
for file in os.listdir(assets_dir):
    path = os.path.join(assets_dir, file)
    if os.path.isfile(path):
        h = get_hash(path)
        if h:
            if h not in hashes:
                hashes[h] = []
            hashes[h].append(file)

# 2. Identify duplicates
remap = {} # to_delete -> keep
duplicates_count = 0
for h, files in hashes.items():
    if len(files) > 1:
        keep = files[0]
        for other in files[1:]:
            remap[other] = keep
            duplicates_count += 1

if not remap:
    print("No duplicates found.")
    exit()

print(f"Found {duplicates_count} duplicate files.")

# 3. Build a fast replacement function
# We want to replace '../assets/file_to_delete' with '../assets/file_to_keep'
# Use a regex that matches any of the keys in remap
pattern = re.compile(r'\.\./assets/(' + '|'.join(map(re.escape, remap.keys())) + r')')

def replace_func(match):
    other = match.group(1)
    return '../assets/' + remap[other]

# 4. Update markdown files
print("Updating markdown files...")
md_files = [f for f in os.listdir(test_bank_dir) if f.endswith(".md")]
total_updates = 0

for md_file in md_files:
    path = os.path.join(test_bank_dir, md_file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(replace_func, content)
    
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        total_updates += 1

print(f"Updated {total_updates} markdown files.")

# 5. Delete duplicates
print("Deleting duplicate files...")
total_deleted = 0
for other in remap.keys():
    path = os.path.join(assets_dir, other)
    try:
        os.remove(path)
        total_deleted += 1
    except:
        pass

print(f"Deleted {total_deleted} duplicate asset files.")

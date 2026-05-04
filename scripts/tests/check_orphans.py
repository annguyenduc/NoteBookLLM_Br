import os
import re

wiki_dir = r"d:\NoteBookLLM_Br\brain\wiki"
distilled_dir = r"d:\NoteBookLLM_Br\brain\distilled"

# Get all wiki files
wiki_files = [f for f in os.listdir(wiki_dir) if f.startswith("WIKI_") and f.endswith(".md")]
# Extract names without extension for matching [[links]]
wiki_names = [os.path.splitext(f)[0] for f in wiki_files]

# Map of file -> list of files that link to it
inbound_links = {name: [] for name in wiki_names}

# Scan all wiki and distilled files for links
search_files = []
for root, dirs, files in os.walk(wiki_dir):
    for f in files:
        if f.endswith(".md"):
            search_files.append(os.path.join(root, f))
for root, dirs, files in os.walk(distilled_dir):
    for f in files:
        if f.endswith(".md"):
            search_files.append(os.path.join(root, f))

link_pattern = re.compile(r"\[\[(wiki/)?(WIKI_[^\]|]+)(\|[^\]]+)?\]\]")

for file_path in search_files:
    file_basename = os.path.splitext(os.path.basename(file_path))[0]
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            matches = link_pattern.findall(content)
            for match in matches:
                target = match[1].strip()
                if target in inbound_links and target != file_basename:
                    inbound_links[target].append(file_basename)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

# Identify orphans
orphans = [name for name, links in inbound_links.items() if len(links) == 0]

print(f"Total Concept Pages: {len(wiki_names)}")
print(f"Orphan Pages found: {len(orphans)}")
for orphan in sorted(orphans):
    print(f"- {orphan}")

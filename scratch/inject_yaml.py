import os
import re

concept_dir = r"d:\NoteBookLLM_Br\3-resources\wiki\concepts"

def inject_yaml(filename, content):
    if content.startswith("---"):
        return content # Already has YAML (or at least looks like it)
    
    file_id = filename.replace(".md", "")
    
    # Try to find title
    title_match = re.search(r"^#\s+(.*)", content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else file_id
    
    # Try to find source
    source_match = re.search(r"Nguồn:\s*\"?\[\[(SOURCE_[^\]]+)\]\]\"?", content)
    source = f"[[{source_match.group(1)}]]" if source_match else "unknown"
    
    # Clean title from brackets if any
    title = re.sub(r"\[\[|\]\]", "", title)
    # If title has a pipe like CONCEPT: [[...|Name]], take Name
    if "|" in title:
        title = title.split("|")[-1].strip()

    yaml = f"""---
file_id: {file_id}
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
title: "{title}"
source: "{source}"
created: "2026-05-03"
---

"""
    return yaml + content

count = 0
for filename in os.listdir(concept_dir):
    if not filename.endswith(".md"):
        continue
    
    path = os.path.join(concept_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = inject_yaml(filename, content)
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Injected YAML frontmatter into {count} files.")

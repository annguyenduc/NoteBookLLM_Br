import os
import re

wiki_dir = r"d:\NoteBookLLM_Br\3-resources\wiki"
projects_dir = r"d:\NoteBookLLM_Br\1-projects\2026_Data_Analyst"
concepts_dir = os.path.join(wiki_dir, "concepts")

# 1. Collect all files to rename
files_to_rename = []
for f in os.listdir(concepts_dir):
    if f.endswith(".md") and (f.startswith("THINK_") or f.startswith("ACAD_")):
        old_name = f
        new_name = "CONCEPT_" + old_name
        files_to_rename.append((old_name, new_name))

# 2. Rename files
for old, new in files_to_rename:
    old_path = os.path.join(concepts_dir, old)
    new_path = os.path.join(concepts_dir, new)
    os.rename(old_path, new_path)
    print(f"Renamed: {old} -> {new}")

# 3. Update links in all markdown files
def update_links(directory):
    updated_files_count = 0
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(".md"):
                file_path = os.path.join(root, f)
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                
                new_content = content
                for old, new in files_to_rename:
                    old_base = old[:-3]
                    new_base = new[:-3]
                    # Replace [[OLD_NAME]] with [[NEW_NAME]]
                    # Also handles [[OLD_NAME|alias]]
                    pattern = r"\[\[" + re.escape(old_base) + r"(\]|\|)"
                    repl = r"[[" + new_base + r"\g<1>"
                    new_content = re.sub(pattern, repl, new_content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    updated_files_count += 1
    return updated_files_count

count_wiki = update_links(wiki_dir)
count_projects = update_links(projects_dir)
print(f"Updated links in {count_wiki + count_projects} files.")

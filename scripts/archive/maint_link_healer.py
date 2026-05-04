import os
import json
import re

def link_healer(root_path, map_file="brain/link_map.json"):
    if not os.path.exists(map_file):
        print(f"Error: Map file {map_file} not found.")
        return
        
    with open(map_file, "r", encoding="utf-8") as f:
        link_map = json.load(f)
        
    print(f"Loaded {len(link_map)} mapping entries. Starting healing process...")
    
    # Wiki link pattern: [[Link]] or [[Link|Alias]]
    wiki_pattern = re.compile(r"\[\[(.*?)\]\]")
    # Markdown link pattern: [Text](Path)
    md_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    
    changed_count = 0
    total_files = 0
    
    # Process distilled and archive
    target_dirs = [
        os.path.join(root_path, "3-resources", "distilled"),
        os.path.join(root_path, "3-resources", "archive")
    ]
    
    for target_dir in target_dirs:
        if not os.path.exists(target_dir):
            continue
            
        for root, dirs, files in os.walk(target_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                    
                total_files += 1
                file_path = os.path.join(root, f)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                        
                    old_content = content
                    
                    # 1. Heal Wiki Links
                    def wiki_replace(match):
                        link_full = match.group(1)
                        if "|" in link_full:
                            link, alias = link_full.split("|", 1)
                            # Cleanup link (remove ./ or leading /)
                            link_clean = link.replace("./", "").lstrip("/")
                            if link_clean in link_map:
                                return f"[[{link_map[link_clean]}|{alias}]]"
                        else:
                            link_clean = link_full.replace("./", "").lstrip("/")
                            if link_clean in link_map:
                                return f"[[{link_map[link_clean]}]]"
                        return match.group(0) # No change
                        
                    content = wiki_pattern.sub(wiki_replace, content)
                    
                    # 2. Heal Markdown Links (relative paths only)
                    def md_replace(match):
                        text = match.group(1)
                        path = match.group(2)
                        # Skip web links
                        if path.startswith("http"):
                            return match.group(0)
                            
                        path_clean = path.replace("./", "").lstrip("/").replace(os.sep, "/")
                        if path_clean in link_map:
                            return f"[{text}]({link_map[path_clean]})"
                        return match.group(0)
                        
                    content = md_pattern.sub(md_replace, content)
                    
                    if content != old_content:
                        with open(file_path, "w", encoding="utf-8") as file:
                            file.write(content)
                        changed_count += 1
                except Exception:
                    continue
                    
    print(f"\nHealing complete. Scanned {total_files} files, updated {changed_count} files.")

if __name__ == "__main__":
    current_dir = os.getcwd()
    link_healer(current_dir)

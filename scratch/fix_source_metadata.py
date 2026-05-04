import os
import re

concept_dir = r"d:\NoteBookLLM_Br\3-resources\wiki\concepts"
source_dir = r"d:\NoteBookLLM_Br\3-resources\wiki\sources"
source_files = [f.replace(".md", "") for f in os.listdir(source_dir) if f.startswith("SOURCE_")]

def fix_source_metadata(content):
    # Target only the source field in YAML (between --- lines)
    yaml_match = re.search(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL | re.MULTILINE)
    if not yaml_match:
        return content
    
    yaml_content = yaml_match.group(1)
    
    # Regex to find source: value inside YAML
    pattern = r"source:\s*\"?(`?)('?)([^\"'\r\n`\]]+)('?)(`?)\"?"
    
    def replacement(match):
        original_name = match.group(3).strip()
        
        # Try direct match
        if original_name in source_files:
            return f"source: \"[[{original_name}]]\""
        
        # Try adding SOURCE_ prefix
        prefixed_name = f"SOURCE_{original_name}"
        if prefixed_name in source_files:
            return f"source: \"[[{prefixed_name}]]\""
        
        return match.group(0) # No change if no match found

    new_yaml = re.sub(pattern, replacement, yaml_content)
    
    if new_yaml != yaml_content:
        return content.replace(yaml_content, new_yaml)
    return content

count = 0
for filename in os.listdir(concept_dir):
    if not filename.endswith(".md"):
        continue
    
    path = os.path.join(concept_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = fix_source_metadata(content)
    
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Fixed source metadata in {count} files.")

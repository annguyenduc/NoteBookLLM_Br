import os
import re
import unicodedata
import sys

# Ensure UTF-8 output for console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def slugify(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text).replace('-', '_')

def process_file(file_path, target_dir, prefix_type):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    content = "".join(lines)
    filename = os.path.basename(file_path)
    base_name = os.path.splitext(filename)[0]
    
    # 1. New filename
    new_base = f"{prefix_type}_{slugify(base_name)}"
    new_filename = f"{new_base}.md"
    new_path = os.path.join(target_dir, new_filename)
    
    # 2. Extract Title
    title = base_name
    for line in lines:
        if line.startswith('# '):
            title = line.replace('# ', '').strip()
            break
            
    # 3. Inject YAML Frontmatter
    category = "Assessment" if prefix_type == "LMS_Tests" else "Atomic Note"
    yaml_header = f"""---
yaml_frontmatter:
  file_id: {new_base}
  title: {title}
  category: {category}
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

"""
    # 4. Convert Links to Wikilinks
    # This is a simple regex for [text](path) -> [[path_slug]]
    # Note: Complex link conversion might need more logic
    
    processed_content = yaml_header + content
    
    with open(new_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)
    
    print(f"Processed: {filename} -> {new_filename}")

def run_standardization():
    base_distilled = r"d:\NoteBookLLM_Br\brain\distilled"
    assessments_dir = os.path.join(base_distilled, "assessments")
    atomic_dir = os.path.join(base_distilled, "atomic")
    
    if os.path.exists(assessments_dir):
        for f in os.listdir(assessments_dir):
            if f.endswith('.md'):
                process_file(os.path.join(assessments_dir, f), base_distilled, "LMS_Tests")
                
    if os.path.exists(atomic_dir):
        for f in os.listdir(atomic_dir):
            if f.endswith('.md'):
                process_file(os.path.join(atomic_dir, f), base_distilled, "LMS_Atoms")

if __name__ == "__main__":
    run_standardization()

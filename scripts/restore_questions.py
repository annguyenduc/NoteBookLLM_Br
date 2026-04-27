import os
import re
import shutil
import hashlib

ARCHIVE_DIR = os.path.join("brain", "archive")
WIKI_DIR = os.path.join("brain", "wiki")

def shorten_filename(filename):
    # Match PREFIX
    prefix = ""
    if filename.startswith("NEEDS_REVIEW_QUESTION_"):
        prefix = "NEEDS_REVIEW_QUESTION_"
        rest = filename[len(prefix):]
    elif filename.startswith("QUESTION_"):
        prefix = "QUESTION_"
        rest = filename[len(prefix):]
    else:
        return None

    # Match Module and SubModule (assume first two tokens separated by underscore, or three)
    # E.g., Robot_Rover, DESIGN_3D_Tinkercad, IOT_AI_Arduino, KHMT_Python
    parts = rest.split('_')
    
    # Heuristic to find where the uppercase Module_SubModule ends and the lowercase repeat begins
    module_parts = []
    for p in parts:
        if p and (p[0].isupper() or p[0].isdigit()):
            module_parts.append(p)
        else:
            break
            
    if not module_parts:
        module_name = "Unknown"
    else:
        module_name = "_".join(module_parts)

    # Find the question number at the end
    match_q = re.search(r'_(\d+)\.md$', filename)
    q_num = match_q.group(1) if match_q else "X"
    q_str = f"Q{int(q_num):02d}" if q_num.isdigit() else f"Q{q_num}"
    
    # Attempt to find "de X"
    match_de = re.search(r'de[_\s]*(\d+)', filename, re.IGNORECASE)
    de_str = f"De{match_de.group(1)}_" if match_de else ""
    
    # Hash of original filename to guarantee uniqueness
    short_hash = hashlib.md5(filename.encode()).hexdigest()[:4]
    
    new_name = f"{prefix}{module_name}_{de_str}{q_str}_{short_hash}.md"
    return new_name

def main():
    if not os.path.exists(WIKI_DIR):
        os.makedirs(WIKI_DIR)
        
    count = 0
    for file in os.listdir(ARCHIVE_DIR):
        if file.startswith("QUESTION_") or file.startswith("NEEDS_REVIEW_QUESTION_"):
            old_path = os.path.join(ARCHIVE_DIR, file)
            new_name = shorten_filename(file)
            if new_name:
                new_path = os.path.join(WIKI_DIR, new_name)
                
                # Update file_id inside the file
                with open(old_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                new_file_id = new_name.replace(".md", "")
                content = re.sub(r'file_id:\s*".*?"', f'file_id: "{new_file_id}"', content, count=1)
                
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content)
                
                shutil.move(old_path, new_path)
                count += 1
                
    print(f"Restored and renamed {count} files to {WIKI_DIR}.")

if __name__ == "__main__":
    main()

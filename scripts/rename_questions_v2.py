import os
import re

WIKI_DIR = os.path.join("brain", "wiki")

def parse_de_from_source(content):
    # match source: "..."
    match = re.search(r'^source:\s*"(.*?)"', content, re.MULTILINE)
    if match:
        source_val = match.group(1)
        # Search for 'de 4', 'de_4', 'Đề 4', 'Đề kiểm tra 2'
        m2 = re.search(r'(?:de|đề).*?(\d+)', source_val, re.IGNORECASE)
        if m2:
            return m2.group(1)
    return "0"

def get_new_name(filename, content):
    prefix = ""
    if filename.startswith("NEEDS_REVIEW_QUESTION_"):
        prefix = "NEEDS_REVIEW_QUESTION_"
        rest = filename[len(prefix):]
    elif filename.startswith("QUESTION_"):
        prefix = "QUESTION_"
        rest = filename[len(prefix):]
    else:
        return None
    
    q_match = re.search(r'_(Q\d+)', rest)
    q_str = q_match.group(1) if q_match else "Q00"
    
    mod_match = re.split(r'_(De\d+|Q\d+)', rest)
    module_name = mod_match[0] if mod_match else "Unknown"
    
    # Abbreviation mappings
    module_name = module_name.replace("Tieu_hoc", "TH")
    module_name = module_name.replace("Tieu", "TH")
    module_name = module_name.replace("Trung_hoc_co_so", "THCS")
    
    module_name = module_name.strip('_')
    
    de_num = parse_de_from_source(content)
    de_str = f"De{de_num}" if de_num != "0" else "DeX"
    
    return f"{prefix}{module_name}_{de_str}_{q_str}.md"

def main():
    count = 0
    for file in os.listdir(WIKI_DIR):
        if file.startswith("QUESTION_") or file.startswith("NEEDS_REVIEW_QUESTION_"):
            old_path = os.path.join(WIKI_DIR, file)
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            new_name = get_new_name(file, content)
            if not new_name:
                continue
                
            if new_name == file:
                continue
                
            base_name, ext = os.path.splitext(new_name)
            final_name = new_name
            counter = 2
            while os.path.exists(os.path.join(WIKI_DIR, final_name)):
                if final_name == file:
                    break
                final_name = f"{base_name}_v{counter}{ext}"
                counter += 1
                
            new_path = os.path.join(WIKI_DIR, final_name)
            
            if old_path != new_path:
                new_file_id = final_name.replace(".md", "")
                content = re.sub(r'^file_id:\s*".*?"', f'file_id: "{new_file_id}"', content, count=1, flags=re.MULTILINE)
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content)
                    
                os.rename(old_path, new_path)
                count += 1
                
    print(f"Successfully renamed {count} question files.")

if __name__ == "__main__":
    main()

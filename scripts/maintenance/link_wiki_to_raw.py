import os
import re

RAW_DIR = r"d:\NoteBookLLM_Br\brain\raw"
WIKI_DIR = r"d:\NoteBookLLM_Br\brain\wiki"

def get_raw_files():
    return [f for f in os.listdir(RAW_DIR) if f.endswith('.md')]

def link_wiki_to_raw():
    raw_files = get_raw_files()
    raw_files_set = set(raw_files)
    count = 0
    
    for filename in os.listdir(WIKI_DIR):
        if not filename.endswith('.md'):
            continue
            
        filepath = os.path.join(WIKI_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find citations in the source section
        # Look for something after "📖 Nguồn:" or in the bottom section
        # We'll just look for any mention of a raw filename that isn't linked yet
        
        new_content = content
        for raw_file in raw_files:
            # Avoid double linking and only link if it looks like a citation
            # We look for the filename in backticks or just as plain text in the last part of the file
            escaped_raw = re.escape(raw_file)
            # Pattern: matches `raw_file` or raw_file but not inside [[ ]]
            pattern = rf'(?<!\[\[)([`]?{escaped_raw}[`]?)(?!\]\])'
            
            replacement = f'[[brain/raw/{raw_file}]]'
            new_content = re.sub(pattern, replacement, new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Linked {filename} to Raw sources.")
            
    return count

if __name__ == "__main__":
    print("Starting Wiki -> Raw linking process...")
    affected = link_wiki_to_raw()
    print(f"Finished. Updated {affected} Wiki pages.")

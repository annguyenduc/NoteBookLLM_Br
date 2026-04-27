import os
import re

def neutralize_atom_links_in_index(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        in_atom_section = False
        
        for line in lines:
            if '## ⚛️ ATOM PAGES' in line:
                in_atom_section = True
                new_lines.append(line)
                continue
            
            if in_atom_section and line.startswith('- [['):
                # Convert [[test-bank/file.md]] to `test-bank/file.md`
                new_line = re.sub(r'\[\[(.*?)\]\]', r'`\1`', line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
                
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    index_path = r"d:\NoteBookLLM_Br\brain\WIKI_INDEX.md"
    if neutralize_atom_links_in_index(index_path):
        print("Successfully neutralized atom links in WIKI_INDEX.md")
    else:
        print("Failed to neutralize links.")

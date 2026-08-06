import os
import re

def neutralize_links(directory):
    pattern = re.compile(r'\[\[(.*?)\]\]')
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = pattern.sub(r'`\1`', content)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
    return count

if __name__ == "__main__":
    archive_dir = r"d:\NoteBookLLM_Br\archive"
    print(f"Neutralizing Wikilinks in {archive_dir}...")
    affected = neutralize_links(archive_dir)
    print(f"Done. Neutralized links in {affected} files.")

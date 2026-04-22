import os
import re

BRAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'brain'))
INDEX_FILE = os.path.join(BRAIN_DIR, 'WIKI_INDEX.md')
DIRS_TO_INDEX = ['atoms', 'distilled']

def parse_markdown_file(filepath):
    title = os.path.basename(filepath)
    summary = ""
    status = ""
    tags = ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
        # Try to parse frontmatter
        frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if frontmatter_match:
            fm = frontmatter_match.group(1)
            title_match = re.search(r'^title:\s*"(.*?)"', fm, re.MULTILINE)
            if title_match:
                title = title_match.group(1)
            
            status_match = re.search(r'^status:\s*"(.*?)"', fm, re.MULTILINE)
            if status_match:
                status = status_match.group(1)
                
            tags_match = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
            if tags_match:
                tags = tags_match.group(1)
                
            # Remove frontmatter for summary search
            content = content[frontmatter_match.end():]
        else:
            # Fallback to H1
            h1_match = re.search(r'^#\s+(.*?)$', content, re.MULTILINE)
            if h1_match:
                title = h1_match.group(1)
                
        # Find first paragraph after H1 or headings
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('<!--') and not line.startswith('---'):
                if len(line) > 20: # Arbitrary length to ignore short noise
                    summary = line[:150] + "..." if len(line) > 150 else line
                    break
                    
    return {
        'title': title,
        'summary': summary,
        'status': status,
        'tags': tags,
        'rel_path': os.path.relpath(filepath, BRAIN_DIR).replace('\\', '/')
    }

def main():
    entries = {'atoms': [], 'distilled': []}
    
    for dir_name in DIRS_TO_INDEX:
        dir_path = os.path.join(BRAIN_DIR, dir_name)
        if not os.path.exists(dir_path):
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md') and not file.endswith('_TEMPLATE.md'):
                    filepath = os.path.join(root, file)
                    info = parse_markdown_file(filepath)
                    entries[dir_name].append(info)
                    
    # Generate Index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write("# 📚 LLM WIKI INDEX\n\n")
        f.write("> **Auto-generated Catalog of Wiki Knowledge**\n")
        f.write("> Lớp này là Mục lục của toàn bộ các file Kiến thức đã được LLM tạo ra, giúp tìm kiếm nhanh chóng.\n\n")
        
        for section, files in entries.items():
            f.write(f"## 📂 {section.upper()}\n")
            if not files:
                f.write("*Thư mục trống*\n\n")
                continue
                
            # Sort alphabetically by title
            files.sort(key=lambda x: x['title'].lower())
            
            for file in files:
                tags_str = f" `{file['tags']}`" if file['tags'] else ""
                status_str = f" **[{file['status'].upper()}]**" if file['status'] else ""
                f.write(f"- [[{file['rel_path']}]] | **{file['title']}**{status_str}{tags_str}\n")
                f.write(f"  > {file['summary']}\n")
            f.write("\n")
            
    print(f"Successfully generated WIKI_INDEX.md at {INDEX_FILE}")
    print(f"Indexed {len(entries['atoms'])} atoms and {len(entries['distilled'])} distilled files.")

if __name__ == '__main__':
    main()

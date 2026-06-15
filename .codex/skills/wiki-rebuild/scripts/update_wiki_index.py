import os
import re
from pathlib import Path

# Configuration
# Path to 3-resources/
# Now located in .agent/skills/wiki-rebuild/scripts/, so 4 levels up to reach ROOT
BRAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '3-resources'))
# Path to 3-resources/wiki/index.md
INDEX_FILE = os.path.join(BRAIN_DIR, 'wiki', 'index.md')

# Subdirectories within 3-resources/wiki/
WIKI_SUBDIRS = ['concepts', 'entities', 'sources', 'synthesis', 'queries', 'comparisons']
# Other directories in 3-resources/
OTHER_DIRS = ['test-bank']

def parse_markdown_file(filepath):
    stem = Path(filepath).stem
    title = stem
    summary = ""
    status = ""
    tags = ""
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None
        
    # Fix Windows line endings
    content = content.replace('\r\n', '\n').replace('\r', '\n')
        
    # Try to parse frontmatter
    frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if frontmatter_match:
        fm = frontmatter_match.group(1)
        title_match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip('"\'')
        
        status_match = re.search(r'^status:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
        if status_match:
            status = status_match.group(1).strip('"\'')
            
        tags_match = re.search(r'^tags:\s*\[(.*?)\]', fm, re.MULTILINE)
        if tags_match:
            tags = tags_match.group(1)
            
        content = content[frontmatter_match.end():]
    # Fallback to H1 if title is still stem
    if title == stem:
        h1_match = re.search(r'^#\s+(.*?)$', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            
    # Find first meaningful paragraph
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if (line and 
            not line.startswith('#') and 
            not line.startswith('<!--') and 
            not line.startswith('---') and
            not line.startswith('|') and
            not line.startswith('>') and
            not re.match(r'^(file_id|title|category|prefix|tags|source|status|created|last_updated):', line) and
            len(line) > 20):
            summary = line[:120] + "..." if len(line) > 120 else line
            break
                     
    return {
        'stem': stem,
        'title': title,
        'summary': summary,
        'status': status,
        'tags': tags,
        'rel_path': os.path.relpath(filepath, BRAIN_DIR).replace('\\', '/')
    }

def main():
    sections = {
        'concepts': [],
        'entities': [],
        'sources': [],
        'synthesis': [],
        'queries': [],
        'comparisons': [],
        'atoms': []
    }
    
    # Scan wiki subdirs
    wiki_root = os.path.join(BRAIN_DIR, 'wiki')
    for subdir in WIKI_SUBDIRS:
        subdir_path = os.path.join(wiki_root, subdir)
        if not os.path.exists(subdir_path):
            continue
        for root, _, files in os.walk(subdir_path):
            for file in files:
                if file.endswith('.md') and not file.endswith('_TEMPLATE.md'):
                    info = parse_markdown_file(os.path.join(root, file))
                    if info:
                        sections[subdir].append(info)
                        
    # Scan test-bank
    test_bank_path = os.path.join(BRAIN_DIR, 'test-bank')
    if os.path.exists(test_bank_path):
        for root, _, files in os.walk(test_bank_path):
            for file in files:
                if file.endswith('.md'):
                    info = parse_markdown_file(os.path.join(root, file))
                    if info:
                        sections['atoms'].append(info)

    # Sort
    for key in sections:
        sections[key].sort(key=lambda x: x['title'].lower())

    # Generate Index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write("# 📚 LLM WIKI INDEX\n\n")
        f.write("> **Auto-generated Catalog of Wiki Knowledge**\n")
        f.write("> Bản đồ tri thức tự động nén cho Swarm Agent 4.0.\n\n")
        
        # Section: SYNTHESIS (Master Pages)
        f.write(f"## 💎 MASTER PAGES ({len(sections['synthesis'])} file)\n")
        f.write("*Nơi bồi đắp tri thức nén, đa chiều.*\n\n")
        for p in sections['synthesis']:
            f.write(f"- [[{p['stem']}]] | **{p['title']}**\n")
            if p['summary']: f.write(f"  > {p['summary']}\n")
        f.write("\n")

        # Section: CONCEPTS
        f.write(f"## 🧠 CONCEPTS ({len(sections['concepts'])} trang)\n")
        f.write("*Các khái niệm, kỹ thuật nguyên tử.*\n\n")
        for p in sections['concepts']:
            status = f" **[{p['status'].upper()}]**" if p['status'] else ""
            f.write(f"- [[{p['stem']}]] | **{p['title']}**{status}\n")
            if p['summary']: f.write(f"  > {p['summary']}\n")
        f.write("\n")

        # Section: ENTITIES & SOURCES
        f.write(f"## 🏢 ENTITIES ({len(sections['entities'])})\n")
        for p in sections['entities']:
            f.write(f"- [[{p['stem']}]] | **{p['title']}**\n")
        f.write("\n")

        f.write(f"## 📖 SOURCES ({len(sections['sources'])})\n")
        for p in sections['sources']:
            f.write(f"- [[{p['stem']}]] | **{p['title']}**\n")
        f.write("\n")

        # Section: COMPARISONS
        f.write(f"## ⚖️ COMPARISONS ({len(sections['comparisons'])})\n")
        for p in sections['comparisons']:
            f.write(f"- [[{p['stem']}]] | **{p['title']}**\n")
        f.write("\n")

        # Section: QUERIES
        f.write(f"## 🔍 QUERIES ({len(sections['queries'])})\n")
        f.write("*Các cuộc nghiên cứu, research chuyên sâu.*\n\n")
        for p in sections['queries']:
            f.write(f"- [[{p['stem']}]] | **{p['title']}**\n")
        f.write("\n")

        # Section: ATOMS
        f.write(f"## ⚛️ ATOM PAGES ({len(sections['atoms'])} atoms)\n")
        f.write("*Dữ liệu chi tiết, câu hỏi trắc nghiệm.*\n\n")
        # To save tokens, only list first 50 atoms or just count
        f.write(f"*Tổng số {len(sections['atoms'])} câu hỏi đã được phân rã.*\n")
            
    print(f"Successfully updated index.md")

if __name__ == '__main__':
    if os.name == 'nt':
        import sys, io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    main()

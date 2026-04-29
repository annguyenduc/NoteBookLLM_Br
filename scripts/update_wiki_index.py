import os
import re

BRAIN_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '3-resources'))
INDEX_FILE = os.path.join(BRAIN_DIR, 'wiki', 'index.md')
DIRS_TO_INDEX = ['wiki', 'synthesis', 'test-bank']

def parse_markdown_file(filepath):
    title = os.path.basename(filepath)
    summary = ""
    status = ""
    tags = ""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Fix Windows line endings trÆ°á»›c khi parse
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
            
        # Remove frontmatter for summary search
        content = content[frontmatter_match.end():]
    else:
        # Fallback to H1
        h1_match = re.search(r'^#\s+(.*?)$', content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            
    # Find first meaningful paragraph (skip headers, dividers, YAML-like lines)
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
        'title': title,
        'summary': summary,
        'status': status,
        'tags': tags,
        'rel_path': os.path.relpath(filepath, BRAIN_DIR).replace('\\', '/')
    }

def is_concept_page(filename):
    """Concept pages lÃ  WIKI_*.md vÃ  KB_*.md â€” dÃ¹ng cho File-Back judgment."""
    name = os.path.basename(filename)
    return (name.startswith('WIKI_') or name.startswith('KB_'))

def main():
    concept_pages = []
    atom_pages = []
    distilled_pages = []
    
    for dir_name in DIRS_TO_INDEX:
        dir_path = os.path.join(BRAIN_DIR, dir_name)
        if not os.path.exists(dir_path):
            continue
            
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith('.md') and not file.endswith('_TEMPLATE.md'):
                    filepath = os.path.join(root, file)
                    info = parse_markdown_file(filepath)
                    if dir_name == 'synthesis':
                        distilled_pages.append(info)
                    elif dir_name == 'wiki':
                        concept_pages.append(info)
                    else:
                        atom_pages.append(info)
                    
    # Sort all sections alphabetically
    for lst in [concept_pages, atom_pages, distilled_pages]:
        lst.sort(key=lambda x: x['title'].lower())

    # Generate Index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write("# ðŸ“š LLM WIKI INDEX\n\n")
        f.write("> **Auto-generated Catalog of Wiki Knowledge**\n")
        f.write("> Lá»›p nÃ y lÃ  Má»¥c lá»¥c cá»§a toÃ n bá»™ cÃ¡c file Kiáº¿n thá»©c Ä‘Ã£ Ä‘Æ°á»£c LLM táº¡o ra.\n\n")
        f.write("> **HÆ°á»›ng dáº«n File-Back Judgment**: Chá»‰ cáº§n Ä‘á»c section **CONCEPT PAGES** Ä‘á»ƒ kiá»ƒm tra xem má»™t insight má»›i Ä‘Ã£ tá»“n táº¡i chÆ°a. KhÃ´ng cáº§n Ä‘á»c ATOM PAGES.\n\n")

        # Section 1: Concept Pages (cho File-Back judgment)
        f.write(f"## ðŸ§  CONCEPT PAGES ({len(concept_pages)} trang)\n")
        f.write("*DÃ nh cho File-Back Judgment â€” LLM Ä‘á»c section nÃ y Ä‘á»ƒ kiá»ƒm tra trÃ¹ng láº·p.*\n\n")
        if concept_pages:
            for page in concept_pages:
                status_str = f" **[{page['status'].upper()}]**" if page['status'] else ""
                f.write(f"- [[{os.path.splitext(os.path.basename(page['rel_path']))[0]}]] | **{page['title']}**{status_str}\n")
                if page['summary']:
                    f.write(f"  > {page['summary']}\n")
        else:
            f.write("*ChÆ°a cÃ³ trang nÃ o.*\n")
        f.write("\n")

        # Section 2: Distilled KB
        f.write(f"## ðŸ’Ž DISTILLED KB ({len(distilled_pages)} file)\n\n")
        if distilled_pages:
            for page in distilled_pages:
                f.write(f"- [[{os.path.splitext(os.path.basename(page['rel_path']))[0]}]] | **{page['title']}**\n")
                if page['summary']:
                    f.write(f"  > {page['summary']}\n")
        f.write("\n")

        # Section 3: Atom pages (MCQ, etc.)
        f.write(f"## âš›ï¸ ATOM PAGES ({len(atom_pages)} cÃ¢u há»i/atom)\n")
        f.write("*MCQ atoms vÃ  dá»¯ liá»‡u chi tiáº¿t â€” khÃ´ng cáº§n Ä‘á»c cho File-Back.*\n\n")
        if atom_pages:
            for page in atom_pages:
                f.write(f"- `{page['rel_path']}` | {page['title']}\n")
        f.write("\n")
            
    total = len(concept_pages) + len(atom_pages) + len(distilled_pages)
    print(f"Successfully generated WIKI_INDEX.md at {INDEX_FILE}")
    print(f"Concept pages: {len(concept_pages)} | Distilled: {len(distilled_pages)} | Atoms: {len(atom_pages)} | Total: {total}")

if __name__ == '__main__':
    main()




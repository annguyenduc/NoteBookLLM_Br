import sqlite3
import os
import re
import yaml
import sys

# Ensure UTF-8
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = r"d:\NoteBookLLM_Br"
WIKI_DIR = os.path.join(ROOT, "3-resources", "wiki")
DB_PATH = os.path.join(WIKI_DIR, "wiki_brain.db")

def clean_id(raw_data):
    # Handle if YAML parsed [[ID]] as a list of lists
    if isinstance(raw_data, list):
        if len(raw_data) > 0 and isinstance(raw_data[0], list):
            # It's [[ID]] parsed as list of lists
            return str(raw_data[0][0])
        elif len(raw_data) > 0:
            return str(raw_data[0])
        return ""
    
    if not raw_data: return ""
    raw_id = str(raw_data)
    return raw_id.replace("[[", "").replace("]]", "").strip()

def sync_file_relationships(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract YAML frontmatter
        match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return 0
            
        data = yaml.safe_load(match.group(1))
        source_id = data.get('file_id')
        if not source_id:
            return 0
            
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        edges_created = 0
        
        # 1. Process 'relationships' list
        rels = data.get('relationships', [])
        if isinstance(rels, list):
            for rel in rels:
                if isinstance(rel, dict):
                    edge_type = rel.get('type', 'MENTIONS').upper()
                    target_id = clean_id(rel.get('target'))
                    
                    if target_id:
                        cursor.execute("""
                            INSERT OR IGNORE INTO edges (source_id, target_id, edge_type, confidence)
                            VALUES (?, ?, ?, 1.0)
                        """, (source_id, target_id, edge_type))
                        if cursor.rowcount > 0:
                            edges_created += 1
                            
        # 2. Process 'sources' list as REFERENCES
        sources = data.get('sources', [])
        if isinstance(sources, list):
            for s in sources:
                target_id = clean_id(s)
                if target_id:
                    cursor.execute("""
                        INSERT OR IGNORE INTO edges (source_id, target_id, edge_type, confidence)
                        VALUES (?, ?, ?, 1.0)
                    """, (source_id, target_id, 'REFERENCES'))
                    if cursor.rowcount > 0:
                        edges_created += 1
                        
        conn.commit()
        conn.close()
        return edges_created
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        import traceback
        traceback.print_exc()
        return 0

if __name__ == "__main__":
    target_file = os.path.join(WIKI_DIR, "synthesis", "SYNTHESIS_LLM_WIKI_STANDARD.md")
    count = sync_file_relationships(target_file)
    print(f"Edges created for Standard: {count}")

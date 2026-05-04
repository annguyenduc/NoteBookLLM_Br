import sqlite3
import os
import re
import json
from datetime import datetime

# Path Configuration
# Now located in .agent/skills/wiki-rebuild/scripts/, so 4 levels up to reach ROOT
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
WIKI_PATH = os.path.join(REPO_ROOT, "3-resources", "wiki")
DB_PATH = os.path.join(WIKI_PATH, "wiki_brain.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Table for content (FTS5 for fast search)
    cursor.execute("DROP TABLE IF EXISTS nodes_fts")
    cursor.execute("""
        CREATE VIRTUAL TABLE nodes_fts USING fts5(
            path UNINDEXED,
            title,
            content,
            metadata UNINDEXED
        )
    """)

    # 2. Table for metadata and state
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nodes_meta (
            path TEXT PRIMARY KEY,
            file_id TEXT,
            category TEXT, -- Wings/Rooms/Drawers (MemPalace style)
            agent_id TEXT,
            status TEXT,
            last_modified TIMESTAMP
        )
    """)

    # 3. Table for Knowledge Graph (V3.2 Addition)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS edges (
            source_id TEXT,
            target_id TEXT,
            edge_type TEXT, -- MENTIONS | CONTRADICTS | SUPERSEDES
            confidence REAL DEFAULT 1.0,
            created_at TIMESTAMP,
            FOREIGN KEY(source_id) REFERENCES nodes_meta(path)
        )
    """)

    conn.commit()
    return conn

def extract_metadata(content):
    meta = {}
    # Simple YAML-like extraction for metadata
    if content.startswith("---"):
        match = re.search(r"---(.*?)---", content, re.DOTALL)
        if match:
            meta_str = match.group(1)
            for line in meta_str.split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    meta[k.strip()] = v.strip().strip('"')
    return meta

def get_category(path):
    # Mapping to MemPalace Structure
    if "concepts" in path: return "Drawers (Concepts)"
    if "entities" in path: return "Drawers (Entities)"
    if "sources" in path: return "Wings (Sources)"
    if "synthesis" in path: return "Rooms (Synthesis)"
    return "Generic"

def index_wiki():
    print(f"[*] Initializing Smart Spine at {DB_PATH}...")
    conn = init_db()
    cursor = conn.cursor()

    count = 0
    for root, dirs, files in os.walk(WIKI_PATH):
        if "wiki_brain.db" in files: continue
        
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, WIKI_PATH)
                
                with open(full_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                meta = extract_metadata(content)
                title = meta.get("title", file.replace(".md", ""))
                
                # Insert into FTS
                cursor.execute(
                    "INSERT INTO nodes_fts (path, title, content, metadata) VALUES (?, ?, ?, ?)",
                    (rel_path, title, content, json.dumps(meta))
                )
                
                # Insert into Meta
                cursor.execute("""
                    INSERT OR REPLACE INTO nodes_meta (path, file_id, category, agent_id, status, last_modified)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (
                    rel_path,
                    meta.get("file_id"),
                    get_category(rel_path),
                    meta.get("agent_id"),
                    meta.get("status", "verified"),
                    datetime.fromtimestamp(os.path.getmtime(full_path))
                ))
                
                # Basic Edge Extraction (MENTIONS) - looking for [[wikilinks]]
                links = re.findall(r"\[\[(.*?)\]\]", content)
                for link in links:
                    # Clean link name
                    target = link.split("|")[0].strip()
                    # We store it as a tentative edge, validation happens later
                    cursor.execute("""
                        INSERT INTO edges (source_id, target_id, edge_type, created_at)
                        VALUES (?, ?, ?, ?)
                    """, (rel_path, target, "MENTIONS", datetime.now()))
                
                count += 1

    conn.commit()
    conn.close()
    print(f"[+] Indexed {count} atoms successfully.")

if __name__ == "__main__":
    index_wiki()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Brain Lint v1.0 - NoteBookLLM_Br
Kiá»ƒm tra sá»©c khá»e Wiki: Orphan pages vÃ  Broken links.
"""

import os, re
from pathlib import Path

WIKI_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki")
DISTILLED_DIR = Path(r"d:\NoteBookLLM_Br\3-resources\wiki\synthesis")

def get_all_target_files():
    files = [f for f in WIKI_DIR.rglob("*.md") if f.stem not in ['log', 'index', 'index', 'overview']]
    return {f.stem: f for f in files}

def get_all_content_files():
    return list(WIKI_DIR.rglob("*.md")) + list(DISTILLED_DIR.rglob("*.md"))

def lint():
    target_files = get_all_target_files()
    all_content_files = get_all_content_files()
    
    inbound_links = {stem: 0 for stem in target_files}
    broken_links = []
    
    # Regex to find [[Wikilinks]]
    link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|[^\]]*)?]]')
    
    for file_path in all_content_files:
        if file_path.stem in ['log', 'index', 'index', 'overview']: continue

        try:
            content = file_path.read_text(encoding='utf-8')
        except:
            continue
            
        links = link_pattern.findall(content)
        for link in links:
            link_stem = link.strip()
            if link_stem in inbound_links:
                inbound_links[link_stem] += 1
            elif link_stem not in ["log", "index", "WIKI_INDEX"]: # Skip system files
                broken_links.append((file_path.name, link_stem))
                    
    orphans = [stem for stem, count in inbound_links.items() if count == 0]
    
    print("--- LINT REPORT ---")
    print(f"Total Target Pages: {len(target_files)}")
    print(f"Orphan Pages Found: {len(orphans)}")
    for o in orphans:
        print(f"  - [ORPHAN] {o}")
        
    print(f"Broken Wikilinks Found: {len(broken_links)}")
    unique_broken = set([b[1] for b in broken_links])
    for b in unique_broken:
        print(f"  - [GAP] [[{b}]]")
        
    print("--- END REPORT ---")

if __name__ == "__main__":
    lint()





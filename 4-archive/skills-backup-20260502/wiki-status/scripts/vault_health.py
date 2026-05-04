"""
vault_health.py — NoteBookLLM_Br Health Check (Adapted from eugeniughelbur)

Audits the Wiki 2.0 vault for structural issues and calculates Link Density.
"""

import argparse
import json
import re
import os
from collections import defaultdict
from datetime import date
from pathlib import Path

TODAY = date.today()
# Adapt for NoteBookLLM_Br structure
EXCLUDE_DIRS = {".obsidian", ".trash", "_trash", ".git", "Templates", "4-archive", "00_Inbox", "assets", ".agent", ".codex"}
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")

def parse_aliases(frontmatter: str) -> list:
    """Extract aliases list from frontmatter text."""
    ALIAS_RE = re.compile(r"^aliases:\s*\n((?:\s+-\s+.+\n?)+)", re.MULTILINE)
    ALIAS_ITEM_RE = re.compile(r"^\s+-\s+(.+)$", re.MULTILINE)
    block = ALIAS_RE.search(frontmatter)
    if not block:
        return []
    return [m.strip().strip('"\'').lower() for m in ALIAS_ITEM_RE.findall(block.group(1))]

def load_vault(vault: Path) -> dict:
    notes = {}
    vault_str = str(vault)
    for root, dirs, files in os.walk(vault_str):
        # Sửa dirs tại chỗ để os.walk bỏ qua các thư mục bị loại trừ
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if not file.endswith(".md"):
                continue
            
            full_path = Path(root) / file
            rel = str(full_path.relative_to(vault))
            
            try:
                content = full_path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
                
            fm_match = FRONTMATTER_RE.match(content)
            frontmatter = fm_match.group(1) if fm_match else ""
            links = [l.strip().rstrip("\\") for l in LINK_RE.findall(content)]
            
            notes[rel] = {
                "path": full_path,
                "rel": rel,
                "stem": full_path.stem,
                "content": content,
                "frontmatter": frontmatter,
                "has_frontmatter": bool(fm_match),
                "links": links,
                "aliases": parse_aliases(frontmatter),
                "size": len(content),
            }
    return notes

def check_duplicates(notes: dict) -> list:
    issues = []
    stems = defaultdict(list)
    for rel, note in notes.items():
        # Normalize stem for duplicate check
        norm = re.sub(r"\d{4}-\d{2}-\d{2}", "", note["stem"]).lower()
        norm = re.sub(r"[^a-z0-9 ]", " ", norm).strip()
        norm = re.sub(r"\s+", " ", norm)
        stems[norm].append(rel)
    for norm, files in stems.items():
        if len(files) > 1 and norm.strip():
            issues.append({
                "type": "duplicate",
                "severity": "warning",
                "message": f"Possible duplicates: {norm!r}",
                "files": files,
            })
    return issues

def check_orphans(notes: dict) -> list:
    all_links = set()
    for note in notes.values():
        for link in note["links"]:
            all_links.add(link.lower())

    issues = []
    # Skip non-content folders
    skip_folders = {"Templates", "4-archive", "00_Inbox", "scripts", ".agent"}

    for rel, note in notes.items():
        top_folder = rel.split("/")[0] if "/" in rel else ""
        if top_folder in skip_folders or rel.startswith("."):
            continue
        if rel in ("index.md", "overview.md", "log.md", "purpose.md"):
            continue
            
        stem_lower = note["stem"].lower()
        linked = (
            stem_lower in all_links
            or any(alias in all_links for alias in note["aliases"])
        )
        if not linked:
            issues.append({
                "type": "orphan",
                "severity": "info",
                "message": f"No incoming links: {rel}",
                "files": [rel],
            })
    return issues

def check_broken_links(notes: dict) -> list:
    all_stems = {note["stem"].lower(): rel for rel, note in notes.items()}
    all_aliases = {}
    for rel, note in notes.items():
        for alias in note["aliases"]:
            all_aliases[alias.lower()] = rel

    issues = []
    for rel, note in notes.items():
        for link in note["links"]:
            link_stem = Path(link).stem.lower() if "/" in link else link.lower()
            resolved = (
                link_stem in all_stems
                or link_stem in all_aliases
            )
            if not resolved:
                issues.append({
                    "type": "broken_link",
                    "severity": "warning",
                    "message": f"Broken link [[{link}]] in {rel}",
                    "files": [rel],
                })
    return issues

def run_health_check(vault: Path) -> dict:
    notes = load_vault(vault)
    
    # Calculate Link Density Index (LDI)
    total_notes = len(notes)
    total_links = sum(len(note["links"]) for note in notes.values())
    ldi = total_links / total_notes if total_notes > 0 else 0
    
    checks = [
        ("Duplicates", check_duplicates(notes)),
        ("Orphans", check_orphans(notes)),
        ("Broken links", check_broken_links(notes)),
    ]

    all_issues = []
    counts = {}
    for label, issues in checks:
        counts[label] = len(issues)
        all_issues.extend(issues)

    return {
        "vault": str(vault),
        "scanned": TODAY.isoformat(),
        "total_notes": total_notes,
        "total_links": total_links,
        "link_density": round(ldi, 2),
        "total_issues": len(all_issues),
        "counts": counts,
        "issues": all_issues,
    }

def main():
    parser = argparse.ArgumentParser(description="NoteBookLLM_Br Health Checker")
    parser.add_argument("--path", required=True, help="Path to the vault")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    vault = Path(args.path).expanduser().resolve()
    result = run_health_check(vault)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("=" * 60)
        print(f"  VAULT HEALTH REPORT — {result['scanned']}")
        print("=" * 60)
        print(f"  Notes scanned: {result['total_notes']}")
        print(f"  Total links:   {result['total_links']}")
        print(f"  Link Density:  {result['link_density']} (Target: > 3.0)")
        print(f"  Issues found:  {result['total_issues']}")
        print("-" * 60)
        for label, count in result["counts"].items():
            if count > 0:
                print(f"  {label}: {count}")
        print("=" * 60)

if __name__ == "__main__":
    main()

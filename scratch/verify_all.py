r"""
verify_all.py — Master Verification Script
NoteBookLLM_Br Wiki System V3.1
Chạy: python d:\NoteBookLLM_Br\scratch\verify_all.py
"""

import os
import sqlite3
import sys

# Force UTF-8 for Windows terminal
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = r"d:\NoteBookLLM_Br"
DB   = os.path.join(ROOT, "3-resources", "wiki", "wiki_brain.db")

PASS = "[OK]"
FAIL = "[FAIL]"
WARN = "[WARN]"

results = []

def check(label, condition, critical=True):
    icon = PASS if condition else (FAIL if critical else WARN)
    results.append((icon, label, condition))
    print(f"  {icon} {label}")

def section(title):
    print(f"\n{'-'*50}")
    print(f"  {title}")
    print('-'*50)


# ══════════════════════════════════════════
# PHASE 1 — Foundation
# ══════════════════════════════════════════
section("PHASE 1 — Foundation")

# 1a. Folders
section("1a. Folder structure")
for folder in [
    r"00_Inbox",
    r"1-projects",
    r"2-areas",
    r"3-resources\raw",
    r"3-resources\wiki\concepts",
    r"3-resources\wiki\entities",
    r"3-resources\wiki\sources",
    r"3-resources\wiki\comparisons",
    r"3-resources\wiki\queries",
    r"3-resources\wiki\synthesis",
    r"3-resources\wiki\decisions",
    r"3-resources\wiki\review_queue",
    r"3-resources\wiki\session_insights",
    r"4-archive",
    r".agent\skills\wiki-ingest\scripts",
    r".agent\skills\wiki-absorb\scripts",
    r".agent\skills\wiki-query",
    r".agent\skills\wiki-breakdown\scripts",
    r".agent\skills\wiki-cleanup\scripts",
    r".agent\skills\wiki-status",
    r".agent\skills\wiki-rebuild\scripts",
    r".agent\skills\wiki-council",
    r".agent\mcp",
]:
    path = os.path.join(ROOT, folder)
    check(folder, os.path.isdir(path))

# 1b. Root identity files
section("1b. Identity files (root)")
for f in ["SOUL.md", "USER.md", "AGENTS.md"]:
    path = os.path.join(ROOT, f)
    exists = os.path.isfile(path)
    check(f, exists)
    if exists:
        size = os.path.getsize(path)
        check(f"  {f} > 200 chars", size > 200)

# 1c. SOUL.md keywords
section("1c. SOUL.md content")
soul_path = os.path.join(ROOT, "SOUL.md")
if os.path.isfile(soul_path):
    soul = open(soul_path, encoding="utf-8").read()
    for kw in ["Ranh giới tuyệt đối", "Nhiệm vụ cốt lõi",
                "Khi bất định", "SYNTHESIZED", "IMMUTABLE"]:
        check(f"  keyword: {kw}", kw in soul)

# 1d. USER.md sections
section("1d. USER.md sections")
user_path = os.path.join(ROOT, "USER.md")
if os.path.isfile(user_path):
    user = open(user_path, encoding="utf-8").read()
    for section_kw in ["identity", "expertise", "output_constraints",
                        "solution_space_limits", "learning_stance",
                        "review_preferences"]:
        check(f"  section: {section_kw}", section_kw in user)

# 1e. Database
section("1e. wiki_brain.db")
check("DB file exists", os.path.isfile(DB))
if os.path.isfile(DB):
    conn = sqlite3.connect(DB)

    # Tables
    tables = [r[0] for r in conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()]
    for t in ["atoms", "edges", "review_queue",
              "session_insights", "structure", "atom_search"]:
        check(f"  table: {t}", t in tables)

    # atoms columns
    cols = [r[1] for r in conn.execute("PRAGMA table_info(atoms)").fetchall()]
    for c in ["confidence", "learning_source", "status",
              "human_review_flag", "title", "type"]:
        check(f"  atoms.{c}", c in cols)

    # Row counts
    atom_count = conn.execute("SELECT COUNT(*) FROM atoms").fetchone()[0]
    edge_count  = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
    check(f"  atoms rows >= 289 (got {atom_count})", atom_count >= 289)
    check(f"  edges rows >= 15749 (got {edge_count})", edge_count >= 15749)

    # Schema version
    ver = conn.execute(
        "SELECT value FROM structure WHERE key='schema_version'"
    ).fetchone()
    check(f"  schema_version = V3.1", ver and ver[0] == "V3.1")

    conn.close()

# 1f. Backup exists
section("1f. Backup")
backup = os.path.join(ROOT, "4-archive", "wiki_brain_backup_20260503.db")
check("Backup file exists", os.path.isfile(backup))
if os.path.isfile(backup) and os.path.isfile(DB):
    orig_size = os.path.getsize(DB)
    back_size = os.path.getsize(backup)
    check(f"  Backup size matches original", orig_size >= back_size * 0.95)


# ══════════════════════════════════════════
# PHASE 2 — Skills
# ══════════════════════════════════════════
section("PHASE 2 — Skills")

SKILLS = {
    "wiki-ingest": {
        "has_scripts": True,
        "scripts": ["ingest.py", "magika_router.py"],
        "skill_keywords": ["Gate", "magika", "DRAFT", "confidence", "IMMUTABLE"],
        "min_lines": {"ingest.py": 100, "magika_router.py": 40},
    },
    "wiki-absorb": {
        "has_scripts": True,
        "scripts": ["reconciler.py"],
        "skill_keywords": ["ADDITIVE", "CONTRADICTS", "reconcile",
                           "human_review_flag", "SYNTHESIZED"],
        "min_lines": {"reconciler.py": 80},
    },
    "wiki-query": {
        "has_scripts": False,
        "scripts": [],
        "skill_keywords": ["FTS5", "graph", "confidence", "USER.md", "Rule 14"],
        "min_lines": {},
    },
    "wiki-breakdown": {
        "has_scripts": True,
        "scripts": ["noun_miner.py"],
        "skill_keywords": ["gap", "stub", "noun", "breakdown"],
        "min_lines": {"noun_miner.py": 50},
    },
    "wiki-cleanup": {
        "has_scripts": True,
        "scripts": ["lint_engine.py"],
        "skill_keywords": ["broken link", "stale", "lint", "Steve Jobs"],
        "min_lines": {"lint_engine.py": 60},
    },
    "wiki-status": {
        "has_scripts": False,
        "scripts": [],
        "skill_keywords": ["density", "verified", "draft", "dashboard"],
        "min_lines": {},
    },
    "wiki-rebuild": {
        "has_scripts": True,
        "scripts": ["rebuild.py", "indexer.py"],
        "skill_keywords": ["index.md", "_backlinks", "sync", "nightly"],
        "min_lines": {"rebuild.py": 50, "indexer.py": 50},
    },
    "wiki-council": {
        "has_scripts": False,
        "scripts": [],
        "skill_keywords": ["council", "conflict", "shared utility",
                           "poll", "peer review", "chairman"],
        "min_lines": {},
    },
}

for skill_name, config in SKILLS.items():
    section(f"2. {skill_name}")
    skill_base = os.path.join(ROOT, ".agent", "skills", skill_name)
    skill_md   = os.path.join(skill_base, "SKILL.md")

    check(f"  SKILL.md exists", os.path.isfile(skill_md))
    if os.path.isfile(skill_md):
        content = open(skill_md, encoding="utf-8").read()
        check(f"  SKILL.md > 300 chars", len(content) > 300)
        for kw in config["skill_keywords"]:
            check(f"  keyword: {kw}", kw.lower() in content.lower())

    for script in config["scripts"]:
        script_path = os.path.join(skill_base, "scripts", script)
        check(f"  script exists: {script}", os.path.isfile(script_path))
        if os.path.isfile(script_path):
            lines = len(open(script_path, encoding="utf-8").readlines())
            min_l = config["min_lines"].get(script, 0)
            check(f"  {script} >= {min_l} lines (got {lines})",
                  lines >= min_l)


# ══════════════════════════════════════════
# PHASE 3 — Integration
# ══════════════════════════════════════════
section("PHASE 3 — Integration")

# AGENTS.md
section("3a. AGENTS.md")
agents_path = os.path.join(ROOT, "AGENTS.md")
if os.path.isfile(agents_path):
    agents = open(agents_path, encoding="utf-8").read()
    for kw in ["1%", "wiki-ingest", "wiki-absorb", "wiki-query",
                "SYNTHESIZED", "invoke"]:
        check(f"  keyword: {kw}", kw in agents)

# MCP server
section("3b. MCP server")
mcp_path = os.path.join(ROOT, ".agent", "mcp", "mcp_server.py")
check("mcp_server.py exists", os.path.isfile(mcp_path))
if os.path.isfile(mcp_path):
    mcp = open(mcp_path, encoding="utf-8").read()
    for tool in ["search_atoms", "expand_neighbors",
                 "get_cluster", "get_revision_history"]:
        check(f"  tool: {tool}", tool in mcp)

# score_engine
section("3c. score_engine")
score_path = os.path.join(ROOT, ".agent", "skills",
                           "wiki-ingest", "scripts", "score_engine.py")
check("score_engine.py exists", os.path.isfile(score_path), critical=False)


# ══════════════════════════════════════════
# PHASE 4 — Safety checks
# ══════════════════════════════════════════
section("PHASE 4 — Safety checks")

if os.path.isfile(DB):
    conn = sqlite3.connect(DB)

    # Ranh giới thép: không có SYNTHESIZED do agent set
    synth = conn.execute(
        "SELECT COUNT(*) FROM atoms WHERE status='SYNTHESIZED'"
    ).fetchone()[0]
    check(f"  No agent-set SYNTHESIZED (count={synth})", synth == 0)

    # raw/ không bị ghi vào
    raw_violations = conn.execute(
        "SELECT COUNT(*) FROM task_logs WHERE details LIKE '%raw%' "
        "AND status='success'"
    ).fetchone()[0]
    check(f"  No raw/ write violations (count={raw_violations})",
          raw_violations == 0)

    # task_logs có entries
    log_count = conn.execute(
        "SELECT COUNT(*) FROM task_logs"
    ).fetchone()[0]
    check(f"  task_logs has entries (count={log_count})", log_count > 0)

    conn.close()


# ══════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════
print(f"\n{'='*50}")
print("  SUMMARY")
print('='*50)
total    = len(results)
passed   = sum(1 for r in results if r[0] == PASS)
failed   = sum(1 for r in results if r[0] == FAIL)
warnings = sum(1 for r in results if r[0] == WARN)

print(f"  Total  : {total}")
print(f"  {PASS} Pass   : {passed}")
print(f"  {FAIL} Fail   : {failed}")
print(f"  {WARN} Warning: {warnings}")

if failed == 0:
    print("\n  🎉 ALL CHECKS PASSED — System ready")
else:
    print(f"\n  🚨 {failed} check(s) failed — review before proceeding")
    print("\n  Failed items:")
    for icon, label, _ in results:
        if icon == FAIL:
            print(f"    {FAIL} {label}")
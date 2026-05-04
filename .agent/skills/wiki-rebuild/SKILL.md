---
name: wiki-rebuild
description: "Use when the database is out of sync with the filesystem, after files are added or deleted manually, or on nightly maintenance. Triggers on /rebuild command or when index.md is stale. Do NOT use for content edits."
---

Synchronize knowledge infrastructure, update indices, and manage backlink injection.

## Context
As the volume of atoms grows, manual index maintenance becomes impossible. `wiki-rebuild` maintains a live knowledge map and enables deep traceability via backlinks.

## Workflow

### Step 1: Structural Sync
Synchronize the state between the filesystem and the database.
```bash
python .agent/skills/wiki-rebuild/scripts/rebuild.py
```
This should be run **nightly** for maintenance.

### Step 2: Index Generation
Update the central `index.md` at `3-resources/wiki/index.md`. Categories include Concepts, Entities, Sources, and Synthesis.

### Step 3: Backlinks Injection
Inject a list of files linking to the current Atom into the `_backlinks` section at the end of each Markdown file.

## Constraints
- Do not alter the core content of an Atom when injecting backlinks.
- Always verify Database integrity before performing a sync.
description: Use when wiki files, database indexes, or infrastructure views drift out of sync after manual file changes, failed automation, nightly maintenance, or orphan-link repair work.
---

# Wiki Rebuild

## Overview
Repair infrastructure state between the filesystem, database, and generated indexes. This is a low-freedom maintenance skill and should not be used for editorial content changes.

## Guardrails
- Use the main entrypoint first: `rebuild.py`.
- Treat `--heal-orphans` as a write operation that adds graph edges.
- Do not use rebuild to bypass the file-first rule; physical markdown remains the source of truth.
- Expect legacy helper scripts in this folder; prefer the documented entrypoints unless you are debugging the index layer itself.

## Workflow
1. Confirm the problem is infrastructure drift, not content quality.
2. Run the main repair:
   `python .agent/skills/wiki-rebuild/scripts/rebuild.py`
3. If orphan healing is explicitly needed, run:
   `python .agent/skills/wiki-rebuild/scripts/rebuild.py --heal-orphans`
4. Regenerate the human-readable index when needed:
   `python .agent/skills/wiki-rebuild/scripts/update_wiki_index.py`
5. Review the DB and generated files before declaring the rebuild complete.

## Quick Reference
- Main repair:
  `rebuild.py`
- Optional orphan healing:
  `rebuild.py --heal-orphans`
- Index regeneration:
  `update_wiki_index.py`
- Lower-level or legacy helpers:
  `indexer.py`, `wiki_indexer.py`

## Common Mistakes
- Using rebuild when the real issue is a bad ingest or cleanup pass.
- Assuming DB-to-file sync is allowed for anything beyond the approved status flow.
- Running orphan healing casually and creating weak graph edges without review.

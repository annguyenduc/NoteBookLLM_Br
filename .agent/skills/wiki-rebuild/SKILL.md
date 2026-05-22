---
name: wiki-rebuild
description: "Sync database with filesystem after manual additions/deletions. Triggers on /rebuild or stale index. Do NOT use for content edits."
---

# Wiki Rebuild (Resilient/Sync)

## Overview
Repair infrastructure state between the filesystem and database. This skill ensures that physical markdown files are correctly mirrored in the DB, and atoms whose files are missing on disk are marked as **DEPRECATED**.

## Testing
This skill uses **TDD** to ensure synchronization integrity.
Run tests from the workspace root:
```powershell
python .agent/skills/wiki-rebuild/tests/test_rebuild.py
```

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

## Technical Keywords (Audit)
- **_backlinks**: Indexing feature for bidirectional discovery.

## Technical Reference
- _backlinks.json: file lưu backlink graph của vault
- index.md: file index tổng hợp toàn bộ vault
- sync: đồng bộ DB với filesystem
- nightly: chạy tự động mỗi đêm qua cron

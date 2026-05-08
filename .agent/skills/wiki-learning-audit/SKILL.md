---
name: wiki-learning-audit
description: "Use when auditing unverified knowledge in the vault — specifically to find Atoms tagged learning_source=true that have not been confirmed through practice. Triggers on 'audit learning atoms', 'check unverified atoms', 'review queue audit', 'learning audit', or when weekly review cycle starts. Do NOT use for general ingest tasks or content editing."
---

# Wiki Learning Audit

## Overview
Scan the vault database for Atoms marked `learning_source=true` that remain in `DRAFT` or `VERIFIED` (not `SYNTHESIZED`) status, then push them into the review queue for human verification. This enforces the principle: knowledge read from a source ≠ knowledge confirmed through practice.

## Guardrails
- Never auto-promote Atoms to `SYNTHESIZED`; that gate is human-only.
- Do not edit Atom content during audit — only update frontmatter fields and queue entries.
- Cap each audit run at the `max_items` value from USER.md (default: 10 atoms/run) to prevent queue overflow.
- Lower `confidence` by 0.1 relative to the source's base score when flagging — do not override manually set confidence values below 0.5.
- If the DB is unavailable, fall back to scanning markdown frontmatter directly in `3-resources/wiki/`.

## Workflow
1. **Query unverified learning atoms.**
   Run:
   `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --dry-run`
   Review the list before making any changes.

2. **Confirm scope with user** if the result count exceeds `max_items` (10).
   Ask: which domains to prioritize, or defer the rest to next cycle.

3. **Execute the audit.**
   `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py`
   The script will:
   - Set `needs_practice_verification=true` in each Atom's frontmatter.
   - Reduce `confidence` by 0.1 (floor: 0.5).
   - Insert each Atom into `review_queue` table with `reason=learning_unverified`.

4. **Report results** in plain text:
   - Count of Atoms flagged.
   - Domains covered.
   - Earliest Atom by `created_date` (oldest unverified knowledge first).

## Script Contract (`audit_learning_atoms.py`)
Expected behavior when the script is built:
```
--dry-run        Print affected Atoms, make no changes
--limit N        Override max_items cap
--domain SLUG    Filter by domain tag
--since DATE     Only flag Atoms created after this date
```
Output: plain list of `atom_id | title | domain | current_confidence`.

## Quick Reference
- Dry run:
  `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --dry-run`
- Audit single domain:
  `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --domain ai-engineering`
- Check queue after run:
  `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "review_queue learning_unverified" --limit 20`

## Common Mistakes
- Running without `--dry-run` first and flooding the queue.
- Auditing `SYNTHESIZED` atoms — these are already human-verified, skip them.
- Treating `VERIFIED` status as "confirmed through practice" — it only means the source is credible, not that the knowledge was applied.
- Forgetting to report results; the human needs the list to plan the next review session.

## Technical Keywords (Audit)
- **learning_source**: frontmatter flag — true when knowledge comes from reading/research, not practice.
- **needs_practice_verification**: frontmatter flag set by this skill.
- **review_queue**: DB table / Obsidian note where flagged Atoms accumulate.
- **SYNTHESIZED**: human-only status; this skill must never set it.
- **confidence**: float 0.0–1.0; this skill subtracts 0.1 when flagging.

## Technical Reference
- `learning_source=true`: Atom nguồn từ đọc/research, chưa kiểm chứng qua thực hành.
- `needs_practice_verification=true`: flag do skill này set, cần human verify.
- `review_queue`: nơi tập trung Atoms cần human review mỗi cuối tuần.
- confidence floor: 0.5 — không giảm xuống dưới mức này dù tính toán.
- max_items: lấy từ USER.md → `review_preferences.weekly_review.max_items`.

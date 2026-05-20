---
name: wiki-learning-audit
description: "Use when auditing unverified knowledge in the vault — specifically to find Atoms tagged learning_source=true that have not been confirmed through practice OR Atoms that are due for spaced repetition review. Triggers on 'audit learning atoms', 'check unverified atoms', 'review queue audit', 'learning audit', or when weekly review cycle starts. Do NOT use for general ingest tasks or content editing."
---

# Wiki Learning Audit

## Overview
Scan the vault database for:
1. Atoms marked `learning_source=true` (or column `learning_source = 1` in SQLite) that remain in `DRAFT` or `VERIFIED` (not `SYNTHESIZED`) status, then push them into the review queue for human verification. This enforces the principle: knowledge read from a source ≠ knowledge confirmed through practice.
2. Atoms that have an active study progress (`IN_PROGRESS`, `LEARNED`) and are due for spaced repetition review (`next_review` <= today), then push them into the review queue with tag `spaced_repetition_due`.

## Guardrails
- Never auto-promote Atoms to `SYNTHESIZED`; that gate is human-only.
- Do not edit Atom content during audit — only update frontmatter fields and queue entries.
- Cap each audit run at the `max_items` value from USER.md (default: 10 atoms/run) to prevent queue overflow.
- Lower `confidence` by 0.1 relative to the source's base score when flagging — do not override manually set confidence values below 0.5 (only applicable for default `learning_source` audit, not for Spaced Repetition due audit).
- If the DB is unavailable, fall back to scanning markdown frontmatter directly in `3-resources/wiki/`.

## Workflow
1. **Query unverified learning atoms or due review atoms.**
   Run (for unverified raw learning):
   `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --dry-run`
   
   Run (for Spaced Repetition due atoms):
   `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --due --dry-run`
   
   Review the list before making any changes.

2. **Confirm scope with user** if the result count exceeds `max_items` (10).
   Ask: which domains to prioritize, or defer the rest to next cycle.

3. **Execute the audit.**
   `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py`
   (Or `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --due`)
   
   The script will:
   - For unverified learning: Set `needs_practice_verification=true` in each Atom's frontmatter, reduce `confidence` by 0.1 (floor: 0.5), and insert each Atom into `review_queue` table with `reason=learning_unverified`.
   - For due review: Insert each Atom into `review_queue` table with `reason=spaced_repetition_due` to prompt the user to study via personalized learning path dashboard.

4. **Report results** in plain text:
   - Count of Atoms flagged.
   - Domains covered.
   - Earliest Atom by `created_date`/`next_review` (oldest/most urgent knowledge first).

## Script Contract (`audit_learning_atoms.py`)
Expected behavior when the script is built:
```
--dry-run        Print affected Atoms, make no changes
--limit N        Override max_items cap
--domain SLUG    Filter by domain tag
--since DATE     Only flag Atoms created/modified after this date
--due            Only scan Atoms that are due for spaced repetition review (next_review <= today)
```
Output: plain list of `atom_id | title | domain | current_confidence / next_review`.

## Quick Reference
- Dry run (Default learning audit):
  `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --dry-run`
- Dry run (Spaced Repetition due):
  `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --due --dry-run`
- Execute Spaced Repetition due audit:
  `python .agent/skills/wiki-learning-audit/scripts/audit_learning_atoms.py --due`
- Check queue after run:
  `python .agent/skills/wiki-query/scripts/wiki_query_helper.py --query "review_queue spaced_repetition_due" --limit 20`

## Common Mistakes
- Running without `--dry-run` first and flooding the queue.
- Auditing `SYNTHESIZED` atoms — these are already human-verified, skip them.
- Confusing Spaced Repetition Due with Raw Ingest; they serve different purposes.

## Technical Reference
- `learning_source=true`: Atom nguồn từ đọc/research, chưa kiểm chứng qua thực hành.
- `needs_practice_verification=true`: flag do skill này set, cần human verify.
- `next_review`: trường lưu ngày ôn tập Spaced Repetition do SM-2 tính toán.
- `spaced_repetition_due`: lý do đẩy vào review_queue cho các atom đến hạn ôn tập.
- `learning_unverified`: lý do đẩy vào review_queue cho các atom nguồn thô chưa thực hành.

---
name: wiki-absorb
description: "Use when new Wiki Atoms in DRAFT status need to be reconciled against existing knowledge, or when contradictions between sources are detected and require resolution."
---

# Wiki Absorb

## Overview
Reconcile `DRAFT` atoms against existing atoms in the database. This is the promotion and conflict-handling step between ingest and human synthesis.

## Guardrails
- Only `reconciler.py` should promote items from `DRAFT` to `VERIFIED`.
- **MANDATORY**: Never physically move files out of the `review_queue/` directory during the absorb process. Promotion to root folders is a separate step triggered ONLY by human approval.
- Never set `SYNTHESIZED`; that remains human-only.
- Use this skill for DB reconciliation, not for editing wiki markdown by hand.
- If confidence is low or the conflict is ambiguous, leave a decision trail instead of forcing a merge.

## Workflow
1. Confirm there are `DRAFT` atoms to process.
2. Run `python .agent/skills/wiki-absorb/scripts/reconciler.py`.
3. Review which path each atom took:
   additive promotion, duplicate removal, high-confidence supersede, or human-review flagging.
4. If a conflict was escalated, inspect `3-resources/wiki/decisions/` and `review_queue` before claiming the batch is complete.

## Quick Reference
- Main entrypoint:
  `python .agent/skills/wiki-absorb/scripts/reconciler.py`
- Test harness:
  `python .agent/skills/wiki-absorb/scripts/pressure_test_absorb.py`
- Helper:
  `wiki_council_helper.py` supports council-style escalation paths.

## Common Mistakes
- Running absorb when the real problem is a bad source file or bad ingest.
- Assuming all same-title atoms should merge automatically.
- Forgetting that low-confidence conflicts should stay visible for human review.
- Reporting success without checking whether decision files or queue entries were created.

## Technical Keywords (Audit)
- **CONTRADICTS**: Edge type for knowledge conflict.
- **human_review_flag**: Governance gate for manual verification.

## Technical Reference
- CONTRADICTS: edge type khi 2 atoms mâu thuẫn nhau
- human_review_flag: set = 1 khi conflict ambiguous
- ADDITIVE: merge tự động khi không có conflict
- SYNTHESIZED: chỉ human được set trạng thái này

---
name: wiki-absorb
description: "Use when new Wiki Atoms in DRAFT status need to be reconciled against existing knowledge, or when contradictions between sources are detected and require resolution."
---

Reconcile and upgrade DRAFT atoms into verified knowledge within the Wiki system.

## Context
After `wiki-ingest` populates the database with DRAFT atoms, `wiki-absorb` ensures these atoms are correctly integrated without causing contradictions or redundancy.

## Workflow

### Tier 1: Structural Analysis (Automatic)
1. **Scan**: Retrieve all atoms with `status='DRAFT'`.
2. **Hash Comparison**: If the hash matches a `VERIFIED/SYNTHESIZED` atom, log as `DUPLICATE` and skip.
3. **Exact Match**: If the content matches exactly (even if hash differs due to metadata), log as `EXACT` and skip.
4. **Additive Check**: If no existing atom shares the same title/topic, upgrade to `VERIFIED`.

### Tier 2: Cognitive Reconciliation (LLM-Assisted)
1. **Contradiction Detection**: Flag atoms with the same title but differing content.
2. **Reasoning**: Invoke LLM to determine if the new information supplements or replaces the old one.
3. **Resolution**:
   - If the new info is superior/updated: Upgrade to `VERIFIED` and mark the old atom as `SUPERSEDES`.
   - If it's a different perspective: Create a `RELATED_TO` edge.

### Tier 3: Human Governance (Escalation)
1. **Risk Logging**: For significant contradictions with low confidence sources.
2. **Decision Recording**: Create `3-resources/wiki/decisions/DECISION_[ID].md`.
3. **Review Queue**: Set `human_review_flag = 1` for final user approval.

## Execution
```bash
python .agent/skills/wiki-absorb/scripts/reconciler.py
```

## Constraints
- **Rule 8**: Agents must NEVER set status to `SYNTHESIZED` (Human-only).
- **Rule 4**: Every DB or file change must be logged in `3-resources/wiki/log.md`.
- **Traceability**: Always maintain the link to the original `raw/` source.
description: Use when `DRAFT` atoms in `wiki_brain.db` need deduplication, additive promotion, or conflict escalation before human review, especially after a fresh ingest batch.
---

# Wiki Absorb

## Overview
Reconcile `DRAFT` atoms against existing atoms in the database. This is the promotion and conflict-handling step between ingest and human synthesis.

## Guardrails
- Only `reconciler.py` should promote items from `DRAFT` to `VERIFIED`.
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

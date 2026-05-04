---
name: wiki-absorb
description: "Nâng cấp và hòa giải các DRAFT atoms thành tri thức chính thức trong Wiki."
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

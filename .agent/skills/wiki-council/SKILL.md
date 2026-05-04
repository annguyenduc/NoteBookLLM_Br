---
name: wiki-council
description: "Use when knowledge contradictions (CONTRADICTS edges) cannot be resolved by automated logic and require multi-agent consensus. Do NOT use for minor conflicts resolvable by wiki-absorb."
---

Resolve complex knowledge conflicts through multi-agent consensus and formal voting.

## Context
When automated logic cannot resolve direct contradictions (CONTRADICTS) between atoms, `wiki-council` is activated to make evidence-based decisions.

## Workflow

### Step 1: Summon Council
Any agent detecting a high-level conflict can summon the council. This includes listing contradictory atoms and their respective sources.

### Step 2: Peer Review
Participating agents perform peer reviews:
- Verify Source Confidence Scores.
- Check Recency (timeliness).
- Analyze Claim Logic.

### Step 3: Poll & Decision
Perform a virtual poll among specialized agents.
- > 70% Consensus: Update new atom and create a `SUPERSEDES` edge.
- No Consensus: Escalate to the **Chairman** (Human) for the final decision.

## Constraints
- Decisions must not be made without clear Source Tracing.
- All council minutes must be recorded in `3-resources/wiki/decisions/`.
description: Use when absorb or manual review surfaces a real contradiction that cannot be resolved safely by heuristics alone and the team needs a recorded decision note in `3-resources/wiki/decisions/`.
---

# Wiki Council

## Overview
Handle unresolved contradictions with explicit evidence review and a written decision trail. This is a governance skill, not an automatic merge script.

## Guardrails
- Use `wiki-absorb` first for routine additive and high-confidence cases.
- Do not call council for minor naming differences or easy duplicate cleanup.
- Every conclusion must cite the competing atom IDs and their sources.
- If consensus is weak, stop at a decision record and leave the final status to the human gate.

## Workflow
1. Gather the conflict package.
List the atom IDs, titles, source references, confidence signals, and why the conflict matters.
2. Compare the evidence.
Prioritize source quality, recency, and whether the statements are truly incompatible.
3. Write a decision note in `3-resources/wiki/decisions/`.
Record the options, rationale, and recommended next action.
4. Hand the result back to human review or to a follow-up absorb step if the resolution becomes clear.

## Quick Reference
- There is no dedicated council runner in this folder.
- Use `wiki_council_helper.py` from `wiki-absorb/scripts/` only as a supporting utility when the conflict originated in absorb.
- Store durable outcomes in `3-resources/wiki/decisions/`.

## Common Mistakes
- Calling council before checking whether the conflict is just a duplicate.
- Recording a verdict without source tracing.
- Treating "more recent" as automatically "more correct".

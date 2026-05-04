---
name: wiki-council
description: "Giải quyết mâu thuẫn tri thức phức tạp thông qua cơ chế Hội đồng (Council) và biểu quyết (Poll)."
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

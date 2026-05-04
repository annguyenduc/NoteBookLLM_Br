---
name: wiki-status
description: "Use when the user asks about Wiki health, atom counts, verification rates, or link density. Also use before a large ingest batch to establish a baseline. Triggers on 'wiki status', 'dashboard', or '/status' commands."
---

Report system health through a dashboard and knowledge connectivity metrics.

## Context
Sustainable Wiki growth requires monitoring. `wiki-status` provides statistics on knowledge connectivity and reliability.

## Workflow

### Step 1: Dashboard Overview
Report the distribution of Atoms by status:
- **Verified**: Verified knowledge.
- **Draft**: Raw knowledge awaiting reconciliation.
- **Synthesized**: Human-finalized knowledge.

### Step 2: Link Density Analysis
Calculate the **Link Density Index (LDI)**.
- LDI = Total Edges / Total Atoms.
- Goal: Maintain LDI > 2.0 to ensure a robust knowledge graph.

### Step 3: Error Rate Tracking
Monitor the volume of errors detected by `wiki-cleanup` across recent sessions.

## Execution
```bash
python .agent/skills/wiki-status/scripts/dashboard.py
```

## Constraints
- Reports must be based on real data from `wiki_brain.db`.
- **Rule 2**: No fake numbers or reports.
description: Use when reporting current vault health, atom and edge counts, verification mix, or a before-and-after baseline for ingest, cleanup, absorb, or rebuild work.
---

# Wiki Status

## Overview
Produce a real status snapshot from the database and filesystem health checks. This skill is for measurement and reporting, not for repair.

## Guardrails
- Quote only live script output.
- If the dashboard reports DB or health-check errors, surface those errors instead of inventing fallback numbers.
- Use status metrics as signals, not as proof that content quality is good.

## Workflow
1. Run the combined dashboard:
   `python .agent/skills/wiki-status/scripts/dashboard.py`
2. If you need machine-readable detail, run:
   `python .agent/skills/wiki-status/scripts/vault_health.py --path d:/NoteBookLLM_Br --json`
3. Summarize the current counts, link density, and recent log/error signals.
4. When comparing before and after a maintenance task, use absolute numbers from both runs.

## Quick Reference
- Main dashboard:
  `dashboard.py`
- JSON health report:
  `vault_health.py --path d:/NoteBookLLM_Br --json`
- Typical signals:
  total atoms, total edges, status distribution, link density, recent task logs

## Common Mistakes
- Repeating old dashboard numbers after the vault changed.
- Ignoring a failing health script and still presenting a polished report.
- Treating more atoms as automatically better health.

---
name: wiki-status
description: "Báo cáo sức khỏe hệ thống thông qua Health Dashboard và các chỉ số tri thức."
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

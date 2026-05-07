---
name: wiki-status
description: "Use when the user asks about Wiki health, atom counts, verification rates, or link density. Also use before a large ingest batch to establish a baseline. Triggers on 'wiki status', 'dashboard', or '/status' commands."
---

# Wiki Status (Dashboard/Health)

## Overview
Produce a real-time status snapshot from the database and filesystem. This skill provides the **Executive Summary** of the Wiki 2.0 health, including atom counts, link density, and recent activity logs.

## Testing
This skill uses **TDD** to ensure reporting accuracy.
Run tests from the workspace root:
```powershell
python .agent/skills/wiki-status/tests/test_status.py
```

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

## Technical Keywords (Audit)
- **verified**: Status for high-confidence knowledge.
- **draft**: Initial state for newly ingested content.

## Technical Reference
- verified: trạng thái atom đã qua score threshold
- draft: trạng thái atom mới được ingest, chưa review
- density: Link Density Index = edges / atoms
- dashboard: output tổng hợp sức khỏe vault

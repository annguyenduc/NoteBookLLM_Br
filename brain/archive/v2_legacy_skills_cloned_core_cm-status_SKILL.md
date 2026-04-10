---


name: cm-status
description: "CORE — Project Health & Velocity Monitor. Tóm tắt tình trạng dự án và chỉ số sức khỏe (PHI) dưới 60 giây."
version: 2.0.0
---

# cm-status — Project Health Monitor (PRO)

> **Goal:** Provide an instant view of the project's "health". Analyze progress, outstanding errors, and forecast risk via the PHI (Project Health Index).

## When to Activate

- Starting or ending any work session
- User asks "/cm-status"
- Before planning the next iteration
- When a blocker is suspected but not yet identified

## Instructions

### Status Command Behavior

When activated, the agent performs:
1. **PHI Scoring (1-10):** Evaluate health based on:
   - Number of Tasks Done vs Todo.
   - Outstanding critical bugs not yet fixed.
   - Task completion velocity.
2. **Dashboard Render:**
   - 🔴 TO DO | 🟡 IN PROGRESS | 🟢 DONE
   - Current mode: (Planning / Execution / Verification)
3. **Blocker Analysis:** Auto-scan `task.md` and logs to find the reason for any blockage.

### Project Health Index (PHI) Scale

| PHI | Meaning | Action |
|-----|---------|--------|
| 9-10 | Everything stable, build passing, tasks on track. | Continue as-is. |
| 6-8 | Minor bugs or delayed tasks, no architectural impact. | Monitor closely. |
| < 5 | **Warning!** Architectural problems or a critical bug with no Root Cause yet. | Stop, escalate, fix. |

### Integration Protocol

- **`cm-dashboard`:** `/cm-status` is typically called before `/cm-dashboard` to gather summary metrics.
- **`cm-planning`:** Automatically updates PHI after every `task.md` update.

## Quality Gate (Red Flags)

- ❌ Reporting high PHI when a critical unresolved bug exists.
- ❌ Forgetting to mention a blocker.
- ❌ Reporting the wrong current mode vs what is actually being executed.

## Example Triggers

- "/cm-status"
- "Is the current project healthy? (PHI check)"
- "Status summary: what is blocking me right now?"
- "Give me a 60-second health snapshot of this project."

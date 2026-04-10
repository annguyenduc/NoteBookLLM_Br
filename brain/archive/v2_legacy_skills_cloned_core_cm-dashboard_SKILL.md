---


name: cm-dashboard
description: "CORE — Kanban board trực quan theo dõi trạng thái tất cả công việc đang thực hiện."
version: 2.0.0
---

# cm-dashboard — Project Kanban Dashboard (LITE)

> **Goal:** Provide a project progress overview via a visual Markdown Kanban board. Convert data from `task.md` into actionable status columns.

## When to Activate

- User asks "/cm-dashboard"
- Need a visual snapshot of all tasks across phases
- Before a daily standup or session review
- To identify which tasks are stuck in progress

## Instructions

### Dashboard Render Protocol

When activated:
1. **Data Fetch:** Read `task.md` (and optionally `cm-tasks.json` if present).
2. **Kanban Render:** Generate a Markdown table with 3 columns:
   - **🔴 TO DO:** Tasks not yet started.
   - **🟡 IN PROGRESS:** Tasks currently being worked on.
   - **🟢 DONE:** Completed tasks.
3. **Flow Report:** Brief summary of current mode (Planning/Execution/Verification) and Next Step.

### Output Format

```markdown
## 📊 Project Kanban

| 🔴 TO DO | 🟡 IN PROGRESS | 🟢 DONE |
|---------|---------------|---------|
| Task A  | Task C        | Task E  |
| Task B  | Task D        | Task F  |

**Current Mode:** Execution
**Next Step:** Complete Task C, then move to Task A
**PHI:** 7/10
```

## Quality Gate (Red Flags)

- ❌ Displaying stale task information from not reading the latest `task.md`.
- ❌ Missing a status column, leaving the user unaware of progress.
- ❌ Reporting the wrong current mode compared to what is actually being executed.

## Example Triggers

- "/cm-dashboard"
- "Show me the Kanban board for this project."
- "Dashboard status: which tasks are blocked?"
- "Render the task board before I start this session."

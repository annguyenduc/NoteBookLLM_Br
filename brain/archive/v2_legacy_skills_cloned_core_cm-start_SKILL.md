---

name: cm-start
description: "CORE — Khởi động workflow: thu nhận yêu cầu, định tuyến skill phù hợp và chốt chiến lược thực thi ban đầu."
version: 4.0.0
---

# cm-start — Workflow Orchestrator (LITE)

> **Goal:** Activate the workflow from idea to completed product. Analyze complexity, establish working memory, and coordinate the right skills to execute the user's objective.

## When to Activate

- Starting any new task or feature
- User asks "where do we begin?" or "kick off this project"
- Resuming work after a session break
- Routing an ambiguous request to the right skill

## Instructions

### The Startup Sequence

1. **Load Memory:** Read `CONTINUITY.md` → Update `Active Goal` with the new objective.
2. **Skill Check:** Scan Triggers in the request → If a skill is missing → `npx skills find`.
3. **Intelligence Setup:** Run `cm-codeintell` to get the project's Skeleton structure.
4. **Complexity Detection:** Classify the request into levels L0-L3.

### Project Complexity Levels

| Level | Scope | Recommended Workflow |
|-------|-------|---------------------|
| **L0 (Micro)** | Small bug fix, 1 file. | `cm-tdd` → `cm-quality-gate`. |
| **L1 (Small)** | Small feature, < 3 files. | `cm-planning` (Lite) → `tdd` → deploy. |
| **L2 (Medium)** | Complex feature. | `brainstorm` → `planning` → `tdd` + `execution`. |
| **L3 (Large)** | New module / major refactor. | `brainstorm` (Mandatory) → `planning` → sprint. |

### Phase Mode (for large refactors)

When a major taxonomy or skill-pack refactor is requested, run in 2 phases:
1. **Phase 1 — Stabilize:** Fix broken links, add alias mapping, run validator.
2. **Phase 2 — Refactor:** Rename legacy folders, sync frontmatter names, update index/router.

**Hard rule:** Do NOT merge Phase 2 until Phase 1 checks pass completely.

### Progress Tracking

- **Task Breakdown:** Auto-break the objective into L1-L4 tasks in `task.md`.
- **Command:** Suggest user run `/cm-dashboard` for Kanban view or `/cm-status` for health check.
- **Handoff:** Transfer context to `cm-planning` or `cm-execution`.

## Quality Gate (Red Flags)

- ❌ Jumping into execution without first classifying complexity (L-Level).
- ❌ Skipping identity check (`cm-identity-guard`) when starting a new project.
- ❌ Not updating working memory at the very start of the session.
- ❌ Missing skill coverage audit — leads to using the wrong tools.

## Example Triggers

- "/cm-start [your objective]"
- "Start building feature X."
- "Kick off the workflow for task Y."
- "Initialize this session with the right skills."

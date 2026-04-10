---


name: cm-execution
description: "CORE — Chọn chế độ thực thi phù hợp (theo lô, song song, tuần tự) để hoàn thành kế hoạch đã lập."
version: 2.0.0
---

# cm-execution — Execution Engine (LITE)

> **Goal:** Execute plans systematically, optimizing speed through parallel processing (TRIZ-Parallel) and ensuring quality via an autonomous verification loop (RARV).

## When to Activate

- An implementation plan is ready and execution needs to begin
- Choosing the right execution mode for a set of tasks
- Running autonomous task loops until a backlog is cleared
- Coordinating subagents with a mandatory cross-review gate

## Instructions

### Execution Modes

| Mode | When to Use | Strategy |
|------|-------------|----------|
| **A: Batch** | Plan has clear checkpoints. | Execute 3 tasks → Report → Feedback → Continue. |
| **B: Subagent** | Independent tasks within the same session. | 1 subagent/task + mandatory 2-stage review. |
| **C: Parallel** | System broken across multiple independent modules. | 1 agent per module to avoid context conflicts. |
| **D: RARV** | Fully autonomous execution required. | **R**eason → **A**ct → **R**eflect → **V**erify. |
| **E: TRIZ-Parallel** | Maximum speed + quality required. | Segment tasks by dependency graph + Quality Gates. |

### Two-Stage Review (Subagent Mode B)

Mandatory "Cross-Review" process when delegating to a Subagent (Subagent-Driven-Development):

1. **Stage 1 — Spec Compliance:** Compare Subagent output against original design/goals. Must meet the design logic exactly and completely. If incorrect/incomplete → Reject output.
2. **Stage 2 — Code Quality:** Only after Stage 1 passes, evaluate Code Smell, Security (XSS, Injection, Path Traversal), and TDD Coverage. If poor → Force refactor.

### Security Rules (Never Violate)

- **Frontend:** Never use `innerHTML` with raw data (prevents XSS). Use `textContent`.
- **Backend (Python):** Never use `shell=True` in `subprocess`. Use list arguments instead.
- **Path Safety:** Always use `safe_resolve()` to block Path Traversal attacks.

### RARV Operation Loop (Mode D)

1. **Reason:** Read `task.md` → Select highest-priority task.
2. **Act:** Use the appropriate specialized skill (`cm-tdd`, `cm-debugging`) to handle it.
3. **Reflect:** Update results in memory and task log.
4. **Verify:** Run `cm-quality-gate`. If FAIL → Retry (max 3 times) → If still FAIL → Block and escalate.

## Quality Gate (Red Flags)

- ❌ Executing before auditing skill coverage (missing required tools).
- ❌ Merging code when tests are failing or review has not passed.
- ❌ Not updating task status in `task.md` in real time.
- ❌ Skipping `cm-codeintell` pre-flight check, leading to modifying the wrong module.

## Example Triggers

- "Start executing Batch 1 of the implementation plan."
- "Run TRIZ-Parallel mode for these independent UI tasks."
- "RARV: autonomously complete the task list in the backlog."
- "Which execution mode is best for this set of tasks?"

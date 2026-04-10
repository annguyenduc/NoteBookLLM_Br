---


name: cm-skill-chain
description: "CORE — Tạo pipeline tự động ghép nhiều skills thành workflow phức tạp."
version: 2.0.0
---

# cm-skill-chain — Automated Skill Pipeline Engine (LITE)

> **Goal:** Connect individual skills into an autonomous workflow pipeline, automating the hand-off between phases from Idea to Deployment.

## When to Activate

- Running a known multi-skill end-to-end workflow
- Automating a repetitive sequence of skill invocations
- Want to track which step in a multi-phase process you are at
- Building or debugging a cross-skill automation pipeline

## Instructions

### Built-in Skill Chains

| Chain ID | Workflow Sequence |
|----------|------------------|
| **feature-dev** | `brainstorm` → `planning` → `tdd` → `execution` → `quality-gate` → `safe-deploy` |
| **bug-fix** | `debugging` → `planning` → `tdd` → `quality-gate` |
| **content-launch** | `content-factory` → `ads-tracker` → `cro-methodology` |
| **new-project** | `project-bootstrap` → `planning` → `tdd` → `execution` → `quality-gate` |

### Chain Control Commands

- `chain auto "task"` — Auto-detect and launch the most appropriate chain.
- `chain start <id>` — Manually launch a specific chain.
- `chain advance <id>` — Complete the current step and move to the next.
- `chain status` — Check progress and current position in the chain.
- `chain abort` — Cancel the running chain.

### Operation Protocol

1. **Detection:** Agent identifies the task pattern (e.g., Fix bug → `bug-fix` chain).
2. **Activation:** Suggest the appropriate Chain to the user.
3. **Execution:** Run each step in sequence, invoking skills via `@[/skill-name]`.
4. **Relay:** After each step, run `chain advance` to hand off context (Continuity).

## Quality Gate (Red Flags)

- ❌ Skipping critical steps (e.g., jumping to Execution without Planning).
- ❌ Missing context sync between chain links (causes requirement drift).
- ❌ Not stopping when a chain link FAILS (must fix before advancing).
- ❌ Forgetting to update `CONTINUITY.md` status while the chain is running.

## Example Triggers

- "Run the full pipeline for the social login feature."
- "Start the bug-fix chain for the payment module."
- "Skill chain: from idea to landing page."
- "What step are we at in the feature-dev chain?"

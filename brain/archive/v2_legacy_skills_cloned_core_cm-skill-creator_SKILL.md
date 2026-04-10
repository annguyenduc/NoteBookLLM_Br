---

name: cm-skill-creator
description: "CORE — Công cụ giúp xây dựng, kiểm tra và tối ưu hóa các Kỹ năng (Skills) khác trong bộ Kit."
version: 2.0.0
---

# cm-skill-creator — Skill-Driven Development Engine (LITE)

> **Goal:** Automate the **Skill-Driven Development (SDD)** lifecycle. Help the agent self-evolve by creating, evaluating, and refining Skills to achieve maximum performance at minimum token cost.

## When to Activate

- Creating a new skill from scratch
- Auditing an existing skill for quality or token efficiency
- Running evaluations to validate skill output quality
- Detecting a gap where no existing skill covers a domain

## Instructions

### SDD Lifecycle

| Phase | Action | Tool |
|-------|--------|------|
| **Initialize** | Research gaps → Create `SKILL.md` (Lite format). | `scripts/run_eval.py` |
| **Evaluate** | Run 3-5 real test cases (Input/Output pairs). | `eval_cases.json` |
| **Optimize** | Refine based on feedback-loop results. | Agent Comparator |
| **Learning** | Auto-update rules when encountering "Don't do X" errors. | `CONTINUITY.md` |

### Lite Format Standard (v2.0)

- **Metadata:** YAML Header (Name, Description, Version, Tags).
- **Core Goal:** 1-2 sentences defining the core objective.
- **Rules/Tables:** Present in table/list format (token-efficient).
- **Quality Gate:** Red Flags & anti-patterns.
- **Triggers:** List of activation keywords and phrases.

### Refinement Protocol

- **A/B Testing:** Compare original (verbose) vs refined (lite) versions to confirm output quality is not degraded.
- **Token Check:** Every Lite skill should be between **1.5KB - 2.5KB** in size.
- **Index Sync:** Automatically call `cm-skill-index` after creating or updating a skill.

## Quality Gate (Red Flags)

- ❌ Creating a new skill without checking for duplication with existing skills.
- ❌ Output template too vague — not providing concrete enough guidance for the agent.
- ❌ Missing Red Flags section to prevent incorrect logic from being applied.
- ❌ Not running `run_eval.py` before announcing a skill as complete.

## Example Triggers

- "Create a new skill specializing in PowerPoint slide design."
- "Optimize the module-architect skill to Lite format to save tokens."
- "Run evaluation (Eval) for the current skill set."
- "Audit this skill: is it token-efficient and does it have proper quality gates?"

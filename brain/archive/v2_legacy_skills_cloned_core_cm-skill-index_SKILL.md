---

name: cm-skill-index
description: "CORE — Nạp danh mục skills theo 3 lớp (index → tóm tắt → chi tiết) để tiết kiệm token."
version: 3.0.0
---

# cm-skill-index — Progressive Skill Catalog (LITE)

> **Goal:** Save 90%+ tokens through Progressive Disclosure. The agent loads only a lightweight index to select the right skill, then loads the full detail only when executing.

## When to Activate

- Starting a new session and need to orient across the full skill set
- Unsure which skill to use for a given task
- Looking up triggers or domain coverage for a specific area
- After installing a new skill — must register it in the index

## Instructions

### 3-Layer Loading Model

| Layer | Name | Content | Token Cost |
|-------|------|---------|------------|
| **L1** | **Index** | Name + Domain + Triggers. | ~100t / skill |
| **L2** | **Summary** | Description + Integration table. | ~300t / skill |
| **L3** | **Full** | Complete Instructions + Red Flags. | 1500t+ / skill |

### Core Skill Domains (L1 Quick Reference)

| Domain | Skills | Key Triggers |
|--------|--------|-------------|
| **`ToT —`** (Trainer) | `module-architect`, `teacher-needs`, `steam-content-factory`, `assessment-forge`, `unit-planner` | teacher training, ToT, lesson plan, slide training, audit |
| **`K-12 —`** (Student) | `k12-pbl-designer`, `k12-id-expert`, `k12-iot-scaffold`, `k12-math-expert`, `k12-science-inquiry` | student projects, PBL, experiments, math, robotics |
| **`CORE —`** (System) | `cm-planning`, `cm-terminal`, `cm-git-flow`, `cm-code-review`, `cm-codeintell`, `cm-start` | planning, terminal, git, review, system kickoff |
| **Orchestration** | `cm-execution`, `cm-continuity`, `cm-skill-mastery`, `cm-skill-chain` | execution, memory, skill routing, automation chains |
| **Docs/Publish** | `cm-dockit`, `cm-document-publishing`, `cm-auto-publisher` | documentation, B2B publish, Astro web push |

### Usage Protocol

1. **At Session Start:** Load Layer 1 Index (~2500 tokens) to map the full Kit.
2. **Task Matching:** Use Triggers to select the appropriate skill.
3. **Deep Dive:** Read Layer 2 (first 20 lines) if confirmation is needed.
4. **Execution:** Load Layer 3 (full `SKILL.md`) to begin implementing.

### Migration Compatibility

- Legacy `tot-*` IDs are mapped through `skill-alias-map.v5.json`.
- Router/index must resolve both legacy and canonical IDs during transition.

## Quality Gate (Red Flags)

- ❌ Loading all 66 `SKILL.md` files at session start (massive token waste).
- ❌ Using the wrong skill due to not checking Triggers at Layer 1.
- ❌ Forgetting to update the Index after installing a new skill.
- ❌ Mis-classifying a skill into the wrong domain, making it hard to discover.

## Example Triggers

- "List the available skills in the Kit."
- "Which skill supports Prisma database design?"
- "What skill should I use for a marketing blog task?"
- "Show me the L1 index of all available skills."

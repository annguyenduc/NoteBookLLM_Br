---


name: cm-skill-mastery
description: "CORE — Hướng dẫn lựa chọn và kích hoạt đúng skill theo ngữ cảnh."
version: 2.0.0
---

# cm-skill-mastery — Skill Selection & Activation (LITE)

> **The Meta-Skill:** The skill of skills. Governs Discovering, Using, and Creating skills within the Antigravity/CodyMaster ecosystem.

## When to Activate

- Unsure which skill to activate for a given task
- Setting up a new skill installation workflow
- Creating a new skill and need to follow the right format
- Routing a complex request across multiple skills in sequence

## Instructions

### Part A: Using Skills (Invocation Rules)

- **Invoke First:** Always invoke the relevant skill BEFORE providing an answer or taking action.
- **Decision Flow:** Is there a matching skill? (Even 1% match) → Read the skill → Follow it.
- **Priority order:**
  1. Process Skills (`cm-planning`, `cm-debugging`) — Define HOW to approach.
  2. Implementation Skills (`cm-tdd`, `cm-execution`) — Guide HOW to execute.

### Part B: Creating Skills (Bootstrap Rules)

- **Lite Structure:** Metadata → Goal → Rules/Tables → Quality Gate → Triggers.
- **SDD Standards:** Optimize for tokens (under 2.5KB), use tables over long prose, reference instead of copy-paste.

### Part C: Discovering Skills (Adaptive Search)

1. **Index Check:** Scan `cm-skill-index` (Layer 1).
2. **External Search:** `npx skills find "{keyword}"` on skills.sh.
3. **Review & Install:** Read `SKILL.md` → Ask user for approval → `npx skills add`.
4. **Log:** Record the installation in `.cm-skills-log.json`.

## Quality Gate (Red Flags)

- ❌ Assuming a task is "too simple" to need a skill (common mistake — always check first).
- ❌ Executing before checking for a relevant skill (leads to bypassing the Kit's workflow).
- ❌ Creating a new skill that duplicates an existing skill's functionality.
- ❌ Installing a skill from an unknown source without a safety review step.

## Example Triggers

- "Which skill should I use for this task?"
- "Install a skill that supports React Native."
- "Guide me on creating a new skill in the Lite format."
- "Route this complex request to the right combination of skills."

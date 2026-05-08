---
name: write-skill
description: Use when creating, editing, rewriting, or upgrading any SKILL.md file. Triggers on 'viết skill', 'sửa skill', 'nâng cấp skill', 'improve this skill', 'update the skill', or when a user shows you a SKILL.md and asks for feedback. Do NOT use for wiki content editing, ingest tasks, or general documentation outside skill folders.
---

# Write Skill

## Overview

Write skills as operational guides for another agent, not as project notes. Keep the body short, make the trigger description precise, and only document behavior that is true in the current environment.

**Before writing anything, figure out where the user is:**
- "I want to create a skill for X" → start from scratch (Workflow step 1)
- "Here's my SKILL.md, can you improve it?" → jump to step 2 (Audit & Diagnose)
- "Just fix the description" → jump to step 4 (Rewrite frontmatter)

---

## Required Reading

When editing a skill family for the first time in a session, read these reference files from the skill's `references/` folder if they exist:
- `references/superpowers-writing-skills.md`
- `references/anthropic-best-practices.md`
- `references/testing-skills-subagents.md`

Do not skip these if present. If absent, proceed without them.

---

## Workflow

### 1. Capture Intent
Understand what the skill should enable Claude to do. Extract from conversation history first — tools used, step sequence, corrections made, input/output formats. Ask user to fill gaps, then confirm before proceeding.

Key questions:
- What should this skill enable Claude to do?
- When should it trigger? (user phrases, contexts)
- What's the expected output format?
- Does it need test cases? (verifiable outputs → yes; subjective outputs → probably not)

### 2. Audit the Target
Read the existing `SKILL.md` (if any). List scripts, references, assets. Note:
- Hard-coded paths or platform-specific commands
- Legacy behavior that no longer applies
- Missing guardrails or safety constraints
- Description that describes process instead of trigger

### 3. Diagnose & Define Tests (if verifiable output)
Document why the current skill is weak. If the skill has objectively verifiable outputs, create a `tests/` directory and write a baseline test (RED phase) defining success criteria before rewriting.

### 4. Rewrite Frontmatter
- `name`: lowercase, hyphenated
- `description`: starts with `Use when...`, focuses on triggering conditions — not the workflow. Include specific phrases, contexts, and anti-triggers. Make it slightly "pushy" to counter Claude's tendency to under-trigger skills.

**Good description pattern:**
> "Use when X. Triggers on [phrases]. Also use when [edge cases]. Do NOT use for [anti-triggers]."

### 5. Rewrite Body (GREEN phase)
Preferred sections: `Overview`, `Workflow`, `Guardrails`, `Quick Reference`, `Common Mistakes`.

Rules:
- Reference scripts by **relative path** from `SKILL.md` (e.g., `scripts/init_skill.py`) — never absolute paths
- Move heavy detail into `references/` files instead of bloating `SKILL.md`
- Keep `SKILL.md` under 500 lines; add hierarchy + pointers if approaching limit
- For files >300 lines, include a table of contents

### 6. Validate
Re-read the final file and check:
- [ ] Trigger description focuses on conditions, not process
- [ ] No absolute/hardcoded paths
- [ ] Body matches what scripts in the folder can actually produce
- [ ] Critical safety rules are visible, not buried in examples
- [ ] References use plain paths, not `@file` links

Run validation script if available: `scripts/quick_validate.py <skill-folder>`

---

## Guardrails

- Do not describe commands or outputs the folder cannot actually produce
- Do not hide critical safety rules inside examples
- Do not use `@file` links inside skill prose — use plain relative paths
- Do not summarize the whole workflow in `description`; that encourages agents to skip the body
- Do not hardcode absolute paths or OS-specific separators — use relative paths and forward slashes
- Do not rewrite skills in batch without checking each folder's real scripts and constraints

---

## Quick Reference

Initialize a new skill (if `init_skill.py` is available in your environment):
```
python scripts/init_skill.py <skill-name> --path <parent-dir>
```

Validate a skill folder (if `quick_validate.py` is available):
```
python scripts/quick_validate.py <skill-folder>
```

Generate agent metadata (if `generate_openai_yaml.py` is available):
```
python scripts/generate_openai_yaml.py <skill-folder> --interface key=value
```

> Note: These scripts may live in a `.system/skill-creator/scripts/` directory relative to your skills root. Locate them before running — do not assume an absolute path.

---

## Common Mistakes

- `description` explains the process instead of the trigger → rewrite to focus on when/why
- `SKILL.md` promises behavior that only exists in a legacy or missing script
- Absolute paths hardcoded for one machine/OS → use relative paths
- Body duplicates long reference material instead of linking to it
- Skill rewritten in batch without checking each folder's actual scripts
- Write-heavy commands presented without warning about what they edit

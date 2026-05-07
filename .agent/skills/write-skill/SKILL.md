---
name: write-skill
description: Use when creating, editing, rewriting, or upgrading any SKILL.md file. Triggers on 'viết skill', 'sửa skill', 'nâng cấp skill'. Do NOT use for wiki content editing, ingest tasks, or general documentation outside .agent/skills/.
---

# Write Skill

## Overview
Write skills as operational guides for another agent, not as project notes. Keep the body short, make the trigger description precise, and only document behavior that is true in the current folder.

## Required Reading
- Read `.agent/skills/references/superpowers-writing-skills.md`.
- Read `.agent/skills/references/anthropic-best-practices.md`.
- Read `.agent/skills/references/testing-skills-subagents.md`.

Do not skip these files when editing a skill family for the first time in a session.

## Workflow
1. Audit the target folder before writing.
Read `SKILL.md`, list scripts, references, assets, and note any hard-coded paths, legacy behavior, or safety constraints.
2. Capture the baseline problem.
Document why the current skill is weak: bad trigger text, stale commands, missing guardrails, or structure that invites shortcut behavior.
3. Capture the baseline problem & Define Tests.
Document why the current skill is weak. **MANDATORY**: Create a `tests/` directory and write a baseline test script (RED phase) that defines the success criteria before writing the actual logic.
4. Rewrite the frontmatter.
Use lowercase hyphenated `name` and a `description` that starts with `Use when...` and focuses on triggering conditions, not the workflow.
5. Implementation (GREEN phase).
Write the minimum code in `scripts/` to pass the tests. Prefer `Overview`, `Guardrails`, `Workflow`, `Quick Reference`, and `Common Mistakes`. Reference scripts by path. Move heavy detail into separate files instead of bloating `SKILL.md`.
6. Refactor & Validate.
Optimize code and documentation. Re-read the final file for trigger quality, path correctness, and agreement with the actual scripts. Run the `quick_validate.py` script and ensure all tests in `tests/` are GREEN.

## Guardrails
- Do not describe commands or outputs that the folder cannot actually produce.
- Do not hide critical safety rules inside examples.
- Do not use `@file` links inside skill prose; use plain paths.
- Do not summarize the whole workflow in `description`; that encourages the agent to skip the body.
- Keep references one level deep from `SKILL.md`.
- Prefer forward-slash paths in documentation, even on Windows.

## Quick Reference
- Initialize a new skill only when the folder does not already exist:
  `python D:/anngu/.codex/skills/.system/skill-creator/scripts/init_skill.py <skill-name> --path <parent-dir>`
- Validate a skill folder:
  `python D:/anngu/.codex/skills/.system/skill-creator/scripts/quick_validate.py <skill-folder>`
- Regenerate agent metadata when needed:
  `python D:/anngu/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py <skill-folder> --interface key=value`

## Common Mistakes
- `description` explains the process instead of the trigger.
- `SKILL.md` promises behavior that only exists in a legacy script.
- A write-heavy command is presented without any warning about what it edits.
- The body duplicates long reference material instead of linking to it.
- A skill is rewritten in batch without checking each folder's real scripts and constraints.

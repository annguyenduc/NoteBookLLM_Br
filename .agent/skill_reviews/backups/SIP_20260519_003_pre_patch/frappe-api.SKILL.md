---


name: frappe-api
description: "CORE — Tham chiếu Frappe Python và JavaScript API bao gồm thao tác document, truy vấn database, tiện ích và các mẫu REST API."
version: 1.0.0
---
# Frappe Api

## Goal
Execute the `frappe-api` workflow safely and consistently.
Scope trigger is defined in frontmatter description.

## Instructions
- Parse user intent and confirm this skill is the best semantic match.
- Produce a concise execution plan before modifying files or running commands.
- Run the minimum set of actions required to complete the task.
- Validate output quality before returning the final result.
- Use `references/` as source-of-truth when domain rules are ambiguous.

## Examples
- User asks for work aligned with `frappe-api`.
- The task semantics clearly match the frontmatter description.
- The workflow requires the policy/rules packaged in this skill.

## Constraints
- Do not run destructive actions without explicit user approval.
- Do not fabricate outputs when evidence or validation is missing.
- Keep changes auditable and summarize assumptions explicitly.

## Legacy Notes
- Original pre-migration body is preserved in `references/legacy_body.vi.md`.

## Quality Gate
- Frontmatter is valid YAML and includes required keys.
- Description remains in Vietnamese and is readable on Windows editors.
- Body content is in English and free from mojibake artifacts.
- Links resolve correctly with relative paths where applicable.

## Example Triggers
- "Plan this task before implementation."
- "Route this request to the right skills."
- "Audit the skill and report risks."

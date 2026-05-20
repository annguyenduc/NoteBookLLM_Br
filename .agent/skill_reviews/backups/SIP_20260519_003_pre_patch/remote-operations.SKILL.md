---


name: remote-operations
description: "CORE — Các mẫu REST API và phương pháp hay nhất để quản lý các trang Frappe/ERPNext từ xa."
version: 1.0.0
---
# Remote Operations

## Goal
Execute the `remote-operations` workflow safely and consistently.
Scope trigger is defined in frontmatter description.

## Instructions
- Parse user intent and confirm this skill is the best semantic match.
- Produce a concise execution plan before modifying files or running commands.
- Run the minimum set of actions required to complete the task.
- Validate output quality before returning the final result.
- Use `references/` as source-of-truth when domain rules are ambiguous.

## Examples
- User asks for work aligned with `remote-operations`.
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

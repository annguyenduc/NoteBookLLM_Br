---


name: cm-core-edit
description: "CORE — \"LITE — Kích hoạt khi cần chỉnh sửa file (refactor, fix log, add logic). Áp dụng phương pháp 'Minimalist In-place Editing' (giống Claude Code FileEditTool) để bảo toàn cấu trúc file, giảm thiểu token và tránh xung đột mã nguồn.\""
version: 2.0.0
---

# cm-core-edit — Minimalist File Editing (LITE)

> **Goal:** Modify source code "surgically" — performing targeted replacement of only the necessary segment rather than overwriting the entire file.

## When to Activate

- Fixing a specific bug in a known location
- Refactoring a single function or variable
- Adding a comment, log line, or small logic branch
- Any file edit where the change is ≤ 20% of the file

## Instructions

### Execution Workflow

1. **Read & Contextualize:** Use `view_file` to identify the exact line numbers and code segment to replace.
2. **Target Selection:** Define `TargetContent` as a UNIQUE and sufficiently long string — long enough that it cannot be confused with other occurrences.
3. **Diff Validation:** Mentally simulate the change before executing `replace_file_content`.
4. **Verification:** After editing, always call Terminal or TDD to confirm the logic is not broken.

## Pro Tips (Inspired by Claude Code FileEditTool)

- **Token Efficiency:** Pass the narrowest possible `TargetContent` — no more than needed to uniquely identify the target.
- **Context Preservation:** Keep surrounding comments and structure intact.
- **Atomic Operations:** Each edit should be one complete logical unit. Do not bundle unrelated changes.

## Quality Gate (Red Flags)

- ❌ Editing a file without first reading its current content (`view_file`).
- ❌ Overwriting an entire file (> 100 lines) when only 1-2 logic lines need to change.
- ❌ Using `ReplacementContent` that does not match the surrounding indentation and context.
- ❌ Editing multiple unrelated blocks in a single tool call when separate calls would be safer.

## Example Triggers

- "Fix the typo in this file."
- "Refactor the `calculate_total` function to use `sum()`."
- "Add a comment at the top of the logic file."
- "Update the environment variable value in this JSON config."

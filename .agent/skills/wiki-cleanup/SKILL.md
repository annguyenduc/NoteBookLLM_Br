---
name: wiki-cleanup
description: "Use when broken links, stale content (not updated in 30+ days), or structural inconsistencies are detected in Wiki Atoms. Also triggers on /cleanup command or after a large ingest batch."
---

Maintain and audit the quality of the Wiki system through linting and structure verification.

## Context
A high-quality Wiki requires consistent structure, valid links, and up-to-date information. `wiki-cleanup` ensures cognitive integrity.

## Workflow

### Step 1: Quality Linting
Run the `lint_engine.py` to detect structural errors.
```bash
python .agent/skills/wiki-cleanup/scripts/lint_engine.py
```
Checks performed:
- **Broken Links**: Internal `[[ ]]` links pointing to non-existent files.
- **Stale Content**: Files not updated for over 30 days.
- **Formatting**: Markdown linting and metadata compliance.

### Step 2: The Steve Jobs Test
Apply a "Simple and Perfect" philosophy. Flag atoms with structural errors for human review. If a concept is overly complex, suggest a **Refactor** to simplify.

### Step 3: Automatic Healing
Automatically fix minor issues:
- Remove trailing whitespace.
- Standardize Metadata headers.

## Constraints
- **NEVER** delete files in `raw/`.
- All automated changes must be logged in `3-resources/wiki/log.md`.

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
description: Use when the wiki needs structural linting for broken links, missing template sections, or consistency drift, especially after batch edits, ingest, absorb, or rebuild work.
---

# Wiki Cleanup

## Overview
Audit wiki structure first, then fix only the issues the scripts are designed to handle. The main linter checks links and required template sections; other scripts are support utilities, not a blanket auto-heal system.

## Guardrails
- Default to read-only linting.
- `--fix` writes changes into `3-resources/wiki/`; use it only when those changes are intended.
- Never use this skill against `3-resources/raw/`.
- Separate structural cleanup from factual review. A clean file can still contain bad claims.

## Workflow
1. Run the main audit:
   `python .agent/skills/wiki-cleanup/scripts/lint_engine.py`
2. Inspect the reported issue types and decide whether scriptable fixes are appropriate.
3. If the fixes are acceptable, run:
   `python .agent/skills/wiki-cleanup/scripts/lint_engine.py --fix`
4. Review the modified files and recent task logs before closing the cleanup pass.

## Quick Reference
- Main linter:
  `lint_engine.py`
- Vault-wide health support:
  `brain_lint.py`
- Other support utilities:
  `dense_linker.py`, `consolidation_engine.py`, `retention_manager.py`

## Common Mistakes
- Running `--fix` without checking what the script actually edits.
- Confusing broken-link repair with knowledge reconciliation.
- Treating missing `4F Reflection` sections as proof of content quality.

---
name: wiki-md-auditor
description: "Use when evaluating Markdown quality, fixing font artifacts (ligatures), and standardizing asset naming with prefixes before promotion to raw_ingest/. MANDATORY: Must follow TDD protocols."
---

# Wiki Markdown Auditor

## Overview
The Markdown Auditor acts as the primary Quality Gate at the `00_Inbox` Processing Hub. It ensures that only high-fidelity, clean Markdown files with standardized asset links are promoted to the permanent Wiki infrastructure.

## Guardrails
- **Immutable Gate**: Never promote a file that has a quality score < 90% or broken image links.
- **Prefix Standard**: All assets must be renamed using the source filename as a prefix (e.g., `DOCNAME_fig_01.png`).
- **3-Flatten Compliance**: Assets must be moved to the flat `raw_assets/` directory.

## Workflow
1. **Audit**: Run the auditor script on a Markdown file in `00_Inbox`.
2. **Analysis**: The script scans for noise (ligatures), structural integrity, and link validity.
3. **Standardization**:
   - Renames local images.
   - Updates Markdown links to point to `../raw_assets/`.
4. **Promotion**: If successful, the `@librarian` moves the file to `raw_ingest/` and images to `raw_assets/`.

## Quick Reference
- Run Audit (Dry Run):
  `python .agent/skills/wiki-md-auditor/scripts/md_auditor.py "00_Inbox/file.md" --dry-run`
- Run and Standardize:
  `python .agent/skills/wiki-md-auditor/scripts/md_auditor.py "00_Inbox/file.md" --fix`

## Testing
This skill is developed using **TDD**.
Run tests:
```powershell
$env:PYTHONPATH=".agent/skills/wiki-md-auditor/scripts"; python .agent/skills/wiki-md-auditor/tests/test_md_auditor.py
```

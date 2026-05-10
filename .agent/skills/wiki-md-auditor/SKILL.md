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
- **Promotion Safety**: Never run `promote.py` on a file without a `PASSED` audit stamp.
- **Validation First**: Always run `--dry-run` before the real promote to confirm paths.

## Audit Stamp Schema
The `md_auditor.py --fix` command writes a YAML block to the file frontmatter:
```yaml
audit:
  score: 0.95        # actual float score (1.0 base)
  date: "YYYY-MM-DD" # date of audit
  status: "PASSED"   # or FAILED
  auditor: "v1.0"
```
> [!IMPORTANT]
> `promote.py` will reject any file where `status != PASSED` or the `date` is older than 7 days.

## Workflow
1. **Step 1 — Audit & Fix**:
   Run `md_auditor.py` with the `--fix` flag on a Markdown file in `00_Inbox`.
   ```powershell
   python .agent/skills/wiki-md-auditor/scripts/md_auditor.py "00_Inbox/Converted_Sources/XXX/RAW_XXX.md" --fix
   ```
   **Output**: The script standardizes links, copies assets to `raw_assets/`, and writes the **Audit Stamp** to the frontmatter.

2. **Step 2 — Promote**:
   Execute `promote.py` only after a `PASSED` audit.
   ```powershell
   # Preview first
   python .agent/skills/wiki-md-auditor/scripts/promote.py "00_Inbox/Converted_Sources/XXX/RAW_XXX.md" --dry-run
   # Execute
   python .agent/skills/wiki-md-auditor/scripts/promote.py "00_Inbox/Converted_Sources/XXX/RAW_XXX.md"
   ```
   **Output**: The `.md` file moves to `raw_ingest/`, the original PDF is archived to `raw_sources/`, and the temporary folder is deleted.

## Quick Reference
- **Step 1: Audit & Fix**
  `python .agent/skills/wiki-md-auditor/scripts/md_auditor.py "00_Inbox/Converted_Sources/RAW_file.md" --fix`
- **Step 2: Promote (Dry Run)**
  `python .agent/skills/wiki-md-auditor/scripts/promote.py "00_Inbox/Converted_Sources/RAW_file.md" --dry-run`
- **Step 3: Promote (Execute)**
  `python .agent/skills/wiki-md-auditor/scripts/promote.py "00_Inbox/Converted_Sources/RAW_file.md"`

## Testing
This skill is developed using **TDD**.
Run tests:
```powershell
$env:PYTHONPATH=".agent/skills/wiki-md-auditor/scripts"; python .agent/skills/wiki-md-auditor/tests/test_md_auditor.py; python .agent/skills/wiki-md-auditor/tests/test_promote.py
```

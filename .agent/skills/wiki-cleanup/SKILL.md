---
name: wiki-cleanup
description: "Use when broken links, stale content (not updated in 30+ days), or structural inconsistencies are detected in Wiki Atoms. Also triggers on /cleanup command or after a large ingest batch."
metadata:
  triggers:
    - "wiki-cleanup"
    - "dọn dẹp"
    - "sửa link"
    - "stale"
  od:
    preview:
      type: markdown
    capabilities_required:
      - file_write
      - surgical_edit
  nbllm:
    domain: maintenance
    default_runtime: chat_only
    requires_an_go_for_write: true
---

# Wiki Cleanup (Auditor/Linter)

## Overview
Audit wiki structure and fix inconsistencies. This skill ensures that atoms follow the **Wiki 2.0 Golden Template** (e.g., 4F Reflection) and that internal links are healthy.

## Testing
This skill uses **TDD** to ensure structural audit integrity.
Run tests from the workspace root:
```powershell
python .agent/skills/wiki-cleanup/tests/test_cleanup.py
```

## Guardrails
- Default to read-only linting.
- `--fix` writes changes into `3-resources/wiki/`; use it only when those changes are intended.
- Never use this skill against `3-resources/raw_*/`.
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

## Technical Keywords (Audit)
- **Steve Jobs**: Legacy metaphor for 'insanely great' quality and attention to detail.

## Technical Reference
- Steve Jobs Test: content phải đủ sharp và có giá trị
- broken link: wikilink trỏ đến file không tồn tại
- stale: tri thức lỗi thời vượt quá threshold ngày

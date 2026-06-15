---
name: wiki-crawl-4ai
description: "Use when capturing dynamic URL content or when visual screenshot evidence (R10) is mandatory. MANDATORY: Use ONLY for staging to 00_Inbox/. Prohibited for direct raw/ writing."
---

# Wiki Crawl 4AI (Flexible/Visual)

## Overview
A high-fidelity staging skill for capturing dynamic content and visual proof. It supports both **Headful** (for bot-bypass) and **Headless** (for speed/automation) modes. Essential for fulfilling **R10 (Search & Visual Validation)**.

## Testing
This skill uses **TDD** to ensure visual evidence capture.
Run tests from the workspace root:
```powershell
python .agent/skills/wiki-crawl-4ai/tests/test_crawl.py
```

## Guardrails
- **STAGING BOUNDARY**: NEVER save output directly into `3-resources/raw_*/`. Always use `00_Inbox/`.
- **VISUAL MANDATE**: The `--screenshot` flag is REQUIRED when R10 applies.
- **AUDIT GATE**: You MUST open and verify the `.png` screenshot for quality (no blank pages/404s) before passing to ingest.

## Workflow
1. Select a staging path in `00_Inbox/`.
2. Run crawler:
   `python .agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py --url "<url>" --output "00_Inbox/<name>.md" --screenshot`
3. Confirm existence of both `.md` and `.png`.
4. Pass the verified staging folder/files to the official `/ingest` flow via `ingest-lifecycle`.

## Handoff Rule
- `wiki-crawl-4ai` ends at staged inbox artifacts plus verified screenshot evidence.
- Official ingest must continue through `ingest-lifecycle`; do not hand off a fresh run directly to `wiki-ingest`.

## Quick Reference
- `python .agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py --url <URL> --output 00_Inbox/<name>.md --screenshot --headless`

## Common Mistakes & Rationalizations
| Excuse | Reality |
|--------|---------|
| "The site is public, no need for inbox" | All external data must be staged for audit. No exceptions. |
| "I'll skip the screenshot to save time" | Violation of R10. Visual proof is mandatory for truth-seeking. |
| "The screenshot is generated, so it's fine" | Automation can fail. You must verify the actual image content. |

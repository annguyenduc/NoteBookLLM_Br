---
name: wiki-web-scrape
description: Use when capturing text-only content from static URLs for knowledge ingestion. MANDATORY: Use ONLY for staging content to 00_Inbox/. Prohibited for direct writing to 3-resources/raw_*/.
---

# Wiki Web Scrape (Resilient/Hybrid)

## Overview
A resilient staging skill that captures raw page text. It prefers **Lightpanda** (via CDP) for lightweight execution but automatically falls back to **Standard Chromium** if the Lightpanda server is unavailable. Its sole purpose is to move external data into the `00_Inbox/` for human review and formal ingestion.

## Testing
This skill uses **TDD** to ensure scraping resilience.
Run tests from the workspace root:
```powershell
python .agent/skills/wiki-web-scrape/tests/test_scrape.py
```

## Guardrails
- **STAGING BOUNDARY**: NEVER write directly to `3-resources/raw_*/`. This area is immutable for agents (Rule R1).
- **STAGING TARGET**: All outputs MUST be saved in `00_Inbox/`.
- **NO VISUALS**: If the task requires visual evidence (Rule R10), STOP and use `wiki-crawl-4ai`.

## Workflow
1. Verify the URL is static and public.
2. Run staging command:
   `python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url "<url>" --output "00_Inbox/<filename>.md"`
3. Verify output quality in the inbox.
4. Pass verified file to `wiki-ingest`.

## Quick Reference
- `python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url <URL> --output 00_Inbox/<name>.md`

## Common Mistakes & Rationalizations
| Excuse | Reality |
|--------|---------|
| "It's faster to write to raw/" | Violation of R1/R12. Speed does not justify breaking system integrity. |
| "I'll review it later in raw/" | Raw is the Source of Truth; it must be clean *before* entry. |
| "The page looks simple enough" | If it has complex JS, Lightpanda will return empty text. Switch to crawl-4ai. |

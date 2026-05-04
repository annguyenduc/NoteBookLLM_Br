---
name: wiki-web-scrape
description: "Use when quickly scraping a static or server-rendered URL for raw content. Prefer over wiki-crawl-4ai for simple pages that do not require JavaScript rendering or screenshot evidence. Output goes to raw/ only — not atomized."
---

High-speed technical documentation scraping using Lightpanda.

## Context
Acquire raw data from URLs quickly. This skill is for data acquisition only; use `wiki-ingest` for atomization.

## Workflow
1. Provide a target URL.
2. Run the Lightpanda scraper.
3. Save the raw output to `3-resources/raw/`.

## Execution
```bash
python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py "URL"
```

## Constraints
- Do not use for authenticated pages.
- Respect robots.txt.
description: Use when a simple public page needs fast text extraction without heavy rendering and screenshot evidence is not required; prefer this before `wiki-crawl-4ai` for straightforward pages.
---

# Wiki Web Scrape

## Overview
Use the Lightpanda-based scraper for quick acquisition of simple page text. This is a staging skill for raw capture, not a direct ingest or synthesis step.

## Guardrails
- Save output to `00_Inbox/` or another user-approved staging location, not directly into `3-resources/raw/`.
- Do not use this skill for authenticated pages or for pages that require Rule 10 screenshot evidence.
- If the page is dynamic or badly rendered, stop and switch to `wiki-crawl-4ai`.

## Workflow
1. Confirm the page is public and simple enough for lightweight scraping.
2. Run:
   `python .agent/skills/wiki-web-scrape/scripts/lightpanda_scrape.py --url "<url>" --output "00_Inbox/page.md"`
3. Inspect the captured markdown/text for completeness.
4. If the capture is good, pass the saved file to `wiki-ingest`.

## Quick Reference
- Required arguments:
  `--url`, `--output`
- Runtime assumption:
  the script connects to an existing Lightpanda CDP endpoint at `http://127.0.0.1:9222`

## Common Mistakes
- Writing directly into the immutable raw area.
- Using the fast scraper for JavaScript-heavy or visually sensitive pages.
- Forgetting that this step only captures content; it does not register atoms.

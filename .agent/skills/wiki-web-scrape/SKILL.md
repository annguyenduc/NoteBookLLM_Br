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

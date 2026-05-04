---
name: wiki-web-scrape
description: "Thu thập dữ liệu thô từ web với tốc độ cao bằng Lightpanda."
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

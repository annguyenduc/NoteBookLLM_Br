---
name: wiki-crawl-4ai
description: "Use when a URL requires high-fidelity Markdown extraction with JavaScript rendering, or when visual screenshot evidence (Rule 10) is mandatory. Prefer over wiki-web-scrape for complex/dynamic pages."
---

High-fidelity web crawling for structured markdown and visual evidence.

## Context
Used when high structural fidelity or visual proof is required for ingestion.

## Workflow
1. Provide a target URL.
2. Execute Crawl4AI to extract structured Markdown and capture screenshots (Rule 10).
3. Verify content before final capture to avoid "garbage" data.

## Execution
```bash
python .agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py "URL"
```

## Constraints
- **Rule 10 Compliance**: Must verify content before visual capture.
- Output high-fidelity Markdown only.

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
description: Use when a public URL needs JavaScript rendering, higher-fidelity markdown extraction, or screenshot evidence that must satisfy Rule 10 before the content can enter the wiki pipeline.
---

# Wiki Crawl 4AI

## Overview
Use Crawl4AI for dynamic pages and for any scrape that must produce a screenshot of real page content. This is the higher-fidelity option compared with the fast Lightpanda scraper.

## Guardrails
- Save output to `00_Inbox/` or another user-approved staging path, not directly into `3-resources/raw/`.
- Use `--screenshot` when Rule 10 evidence is required.
- Inspect the image afterward. If the screenshot does not clearly show the target content, stop and report failure.
- Do not use this skill as an ingest substitute; crawl first, ingest later.

## Workflow
1. Choose an output markdown path in a staging location.
2. Run:
   `python .agent/skills/wiki-crawl-4ai/scripts/crawl4ai_run.py --url "<url>" --output "00_Inbox/page.md" --screenshot`
3. Verify that both the markdown and the `.png` evidence file were created.
4. Read the captured output before passing it to `wiki-ingest`.

## Quick Reference
- Required arguments:
  `--url`, `--output`
- Optional evidence flag:
  `--screenshot`
- Output pattern:
  markdown file plus sibling `.png` when screenshots are enabled

## Common Mistakes
- Saving crawler output directly into the immutable raw area.
- Claiming Rule 10 compliance without opening the screenshot result.
- Using this heavier workflow for a simple static page that `wiki-web-scrape` could handle.

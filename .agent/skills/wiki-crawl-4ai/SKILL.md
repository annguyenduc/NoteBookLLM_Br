---
name: wiki-crawl-4ai
description: "Cào dữ liệu web cấu trúc cao (Markdown/Screenshot) bằng Crawl4AI."
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

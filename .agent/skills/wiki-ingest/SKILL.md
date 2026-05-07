---
name: wiki-ingest
description: "Use when raw knowledge sources (PDF, Markdown, HTML, Office) need to be atomized, hash-verified, and integrated into the Wiki 2.0 review queue. Triggers on /ingest command or when new files appear in 00_Inbox/, 3-resources/raw_sources/, or 3-resources/raw_ingest/."
---

# Wiki Ingest

## Overview
Register a source file into the wiki pipeline without altering the raw source. This skill is for file-based ingestion, not for live web crawling.

## Guardrails
- Treat `3-resources/raw_*/` as read-only for general agents.
- For URLs, use `wiki-web-scrape` or `wiki-crawl-4ai` first, save to `00_Inbox/` or another user-approved staging path, then ingest the saved file.
- Do not claim a source is verified just because ingestion succeeded. `ingest.py` creates `DRAFT`.
- Preserve source traceability. If the source section is unclear, flag it instead of inventing one.

## Workflow
1. Confirm the input path exists and is already on disk.
Preferred inputs are files in `00_Inbox/`, `3-resources/raw_sources/`, or `3-resources/raw_ingest/`.
2. Inspect routing before ingestion.
Run `python .agent/skills/wiki-ingest/scripts/magika_router.py "<path>"` to confirm MIME type and parser choice.
3. Run the deterministic ingest step.
Run `python .agent/skills/wiki-ingest/scripts/ingest.py "<path>"`.
4. Verify the outcome.
Check console output or DB/task logs for one of these outcomes: skipped duplicate, rejected raw mutation, or successful `DRAFT` atom plus `review_queue` entry.

## Quick Reference
- Route a file:
  `python .agent/skills/wiki-ingest/scripts/magika_router.py "00_Inbox/example.pdf"`
- Ingest a file:
  `python .agent/skills/wiki-ingest/scripts/ingest.py "00_Inbox/example.pdf"`
- Supporting scripts:
  `score_engine.py` computes confidence.
  `wiki_ingest_helper.py` and `pressure_test.py` are support and test utilities.

## Testing
This skill uses **TDD** to ensure ingestion safety and duplicate detection logic.
Run tests from the workspace root:
```powershell
$env:PYTHONPATH=".agent/skills/wiki-ingest/scripts"; python .agent/skills/wiki-ingest/tests/test_ingest.py
```

## Common Mistakes
- Trying to ingest a URL directly instead of a saved file.
- Writing new web output straight into `3-resources/raw_*/`.
- Assuming ingestion updates wiki pages; this step only registers atoms and review items.
- Ignoring a raw hash mismatch warning, which is a signal to stop.

## Technical Keywords (Audit)
- **Gate**: TDD standard for operational readiness.
- **IMMUTABLE**: R1 Safety rule for raw sources.

## Technical Reference
- Gate -1: Magika content router
- Gate 0: Parse and create DRAFT atom
- Gate 1: Score engine (confidence threshold)
- IMMUTABLE: raw_sources/ must never be modified

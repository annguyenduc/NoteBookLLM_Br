---
name: wiki-ingest
description: "Use when raw knowledge sources (PDF, Markdown, HTML, Office) need to be atomized, hash-verified, and integrated into the Wiki 2.0 review queue. Triggers on /ingest command or when new files appear in 00_Inbox/ or 3-resources/raw/."
---

Standardized ingestion protocol to atomize raw sources with absolute traceability.

## Context
Process raw files from `00_Inbox/` or `3-resources/raw/` into structured Knowledge Atoms (DRAFT).

## Workflow

### Step 1: Content Identification
Use Magika to identify MIME-types regardless of extension.
```bash
python .agent/skills/wiki-ingest/scripts/magika_router.py "path/to/file"
```

### Step 2: High-Fidelity Extraction
Use specialized parsers:
- **PDF**: Docling (preferred).
- **HTML/URL**: `wiki-crawl-4ai`.
- **Office**: MarkItDown.

### Step 3: Atomic Registration
Run `ingest.py` to check for duplicates (SHA-256) and create DRAFT atoms.
```bash
python .agent/skills/wiki-ingest/scripts/ingest.py "path/to/file"
```

## Constraints
- **Rule 1 - Immutable Raw**: Never modify files in `raw/`.
- **Rule 3 - Source Tracing**: Every claim must have a valid source link.
- **Rule 8 - Human Gate**: Default status is always `DRAFT`.
description: Use when a file already exists in `00_Inbox/` or `3-resources/raw/` and needs routing, duplicate checks, confidence scoring, and DRAFT registration in `wiki_brain.db` and the review queue.
---

# Wiki Ingest

## Overview
Register a source file into the wiki pipeline without altering the raw source. This skill is for file-based ingestion, not for live web crawling.

## Guardrails
- Treat `3-resources/raw/` as read-only.
- For URLs, use `wiki-web-scrape` or `wiki-crawl-4ai` first, save to `00_Inbox/` or another user-approved staging path, then ingest the saved file.
- Do not claim a source is verified just because ingestion succeeded. `ingest.py` creates `DRAFT`.
- Preserve source traceability. If the source section is unclear, flag it instead of inventing one.

## Workflow
1. Confirm the input path exists and is already on disk.
Preferred inputs are files in `00_Inbox/` or user-managed files in `3-resources/raw/`.
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

## Common Mistakes
- Trying to ingest a URL directly instead of a saved file.
- Writing new web output straight into `3-resources/raw/`.
- Assuming ingestion updates wiki pages; this step only registers atoms and review items.
- Ignoring a raw hash mismatch warning, which is a signal to stop.

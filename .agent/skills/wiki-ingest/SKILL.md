---
name: wiki-ingest
description: "Nạp nguồn tri thức mới (PDF, Office, Web) vào Wiki Review Queue."
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

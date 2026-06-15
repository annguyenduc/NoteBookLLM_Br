---
name: wiki-hd-convert
description: Use when raw PDF sources contain critical visual information (charts, diagrams, tables) that must be preserved as images and linked within the Markdown output for high-fidelity Wiki ingestion.
---

# Wiki HD Convert (Docling Engine)

## Overview
This skill leverages the **Docling Engine** (IBM) to convert complex PDF documents into high-fidelity Markdown. Unlike basic text extractors, this engine preserves document layout, extracts charts/images, and automatically generates markdown links for visual assets. It supports **Intelligent Chunking** to handle large documents without memory exhaustion.

## Guardrails
- **R1 — Immutable Raw**: NEVER write results directly to `3-resources/raw_*/`. Always output to `00_Inbox/Converted_Sources/` for user review.
- **R12 — Vietnamese Safety**: All output Markdown files MUST be saved with **UTF-8 no BOM** encoding.
- **Asset Integrity**: Extracted images must be stored in an `images/` subfolder relative to the Markdown file to maintain linking integrity.
- **R-NAMING**: Output files without the RAW_ prefix will be rejected by wiki-md-auditor.
- **Chunking Strategy**: Prefer `chapter -> section -> page` using PDF outline/bookmarks when available. Use `--chunk-size` only as the max-page fallback inside a large section, or as page-window fallback when the PDF has no usable structure metadata.
- **Phase A Runtime Note**: Converted outputs may be copied or referenced into `runs/ingest_*/` before audit. `runs/` is transient runtime state, not canonical knowledge storage.


## Workflow
1. **Identification**: Identify the target PDF in `00_Inbox/`. The PDF stays here until conversion is complete.
2. **Execution**: Run `hd_converter.py` with the PDF path. For structured PDFs, the converter should emit a manifest plus section chunks from the PDF outline. Use `--chunk-size 15` as the max-page fallback, not as the first-choice chunk boundary.
3. **Verification**: Check the generated manifest and Markdown chunks in `00_Inbox` to ensure images and tables are preserved and that chunk boundaries follow `chapter -> section -> page`.
4. **Run Package Handoff (Phase A)**: A runner may copy or reference these outputs into `runs/ingest_*/` to build `state.json`, `manifest.md`, `outline.md`, reports, and logs before audit/promote.
5. **Archiving**: After successful conversion, move the original PDF from `00_Inbox/` to `3-resources/raw_sources/` to satisfy R1 (Immutable Raw).

## Output Naming Convention
Canonical outputs under `00_Inbox/Converted_Sources/`:
- Manifest: `RAW_[YYYY-MM-DD]_[original-filename]_MANIFEST.md`
- Structure chunk: `RAW_[YYYY-MM-DD]_[original-filename]_[UNIT_ID]_P[start]-[end].md`

## Quick Reference

### Convert PDF to HD Markdown (Single File)
```powershell
.\.venv\Scripts\python.exe .agent/skills/wiki-hd-convert/scripts/hd_converter.py "path/to/source.pdf"
```

### Convert Large PDF with Chunking
```powershell
.\.venv\Scripts\python.exe .agent/skills/wiki-hd-convert/scripts/hd_converter.py "path/to/source.pdf" --chunk-size 15
```

## Common Mistakes
- **Wrong Tooling**: Using MarkItDown for image-heavy PDFs (MarkItDown is better for spreadsheets/text-only docs).
- **Broken Links**: Moving the Markdown file without its accompanying `images/` folder.
- **Rule Violation**: Attempting to bypass Rule R1 by modifying the script output path to `raw/`.

## Testing
This skill uses **TDD** (Test-Driven Development) to ensure visual asset integrity.
Run the following command from the workspace root to verify the skill:
```powershell
$env:PYTHONPATH=".agent/skills/wiki-hd-convert"; python .agent/skills/wiki-hd-convert/tests/test_hd_converter.py
```

## Resources

### scripts/
- `hd_converter.py`: Core conversion script using Docling v2.x with picture generation enabled.

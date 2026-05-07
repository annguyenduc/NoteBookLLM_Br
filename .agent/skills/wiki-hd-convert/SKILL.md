---
name: wiki-hd-convert
description: Use when raw PDF sources contain critical visual information (charts, diagrams, tables) that must be preserved as images and linked within the Markdown output for high-fidelity Wiki ingestion.
---

# Wiki HD Convert (Docling Engine)

## Overview
This skill leverages the **Docling Engine** (IBM) to convert complex PDF documents into high-fidelity Markdown. Unlike basic text extractors, this engine preserves document layout, extracts charts/images, and automatically generates markdown links for visual assets.

## Guardrails
- **R1 — Immutable Raw**: NEVER write results directly to `3-resources/raw_*/`. Always output to `00_Inbox/Converted_Sources/` for user review.
- **R12 — Vietnamese Safety**: All output Markdown files MUST be saved with **UTF-8 no BOM** encoding.
- **Asset Integrity**: Extracted images must be stored in an `images/` subfolder relative to the Markdown file to maintain linking integrity.

## Workflow
1. **Identification**: Identify the target PDF in `3-resources/raw_sources/`.
2. **Execution**: Run `hd_converter.py` with the PDF path.
3. **Verification**: Check the generated Markdown in `00_Inbox` to ensure `<!-- image -->` placeholders are replaced with actual image links (e.g., `![Image](images/chart_0.png)`).

## Quick Reference

### Convert PDF to HD Markdown
```powershell
python .agent/skills/wiki-hd-convert/scripts/hd_converter.py "path/to/source.pdf"
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

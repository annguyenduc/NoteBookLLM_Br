# Ingest Spec: Global Map + Naming Lock

## Ngôn ngữ artifact

Spec này quy định:

- metadata có thể giữ tiếng Anh hoặc canonical enum để máy đọc ổn định
- phần nội dung markdown cho human review phải viết bằng tiếng Việt

Giữ nguyên tiếng Anh cho:

- `source_id`
- filenames
- status enums
- code
- exact source title
- technical terms khi chưa có bản dịch ngắn gọn, nhưng nên giải thích bằng tiếng Việt ở lần đầu xuất hiện

Áp dụng cho toàn bộ artifact downstream:

- `STRUCTURE_[ID].md`
- `FIGURES_[ID].md`
- `MAP_[ID].md`
- `NAMING_LOCK_[ID].md`
- `Analysis_[ID]_MASTER_STRATEGY.md`
- `Analysis_[ID]_CHUNK_XX.md`
- các report ingest

## Goal

Stabilize ingest for large PDFs by separating:
- `Primary ingest file` as the canonical reading input
- `Source Map` as the global context unit
- `Chunk` as the evidence unit
- `Naming Lock` as the identity unit

This prevents filename drift, title drift, and chunk-level hallucination.

## Pre-Phase: Ingest Input Lock

Before Phase 0 begins, lock three fields:

- `source_evidence_file`
- `primary_ingest_file`
- `source_id`

Rules:
- `source_evidence_file` is the original source artifact, such as the PDF.
- `primary_ingest_file` is the one canonical text artifact the workflow reads by default.
- For large PDFs, the PDF is evidence, not the default ingest-reading file.
- All downstream artifacts must point back to the same `primary_ingest_file`.
- One source must not have multiple competing primary ingest files in the same ingest run.

## Golden Test Case

- Source file: `00_Inbox/ARCH_Thinking_in_Systems.pdf`
- Source ID: `ARCH_TIS`
- Title slug: `Thinking_in_Systems`

Locked ingest inputs:
- `source_evidence_file`: `00_Inbox/ARCH_Thinking_in_Systems.pdf`
- `primary_ingest_file`: `TBD - must be locked before Phase 0`
- `source_id`: `ARCH_TIS`

Canonical outputs:
- `1-projects/MAP_ARCH_TIS.md`
- `1-projects/NAMING_LOCK_ARCH_TIS.md`
- `1-projects/Analysis_ARCH_TIS_MASTER_STRATEGY.md`
- `1-projects/Analysis_ARCH_TIS_CHUNK_01.md`
- `3-resources/wiki/sources/SOURCE_ARCH_TIS_Thinking_in_Systems.md`

## Naming Contract

Use `ID` as the only identity anchor. Do not use `PREFIX` in this workflow.

Canonical filename forms:
- Source node: `SOURCE_[ID]_[TITLE_SLUG].md`
- Concept node: `CONCEPT_[ID]_[TERM_SLUG].md`
- Entity node: `ENTITY_[ID]_[NAME_SLUG].md`
- Master strategy: `Analysis_[ID]_MASTER_STRATEGY.md`
- Chunk analysis: `Analysis_[ID]_CHUNK_XX.md`
- Source map: `MAP_[ID].md`
- Naming lock: `NAMING_LOCK_[ID].md`

## Three-Layer Ingest

### Layer 1: Structure-First

Create structure artifacts before chunk-level analysis:
- source metadata
- table of contents
- part boundaries
- chapter boundaries
- section boundaries
- page ranges

Primary structure hierarchy:

- `Part -> Chapter -> Section -> page_range`

This layer exists to preserve the whole-book view.

Required artifact:
- `STRUCTURE_[ID].md`

### Layer 2: Visual Mapping

For PDFs with meaningful diagrams, tables, or charts, extract visual evidence as a separate artifact.

Track:
- figure/table identifier
- page
- section
- chapter
- caption or label when available
- why it matters

Preferred context order:

- `chapter -> section -> page`

Visual evidence is not optional when the source depends on diagrams for core understanding.

Required artifact when visuals matter:
- `FIGURES_[ID].md`

### Layer 3: Chunked Evidence Extraction

Chunks are technical extraction units only.

Chunking priority:
1. chapter boundary first
2. section heading boundary second
3. page window only when a section is still too large

Each chunk must declare:
- `source_id`
- `chapter_id`
- `section_path`
- `page_range`
- `canonical_terms`

## Naming Lock Rule

Before atom generation, create `NAMING_LOCK_[ID].md`.

It must contain:
- canonical source filename
- canonical source node filename
- approved chunk filenames
- approved canonical term -> concept filename mapping
- approved canonical entity -> entity filename mapping

After naming lock is approved:
- agents must not invent new filename patterns
- display title may evolve
- canonical filename must not drift

## Operational Effect

This design keeps chunking for GPU/throughput reasons while preventing chunk-local naming hallucination and text-only loss of visual knowledge.

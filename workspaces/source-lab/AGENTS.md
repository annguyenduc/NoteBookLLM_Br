# AGENTS.md - source-lab

This workspace is inside NoteBookLLM_Br, but it is NON-CANONICAL.

Purpose:

- xử lý thử nguồn dài.
- convert/OCR/preview ở mức nháp.
- hỏi NotebookLM để lập cấu trúc tài liệu.
- chuẩn bị đề xuất có nên ingest chính thức không.

Allowed:

- read/write inside `workspaces/source-lab/`.
- create temporary preview files.
- create handoff recommendation in chat or local draft.

Forbidden:

- write directly to `../../3-resources/`.
- write directly to `../../3-resources/raw_sources/`.
- write directly to `../../3-resources/raw_ingest/`.
- write directly to `../../3-resources/raw_assets/`.
- write directly to `../../3-resources/wiki/`.
- create official lifecycle artifacts unless AN explicitly starts official ingest.
- create canonical Atom files.
- set `VERIFIED`.
- set `SYNTHESIZED`.

Handoff:

- Default output is `SKIP | KEEP_SUMMARY | PROMOTE`.
- If `PROMOTE`, route to `../../.agent/workflows/ingest-lifecycle.md`.


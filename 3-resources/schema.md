# 🗂️ Quy định cấu trúc Wiki (Schema)

## 1. Cấu trúc thư mục

```
3-resources/
├── purpose.md              # Goals, key questions, research scope
├── schema.md               # Wiki structure rules, page types (THIS FILE)
├── raw_sources/            # EVIDENCE: Uploaded raw documents (PDF, Office, HTML)
├── raw_ingest/             # FUEL: Sanitized Markdown ready for Wiki (R21 forced)
├── raw_assets/             # VISUAL PROOF: Extracted images, charts, and diagrams
├── _deprecated/            # ARCHIVE: Files replaced by higher fidelity versions
└── wiki/
    ├── index.md            # SOURCE OF TRUTH: Catalog of all Atoms
    ├── log.md              # INDEX: Link to daily logs
    ├── logs/               # ARCHIVE: log_YYYY_MM_DD.md (R14)
    ├── overview.md         # DASHBOARD: Global summary (auto-updated)
    ├── entities/           # People, organizations, products (ENTITY_*)
    ├── concepts/           # Theories, methods, techniques (CONCEPT_*)
    ├── sources/            # Source nodes (SOURCE_*)
    ├── queries/            # Complex query results & research notes
    ├── synthesis/          # High-level knowledge synthesis (SYNTHESIS_*)
    ├── comparisons/        # Side-by-side analysis (COMPARE_*)
    ├── decisions/          # Governance decisions (DECISION_*)
    ├── review_queue/       # PENDING: Draft atoms waiting for R8 Human Gate
    ├── session_insights/   # AUDIT: Insights and patterns from sessions
    └── wiki_brain.db       # DATABASE: SQLite Graph & Vector Index
```

## 2. Quy ước Tên trang (Page Types)
- **Concepts**: `CONCEPT_[PREFIX]_[TênKháiNiệm].md` (ví dụ: `CONCEPT_THINK_Logic_Tree.md`, `CONCEPT_ARCH_System_Resilience.md`).
- **Entities**: `ENTITY_[TênThựcThể].md` (ví dụ: `ENTITY_Python.md`).
- **Sources**: `SOURCE_[PREFIX]_[TênTàiLiệu].md` (ví dụ: `SOURCE_ARCH_Thinking_in_Systems.md`).
- **Prefixes cốt lõi**:
    - `THINK`: Problem Solving & Critical Thinking.
    - `ARCH`: Systems Thinking & Agentic Infrastructure (Mới).
    - `AIMET`: Agentic AI, LLM & Orchestration.
    - `DE/DSML/STAT`: Kỹ thuật & Khoa học dữ liệu.

- **Synthesis**: Các file dạng `CASE_STUDY_*.md`, `SYNTHESIS_*.md`.

## 3. Quy định liên kết (Links)
- Chỉ sử dụng `[[wikilinks]]` để liên kết nội bộ trong `wiki/`.
- Không liên kết trực tiếp tới `raw_sources/` trừ khi trong trường `📖 Nguồn` của `[AUDITOR]`.
- Tất cả các trang bắt buộc có Frontmatter chuẩn theo **Master Schema V3.0**.

## 4. Governance Gate (Hard Stops)
- **R16 (Checkpoint)**: Phải khai báo trạng thái trước khi thực hiện task phức tạp.
- **R21 (Audit Gate)**: Mọi file trong `raw_ingest/` phải pass `audit_raw_ingest.py`.
- **R8 (Human Gate)**: Chỉ User mới được chuyển trạng thái sang `SYNTHESIZED`.
- **R15 (Sync)**: Sử dụng `@obsidian-cli` để reload sau khi thay đổi Metadata.

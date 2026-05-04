# 🗂️ Quy định cấu trúc Wiki (Schema)

## 1. Cấu trúc thư mục

```
3-resources/
├── purpose.md              # Goals, key questions, research scope
├── schema.md               # Wiki structure rules, page types
├── raw/
│   ├── sources/            # Uploaded documents (immutable)
│   └── assets/             # Local images
└── wiki/
    ├── index.md            # Content catalog (Tự động tạo)
    ├── log.md              # Operation history (Nhật ký cập nhật)
    ├── overview.md         # Global summary (auto-updated)
    ├── entities/           # People, organizations, products (ENTITY_*)
    ├── concepts/           # Theories, methods, techniques (THINK_*, ACAD_*, ...)
    ├── sources/            # Source summaries (SOURCE_*)
    ├── queries/            # Saved chat answers + research
    ├── synthesis/          # Cross-source analysis (Bài kiểm tra, báo cáo tổng hợp)
    └── comparisons/        # Side-by-side comparisons (COMPARE_*)
    ├── decisions/          # 💡 THÊM — Conflict/Ambiguous resolved decisions
    ├── review_queue/       # 💡 THÊM — Pending atoms waiting for human gate
    └── session_insights/   # 💡 THÊM — Logged insights from each session
    └── wiki_brain.db       # 💡 SQLite Graph DB (FTS5 + Graph)
```

## 2. Quy ước Tên trang (Page Types)
- **Concepts**: `[LĩnhVực]_[TênKháiNiệm].md` (ví dụ: `THINK_Data_Story_Structure.md`).
- **Entities**: `ENTITY_[TênThựcThể].md` (ví dụ: `ENTITY_Python.md`).
- **Comparisons**: `COMPARE_[A]_vs_[B].md`.
- **Sources**: `SOURCE_[TênSách_TàiLiệu].md`.
- **Synthesis**: Các file dạng `CASE_STUDY_*.md`, `SYNTHESIS_*.md`.

## 3. Quy định liên kết (Links)
- Chỉ sử dụng `[[wikilinks]]` để liên kết nội bộ trong `wiki/`.
- Không liên kết trực tiếp tới `raw/` trừ khi trong trường `📖 Nguồn` của `[AUDITOR]`.
- Tất cả các trang bắt buộc có Frontmatter chuẩn với tags và aliases.

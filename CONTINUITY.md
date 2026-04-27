# Project Continuity - NoteBookLLM_Br (Swarm Supreme v8.0 — Post-PARA)

## 🏛️ Status: PARA Migration COMPLETE (2026-04-27)
- **Current Goal**: Hệ thống đã hoàn tất PARA Migration. Ổn định và sẵn sàng cho các dự án mới.
- **Architecture**: PARA hoàn chỉnh — `1-projects/` (active), `2-areas/` (ongoing), `3-resources/` (knowledge), `4-archive/` (done).

## ✅ Accomplishments (Session 27/04 — PARA Migration Sprint)
- [x] **brain/ → 3-resources/**: Migrate 122 files thành công, không mất data.
- [x] **AGENTS.md Full Overhaul**: Rule 7 (3-cấp flatness), bảng phân quyền PARA, loại bỏ `process/`.
- [x] **process/ Deprecated**: Files useful chuyển sang `3-resources/` (WIKI_AGENT_GUIDE, PROCESS_TEMPLATE). Folder đã xóa.
- [x] **Graph Stabilization**: 2010 Atom links trung hòa → ~50 nodes còn lại trong Obsidian Graph View.
- [x] **Script Fix**: Toàn bộ `BRAIN_DIR` trong Python scripts đã đổi sang `3-resources/`.
- [x] **WIKI_INDEX rebuild**: 46 Concepts + 2 Distilled + 2010 Atoms (text-only, không tạo node).
- [x] **README & task_plan**: Cập nhật sơ đồ cây và roadmap sang PARA.
- [x] **LMS Test Bank Full Extraction**: Trích xuất 100% (1,538 câu) từ 84 đề Docx (Robot, IOT, KHMT, DESIGN).
- [x] **Asset Deduplication Pro**: Xóa ~13,400 ảnh trùng lặp, tối ưu hóa assets chỉ còn 4,120 ảnh độc nhất.

- [x] **Giai đoạn 3 — LMS Pivot**: Hoàn tất trích xuất Test Bank (LMS_Pivot).
- [ ] **Giai đoạn 4 — Merge Workspace**: Quét và ánh xạ `Gemini_Study_Hub`.
- [ ] **CONTINUITY update**: Cập nhật CLAUDE.md sang session mới.

## ⚠️ Incidents & Lessons Learned

### [2026-04-27] PARA Migration — process/ Deprecation
- **Vấn đề:** `process/` gây confuse sau PARA vì không rõ scope (dự án nào? lĩnh vực nào?).
- **Giải pháp:** Xóa `process/`, route lại handoff files theo đúng nhà trong PARA:
  - Ephemeral task files → `1-projects/[Project]/`
  - Long-term profiles/eval → `2-areas/Profiles/` và `2-areas/Assessment/`
- **Bài học:** PARA buộc agent phải **luôn đặt câu hỏi** "file này thuộc dự án nào / lĩnh vực nào?" thay vì ném vào vùng đệm chung.

### [2026-04-27] Obsidian Graph — 2000 nodes problem
- **Vấn đề:** WIKI_INDEX.md chứa 2010 Wikilinks → Graph View bùng nổ.
- **Giải pháp:** Đổi Atom entries sang backtick text (`` `path/file.md` ``) thay vì `[[wikilinks]]`.
- **Bài học:** WIKI_INDEX nên là **catalog cho người đọc và LLM**, không phải link graph cho Obsidian.

### [2026-04-27] Python scripts hardcode brain/
- **Vấn đề:** Sau rename, `update_wiki_index.py` và 15 scripts khác vẫn trỏ `BRAIN_DIR = 'brain'`.
- **Giải pháp:** Script `fix_py_vars.py` chạy một lần, batch-replace toàn bộ.
- **Bài học:** Khi đổi tên thư mục cốt lõi, PHẢI audit toàn bộ Python scripts ngay trong cùng session.

### [2026-04-27] Vi phạm append-only với 3-resources/log.md
- **Vấn đề:** Agent đã dùng thao tác tạo file khi ghi log kế hoạch MimiClaw Inbox, làm ghi đè `3-resources/log.md` thay vì append ở cuối file.
- **Giải pháp:** Phục hồi lịch sử log từ snapshot git `e0fa2c7:brain/log.md`, hợp nhất với các entry hiện tại ngày 2026-04-27 và giữ lại entry `CORRECTION` để trace sự cố.
- **Bài học:** Từ đây về sau, mọi lần ghi `3-resources/log.md` phải dùng append an toàn; không được dùng create/replace toàn file trừ khi đang làm phục hồi sự cố có kiểm soát.

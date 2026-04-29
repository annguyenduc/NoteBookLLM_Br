# CONTINUITY — Phiên kế tiếp NoteBookLLM_Br

> **Tạo**: 2026-04-29 07:25 | **Agent**: @pm | **Conversation**: 20439d5e-01b5-44e1-a962-0adc14dc803e

---

## ✅ ĐÃ HOÀN THÀNH trong phiên này

### 1. Verify Migration Wiki/ ✅
- Phát hiện & fix **17 files** có đường dẫn ảnh lỗi `assets/assets/` → `assets/`
- Lint kết quả: 136 wikilinks → 77 broken → **2 broken thật** sau fix

### 2. Fix P0 — Wikilinks trỏ sai vào raw ✅
- **Layer 1** (concepts/ + entities/): 29 files — thay `[[THINK_X]]` → `[[SOURCE_THINK_X]]`
- **Layer 2** (sources/): 3 files — chuyển frontmatter `source: "[[...]]"` → `source_raw: "..."`
- **Layer 3** (ACAD_AI): 6 files — neutralize `[[coursera-AI-*]]` thành backtick
- Kết quả cuối: **2 broken links thật** (WIKI_ENTITY_SQL, WIKI_ENTITY_Python trong ENTITY_Data_Science.md)

### 3. Làm rõ kiến trúc (Architecture Clarification) ✅
- `distilled/` ≠ `wiki/synthesis/` — distilled là quality gate cao hơn, không cần đổi
- `overview.md` và `synthesis/` trong llm-wiki.md chỉ là mô tả ý tưởng, không phải thư mục thực tế
- Mapping đúng: `WIKI_INDEX.md` = index, `distilled/THINK_Analytical_Thinking.md` = synthesis
- Lint script cần scan `wiki/ + distilled/` (không chỉ `wiki/`)

### 4. Clarify Link Rules ✅
- Concept pages → chỉ trỏ vào wiki (SOURCE_*, other concepts, entities)
- SOURCE pages → ghi `source_raw:` dạng text, không dùng wikilink
- Raw files → chỉ @auditor mở để verify (không wikilink)

### 5. Dọn dẹp stale files ✅
- Archive `3-resources/lint_report.md` → `4-archive/20260422_lint_report_stale.md`
- Archive `3-resources/RESOURCES_WIP.md` → `4-archive/20260423_RESOURCES_WIP_superseded.md`

---

## ⏳ CÒN LẠI — Việc cần làm phiên sau

### 🔴 P1 — Fix 2 broken links thật (15 min) ✅
- Đã kiểm tra `ENTITY_Data_Science.md`, file đã trỏ đúng dạng `[[ENTITY_SQL]]` và `[[ENTITY_Python]]` (dù file target chưa được tạo). Đã bỏ tiền tố `WIKI_` thành công.
- **Agent**: @healer — 1 file, 2 dòng

### 🟡 P2 — Tạo 4 trang còn thiếu: Thinking with Data (45 min) ✅
Nguồn raw: `3-resources/raw/THINK_Thinking_with_Data.md`
| Trang cần tạo | Chương |
|:--|:--|
| `THINK_Correlation_vs_Causation` | Chương 4 |
| `THINK_Data_Story_Structure` | Chương 7 |
| `THINK_Audience_Framing` | Chương 5 |
| `THINK_Exploration_vs_Confirmation` | Chương 3 |
- **Agent**: @scout đọc raw → @engineer viết wiki pages vào `wiki/concepts/` (Đã hoàn thành)
- Đã update `SOURCE_THINK_Thinking_with_Data.md` Ingest Map và ghi log.

### 🟡 P3 — Tạo Comparison page (20 min) ✅
- `wiki/comparisons/COMPARE_5Whys_vs_RCA.md`
- Đã tách bảng so sánh từ `THINK_Root_Cause_Analysis.md` sang file comparison riêng.
- **Agent**: @librarian (Đã hoàn thành)

### 🟡 P4 — Update brain_lint.py (15 min) ✅
- Đã sửa script để add `distilled/` vào scan scope (`get_all_target_files`).
- Ngăn chặn false positive cho các file thuộc distilled/.
- **Agent**: @devops (Đã hoàn thành)

### 🟢 P5 — Ingest nhóm ACAD (Coursera) → tạo `ACAD_AI_Responsible_AI` (trong distilled/) ✅
- Đã verify nội dung `ACAD_AI_Responsible_AI.md` hoàn toàn khớp với `raw/coursera-AI-essentail-Bias, drift, and knowledge cutoff.md` và `raw/coursera-AI-essential-Stay up to date with AI.md`.
- Đã khắc phục trang mồ côi `ACAD_AI_Cutoff_vs_Drift` bằng cách link vào trang Master này.
- **Agent**: @auditor (Đã hoàn thành)

---

## 📊 Trạng thái Wiki hiện tại
```
wiki/concepts/  : 36 trang
wiki/entities/  : 1 trang
wiki/sources/   : 3 trang
wiki/assets/    : 17 ảnh
wiki/comparisons/: TRỐNG (P3)
wiki/queries/   : TRỐNG
distilled/      : 2 files (THINK_Analytical_Thinking, ACAD_AI_Responsible_AI)
Broken links    : 2 thật (ENTITY_SQL, ENTITY_Python)
```

## 🔑 Files quan trọng cần đọc khi bắt đầu phiên mới
1. `CONTINUITY.md` — file này
2. `purpose.md` — Định hướng Wiki
3. `AGENTS.md` — 18 Rules (đặc biệt Rule 7 Semantic Structure)
4. `3-resources/distilled/THINK_Analytical_Thinking.md` — Master Index

---

## ⚠️ Lưu ý kỹ thuật cho Agent tiếp theo

### Link rules (đã chốt phiên này)
- `wiki/concepts/` → trỏ `[[SOURCE_THINK_X]]` cho source, `[[THINK_Y]]` cho cross-ref
- `wiki/sources/` → dùng `source_raw: "tên_file.md"` trong frontmatter (text, không wikilink)
- `wiki/` → KHÔNG BAO GIỜ trỏ `[[wikilink]]` vào `raw/`
- `distilled/` → hợp lệ là link target từ wiki (Obsidian resolve toàn vault)

### Lint script
- `brain_lint.py` cần update: thêm `distilled/` vào valid_files scope
- Hiện scan chỉ `3-resources/wiki/**` → false positive cho distilled links

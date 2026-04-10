# 🔍 Deep Search (LITE)

> **Goal:** Cung cấp khả năng tìm kiếm ngữ nghĩa (Semantic Search) mạnh mẽ khi dự án vượt quá cửa sổ ngữ cảnh của AI. Kết hợp BM25 + Vector + LLM re-ranking thông qua công cụ `qmd`.

## 🚀 Detection Thresholds (Ngưỡng kích hoạt)
Tự động đề xuất khi quét codebase thấy:
- 📂 Thư mục `docs/` chứa **> 50** file markdown.
- 💻 Toàn bộ project có **> 200** file nguồn (Source files).
- 🗣️ User yêu cầu: "Tìm lại file cũ nói về X", "Lục lại các quyết định quá khứ".

## 🛠️ QMD Setup & Workflow
1. **Install:** `npm install -g @tobilu/qmd`.
2. **Index:** 
   - `qmd collection add ./docs --name project-docs`
   - `qmd context add qmd://project-docs "Mô tả mục đích bộ docs"`
3. **Embed:** `qmd embed` (Chạy local, tạo vector embeddings).
4. **Query:** `qmd query "câu hỏi của bạn"` → Trả về context chính xác nhất.

## 📐 Memory Hierarchy (Hệ thống bộ nhớ)
- **Continuity:** Bộ nhớ làm việc (Working Memory - ~500 từ).
- **Learnings/Decisions:** Bộ nhớ dài hạn (Long-term Memory).
- **Deep Search (qmd):** Bộ nhớ ngữ nghĩa bên ngoài (External Semantic - Searchable).
- **CodeGraph:** Bộ nhớ cấu trúc mã nguồn (Structural Code).

## 🚨 Quality Gate (Red Flags)
- ❌ Đề xuất `qmd` cho các project quá nhỏ (Gây lãng phí tài nguyên).
- ❌ Để index bị cũ (Stale) → AI sẽ đọc tài liệu lỗi thời và sinh code sai.
- ❌ Quên chạy `qmd embed` sau khi `cm-dockit` tạo ra một lượng lớn tài liệu mới.
- ❌ Coi Deep Search là thay thế cho `cm-continuity` (Chúng hỗ trợ nhau, không thay thế).

## 💡 Example Triggers
- "Project này lớn quá, có cách nào tìm kiếm tài liệu nhanh không?"
- "Tìm các quyết định về tích hợp thanh toán trong các PRD cũ."
- "Deep Search: truy vấn quy trình triển khai hệ thống."

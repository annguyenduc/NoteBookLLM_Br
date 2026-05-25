# Outside Superpowers Scope

Dưới đây là các cơ chế đặc thù và nâng cao của vault `NoteBookLLM_Br` nằm ngoài phạm vi và thẩm quyền chấm điểm của **Superpowers Direct Grader**. Các cơ chế này không được coi là lỗi hay lỗ hổng, mà là thiết kế chuyên biệt phục vụ mục tiêu tối thượng của Second Brain.

## 1. Chu kỳ nạp tri thức chính thức (Canonical Ingest Lifecycle)
- **Cơ chế:** Vòng đời 6 bước với các chốt chặn artifact gate cực kỳ chặt chẽ:
  ```text
  prepare-source -> audit-promote-source -> lock-ingest-input -> ingest -> ingest-generate -> ingest-index-log
  ```
- **Lý do ngoài phạm vi:** Superpowers core chỉ tập trung vào các kỹ năng lập trình tổng quát và quản trị Git. Nó không có khái niệm về việc đóng băng tri thức (Atom) hay các tầng review queue chuyên biệt dành cho Obsidian.

## 2. Đối chiếu tri thức NotebookLM (NotebookLM Knowledge Reconciliation)
- **Cơ chế:** Lưu trữ các đối chiếu ngữ nghĩa phức tạp và đẩy dữ liệu lên Google NotebookLM để tạo flashcards, podcast liên phiên.
- **Lý do ngoài phạm vi:** Superpowers không hỗ trợ các MCP hay tích hợp sâu với NotebookLM API ở mức độ quản lý tri thức cá nhân.

## 3. Quản trị học tập Sư phạm (Pedagogy & Spaced Repetition)
- **Cơ chế:** Chuyển hóa Atom thành giáo án (Lesson Plan), slide thuyết trình (VitePress/Reader) và kiểm định Spaced Repetition định kỳ.
- **Lý do ngoài phạm vi:** Superpowers là bộ công cụ hỗ trợ nhà phát triển (developer-focused), không có định hướng về mặt sư phạm (pedagogy-focused) hay thiết kế lộ trình học tập cho con người.

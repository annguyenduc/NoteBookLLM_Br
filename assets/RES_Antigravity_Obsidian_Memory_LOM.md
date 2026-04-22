# 🧠 Antigravity Long-term Operational Memory (LOM) v3.0

> **Architecture Purpose**: Kiến tạo một hệ thống tri thức bền vững theo mô hình "LLM OS", nơi AI Agent và Con người cộng tác trên một substrate dữ liệu Markdown sống động.

## 1. Phân tầng Bộ nhớ (Memory Hierarchy)
Tuân thủ triết lý **"Accumulation over Retrieval" (Karpathy)**:

| Layer | Tên gọi | Lưu trữ | Mục đích |
| :--- | :--- | :--- | :--- |
| **L1** | **Working Memory** | `CONTINUITY.md` | RAM: Trạng thái tức thời, checklist hiện hành. |
| **L2** | **Episodic Memory** | `brain/raw/` | I/O Logs: Dấu vết thực thi thô từ bầy đàn Agent. |
| **L3** | **Semantic Local** | `brain/distilled/` | **LLM Wiki (Kernel)**: Tri thức chưng cất, liên kết bằng `[[Wikilinks]]`. |
| **L4** | **Semantic Cloud** | **NotebookLM** | Deep Research: Thư viện tài liệu khổng lồ và podcast tri thức. |

## 2. Hiến pháp Vận hành (The Constitution)
Dự án sử dụng **[[CLAUDE.md]]** làm văn bản pháp lý cao nhất cho Agent. Agent phải đọc tệp này trước khi thực hiện bất kỳ thao tác nào trên Vault để đảm bảo tính nhất quán.

## 3. Quy trình Tổng hợp (Continuous Synthesis)
Thay vì chưng cất thụ động, `@researcher` thực hiện vòng lặp "Heartbeat":
1.  **Ingestion**: Thu nhận Log thô từ `brain/raw/`.
2.  **Synthesis**: Cập nhật thông tin mới vào các bài viết Wiki tương ứng thay vì tạo file mới (Wiki Merge).
3.  **Graph Weaving**: Tự động tạo các liên kết ngang giữa những khối tri thức liên quan.
4.  **Reconciliation**: Phát hiện và xử lý mâu thuẫn tri thức (Tag `#deprecated` cho thông tin cũ).

## 4. Tiêu chuẩn Formatting (B2B Standard)
- **Templates**: Luôn khởi tạo từ `templates/Wiki_Article_Template.md`.
- **Typography**: Font Montserrat (Tiêu đề) / Arial (Nội dung) cho các bản xuất bản PPTX/PDF.
- **Identity**: Sử dụng ký hiệu `@` gắn với Registry trong `AGENTS.md`.

---
**FrameWork**: Antigravity v3.0 | **Triết lý**: Karpathy & Spisak | **Duy trì bởi**: @pm & @researcher

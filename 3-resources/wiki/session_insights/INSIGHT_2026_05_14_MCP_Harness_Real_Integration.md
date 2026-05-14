# Session Insight: MCP Harness Real Integration & Tool-Skill Duality

**Date:** 2026-05-14
**Phase:** System Hardening (Phase 5/6)
**Tags:** #architecture, #mcp, #governance, #r8, #r25

## 1. Bối cảnh (Context)
Tiếp nối việc xây dựng cấu trúc Micro-MCP Servers (`Wiki-Ops-MCP` và `Local-AI-MCP`), phiên làm việc này tập trung vào việc **nối mạng thực tế (Real Integration)**, thay thế các dữ liệu mô phỏng (Mock data) bằng logic thao tác thật với hệ thống 파일 và Ollama API.

## 2. Các Thay Đổi Kỹ Thuật (Technical Implementations)
- **Wiki-Ops-MCP (`wiki_ops.py`):**
  - Đã tích hợp `pathlib` để đọc trực tiếp thư mục `3-resources/wiki/`.
  - Nâng cấp `query_wiki`: Quét và lọc tên file Markdown thực tế trong `concepts/` và `entities/`.
  - Nâng cấp `wiki_status`: Đếm chính xác số lượng Atom trong các thư mục cốt lõi.
- **Local-AI-MCP (`local_ai.py`):**
  - Tích hợp thư viện `httpx` để gọi API trực tiếp tới cổng `11434` của Ollama nội bộ.
  - **Thực thi R25 (Non-blocking):** Bọc block `try-except` cho các request AI. Nếu Ollama tắt hoặc lỗi, tool không làm treo Agent mà trả về chuỗi `WARNING`, cho phép Agent tiếp tục chạy (Graceful degradation).

## 3. Quyết định Kiến trúc: Sự Nhị Nguyên giữa Tool và Skill (Tool-Skill Duality)
Một thảo luận quan trọng đã diễn ra về việc có nên đưa toàn bộ bộ lệnh (7-10 lệnh) của Wiki 2.0 (như `absorb`, `cleanup`, `rebuild`) vào MCP hay không. Quyết định cuối cùng là **KHÔNG**.
- **MCP Tools:** Phải tuân thủ "Nguyên tắc Đặc quyền Tối thiểu". Chỉ đóng gói các tác vụ **Read-only** hoặc **Safe-trigger** (như tìm kiếm, đọc file, gọi API AI) để LLM có thể gọi tự động mà không lo phá hỏng dữ liệu.
- **Agent Skills (`.agent/skills/`):** Chứa các SOPs (Standard Operating Procedures) cho các tác vụ đột biến dữ liệu (State Mutation) như gộp, xóa, di chuyển hàng loạt. Các tác vụ này BẮT BUỘC LLM phải thực thi bằng code/Terminal dưới sự giám sát của User để tuân thủ **R8 (Human Supremacy)** và **R22 (Staging-Promote)**.
- **Lợi ích:** Tránh cho Agent bị "quá tải ngữ cảnh" (Agentic Confusion) và loại trừ nguy cơ phá hoại không chủ đích.

## 4. Bước Tiếp Theo (Next Actions)
- Đóng phiên cấu hình hạ tầng MCP.
- Bắt đầu phiên làm việc mới tập trung vào quá trình **Tổng hợp (Synthesis)** các Knowledge Atoms.

---
file_id: CONCEPT_META_SB3_TASK_LEDGER
title: "Task Ledger (Nhật ký tác vụ bền vững)"
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
created: "2026-05-03"
last_updated: "2026-05-03"
sources:
  - "[[SOURCE_META_KARPATHY_LLM_WIKI]]"
---

## ## For future Claude
Trang này định nghĩa khái niệm **Task Ledger** - một cơ chế ghi chép tác vụ bền vững giúp AI Agent duy trì ngữ cảnh xuyên suốt các phiên làm việc (session). Thay vì phụ thuộc vào bộ nhớ ngắn hạn của chat history, Task Ledger lưu trữ trạng thái, mục tiêu và các bước thực hiện vào một file log có cấu trúc để "Second Brain" có thể phục hồi ngay lập tức.

## ## Key Claims / Summary
1.  **Durable Session Memory**: Lưu trữ tiến trình công việc để không bao giờ phải bắt đầu lại từ đầu.
2.  **Auditability**: Cho phép con người và Agent khác kiểm tra lộ trình thực hiện của một tác vụ phức tạp.
3.  **Conflict Resolution**: Phát hiện sớm các bước đi sai lệch hoặc mâu thuẫn trong kế hoạch thực thi.

## 1. Bản chất kỹ thuật
Task Ledger vận hành như một "quyển sổ cái" (Ledger) ghi lại mọi thay đổi trạng thái của hệ thống. Trong mô hình LLM Wiki, tệp `log.md` đóng vai trò là một Task Ledger sơ khởi, ghi lại các hành động `ingest`, `query`, và `lint`.

## 2. Các thành phần của một Ledger Entry
- **Timestamp**: Thời điểm thực thi.
- **Action Type**: Loại hành động (Create, Modify, Delete, Research).
- **Context Pointer**: Liên kết tới các node raw hoặc wiki liên quan.
- **Outcome/Status**: Kết quả (Success, Fail, Partial) và lý do.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### Ví dụ từ Swarm (Original)
> **Bối cảnh**: Hệ thống đa Agent (SwarmVault) thực hiện nạp 100 tài liệu.
> **Ứng dụng**: Một Agent gặp lỗi ở tài liệu thứ 45. Thay vì dừng toàn bộ, Task Ledger ghi nhận lỗi và Agent tiếp theo có thể đọc ledger để tiếp tục từ tài liệu 46 hoặc thử lại tài liệu 45 với thông số khác.
> **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Section: Community Comments.

### Ẩn dụ sư phạm (Pedagogical Application)
> **Bối cảnh**: Quá trình lắp ráp một bộ mô hình LEGO khổng lồ (như Millennium Falcon).
> **Ứng dụng**: Task Ledger giống như cuốn sách hướng dẫn có đánh dấu tích (checklist). Nếu bạn phải dừng lại để đi ngủ, sáng hôm sau bạn chỉ cần nhìn vào dấu tích cuối cùng để biết mình đang ở bước nào và cần lấy mảnh ghép nào tiếp theo, thay vì phải lục lại cả đống mảnh ghép từ đầu.

## ## Source Tracing
- **Nguồn**: [[SOURCE_META_KARPATHY_LLM_WIKI]] — Section: Task Memory & Ledger Patterns.

## ## History / Revisions
- **2026-05-03**: [@engineer] Khởi tạo concept SB3 Task Ledger.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

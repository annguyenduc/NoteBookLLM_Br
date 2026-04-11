# Implementation Plan: Token Budget Expansion for Swarm

Tài liệu này mô phỏng kế hoạch nâng cấp khả năng xử lý văn bản dài của hệ thống Swarm, đảm bảo các bài giảng và đề thi không bị cắt cụt giữa chừng.

## User Review Required

> [!IMPORTANT]
> - **Tiêu chuẩn mới**: Nâng `max_tokens` mặc định cho vai trò `@engineer` và `@designer` từ 1800 lên **4000 tokens**.
> - **Tùy biến linh hoạt**: Bổ sung cờ `--max_tokens` vào `swarm_orchestrator.py` để người dùng có thể tự đẩy lên cao hơn khi cần (ví dụ: soạn đề thi 50 câu).
> - **Chi phí**: Việc tăng token trả về có thể làm tăng nhẹ độ trễ (latency) nhưng đảm bảo tính toàn vẹn của dữ liệu.

## Proposed Changes

### [libs/core](file:///d:/NoteBookLLM_Br/libs/core)

#### [MODIFY] [llm_client.py](file:///d:/NoteBookLLM_Br/libs/core/llm_client.py)
- Cập nhật các hàm `call_designer`, `call_pedagogical_engineer`, và `call_creative`.
- Thay đổi `max_tokens` mặc định từ 1800 -> **4000**.
- Đảm bảo tham số `max_tokens` được truyền xuyên suốt xuống `_call_with_fallback`.

### [scripts](file:///d:/NoteBookLLM_Br/scripts)

#### [MODIFY] [swarm_orchestrator.py](file:///d:/NoteBookLLM_Br/scripts/swarm_orchestrator.py)
- Bổ sung tham số CLI:
    - `--max_tokens`: Cho phép ghi đè giới hạn token.
    - `--temp`: Cho phép điều chỉnh độ sáng tạo (temperature).
- Truyền các tham số này vào các hàm gọi Agent tương ứng.

## Verification Plan

### Automated Tests
- Chạy thử lệnh soạn thảo nội dung dài với cờ `--max_tokens 4000` cho Module 2 để kiểm tra xem nội dung còn bị cắt ở dòng 152 như trước không.
- Kiểm tra log 9Router để xác nhận tham số `max_tokens` đã được gửi đúng.

### Manual Verification
- Kiểm tra tệp tin đầu ra (`.md`) để xác nhận phần **Đáp án/Rubric** ở cuối đã xuất hiện đầy đủ chưa.

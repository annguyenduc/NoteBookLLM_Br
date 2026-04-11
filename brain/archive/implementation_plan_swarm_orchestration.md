# Implementation Plan: Swarm Orchestration for Pedagogical Content

Kế hoạch này giải quyết vấn đề "Bỏ qua Swarm" mà người dùng đã nêu. Chúng ta sẽ chuyển từ việc Antigravity tự viết nội dung sang việc **Điều phối** (Orchestrate) các Agent chuyên biệt trong Swarm thực hiện.

## User Review Required

> [!IMPORTANT]
> - **Chế độ Ủy thác (Delegation)**: Antigravity sẽ đóng vai trò Giao dịch viên (@pm), soạn thảo Prompt và gửi cho các Agent chuyên biệt thông qua một script thực thi 9Router.
> - **Minh bạch hệ thống**: Người dùng sẽ thấy log và traffic thực tế trên 9Router Dashboard khi các Agent (Llama, Qwen) phản hồi.
> - **Tuân thủ Rule 11**: Thực hiện đúng trình tự @profiler -> @designer -> @engineer.

## Proposed Changes

### [scripts](file:///d:/NoteBookLLM_Br/scripts)

#### [NEW] [swarm_orchestrator.py](file:///d:/NoteBookLLM_Br/scripts/swarm_orchestrator.py)
- Một công cụ CLI cho phép gọi bất kỳ Agent nào trong Swarm (Profiler, Designer, Engineer, Auditor) với ngữ cảnh cụ thể.
- Tự động ghi log vào `storage/logs/swarm_activity.log`.
- Trả về kết quả đầu ra sạch để Antigravity ghi vào các file tri thức.

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [MODIFY] [G10_Mod1_Generative_AI_Foundation.md](file:///d:/NoteBookLLM_Br/brain/distilled/G10_Mod1_Generative_AI_Foundation.md)
- Nội dung này sẽ được **biên soạn lại** bởi @engineer (Qwen 32B) sau khi @designer đã duyệt cấu trúc 5E.

## Open Questions

> [!CAUTION]
> 1. **Ngữ cảnh bổ sung**: Bạn có muốn tôi nạp toàn bộ `Prompt_Engineering_Master.md` vào làm ngữ cảnh "bắt buộc" cho @engineer không?
> 2. **Kiểm soát chi phí**: Các lần gọi Swarm này sẽ sử dụng Free Tier Supreme (Llama 3.3 70B, Qwen 32B). Quá trình này sẽ sinh ra khoảng 3-4 request 9Router cho mỗi module.

## Verification Plan

### Automated Tests
- Chạy `python scripts/swarm_orchestrator.py --role profiler --prompt "Test"` để xác nhận 9Router nhận request.
- Kiểm tra log 9Router để thấy traffic từ các model tương ứng.

### Manual Verification
- Người dùng kiểm định văn phong của @engineer (thường sẽ khác biệt so với Antigravity).

# Implementation Plan: Role-Based Fallback & Registry Refinement

Kế hoạch này thực hiện việc chuẩn hóa `MODEL_FALLBACK_CHAINS` theo sơ đồ vai trò (Role-based) do người dùng đề xuất và khắc phục các lỗi định danh model trong Index.

## User Review Required

> [!IMPORTANT]
> - **Cấu trúc Fallback mới**: Thay đổi lộ trình dự phòng để ưu tiên các model cùng nhóm năng lực (Tier) trước khi quay về Gemini Flash.
> - **Xác nhận Model Engineer**: Sử dụng `qw/qwen3-coder-plus` làm model chủ lực cho `@engineer`.

## Proposed Changes

### [brain/distilled](file:///d:/NoteBookLLM_Br/brain/distilled)

#### [MODIFY] [agents-index.md](file:///d:/NoteBookLLM_Br/brain/distilled/agents-index.md)
- Sửa lỗi định danh `@engineer`: `qw/coder-model` -> `qw/qwen3-coder-plus`.
- Cập nhật backup cho `@designer`: ưu tiên `groq/llama-3.3-70b-versatile` thay vì coder model.

### [libs/core](file:///d:/NoteBookLLM_Br/libs/core)

#### [MODIFY] [llm_client.py](file:///d:/NoteBookLLM_Br/libs/core/llm_client.py)

- **[DONE] Cập nhật `PEDAGOGICAL_MODEL_PRESETS["free"]`**:
    - `engineer`: `qw/qwen3-coder-plus` (Đã được ping xác nhận ONLINE 200).
- **[DONE] Cập nhật `MODEL_FALLBACK_CHAINS`**:
    - Áp dụng sơ đồ 3 tầng: **Primary** -> **Tier Backup** -> **Last Resort** (`ag/gemini-3-flash`).
    - Các model Trả phí (Claude, Gemini Pro) bị loại bỏ hoàn toàn.
    - Không thêm `groq/openai/gpt-oss-120b` cho đến khi có cấu hình ping ổn định.

## Open Questions

- Không còn câu hỏi tồn đọng. Tôi sẽ giữ 3 tầng dự phòng như bạn đề xuất để đảm bảo tính ổn định và tránh lỗi 404 tầng cuối.

## Verification Plan

### Automated Tests
- Chạy `python scripts/ping_free_tier.py` tập trung vào 4 model chủ lực: Llama 70B, Qwen 32B, Kimi 2.5, Qwen Coder Plus.
- Chạy `python scripts/verify_9router.py` để test agent designer (dùng Qwen 32B).

### Manual Verification
- Kiểm tra log để xem logic fallback có kích hoạt đúng thứ tự Primary -> Backup -> Last Resort không (giả lập bằng cách đổi model name sai tạm thời).

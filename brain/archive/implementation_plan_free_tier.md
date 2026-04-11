# Implementation Plan: Free Tier Transition & Model Expansion

Kế hoạch này thực hiện yêu cầu của người dùng về việc loại bỏ các model trả phí/hot (Claude, Gemini Pro) và mở rộng danh sách các model miễn phí bền bỉ từ 9Router.

## User Review Required

> [!WARNING]
> - **Loại bỏ Model trả phí**: Các model `ag/claude-sonnet-4-6`, `ag/claude-opus-4-6-thinking`, `ag/gemini-3.1-pro-low` và `gc/gemini-3-pro-preview` sẽ bị gỡ bỏ hoàn toàn khỏi logic điều phối.
> - **Model Mặc định mới**: `ag/gemini-3-flash` vẫn giữ vai trò model nhanh, nhưng sẽ có thêm các fallback mạnh mẽ từ Groq và Qwen.

## Proposed Changes

### [libs/core](file:///d:/NoteBookLLM_Br/libs/core)

#### [MODIFY] [llm_client.py](file:///d:/NoteBookLLM_Br/libs/core/llm_client.py)

- **[DONE] Cập nhật `PEDAGOGICAL_MODEL_PRESETS["free"]`**: 
    - **Profiler/Auditor**: `groq/llama-3.3-70b-versatile` (Mạnh hơn Flash về lý luận).
    - **Designer/Evaluator**: `groq/qwen/qwen3-32b` (Mạnh về cấu trúc sư phạm).
    - **Engineer**: `qw/coder-model` (Chuyên biệt code).
    - **Creative**: `nvidia/moonshotai/kimi-k2.5` (Thế mạnh sáng tạo).
- **[DONE] Cấu trúc lại `MODEL_FALLBACK_CHAINS`**: Loại bỏ toàn bộ model trả phí, sử dụng chain hoàn toàn free.
- **[DONE] Tạo tài liệu tham khảo**: [agents-index.md](file:///d:/NoteBookLLM_Br/brain/distilled/agents-index.md).

### [scripts](file:///d:/NoteBookLLM_Br/scripts)

#### [NEW] [ping_free_tier.py](file:///d:/NoteBookLLM_Br/scripts/ping_free_tier.py)
- Script dùng để kiểm tra sức khỏe của riêng các model thuộc "Free Tier" định kỳ.

## Open Questions

- Bạn có muốn giữ lại `gc/gemini-3-flash-preview` như một lựa chọn "Free" không? (Dù là preview nhưng nó phản hồi khá tốt trong bài test vừa rồi).
- Có model nào trong danh sách Discovery bạn muốn ưu tiên đặc biệt không (ví dụ: `qw/vision-model`)?

## Verification Plan

### Automated Tests
- Chạy `python scripts/ping_free_tier.py` để đảm bảo tất cả các model được cấu hình mới đều ONLINE.
- Chạy `python scripts/verify_9router.py` để verify agent swarm.

### Manual Verification
- Kiểm tra Dashboard 9Router để xác nhận traffic không còn chảy về các model Claude/Pro.

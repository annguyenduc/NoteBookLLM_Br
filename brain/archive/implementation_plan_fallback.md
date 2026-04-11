# Implementation Plan: Smart Model Fallback & Agent Bug Fix for 9Router

Kế hoạch này tích hợp cơ chế tự động chuyển đổi model (fallback), xử lý lỗi chuyên sâu (404/429/502) và sửa lỗi ghi đè model mặc định trong `llm_client.py`.

## User Review Required

> [!IMPORTANT]
> - **Cơ chế Fallback**: Hệ thống sẽ tự động duyệt qua `MODEL_FALLBACK_CHAINS` khi gặp lỗi 404 (Model Not Found).
> - **Xử lý 429 (Rate Limit)**: Tự động chờ (Wait) 10-30 giây trước khi thử lại thay vì crash ngay lập tức.
> - **Sửa lỗi Model Override**: Đảm bảo các hàm `call_worker` và `call_designer` không bị ép về Gemini Flash một cách âm thầm.

## Proposed Changes

### [libs/core](file:///d:/NoteBookLLM_Br/libs/core)

#### [MODIFY] [llm_client.py](file:///d:/NoteBookLLM_Br/libs/core/llm_client.py)

- **Thêm `MODEL_FALLBACK_CHAINS`**: Định nghĩa lộ trình dự phòng cho từng loại model.
- **Thêm `_classify_error` & `_call_with_fallback`**: Chuyển đổi toàn bộ hệ thống sang logic fallback thông minh thay vì retry mù quáng.
- **[FIX 1] Thay đổi Default Model**: Sửa `call_worker` giá trị mặc định từ `power-engine` (bị override) thành `"ag/gemini-3-flash"`.
- **[FIX 2] Model Override cho Agent**: Thêm tham số `model` vào `call_pedagogical_agent` và toàn bộ các hàm wrapper (`call_designer`, `call_profiler`, v.v.)
- **Refactor `_resolve_router_model`**: Làm cho logic giải quyết model minh bạch hơn, ưu tiên model được truyền trực tiếp.

## Open Questions

- Các tham số danh sách fallback (`ag/claude-sonnet-4-6`, `ag/claude-opus-4-6-thinking`) đã được kích hoạt trên 9Router của bạn chưa?

## Verification Plan

### Automated Tests
- Chạy `scripts/verify_9router.py` sau khi sửa để xác nhận logic cơ bản.
- Chạy `scripts/test_9router.py` để verify khả năng override model thủ công.

### Manual Verification
- Kiểm tra log tại `storage/logs/` để xác nhận thông báo `[Fallback] Switching to next model` hoạt động đúng khi giả lập lỗi 404 (nếu có thể).

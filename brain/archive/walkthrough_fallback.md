# Walkthrough: Smart Fallback & Model Override Fix

Chúng ta đã hoàn thành việc nâng cấp `llm_client.py` để giải quyết triệt để các vấn đề về độ ổn định của API và lỗi ghi đè model.

## Các thay đổi chính

### 1. Smart Fallback Mechanism
Hệ thống hiện tại không còn "chết đứng" khi gặp lỗi model không tồn tại (404) hoặc bị giới hạn băng thông (429).
- **Lỗi 404**: Tự động chuyển qua model dự phòng trong `MODEL_FALLBACK_CHAINS`.
- **Lỗi 429**: Tạm dừng (Wait) từ 10-30 giây và thử lại.
- **Lỗi 502/503**: Thử lại với cơ chế Exponential Backoff.

### 2. Fix Bug A: Default Override
Trước đây, các hàm `call_worker` sử dụng alias cũ gây ra việc tự động bị ép về Gemini Flash. Chúng tôi đã đổi giá định mặc định sang ID model tường minh `"ag/gemini-3-flash"`.

### 3. Fix Bug B: Pedagogical Model Override
Đã bổ sung tham số `model` vào [llm_client.py](file:///d:/NoteBookLLM_Br/libs/core/llm_client.py) cho các hàm như `call_designer`, `call_profiler`, v.v.
Bạn có thể gọi trực tiếp:
```python
call_designer(messages, model="ag/claude-sonnet-4-6")
```

## Kết quả xác minh

Chúng tôi đã chạy script [verify_9router.py](file:///d:/NoteBookLLM_Br/scripts/verify_9router.py) và thu được kết quả thành công:

> [!NOTE]
> **INFO [Fallback] Trying model: ag/gemini-3-flash (attempt 1/3)**
> **STATUS: 9Router is working perfectly and routing requests!**

## Lưu vết

- **Mã nguồn gốc**: Đã được lưu trữ tại `brain/archive/llm_client_patch_v2.py`.
- **Nhật ký tri thức**: Đã cập nhật tại [log.md](file:///d:/NoteBookLLM_Br/brain/log.md).

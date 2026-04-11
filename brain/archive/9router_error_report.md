# 📊 Báo cáo Lỗi Hệ thống 9Router (AI Gateway)

Báo cáo này tổng hợp các lỗi kỹ thuật được ghi nhận trong quá trình vận hành và Stress Test hệ thống điều phối AI (Swarm Gateway) tại `localhost:20128`.

## 1. Tóm tắt Trạng thái
- **Gateway**: `http://localhost:20128/v1`
- **Model chính**: `ag/gemini-3-flash`
- **Tình trạng**: Đang trong quá trình Stress Test (Phase 1). Gần đây đã ghi nhận các lỗi nghiêm trọng về định danh model và kết nối upstream.

---

## 2. Các Lỗi Nghiêm Trọng Đã Ghi Nhận

### ❌ Lỗi 404: Model Not Found / No Active Credentials
- **Mô tả**: Gateway không nhận diện được model yêu cầu hoặc không tìm thấy thông tin xác thực cho provider.
- **Log thực tế**: `9Router Error (404): {"error":{"message":"No active credentials for provider: openai","type":"invalid_request_error","code":"model_not_found"}}`
- **Nguyên nhân**: 
  - Xung đột cách đặt tên (Nomenclature Collision). Một số script gán prefix `openai/` tự động trong khi gateway yêu cầu prefix `ag/` hoặc định danh thuần túy.
  - Sử dụng các legacy alias (`fast-engine`, `main-engine`) chưa được map đúng trong `llm_client.py` tại thời điểm đó.

### ❌ Lỗi 502: Bad Gateway / Fetch Failed
- **Mô tả**: Lỗi kết nối giữa 9Router và nhà cung cấp dịch vụ thượng nguồn (Upstream - Gemini/OpenRouter).
- **Log thực tế**: `9Router Error (502): {"error":{"message":"[antigravity/gemini-3-flash] [502]: fetch failed (reset after 7s)"}}`
- **Nguyên nhân**:
  - Upstream Provider bị timeout hoặc reset kết nối sau 7 giây.
  - Tải hệ thống cao hoặc sự cố mạng tại thời điểm gọi API.

### ⚠️ Lỗi Xác thực (Authentication)
- **Mô tả**: Script không tìm thấy API Key trong môi trường.
- **Nguyên nhân**: Một số script test (`test_9router_v54.py`) yêu cầu load `.env` từ đường dẫn tuyệt đối `D:/01_Workspaces/SmartProxyHub/.env`. Nếu đường dẫn này không khả dụng hoặc file bị thay đổi, xác thực sẽ thất bại.

---

## 3. Hành động Đang thực hiện

### ✅ Đã triển khai (Fixed/Mitigated)
- **Nomenclature Mapping**: Cập nhật `libs/core/llm_client.py` để chuẩn hóa việc giải quyết model (`_resolve_router_model`).
- **Nâng cấp Tier**: Chuyển đổi một số yêu cầu sang `Tier 1 (Pro/Sonnet)` để tránh giới hạn của bản Free.
- **Sync Rule**: Luôn đồng bộ key từ SmartProxy Hub trước khi thực hiện cuộc gọi.

### 🔄 Đang xử lý (In Progress)
- **Stress Test Multi-Model**: Đang thực hiện Phase 1 để kiểm tra độ trễ (latency) và tỷ lệ lỗi khi gọi model liên tiếp.
- **Monitoring**: Theo dõi `x-request-id` để đối soát với Dashboard của 9Router.

## 4. Khuyến nghị Tiếp theo
1. **Kiểm tra Gateway nội bộ**: Đảm bảo Proxy Hub đang chạy (Service tại Port 4000 hoặc 20128).
2. **Standardize Model IDs**: Tuyệt đối sử dụng Model ID đầy đủ có prefix `ag/` để tránh collision.
3. **Tăng Timeout**: Duy trì mức Timeout 180s cho các tác vụ Audit sư phạm phức tạp.

---
*Báo cáo bởi @pm | Dự án: NoteBookLLM_Br | Ngày: 2026-04-11*

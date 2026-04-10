# 🛡️ Multi-Layer Test Gate (LITE)

> **Goal:** Thiết lập "Cổng kiểm soát" chất lượng tự động. Lệnh `test:gate` là tuyến phòng thủ đầu tiên, xác minh độ an toàn của giao diện, hành vi API, logic nghiệp vụ và tính đồng bộ của đa ngôn ngữ.

## 🏗️ The 5-Layer Defense System
| Layer | Name | Focus |
|---|---|---|
| **L1** | **Frontend Safety** | Chống "màn hình trắng", lỗi cú pháp JS, lỗi thẻ HTML. |
| **L2** | **API Routes** | Đảm bảo Endpoint phản hồi đúng (200 OK), handle JSON sạch. |
| **L3** | **Business Logic**| Test các hàm tính toán, xử lý dữ liệu thuần túy (Pure logic). |
| **L4** | **i18n Sync** | Đảm bảo các file ngôn ngữ có cấu trúc và số lượng key bằng nhau. |
| **L5** | **Security Scan** | Quét Secret, thông tin nhạy cảm không được commit vào Git. |

## 🛠️ Implementation Protocol
1. **Stack Detection:** Xác định framework (React, Vue, Workers) để cài đặt Vitest/Jest phù hợp.
2. **Environment Setup:** Cấu hình `vitest.config.ts`, `jsdom`, và các file setup test.
3. **Core Test Files:** Tạo riêng biệt 5 file test tương ứng cho 5 Layer trên (Không gộp chung).
4. **Script Wiring:** Thêm `"test:gate": "vitest run --reporter=verbose"` vào `package.json`.
5. **Verification:** Chạy thử `npm run test:gate` để chứng minh hệ thống hoạt động.

## 🚨 Quality Gate (Red Flags)
- ❌ Gộp tất cả các tầng test vào một file duy nhất (Gây khó bảo trì).
- ❌ Sử dụng thông tin đăng nhập (Credentials) thật của Production trong môi trường test.
- ❌ Bỏ qua lớp L1 (Frontend Safety) đối với các dự án SPA/Giao diện phức tạp.
- ❌ Cố tình bỏ qua (Skip) các test case thất bại để tiếp tục Deploy.

## 💡 Example Triggers
- "Thiết lập hệ thống test gate cho project này."
- "Cài đặt tự động kiểm tra đa ngôn ngữ."
- "Tạo cổng kiểm soát chất lượng trước khi deploy."

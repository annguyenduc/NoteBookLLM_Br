# 📊 STEAM K-12 Dashboard (LITE)

> **Goal:** Cung cấp trung tâm điều khiển (Control Center) cho chuyên viên thiết kế bài học. Hiển thị Kanban board, thống kê bài học, bộ nhớ phiên làm việc và các lối tắt kích hoạt skill nhanh.

## 🚀 Interactive Features
- **Kanban Tracker:** 4 cột (Backlog, Draft, Review, Done). Double-click để chuyển trạng thái.
- **Real-time Stats:** Tự động đếm tổng số bài học, tỷ lệ hoàn thành và các task đang thực hiện.
- **Quick Launch:** Danh sách các Skill STEAM K-12 (Lesson Architect, assessment, etc.) kèm nút copy Trigger nhanh.
- **Memory Log:** Ghi chép nhanh các quyết định quan trọng ngay trên dashboard.
- **Persistence:** Lưu trữ bằng `localStorage`, không sợ mất dữ liệu khi Refresh hoặc tắt trình duyệt.

## 🛠️ Implementation Workflow
Khi người dùng gõ lệnh "dashboard" hoặc "mở dashboard":
1. **Generate File:** Tạo file `steam-dashboard.html` tại thư mục hiện tại.
2. **Inject Content:** Đưa mã HTML/CSS/JS (Lightweight) vào file.
3. **Notify:** Thông báo: "✅ Dashboard đã sẵn sàng tại `steam-dashboard.html`. Hãy mở bằng trình duyệt."

## 📐 Design Standards
- **Style:** Dark mode Premium, giao diện Kanban hiện đại.
- **No Dependencies:** Không sử dụng thư viện ngoài, chạy 100% bằng Vanilla JS/CSS.
- **Self-contained:** Mọi logic xử lý và lưu trữ nằm gọn trong 1 file HTML duy nhất.

## 🚨 Quality Gate (Red Flags)
- ❌ Yêu cầu người dùng cài đặt Server hoặc môi trường phức tạp để chạy dashboard.
- ❌ Logic lưu trữ bị mất sau khi tắt trình duyệt (Phải dùng `localStorage`).
- ❌ Giao diện quá đơn giản, không đủ độ "WOW" (Premium feeling).
- ❌ Thiếu các nút Quick Launch dẫn đến dashboard chỉ mang tính xem, không giúp thực thi.

## 💡 Example Triggers
- "Mở dashboard theo dõi tiến độ bài học."
- "Xem tổng quan dự án STEAM."
- "dashboard"



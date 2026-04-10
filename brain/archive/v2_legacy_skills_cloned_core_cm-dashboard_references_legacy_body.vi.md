# 📊 Dashboard (LITE)

> **Goal:** Cung cấp cái nhìn tổng quan về tiến độ dự án thông qua bảng Kanban trực quan (Markdown). Chuyển đổi dữ liệu từ `task.md` hoặc `cm-tasks.json` thành trạng thái hành động.

## 🛠️ Dashboard Command: `/cm-dashboard`
Khi lệnh này được gọi, AI Assistant thực hiện:
1. **Data Fetch:** Đọc file `task.md` hoặc `cm-tasks.json`.
2. **Kanban Render:** Tạo bảng Markdown với 3 cột:
   - **🔴 TO DO:** Những task chưa bắt đầu.
   - **🟡 IN PROGRESS:** Những task đang xử lý.
   - **🟢 DONE:** Những task đã hoàn thành.
3. **Flow Report:** Tóm tắt ngắn gọn Chế độ hiện tại (Planning/Execution/Verification) và Bước tiếp theo (Next Step).

## 🚨 Quality Gate (Red Flags)
- ❌ Hiển thị thông tin task lỗi thời do không đọc `task.md` mới nhất.
- ❌ Thiếu cột trạng thái quan trọng khiến User không nắm được tiến độ.
- ❌ Báo cáo sai Mode hiện tại so với thực tế đang thực thi.

## 💡 Example Triggers
- "/cm-dashboard"
- "Cho tôi xem bảng Kanban tiến độ."
- "Dashboard status: xem task nào đang bị nghẽn."

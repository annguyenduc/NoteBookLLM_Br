---
file_id: "WIKI_ROBOT_Rover_Expansion"
title: "Module Mở rộng & Tính năng Nâng cao (Rover & xBot)"
category: "Robot"
sub_category: "Expansion"
prefix: "WIKI"
tags: ["Gripper", "Servo", "AI", "IOT", "OhStem"]
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🚀 Module Mở rộng & Tính năng Nâng cao (Rover & xBot)

Tài liệu này tập trung vào các thành phần mở rộng giúp nâng cấp khả năng của Robot OhStem, từ cơ cấu cơ khí đến trí tuệ nhân tạo.

---

## 🦾 1. Hệ thống Tay gắp (Gripper) & Servo

Tay gắp là module mở rộng phổ biến nhất, cho phép robot tương tác vật lý với môi trường.

### Động cơ Servo MG90S
- **Đặc tính:** Là động cơ điều khiển góc xoay chính xác từ **0° đến 180°**.
- **Kết nối dây:** 3 dây tín hiệu phân biệt theo màu:
    - **Đỏ:** Cực dương (+).
    - **Nâu/Đen:** Cực âm (-).
    - **Cam/Vàng:** Dây tín hiệu (Signal).
- **Cách kết nối:** Gắn vào các chân mở rộng (như S1, S2, S3) trên mạch mở rộng của Rover/xController.

### Lập trình Điều khiển Tay gắp
- **Logic Đóng/Mở:** 
    - Để mở tay gắp: Xoay Servo đến góc nhất định (Ví dụ: 90°).
    - Để đóng tay gắp: Xoay Servo về góc ban đầu (Ví dụ: 0°).
- **Lập trình bước:** Có thể cộng/trừ góc xoay hiện tại (Ví dụ: mỗi lần nhấn nút A, mở thêm 30°).

---

## 🧠 2. Trí tuệ Nhân tạo (AI) & Nhận diện

Dòng Rover (qua Yolobit) hỗ trợ mạnh mẽ các tính năng AI thông qua OhStem App.

### Nhận diện Hình ảnh (Image Recognition)
- **Quy trình:** Huấn luyện mô hình AI trên máy tính ➔ Kết nối Bluetooth với Robot ➔ Chạy chương trình "Lập trình AI".
- **Ứng dụng:** Robot di chuyển theo biển báo, phân loại rác thải, nhận diện khuôn mặt để chào hỏi.

### Nhận diện Giọng nói (Speech Recognition)
- **Ngôn ngữ:** Hỗ trợ đa ngôn ngữ (Tiếng Việt, Tiếng Anh).
- **Khối lệnh chính:**
    - `Kết quả nhận diện giọng nói`: Trả về chuỗi ký tự âm thanh thu được.
    - `Nếu kết quả nhận diện có chứa [từ khóa]`: Thực hiện hành động tương ứng (Ví dụ: nói "Bật đèn" -> bật LED).

---

## 🌐 3. Hệ sinh thái IOT (Internet of Things)

Khả năng kết nối vạn vật giúp Robot có thể được điều khiển từ xa qua Internet.

### Kết nối Wifi
- Cần nạp khối lệnh mở rộng "Wifi" để Robot kết nối vào mạng nội bộ.

### Bảng điều khiển IOT (IOT Dashboard)
- **Chức năng:** Tạo các nút nhấn, thanh trượt hoặc biểu đồ trên trình duyệt/điện thoại để:
    - Gửi lệnh điều khiển cho Robot.
    - Hiển thị dữ liệu cảm biến (nhiệt độ, khoảng cách) theo thời gian thực.

---

## 🔗 Liên kết Wiki & Nguồn
- [[WIKI_ROBOT_Hardware_Master]] — Các cổng kết nối Servo.
- [[WIKI_ROBOT_Logic_Master]] — Cách sử dụng biến để lưu trạng thái Servo.
- [[KB_ROBOT_Master]] — Tổng hợp tri thức.

**📖 Nguồn xác thực:**
- [[brain/raw/Robot_Rover_de_trac_nghiem_1_-_rover.md]] (Câu 16-23)
- [[brain/raw/Robot_xBot_de_trac_nghiem_1_-_xbot.md]]
- `WIKI_Machine_Learning_Teachable_Machine.md` (Đối chiếu quy trình AI)

---
**Xác nhận bởi @auditor: 2026-04-26**

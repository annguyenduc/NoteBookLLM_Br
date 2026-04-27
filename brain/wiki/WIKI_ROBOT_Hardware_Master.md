---
file_id: "WIKI_ROBOT_Hardware_Master"
title: "Trụ cột Phần cứng Robot (xBot & Rover)"
category: "Robot"
sub_category: "Hardware"
prefix: "WIKI"
tags: ["xBot", "Rover", "Hardware", "OhStem", "Sensors"]
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🏗️ Trụ cột Phần cứng Robot (xBot & Rover)

Tài liệu này tổng hợp cấu trúc phần cứng và các chuẩn kết nối của hệ sinh thái Robot OhStem, tập trung vào hai dòng chính: **xBot** và **Rover**.

---

## 🤖 1. Robot xBot (Sử dụng xController)

xBot là dòng robot giáo dục đa năng sử dụng mạch điều khiển chuyên dụng **xController**.

### 📱 Bộ xử lý & Cổng kết nối
- **Mạch điều khiển:** xController.
- **Cổng mở rộng:** **6 cổng** (đánh số từ 1 đến 6) dùng để kết nối các module ngoại vi.
- **Kết nối máy tính:** Sử dụng cáp **USB Type C** hoặc Bluetooth.
- **Pin:** Thường sử dụng pin sạc Li-ion 3.7V (2 viên).

### 📡 Linh kiện tích hợp & Ngoại vi
- **Đèn LED:** Tích hợp 2 đèn LED RGB trên board.
- **Âm thanh:** Buzzer tích hợp để phát nhạc/cảnh báo.
- **Cảm biến siêu âm:** Kết nối qua cổng RJ11, dùng để đo khoảng cách và né vật cản.
- **Cảm biến dò line:** Thường sử dụng module **4 mắt đọc** hồng ngoại.
- **Động cơ:** 2 động cơ DC (động cơ vàng) điều khiển bánh xe.

---

## 🏎️ 2. Robot Rover (Sử dụng Yolobit)

Rover là dòng robot 4 bánh linh hoạt, tận dụng sức mạnh của mạch lập trình **Yolobit**.

### 🧠 Bộ xử lý & Cấu trúc
- **Mạch điều khiển:** **Yolobit** (đóng vai trò là bộ não, gắn vào mạch mở rộng của Rover).
- **Cảm biến gia tốc:** Tích hợp sẵn trên Yolobit, hỗ trợ nhận biết độ nghiêng/va chạm qua 3 trục (X, Y, Z).
- **Màn hình LED:** Ma trận 5x5 trên Yolobit dùng để hiển thị biểu cảm/thông tin.

### 🔌 Khả năng kết nối
- **Cổng mở rộng:** Hỗ trợ các cổng Grove/RJ11 để mở rộng linh kiện.
- **Mắt nhận hồng ngoại:** Tích hợp sẵn để nhận tín hiệu điều khiển từ Remote IR.
- **Bluetooth:** Tích hợp trên Yolobit để kết nối App Gamepad.

### 💡 Hệ thống đèn & Cảm biến
- **Đèn pha:** 2 đèn LED pha phía trước (thường dùng làm đèn chiếu sáng hoặc báo hiệu).
- **Đèn gầm:** Hệ thống LED RGB phía dưới tạo hiệu ứng màu sắc.
- **Cảm biến dò line:** Tích hợp 4 mắt đọc hồng ngoại phía dưới gầm.
- **Cảm biến siêu âm:** Lắp phía trước để phát hiện vật cản.

---

## 📏 3. Nguyên lý Vận hành Chung

### 🦇 Cảm biến Siêu âm (Ultrasonic Sensor)
- **Nguyên lý:** Phát sóng siêu âm và đo thời gian phản hồi để tính khoảng cách.
- **Ứng dụng:** Né vật cản, di chuyển theo người (bám đuôi), đo kích thước vật thể.

### 🛤️ Cảm biến Dò đường (Line Follower)
- **Nguyên lý:** Sử dụng tia **hồng ngoại (IR)**. Nền trắng phản xạ hồng ngoại (đèn tắt), vạch đen hấp thụ hồng ngoại (đèn sáng).
- **Cấu tạo:** 4 mắt đọc giúp robot nhận diện ngã tư, cua gắt và lệch quỹ đạo chính xác hơn.

### 🎮 Giao tiếp & Điều khiển
- **OhStem App:** Giao diện lập trình khối lệnh (Blockly) và điều khiển qua Bluetooth.
- **Remote IR:** Điều khiển bằng tín hiệu hồng ngoại trong phạm vi hẹp.
- **Gamepad:** Chế độ điều khiển từ xa bằng điện thoại/máy tính bảng.

---

## 🔗 Liên kết Wiki & Nguồn
- [[WIKI_ROBOT_Logic_Master]] — Tư duy lập trình chung cho Robot.
- [[WIKI_ROBOT_Rover_Expansion]] — Các module đặc thù cho Rover (Tay gắp, AI).
- [[KB_ROBOT_Master]] — Bản tóm tắt tri thức Robotics.

**📖 Nguồn xác thực:**
- [[brain/raw/Robot_xBot_de_trac_nghiem_1_-_xbot.md]]
- [[brain/raw/Robot_Rover_de_trac_nghiem_1_-_rover.md]]
- `WIKI_Codey_Rocky_System.md` (Đối chiếu hệ sinh thái mBlock)

---
**Xác nhận bởi @auditor: 2026-04-26**

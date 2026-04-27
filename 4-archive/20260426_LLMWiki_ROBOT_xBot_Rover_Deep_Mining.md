---
file_id: "ROBOT_xBot_Rover_Deep_Mining"
title: "Khai thác tri thức Robotics (xBot & Rover)"
category: "Process Log"
prefix: "ROBOT"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# ⛏️ Robotics (xBot & Rover) - Báo cáo Khai thác sâu tri thức

### 📊 Thống kê hiệu suất Khai thác (Mining Stats)
| Chỉ số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| **Số tệp nguồn đã quét** | 12 tệp | Toàn bộ kho raw xBot và Rover OhStem |
| **Tổng số câu hỏi** | 240 câu | Trung bình 20 câu/đề |
| **Nguyên tử tri thức (Atoms)** | 25 | Concepts độc lập về phần cứng và Python |
| **Tỷ lệ tri thức/câu hỏi** | **1 : 9.6** | Mật độ tri thức khá cao cho các lệnh Python |

---

## 📂 PHẦN CỨNG (HARDWARE)

### 1.1. Hệ thống xController (xBot)
- **Cổng kết nối**: Có 4 cổng mở rộng (Port 1-4) dùng chuẩn RJ11. (Nguồn: `Robot_xBot_de_trac_nghiem_1` - Q3).
- **Động cơ**: 2 cổng Motor (M1, M2) và 2 cổng Servo (S1, S2). (Nguồn: `Robot_xBot_de_trac_nghiem_1` - Q5, Q6).
- **Tích hợp**: 2 đèn LED RGB, Buzzer và cảm biến hồng ngoại thu xa.

### 1.2. Hệ thống Yolo:Bit & Rover Shield
- **Bộ não**: Sử dụng Yolo:Bit với ma trận LED 5x5.
- **Shield mở rộng**: Cung cấp 4 cổng RJ11, 2 cổng motor. (Nguồn: `Robot_Rover_de_trac_nghiem_1`).
- **Cổng cảm biến**: Siêu âm cắm Port 1, Dò đường (mắt lẻ) cắm Port 2. (Nguồn: `Robot_Rover_de_trac_nghiem_5` - Q8).
- **Đèn RGB**: Tích hợp 2 mắt LED RGB phía trước.
- **Tay gắp (Gripper)**: Sử dụng động cơ Servo kết nối qua cổng S1/S2 trên Shield. (Nguồn: `Robot_Rover_de_trac_nghiem_2`).
- **Cảm biến mở rộng**: Cảm biến màu sắc và cảm biến âm thanh thường được cắm vào Port 3 hoặc 4.

---

## 📂 LẬP TRÌNH PYTHON (LOGIC)

### 2.1. Thư viện & Khởi tạo
- **xBot**: `from xbot import *`.
- **Rover**: `from rover import *`.

### 2.2. Lệnh di chuyển & Hiệu ứng
- **Tốc độ**: Phạm vi từ 0 đến 100. (Nguồn: `Robot_Rover_de_trac_nghiem_3`).
- **Lệnh rẽ**: `rover.turn_left(speed)`, `rover.turn_right(speed)`.
- **Hiển thị**: `display.show(Image.HEART)` trên ma trận LED Yolo:Bit.
- **Màu sắc**: Sử dụng tuple RGB (R, G, B) hoặc mã Hex.

### 2.3. Cảm biến & Điều kiện
- **Siêu âm**: `rover.get_distance()` trả về giá trị cm.
- **Tay gắp (Servo)**: `rover.servo(index, angle)` (index 1: S1, 2: S2).
- **Dò line**: `rover.read_line_sensors()` trả về trạng thái vạch đen/trắng. (Nguồn: `Robot_Rover_de_trac_nghiem_4`).

---
*Báo cáo được khởi tạo theo chuẩn Swarm 4.0 Supreme. Mọi thay đổi phải cập nhật lại bảng thống kê.*

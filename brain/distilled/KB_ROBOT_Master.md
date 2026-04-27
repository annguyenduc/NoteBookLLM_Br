---
file_id: "KB_ROBOT_Master"
title: "Tri thức cốt lõi Robotics (xBot & Rover)"
category: "Distilled Knowledge"
prefix: "KB"
tags: ["Robotics", "OhStem", "xBot", "Rover", "Python"]
source: "Multiple Wiki Atoms"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# 🤖 Tri thức cốt lõi Robotics (xBot & Rover)

Tệp này chưng cất (distill) toàn bộ tri thức kỹ thuật và logic lập trình cho hệ sinh thái robot giáo dục của OhStem, phục vụ làm "Ground Truth" cho việc ra đề thi và phát triển khóa học.

## 1. 🏗️ Phân tầng Phần cứng (Hardware Architecture)

Hệ sinh thái OhStem chia làm 2 nhánh phần cứng chính:

### 1.1. Dòng xBot (Sử dụng xController)
- **Chuẩn kết nối**: RJ11 (chống cắm ngược).
- **Cổng giao tiếp**:
  - 4 Port mở rộng (Port 1, 2, 3, 4) cho cảm biến.
  - 2 Port Motor (M1, M2) cho động cơ DC di chuyển.
  - 2 Port Servo (S1, S2) cho động cơ Servo (góc quay).
- **Tích hợp sẵn**: 2 đèn LED RGB, Buzzer (loa), nút nhấn.

### 1.2. Dòng Rover (Sử dụng Yolo:Bit + Shield)
- **Bộ não Yolo:Bit**: Sở hữu ma trận LED 5x5, 2 nút nhấn (A, B) và các cảm biến nâng cao (Gia tốc, la bàn, ánh sáng, nhiệt độ).
- **Rover Shield (Mạch mở rộng)**:
  - 4 Port mở rộng chuẩn RJ11.
  - **Sơ đồ cắm chuẩn**: Siêu âm (Port 1), Dò line (tích hợp hoặc Port 2), Cảm biến màu (Port 3/4).
- **Mở rộng (Expansion)**: Tay gắp (Gripper) sử dụng động cơ Servo cắm vào cổng S1 hoặc S2.

---

## 2. 🧠 Mô thức Lập trình (Python Logic Patterns)

Định hướng ngôn ngữ chính là **Python** (không sử dụng mBlock).

### 2.1. Khởi tạo & Lệnh cơ bản
- **Thư viện**: `from xbot import *` hoặc `from rover import *`.
- **Di chuyển**: Tốc độ định tuyến từ 0 đến 100%. Các lệnh chính: `forward(speed)`, `backward(speed)`, `turn_left(speed)`, `turn_right(speed)`, `stop()`.

### 2.2. Logic Cảm biến & Điều khiển
| Bài toán | Thiết bị | Lệnh Python | Logic Xử lý |
| :--- | :--- | :--- | :--- |
| **Tránh vật cản** | Cảm biến Siêu âm | `rover.get_distance()` | Nếu khoảng cách < ngưỡng (ví dụ 15cm) ➔ Dừng hoặc rẽ. |
| **Dò đường (Line)** | Cảm biến Hồng ngoại | `rover.read_line_sensors()` | (0,0): Tiến thẳng. <br>(1,0): Lệch trái ➔ Rẽ phải. <br>(0,1): Lệch phải ➔ Rẽ trái. |
| **Gắp vật thể** | Tay gắp (Servo) | `rover.servo(index, angle)` | Index (1/2 tương ứng S1/S2). Thay đổi góc `angle` để mở/đóng. |
| **Tương tác màu** | Cảm biến Màu sắc | (Thư viện mở rộng) | Nhận diện Đỏ, Xanh, Vàng ➔ Đưa ra quyết định dừng hoặc rẽ. |

### 2.3. Hiển thị Trực quan
- **LED RGB (Mắt robot)**: `rover.show_led(0, (R, G, B))` (0 điều khiển cả 2 mắt).
- **Ma trận Yolo:Bit**: `display.show(Image.SMILE)`, `display.scroll('Hello')`.

---

## 3. 🎯 Hướng dẫn Đánh giá (Assessment Guidelines)

Khi xây dựng câu hỏi trắc nghiệm (MCQ) hoặc bài tập thực hành:
1. **Phân biệt rạch ròi Board mạch**: Câu hỏi về ma trận LED 5x5 phải gắn với Rover/Yolo:Bit, không được hỏi cho xBot/xController.
2. **Cú pháp Python chuẩn xác**: Luôn sử dụng cú pháp snake_case của thư viện (`get_distance`, `read_line_sensors`).
3. **Logic vận hành**: Đặc biệt lưu ý bảng trạng thái (0,0), (1,0), (0,1) của cảm biến dò đường.

---
**Xác nhận bởi @pm & @librarian: 2026-04-25**

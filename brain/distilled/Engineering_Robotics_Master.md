# 🤖 Engineering & Robotics Handbook (Master)

> **Mô tả**: Tổng hợp toàn bộ kỹ thuật hệ thống nhúng, thiết kế Robot và in 3D được đúc kết từ thực tế dự án Mars Rover, Yolo_UNO và ESP8266.

## 1. 🚜 Robotics & Embedded Systems (Mars Rover & Yolo_UNO)
- **Mars Rover Architecture**: Cơ cấu servo, điều khiển chuyển động và tích hợp cảm biến (siêu âm, PIR).
- **Yolo_UNO IoT Integration**: Tích hợp Teachable Machine, Blynk/Wifi và điều khiển đèn LED/Relay.
- **ESP8266 & Arduino**: Lập trình cảm biến DHT11, module Bluetooth HC-06 và kỹ thuật giải quyết lỗi COM Port (COM5).
- **Hardware Best Practices**: Sơ đồ nối chân (Pin Map), kịch bản Fail-safe và nguyên tắc cấp nguồn cho động cơ/servo.

### Thuật toán Điều khiển Robot
- **PID (Proportional-Integral-Derivative)**: Giúp robot bám line mượt mà.
    - **P (Tỷ lệ)**: Phản ứng với sai số hiện tại.
    - **I (Tích phân)**: Triệt tiêu sai số tích lũy (giúp robot không bị lệch hẳn).
    - **D (Đạo hàm)**: Dự đoán sai số tương lai để giảm rung lắc.
- **State Machine (Máy trạng thái)**: Sử dụng để xử lý logic đa nhiệm. Các trạng thái phổ biến: `FOLLOW_LINE`, `INTERSECTION`, `OBSTACLE_DETECTED`, `STATION_STOP`.

### Kiến trúc Decompiler (MicroPython to Blockly)
Quy trình dịch ngược mã nguồn sang khối lệnh kéo thả:
- **Parser**: Phân tích cú pháp MicroPython dựa trên thư viện `ast` (Abstract Syntax Tree).
- **Mapping**: Đối chiếu các hàm Python (ví dụ: `pin1.write_digital(1)`) sang ID của khối Blockly tương ứng.
- **Generator**: Xuất ra tệp JSON định dạng workspace của Google Blockly.

## 2. 🖨️ 3D Printing & Design (Neptune 4 Focus)
### Kỹ thuật Bù trừ (Horizontal Expansion)
- **OD (Kích thước ngoài)**: Tăng +0.25mm với Horizontal Expansion = +0.125.
- **ID (Kích thước lỗ)**: Giảm -0.25mm. Công thức CAD: `D_CAD = D_truc + 0.50mm`.
- **Infill & Wall**: Thông số in PLA chuẩn cho Neptune 4, kỹ thuật bù trừ dung sai cho lắp khít (Snug Fit).
- **Maintenance**: Xử lý kẹt nhựa, sấy mực ẩm (nhiệt độ/thời gian), và tối ưu hóa file Cura.

## 3. 🛡️ IoT Security & Networking
- **ESP8266 Brute Force**: Nghiên cứu khả năng bảo mật và các biện pháp bảo mật IoT cơ bản.
- **Wifi & Bluetooth**: Giả lập kết nối, cấu hình IP addressing cho học sinh và khắc phục lag tín hiệu Yolo.

---
*Ghi chú: Nội dung được hợp nhất từ 42 tệp kỹ thuật legacy.*
*Tham khảo chi tiết tại bộ lưu trữ Archive/v2_legacy.*

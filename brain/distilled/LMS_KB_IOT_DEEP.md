# ⚡ LMS Deep Knowledge: Module IoT & Tự động hóa

> **Mô tả**: Tổng hợp tri thức chuyên sâu CHỈ từ các bộ đề Arduino, YoloBit.
> **Kiểm định bởi**: @auditor (AG-SWARM-006)
> **Trạng thái**: ĐÃ CHUẨN HÓA TRÍCH DẪN (Verify bởi @pm v6.2)

---

## 🏗️ 1. Hệ sinh thái Thiết bị & Board mạch

| Thiết bị | Đặc điểm Kỹ thuật (Khai thác từ đề thi) | Trích dẫn nguồn |
| :--- | :--- | :--- |
| **Yolo:Bit** | Board mạch IoT. Ma trận LED 5x5 (25 RGB LEDs). Cảm biến: Nhiệt độ, Ánh sáng (mặt trước), Gia tốc (mặt sau). Nút nhấn A/B. Loa tích hợp. | [YoloBit_01] |
| **Arduino Uno** | Board mạch nhúng. Chân Digital (D0-D13 - hạn chế dùng D0, D1), Analog (A0-A5 - 1024 giá trị), PWM (256 giá trị). | [Arduino_M1] |
| **Breadboard** | Bo cắm thử nghiệm. Thanh nguồn (+) (-) nối ngang; các lỗ linh kiện nối dọc thành từng cụm 5 lỗ. | [Arduino_M1] |

---

## 🌍 2. Internet of Things (IoT) & Dashboard

Hệ thống tập trung vào việc giám sát và điều khiển qua Internet:

- **Kết nối Dashboard**: Sử dụng OhStem Web/App. Gửi dữ liệu cảm biến (Nhiệt độ, Độ ẩm đất, Ánh sáng) lên các "Widget/Gadget" để theo dõi. `[Nguồn: YoloBit_01]`
- **Điều khiển từ xa**: Nhận lệnh từ nút nhấn hoặc thanh gạt trên Dashboard để bật/tắt thiết bị ngoại vi (Đèn, Máy bơm). `[Nguồn: YoloBit_01]`
- **Cơ chế Tự động hóa**: Sự kết hợp giữa `Nếu [Giá trị cảm biến] < [Ngưỡng]` thì `Thực hiện hành động`. `[Nguồn: Arduino_M2]`

---

## 🛠️ 3. Linh kiện & Giao tiếp (Sensors & Actuators)

- **Cảm biến (Input)**:
    - **Siêu âm (HC-SR04)**: Đo khoảng cách (2cm - vô hạn). Gồm 2 đầu: Trig (phát) và Echo (thu). `[Nguồn: Arduino_M2]`
    - **DHT11/DHT20**: Đo nhiệt độ và độ ẩm không khí. Cần đợi cập nhật mỗi 2 giây. `[Nguồn: Arduino_M2/YoloBit_01]`
    - **PIR**: Phát hiện chuyển động của vật thể phát bức xạ hồng ngoại (con người). `[Nguồn: YoloBit_01]`
- **Cơ cấu chấp hành (Output)**:
    - **LCD 1602**: Hiển thị văn bản. Dùng module I2C (4 chân: GND, VCC, SDA, SCL). SDA nối A4, SCL nối A5 trên Arduino. `[Nguồn: Arduino_M2]`
    - **Servo (MG90S)**: Động cơ quay góc (0-180 độ). Dây Cam (Tín hiệu), Đỏ (5V), Nâu (GND). `[Nguồn: Arduino_M1]`
    - **L298**: Mạch cầu H điều khiển động cơ DC (động cơ vàng/bơm). `[Nguồn: Arduino_M2/Joystick]`

---

## 🚩 4. Lỗi thường gặp & An toàn

1. **Sai nguồn cấp**: Cảm biến 5V nếu nối vào chân 3.3V sẽ hoạt động không chính xác. Đèn LED gãy chân phân biệt bằng bản cực: bản to (Âm), bản nhỏ (Dương). `[Nguồn: Arduino_M1]`
2. **Lỗi I2C**: Không hiển thị màn hình LCD do sai địa chỉ I2C hoặc lỏng chân SDA/SCL. `[Nguồn: Arduino_M2]`
3. **Lỗi Logic Joystick**: Giá trị nghỉ là ~511. Đẩy lên/xuống làm giá trị Y thay đổi về 0 hoặc lên 1023. `[Nguồn: Joystick_M1]`

---
*Verify Source Checklist:*
- `[YoloBit_01]`: LMS_Tests_IOT_YoloBit_de-trac-nghiem-1-yolobit.md
- `[Arduino_M1]`: LMS_Tests_IOT_Arduino_1_de-kiem-tra-arduino-module-1.md
- `[Arduino_M2]`: LMS_Tests_IOT_Arduino_2_de-1-trac-nghiem-arduino.md

---
file_id: "WIKI_IOT_Arduino_Advanced"
title: "Kiến thức Arduino Nâng cao & Phức hợp"
category: "Advanced Wiki"
prefix: "WIKI"
tags: ['Arduino', 'Advanced', 'Sensors', 'Automation', 'Robotics']
source: "[[120_Cau_Hoi_IOT_Arduino_LMS]]"
status: "verified"
created: "2026-04-25"
last_updated: "2026-04-25"
---

# 🚀 Kiến thức Arduino Nâng cao & Phức hợp

Tài liệu này đi sâu vào chi tiết kỹ thuật, đấu nối và logic xử lý phức hợp được đúc kết từ 120 câu hỏi sát hạch Arduino.

---

## 1. Màn hình LCD 1602 (Giao tiếp I2C)

Đây là thiết bị hiển thị phổ biến nhất trong các dự án Smart Home và Smart City.

### 1.1. Chi tiết đấu nối (I2C Interface)
Sử dụng Module I2C giúp tiết kiệm chân Arduino (chỉ dùng 2 chân thay vì 6 chân).
- **GND**: Nối cực âm (GND).
- **VCC**: Nối nguồn 5V.
- **SDA (Data)**: Chân **A4** (Arduino Uno).
- **SCL (Clock)**: Chân **A5** (Arduino Uno).
- **Địa chỉ I2C**: Thường là `0x27` hoặc `0x3F`.

### 1.2. Logic Hiển thị nâng cao
- **Tọa độ**: Cột (0-15), Dòng (0-1).
    - `lcd.setCursor(0, 0)`: Đầu dòng 1.
    - `lcd.setCursor(0, 1)`: Đầu dòng 2.
- **Quy tắc làm mới**: Luôn dùng lệnh **Xóa (Clear)** trước khi ghi nội dung mới có độ dài ngắn hơn nội dung cũ để tránh hiện tượng "chữ ma" (rác dữ liệu).
- **Ứng dụng**: Hiển thị giá trị cảm biến kèm đơn vị (Ví dụ: "N.Do: 25 do C"). (Nguồn: `IOT_MCQ_Arduino_De2_Q07`)

---

## 2. Hệ thống Xe Robot & Động cơ (L298 Driver)

### 2.1. Hiệu chuẩn di chuyển (Calibration)
Trong thực tế, hai động cơ vàng hiếm khi quay cùng tốc độ. Để xe chạy thẳng:
- **Lỗi**: Cấp cùng mức HIGH/LOW cho cả 2 bên nhưng xe bị lệch.
- **Giải pháp**: Sử dụng chân **PWM** (các chân có dấu `~`) để điều chỉnh giá trị từ 0-255. Bánh nào chạy nhanh hơn thì giảm PWM bánh đó xuống. (Nguồn: `IOT_MCQ_Arduino_De1_Q60`)

### 2.2. Điều khiển bằng Joystick
Joystick trả về giá trị Analog (0-1023) trên 2 trục X và Y.
- **Ngưỡng chết (Deadzone)**: Từ 400 đến 600. Trong khoảng này robot đứng yên.
- **Logic di chuyển**:
    - `Y < 400`: Robot đi tới.
    - `Y > 600`: Robot đi lùi.
    - `X < 400`: Robot xoay trái.
    - `X > 600`: Robot xoay phải.
(Nguồn: `IOT_MCQ_Arduino_De1_Q60`, `NON_MCQ_IOT_Arduino_De4_Q01`)

---

## 3. Cảm biến Nâng cao & Logic Tương tác

### 3.1. Cảm biến Siêu âm (Distance Sensor)
- **Trig (Trigger)**: Chân phát sóng siêu âm.
- **Echo**: Chân nhận sóng phản hồi.
- **Logic**: Nếu khoảng cách `< 10cm` thì thực hiện né vật cản hoặc dừng lại. (Nguồn: `IOT_MCQ_Arduino_De1_Q09`)

### 3.2. Cảm biến DHT11 (Nhiệt độ & Độ ẩm)
- **Đặc điểm**: Trả về dữ liệu kỹ thuật số (Digital) nhưng cần xử lý qua thư viện để bóc tách nhiệt độ và độ ẩm riêng biệt.
- **Logic tương tác**: `Nếu Nhiệt độ > 27 thì Bật quạt/LED đỏ`. (Nguồn: `IOT_MCQ_Arduino_De2_Q07`)

### 3.3. Cảm biến Mưa & Hồng ngoại
- **Logic Mưa**: Thường dùng Analog (AO) để đo mức độ mưa hoặc Digital (DO) để biết có mưa hay không.
- **Logic Hồng ngoại**: `Vật cản = 0`, `Không vật cản = 1`. (Nguồn: `IOT_MCQ_Arduino_De1_Q50`)

---

## 4. Bảng Tra cứu Nguồn (Audit Trail)

| Chủ đề | Trích dẫn (Reference) | Fact xác thực |
|:---|:---|:---|
| **LCD Pins** | `IOT_MCQ_Arduino_De1_Q15` | SDA=A4, SCL=A5 |
| **LCD Cursor** | `IOT_MCQ_Arduino_De2_Q07` | Set cursor (0,0) cho dòng 1 |
| **Motor L298** | `IOT_MCQ_Arduino_De1_Q60` | Đảo chân để xe đi thẳng |
| **Joystick Threshold** | `NON_MCQ_IOT_Arduino_De4_Q01` | Ngưỡng 400 và 600 |
| **PIR / IR Sensor** | `IOT_MCQ_Arduino_De1_Q50` | Logic 0/1 |
| **Ultrasonic** | `IOT_MCQ_Arduino_De1_Q09` | Trig/Echo Pins |
| **Buzzer Pins** | `IOT_MCQ_Arduino_De1_Q33` | Dài (+), Ngắn (-) |
| **Power Supply** | [[KB_IOT_Arduino_Master]] | Common Ground (GND chung) |
| **Rain Logic** | `NON_MCQ_IOT_Arduino_De3_Q24` | Rain -> LCD text |
| **Servo Angle** | [[KB_IOT_Arduino_Master]] | 0-180 độ |
| **DHT11 Logic** | `IOT_MCQ_Arduino_De2_Q07` | Temp > 27 logic |
| **Baudrate** | [[WIKI_IOT_Arduino_Logic]] | 9600 cho Serial |
| **Breadboard** | `IOT_MCQ_Arduino_De1_Q01` | Hàng ngang khu A/D (25 lỗ) |

---

## 4F — Phản tư sư phạm
| | Nội dung |
|---|---|
| **Facts** | Tri thức nâng cao tập trung vào tham số (threshold) và đấu nối chân (pinout). |
| **Feelings** | Học sinh dễ nhầm lẫn giữa chân A4/A5 của I2C và các chân Analog khác. |
| **Findings** | Logic điều khiển phức hợp (nhiều cảm biến) đòi hỏi việc xóa màn hình LCD và quản lý biến số tốt. |
| **Futures** | Áp dụng cho các dự án Smart Home quy mô lớn và Xe robot tự hành. |

---
- [x] Chỉ có 1 khái niệm duy nhất trong file này
- [x] Có ít nhất 2 [[wikilinks]]
- [x] Phần Futures không để trống
- [x] Nguồn có thể trace về brain/raw/
- [x] **[Rule 14]** Đã xác nhận fact từ 120 câu hỏi và ghi rõ vào Bảng tra cứu nguồn.

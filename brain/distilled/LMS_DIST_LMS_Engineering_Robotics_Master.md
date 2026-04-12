---
file_id: LMS_Engineering_Robotics_Master
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Engineering Robotics Master

# 📚 Tài Liệu Học Tập - Hệ Thống Nhúng & Robot (LOM v4.4 Supreme)

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, học viên sẽ có thể:

| Mục Tiêu | Mức Độ | Mô Tả |
|----------|--------|-------|
| **Hiểu kiến trúc robot** | Nhận biết | Xác định các thành phần chính trong hệ thống Mars Rover |
| **Thiết kế điều khiển PID** | Hiểu | Giải thích vai trò của P, I, D trong điều khiển robot |
| **Lắp ráp hệ thống IoT** | Ứng dụng | Kết nối ESP8266 với cảm biến và điều khiển từ xa |
| **Tối ưu in 3D** | Phân tích | Áp dụng kỹ thuật bù trừ dung sai cho sản phẩm lắp khít |

---

## 📖 Nội Dung Bài Học

### 1. 🤖 Kiến Trúc Hệ Thống Nhúng & Robot

#### 1.1. Hệ Thống Mars Rover

**Cấu trúc cơ bản:**
- **Cơ cấu servo**: Điều khiển bánh xe và cảm biến di chuyển
- **Cảm biến siêu âm**: Phát hiện chướng ngại vật
- **Cảm biến PIR**: Phát hiện chuyển động
- **Module điều khiển**: Arduino UNO hoặc ESP8266

**Sơ đồ kết nối tiêu chuẩn:**
```
Arduino UNO → Servo Motor (D9, D10)
            → Cảm biến siêu âm (Trig: D7, Echo: D8)
            → Module Bluetooth HC-06 (RX: D2, TX: D3)
```

![Sơ đồ kết nối Mars Rover](../../brain/raw/lms_multi_media_dump/assets/Engineering_Robotics_Handbook_image1.png)

> **Lưu ý**: Luôn sử dụng cầu chì bảo vệ cho động cơ servo để tránh cháy board [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### 1.2. Thuật Toán Điều Khiển PID

**PID Controller** là thuật toán điều khiển phản hồi giúp robot bám đường mượt mà:

| Thành Phần | Chức Năng | Công Dụng |
|------------|-----------|-----------|
| **P (Proportional)** | Phản ứng tức thời | Giảm sai số hiện tại |
| **I (Integral)** | Bù sai số tích lũy | Ngăn robot lệch khỏi đường |
| **D (Derivative)** | Dự đoán sai số | Giảm rung lắc và dao động |

**Ví dụ mã giả:**
```python
error = setpoint - current_value
p_term = kp * error
i_term += ki * error * dt
d_term = kd * (error - last_error) / dt
output = p_term + i_term + d_term
last_error = error
```

> **Nguyên tắc**: Tăng Kp để phản ứng nhanh, tăng Ki để triệt tiêu sai số, tăng Kd để ổn định [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### 2. 🖨️ Thiết Kế & In 3D

#### 2.1. Kỹ Thuật Bù Trừ Dung Sai

**Công thức tính toán:**

| Loại Kích Thước | Công Thức | Ghi Chú |
|-----------------|-----------|---------|
| **OD (Outside Diameter)** | `CAD_OD = Thực_tế + 2 × Horizontal_Expansion` | Tăng kích thước ngoài |
| **ID (Inside Diameter)** | `CAD_ID = Thực_tế - 2 × Horizontal_Expansion` | Giảm kích thước lỗ |

**Ví dụ thực tế:**
- Trục φ10mm cần lắp khít → `D_CAD = 10.50mm` (với expansion +0.25mm)
- Lỗ φ10mm → `D_CAD = 9.50mm` (với expansion -0.25mm)

#### 2.2. Cài Đặt Cura cho Neptune 4

**Thông số khuyến nghị cho PLA:**
- **Nhiệt độ đầu in**: 200°C
- **Nhiệt độ bàn in**: 60°C
- **Tốc độ in**: 50mm/s
- **Infill**: 20%
- **Wall thickness**: 1.2mm

> **Lưu ý bảo trì**: Sấy mực ở 60°C trong 4-6 giờ trước khi in để loại bỏ ẩm [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### 3. 🛡️ IoT & Bảo Mật Mạng

#### 3.1. Kết Nối ESP8266

**Các module phổ biến:**
- **DHT11**: Cảm biến nhiệt độ và độ ẩm
- **HC-06**: Module Bluetooth điều khiển từ xa
- **Blynk**: Giao diện điều khiển qua WiFi

**Xử lý lỗi COM Port:**
```
Lỗi: "Port COM5 is busy"
→ Giải pháp: 
  1. Đóng Arduino IDE
  2. Ngắt kết nối USB
  3. Khởi động lại máy tính
  4. Kiểm tra Device Manager
```

#### 3.2. An Toàn IoT

**Biện pháp bảo mật cơ bản:**
- Không sử dụng mật khẩu mặc định
- Cập nhật firmware thường xuyên
- Giới hạn quyền truy cập mạng
- Mã hóa dữ liệu truyền nhận

> **Cảnh báo**: ESP8266 dễ bị tấn công brute force nếu không có biện pháp bảo vệ [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📋 Worksheet Thực Hành

### Bài 1: Lắp Ráp Mars Rover Cơ Bản

**Mục tiêu:** Xây dựng robot bám đường đơn giản

**Vật liệu cần có:**
- 1 x Arduino UNO
- 2 x Servo SG90
- 1 x Cảm biến siêu âm HC-SR04
- 1 x Breadboard
- Dây nối, pin 9V

**Công việc:**
1. Vẽ sơ đồ mạch điện
2. Lắp ráp cơ cấu servo
3. Nạp code điều khiển PID cơ bản
4. Kiểm thử phát hiện chướng ngại vật

### Bài 2: Thiết Kế Chi Tiết In 3D

**Yêu cầu:** Thiết kế khớp nối có dung sai phù hợp

**Nhiệm vụ:**
1. Tính toán kích thước CAD theo công thức bù trừ
2. Mô phỏng lắp ghép trong Fusion 360
3. Xuất file STL và kiểm tra trên Cura
4. In thử nghiệm và đo sai số thực tế

---

## 🧠 Quiz Kiểm Tra

### Câu 1: Thành phần nào trong PID giúp triệt tiêu sai số tích lũy?
A) P (Proportional)  
B) I (Integral) ✅  
C) D (Derivative)  
D) Tất cả các thành phần  

### Câu 2: Khi muốn tăng độ chính xác cho lỗ φ10mm, bạn nên:
A) Giữ nguyên φ10mm  
B) Tăng lên φ10.25mm  
C) Giảm xuống φ9.75mm ✅  
D) Không cần điều chỉnh  

### Câu 3: Mục đích của Horizontal Expansion trong in 3D là gì?
A) Tăng tốc độ in  
B) Bù trừ sai số vật lý ✅  
C) Giảm lượng mực tiêu thụ  
D) Tăng độ bền sản phẩm  

### Câu 4: Lỗi "Port COM5 is busy" thường xảy ra khi:
A) Board bị hỏng  
B) Có nhiều chương trình truy cập cổng ✅  
C) Thiếu driver  
D) Pin yếu  

---

## 🎭 Scenario Ứng Dụng

### Tình Huống: Cuộc Thi Robot Bám Đường

**Bối cảnh:** Đội của bạn đang chuẩn bị cho cuộc thi Mars Rover với yêu cầu robot phải đi theo đường kẻ đen, vượt chướng ngại vật và dừng đúng trạm.

**Vấn đề gặp phải:**
- Robot bị rung lắc khi bám đường
- Cảm biến siêu âm không phản ứng kịp
- Kết nối Bluetooth bị ngắt quãng

**Yêu cầu:**
1. Điều chỉnh thông số PID để robot chạy mượt hơn
2. Tối ưu thuật toán phát hiện chướng ngại vật
3. Cải thiện độ ổn định kết nối IoT

**Giải pháp gợi ý:**
- Tăng hệ số D để giảm rung lắc
- Sử dụng State Machine để quản lý các trạng thái: `FOLLOW_LINE`, `OBSTACLE_DETECTED`, `STATION_STOP`
- Thêm cơ chế retry cho kết nối Bluetooth

> **Gợi ý nâng cao:** Áp dụng kỹ thuật decompiler từ MicroPython sang Blockly để học sinh dễ tiếp cận lập trình robot [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📚 Tài Liệu Tham Khảo

- [[LMS_Tests_Robotics_Mars-Rover]]
- [[LMS_Tests_Tu-dong-hoa-va-IOT-YoloBit]]
- [[LMS_Tests_Thiet-ke-va-in-3D]]
- [[CONV_Optimized_Part_1]]

---

*© 2024 - Content Engineering Team - LOM v4.4 Supreme Standard*  
*📖 Nguồn xác thực: [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)*
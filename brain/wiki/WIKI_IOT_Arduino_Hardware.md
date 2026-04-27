---
file_id: "WIKI_IOT_Arduino_Hardware"
title: "Từ điển Thiết bị IOT Arduino"
category: "Hardware Wiki"
prefix: "WIKI"
tags: ['Hardware', 'Arduino', 'Sensors', 'Actuators', 'Wiring']
source: "[[120_Cau_Hoi_IOT_Arduino_LMS]]"
status: "verified"
created: "2026-04-24"
last_updated: "2026-04-25"
---


# 🔌 Từ điển Thiết bị IOT Arduino

Wiki này tập trung vào phần cứng, cách nhận diện linh kiện và quy tắc đấu nối vật lý chi tiết cho hệ thống IOT Arduino Uno R3.

---

## 1. Board mạch và Kết nối nền tảng

### 1.1. Arduino Uno R3
- **Nhận diện:** Board mạch màu xanh, có chip xử lý trung tâm.
- **Quy tắc nguồn:**
    - Nạp code/Cấp nguồn nhẹ: Cổng USB Type B.
    - Cấp nguồn nặng (Xe robot): Jack DC (7-12V).
    - **Cấm:** Không cấp nguồn vào chân 5V hoặc 3.3V (đây là chân Output).
- **Quy tắc chân cắm:** Hạn chế dùng chân 0 (RX) và 1 (TX) để tránh lỗi giao tiếp.

### 1.2. Breadboard (Mạch thử nghiệm)
- **Quy tắc vật lý:** 
    - Hai hàng dọc ngoài cùng (Rails): Nối thông theo **Hàng ngang** (dùng cho Nguồn/GND).
    - Các hàng ở giữa (Terminal): Nối thông theo **Cột dọc** (5 lỗ).
    - **Cấu tạo chi tiết:** Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau. (Nguồn: `IOT_MCQ_Arduino_De1_Q01`)
- **Lưu ý:** Không cắm 2 chân của 1 linh kiện vào cùng 1 cột dọc (gây ngắn mạch).


### 1.3. Quy ước dây cắm (Jumper Wires)
- **Màu Đỏ:** Dương nguồn (+).
- **Màu Đen/Nâu:** Âm nguồn (GND/-).
- **Màu khác:** Tín hiệu (S).

---

## 2. Thiết bị Đầu ra (Output Devices)

### 2.1. Đèn LED đơn (2 chân)
- **Quy tắc vật lý:** Chân dài là cực Dương (+), chân ngắn là cực Âm (-).
- **Quy tắc đấu nối:** 
    - Chân ngắn (-) ➔ GND.
    - Chân dài (+) ➔ Điện trở 220Ω ➔ Chân Digital (D2-D13).

### 2.2. Đèn LED RGB (4 chân)
- **Quy tắc vật lý:** Gồm 4 chân. Chân dài nhất là chân Chung (thường là cực Âm - Cathode). 3 chân còn lại tương ứng R (Red), G (Green), B (Blue).
- **Quy tắc đấu nối:**
    - Chân Chung ➔ GND.
    - Chân R, G, B ➔ 3 Điện trở ➔ 3 chân Digital (Ưu tiên chân có dấu ~ để chỉnh màu mịn).

### 2.3. Động cơ Servo (MG90S)
- **Quy tắc vật lý:** Thiết bị đầu ra (actuator) quay 0-180 độ. Có 3 dây màu quy ước.
- **Quy tắc đấu nối:** 
    - **Nâu (hoặc Đen):** GND (-)
    - **Đỏ:** 5V (+)
    - **Cam (hoặc Vàng):** Tín hiệu (S) ➔ Nối vào chân Digital hỗ trợ PWM (có dấu ~) như 3, 5, 6, 9, 10, 11.


### 2.4. Động cơ DC & Mạch L298 (Xe Robot)
- **Quy tắc vật lý:** Động cơ DC (vàng) có 2 cực. Mạch L298 có các cọc đấu dây (Terminal).
- **Quy tắc đấu nối:** 
    - Động cơ ➔ Cọc OUT1/OUT2 trên L298.
    - L298 ➔ Nối nguồn riêng (Pin 9V) vào cọc 12V và GND.
    - **Lưu ý:** GND của L298 phải nối chung với GND của Arduino. **Tuyệt đối không** nối trực tiếp động cơ vào chân Arduino.

### 2.5. Còi báo (Buzzer)
- **Quy tắc vật lý:** Thiết bị Output phát âm thanh, hoạt động ở 3V–5V. Thường có ký hiệu (+) trên bề mặt.
- **Quy tắc chân cắm:** Chân dài là cực dương (+), chân ngắn là cực âm (-).
- **Quy tắc đấu nối:** Chân ngắn (-) ➔ GND | Chân dài (+) ➔ Digital Pin (D2-D13).


### 2.6. Màn hình LCD I2C
- **Quy tắc vật lý:** Mặt sau có module I2C 4 chân kim.
- **Quy tắc đấu nối:** GND ➔ GND | VCC ➔ 5V | SDA ➔ chân A4 | SCL ➔ chân A5.

---

## 3. Thiết bị Đầu vào & Cảm biến (Input & Sensors)

### 3.1. Nút nhấn (Push Button)
- **Quy tắc vật lý:** Linh kiện 4 chân (thực chất là 2 cặp thông nhau).
- **Quy tắc đấu nối:** Cắm chéo 2 chân vào 2 cột khác nhau trên Breadboard. Một chân nối GND, chân kia nối Digital Pin (Sử dụng chế độ `INPUT_PULLUP`).

### 3.2. Joystick (Cần điều khiển)
- **Quy tắc vật lý:** Gồm 5 chân cắm (GND, VCC, VRx, VRy, SW).
- **Quy tắc đấu nối:** 
    - VRx ➔ Analog (A0) | VRy ➔ Analog (A1).
    - SW ➔ Digital Pin.
    - VCC/GND ➔ 5V/GND.

### 3.3. Cảm biến Khoảng cách (Siêu âm SR04)
- **Quy tắc vật lý:** Gồm 4 chân (VCC, Trig, Echo, GND).
- **Quy tắc đấu nối:** 
    - Trig (Phát) ➔ Digital Pin.
    - Echo (Thu) ➔ Digital Pin.
    - VCC/GND ➔ 5V/GND.

### 3.4. Cảm biến Nhiệt độ & Độ ẩm (DHT11)
- **Quy tắc vật lý:** Có 3 chân (VCC, Data, GND) hoặc 4 chân.
- **Quy tắc đấu nối:** Data ➔ Digital Pin | VCC/GND ➔ 5V/GND.

### 3.5. Nhóm Cảm biến Analog chuẩn (Lửa, Gas, Ánh sáng, Mưa)
- **Quy tắc vật lý:** Thường có 3 hoặc 4 chân cắm.
- **Quy tắc đấu nối (Chuẩn G-V-S):**
    - **G (GND)** ➔ GND.
    - **V (VCC)** ➔ 5V.
    - **S (Signal)** ➔ Chân Analog (A0-A5).
- **Lưu ý:** Xoay biến trở xanh để điều chỉnh độ nhạy.

---

## 4. Thiết bị hỗ trợ AI (PC-side)

Dữ liệu AI phức tạp thường được xử lý trên máy tính (chế độ Live Mode) trước khi gửi lệnh thực thi xuống Arduino:
- **Camera (Webcam)**: Thu thập hình ảnh cho Thị giác máy tính (Nhận diện khuôn mặt, vật thể). (Nguồn: Đề AI 1 - Câu 10).
- **Microphone**: Thu thập âm thanh cho Nhận diện giọng nói.
- **Yêu cầu Internet**: Bắt buộc có kết nối mạng để sử dụng các dịch vụ Cloud (Cognitive Services). (Nguồn: Đề AI 1 - Câu 5).

### 4.1. Quy tắc "Bất di bất dịch" (Physical Golden Rules)
- **GND Hợp nhất (Common Ground)**: BẮT BUỘC nối chung cực âm (GND) của Arduino với nguồn nuôi cảm biến/Relay bên ngoài.
- **Chống nhiễu**: Không đặt Camera quá gần các thiết bị phát sóng mạnh hoặc động cơ công suất lớn để tránh làm nhiễu tín hiệu AI.

---

## 📖 Nguồn tham khảo (Traceability)
- [Rule 14] Đã xác nhận fact từ 120 câu hỏi LMS và 238 câu hỏi AI Arduino.
- **Trích dẫn:** `MCQ_Arduino_De2_Q01`, `MCQ_Arduino_De4_Q04`, `MCQ_IOT_AI_De1_Q10`, `MCQ_IOT_AI_De1_Q05`.

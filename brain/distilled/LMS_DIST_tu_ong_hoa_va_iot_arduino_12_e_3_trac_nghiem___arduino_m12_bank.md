---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_3_trac_nghiem___arduino_m12_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 e 3 trac nghiem   arduino m12 bank

---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_3_trac_nghiệm___arduino_m12_bank
title: TEST BANK: Tự_động_hóa_và_IOT_Arduino_1+2_Đề_3_Trắc_nghiệm_-_Arduino_M1,2
category: Assessment
prefix: LMS
source: MASTER_SOURCE_INDEX.md
status: standardized
---

# Ngân Hàng Câu Hỏi Trắc Nghiệm: Tự Động Hóa & IoT Arduino Mô-đun 1&2

## Tổng Quan Bài Kiểm Tra

| Thuộc tính | Giá trị |
|------------|---------|
| Môn học | Tự Động Hóa & IoT Arduino |
| Mô-đun | 1 & 2 |
| Loại bài kiểm tra | Trắc nghiệm khách quan |
| Số lượng câu hỏi | 9 câu (cập nhật đến câu 9) |
| Định dạng | Multiple Choice (nhiều lựa chọn) |

---

## Câu Hỏi & Đáp Án Chi Tiết

### Câu 1: Những cách cấp nguồn cho Arduino Uno R3? (Chọn nhiều đáp án)

**Câu hỏi:**  
Những cách nào sau đây có thể sử dụng để cấp nguồn cho Arduino Uno R3?

**Lựa chọn:**
- A. Cấp nguồn từ cổng USB
- B. Cấp nguồn thông qua Adapter
- C. Cấp nguồn từ pin thông qua chân V(in)
- D. Cấp nguồn từ pin thông qua chân Digital
- E. Cấp nguồn từ pin thông qua chân Analog
- F. Cấp nguồn không dây qua tín hiệu bluetooth

**Đáp án đúng:** A, B, C

**Giải thích:**  
Arduino hỗ trợ cấp nguồn qua cổng USB (5V), Jack DC (7-12V) và chân Vin (7-12V). Các chân Digital/Analog không có chức năng nhận nguồn nuôi mạch. Bluetooth không hỗ trợ cấp nguồn vật lý [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 2: Phát biểu nào sau đây là sai khi nói về đèn LED đơn?

**Câu hỏi:**  
Phát biểu nào sau đây là **sai** khi nói về đèn LED đơn?

**Lựa chọn:**
- A. Phần bản to hơn là cực dương, phần bản nhỏ là cực âm
- B. Đèn LED là thiết bị output
- C. Cực âm của đèn LED được cắm vào chân GND của Arduino
- D. Cực dương của đèn LED được cắm vào chân D2-D13 của Arduino

**Đáp án đúng:** A

**Giải thích:**  
Trong cấu tạo nội tại của LED, phần bản kim loại to hơn là cực âm (Cathode), phần bản nhỏ hơn là cực dương (Anode). Câu A đảo ngược thông tin này [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 3: Phát biểu về còi buzzer nào sau đây là SAI?

**Câu hỏi:**  
Phát biểu nào sau đây là **sai** khi nói về còi buzzer?

**Lựa chọn:**
- A. Còi buzzer có 2 chân kết nối. Chân dài là chân âm; chân ngắn là chân dương
- B. Còi buzzer là một thiết bị có thể phát ra âm thanh
- C. Còi buzzer có khả năng tiếp nhận điện năng và chuyển chúng thành tín hiệu âm thanh
- D. Chân dương của còi buzzer được nối với chân digital từ 2 đến 13 trên Arduino, chân âm được nối với GND

**Đáp án đúng:** A

**Giải thích:**  
Quy ước linh kiện điện tử: chân dài luôn là cực dương (+), chân ngắn là cực âm (-). Câu A đảo ngược thông tin này [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 4: Dây màu cam của servo cắm với chân nào của Arduino?

**Câu hỏi:**  
Dây màu cam của servo được cắm với chân nào của Arduino?

**Lựa chọn:**
- A. D2-D13
- B. 5V
- C. GND
- D. VIN

**Đáp án đúng:** A

**Giải thích:**  
Dây màu cam là dây tín hiệu (Signal), cần kết nối với các chân Digital (đặc biệt là các chân PWM) để điều khiển góc quay [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 5: Trong breadboard, những hàng cột nào được nối với nhau?

**Câu hỏi:**  
Trong breadboard, cấu trúc nối điện như thế nào?

**Lựa chọn:**
- A. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau
- B. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực A/B/C/D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau
- C. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau
- D. Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện với nhau

**Đáp án đúng:** A

**Giải thích:**  
Đây là cấu tạo chuẩn của breadboard: hàng ngang ngoài cùng cho nguồn và hàng dọc ở giữa cho linh kiện [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 6: Để kết nối các chân của Arduino với các chân của cảm biến hồng ngoại ta sử dụng dây jumper loại nào?

**Câu hỏi:**  
Để kết nối các chân của Arduino với các chân của cảm biến hồng ngoại, ta sử dụng dây jumper loại nào?

**Lựa chọn:**
- A. Dây âm (-), âm (-)
- B. Dây dương (+), dương (+)
- C. Dây âm (-), dương (+)
- D. Nối trực tiếp chân của cảm biến với Arduino mà không cần dây điện trung gian

**Đáp án đúng:** A

**Giải thích:**  
(Lưu ý: Trong ngữ cảnh đề bài này, "âm" tương ứng với đầu Cái/Female, "dương" tương ứng với đầu Đực/Male). Cảm biến hồng ngoại thường có chân đực, Arduino có lỗ cái, nên dùng dây Cái-Cái (Female-Female) nếu cắm trực tiếp [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 7: Cách điều chỉnh độ nhạy của các loại cảm biến là:

**Câu hỏi:**  
Cách điều chỉnh độ nhạy của các loại cảm biến là:

**Lựa chọn:**
- A. Dùng tua vít điều chỉnh biến trở (núm vặn màu xanh) trên cảm biến
- B. Dùng băng keo dán lên mặt tấm cảm biến
- C. Nối chân VCC của cảm biến với chân 3,3V để giảm điện áp của cảm biến
- D. Nối chân GND của cảm biến với chân 3,3V để giảm mức chênh lệch điện áp so với chân VCC

**Đáp án đúng:** A

**Giải thích:**  
Biến trở tối ưu trên module cảm biến dùng để thay đổi ngưỡng so sánh điện áp, từ đó thay đổi độ nhạy [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 8: Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?

**Câu hỏi:**  
Màn hình LCD I2C có mấy chân kết nối và tên gọi của chúng là gì?

**Lựa chọn:**
- A. 4 chân (VCC, GND, SCL, SDA)
- B. 4 chân (VCC, GND, LCD, SDA)
- C. 4 chân (VCC, GND, LCD, DSA)
- D. 4 chân (VCC, GND, SCL, DSA)

**Đáp án đúng:** A

**Giải thích:**  
Giao tiếp I2C chuẩn gồm 2 dây nguồn (VCC, GND) và 2 dây tín hiệu (SCL - Clock, SDA - Data) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 9: Khi núm điều khiển trên Joystick được gạt lên

**Câu hỏi:**  
(Đang chờ hoàn thiện nội dung câu hỏi số 9)

**Trạng thái:** Đang cập nhật...

---

## Hướng Dẫn Sử Dụng Ngân Hàng Câu Hỏi

### Đối Tượng Sử Dụng:
- Giảng viên dạy môn Tự Động Hóa & IoT Arduino
- Học viên đang học mô-đun 1&2
- Người làm nội dung đánh giá kỹ năng thực hành Arduino

### Cách Tạo Đề Thi:
1. Chọn ngẫu nhiên 10-15 câu từ ngân hàng này
2. Kết hợp với câu hỏi thực hành thực tế
3. Thời gian khuyến nghị: 45-60 phút
4. Hình thức: Trắc nghiệm online hoặc giấy

### Mức Độ Khó:
- Câu 1-3: Cơ bản (Nhận biết)
- Câu 4-6: Trung bình (Hiểu)
- Câu 7-8: Nâng cao (Vận dụng)

---

## Tài Nguyên Liên Kết

![Sơ đồ kết nối Arduino](../../brain/raw/lms_multi_media_dump/assets/TEST_BANK_image1.png)
*Hình minh họa: Sơ đồ kết nối cơ bản Arduino với các linh kiện*

> **Lưu ý:** Tài liệu này là một phần của hệ thống học tập tích hợp LOM v4.4 Supreme. Mọi nội dung đều đã được chuẩn hóa theo tiêu chuẩn giáo dục kỹ thuật số [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
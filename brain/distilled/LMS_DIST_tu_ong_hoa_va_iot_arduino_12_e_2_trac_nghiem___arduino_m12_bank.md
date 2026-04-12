---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_2_trac_nghiem___arduino_m12_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 e 2 trac nghiem   arduino m12 bank

```yaml
---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_e_2_trac_nghiem___arduino_m12_bank
title: "Kiểm Tra Trắc Nghiệm: Arduino Cơ Bản - Module 1 & 2"
category: Assessment
prefix: LMS
source: MASTER_SOURCE_INDEX.md
status: standardized
version: LOM v4.4 Supreme
learning_objectives:
  - Nhận diện các thành phần cơ bản của bo mạch Arduino Uno
  - Xác định chân cực của linh kiện điện tử (LED, Buzzer, Servo)
  - Hiểu nguyên lý hoạt động của cảm biến hồng ngoại và cảm biến mưa
  - Kết nối đúng cách các module hiển thị và breadboard
prerequisites:
  - Kiến thức cơ bản về điện tử
  - Hiểu biết về mạch điện đơn giản
duration: 45 phút
format: Multiple Choice Questions
---
```

# Kiểm Tra Trắc Nghiệm: Arduino Cơ Bản - Module 1 & 2

> **Mục tiêu học tập**: Đánh giá mức độ hiểu biết về các thành phần cơ bản trong hệ thống Arduino, cách nhận diện linh kiện, kết nối mạch và nguyên lý hoạt động của cảm biến.

---

## Câu 1: Nhận diện cổng kết nối Arduino

**Câu hỏi**: Bộ phận nào dùng để gắn dây kết nối với máy tính?

![Cổng kết nối Arduino Uno](../../brain/raw/lms_multi_media_dump/assets/Tu_dong_hoa_va_IOT_Arduino_1+2_De_2_Trac_nghiem_-_Arduino_M1,2_image29.png)

| Phương án | Nội dung |
|----------|----------|
| A | D |
| B | B |
| C | C |
| D | A |

**Đáp án đúng**: D  
**Giải thích**: Vị trí A trên mạch Arduino Uno là cổng USB Type-B, dùng để kết nối với máy tính [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 2: Xác định cực tính của LED

**Câu hỏi**: Trong trường hợp chân đèn led bị gãy làm không biết được chân âm - dương qua độ dài của chân đèn thì ta còn có thể dựa vào đặc điểm nào dưới đây? (Chọn nhiều đáp án đúng)

| Phương án | Nội dung |
|----------|----------|
| A | Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân dương, phần (bản) cực to hơn là chân âm |
| B | Nhìn vào phần (bản) cực bên trong đèn nhỏ hơn là chân âm, phần (bản) cực to hơn là chân dương |
| C | Không thể xác định được chân dương hay chân âm nếu đèn Led bị gãy chân |
| D | Nối 2 chân gãy vào 2 dây điện đen, đỏ của đế pin 2. Nếu đèn sáng lên thì chân đèn LED nối với dây điện đen là cực âm, chân còn lại là cực dương |
| E | Nối 2 chân gãy vào 2 dây điện đen, đỏ của đế pin 2. Nếu đèn sáng lên thì chân đèn LED nối với dây điện đen là cực dương, chân còn lại là cực âm |

**Đáp án đúng**: A, D  
**Giải thích**: Bản cực nhỏ bên trong LED là cực dương. Khi thử với pin, dây đen là cực âm, nếu LED sáng thì chân nối với dây đen chính là cực âm của LED [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 3: Kết nối còi Buzzer

**Câu hỏi**: Phát biểu nào sau đây là đúng khi nói về còi Buzzer?

| Phương án | Nội dung |
|----------|----------|
| A | Chân ngắn của còi buzzer gắn với chân GND của arduino |
| B | Chân dài của còi buzzer gắn với chân GND của arduino |
| C | Chân ngắn của còi buzzer gắn với cực dương của pin |
| D | Chân dài của còi buzzer gắn với cực âm của pin |

**Đáp án đúng**: A  
**Giải thích**: Còi Buzzer có cực tính, chân ngắn là cực âm nên phải nối với GND [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 4: Đặc điểm động cơ Servo

**Câu hỏi**: Chọn phát biểu đúng khi nói về động cơ Servo?

| Phương án | Nội dung |
|----------|----------|
| A | Động cơ Servo MG90S có thể xoay từ 0 đến 180 độ và ngược lại |
| B | Động cơ Servo có cấu tạo hoàn toàn giống động cơ DC bình thường, chỉ khác là được tích hợp thêm 1 chân tín hiệu để lập trình thay đổi góc |
| C | Động cơ Servo chỉ có thể xoay góc từ 0 đến 180 độ |
| D | Chân tín hiệu của động cơ Servo được nối với chân tín hiệu analog của Arduino |

**Đáp án đúng**: A  
**Giải thích**: Servo MG90S là loại servo phổ biến trong học tập, có giới hạn góc quay từ 0-180 độ [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 5: Cấu trúc Breadboard

**Câu hỏi**: Trong breadboard, các dây điện được nối với nhau như thế nào?

| Phương án | Nội dung |
|----------|----------|
| A | Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng ngang được cách điện với hàng còn lại. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột dọc được cách điện với các cột còn lại |
| B | Khu vực A và D các lỗ được nối theo cột dọc, mỗi cột được cách điện với cột còn lại. Khu vực B và C các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với các hàng còn lại |
| C | Khu vực A và D các lỗ được nối theo hàng ngang và theo từng cặp, 5 cặp theo hàng là cách điện nhau. Khu vực B và C các lỗ được nối theo cột, mỗi cột được cách điện với các cột còn lại |
| D | Khu vực A và D các lỗ được nối theo hàng ngang, mỗi hàng được cách điện với hàng còn lại và bắt buộc phải nối thiết bị theo cực (+) và cực (-) đã ký hiệu. Khu vực B và C các lỗ được nối theo cột dọc, mỗi cột được cách điện với các cột còn lại |

**Đáp án đúng**: A  
**Giải thích**: Theo quy ước thông thường trên breadboard, hai dải biên (A, D) nối thông hàng ngang (thường dùng làm đường nguồn), khu vực giữa (B, C) nối thông theo cột dọc [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 6: Nguyên lý cảm biến hồng ngoại

**Câu hỏi**: Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc nào?

| Phương án | Nội dung |
|----------|----------|
| A | Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng hồng ngoại |
| B | Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc thu và phát ánh sáng màu hồng |
| C | Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện nhiệt độ của vật cản |
| D | Cảm biến hồng ngoại hoạt động dựa trên nguyên tắc phát hiện ánh sáng màu đỏ do vật cản phát ra |

**Đáp án đúng**: A  
**Giải thích**: Cảm biến hồng ngoại (IR) sử dụng một LED phát tia hồng ngoại và một mắt thu hồng ngoại để phát hiện vật cản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 7: Điện áp hoạt động cảm biến mưa

**Câu hỏi**: Để cảm biến mưa có thể hoạt động được thì cần phải cung cấp lượng điện áp bao nhiêu?

| Phương án | Nội dung |
|----------|----------|
| A | 5V |
| B | 3V |
| C | 3,3V |
| D | 1,5V |

**Đáp án đúng**: A  
**Giải thích**: Đa số các module cảm biến cho Arduino được thiết kế để hoạt động với điện áp chuẩn 5V [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu 8: Kết nối màn hình LCD

**Câu hỏi**: Đáp án nào sau đây là đúng khi nói về cách kết nối màn hình LCD với Arduino?

![Kết nối LCD với Arduino](../../brain/raw/lms_multi_media_dump/assets/Tu_dong_hoa_va_IOT_Arduino_1+2_De_2_Trac_nghiem_-_Arduino_M1,2_image62.png)

| Phương án | Nội dung |
|----------|----------|
| A | Hình A |
| B | Hình B |
| C | Hình C |
| D | Hình D |

**Đáp án đúng**: A  
**Giải thích**: Màn hình LCD sử dụng module I2C cần kết nối đúng 4 chân: nguồn (VCC, GND) và tín hiệu (SDA, SCL) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng điểm và phân tích

| Câu | Chủ đề | Mức độ | Số điểm |
|-----|--------|--------|---------|
| 1 | Nhận diện linh kiện | Cơ bản | 1 |
| 2 | Xác định cực tính | Trung bình | 2 |
| 3 | Kết nối thiết bị | Cơ bản | 1 |
| 4 | Hiểu biết về servo | Trung bình | 1 |
| 5 | Cấu trúc breadboard | Cơ bản | 1 |
| 6 | Nguyên lý cảm biến | Trung bình | 1 |
| 7 | Thông số kỹ thuật | Cơ bản | 1 |
| 8 | Kết nối module | Trung bình | 2 |

**Tổng điểm**: 10  
**Thời gian làm bài**: 45 phút  
**Điểm đạt yêu cầu**: 6/10

---

> **Ghi chú giảng viên**: Bài kiểm tra này đánh giá kiến thức nền tảng về Arduino, phù hợp cho sinh viên mới bắt đầu. Các câu hỏi trắc nghiệm giúp kiểm tra nhanh khả năng nhận diện và hiểu nguyên lý hoạt động của các thành phần cơ bản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
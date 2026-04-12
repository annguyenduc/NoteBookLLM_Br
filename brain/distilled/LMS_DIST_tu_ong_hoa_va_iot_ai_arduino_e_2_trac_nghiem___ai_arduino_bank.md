---
file_id: LMS_Tests_tu_ong_hoa_va_iot_ai_arduino_e_2_trac_nghiem___ai_arduino_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot ai arduino e 2 trac nghiem   ai arduino bank

# Tài liệu Học tập LOM v4.4 Supreme
## TEST BANK: Tự động hóa và IoT AI Arduino - Đề 2 Trắc nghiệm

| **Thông tin tài liệu** | **Chi tiết** |
|------------------------|--------------|
| **ID Tài liệu** | LMS_Tests_tu_ong_hoa_va_iot_ai_arduino_e_2_trac_nghiem___ai_arduino_bank |
| **Loại tài liệu** | Assessment |
| **Chuyên mục** | Tự động hóa & IoT AI Arduino |
| **Trạng thái** | Đã chuẩn hóa |

---

## Mục tiêu học tập

Sau khi hoàn thành bài kiểm tra này, học viên sẽ có khả năng:

- Hiểu rõ cấu trúc và cách cấp nguồn cho mạch Arduino Uno
- Phân biệt được các chế độ lập trình Live và Upload trong mBlock5
- Xác định đúng cách nhận biết cực tính của linh kiện LED
- Lựa chọn đúng khối lệnh để điều khiển thiết bị ngoại vi
- Hiểu nguyên lý hoạt động của mạch thu phát âm thanh ISD1820

---

## Câu hỏi trắc nghiệm

### Câu 1: Cấp nguồn cho Arduino

**Câu hỏi:** Khẳng định nào dưới đây là **SAI**?

A. Có thể cấp nguồn cho Arduino thông qua pin với chân 3,3V hoặc 5V.

B. Có thể cấp nguồn cho Arduino bằng cách kết nối với máy tính thông qua dây cáp.

C. Có thể cấp nguồn cho Arduino thông qua dây adapter 9V.

D. Có thể cấp nguồn cho Arduino thông qua pin với cổng Vin.

**Đáp án đúng:** A

**Giải thích:** Chân 3.3V và 5V là chân nguồn ra (output) để nuôi linh kiện, không phải chân cấp nguồn vào (input) cho mạch Arduino [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 2: Nhận diện các bộ phận Arduino Uno

**Câu hỏi:** Nối tên với các bộ phận tương ứng trên mạch Arduino Uno:

A. Nút reset  
B. Cổng USB - type B  
C. Jack DC  
D. Các chân nguồn  
E. Các chân pin (chân tín hiệu)

**Đáp án đúng:** 
- A - Nút nhấn màu đỏ/vàng
- B - Cổng vuông kết nối máy tính
- C - Cổng tròn cấp nguồn
- D - Dãy chân Power (5V, GND, Vin)
- E - Dãy chân Digital/Analog

**Giải thích:** Đây là các thành phần cơ bản của mạch Arduino Uno giúp người học nhận diện và hiểu chức năng từng bộ phận [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 3: Chế độ lập trình Arduino

**Câu hỏi:** Phát biểu nào sau đây là **đúng** khi nói về chế độ Live và chế độ Upload khi lập trình Arduino trên mBlock5?

A. Chế độ Live chỉ hoạt động trong quá trình mở mBlock5 và kết nối với board Arduino.

B. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta ngắt kết nối giữa hai thiết bị, chương trình được tải lên sẽ bị xóa khỏi bộ nhớ của Arduino.

C. Sau khi tải chương trình từ máy tính sang Arduino bằng chế độ Upload, nếu ta xóa câu lệnh ở khu vực lập trình, chương trình hoạt động của Arduino sẽ bị thay đổi ngay lập tức.

D. Với chế độ Live, ta có thể thấy trực tiếp chương trình đang chạy đến khối lệnh nào khi chọn "Setting - Update firmware - OK".

**Đáp án đúng:** A

**Giải thích:** Chế độ Live yêu cầu kết nối thời gian thực. Chế độ Upload lưu chương trình vĩnh viễn vào chip cho đến khi có chương trình mới đè lên [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 4: Nhận biết cực tính LED

**Câu hỏi:** Ta có thể phân biệt được chân dương, chân âm của đèn LED siêu sáng bằng cách nào?

A. Phần chân âm của đèn LED có dấu (-); chân dương của đèn LED có dấu (+).

B. Phần chân âm của đèn LED dài hơn; chân dương của đèn LED ngắn hơn.

C. Phần chân dương của đèn LED được đánh dấu bằng một lỗ tròn nhỏ, chân âm không có.

D. Phần chân dương của đèn LED dài hơn; chân âm của đèn LED ngắn hơn.

**Đáp án đúng:** D

**Giải thích:** Theo quy ước linh kiện điện tử, chân dài của LED là cực dương (Anode), chân ngắn là cực âm (Cathode) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 5: Điều khiển động cơ rung

**Câu hỏi:** Khối lệnh nào sau đây được sử dụng để điều khiển việc hoạt động/tắt của động cơ rung 0834 3-5V?

![Khối lệnh điều khiển động cơ rung](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_AI_Arduino_Đề_2_trắc_nghiệm_-_AI_Arduino_docx_image29.png)

A. Khối lệnh thiết lập chân Digital đầu ra (High/Low).

B. Khối lệnh đọc chân Analog.

C. Khối lệnh Servo.

D. Khối lệnh hiển thị màn hình.

**Đáp án đúng:** A

**Giải thích:** Động cơ rung hoạt động như một thiết bị On/Off đơn giản, sử dụng lệnh xuất mức logic High/Low tại chân Digital [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 6: Mạch thu phát âm thanh ISD1820

**Câu hỏi:** Phát biểu nào sau đây là **SAI** khi nói về các chân kết nối của mạch thu phát âm thanh ISD1820?

A. PLAYE, PLAYL của mạch chỉ có thể được bật bằng cách nhấn nút thủ công.

B. Chân PLAYE, PLAYL của mạch chỉ có thể được gắn ở một số chân Digital không có dấu ngã (~): 2, 4, 7, 8, 12, 13.

C. Chân VCC của mạch được gắn với cổng 5V của Arduino.

D. Chân REC của mạch được gắn với cổng Digital 2-13 của Arduino.

**Đáp án đúng:** A

**Giải thích:** Các chân PLAYE, PLAYL có thể được điều khiển bằng xung điện từ các chân Digital của Arduino [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Hướng dẫn sử dụng tài liệu

### Đối với giảng viên:
- Sử dụng bài kiểm tra này như một bài đánh giá giữa kỳ hoặc cuối kỳ
- Có thể tùy chỉnh số lượng câu hỏi theo nhu cầu giảng dạy
- Kết hợp với thực hành để đánh giá toàn diện kiến thức học viên

### Đối với học viên:
- Làm bài kiểm tra trong thời gian 45 phút
- Ôn tập kỹ lý thuyết trước khi làm bài
- Phân tích kỹ từng lựa chọn trước khi quyết định đáp án

---

## Ma trận đề thi

| Nội dung | Số câu | Tỷ lệ % |
|----------|--------|---------|
| Cấu trúc Arduino | 2 | 33.3% |
| Chế độ lập trình | 1 | 16.7% |
| Linh kiện điện tử | 1 | 16.7% |
| Lập trình điều khiển | 1 | 16.7% |
| Mạch âm thanh | 1 | 16.7% |
| **Tổng cộng** | **6** | **100%** |

---

## Đánh giá kết quả

| Mức độ | Điểm số | Mô tả |
|--------|---------|-------|
| Xuất sắc | 90-100% | Hiểu sâu sắc kiến thức, áp dụng linh hoạt |
| Tốt | 70-89% | Hiểu tốt kiến thức, áp dụng đúng |
| Đạt yêu cầu | 50-69% | Hiểu cơ bản, cần bổ sung kiến thức |
| Chưa đạt | <50% | Cần ôn tập lại toàn bộ kiến thức |

---

*Tài liệu được chuẩn hóa theo tiêu chuẩn LOM v4.4 Supreme*  
*Bản quyền © 2024 - Hệ thống đào tạo Tự động hóa & IoT AI Arduino* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
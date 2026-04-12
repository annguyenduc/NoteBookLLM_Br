---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_2___tieu_chi_cham_va_thang_iem___arduino_m2_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 arduino 2 e 2   tieu chi cham va thang iem   arduino m2 bank

# Tài Liệu Học Tập Chuẩn LOM v4.4 Supreme
**Mã Tài Liệu:** LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_2___tieu_chi_cham_va_thang_iem___arduino_m2_bank  
**Tên Tài Liệu:** Ngân Hàng Câu Hỏi Kiểm Tra: Tự Động Hóa và IoT Arduino - Đề Thi Arduino M2  
**Loại:** Đánh Giá  
**Trạng Thái:** Đã Chuẩn Hóa  

---

## Tổng Quan Nội Dung

Tài liệu này chứa ngân hàng câu hỏi trắc nghiệm phục vụ kiểm tra đánh giá kiến thức về thiết kế và lập trình hệ thống điều khiển xe tự hành sử dụng Arduino. Nội dung tập trung vào các kỹ năng thực hành mạch điện, lập trình điều khiển động cơ và tích hợp cảm biến.

[Liên kết nguồn gốc đầy đủ](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu Hỏi Đánh Giá

### Câu 1: Kết Nối Nguồn Điện Cho Arduino

**Câu hỏi:** Trong sơ đồ mạch điện xe tự hành, khi sử dụng nguồn điện từ đế pin để cấp cho Arduino, dây dương (màu đỏ) của đế pin nên được nối vào chân nào?

**Lựa chọn:**
- A. Chân 5V
- B. Chân 3.3V  
- C. Chân VIN
- D. Chân Analog A0

**Đáp án đúng:** C

**Phân tích chi tiết:**
Theo tiêu chí chấm điểm mạch điện, dây dương của nguồn pin phải được kết nối đến chân VIN của Arduino để sử dụng bộ ổn áp tích hợp trên board. Việc sử dụng chân VIN cho phép board Arduino tự điều chỉnh điện áp phù hợp với các thành phần bên trong.

**Mức độ nhận thức:** Hiểu - Áp dụng  
**Thời gian dự kiến:** 60 giây  
**Chủ đề:** Kết nối mạch điện cơ bản

[Chi tiết nguồn](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 2: Kết Nối Mạch Cầu H Với Arduino

**Câu hỏi:** Để điều khiển động cơ DC thông qua mạch cầu H L298, các chân IN 1, 2, 3, 4 của mạch L298 nên được ưu tiên kết nối với loại chân nào trên Arduino?

**Lựa chọn:**
- A. Các chân Analog (A0 - A5)
- B. Các chân Digital có ký hiệu dấu "~" (PWM)
- C. Các chân GND
- D. Các chân truyền nhận dữ liệu TX/RX

**Đáp án đúng:** B

**Phân tích chi tiết:**
Các chân Digital PWM (có dấu ~) cho phép điều khiển độ rộng xung, từ đó có thể điều chỉnh được tốc độ của động cơ thay vì chỉ bật/tắt đơn thuần. Điều này rất quan trọng trong việc điều khiển chính xác vận tốc và hướng quay của động cơ.

**Mức độ nhận thức:** Hiểu - Phân tích  
**Thời thời gian dự kiến:** 90 giây  
**Chủ đề:** Điều khiển động cơ bằng PWM

[Chi tiết nguồn](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 3: Hành Vi Xe Khi Phát Hiện Vật Cản

**Câu hỏi:** Theo yêu cầu của đề bài, khi cảm biến siêu âm phát hiện vật cản ở khoảng cách gần, xe cần thực hiện chuỗi hành động nào?

**Lựa chọn:**
- A. Dừng lại và bật đèn LED
- B. Tiếp tục đi thẳng và tăng tốc
- C. Di chuyển lùi lại, xoay hướng khác và sau đó tiếp tục di chuyển
- D. Xoay tròn tại chỗ liên tục

**Đáp án đúng:** C

**Phân tích chi tiết:**
Theo yêu cầu lập trình số 3 và 4, khi gặp vật cản xe phải lùi lại, xoay hướng khác (sử dụng 1 động cơ đứng yên, 1 động cơ xoay) trước khi tiếp tục hành trình. Đây là hành vi tránh vật cản thông minh trong hệ thống điều khiển tự động.

**Hình ảnh minh họa:**  
![Sơ đồ mô hình xe tự hành](../../brain/raw/lms_multi_media_dump/assets/Tu_dong_hoa_va_IOT_Arduino_1+2_Arduino_2_De_2___Tieu_chi_cham_va_thang_diem___Arduino_M2_image4.png)

**Mức độ nhận thức:** Áp dụng - Phân tích  
**Thời gian dự kiến:** 120 giây  
**Chủ đề:** Lập trình logic điều khiển

[Chi tiết nguồn](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 4: Đọc Giá Trị Cảm Biến Ánh Sáng

**Câu hỏi:** Để lập trình tính năng "Đèn tự động bật khi trời tối", bạn cần sử dụng câu lệnh nào để đọc giá trị từ cảm biến ánh sáng?

**Lựa chọn:**
- A. Read digital pin
- B. Read ultrasonic sensor
- C. Read analog pin
- D. Write digital pin

**Đáp án đúng:** C

**Phân tích chi tiết:**
Cảm biến ánh sáng thường trả về giá trị cường độ ánh sáng dưới dạng tín hiệu tương tự, do đó cần sử dụng câu lệnh "Read analog pin" để xét điều kiện sáng/tối. Giá trị đọc được sẽ nằm trong khoảng 0-1023, cho phép phân biệt mức độ ánh sáng môi trường.

**Mức độ nhận thức:** Hiểu - Áp dụng  
**Thời gian dự kiến:** 75 giây  
**Chủ đề:** Cảm biến ánh sáng và xử lý tín hiệu tương tự

[Chi tiết nguồn](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu 5: Hành Vi Khởi Động Hệ Thống

**Câu hỏi:** Theo yêu cầu khởi động của đề bài, trạng thái của xe và đèn LED như thế nào là đúng?

**Lựa chọn:**
- A. Xe chạy thẳng ngay lập tức, đèn LED tắt
- B. Xe đứng yên, 2 đèn LED chớp tắt cùng nhau 3 lần
- C. Xe lùi lại, 2 đèn LED sáng liên tục
- D. Xe đứng yên, 2 đèn LED sáng luân phiên

**Đáp án đúng:** B

**Phân tích chi tiết:**
Yêu cầu lập trình số 1 quy định: Khi khởi động, xe đứng yên và 2 đèn chớp tắt cùng nhau 3 lần trước khi bắt đầu di chuyển. Đây là tín hiệu báo hiệu hệ thống đã sẵn sàng hoạt động.

**Mức độ nhận thức:** Nhớ - Hiểu  
**Thời gian dự kiến:** 45 giây  
**Chủ đề:** Chuỗi hành vi khởi động hệ thống

[Chi tiết nguồn](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng Phân Tích Câu Hỏi

| STT | Chủ Đề | Mức Độ | Thời Gian | Trọng Số |
|-----|--------|--------|-----------|----------|
| 1 | Kết nối mạch điện | Hiểu | 60s | 20% |
| 2 | Điều khiển động cơ | Phân tích | 90s | 25% |
| 3 | Logic tránh vật cản | Ứng dụng | 120s | 30% |
| 4 | Cảm biến ánh sáng | Hiểu | 75s | 15% |
| 5 | Hành vi khởi động | Nhớ | 45s | 10% |

---

## Hướng Dẫn Sử Dụng Tài Liệu

### Đối Với Người Học:
- Thực hành các câu hỏi này sau khi hoàn thành module về Arduino và cảm biến
- Sử dụng để tự kiểm tra kiến thức trước kỳ thi thực hành
- Kết hợp với tài liệu thực hành để hiểu rõ hơn về mạch điện và lập trình

### Đối Với Giáo Viên:
- Sử dụng làm ngân hàng câu hỏi cho các kỳ thi đánh giá
- Có thể điều chỉnh mức độ khó bằng cách thay đổi các lựa chọn
- Kết hợp với bài thực hành để đánh giá toàn diện năng lực học viên

---

**Tài liệu được chuẩn hóa theo tiêu chuẩn LOM v4.4 Supreme**  
**Ngày tạo:** [Tự động sinh]  
**Phiên bản:** 1.0  
**Tác giả nội dung:** @engineer - Content Engineering Team

[Liên kết nguồn gốc đầy đủ](../raw/MASTER_SOURCE_INDEX.md)
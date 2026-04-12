---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_cu_chua_sua_extension_kdi_e_trac_nghiem_1___arduino_m2_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 arduino 2 cu chua sua extension kdi e trac nghiem 1   arduino m2 bank

# Tài liệu Đánh giá: TEST BANK - Tự Động Hóa và IoT Arduino M2

## Thông tin Tài liệu
| Thuộc tính | Giá trị |
|------------|---------|
| ID Tài liệu | LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_cu_chua_sua_extension_kdi_e_trac_nghiem_1___arduino_m2_bank |
| Danh mục | Đánh giá |
| Loại | Ngân hàng câu hỏi trắc nghiệm |
| Mức độ | Arduino Mô-đun 2 |
| Nguồn | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## Bài kiểm tra: Cấu trúc Breadboard và Lập trình Arduino Cơ bản

### Câu hỏi 1: Cấu trúc điện của Breadboard

**Câu hỏi:** Trong breadboard, những hàng cột nào được nối với nhau?

**Lựa chọn:**

A. Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện với nhau.

B. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực A/B/C/D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau.

C. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau.

D. Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau.

**Đáp án đúng:** D

**Giải thích:** Đây là cấu tạo tiêu chuẩn của breadboard phổ biến: hàng nguồn chạy ngang và hàng linh kiện chạy dọc theo từng cụm 5 lỗ [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu hỏi 2: Điều khiển LED nhấp nháy

**Câu hỏi:** Cho mạch Arduino và đèn LED như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn LED sáng nhấp nháy (sáng-tắt) với chu kỳ 2 giây?

**Hình ảnh minh họa:**
![Sơ đồ mạch Arduino và LED](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image29.png)
![Lựa chọn A](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image29.png)
![Lựa chọn B](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image37.png)
![Lựa chọn C](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image54.png)
![Lựa chọn D](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image45.png)

**Đáp án đúng:** A

**Giải thích:** Chu kỳ 2 giây nghĩa là 1 giây sáng và 1 giây tắt. Lệnh `wait 1 seconds` (1000ms) tương ứng với đáp án A [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### Câu hỏi 3: Lập trình điều khiển cảm biến mưa

**Câu hỏi:** Yêu cầu lập trình cho cảm biến mưa và các đèn LED hoạt động như sau: khi trời không mưa, đèn đỏ sáng, đèn xanh tắt; khi trời mưa, đèn đỏ tắt, đèn xanh sáng. Một học sinh đã lập trình như sau:

![Chương trình cảm biến mưa](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2__CŨ_chưa_sửa_Extension_KDI__Đề_trắc_nghiệm_1_-_Arduino_M2_image28.png)

Hỏi học sinh đó đã nối chân tín hiệu của cảm biến mưa và đèn LED với các chân nào của Arduino?

**Lựa chọn:**

A. Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn LED xanh nối với chân D4. Chân dương của đèn LED đỏ nối với chân D5.

B. Chân tín hiệu của cảm biến mưa được nối với chân A5. Chân dương của đèn LED xanh nối với chân D5. Chân dương của đèn LED đỏ nối với chân D4.

C. Chân tín hiệu của cảm biến mưa được nối với chân A4. Chân dương của đèn LED xanh nối với chân D6. Chân dương của đèn LED đỏ nối với chân D5.

D. Chân tín hiệu của cảm biến mưa được nối với chân A5. Chân dương của đèn LED xanh nối với chân D4. Chân dương của đèn LED đỏ nối với chân D6.

**Đáp án đúng:** A

**Giải thích:** Dựa vào mã nguồn lập trình, cảm biến mưa được đọc từ cổng analog A6, đèn xanh được điều khiển qua cổng số D4, đèn đỏ qua cổng số D5 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Hướng dẫn sử dụng tài liệu

### Đối tượng sử dụng:
- Học viên đang học môn Tự động hóa và IoT Arduino Mô-đun 2
- Giáo viên giảng dạy chuyên ngành điện tử - tự động hóa

### Mục tiêu đánh giá:
- Kiến thức về cấu trúc breadboard
- Kỹ năng lập trình Arduino cơ bản
- Hiểu biết về cảm biến và điều khiển thiết bị đầu ra

### Thời lượng khuyến nghị:
- 45 phút cho toàn bộ bài kiểm tra
- 15 phút cho mỗi câu hỏi trắc nghiệm

---

## Ghi chú kỹ thuật

> [!NOTE]
> Tài liệu này thuộc ngân hàng câu hỏi chuẩn hóa theo tiêu chuẩn LOM v4.4 Supreme. Mọi sửa đổi cần được phê duyệt trước khi cập nhật phiên bản chính thức.

> [!WARNING]
> Hình ảnh minh họa có thể chưa hoàn chỉnh do giới hạn từ nguồn gốc tài liệu. Đề nghị kiểm tra lại đường dẫn hình ảnh trước khi sử dụng trong giảng dạy chính thức.

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
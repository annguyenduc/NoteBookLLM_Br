---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_trac_nghiem_1___arduino_m2_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 arduino 2 e trac nghiem 1   arduino m2 bank

# Tài Liệu Học Tập LOM v4.4 Supreme

## Thông Tin Tài Liệu
| Thuộc tính | Giá Trị |
|------------|---------|
| **ID Tài Liệu** | LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_trac_nghiem_1___arduino_m2_bank |
| **Tiêu Đề** | Ngân Hàng Câu Hỏi Trắc Nghiệm Arduino - Mạch Điện & Lập Trình |
| **Loại Tài Liệu** | Đánh Giá/Trắc Nghiệm |
| **Chuyên Ngành** | Tự Động Hóa & IoT |
| **Mức Độ** | Trung Cấp |
| **Nguồn Gốc** | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## Bài Kiểm Tra: Cấu Trúc Breadboard và Lập Trình Arduino Cơ Bản

### Câu Hỏi 1: Cấu Trúc Kết Nối Breadboard

**Câu hỏi:** Trong breadboard, những hàng cột nào được nối với nhau?

**Lựa chọn:**
- **A.** Tất cả các lỗ ở cả 4 khu vực A, B, C, D đều dẫn điện với nhau.
- **B.** Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong từng khu vực A/B/C/D, tất cả các lỗ trong khu vực đó đều dẫn điện với nhau.
- **C.** Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng DỌC (2 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng NGANG (30 lỗ) dẫn điện với nhau.
- **D.** Các lỗ ở từng khu vực A, B, C, D cách điện với nhau. Trong khu vực A và D, các lỗ hàng NGANG (25 lỗ) dẫn điện với nhau. Trong khu vực B và C, các lỗ hàng DỌC (5 lỗ) dẫn điện với nhau.

**Đáp án đúng:** **D**

**Giải thích:** Theo cấu tạo chuẩn của breadboard, các dải nguồn (A, D) nối thông theo hàng ngang dài, còn các dải linh kiện (B, C) nối thông theo các cột dọc ngắn (thường là 5 lỗ) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### Câu Hỏi 2: Lập Trình Điều Khiển LED Nhấp Nháy

**Câu hỏi:** Cho mạch Arduino và đèn LED như hình bên dưới, hỏi đoạn chương trình nào dùng để điều khiển cho đèn LED sáng nhấp nháy (sáng-tắt) với chu kỳ 2 giây?

![Sơ đồ mạch Arduino và LED](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image54.png)

**Lựa chọn:**
- **A.** ![Lựa chọn A](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image37.png)
- **B.** ![Lựa chọn B](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image29.png)
- **C.** ![Lựa chọn C](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image46.png)
- **D.** ![Lựa chọn D](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image45.png)

**Đáp án đúng:** **B**

**Giải thích:** Chu kỳ 2 giây nghĩa là tổng thời gian 1 lần sáng và 1 lần tắt là 2 giây. Do đó mỗi trạng thái (sáng/tắt) cần `delay(1000)` (1 giây) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

### Câu Hỏi 3: Kết Nối Cảm Biến Mưa và LED

**Câu hỏi:** Yêu cầu lập trình cho cảm biến mưa và các đèn LED hoạt động như sau: khi trời không mưa, đèn đỏ sáng, đèn xanh tắt; khi trời mưa, đèn đỏ tắt, đèn xanh sáng. Một học sinh đã lập trình như sau:

![Chương trình cảm biến mưa](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_trắc_nghiệm_1_-_Arduino_M2_image28.png)

Hỏi học sinh đó đã nối chân tín hiệu của cảm biến mưa và đèn LED với các chân nào của Arduino?

**Lựa chọn:**
- **A.** Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn LED xanh nối với chân D4. Chân dương của đèn LED đỏ nối với chân D5.
- **B.** Chân tín hiệu của cảm biến mưa được nối với chân A6. Chân dương của đèn LED xanh nối với chân D5. Chân dương của đèn LED đỏ nối với chân D4.
- **C.** Chân tín hiệu của cảm biến mưa được nối với chân D6. Chân dương của đèn LED xanh nối với chân D4. Chân dương của đèn LED đỏ nối với chân D5.
- **D.** [Nội dung bị cắt]

**Đáp án đúng:** **A**

**Giải thích:** Dựa vào chương trình, cảm biến mưa được đọc từ cổng analog A6, đèn xanh được điều khiển bởi chân số D4, đèn đỏ bởi chân số D5 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## Bảng Đánh Giá Năng Lực

| Mức Độ | Nội Dung | Số Câu | Trọng Số |
|--------|----------|--------|----------|
| **Nhận biết** | Hiểu cấu trúc breadboard | 1 | 33% |
| **Thông hiểu** | Áp dụng lập trình cơ bản | 1 | 33% |
| **Vận dụng** | Phân tích kết nối phần cứng | 1 | 34% |

---

## Hướng Dẫn Sử Dụng Tài Liệu

### Đối Tượng Sử Dụng:
- Học viên lớp Tự Động Hóa & IoT
- Sinh viên kỹ thuật điện tử
- Người mới bắt đầu với Arduino

### Thời Gian Làm Bài:
- **Thời lượng:** 45 phút
- **Hình thức:** Trắc nghiệm trực tuyến hoặc giấy
- **Số câu:** 3 câu hỏi trắc nghiệm

### Tiêu Chí Đánh Giá:
- **Điểm đạt:** ≥ 60%
- **Phản hồi tự động:** Có
- **Gợi ý cải thiện:** Có

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
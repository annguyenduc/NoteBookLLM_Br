---
file_id: LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_1___tieu_chi_cham_va_thang_iem___arduino_m2_bank
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS Tests tu ong hoa va iot arduino 12 arduino 2 e 1   tieu chi cham va thang iem   arduino m2 bank

# LMS_Tests_tu_ong_hoa_va_iot_arduino_12_arduino_2_e_1___tieu_chi_cham_va_thang_iem___arduino_m2_bank

## Tài Liệu Kiểm Tra: Thiết Kế Hệ Thống Xe Điều Khiển Từ Xa IoT Arduino

**Môn học:** Tự Động Hóa và IoT Arduino  
**Mức độ:** Trung cấp (Module 2)  
**Loại đánh giá:** Trắc nghiệm ứng dụng thực tiễn  
**Thời lượng:** 45 phút  
**Nguồn:** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Mục Tiêu Học Tập

Sau khi hoàn thành bài kiểm tra này, người học sẽ có khả năng:

- Phân tích yêu cầu hệ thống điều khiển xe IoT đa chức năng
- Thiết kế mạch điện tích hợp cảm biến, động cơ và giao tiếp không dây
- Lập trình điều khiển từ xa qua giao thức hồng ngoại
- Triển khai hệ thống giám sát môi trường thời gian thực

---

## Câu Hỏi Đánh Giá

### Câu hỏi trắc nghiệm ứng dụng

**Câu hỏi:**  
Lập trình, gắn mạch điện và chế tạo xe điều khiển từ xa kết hợp thu thập dữ liệu nhiệt độ, độ ẩm với các yêu cầu sau:

1. **Điều khiển di chuyển:** Sử dụng mạch L298 điều khiển 2 động cơ vàng di chuyển: Tiến (phím 2), Lùi (phím 8), Xoay trái (phím 4), Xoay phải (phím 6), Dừng (phím 5) qua Remote hồng ngoại.
2. **Hiển thị dữ liệu:** Hiển thị dữ liệu DHT11 lên LCD 16x2 I2C: Dòng 1 hiển thị "N.do: [giá trị] do C", Dòng 2 hiển thị "Do am: [giá trị] %".
3. **Hệ thống cảnh báo:** 3 LED với logic:
   - LED 1: Sáng khi khởi động thành công
   - LED 2 (Đỏ): Sáng khi nhiệt độ ngoài khoảng 25-35°C
   - LED 3 (Xanh dương): Sáng khi độ ẩm ngoài khoảng 40-70%
4. **Phần cứng yêu cầu:** Nguồn 2 đế pin 4 mắc song song, có mái che bảo vệ linh kiện khi phun sương

> ![Sơ đồ mạch điện tổng thể](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_image1.png)

**Các phương án lựa chọn:**

| Phương án | Kết nối LCD | Logic cảnh báo | Ghi chú |
|-----------|-------------|----------------|---------|
| **A** | SDA-A5, SCL-A4 | LED 2 sáng khi nhiệt độ 30°C | Sai chân I2C chuẩn |
| **B** | SDA-A4, SCL-A5 | LED 3 sáng khi độ ẩm 50% | Sai logic cảnh báo |
| **C** | SDA-A4, SCL-A5 | LED 2 sáng khi nhiệt độ 38°C; LED 3 sáng khi độ ẩm 80% | **Đáp án đúng** |
| **D** | SDA-A5, SCL-A4 | Sử dụng nguồn nối tiếp cho L298 | Sai chân I2C và cấu hình nguồn |

**Đáp án đúng:** C

**Giải thích chi tiết:**
- Theo chuẩn giao tiếp I2C trên Arduino Uno: **SDA nối A4** và **SCL nối A5** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Theo yêu cầu đề bài:
  - LED 2 (Đỏ) sáng khi **nhiệt độ ngoài khoảng 25-35°C** → 38°C là **ngoài ngưỡng** nên LED phải sáng
  - LED 3 (Xanh dương) sáng khi **độ ẩm ngoài khoảng 40-70%** → 80% là **ngoài ngưỡng** nên LED phải sáng
- Phương án A và D sai sơ đồ chân I2C chuẩn
- Phương án B sai logic cảnh báo (50% là giá trị bình thường nên LED phải tắt)

---

## Hình Ảnh Minh Họa Hệ Thống

### Sơ đồ kết nối linh kiện chính
> ![Sơ đồ kết nối các linh kiện chính](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_image3.png)

### Giao diện lập trình khối điều khiển IR
> ![Giao diện lập trình khối điều khiển IR](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_image15.png)

### Mô hình xe thực tế với mái che bảo vệ
> ![Mô hình xe thực tế với mái che bảo vệ](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_image18.jpg)

### Cấu trúc vòng lặp kiểm tra điều kiện cảm biến
> ![Cấu trúc vòng lặp kiểm tra điều kiện cảm biến](../../brain/raw/lms_multi_media_dump/assets/Tự_động_hóa_và_IOT_Arduino_1+2_Arduino_2_Đề_1_-_Tiêu_chí_chấm_và_thang_điểm_-_Arduino_M2_image6.png)

---

## Ma trận Đánh Giá

| Nội dung | Mức độ | Số câu | Tỷ lệ |
|----------|--------|--------|-------|
| Kết nối phần cứng | Nhận biết | 1 | 25% |
| Giao tiếp I2C | Thông hiểu | 1 | 25% |
| Logic điều khiển | Vận dụng | 1 | 25% |
| Hệ thống cảnh báo | Vận dụng cao | 1 | 25% |

---

## Hướng Dẫn Chấm Điểm

| Tiêu chí | Số điểm | Ghi chú |
|----------|---------|---------|
| Hiểu chuẩn I2C Arduino | 2.5 điểm | SDA-A4, SCL-A5 |
| Áp dụng ngưỡng cảnh báo | 2.5 điểm | 25-35°C, 40-70% |
| Phân tích logic điều kiện | 2.5 điểm | LED sáng khi vượt ngưỡng |
| Tổng hợp kiến thức | 2.5 điểm | Kết hợp nhiều yếu tố |

**Tổng cộng:** 10 điểm

---

## Gợi ý Bài Tập Tự Luận Liên Quan

1. Viết đoạn mã Arduino xử lý logic điều khiển xe theo tín hiệu IR
2. Thiết kế mạch điện hoàn chỉnh với các chân GPIO phù hợp
3. Phân tích ưu nhược điểm của cấu hình nguồn song song so với nối tiếp

---

**Tài liệu tham khảo:** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
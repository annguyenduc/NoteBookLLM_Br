---
file_id: CONV_Atoms_atoms_v04_3
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v04 3

# Tài liệu Học tập: Thiết kế và Lập trình Hệ thống IoT & Robotics

## Thông tin Tài liệu
| Thuộc tính | Giá trị |
|------------|---------|
| Mã tài liệu | LOM-v4.4-Supreme-IoT-Robotics-VV04 |
| Ngôn ngữ | Vietnamese |
| Loại tài liệu | Lesson Draft + Worksheet + Quiz |
| Đối tượng | Học sinh THPT - Lớp 10-12 |
| Thời lượng | 8-10 tiết học (40 phút/tiết) |
| Nguồn gốc | Volume v04 - IoT, Robotics và lập trình điều khiển [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## # Bài học 1: Quy chuẩn Sơ đồ khối và Lập trình IoT

### ## Mục tiêu học tập
Sau bài học này, học sinh sẽ:
- Hiểu và áp dụng quy chuẩn sơ đồ khối IoT tiêu chuẩn
- Thiết kế logic điều khiển chuyên sâu với ngưỡng và hysteresis
- Xây dựng cơ chế an toàn cho hệ thống IoT
- Lập kế hoạch kiểm thử sản phẩm IoT

### ## Nội dung chính

#### ### 1.1 Sơ đồ khối IoT tiêu chuẩn

Một hệ thống IoT hoàn chỉnh phải bao gồm **5 khối chức năng chính** theo thứ tự sau:

| Khối chức năng | Chức năng | Ví dụ cụ thể |
|----------------|-----------|--------------|
| **Nguồn điện** | Cung cấp năng lượng | 5V/USB-C |
| **Cảm biến (Input)** | Thu thập dữ liệu môi trường | DHT20, cảm biến ánh sáng |
| **Bộ điều khiển trung tâm** | Xử lý logic điều khiển | Yolo:Bit/Arduino UNO |
| **Cơ cấu chấp hành (Output)** | Thực hiện hành động | Relay, động cơ servo |
| **Giao diện người dùng** | Tương tác với người dùng | UI/Hiển thị LCD |

> [!NOTE]
> Sơ đồ khối là nền tảng thiết kế bắt buộc cho mọi dự án IoT [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### ### 1.2 Logic điều khiển chuyên sâu

**Ngưỡng (Threshold)** và **Hysteresis** là hai yếu tố quan trọng để tránh hiện tượng bật/tắt liên tục:

```python
# Ví dụ mã giả cho logic điều khiển với hysteresis
if (sensor_value < threshold_low):
    output = ON
elif (sensor_value > threshold_high):
    output = OFF
```

**Lọc nhiễu theo thời gian** giúp ổn định tín hiệu đầu vào, tránh phản ứng sai do nhiễu ngẫu nhiên.

#### ### 1.3 Cơ chế an toàn (Fail-safe)

Các cơ chế an toàn bắt buộc cho hệ thống có cơ cấu chấp hành mạnh:

| Cơ chế | Mô tả | Ví dụ |
|--------|-------|-------|
| **Timeout** | Thời gian chạy tối đa | Bơm tự ngắt sau 5 phút |
| **Lockout** | Thời gian nghỉ bắt buộc | Nghỉ 10 phút giữa các lần kích hoạt |
| **Manual override** | Chế độ điều khiển thủ công | Công tắc tắt/mở bằng tay |

#### ### 1.4 Kế hoạch kiểm thử (Test Plan)

Một kế hoạch kiểm thử hiệu quả cần có tối thiểu **5 ca kiểm thử**:

| Test Case | Điều kiện đầu vào | Kết quả mong đợi | Trạng thái |
|-----------|-------------------|------------------|------------|
| TC01 | Nhiệt độ > 30°C | Bật quạt làm mát | Pass/Fail |
| TC02 | Độ ẩm < 35% | Kích hoạt bơm tưới | Pass/Fail |

---

## # Bài học 2: Linh kiện và Kit Phát triển IoT

### ## Mục tiêu học tập
- Nhận biết các loại cảm biến phổ biến trong kit IoT
- Hiểu chức năng của các cơ cấu chấp hành
- Áp dụng ngưỡng vận hành thực tế cho hệ thống

### ## Nội dung chính

#### ### 2.1 Cảm biến tiêu chuẩn trong kit

| Tên cảm biến | Chức năng | Ứng dụng |
|--------------|-----------|----------|
| **DHT20** | Đo nhiệt độ, độ ẩm không khí | Hệ thống điều hòa tự động |
| **Cảm biến ánh sáng** | Đo cường độ ánh sáng | Đèn đường tự động |
| **Cảm biến siêu âm** | Đo khoảng cách | Báo động khi có người |
| **Cảm biến độ ẩm đất** | Đo độ ẩm môi trường trồng | Tưới cây thông minh |

#### ### 2.2 Cơ cấu chấp hành phổ biến

| Thiết bị | Chức năng | Ứng dụng |
|----------|-----------|----------|
| **Relay** | Kích hoạt thiết bị điện | Bật/tắt bơm, đèn |
| **Động cơ Servo** | Điều khiển góc quay | Van điều tiết, cửa tự động |
| **Quạt mini** | Làm mát | Hệ thống thông gió |
| **LED đơn/RGB** | Cảnh báo, hiển thị | Đèn báo trạng thái |

#### ### 2.3 Ngưỡng vận hành thực tế

**Ví dụ: Hệ thống tưới cây thông minh**
- Kích hoạt bơm khi: `Độ ẩm đất < 35%` và `Ánh sáng > 200 lux`
- Tự động ngắt bơm nếu: `Khoảng cách người < 30cm`

> [!IMPORTANT]
> Các ngưỡng này là giá trị mẫu được đề xuất để đảm bảo tính khả thi của logic điều khiển [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## # Bài học 3: Thiết kế 3D và In ấn Kỹ thuật

### ## Mục tiêu học tập
- Hiểu tiêu chuẩn thiết kế 3D cho in ấn
- Phân tích tính "Watertight" của mô hình
- Thiết kế vỏ hộp cho thiết bị IoT

### ## Nội dung chính

#### ### 3.1 Tiêu chuẩn thiết kế 3D

File STL đạt chuẩn in ấn cần đảm bảo:

- ✅ **Watertight**: Khối đặc, không rỗng bên trong
- ✅ **Không có shells rời rạc**: Tất cả thành phần dính liền nhau
- ✅ **Không có cạnh suy biến**: Không có cạnh dài 0mm

#### ### 3.2 Góc overhang trong in 3D FDM

| Góc overhang | Yêu cầu support | Ghi chú |
|--------------|-----------------|---------|
| `< 60°` | Không cần | In trực tiếp được |
| `≥ 60°` | Cần support | Cấu trúc hỗ trợ bắt buộc |

![Phân tích overhang](../../brain/raw/lms_multi_media_dump/assets/vv04_image1.png)

#### ### 3.3 Thiết kế vỏ hộp IoT

**Yêu cầu kỹ thuật:**
- Dung sai lắp ráp: 0.3mm - 0.4mm
- Khoang chờ cho LCD 1602
- Khoang chờ cho board mạch điều khiển
- Lỗ thoát nhiệt và cáp

---

## # Bài học 4: Hệ thống IoT Mở rộng

### ## Mục tiêu học tập
- Hiểu kiến trúc hệ thống IoT nâng cao
- Kết nối ESP32 với Internet
- Tích hợp ứng dụng di động và database

### ## Nội dung chính

#### ### 4.1 Hệ thống đèn học thông minh (Smart Focus Lamp)

**Kiến trúc hệ thống:**

```
Cảm biến ánh sáng → ESP32 → Ứng dụng di động ↔ Database
     ↑                                    ↓
   Cảm biến chuyển động ←------------- Lịch sử vận hành
```

**Tính năng mở rộng:**
- Đồng bộ dữ liệu với App
- Lưu trữ lịch sử vận hành
- Điều khiển từ xa

---

## # Worksheet: Thực hành Thiết kế Hệ thống IoT

### ## Bài tập 1: Vẽ sơ đồ khối IoT
Thiết kế sơ đồ khối cho hệ thống "Đèn ngủ thông minh" với các yêu cầu:
- Tự động bật khi trời tối và có người
- Tự động tắt sau 30 phút
- Có nút nhấn tắt khẩn cấp

### ## Bài tập 2: Thiết lập ngưỡng điều khiển
Cho hệ thống điều hòa không khí, thiết lập:
- Ngưỡng nhiệt độ: ON khi > 28°C, OFF khi < 26°C
- Ngưỡng độ ẩm: ON khi > 70%, OFF khi < 65%
- Cơ chế an toàn: Tự động tắt sau 8 tiếng liên tục

### ## Bài tập 3: Kế hoạch kiểm thử
Xây dựng 5 test case cho hệ thống tưới cây thông minh.

---

## # Quiz: Kiểm tra kiến thức

### ## Câu hỏi trắc nghiệm

**Câu 1:** Một sơ đồ khối IoT tiêu chuẩn gồm bao nhiêu khối chức năng chính?
A. 3
B. 4  
C. 5
D. 6

**Câu 2:** Ngưỡng độ ẩm đất để kích hoạt bơm tưới theo tài liệu là:
A. < 25%
B. < 30%
C. < 35%
D. < 40%

**Câu 3:** Góc overhang nào yêu cầu cấu trúc hỗ trợ trong in 3D FDM?
A. < 45°
B. < 60°
C. ≥ 60°
D. ≥ 90°

### ## Câu hỏi tự luận

**Câu 4:** Trình bày 3 cơ chế an toàn bắt buộc cho hệ thống có cơ cấu chấp hành mạnh và giải thích vai trò của từng cơ chế.

**Câu 5:** Thiết kế một kế hoạch kiểm thử gồm 3 test case cho hệ thống đèn học thông minh.

---

## # Scenario: Dự án Thực tế

### ## Tình huống: Thiết kế hệ thống vườn rau thông minh

Bạn là kỹ sư IoT được giao nhiệm vụ thiết kế hệ thống vườn rau thông minh cho trường học. Hệ thống cần:

1. **Theo dõi môi trường:** Nhiệt độ, độ ẩm không khí, ánh sáng, độ ẩm đất
2. **Tự động tưới cây:** Khi độ ẩm đất < 35% và ánh sáng > 200 lux
3. **An toàn:** Tự động ngắt bơm nếu phát hiện người trong bán kính 30cm
4. **Hiển thị:** LCD hiển thị trạng thái hệ thống
5. **Thiết kế 3D:** Vỏ bảo vệ cho mạch điện

### ## Yêu cầu:
- Vẽ sơ đồ khối hệ thống
- Thiết lập logic điều khiển với hysteresis
- Xây dựng 5 test case kiểm thử
- Đề xuất thiết kế 3D cho vỏ bảo vệ

> [!CAUTION]
> Tất cả thông tin kỹ thuật quan trọng đều có nguồn gốc từ tài liệu chính thức [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
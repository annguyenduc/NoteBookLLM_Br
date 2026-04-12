---
file_id: CONV_Atoms_conv_atoms_v02_4
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v02 4

# Tài liệu Học Tập: IoT, AI và TinyML trên Nền Tảng OhStem

**Phiên bản:** LOM v4.4 Supreme  
**Ngôn ngữ:** Tiếng Việt  
**Mục tiêu:** Cung cấp kiến thức nền tảng và kỹ thuật thực tiễn về IoT, AI, và TinyML trên nền tảng OhStem cho học sinh THPT và sinh viên năm nhất.

---

## # Mục Lục

1. [Giới thiệu về IoT và TinyML](#gioi-thieu)
2. [Hiệu chỉnh cảm biến và xử lý tín hiệu](#hieu-chinh-cam-bien)
3. [Trích xuất đặc trưng và tăng cường dữ liệu](#trich-xuat-dac-trung)
4. [Giao thức truyền thông IoT](#giao-thuc-truyen-thong)
5. [Phần cứng và tối ưu hóa hiệu năng](#phan-cung-toi-uu)
6. [Thiết bị đầu vào và đầu ra](#thiet-bi-dau-vao-ra)
7. [Ứng dụng thực tế trong hackathon](#ung-dung-thuc-te)

---

## # 1. Giới thiệu về IoT và TinyML {#gioi-thieu}

### ## Mục tiêu học tập

- Hiểu vai trò của IoT và AI trong đời sống hiện đại.
- Nhận biết các thành phần chính trong hệ thống IoT.
- Làm quen với nền tảng OhStem và YoloBit.

### ## Nội dung chính

IoT (Internet of Things) là mạng lưới các thiết bị vật lý có cảm biến, phần mềm và kết nối internet để thu thập và trao đổi dữ liệu. TinyML là lĩnh vực nghiên cứu và phát triển các mô hình học máy chạy trên vi điều khiển có tài nguyên hạn chế như ESP32, giúp đưa AI đến gần hơn với thiết bị đầu cuối.

> **Lưu ý:** Việc tích hợp AI vào thiết bị IoT giúp hệ thống có thể ra quyết định thông minh tại chỗ, tiết kiệm băng thông và thời gian phản hồi [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 2. Hiệu chỉnh cảm biến và xử lý tín hiệu {#hieu-chinh-cam-bien}

### ## Mục tiêu học tập

- Hiểu tầm quan trọng của hiệu chỉnh cảm biến.
- Áp dụng kỹ thuật làm mượt dữ liệu và lọc tín hiệu.

### ## Nội dung chính

#### ### Hiệu chỉnh cảm biến

Hiệu chỉnh (calibrate) cảm biến giúp mô hình học được đặc trưng thực tế thay vì lỗi hệ thống [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Lọc mũ (Exponential Smoothing)

Lọc mũ là phương pháp làm mượt dữ liệu cảm biến hiệu quả với công thức:

```
ema = α * đọc_mới + (1 - α) * ema
```

Trong đó `α` là hệ số làm mượt (0 < α < 1).

#### ### Kỹ thuật Hysteresis

Sử dụng hai ngưỡng `T_high` và `T_low` giúp hệ thống ra quyết định ổn định, tránh tình trạng chập chờn khi dữ liệu sát ngưỡng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 3. Trích xuất đặc trưng và tăng cường dữ liệu {#trich-xuat-dac-trung}

### ## Mục tiêu học tập

- Hiểu vai trò của trích xuất đặc trưng trong học máy.
- Biết cách áp dụng tăng cường dữ liệu để cải thiện mô hình.

### ## Nội dung chính

#### ### Trích xuất đặc trưng (Feature Extraction)

- **MFCC (Mel-Frequency Cepstral Coefficients)**: Dùng cho âm thanh.
- **FFT (Fast Fourier Transform)**: Dùng cho rung động.

Việc trích xuất đặc trưng giúp giảm khối lượng tính toán và nhiễu cho mô hình chính [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Tăng cường dữ liệu (Data Augmentation)

Tăng cường dữ liệu bằng cách xoay ảnh, thay đổi độ sáng hoặc thêm nhiễu nhân tạo giúp mô hình tổng quát tốt hơn và tránh overfit [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Nền tảng hỗ trợ

Nền tảng Edge Impulse và TinyML cho phép định nghĩa khối DSP để xử lý dữ liệu cảm biến trước khi đưa vào mạng neural [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 4. Giao thức truyền thông IoT {#giao-thuc-truyen-thong}

### ## Mục tiêu học tập

- So sánh các giao thức truyền thông phổ biến trong IoT.
- Hiểu cách sử dụng MQTT và ESP-NOW.

### ## Nội dung chính

#### ### So sánh giao thức

| Giao thức | Ưu điểm | Nhược điểm |
|-----------|----------|------------|
| HTTP REST | Dễ lập trình | Chậm, tốn băng thông |
| MQTT | Nhanh hơn HTTP 20–25 lần, nhẹ | Cần broker | 
| ESP-NOW | Rất nhanh, không cần TCP/IP | Chỉ dùng cho chip ESP |

Giao thức MQTT nhanh hơn HTTP REST từ 20–25 lần trong việc truyền dữ liệu IoT liên tục [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Thư viện hỗ trợ

Thư viện **PubSubClient** trên Arduino hỗ trợ MQTT với các tính năng hữu ích như QoS (Chất lượng dịch vụ) và Last Will (Di chúc cuối cùng) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

ESP-NOW là giao thức không dây riêng của Espressif cho phép truyền dữ liệu trực tiếp giữa các chip ESP32 rất nhanh và nhẹ, bỏ qua tầng TCP/IP [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 5. Phần cứng và tối ưu hóa hiệu năng {#phan-cung-toi-uu}

### ## Mục tiêu học tập

- Nhận biết các tính năng nổi bật của chip ESP32-S3.
- Hiểu cách tối ưu hiệu năng và quản lý năng lượng.

### ## Nội dung chính

#### ### ESP32-S3

- **Tập lệnh vector**: Giúp tăng tốc tính toán AI/DSP thông qua các thư viện ESP-DSP và ESP-NN [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).
- **ULP (Ultra-Low-Power Core)**: Có thể theo dõi cảm biến trong khi CPU chính đang ở chế độ Deep Sleep [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### TFLite Micro

TensorFlow Lite Micro trên ESP32-S3 tích hợp các kernel tối ưu (ESP-NN) để tăng tốc các phép tính ma trận và tích chập [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Camera AI V2 của OhStem

Module Camera AI V2 của OhStem có khả năng tự xử lý các tác vụ nặng như nhận diện khuôn mặt, giúp giảm tải cho vi điều khiển chính Yolo UNO [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 6. Thiết bị đầu vào và đầu ra {#thiet-bi-dau-vao-ra}

### ## Mục tiêu học tập

- Liệt kê và phân loại các thiết bị đầu vào và đầu ra phổ biến.
- Biết cách sử dụng các thiết bị này trong dự án IoT.

### ## Nội dung chính

#### ### Thiết bị đầu vào (Input)

- **Cảm biến ánh sáng (LDR)**
- **Siêu âm (HC-SR04)**
- **DHT20 (nhiệt độ, độ ẩm)**
- **Nút nhấn**

Các thiết bị đầu vào phổ biến trong hackathon gồm: Cảm biến ánh sáng (LDR), siêu âm (HC-SR04), DHT20 và Nút nhấn [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

#### ### Thiết bị đầu ra (Output)

- **LED đơn, LED RGB**
- **Servo**
- **Relay**
- **LCD 1602**
- **Động cơ DC**

Các thiết bị đầu ra phổ biến gồm: LED đơn, LED RGB, Servo, Relay, LCD 1602 và Động cơ DC [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # 7. Ứng dụng thực tế trong hackathon {#ung-dung-thuc-te}

### ## Mục tiêu học tập

- Xác định các chủ đề thường gặp trong cuộc thi IoT/AI.
- Lên ý tưởng dự án theo từng lĩnh vực.

### ## Nội dung chính

#### ### Các chủ đề phổ biến

- **Môi trường**: Giám sát chất lượng không khí, nước.
- **Y tế**: Theo dõi sức khỏe, phát hiện bất thường.
- **Giáo dục**: Thiết bị hỗ trợ học tập thông minh.
- **Giao thông/An toàn**: Phát hiện tai nạn, cảnh báo giao thông.
- **Năng lượng**: Tối ưu hóa tiêu thụ điện, giám sát năng lượng tái tạo.

Các chủ đề thực tế thường gặp trong thi đấu IoT AI gồm: Môi trường, Y tế, Giáo dục, Giao thông/An toàn, Năng lượng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## # Bài tập thực hành (Worksheet)

### ## Bài 1: Hiệu chỉnh cảm biến

1. Viết đoạn mã hiệu chỉnh cảm biến nhiệt độ DHT20.
2. Áp dụng bộ lọc mũ để làm mượt dữ liệu cảm biến.
3. Giải thích tại sao cần hiệu chỉnh cảm biến?

### ## Bài 2: Giao tiếp MQTT

1. Kết nối ESP32 với broker MQTT.
2. Gửi dữ liệu cảm biến mỗi 5 giây.
3. So sánh hiệu suất với HTTP REST.

### ## Bài 3: Dự án nhỏ

- Chọn một chủ đề từ danh sách trên.
- Lên sơ đồ mạch và flowchart hoạt động.
- Trình bày ý tưởng trong 5 phút.

---

## # Kiểm tra nhanh (Quiz)

1. Giao thức nào nhanh hơn HTTP REST trong IoT?
   - A. HTTP
   - B. MQTT
   - C. FTP
   - D. TCP
   > ✅ Đáp án: B

2. ESP32-S3 có hỗ trợ tăng tốc phần cứng không?
   - A. Có
   - B. Không
   > ✅ Đáp án: A

3. Tăng cường dữ liệu giúp gì cho mô hình?
   - A. Giảm overfit
   - B. Tăng tốc độ
   - C. Giảm RAM
   - D. Không ảnh hưởng
   > ✅ Đáp án: A

---

## # Scenario: Hệ thống giám sát môi trường thông minh

Bạn là kỹ sư IoT trong một dự án giám sát môi trường. Nhiệm vụ:

- Thu thập dữ liệu từ cảm biến DHT20, MQ-135, LDR.
- Gửi dữ liệu lên cloud qua MQTT.
- Phát hiện bất thường và cảnh báo qua LED RGB.
- Tối ưu hóa pin bằng chế độ Deep Sleep.

Hãy thiết kế hệ thống theo các bước:

1. Sơ đồ mạch.
2. Flowchart chương trình.
3. Mã giả (pseudo-code).
4. Phân tích hiệu suất và năng lượng.

---

**Tài liệu này thuộc quyền sở hữu của OhStem và được phân phối theo giấy phép LOM v4.4 Supreme.**  
[Liên kết nguồn đầy đủ](../raw/MASTER_SOURCE_INDEX.md)
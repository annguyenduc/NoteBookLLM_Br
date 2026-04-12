---
file_id: CONV_Atoms_atoms_v02_4
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v02 4

# Tài liệu Học Tập: TinyML & IoT trên ESP32-S3 với Yolo UNO

## Thông tin chung
| Thuộc tính | Giá trị |
|------------|---------|
| Mã học phần | LOM-TinyML-IoT-v4.4 |
| Tên tiếng Việt | TinyML và IoT trên nền tảng ESP32-S3 |
| Thời lượng | 12 tiết học (3 buổi) |
| Đối tượng | Học sinh THCS/THPT, người mới bắt đầu IoT |
| Mức độ | Trung cấp |
| Nguồn gốc | [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) |

---

## Mục tiêu học tập

Sau khi hoàn thành bài học này, học sinh sẽ có khả năng:

- Hiểu và áp dụng các kỹ thuật xử lý dữ liệu cảm biến trong hệ thống TinyML
- Thiết kế hệ thống IoT hiệu quả sử dụng giao thức MQTT và ESP-NOW
- Tối ưu hóa hiệu suất hệ thống bằng các kỹ thuật lập trình đa nhiệm và quản lý năng lượng
- Phối hợp các thiết bị cảm biến và đầu ra để xây dựng ứng dụng thực tiễn

---

## Bài 1: Xử lý dữ liệu & AI trên nền tảng TinyML

### 1.1 Hiệu chỉnh cảm biến (Calibration)

Hiệu chỉnh cảm biến là bước quan trọng giúp mô hình AI học được đặc trưng thực tế thay vì lỗi hệ thống. Quá trình này đảm bảo rằng dữ liệu đầu vào phản ánh đúng điều kiện thực tế, từ đó nâng cao độ chính xác của mô hình.

> **Ví dụ thực tế**: Một cảm biến nhiệt độ có sai số +2°C cần được hiệu chỉnh để đưa ra giá trị chính xác.

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 1.2 Trích xuất đặc trưng (Feature Extraction)

Trích xuất đặc trưng giúp giảm khối lượng tính toán và nhiễu so với việc dùng dữ liệu thô. Một số kỹ thuật phổ biến:

- **MFCC (Mel-Frequency Cepstral Coefficients)**: Dùng trong xử lý âm thanh
- **FFT (Fast Fourier Transform)**: Dùng trong phân tích tín hiệu rung động

![Trích xuất đặc trưng](../../brain/raw/lms_multi_media_dump/assets/volume_v02_image1.png)

> **Lợi ích**: Giảm tải xử lý, tăng tốc độ nhận diện, giảm nhiễu dữ liệu

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 1.3 Tăng cường dữ liệu (Data Augmentation)

Tăng cường dữ liệu bằng cách thêm nhiễu nhân tạo hoặc thay đổi góc chụp giúp mô hình bền bỉ hơn và tránh overfit. Đây là kỹ thuật quan trọng trong huấn luyện mô hình AI.

**Phương pháp phổ biến**:
- Thêm nhiễu Gaussian
- Biến đổi hình ảnh (xoay, lật, zoom)
- Thay đổi ánh sáng

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 1.4 Tăng tốc phần cứng trên ESP32-S3

Chip **ESP32-S3** trên Yolo UNO hỗ trợ tập lệnh vector tăng tốc AI thông qua thư viện **ESP-NN** và **ESP-DSP**, giúp xử lý ma trận nhanh hơn CPU thuần.

**Ưu điểm**:
- Tăng tốc độ xử lý AI
- Tiết kiệm năng lượng
- Hỗ trợ mô hình phức tạp hơn

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 2: Truyền thông IoT & Hiệu suất hệ thống

### 2.1 So sánh giao thức: MQTT vs HTTP REST

**MQTT** nhanh hơn **HTTP REST** từ **20-25 lần** trong việc truyền dữ liệu IoT liên tục trên ESP32. Đây là lý do MQTT được ưa chuộng trong các ứng dụng IoT thời gian thực.

| Tiêu chí | HTTP REST | MQTT |
|----------|-----------|------|
| Tốc độ | Chậm hơn | Nhanh hơn 20-25x |
| Overhead | Cao | Thấp |
| Phù hợp | API web | IoT thời gian thực |

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 2.2 Đóng gói dữ liệu hiệu quả

Đóng gói dữ liệu dạng **CSV** (chuỗi ngắn) thay vì **JSON** giúp giảm kích thước gói tin đáng kể. Ví dụ: từ 27 byte xuống chỉ còn 6 byte.

**So sánh**:
```json
// JSON: 27 byte
{"temp":25.5,"hum":60}
```
```csv
// CSV: 6 byte  
25.5,60
```

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 2.3 Giao thức ESP-NOW

**ESP-NOW** là giao thức không dây riêng của Espressif cho phép các chip ESP32 truyền dữ liệu trực tiếp cho nhau rất nhanh mà không cần qua tầng TCP/IP.

**Đặc điểm**:
- Không cần kết nối WiFi
- Độ trễ cực thấp
- Phù hợp cho mạng cảm biến

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 2.4 Quản lý năng lượng với ULP

ESP32-S3 sở hữu lõi phụ **ULP (Ultra-low-power)** có thể theo dõi cảm biến khi CPU chính đang ở chế độ **Deep Sleep**, giúp tiết kiệm năng lượng đáng kể.

**Ứng dụng**:
- Giám sát liên tục với pin lâu dài
- Hệ thống cảm biến không cần xử lý mạnh

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 3: Tối ưu hóa lập trình & Ứng dụng thực tiễn

### 3.1 Lọc mũ (Exponential Moving Average)

Lọc mũ với công thức `ema = α*mới + (1-α)*ema` giúp làm mịn dữ liệu cảm biến hiệu quả hơn lọc trung bình đơn giản.

**Cú pháp**:
```
EMA mới = α × Giá trị mới + (1-α) × EMA cũ
```

**Ưu điểm**:
- Phản hồi nhanh hơn
- Giảm nhiễu hiệu quả
- Tiết kiệm bộ nhớ

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 3.2 Cơ chế Hysteresis

Cơ chế **Hysteresis** sử dụng 2 ngưỡng cao/thấp giúp ngăn chặn tình trạng thiết bị đầu ra (như Relay) bị bật/tắt liên tục khi dữ liệu cảm biến dao động quanh một ngưỡng đơn.

**Nguyên lý hoạt động**:
- Bật khi vượt ngưỡng CAO
- Tắt khi xuống dưới ngưỡng THẤP
- Tránh hiện tượng "run relay"

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

### 3.3 Đa nhiệm giả lập với "Mỗi ... ms"

Sử dụng khối lệnh **"Mỗi ... ms"** thay vì lệnh **"Chờ (delay)"** cho phép Yolo UNO thực hiện đa nhiệm giả lập trên giao diện lập trình khối.

**So sánh**:
- `Chờ(1000)` → Dừng toàn bộ chương trình
- `Mỗi 1000ms` → Thực hiện song song nhiều tác vụ

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Bộ thiết bị phổ biến trong Hackathon

### Thiết bị đầu vào (Input)
- **Cảm biến ánh sáng (LDR)**
- **Cảm biến siêu âm (HC-SR04)**
- **Cảm biến DHT20 (Nhiệt độ/Độ ẩm)**
- **Nút nhấn**

### Thiết bị đầu ra (Output)
- **LED đơn, LED RGB**
- **Servo**
- **Relay**
- **LCD 1602**
- **Động cơ DC**

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Ứng dụng thực tiễn theo chủ đề

### Combo "Siêu âm + Servo"
**Ứng dụng**: Cửa tự động, Barie thông minh  
**Chủ đề**: An toàn, Giao thông

### Combo "DHT20 + Quạt DC/Relay"  
**Ứng dụng**: Hệ thống làm mát, tưới tiêu tự động  
**Chủ đề**: Môi trường, Nông nghiệp

### Các chủ đề Hackathon phổ biến
- Môi trường
- Y tế
- Giáo dục
- An toàn
- Năng lượng
- Giao thông

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Phiếu bài tập thực hành

### Bài tập 1: Thiết kế hệ thống giám sát nhiệt độ
**Yêu cầu**: Sử dụng DHT20 + Relay + Quạt DC để xây dựng hệ thống làm mát tự động

**Hướng dẫn**:
1. Áp dụng cơ chế Hysteresis
2. Sử dụng lọc mũ cho dữ liệu cảm biến
3. Gửi dữ liệu lên server qua MQTT

### Bài tập 2: Cổng kiểm soát thông minh
**Yêu cầu**: Kết hợp HC-SR04 + Servo để tạo cổng tự động

**Hướng dẫn**:
1. Phát hiện vật cản trong khoảng cách 20cm
2. Điều khiển servo mở cổng
3. Sử dụng đa nhiệm để đồng thời giám sát và điều khiển

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu hỏi kiểm tra

### Câu 1
**MQTT nhanh hơn HTTP REST bao nhiêu lần trong truyền dữ liệu IoT?**
- A. 5-10 lần
- B. 10-15 lần
- C. 20-25 lần
- D. 30-35 lần

### Câu 2
**ESP-NOW là gì?**
- A. Giao thức truyền dữ liệu qua Internet
- B. Giao thức không dây riêng của Espressif
- C. Thư viện xử lý AI
- D. Bộ nhớ đệm dữ liệu

### Câu 3
**Cơ chế Hysteresis sử dụng mấy ngưỡng?**
- A. 1 ngưỡng
- B. 2 ngưỡng
- C. 3 ngưỡng
- D. Không giới hạn

### Câu 4
**Lọc mũ sử dụng công thức nào?**
- A. `ema = (mới + cũ) / 2`
- B. `ema = α*mới + (1-α)*ema`
- C. `ema = max(mới, cũ)`
- D. `ema = min(mới, cũ)`

[Chi tiết kỹ thuật](../raw/MASTER_SOURCE_INDEX.md)

---

## Tài nguyên tham khảo

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Tài liệu Edge Impulse
- Tài liệu Espressif ESP32-S3
- Hướng dẫn lập trình app.ohstem.vn

---

*© 2024 Content Engineering Team - LOM v4.4 Supreme Standard*
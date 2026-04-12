---
file_id: LMS_KB_ROBOTICS_V4.1
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS KB ROBOTICS V4.1

# 🚗 LẬP TRÌNH ROBOTICS VỚI PYTHON & YOLOBIT

## 📋 THÔNG TIN BÀI HỌC

| Thuộc tính | Giá trị |
|------------|---------|
| Mã bài học | LMS-KB-ROBOTICS-V4.1 |
| Thời lượng | 90 phút |
| Đối tượng | Học sinh THCS/THPT |
| Ngôn ngữ | Tiếng Việt |
| Phiên bản | 4.4 Supreme |

---

## 🎯 MỤC TIÊU HỌC TẬP

Sau bài học này, học sinh sẽ có thể:

- **[BLOOM-APPLY]** Áp dụng ngôn ngữ Python để điều khiển robot YoloBit trong các nhiệm vụ điều khiển cơ bản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **[BLOOM-ANALYZE]** Phân tích cấu trúc cảm biến - logic - cơ cấu chấp hành trong hệ thống Robotics [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- **[BLOOM-EVALUATE]** Đánh giá hiệu quả của các thuật toán điều khiển robot đơn giản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📚 NỘI DUNG BÀI HỌC

### 1. GIỚI THIỆU PYTHON TRONG ROBOTICS

Python là ngôn ngữ nền tảng được sử dụng rộng rãi để điều khiển robot và triển khai các mô hình AI nhờ vào khả năng xử lý dữ liệu và thư viện phong phú [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md). Trong lập trình hệ thống (Robotics/IoT), việc sử dụng vòng lặp kết hợp với `assert` để kiểm tra kiểu dữ liệu của từng phần tử trong danh sách là một kỹ thuật quan trọng để đảm bảo tính ổn định của thuật toán [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

### 2. YOLOBIT - NỀN TẢNG LẬP TRÌNH ROBOTIC

YoloBit là một nền tảng lập trình giáo dục thường được sử dụng trong giảng dạy STEM/Robotics tại Việt Nam, tương tự như Micro:bit [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md). Đây là một máy tính lập trình nhỏ gọn (tương tự Micro:bit) hỗ trợ học STEM, cho phép kết nối các cảm biến để thực hiện các ứng dụng IoT và điều khiển Robot đơn giản [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

YoloBit là một máy tính lập trình nhỏ gọn dựa trên chip ESP32, tích hợp nhiều cảm biến và đèn LED, thường được dùng để giảng dạy lập trình IoT và Robotics cho học sinh [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

![yolobit_board](../../brain/raw/lms_multi_media_dump/assets/LMS_KB_ROBOTICS_V4_1_image1.png)

### 3. CẤU TRÚC CẢM BIẾN - LOGIC - CƠ CẤU CHẤP HÀNH

Cấu trúc "Sensor – Logic – Actuator Canvas" yêu cầu tối thiểu 3 cảm biến và 2 cơ cấu chấp hành để bám sát các bộ kit học tập [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md). Một sơ đồ khối IoT đầy đủ tiêu chuẩn phải bao gồm 5 khối chức năng chính:

- **Nguồn (5V/USB-C)** 
- **Cảm biến (Input)**
- **Bộ điều khiển trung tâm (Yolo:Bit/UNO)**
- **Cơ cấu chấp hành (Output)**
- **Giao diện người dùng (UI/Hiển thị)** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 4. CÁC LOẠI CẢM BIẾN TRONG ROBOTICS

Các cảm biến phổ biến trong Robotics và IoT bao gồm: **DHT11/LM35** (nhiệt độ), **HC-SR04** (siêu âm), **PIR** (chuyển động), **MPU-6050** (gia tốc/cân bằng) và **MQ-2** (khí gas) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

Các loại cảm biến phổ biến trong dự án IoT/Robotics: DHT20 (nhiệt độ/độ ẩm), Ánh sáng (Lux), Siêu âm, Độ ẩm đất (Soil), Vật cản (PersonNear) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

### 5. CƠ CẤU CHẤP HÀNH (ACTUATORS)

Các cơ cấu chấp hành (actuators) phổ biến để thực hiện hóa giải pháp Robotics/IoT gồm: Relay (kích hoạt bơm/đèn), động cơ Servo (điều khiển góc quay van/cửa), quạt mini và hệ thống LED đơn hoặc LED RGB [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

Các cơ cấu chấp hành (Actuators) thường dùng: Relay (điều khiển Bơm/Đèn), Servo, Quạt, màn hình LCD [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## 🛠️ HOẠT ĐỘNG THỰC HÀNH

### Bài tập 1: Điều khiển LED RGB trên YoloBit

```python
# Viết chương trình điều khiển đèn LED RGB trên YoloBit
# Bật đèn màu đỏ trong 2 giây, sau đó chuyển sang xanh lá
from yolobit import *
import time

while True:
    # Bật đèn đỏ
    rgb_matrix.fill(0xFF0000)  # Màu đỏ
    rgb_matrix.show()
    time.sleep(2)
    
    # Chuyển sang xanh lá
    rgb_matrix.fill(0x00FF00)  # Màu xanh lá
    rgb_matrix.show()
    time.sleep(2)
```

### Bài tập 2: Đọc cảm biến siêu âm

```python
# Viết chương trình đọc giá trị từ cảm biến siêu âm
# Nếu khoảng cách < 10cm thì bật đèn đỏ, ngược lại bật đèn xanh
from yolobit import *
import time

def read_ultrasonic():
    # Giả lập đọc cảm biến siêu âm
    distance = 15  # cm
    return distance

while True:
    distance = read_ultrasonic()
    if distance < 10:
        rgb_matrix.fill(0xFF0000)  # Đèn đỏ
    else:
        rgb_matrix.fill(0x00FF00)  # Đèn xanh
    rgb_matrix.show()
    time.sleep(0.5)
```

### Bài tập 3: Điều khiển servo

Động cơ Servo SG90 hoạt động ở tần số 50Hz, có dải xung từ 0.5ms đến 2.4ms, tương ứng với giá trị `duty_u16` từ khoảng 1638 đến 7864 khi lập trình trên vi điều khiển [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

---

## 📋 WORKSHEET: CẢM BIẾN - LOGIC - CƠ CẤU CHẤP HÀNH

| STT | Cảm biến | Chức năng | Cơ cấu chấp hành | Hành động khi kích hoạt |
|-----|----------|-----------|------------------|-------------------------|
| 1   | Siêu âm    | Đo khoảng cách | Đèn LED | Bật đèn đỏ nếu <10cm |
| 2   | Nhiệt độ   | Đo nhiệt độ | Quạt | Bật quạt nếu >30°C |
| 3   | Ánh sáng   | Đo cường độ ánh sáng | Đèn LED | Bật đèn nếu <50 Lux |
| 4   | PIR | Phát hiện chuyển động | Còi báo động | Kêu còi khi phát hiện người |
| 5   | DHT20 | Đo nhiệt độ/độ ẩm | Màn hình LCD | Hiển thị thông số |

---

## ❓ QUIZ: KIỂM TRA HIỂU BIẾT

### Câu 1: Python được sử dụng trong Robotics vì lý do nào?
A. Dễ học và thân thiện với người mới bắt đầu  
B. Có nhiều thư viện hỗ trợ xử lý dữ liệu và điều khiển thiết bị  
C. Chạy nhanh hơn các ngôn ngữ khác  
D. A và B đúng  

**Đáp án: D** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 2: YoloBit sử dụng chip gì làm nền tảng?
A. Arduino UNO  
B. ESP32  
C. Raspberry Pi  
D. Micro:bit  

**Đáp án: B** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 3: Cấu trúc cơ bản của hệ thống IoT gồm các thành phần nào?
A. Cảm biến - Vi xử lý - Cơ cấu chấp hành  
B. Nguồn - Cảm biến - Bộ điều khiển - Cơ cấu chấp hành - Giao diện người dùng  
C. Cảm biến - Động cơ - Màn hình  
D. Nguồn - Cảm biến - Động cơ  

**Đáp án: B** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 4: Động cơ Servo SG90 hoạt động ở tần số bao nhiêu?
A. 60Hz  
B. 50Hz  
C. 40Hz  
D. 30Hz  

**Đáp án: B** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Câu 5: Trong cấu trúc Sensor-Logic-Actuator, thành phần nào đóng vai trò xử lý thông tin?
A. Cảm biến  
B. Cơ cấu chấp hành  
C. Bộ điều khiển  
D. Nguồn điện  

**Đáp án: C** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 🎭 SCENARIO: THÁM HIỂM SAO HỎA

Giả sử bạn là kỹ sư điều khiển robot thám hiểm Sao Hỏa. Robot của bạn (mô phỏng Perseverance) được trang bị:
- Cảm biến siêu âm (phát hiện vật cản)
- Cảm biến ánh sáng (xác định môi trường sáng/tối)
- Cảm biến nhiệt độ (theo dõi điều kiện môi trường)
- Động cơ servo (điều khiển cơ cấu gắp mẫu vật)
- Đèn LED RGB (hiển thị trạng thái)

**Nhiệm vụ**: Viết thuật toán điều khiển robot di chuyển an toàn, tránh vật cản, thu thập mẫu vật khi phát hiện điểm có nhiệt độ phù hợp và ánh sáng yếu (có thể là hang động).

**Yêu cầu**:
- Nếu cảm biến siêu âm phát hiện vật cản <20cm → rẽ phải
- Nếu cảm biến ánh sáng <50 Lux → robot dừng lại và quét khu vực xung quanh
- Nếu nhiệt độ từ 15-25°C → kích hoạt cơ cấu gắp mẫu vật
- Đèn LED đỏ khi gặp nguy hiểm, xanh khi hoạt động bình thường

```python
# Mô phỏng thuật toán điều khiển robot thám hiểm Sao Hỏa
from yolobit import *
import time

def avoid_obstacle():
    # Rẽ phải khi phát hiện vật cản
    print("Phát hiện vật cản! Rẽ phải...")
    # Code điều khiển động cơ

def scan_area():
    # Quét khu vực xung quanh
    print("Quét khu vực...")
    # Code quét servo

def collect_sample():
    # Kích hoạt cơ cấu gắp mẫu vật
    print("Thu thập mẫu vật...")
    # Code điều khiển servo gắp

while True:
    # Đọc cảm biến
    distance = read_ultrasonic()  # giả lập
    light_level = read_light_sensor()  # giả lập
    temperature = read_temperature()  # giả lập
    
    # Kiểm tra vật cản
    if distance < 20:
        avoid_obstacle()
        rgb_matrix.fill(0xFF0000)  # Đèn đỏ
    else:
        rgb_matrix.fill(0x00FF00)  # Đèn xanh
    
    # Kiểm tra ánh sáng
    if light_level < 50:
        scan_area()
    
    # Kiểm tra nhiệt độ để thu thập mẫu
    if 15 <= temperature <= 25:
        collect_sample()
    
    rgb_matrix.show()
    time.sleep(0.5)
```

---

## 📌 GỢI Ý BÀI TẬP NÂNG CAO

1. **Tích hợp thuật toán PID**: Áp dụng điều khiển PID để robot di chuyển chính xác theo đường line [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
2. **Xây dựng state machine**: Quản lý các trạng thái của robot (di chuyển, thu thập mẫu, quay về trạm) [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
3. **Tích hợp AI đơn giản**: Sử dụng cây quyết định để phân loại loại mẫu vật cần thu thập [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📚 TÀI LIỆU THAM KHẢO

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Tổng hợp kiến thức nền tảng
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Thông số kỹ thuật và cảm biến
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Cấu trúc hệ thống IoT
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Thuật toán PID trong robotics
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Hệ thống điều khiển robot Rover
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Ứng dụng AI trong robotics

---

## 📊 ĐÁNH GIÁ KẾT QUẢ HỌC TẬP

| Mức độ | Mô tả | Tiêu chí đánh giá |
|--------|-------|-------------------|
| Tốt | Thực hiện thành thạo tất cả các yêu cầu | Hoàn thành 100% bài tập, hiểu rõ cấu trúc hệ thống |
| Khá | Thực hiện tốt hầu hết yêu cầu | Hoàn thành 80% bài tập, hiểu cơ bản |
| Trung bình | Thực hiện được một phần yêu cầu | Hoàn thành 60% bài tập, cần hướng dẫn thêm |
| Cần cải thiện | Chưa đạt yêu cầu tối thiểu | Hoàn thành dưới 60%, cần ôn tập lại kiến thức |

---

*© 2024 Content Engineering Team - LOM v4.4 Supreme Standard*
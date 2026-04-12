---
file_id: LMS_KB_IOT
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS KB IOT

# Tài liệu Học tập Arduino IoT - LOM v4.4 Supreme

## Thông tin Tài liệu
| Thuộc tính | Giá trị |
|------------|---------|
| **Tiêu đề** | Hệ thống Arduino IoT Cơ bản |
| **Mô tả** | Tài liệu hướng dẫn cơ bản về lập trình Arduino, kết nối IoT và ứng dụng AI trong tự động hóa |
| **Ngôn ngữ** | Vietnamese |
| **Loại tài liệu** | Interactive Learning Module |
| **Trình độ** | Beginner to Intermediate |

---

## Bài 1: Giới thiệu Arduino và Kết nối Cơ bản

### Mục tiêu Học tập
Sau bài học này, học viên sẽ có thể:
- Nhận biết các phương pháp cấp nguồn cho Arduino
- Phân biệt các chân kết nối trên Arduino Uno R3
- Thiết lập kết nối giữa Arduino và máy tính

### Nội dung Chính

#### 1.1 Cấp nguồn cho Arduino
Arduino Uno R3 có **3 cách cấp nguồn chính**:

| Phương pháp | Mô tả | Ghi chú |
|-------------|-------|---------|
| **USB Connection** | Cổng USB kết nối với máy tính | Điện áp 5V, phù hợp cho lập trình cơ bản |
| **Jack Adapter** | Sử dụng adapter nguồn ngoài 9V | Phù hợp cho ứng dụng độc lập |
| **Chân Vin** | Kết nối trực tiếp với nguồn 7-12V | Linh hoạt cho nhiều loại pin |

> [!NOTE]
> Các chân 3.3V và 5V trên Arduino là các chân cấp nguồn đầu ra cho linh kiện, **không dùng để cấp nguồn đầu vào không ổn định** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### 1.2 Kết nối với Máy tính
Để kết nối Arduino với máy tính, sử dụng cáp USB:
- **Đầu USB-A**: Cắm vào máy tính
- **Đầu USB-B**: Cắm vào cổng nạp của Arduino

![Kết nối Arduino với máy tính](../../brain/raw/lms_multi_media_dump/assets/Tu_dong_hoa_va_IOT_AI_Arduino_De_trac_nghiem_1_AI_Arduino_image1.png)

#### 1.3 Chân Giao tiếp Serial
Chân Digital 0 (RX) và 1 (TX) trên Arduino được dành riêng cho **giao tiếp Serial**:
- RX: Nhận dữ liệu
- TX: Truyền dữ liệu
- **Cảnh báo**: Sử dụng các chân này cho mục đích Digital thông thường có thể gây nhiễu quá trình nạp code [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 2: Môi trường Lập trình mBlock5

### Mục tiêu Học tập
- Hiểu sự khác biệt giữa chế độ Live và Upload
- Sử dụng các khối lệnh cơ bản trong mBlock5
- Thiết lập giao tiếp giữa Arduino và máy tính

### 2.1 Chế độ Lập trình

| Chế độ | Mô tả | Ưu điểm | Nhược điểm |
|--------|-------|---------|------------|
| **Live Mode** | Điều khiển trực tiếp từ máy tính | Phản hồi tức thì, dễ debug | Yêu cầu kết nối liên tục, hạn chế khối lệnh |
| **Upload Mode** | Nạp chương trình vào Arduino | Chương trình chạy độc lập | Cần thời gian nạp, khó debug |

> [!IMPORTANT]
> Chế độ Live trong mBlock5 yêu cầu phần mềm luôn mở và duy trì kết nối với board; mọi thay đổi trong code sẽ tác động trực tiếp đến thiết bị ngay lập tức [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2.2 Giao tiếp giữa Thiết bị và Nhân vật
Khối lệnh "Broadcast" và "When I receive message" cho phép truyền nhận thông tin giữa nhân vật (Sprite) và thiết bị (Arduino):

```scratch
Khi nhận được [tin_nhan]
// Thực hiện hành động
```

> [!WARNING]
> Việc truyền (Broadcast) và nhận tin nhắn (When I receive) giữa thiết bị Arduino và nhân vật **chỉ có thể thực hiện khi sử dụng chế độ LIVE** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bài 3: Linh kiện Điện tử Cơ bản

### Mục tiêu Học tập
- Nhận biết và phân biệt các linh kiện cơ bản
- Hiểu nguyên lý hoạt động của từng loại linh kiện
- Kết nối đúng cách các linh kiện với Arduino

### 3.1 Đèn LED Siêu sáng

#### Đặc điểm kỹ thuật:
- **Chân dương (Anode)**: Dài hơn hoặc có lỗ nhỏ đánh dấu
- **Chân âm (Cathode)**: Ngắn hơn hoặc bản cực lớn hơn bên trong
- **Điện áp hoạt động**: 3V - 5V

| Cách phân biệt | Mô tả |
|----------------|-------|
| **Chân vật lý** | Chân dài là dương, chân ngắn là âm |
| **Bản cực bên trong** | Bản cực nhỏ hơn là dương, lớn hơn là âm |
| **Lỗ đánh dấu** | Một lỗ nhỏ trên thân đèn chỉ chân dương |

### 3.2 Còi Buzzer

#### Thông số kỹ thuật:
- **Loại**: Thiết bị đầu ra (output)
- **Điện áp hoạt động**: 3V - 5V
- **Cực tính**: 
  - Chân dài: Cực dương (+)
  - Chân ngắn: Cực âm (-)

### 3.3 Mạch thu phát âm thanh ISD1820

#### Kết nối cơ bản:
| Chân | Chức năng | Kết nối với |
|------|-----------|-------------|
| **VCC** | Nguồn điện | 5V |
| **GND** | Đất | GND |
| **REC** | Ghi âm | Điều khiển ghi |
| **PLAYE** | Phát âm thanh (Edge) | Điều khiển phát |
| **PLAYL** | Phát âm thanh (Level) | Điều khiển phát |

#### Hai chế độ phát âm thanh:
- **PLAYE (Edge-activated)**: Phát toàn bộ đoạn âm thanh đã ghi khi có tín hiệu kích hoạt
- **PLAYL (Level-activated)**: Chỉ phát âm thanh khi nút nhấn được giữ

---

## Bài 4: Breadboard và Mạch điện Cơ bản

### Mục tiêu Học tập
- Hiểu cấu trúc và nguyên lý hoạt động của breadboard
- Thiết kế mạch điện đơn giản trên breadboard
- Kết nối linh kiện đúng cách

### 4.1 Cấu trúc Breadboard

#### Quy tắc dẫn điện:
- **Khu vực nguồn (mép)**: Các lỗ nối thông theo **hàng ngang**
- **Khu vực giữa**: Các lỗ nối thông theo **hàng dọc** (nhóm 5 lỗ)
- **Cách điện**: Các hàng/cột được cách điện với nhau

| Khu vực | Hướng dẫn điện | Số lượng lỗ |
|---------|----------------|-------------|
| **Dải nguồn (A/B)** | Theo hàng ngang | Toàn bộ hàng |
| **Khu vực giữa (C/D)** | Theo cột dọc | Nhóm 5 lỗ |

### 4.2 Hướng dẫn lắp mạch

#### Các bước cơ bản:
1. Xác định vị trí các linh kiện
2. Kiểm tra cực tính của linh kiện
3. Nối dây theo sơ đồ mạch
4. Kiểm tra lại kết nối trước khi cấp nguồn

---

## Bài 5: Động cơ Servo và Điều khiển

### Mục tiêu Học tập
- Hiểu cấu tạo và nguyên lý hoạt động của động cơ servo
- Kết nối servo với Arduino đúng cách
- Điều khiển servo qua lập trình

### 5.1 Đặc điểm Động cơ Servo

#### Thông số kỹ thuật:
- **Loại**: Thiết bị đầu ra (output)
- **Điện áp hoạt động**: 5V
- **Số dây kết nối**: 3 dây
- **Phạm vi quay**: 0° đến 180° (đối với MG90S)

#### Sơ đồ dây kết nối:
| Dây | Màu sắc | Chức năng | Kết nối với |
|-----|---------|-----------|-------------|
| **1** | Nâu/Đen | GND | Chân GND Arduino |
| **2** | Đỏ | VCC | Chân 5V Arduino |
| **3** | Cam | Tín hiệu | Chân Digital PWM (3, 5, 6, 9, 10, 11) |

> [!CAUTION]
> Dây tín hiệu phải được kết nối với các chân Digital có hỗ trợ PWM (ký hiệu dấu ~) trên Arduino như: 3, 5, 6, 9, 10, 11 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 5.2 Lập trình Điều khiển Servo

#### Ví dụ code cơ bản:
```cpp
#include <Servo.h>
Servo myServo;

void setup() {
  myServo.attach(9); // Gắn servo vào chân 9
}

void loop() {
  myServo.write(90); // Quay về vị trí 90 độ
  delay(1000);
  myServo.write(0);  // Quay về vị trí 0 độ
  delay(1000);
}
```

---

## Bài 6: Cảm biến và Đo lường

### Mục tiêu Học tập
- Hiểu nguyên lý hoạt động của các loại cảm biến phổ biến
- Kết nối và đọc dữ liệu từ cảm biến
- Hiệu chỉnh độ nhạy của cảm biến

### 6.1 Cảm biến Hồng ngoại (IR)

#### Nguyên lý hoạt động:
- Phát và thu ánh sáng hồng ngoại
- Phát hiện vật cản dựa trên tín hiệu phản xạ
- **Điện áp hoạt động**: 3.3V - 5V

#### Ứng dụng:
- Phát hiện vật cản
- Điều khiển robot tránh vật cản
- Cổng cảm biến tự động

### 6.2 Cảm biến Siêu âm HC-SR04

#### Đặc điểm:
- **Nguyên lý**: Phát sóng siêu âm và nhận lại tín hiệu phản xạ
- **Phạm vi đo**: 2cm đến 400cm
- **Chân kết nối**: 
  - Trig: Gửi tín hiệu
  - Echo: Nhận tín hiệu phản hồi

#### Code đọc khoảng cách:
```cpp
long duration, distance;
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
```

### 6.3 Hiệu chỉnh Cảm biến

#### Điều chỉnh độ nhạy:
- Sử dụng biến trở (núm vặn màu xanh) trên module cảm biến
- Xoay để tăng/giảm độ nhạy
- Kiểm tra kết quả sau mỗi lần điều chỉnh

---

## Bài 7: Ứng dụng AI và Machine Learning

### Mục tiêu Học tập
- Hiểu về Teachable Machine và ứng dụng trong Arduino
- Tạo mô hình học máy đơn giản
- Tích hợp AI vào dự án Arduino

### 7.1 Teachable Machine

#### Quy trình tạo mô hình:
1. **Thêm Extension** vào mBlock
2. **Training model** → **Build new model**
3. **Cung cấp dữ liệu hình ảnh** cho từng lớp
4. **Learn** (Huấn luyện mô hình)
5. **Use the model** trong chương trình

#### Loại dữ liệu hỗ trợ:
- **Hình ảnh**: Phân loại đối tượng
- **Âm thanh**: Nhận diện tiếng nói
- **Tư thế**: Nhận diện cử chỉ

### 7.2 Extension Cognitive Services

#### Tính năng:
- Nhận diện khuôn mặt
- Nhận diện giọng nói
- **Yêu cầu**: Kết nối Internet
- **Giới hạn**: Số lượt sử dụng mỗi ngày
- **Kết quả**: Trả về dưới dạng chuỗi ký tự (string)

---

## Bài tập Thực hành

### Worksheet 1: Kết nối Cơ bản
**Tên học sinh:** _________________ **Ngày:** _________________

#### Câu 1: Ghép nối các phương pháp cấp nguồn với mô tả
| STT | Phương pháp | Mô tả |
|-----|-------------|-------|
| 1 | USB Connection | A. Nguồn 7-12V qua chân Vin |
| 2 | Jack Adapter | B. Kết nối với máy tính |
| 3 | Chân Vin | C. Sử dụng adapter 9V |

#### Câu 2: Đánh dấu ✓ vào ô đúng
| Câu hỏi | Đúng | Sai |
|---------|------|-----|
| Chân 3.3V và 5V dùng để cấp nguồn đầu vào | | |
| Chân 0 và 1 dùng cho giao tiếp Serial | | |
| Chế độ Live cần kết nối liên tục với máy tính | | |

### Worksheet 2: Linh kiện và Kết nối
**Thời gian:** 30 phút

#### Nhiệm vụ: Vẽ sơ đồ kết nối các linh kiện sau với Arduino Uno
1. Đèn LED (với điện trở hạn dòng)
2. Còi Buzzer
3. Động cơ Servo
4. Cảm biến siêu âm HC-SR04

---

## Quiz Kiểm tra

### Câu hỏi Trắc nghiệm

#### Câu 1: Arduino có thể được cấp nguồn bằng cách nào?
A. Chỉ qua cổng USB  
B. Qua cổng USB, Jack DC hoặc chân Vin  
C. Chỉ qua Jack DC  
D. Chỉ qua chân Vin  

**Đáp án đúng:** B [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### Câu 2: Chân Digital 0 và 1 trên Arduino dùng để làm gì?
A. Điều khiển LED  
B. Giao tiếp Serial  
C. Kết nối cảm biến  
D. Cấp nguồn  

**Đáp án đúng:** B [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### Câu 3: Chế độ Live trong mBlock5 có đặc điểm gì?
A. Chương trình lưu vĩnh viễn  
B. Yêu cầu kết nối liên tục  
C. Không thể debug  
D. Không có giới hạn khối lệnh  

**Đáp án đúng:** B [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### Câu 4: Dây tín hiệu của servo phải nối với chân nào trên Arduino?
A. Bất kỳ chân Digital nào  
B. Chỉ chân 5V  
C. Chân Digital có hỗ trợ PWM  
D. Chỉ chân GND  

**Đáp án đúng:** C [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

#### Câu 5: Breadboard có quy tắc dẫn điện như thế nào?
A. Tất cả các lỗ đều thông nhau  
B. Dải nguồn theo hàng ngang, khu vực giữa theo cột dọc  
C. Chỉ khu vực giữa mới dẫn điện  
D. Mỗi lỗ là riêng biệt  

**Đáp án đúng:** B [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Scenario Học tập

### Tình huống: Hệ thống Báo động Thông minh

#### Bối cảnh:
Bạn là kỹ sư IoT được giao nhiệm vụ thiết kế hệ thống báo động cho cửa hàng nhỏ. Hệ thống cần:
- Phát hiện người đi vào cửa hàng
- Cảnh báo bằng âm thanh và ánh sáng
- Gửi thông báo đến điện thoại chủ cửa hàng

#### Yêu cầu thiết kế:
1. **Cảm biến phát hiện**: Sử dụng cảm biến chuyển động PIR hoặc cảm biến siêu âm
2. **Cảnh báo**: Đèn LED và còi buzzer
3. **Giao tiếp**: Có thể tích hợp với ứng dụng điện thoại
4. **Tự động hóa**: Hoạt động 24/7

#### Giải pháp đề xuất:
- **Arduino Uno** làm trung tâm điều khiển
- **Cảm biến siêu âm HC-SR04** phát hiện khoảng cách
- **LED RGB** làm đèn cảnh báo
- **Buzzer** phát âm thanh cảnh báo
- **Module WiFi ESP8266** gửi thông báo
- **Code logic**: Nếu khoảng cách < 50cm → bật cảnh báo

#### Mở rộng:
- Tích hợp camera đơn giản
- Nhận diện khuôn mặt khách hàng
- Ghi nhận thời gian ra vào

---

## Tài nguyên Bổ sung

### Danh sách Linh kiện Đề xuất
| STT | Tên linh kiện | Số lượng | Ghi chú |
|-----|---------------|----------|---------|
| 1 | Arduino Uno R3 | 1 | Board chính |
| 2 | Breadboard 830 điểm | 1 | Mạch thử nghiệm |
| 3 | LED siêu sáng | 5 | Cảnh báo, hiển thị |
| 4 | Buzzer | 1 | Âm thanh cảnh báo |
| 5 | Động cơ Servo SG90 | 1 | Điều khiển cơ khí |
| 6 | Cảm biến siêu âm HC-SR04 | 1 | Phát hiện khoảng cách |
| 7 | Cảm biến hồng ngoại | 1 | Phát hiện vật cản |
| 8 | Dây nối | 20 | Kết nối mạch |
| 9 | Điện trở | 10 | Hạn dòng LED |

### Tài liệu Tham khảo
- [Arduino Official Documentation](https://www.arduino.cc/reference/)
- [mBlock5 User Guide](https://learn.makeblock.com/mblock5/)
- [Teachable Machine by Google](https://teachablemachine.withgoogle.com/)

---

## Đánh giá và Phản hồi

### Tiêu chí Đánh giá
| Mức độ | Mô tả |
|--------|-------|
| **Xuất sắc** | Hiểu rõ tất cả khái niệm, thực hiện
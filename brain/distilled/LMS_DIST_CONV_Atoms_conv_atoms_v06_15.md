---
file_id: CONV_Atoms_conv_atoms_v06_15
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v06 15

# Tài Liệu Học Tập: Phát Triển MicroPython trên ESP8266 với Cursor IDE

## Thông Tin Tài Liệu
| Thuộc Tính | Giá Trị |
|------------|---------|
| Mã Tài Liệu | LOM-v4.4-Supreme-MicroPython-ESP8266 |
| Ngôn Ngữ | Tiếng Việt |
| Mức Độ | Trung Cấp đến Nâng Cao |
| Thời Lượng | 4-6 giờ học |
| Đối Tượng | Kỹ sư IoT, Nhà phát triển nhúng |

---

## 🎯 Mục Tiêu Học Tập

Sau khi hoàn thành tài liệu này, học viên sẽ:

- Hiểu rõ giới hạn tài nguyên của ESP8266 và chiến lược phát triển hiệu quả [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Áp dụng mô hình HAL (Hardware Abstraction Layer) trong phát triển MicroPython
- Thiết lập workflow phát triển chuyên nghiệp trên Cursor IDE
- Thực hiện được việc test trên desktop và deploy lên thiết bị thực

---

## 📚 Nội Dung Học Tập

### 1. Tổng Quan về ESP8266 và Giới Hạn Tài Nguyên

ESP8266 là vi điều khiển phổ biến trong IoT nhưng có giới hạn nghiêm trọng về tài nguyên:

| Tài Nguyên | Giới Hạn |
|------------|----------|
| RAM Heap | ~40KB |
| Flash | 4MB (tùy loại) |
| CPU | 80MHz (có thể ép xung 160MHz) |

> **Lưu ý:** Do giới hạn RAM chỉ 40KB, các tác vụ xử lý nặng như giao thức PPP phức tạp không phù hợp với MicroPython trên ESP8266 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2. Kiến Trúc HAL (Hardware Abstraction Layer)

Mô hình này cho phép bạn phát triển logic độc lập với phần cứng:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Logic     │───▶│  Interface  │───▶│  Hardware   │
│  (Core)     │    │             │    │  (HAL)      │
└─────────────┘    └─────────────┘    └─────────────┘
```

---

## 📝 Bài Tập Thực Hành

### Worksheet 1: Thiết Lập Cấu Trúc Dự Án

**Họ và Tên:** ________________________  
**Ngày:** ________________________  
**Mục tiêu:** Thiết lập cấu trúc thư mục chuẩn cho phát triển MicroPython

#### Nhiệm vụ 1: Tạo cấu trúc thư mục
Tạo thư mục dự án tại `C:/Projects/esp8266_project/` với cấu trúc sau:

```
/app
  /core
    controller.py
  /hal
    interface.py
    esp_hal.py
    mock_hal.py
/desktop
  boot_desktop.py
/device
  boot.py
.cursorrules
```

#### Nhiệm vụ 2: Viết file `.cursorrules`
Tạo file `.cursorrules` với nội dung sau:

```markdown
# MicroPython Development Rules for ESP8266

## Project Architecture
- Luôn tách biệt Logic (`app/core`) và Phần cứng (`app/hal`).
- Logic trong `app/core` KHÔNG ĐƯỢC import các thư viện đặc thù của MicroPython như `machine`, `network`, `utime`.
- Mọi tương tác phần cứng phải thông qua Interface trong `app/hal/interface.py`.

## Mocking Strategy
- Khi người dùng yêu cầu "Test trên Desktop", hãy sử dụng `app/hal/mock_hal.py`.
- Khi người dùng yêu cầu "Nạp code", hãy đảm bảo `app/device/boot.py` sử dụng `app/hal/esp_hal.py`.

## Coding Standards
- Sử dụng `time.sleep` cho Desktop và `utime.sleep` cho Device (AI tự động chuyển đổi qua HAL).
- Ưu tiên viết code ngắn gọn vì ESP8266 chỉ có 40KB RAM [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).

## Deployment
- Sử dụng lệnh `mpremote connect COMx fs put <file> :<file>` để upload.
- Luôn nhắc nhumber người dùng kiểm tra cổng COM trong Device Manager [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md).
```

---

## 🧪 Quiz Kiểm Tra

### Câu 1: Giới hạn RAM của ESP8266 ảnh hưởng thế nào đến phát triển MicroPython?
A. Không ảnh hưởng gì đáng kể  
B. Chỉ ảnh hưởng khi dùng nhiều biến toàn cục  
C. Giới hạn nghiêm trọng các tác vụ xử lý nặng như giao thức PPP [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)  
D. Chỉ ảnh hưởng khi chạy đa luồng

### Câu 2: Mô hình HAL giúp ích gì trong phát triển MicroPython?
A. Giảm kích thước code  
B. Cho phép test logic trên desktop mà không cần phần cứng [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)  
C. Tăng tốc độ xử lý  
D. Tiết kiệm pin

### Câu 3: Việt Nam đã tắt sóng 2G từ thời điểm nào?
A. 2020  
B. 16/10/2024 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)  
C. 2025  
D. 2023

---

## 📖 Lesson Draft: Thiết Kế Module HAL

### Mục tiêu bài học
- Hiểu cách thiết kế interface module
- Viết mock HAL cho testing
- Viết ESP HAL cho deployment

### Nội dung chi tiết

#### 1. Interface Module
File: `app/hal/interface.py`

```python
class HardwareInterface:
    def toggle_led(self, state: bool):
        """Toggle LED state"""
        raise NotImplementedError
    
    def read_sensor(self):
        """Read sensor value"""
        raise NotImplementedError
```

#### 2. Mock HAL (Desktop Testing)
File: `app/hal/mock_hal.py`

```python
from .interface import HardwareInterface

class MockHAL(HardwareInterface):
    def toggle_led(self, state: bool):
        print(f"[MOCK] LED is {'ON' if state else 'OFF'}")
    
    def read_sensor(self):
        import random
        return random.randint(0, 100)
```

#### 3. ESP HAL (Device Deployment)
File: `app/hal/esp_hal.py`

```python
from machine import Pin
from .interface import HardwareInterface

class ESPHAL(HardwareInterface):
    def __init__(self):
        self.led = Pin(2, Pin.OUT)
    
    def toggle_led(self, state: bool):
        self.led.value(0 if state else 1)  # Logic đảo trên ESP8266
    
    def read_sensor(self):
        # Implementation for actual hardware
        pass
```

---

## 🎮 Scenario: Phát Triển Hệ Thống Giám Sát Đơn Giản

### Bối cảnh
Bạn đang phát triển hệ thống giám sát nhiệt độ sử dụng ESP8266. Hệ thống cần:
- Đọc cảm biến nhiệt độ mỗi 5 giây
- Bật đèn báo nếu nhiệt độ vượt ngưỡng
- Gửi dữ liệu lên server (trong tương lai)

### Yêu cầu
Thiết kế hệ thống theo mô hình HAL với các chức năng:
1. `read_temperature()` - đọc giá trị cảm biến
2. `set_warning_led(state)` - bật/tắt đèn cảnh báo
3. `send_data(data)` - gửi dữ liệu (mock cho desktop)

### Hướng dẫn thực hiện
1. Thiết kế interface trong `interface.py`
2. Viết mock HAL cho testing desktop
3. Viết ESP HAL cho deployment
4. Viết logic chính trong `controller.py`
5. Tạo file boot cho cả desktop và device

---

## 🔧 Công Cụ Hỗ Trợ

### Thay đổi cổng COM trên Windows
Để thay đổi số cổng COM (ví dụ COM5/COM6), người dùng cần vào **Port Settings → Advanced → COM Port Number** trong Device Manager [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### Lệnh upload với mpremote
```bash
mpremote connect COMx fs put app :app
mpremote connect COMx fs put device/boot.py :boot.py
```

---

## 📊 Đánh Giá Kết Quả Học Tập

| Tiêu Chí | Mức Độ Đạt Được | Ghi Chú |
|----------|-----------------|---------|
| Hiểu giới hạn ESP8266 | | |
| Thiết lập cấu trúc HAL | | |
| Viết interface module | | |
| Test trên desktop | | |
| Deploy lên thiết bị | | |

---

## 🔄 Gợi Ý Nâng Cao

- Với các dự án IoT di động, nên cân nhắc sử dụng **ESP32** thay vì ESP8266 vì hỗ trợ PPPoS chính thức trong ESP-IDF [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Chi phí triển khai bộ phát 4G DIY dùng ESP32 và module A7670C (Cat-1) tại Việt Nam khoảng **0,6 - 0,9 triệu VNĐ** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- Việt Nam đã chính thức **tắt sóng 2G từ ngày 16/10/2024** và dự kiến ngừng sóng 3G vào năm 2028 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## 📞 Hỗ Trợ

**Liên hệ giảng viên:** [Thông tin liên hệ]  
**Thời gian hỗ trợ:** [Giờ làm việc]  
**Kênh hỗ trợ:** [Email, diễn đàn, office hours]

---

*© 2024 - Tài liệu học tập chuẩn LOM v4.4 Supreme - Phát triển bởi Content Engineer Team* [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
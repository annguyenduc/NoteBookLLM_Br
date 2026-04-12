Chào bạn, tôi là @scout. Dựa trên dữ liệu từ **Volume v06**, tôi xin trích xuất các sự kiện quan trọng trước khi hướng dẫn bạn thiết lập Workflow chuyên nghiệp trên Cursor IDE.

### 📋 TRÍCH XUẤT SỰ KIỆN (FACTS) - [vv06]

- **Fact:** [CONV] Để thay đổi số cổng COM (ví dụ COM5/COM6) trên Windows, người dùng cần vào **Port Settings → Advanced → COM Port Number** trong Device Manager.
- **Source:** [Dòng 1-2]
- **Tag:** [vv06]

- **Fact:** [CONV] MicroPython trên ESP8266 có tài nguyên RAM rất hạn chế, chỉ khoảng 40KB heap, không phù hợp cho các tác vụ xử lý nặng như giao thức PPP phức tạp.
- **Source:** [Section: Ưu điểm/Nhược điểm của MicroPython trên ESP8266]
- **Tag:** [vv06]

- **Fact:** [CONV] Việt Nam đã chính thức tắt sóng 2G từ ngày 16/10/2024 và dự kiến ngừng sóng 3G vào năm 2028.
- **Source:** [Section: Vì sao không nên dùng ESP8266 cho hotspot 4G?]
- **Tag:** [vv06]

- **Fact:** [CONV] ESP32 được khuyến nghị hơn ESP8266 cho các dự án IoT di động vì hỗ trợ PPPoS chính thức trong ESP-IDF.
- **Source:** [Section: Lộ trình khả thi (khuyên dùng)]
- **Tag:** [vv06]

- **Fact:** [CONV] Chi phí triển khai bộ phát 4G DIY dùng ESP32 và module A7670C (Cat-1) tại Việt Nam khoảng 0,6 - 0,9 triệu VNĐ.
- **Source:** [Section: Phương án 4G (rẻ – dễ làm)]
- **Tag:** [vv06]

---

### 🚀 WORKFLOW PHÁT TRIỂN MICROPYTHON TRÊN CURSOR IDE

Để hiện thực hóa yêu cầu của bạn, chúng ta sẽ sử dụng mô hình **HAL (Hardware Abstraction Layer)**. Điều này cho phép bạn chạy logic trên máy tính (Mock) mà không cần cắm board.

#### 1. Cấu trúc thư mục (Project Structure)
Bạn hãy tạo thư mục dự án với cấu trúc tuyệt đối như sau:
`C:/Projects/esp8266_project/` (Ví dụ trên Windows)

```text
/app
  /core
    controller.py    <-- Logic chính (Không chứa code MicroPython đặc thù)
  /hal
    interface.py     <-- Định nghĩa các hàm (Bật LED, đọc Sensor)
    esp_hal.py       <-- Code thật cho ESP8266 (import machine)
    mock_hal.py      <-- Code giả lập cho Desktop (print ra màn hình)
/desktop
  boot_desktop.py    <-- Chạy thử trên máy tính
/device
  boot.py            <-- File nạp vào ESP8266
.cursorrules         <-- "Bộ não" hướng dẫn AI của Cursor
```

#### 2. Thiết lập `.cursorrules` (Quan trọng nhất)
Bạn hãy tạo file `.cursorrules` tại thư mục gốc của dự án và dán nội dung sau vào. Đây là lệnh để AI luôn tuân thủ workflow của bạn:

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
- Ưu tiên viết code ngắn gọn vì ESP8266 chỉ có 40KB RAM [vv06].

## Deployment
- Sử dụng lệnh `mpremote connect COMx fs put <file> :<file>` để upload.
- Luôn nhắc nhở người dùng kiểm tra cổng COM trong Device Manager [vv06].
```

#### 3. Ví dụ Logic mẫu

**`app/hal/interface.py`**:
```python
class HardwareInterface:
    def toggle_led(self, state: bool): pass
```

**`app/hal/mock_hal.py`**:
```python
from .interface import HardwareInterface
class MockHAL(HardwareInterface):
    def toggle_led(self, state: bool):
        print(f"[MOCK] LED is {'ON' if state else 'OFF'}")
```

**`app/hal/esp_hal.py`**:
```python
from machine import Pin
from .interface import HardwareInterface
class ESPHAL(HardwareInterface):
    def __init__(self):
        self.led = Pin(2, Pin.OUT)
    def toggle_led(self, state: bool):
        self.led.value(0 if state else 1) # ESP8266 logic đảo
```

#### 4. File thực thi

**`desktop/boot_desktop.py`**:
```python
from app.core.controller import run_logic
from app.hal.mock_hal import MockHAL

hal = MockHAL()
run_logic(hal)
```

**`device/boot.py`**:
```python
from app.hal.esp_hal import ESPHAL
from app.core.controller import run_logic

hal = ESPHAL()
run_logic(hal)
```

### 🛠 CÁCH SỬ DỤNG TRÊN CURSOR:
1. **Bước 1 (Viết logic):** Mở Chat (Ctrl+L), gõ: *"Viết logic chớp tắt LED trong controller.py sử dụng interface"*.
2. **Bước 2 (Test Desktop):** Gõ: *"Tạo file boot_desktop.py để chạy thử logic này với MockHAL"*. Bạn nhấn nút Run trên Cursor để xem kết quả in ra terminal.
3. **Bước 3 (Upload):** Gõ: *"Viết lệnh mpremote để upload toàn bộ thư mục app và file device/boot.py lên ESP8266"*.
4. **Bước 4 (Hardware Test):** Cursor sẽ cung cấp lệnh terminal, bạn chỉ cần copy-paste và chạy.

Bạn có muốn tôi viết chi tiết file `app/core/controller.py` cho dự án **"2 ESP8266 chat với nhau"** theo đúng workflow này không?
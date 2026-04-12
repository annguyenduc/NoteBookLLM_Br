Chào bạn, đây là một hướng dẫn chuyên sâu để thiết lập **Workflow "Desktop-First"** cho MicroPython trên Cursor IDE. Cách tiếp cận này giúp bạn code nhanh, ít lỗi và tận dụng tối đa sức mạnh của AI mà không cần cắm mạch liên tục.

### 1. Cấu trúc thư mục chuẩn (Separation of Concerns)

Bạn nên tổ chức thư mục như sau để tách biệt logic và phần cứng:

```text
/project-root
├── .cursorrules          # Luật cho AI của Cursor
├── .vscode/
│   └── tasks.json        # Phím tắt Upload/Monitor
├── src/
│   ├── app/
│   │   ├── core.py       # Logic chính (không chứa code phần cứng)
│   │   └── hal.py        # Hardware Abstraction Layer (Giao tiếp phần cứng)
│   ├── boot_desktop.py   # Chạy thử trên máy tính (Mock)
│   └── main.py           # Chạy thật trên ESP8266
└── requirements.txt      # Thư viện cho desktop (mpremote, v.v.)
```

---

### 2. Thiết lập Cursor Rules (`.cursorrules`)

Hãy tạo file `.cursorrules` ở thư mục gốc và dán nội dung sau vào. Đây là "bản chỉ dẫn" để Cursor không viết code sai kiến trúc:

```markdown
# MicroPython Development Rules (ESP8266)

## 1. Kiến trúc Code (HAL Pattern)
- Tách biệt hoàn toàn Logic (`core.py`) và Phần cứng (`hal.py`).
- `core.py`: Chỉ chứa logic xử lý dữ liệu, tính toán. Không được import `machine`, `network`.
- `hal.py`: Chứa các class/function điều khiển phần cứng. Phải có 2 phiên bản: `MockHAL` (cho Desktop) và `HardwareHAL` (cho ESP8266).

## 2. Quy tắc MicroPython
- Ưu tiên sử dụng thư viện chuẩn của MicroPython (ví dụ: `ujson` thay vì `json`, `utime` thay vì `time`).
- Tránh sử dụng các thư viện Python nặng (như `pandas`, `numpy`).
- Luôn giải phóng tài nguyên (đóng socket, file) để tránh tràn RAM trên ESP8266.

## 3. Workflow Phát triển
- Bước 1: Viết Logic trong `core.py`.
- Bước 2: Viết Mock trong `boot_desktop.py` để kiểm tra logic.
- Bước 3: Chỉ khi logic chạy đúng trên Desktop mới viết code phần cứng vào `hal.py` và `main.py`.

## 4. Đường dẫn Tuyệt đối
- Luôn sử dụng đường dẫn tuyệt đối khi yêu cầu thực hiện các lệnh terminal hoặc thao tác file.
```

---

### 3. Triển khai Workflow mẫu

#### Bước 1: Viết Logic (`src/app/core.py`)
```python
class SmartLightController:
    def __init__(self, hal):
        self.hal = hal

    def update(self, temp):
        if temp > 30:
            self.hal.set_led(True)
        else:
            self.hal.set_led(False)
```

#### Bước 2: Viết HAL và Mock (`src/app/hal.py`)
```python
try:
    import machine # Chỉ có trên ESP8266
    IS_HARDWARE = True
except ImportError:
    IS_HARDWARE = False

class HAL:
    def __init__(self):
        if IS_HARDWARE:
            self.led = machine.Pin(2, machine.Pin.OUT)
        else:
            self.led_state = False

    def set_led(self, state):
        if IS_HARDWARE:
            self.led.value(0 if state else 1) # ESP8266 đảo logic
        else:
            self.led_state = state
            print(f"[MOCK] LED is now: {'ON' if state else 'OFF'}")
```

#### Bước 3: Test trên Desktop (`src/boot_desktop.py`)
```python
from app.core import SmartLightController
from app.hal import HAL

hal = HAL()
app = SmartLightController(hal)

# Giả lập dữ liệu
print("Testing with temp 35...")
app.update(35)
print("Testing with temp 25...")
app.update(25)
```

---

### 4. Tự động hóa với `tasks.json`

Để upload nhanh lên ESP8266 mà không cần gõ lệnh, bạn nhấn `Ctrl+Shift+P` -> `Tasks: Configure Task` và thêm:

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "ESP8266: Upload All",
            "type": "shell",
            "command": "mpremote connect COM5 fs cp -r src/* :",
            "group": "build",
            "problemMatcher": []
        },
        {
            "label": "ESP8266: Soft Reset",
            "type": "shell",
            "command": "mpremote connect COM5 reset",
            "group": "test",
            "problemMatcher": []
        }
    ]
}
```
*(Lưu ý: Thay `COM5` bằng cổng thực tế của bạn. Fact: v06 - Section: Port Settings).*

---

### 5. Cách sử dụng Cursor hiệu quả với Workflow này

Khi bạn muốn thêm tính năng mới (ví dụ: đọc cảm biến độ ẩm), hãy chat với Cursor như sau:

> **User:** "Tôi muốn thêm tính năng đọc độ ẩm. Hãy cập nhật `core.py` để nếu độ ẩm > 80% thì nháy LED, cập nhật `hal.py` để có hàm `get_humidity()`. Sau đó viết code test vào `boot_desktop.py`."

**Tại sao cách này hiệu quả?**
1. **AI không bị loạn:** Nó biết rõ file nào chứa logic, file nào chứa phần cứng.
2. **Debug cực nhanh:** Bạn sửa lỗi logic trên Desktop chỉ mất 1 giây để chạy lại, thay vì mất 20 giây để upload lên mạch.
3. **An toàn:** Bạn không lo làm hỏng phần cứng nếu logic tính toán sai.

Bạn có muốn tôi viết file `main.py` hoàn chỉnh để kết nối tất cả lại và chạy trên ESP8266 không?

--------------------------------------------------
**TRÍCH XUẤT SỰ KIỆN (FACTS) - [vv06]**
- **Fact:** Để đặt số cổng COM gọn (COM5/COM6), truy cập Port Settings → Advanced → COM Port Number.
- **Source:** Dòng 1-2 trong DỮ LIỆU RAW.
- **Tag:** [vv06]

- **Fact:** ESP8266 có RAM hạn chế (khoảng 40KB heap), không phù hợp cho các chương trình quá nặng.
- **Source:** Section: Nhược điểm (MicroPython).
- **Tag:** [vv06]

- **Fact:** Việt Nam đã chính thức tắt sóng 2G từ ngày 16/10/2024.
- **Source:** Section: Dự án phát wifi từ sim.
- **Tag:** [vv06]

- **Fact:** ESP8266 không khuyến nghị làm hotspot Wi-Fi từ SIM do thiếu tài nguyên (RAM/throughput) và không có modem di động tích hợp.
- **Source:** Section: Vì sao không nên dùng ESP8266 cho hotspot 4G?.
- **Tag:** [vv06]
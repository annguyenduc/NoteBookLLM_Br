---
file_id: CONV_Atoms_atoms_v06_15
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v06 15

# Tài liệu Học tập: Workflow "Desktop-First" cho MicroPython trên Cursor IDE

## Thông tin chung

| Thuộc tính | Giá trị |
|------------|---------|
| Mã khóa học | MPY-DF-001 |
| Tên bài học | Workflow "Desktop-First" cho MicroPython |
| Mức độ | Trung cấp |
| Thời lượng | 90 phút |
| Đối tượng | Lập trình viên IoT, Kỹ sư phần mềm nhúng |

## Mục tiêu học tập

Sau khi hoàn thành bài học, học viên sẽ có thể:

- Thiết lập cấu trúc thư mục chuẩn cho dự án MicroPython theo mô hình tách biệt trách nhiệm
- Áp dụng mô hình HAL (Hardware Abstraction Layer) để phát triển code dễ bảo trì
- Sử dụng Cursor IDE hiệu quả với quy tắc phát triển MicroPython
- Triển khai workflow "desktop-first" để giảm thiểu lỗi và tăng tốc độ phát triển

## Nội dung bài học

### 1. Giới thiệu về Workflow "Desktop-First"

Workflow "Desktop-First" là phương pháp phát triển phần mềm nhúng cho phép lập trình viên viết và kiểm thử logic trên môi trường máy tính trước khi triển khai lên phần cứng thực tế. Phương pháp này đặc biệt hiệu quả khi làm việc với các vi điều khiển có tài nguyên giới hạn như ESP8266.

> **Lợi ích chính:**
> - Debug nhanh chóng (1 giây so với 20 giây upload lên mạch)
> - Giảm nguy cơ hỏng phần cứng do lỗi logic
> - Tận dụng tối đa khả năng hỗ trợ của AI trong quá trình phát triển

### 2. Cấu trúc thư mục chuẩn (Separation of Concerns)

Cấu trúc thư mục sau giúp tách biệt rõ ràng giữa logic ứng dụng và phần cứng:

```
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

### 3. Thiết lập Cursor Rules

File `.cursorrules` đóng vai trò như bản chỉ dẫn cho AI của Cursor để đảm bảo code được viết đúng kiến trúc:

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

### 4. Mô hình HAL (Hardware Abstraction Layer)

Mô hình HAL giúp tách biệt logic ứng dụng khỏi phần cứng cụ thể:

#### File `src/app/core.py`
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

#### File `src/app/hal.py`
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

### 5. Kiểm thử trên Desktop

#### File `src/boot_desktop.py`
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

### 6. Tự động hóa với VSCode Tasks

File `tasks.json` giúp tự động hóa quá trình upload lên ESP8266:

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

> **Lưu ý:** Thay `COM5` bằng cổng thực tế của bạn [vv06].

## Thực hành

### Bài tập 1: Thiết lập dự án mới

1. Tạo một thư mục dự án mới với cấu trúc thư mục như trên
2. Tạo file `.cursorrules` với nội dung đã cung cấp
3. Viết một lớp điều khiển đơn giản trong `core.py`
4. Tạo mock HAL trong `hal.py`
5. Viết script test trong `boot_desktop.py`

### Bài tập 2: Mở rộng chức năng

> **Yêu cầu:** Thêm tính năng đọc cảm biến độ ẩm vào ứng dụng

Chat với Cursor với câu lệnh:
> "Tôi muốn thêm tính năng đọc độ ẩm. Hãy cập nhật `core.py` để nếu độ ẩm > 80% thì nháy LED, cập nhật `hal.py` để có hàm `get_humidity()`. Sau đó viết code test vào `boot_desktop.py`."

## Kiến thức nền tảng

### Giới hạn phần cứng ESP8266

ESP8266 có RAM hạn chế (khoảng 40KB heap), không phù hợp cho các chương trình quá nặng [vv06]. Điều này ảnh hưởng đến lựa chọn thư viện và cách quản lý bộ nhớ trong ứng dụng.

### Kết nối phần cứng

Để đặt số cổng COM gọn (COM5/COM6), truy cập Port Settings → Advanced → COM Port Number [vv06].

## Đánh giá

### Câu hỏi trắc nghiệm

1. Mô hình HAL giúp đạt được lợi ích gì?
   - A. Tăng tốc độ xử lý
   - B. Tách biệt logic và phần cứng
   - C. Giảm kích thước code
   - D. Tăng dung lượng RAM

2. Workflow "Desktop-First" có lợi ích chính nào?
   - A. Giảm thời gian debug
   - B. Tăng tốc độ upload
   - C. Cải thiện chất lượng phần cứng
   - D. Giảm chi phí linh kiện

### Câu hỏi tự luận

1. Giải thích tại sao nên tách biệt logic ứng dụng và phần cứng trong dự án MicroPython?
2. Mô tả quy trình phát triển từ viết code đến chạy trên phần cứng theo workflow này?

## Tài nguyên bổ sung

- [Hướng dẫn đầy đủ về MicroPython](https://docs.micropython.org/)
- [Tài liệu Cursor IDE](https://cursor.sh/)
- [ESP8266 Technical Reference](https://www.espressif.com/en/products/socs/esp8266)

## Ghi chú quan trọng

- ESP8266 không khuyến nghị làm hotspot Wi-Fi từ SIM do thiếu tài nguyên (RAM/throughput) và không có modem di động tích hợp [vv06]
- Việt Nam đã chính thức tắt sóng 2G từ ngày 16/10/2024 [vv06], ảnh hưởng đến các dự án sử dụng kết nối di động cũ

---

**Nguồn tham khảo:** [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
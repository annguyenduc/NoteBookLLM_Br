---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v13_14
  title: CONV_atoms_v13_14
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** [CONV] Chip ESP8266EX hỗ trợ WiFi, sử dụng thạch anh (crystal) tần số 26MHz và có địa chỉ MAC định danh duy nhất (ví dụ: e8:db:84:e0:3a:f9).
- **Source:** [vv13] - Section: USER (Thông số từ esptool.py)
- **Tag:** [vv13]

- **Fact:** [CONV] Kích thước bộ nhớ Flash của ESP8266 có thể được tự động phát hiện bởi công cụ nạp, phổ biến là 4MB.
- **Source:** [vv13] - Section: USER (Thông số từ esptool.py)
- **Tag:** [vv13]

- **Fact:** [CONV] Để lập trình ESP8266 trên Arduino IDE, cần thêm URL `http://arduino.esp8266.com/stable/package_esp8266com_index.json` vào mục "Additional Boards Manager URLs" trong Preferences.
- **Source:** [vv13] - Section: ASSISTANT (Bước 1: Cài đặt ESP8266 trong Arduino IDE)
- **Tag:** [vv13]

- **Fact:** [CONV] Đèn LED tích hợp (LED_BUILTIN) trên các module ESP8266 (như NodeMCU) thường được kết nối với chân GPIO2.
- **Source:** [vv13] - Section: ASSISTANT (Bước 2: Viết chương trình Blink LED)
- **Tag:** [vv13]

- **Fact:** [CONV] MicroPython là một lựa chọn để lập trình ESP8266 bằng ngôn ngữ Python, yêu cầu nạp firmware định dạng `.bin` vào địa chỉ `0x00000`.
- **Source:** [vv13] - Section: ASSISTANT (Bước 1: Cài đặt MicroPython trên ESP8266)
- **Tag:** [vv13]

- **Fact:** [CONV] Tốc độ Baud (Baud rate) tiêu chuẩn để giao tiếp với giao diện dòng lệnh REPL của MicroPython trên ESP8266 là 115200.
- **Source:** [vv13] - Section: ASSISTANT (Bước 2: Kết nối với ESP8266 qua REPL)
- **Tag:** [vv13]

- **Fact:** [CONV] Thư viện `pyserial` (cài đặt qua `pip install pyserial`) cho phép các ứng dụng Python trên máy tính giao tiếp với ESP8266 qua cổng Serial.
- **Source:** [vv13] - Section: ASSISTANT (Bước 2: Cài đặt các công cụ để giao tiếp với ESP8266)
- **Tag:** [vv13]

- **Fact:** [CONV] Công cụ `mpremote` được sử dụng để tương tác với thiết bị chạy MicroPython, hỗ trợ các lệnh như tạo thư mục (`mkdir`) và sao chép file (`cp`) vào bộ nhớ của chip.
- **Source:** [vv13] - Section: ASSISTANT (Bước 4: Lưu chương trình vào ESP8266)
- **Tag:** [vv13]

- **Fact:** [CONV] Lệnh `esptool.py --port <PORT> erase_flash` được khuyến nghị để xóa sạch dữ liệu cũ trên bộ nhớ flash trước khi nạp firmware mới nhằm tránh lỗi xung đột.
- **Source:** [vv13] - Section: ASSISTANT (Bước 1: Cài đặt MicroPython trên ESP8266 - nạp lại)
- **Tag:** [vv13]

- **Fact:** [CONV] Trong MicroPython, thư viện `machine` cung cấp các lớp như `Pin` để điều khiển phần cứng (ví dụ: `machine.Pin(2, machine.Pin.OUT)` để cấu hình chân GPIO2 làm đầu ra).
- **Source:** [vv13] - Section: ASSISTANT (Bước 3: Viết chương trình đơn giản)
- **Tag:** [vv13]

- **Fact:** [CONV] File `main.py` là file chương trình chính mà MicroPython sẽ tự động thực thi mỗi khi chip ESP8266 khởi động.
- **Source:** [vv13] - Section: ASSISTANT (Bước 4: Lưu chương trình vào ESP8266)
- **Tag:** [vv13]

- **Fact:** [CONV] Các phần mềm Terminal phổ biến để giao tiếp Serial với vi điều khiển bao gồm PuTTY, Termite (Windows) và lệnh `screen` (Linux/macOS).
- **Source:** [vv13] - Section: ASSISTANT (Bước 1: Cài đặt phần mềm giao tiếp với ESP8266)
- **Tag:** [vv13]
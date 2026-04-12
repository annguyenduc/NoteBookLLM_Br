Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu cung cấp về IoT và ESP8266:

- **Fact:** Chip ESP8266EX có các tính năng tích hợp bao gồm WiFi, sử dụng thạch anh (Crystal) 26MHz và thường đi kèm với bộ nhớ Flash 4MB.
- **Source:** [USER] - Thông báo từ esptool.py v4.8.1.
- **Tag:** [vv13]

- **Fact:** Để nạp firmware cho ESP8266 qua dòng lệnh khi hệ thống không nhận diện trực tiếp script, có thể sử dụng cú pháp: `python -m esptool --port [Tên_Cổng_COM] write_flash [Địa_chỉ] [Đường_dẫn_file_bin]`.
- **Source:** [ASSISTANT] - Hướng dẫn khắc phục lỗi 'esptool.py' is not recognized.
- **Tag:** [vv13]

- **Fact:** Tốc độ Baud (Baud rate) chuẩn để giao tiếp với MicroPython REPL trên ESP8266 là 115200 bps.
- **Source:** [ASSISTANT] - Bước 2: Kết nối với ESP8266 qua REPL.
- **Tag:** [vv13]

- **Fact:** Thư viện `machine` trong MicroPython được sử dụng để điều khiển các chân GPIO của ESP8266, ví dụ: `led = machine.Pin(2, machine.Pin.OUT)`.
- **Source:** [ASSISTANT] - Bước 3: Viết chương trình đơn giản (Nháy đèn LED).
- **Tag:** [vv13]

- **Fact:** Chân LED tích hợp (Built-in LED) trên nhiều module ESP8266 thường được kết nối với chân GPIO2 (tương ứng với Pin 2 trong MicroPython).
- **Source:** [ASSISTANT] - Bước 3: Viết chương trình đơn giản (Nháy đèn LED).
- **Tag:** [vv13]

- **Fact:** Công cụ `mpremote` được sử dụng để tương tác, tạo thư mục và sao chép file (như `main.py`) từ máy tính lên board mạch chạy MicroPython.
- **Source:** [ASSISTANT] - Bước 4: Lưu chương trình vào ESP8266.
- **Tag:** [vv13]

- **Fact:** Trước khi nạp firmware mới cho ESP8266, nên thực hiện lệnh `erase_flash` để xóa sạch dữ liệu cũ trong bộ nhớ.
- **Source:** [ASSISTANT] - Bước 1: Cài đặt MicroPython trên ESP8266.
- **Tag:** [vv13]

- **Fact:** Các phần mềm phổ biến để kết nối Serial Terminal với ESP8266 trên Windows bao gồm PuTTY, Termite và Tera Term.
- **Source:** [ASSISTANT] - Bước 1: Cài đặt phần mềm giao tiếp với ESP8266 (REPL).
- **Tag:** [vv13]

- **Fact:** Lỗi "Errno 2: No such file or directory" khi dùng esptool xảy ra khi đường dẫn tệp firmware .bin không chính xác hoặc tệp không nằm trong thư mục làm việc hiện tại.
- **Source:** [ASSISTANT] - Hướng dẫn khắc phục lỗi argument <address> <filename>.
- **Tag:** [vv13]

- **Fact:** Để đưa ESP8266 vào chế độ nạp (Flash mode), người dùng có thể cần nhấn giữ nút **Boot** trong khi nhấn nút **Reset**, sau đó thả nút Boot.
- **Source:** [ASSISTANT] - Mục 3: Đã Reset ESP8266 (Phần giải quyết PuTTY không hiển thị).
- **Tag:** [vv13]
Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp về quy trình làm việc với ESP8266 và MicroPython:

- Fact: [CONV] Firmware MicroPython dành cho ESP8266 được tải chính thức từ địa chỉ micropython.org/download.
- Source: (v13 - Section: 1.4. Cài đặt firmware MicroPython)
- Tag: [vv13]

- Fact: [CONV] Công cụ `esptool` được sử dụng để xóa bộ nhớ flash của ESP8266 thông qua lệnh `erase_flash` trước khi nạp firmware mới.
- Source: (v13 - Section: 1.4. Cài đặt firmware MicroPython)
- Tag: [vv13]

- Fact: [CONV] Lệnh nạp firmware MicroPython vào ESP8266 yêu cầu xác định cổng COM, tốc độ baud (khuyến nghị 460800), tự động phát hiện kích thước flash và ghi vào địa chỉ bắt đầu là 0.
- Source: (v13 - Section: 1.4. Cài đặt firmware MicroPython)
- Tag: [vv13]

- Fact: [CONV] Để lập trình MicroPython trên VSCode, cần cài đặt các extension: Python (hỗ trợ ngôn ngữ), Pymakr (giao tiếp thiết bị) và Serial Port.
- Source: (v13 - Section: 1.5. Cài đặt plugin VSCode)
- Tag: [vv13]

- Fact: [CONV] File cấu hình `pymakr.conf` trong VSCode dùng để thiết lập địa chỉ kết nối, thư mục đồng bộ và các loại tệp tin được phép tải lên board (py, txt, json, html, js...).
- Source: (v13 - Section: 2. Kết nối ESP8266 với VSCode)
- Tag: [vv13]

- Fact: [CONV] Trong MicroPython, thư viện `machine` dùng để điều khiển các chân GPIO (như Pin 2 cho LED), và thư viện `network` dùng để cấu hình WiFi (STA_IF hoặc AP_IF).
- Source: (v13 - Section: 3. Code Python trên VSCode)
- Tag: [vv13]

- Fact: [CONV] Một máy chủ web cơ bản trên ESP8266 có thể được khởi tạo bằng thư viện `socket`, lắng nghe trên cổng 80 để nhận các yêu cầu HTTP điều khiển thiết bị.
- Source: (v13 - Section: 3. Code Python trên VSCode)
- Tag: [vv13]

- Fact: [CONV] Tệp mã nguồn chính để ESP8266 tự động thực thi khi khởi động phải được đặt tên là `main.py`.
- Source: (v13 - Section: 4. Nạp mã vào ESP8266)
- Tag: [vv13]

- Fact: [CONV] Khi sử dụng PowerShell trên Windows, việc bao bọc tên cổng COM trong dấu `< >` (ví dụ: `<COM32>`) sẽ gây lỗi cú pháp vì đây là ký tự dành riêng cho việc chuyển hướng (redirection).
- Source: [Unverified_Source] (Dựa trên lỗi thực tế của người dùng trong hội thoại)
- Tag: [vv13]

- Fact: [CONV] Nếu hệ thống không nhận diện lệnh trực tiếp `esptool.py`, người dùng có thể thực thi thông qua module Python bằng cú pháp `python -m esptool`.
- Source: [Unverified_Source] (Dựa trên giải pháp khắc phục trong hội thoại)
- Tag: [vv13]

- Fact: [CONV] Để nạp firmware thành công, đôi khi cần nhấn và giữ nút BOOT hoặc FLASH trên board ESP8266 trong khi thực hiện lệnh nạp để đưa chip vào chế độ nạp (Flash Mode).
- Source: [Unverified_Source] (Dựa trên hướng dẫn khắc phục sự cố trong hội thoại)
- Tag: [vv13]
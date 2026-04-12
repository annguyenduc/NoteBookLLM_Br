Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v06):

- **Fact:** [CONV] Kiến trúc phần mềm cho IoT/MicroPython nên tách biệt rõ ràng giữa "Logic thuần Python" (Core) và "Lớp trừu tượng phần cứng" (HAL) để có thể kiểm thử (test) và chạy giả lập trên Desktop trước khi nạp xuống thiết bị.
- **Source:** [vv06] - Section: Rules cho Cursor IDE – file .cursorrules (Goals)
- **Tag:** [vv06]

- **Fact:** [CONV] Lớp `ESPHAL` dành cho ESP8266 sử dụng module `machine` để điều khiển phần cứng và `time.sleep_ms` để tạo độ trễ, thay vì dùng `time.sleep` tiêu chuẩn của Python.
- **Source:** [vv06] - Section: app/hal/esp_hal.py (ESP8266)
- **Tag:** [vv06]

- **Fact:** [CONV] Trên board ESP8266, LED tích hợp (thường gắn với GPIO2) thường hoạt động theo logic đảo: xuất mức thấp (0) để bật LED và mức cao (1) để tắt LED.
- **Source:** [vv06] - Section: app/hal/esp_hal.py (ESP8266) - dòng `self.led.value(1) # tắt mặc định (ESP đảo logic)`
- **Tag:** [vv06]

- **Fact:** [CONV] Sử dụng `typing.Protocol` hoặc `abc.ABC` cho phép định nghĩa giao diện (interface) cho phần cứng, giúp hàm xử lý logic có thể nhận vào bất kỳ đối tượng HAL nào (thật hoặc giả lập) mà không bị phụ thuộc vào thư viện phần cứng cụ thể.
- **Source:** [vv06] - Section: app/core/controller.py & app/hal/base.py
- **Tag:** [vv06]

- **Fact:** [CONV] Công cụ `mpremote` được sử dụng để tương tác với thiết bị chạy MicroPython, hỗ trợ các lệnh như `mip install` để cài thư viện, `fs cp` để sao chép file/thư mục và `reset` để khởi động lại board.
- **Source:** [vv06] - Section: .vscode/tasks.json - Task "Upload (mpremote)"
- **Tag:** [vv06]

- **Fact:** [CONV] Trong lập trình MicroPython, cần hạn chế việc cấp phát bộ nhớ (allocation) bên trong các vòng lặp để giảm thiểu tần suất hoạt động của trình dọn rác (Garbage Collector - GC), giúp hệ thống hoạt động ổn định hơn.
- **Source:** [vv06] - Section: Rules cho Cursor IDE - MicroPython Constraints
- **Tag:** [vv06]

- **Fact:** [CONV] File cấu hình `.cursorrules` trong Cursor IDE giúp định hướng AI ưu tiên các quy tắc thiết kế như: không import các thư viện đặc thù của MicroPython (`machine`, `network`, `uasyncio`) vào các module logic thuần túy.
- **Source:** [vv06] - Section: Rules cho Cursor IDE – file .cursorrules (Coding Guidelines)
- **Tag:** [vv06]

- **Fact:** [CONV] Quy trình phát triển "Desktop-first" cho IoT bao gồm: Viết logic -> Chạy giả lập với MockHAL -> Chạy Unit Test với PyTest -> Nạp code lên thiết bị thật qua mpremote.
- **Source:** [vv06] - Section: Quy trình hằng ngày (tóm tắt)
- **Tag:** [vv06]
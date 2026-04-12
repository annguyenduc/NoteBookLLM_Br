Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** [CONV] Có hai cách để kết nối JavaScript với Arduino UNO: Cách 1 sử dụng Blockly (qua app.ohstem.vn) và Cách 2 nạp trực tiếp code MicroPython/Arduino để chạy webserver trên UNO (không dùng block).
- **Source:** [v01 - Section: Cách 2 (JS đẩy thẳng vào UNO)]
- **Tag:** [vv01]

- **Fact:** [CONV] Để chống lag và nhấp nháy cho thiết bị IoT, nên sử dụng cơ chế debounce (chỉ đổi trạng thái khi 3–5 khung liên tiếp cùng nhãn) và duy trì chu kỳ UNO GET ≥ 300ms.
- **Source:** [v01 - Section: Gợi ý chống lag/nhấp nháy]
- **Tag:** [vv01]

- **Fact:** [CONV] ESP8266 là vi điều khiển tích hợp Wi-Fi 2.4GHz, sử dụng CPU 32-bit Tensilica (80–160 MHz), RAM khả dụng khoảng 50KB và Flash từ 512KB đến 4MB.
- **Source:** [v01 - Section: ⚙️ 1. ESP8266 là gì?]
- **Tag:** [vv01]

- **Fact:** [CONV] Khi sử dụng ESP8266, không nên dùng các chân D0, D3, D4 cho cảm biến khởi động vì chúng ảnh hưởng đến quá trình boot của vi điều khiển.
- **Source:** [v01 - Section: ⚠️ 5. Lưu ý khi dùng ESP8266 cho IoT]
- **Tag:** [vv01]

- **Fact:** [CONV] Yolo UNO (sử dụng chip ESP32-S3) được khuyến nghị sử dụng thay thế cho ESP8266 trong các dự án IoT lớn yêu cầu camera hoặc nhiều cảm biến.
- **Source:** [v01 - Section: ⚠️ 5. Lưu ý khi dùng ESP8266 cho IoT]
- **Tag:** [vv01]

- **Fact:** [CONV] Để ổn định hệ thống MQTT khi có nhiều thiết bị, nên giới hạn tần suất gửi dữ liệu tối đa 1 bản tin/giây/thiết bị và gom nhiều dữ liệu cảm biến vào một gói JSON.
- **Source:** [v01 - Section: 1) Giảm “bão” dữ liệu từ thiết bị]
- **Tag:** [vv01]

- **Fact:** [CONV] Cơ chế "Exponential Backoff" (tăng dần thời gian chờ: 1s → 2s → 4s... tối đa 32s) giúp tránh tình trạng "reconnect storm" khi thiết bị IoT mất kết nối mạng.
- **Source:** [v01 - Section: 2) MQTT cấu hình “chống nghẽn”]
- **Tag:** [vv01]

- **Fact:** [CONV] ThingsBoard bản Community Edition là nền tảng IoT mã nguồn mở cho phép tự host miễn phí, hỗ trợ các giao thức MQTT, HTTP và CoAP.
- **Source:** [v01 - Section: Top 5 nền tảng IoT]
- **Tag:** [vv01]

- **Fact:** [CONV] AWS IoT Core cung cấp gói miễn phí (Free tier) cho phép gửi 250,000 bản tin mỗi tháng trong vòng 12 tháng đầu tiên.
- **Source:** [v01 - Section: Top 5 nền tảng IoT]
- **Tag:** [vv01]

- **Fact:** [CONV] Lỗi widget "Text Log" (ô cam) trên OhStem hiển thị liên tục nhiều dòng thường do lệnh publish dữ liệu được đặt trong vòng lặp Timer có chu kỳ quá ngắn (ví dụ 300ms).
- **Source:** [v01 - Section: Conversation: Khắc phục ô cam liên tục]
- **Tag:** [vv01]

- **Fact:** [CONV] Sử dụng biến cờ "booting" kết hợp với Timer khoảng 1 giây khi khởi động giúp thiết bị IoT bỏ qua các bản tin cũ (retained messages) từ broker, tránh gây nhiễu hệ thống.
- **Source:** [v01 - Section: B. Bỏ qua “đợt bản tin đầu” khi boot]
- **Tag:** [vv01]

- **Fact:** [CONV] Đối với các dự án điều khiển Servo hoặc động cơ, nên thêm thời gian "giữ tối thiểu" từ 1–2 giây sau mỗi lần chuyển trạng thái để đảm bảo độ bền và ổn định.
- **Source:** [v01 - Section: Gợi ý chống lag/nhấp nháy]
- **Tag:** [vv01]
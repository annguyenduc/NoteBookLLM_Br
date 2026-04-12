---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_11
  title: CONV_atoms_v06_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v06:

- **Fact:** [CONV] Thời khóa biểu STEM cho các lớp từ C01 đến C17 được sắp xếp từ Thứ 2 đến Thứ 6, đảm bảo mỗi tiết chỉ có một lớp học duy nhất, không trùng lặp khung thời gian.
- **Source:** [vv06] - Section: Thời khóa biểu STEM (sắp xếp theo thứ)
- **Tag:** [vv06]

- **Fact:** [CONV] ESP8266 không phù hợp để brute force mật khẩu Wi-Fi do CPU yếu (80–160 MHz), RAM hạn chế (~50 KB khả dụng) và firmware không thiết kế cho mục đích tấn công bảo mật.
- **Source:** [vv06] - Section: Conversation: ESP8266 brute force khả thi không
- **Tag:** [vv06]

- **Fact:** [CONV] ESP8266 chỉ hỗ trợ Wi-Fi băng tần 2.4 GHz (chuẩn 802.11 b/g/n), không hỗ trợ 5 GHz.
- **Source:** [vv06] - Section: Phát wifi hotspot tốc độ như thế nào
- **Tag:** [vv06]

- **Fact:** [CONV] Tốc độ phát Wi-Fi hotspot thực tế của ESP8266 thường chỉ đạt 1–5 Mbps và trở nên không ổn định khi có trên 5–8 thiết bị kết nối đồng thời.
- **Source:** [vv06] - Section: Phát wifi hotspot tốc độ như thế nào
- **Tag:** [vv06]

- **Fact:** [CONV] ESP32 hỗ trợ tốc độ Wi-Fi hotspot thực tế cao hơn ESP8266 (khoảng 10–20 Mbps) và xử lý nhiều client ổn định hơn.
- **Source:** [vv06] - Section: Phát wifi hotspot tốc độ như thế nào
- **Tag:** [vv06]

- **Fact:** [CONV] Các dự án Wi-Fi hợp pháp trên ESP8266 bao gồm: Wi-Fi Analyzer (đo RSSI), Captive Portal để cấu hình thiết bị, Data Logger gửi dữ liệu lên Cloud (MQTT, Thingspeak), và ESP-NOW để giao tiếp P2P giữa các vi điều khiển.
- **Source:** [vv06] - Section: Có gì hay ho hơn không? Ví dụ như kích hoặc làm nhiễu sóng wifi
- **Tag:** [vv06]

- **Fact:** [CONV] Lộ trình học MicroPython cho ESP8266 bao gồm các bước: Flash firmware, điều khiển GPIO (LED/Nút nhấn), PWM, Timer/Interrupt, kết nối Wi-Fi, giao thức HTTP/MQTT, và xây dựng Web Server.
- **Source:** [vv06] - Section: Prompt: “ESP8266 Study Buddy”
- **Tag:** [vv06]

- **Fact:** [CONV] Workflow phát triển MicroPython tối ưu gồm 4 bước: (1) Mock logic trên desktop, (2) Test trên PC, (3) Đóng gói file (boot.py, main.py, config.py), (4) Nạp và kiểm thử thực tế bằng công cụ như `mpremote`.
- **Source:** [vv06] - Section: Prompt: “ESP8266 Study Buddy” & Nếu tôi muốn dùng trên cursor ide
- **Tag:** [vv06]

- **Fact:** [CONV] LED on-board trên nhiều dòng ESP8266 (như NodeMCU/Wemos D1 mini) thường được kết nối với chân GPIO2 (D4) và hoạt động theo cơ chế active-LOW (mức 0 là BẬT, mức 1 là TẮT).
- **Source:** [vv06] - Section: Bài 1: Flash MicroPython & chớp LED trên ESP8266
- **Tag:** [vv06]

- **Fact:** [CONV] Công cụ `esptool.py` được sử dụng để xóa flash và nạp firmware MicroPython, trong khi `mpremote` được ưu tiên để quản lý file và truy cập REPL trên ESP8266.
- **Source:** [vv06] - Section: Bài 1: Flash MicroPython & chớp LED trên ESP8266
- **Tag:** [vv06]

- **Fact:** [CONV] Để giả lập phần cứng ESP8266 trên máy tính (Mocking), có thể tạo các lớp Python giả lập (class Pin, PWM, Timer) để kiểm tra logic code trước khi nạp vào thiết bị thật.
- **Source:** [vv06] - Section: Nếu tôi muốn dùng trên cursor ide - src/desktop/hw_mock.py
- **Tag:** [vv06]
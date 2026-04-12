---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_15
  title: atoms_v14_15
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là danh sách các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v14 về chủ đề IoT, Arduino và Robotics:

- **Fact:** Mã PIN mặc định để ghép đôi với module Bluetooth HC-05 hoặc HC-06 thường là `1234` hoặc `0000`.
- **Source:** [v14 - Section: Ghép đôi Bluetooth]
- **Tag:** [vv14]

- **Fact:** Giá trị ngưỡng (threshold) để điều chỉnh joystick trong mã nguồn thường nằm trong khoảng 400 và 600 để phù hợp với thiết bị.
- **Source:** [v14 - Section: Kiểm tra tín hiệu (mục 3)]
- **Tag:** [vv14]

- **Fact:** Một bộ tay cầm điều khiển xe robot cơ bản sử dụng Arduino thường bao gồm: Arduino Uno/Nano, Joystick module, nút nhấn, module Bluetooth HC-05, và điện trở 10kΩ.
- **Source:** [v14 - Section: 1. Tay cầm điều khiển]
- **Tag:** [vv14]

- **Fact:** Các module điều khiển động cơ (Motor Driver) phổ biến cho xe robot là L298N hoặc L293D, có khả năng điều khiển từ 2 đến 4 động cơ DC.
- **Source:** [v14 - Section: 2. Xe điều khiển]
- **Tag:** [vv14]

- **Fact:** Module ESP8266 tích hợp sẵn kết nối Wi-Fi nhưng không có chip Bluetooth tích hợp bên trong.
- **Source:** [v14 - Section: ESP8266 có chip kết nối bluetooth hay sao?]
- **Tag:** [vv14]

- **Fact:** ESP32 là phiên bản nâng cấp của ESP8266, hỗ trợ đồng thời cả kết nối Wi-Fi và Bluetooth (bao gồm Classic và BLE).
- **Source:** [v14 - Section: Sử dụng ESP32 thay vì ESP8266]
- **Tag:** [vv14]

- **Fact:** ESP8266 có thể truyền dữ liệu không dây qua Wi-Fi bằng các giao thức như HTTP, UDP hoặc WebSocket.
- **Source:** [v14 - Section: Hướng dẫn giao tiếp qua Wi-Fi]
- **Tag:** [vv14]

- **Fact:** Module Bluetooth HC-05 có thể thiết lập hoạt động ở cả hai chế độ Master (chủ) và Slave (phụ), trong khi HC-06 chỉ có thể hoạt động ở chế độ Slave.
- **Source:** [v14 - Section: Cách sử dụng HC-05 và HC-06 cùng nhau]
- **Tag:** [vv14]

- **Fact:** Để cấu hình module HC-05 bằng lệnh AT (AT Command), cần kết nối chân KEY lên mức cao (3.3V) và sử dụng tốc độ Baud rate là 38400.
- **Source:** [v14 - Section: 3. Cấu hình module Bluetooth HC-05]
- **Tag:** [vv14]

- **Fact:** Khi kết nối chân RX của module Bluetooth với các vi điều khiển có mức điện áp khác biệt, cần sử dụng mạch chia điện áp (voltage divider) để bảo vệ module.
- **Source:** [v14 - Section: Sơ đồ kết nối phần cứng (ESP8266 + HC-05)]
- **Tag:** [vv14]

- **Fact:** Module NRF24L01 là một giải pháp giao tiếp RF không dây có độ trễ thấp và tầm xa từ 10m đến 100m.
- **Source:** [v14 - Section: 2. Giao tiếp qua giao thức NRF24L01]
- **Tag:** [vv14]

- **Fact:** Công nghệ LoRa (module SX1278) cho phép truyền tín hiệu điều khiển ở khoảng cách rất xa, từ 1km đến 5km trong môi trường mở.
- **Source:** [v14 - Section: 4. Giao tiếp qua LoRa (tầm xa)]
- **Tag:** [vv14]

- **Fact:** ESP8266 có thể hoạt động ở chế độ Access Point (AP) để tự tạo một mạng Wi-Fi hotspot cho các thiết bị khác kết nối vào.
- **Source:** [v14 - Section: Hướng dẫn giao tiếp qua Wi-Fi]
- **Tag:** [vv14]
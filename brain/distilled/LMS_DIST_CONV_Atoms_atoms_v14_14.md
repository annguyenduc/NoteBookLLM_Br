---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_14
  title: atoms_v14_14
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v14 về IoT, Arduino và Robotics:

- **Fact:** Các mô-đun GSM phổ biến như SIM800, SIM900 hoặc Quectel có tuổi thọ linh kiện trung bình từ 5 đến 10 năm nếu hoạt động trong môi trường tiêu chuẩn.
- **Source:** [vv14] - Section: 1. Chất lượng phần cứng và linh kiện (GSM Modules).
- **Tag:** [vv14]

- **Fact:** Hệ thống GSM tự chế yêu cầu nguồn cấp điện ổn định trong khoảng DC 5V-12V; nguồn điện không ổn định là nguyên nhân chính gây hỏng mô-đun GSM.
- **Source:** [vv14] - Section: 1. Phần cứng của hệ thống GSM (b. Bộ nguồn).
- **Tag:** [vv14]

- **Fact:** Để điều khiển động cơ DC cho xe robot Arduino, các mạch điều khiển (Motor Driver) phổ biến được sử dụng là L298N hoặc L293D.
- **Source:** [vv14] - Section: 1. Phần cứng cần thiết (Xe Bluetooth).
- **Tag:** [vv14]

- **Fact:** Trong giao tiếp không dây cho Robot, Module Bluetooth HC-05/HC-06 kết nối với Arduino qua các chân RX và TX (giao thức Serial).
- **Source:** [vv14] - Section: 4. Sơ đồ kết nối cơ bản (Xe Bluetooth).
- **Tag:** [vv14]

- **Fact:** Module Joystick 2 trục hoạt động bằng cách gửi tín hiệu Analog đến Arduino: trục X (ngang) kết nối chân A0 và trục Y (dọc) kết nối chân A1 để điều hướng robot.
- **Source:** [vv14] - Section: 3. Sơ đồ kết nối tay cầm (Gamepad controller).
- **Tag:** [vv14]

- **Fact:** Thư viện `AFMotor.h` thường được sử dụng trong lập trình Arduino để điều khiển các cổng động cơ (M1, M2, M3, M4) trên Motor Shield.
- **Source:** [vv14] - Section: 5. Chương trình cơ bản cho Arduino (Xe Bluetooth).
- **Tag:** [vv14]

- **Fact:** Module RF NRF24L01 là giải pháp thay thế Bluetooth khi cần khoảng cách truyền tín hiệu điều khiển xa hơn trong các ứng dụng Robotics.
- **Source:** [vv14] - Section: 1. Module RF (NRF24L01) hoặc Bluetooth (HC-05).
- **Tag:** [vv14]

- **Fact:** Chi phí đầu tư ban đầu cho một hệ thống IoT GSM cơ bản (bao gồm Raspberry Pi, mô-đun GSM, nguồn và vỏ bảo vệ) ước tính khoảng 2.500.000 VND.
- **Source:** [vv14] - Section: Chi phí đầu tư ban đầu (Bảng kê).
- **Tag:** [vv14]

- **Fact:** Để giám sát môi trường cho thiết bị IoT, các cảm biến nhiệt độ và độ ẩm được tích hợp để theo dõi và bảo vệ linh kiện khỏi sự thay đổi nhiệt độ đột ngột.
- **Source:** [vv14] - Section: 1. Phần cứng của hệ thống GSM (e. Cảm biến nhiệt độ và độ ẩm).
- **Tag:** [vv14]

- **Fact:** Trong lập trình IoT trên máy tính nhúng (như Raspberry Pi), thư viện Python `PySerial` được sử dụng để giao tiếp với các mô-đun phần cứng qua cổng nối tiếp.
- **Source:** [vv14] - Section: 2. Phần mềm và Cấu hình (a. Phần mềm điều khiển).
- **Tag:** [vv14]
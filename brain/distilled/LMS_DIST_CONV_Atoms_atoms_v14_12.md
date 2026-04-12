---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_12
  title: atoms_v14_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v14) về IoT, Arduino, và Robotics:

- **Fact:** Thư viện `SoftwareSerial` được sử dụng trên Arduino để thiết lập giao tiếp Serial với các module Bluetooth như HC-06 hoặc HC-05 thông qua các chân kỹ thuật số (ví dụ: chân 10 là RX, chân 11 là TX).
- **Source:** [vv14] - Section: 4. Giao tiếp Bluetooth với HC-06 (Code snippet).
- **Tag:** [vv14]

- **Fact:** Tốc độ Baud mặc định thường dùng để giao tiếp giữa Arduino và module HC-06/HC-05 là 9600.
- **Source:** [vv14] - Section: 4. Giao tiếp Bluetooth với HC-06 & Section: 7. Kiểm tra với Serial Monitor.
- **Tag:** [vv14]

- **Fact:** Để đưa module HC-06 vào chế độ AT nhằm thay đổi cấu hình (tên, mật khẩu), người dùng cần ngắt kết nối Bluetooth, đưa chân EN (Enable) xuống mức LOW (nối với GND) và khởi động lại module.
- **Source:** [vv14] - Section: 1. Chuyển HC-06 sang chế độ AT.
- **Tag:** [vv14]

- **Fact:** Lệnh AT để thay đổi mật khẩu trên module Bluetooth là `AT+PSWD=xxxx` và lệnh thay đổi tên là `AT+NAME=NewName`.
- **Source:** [vv14] - Section: 2. Sử dụng lệnh AT để thay đổi mật khẩu.
- **Tag:** [vv14]

- **Fact:** Module Bluetooth (HC-05/HC-06) có hai chế độ hoạt động tách biệt: Chế độ AT (AT Command Mode) để cấu hình và Chế độ kết nối (Connected Mode) để truyền dữ liệu; lệnh AT không hoạt động khi module đang ở chế độ kết nối.
- **Source:** [vv14] - Section: KHI KẾT NỐI BLUETOOTH THÌ CÁC CÂU LỆNH AT KHÔNG DÙNG ĐƯỢC SAO.
- **Tag:** [vv14]

- **Fact:** Hệ thống nhận và báo mã OTP có thể được xây dựng bằng module GSM (SIM800L hoặc SIM900A) kết hợp với vi điều khiển như ESP32 hoặc Arduino.
- **Source:** [vv14] - Section: Hệ thống nhận OTP - Phần cứng cần thiết.
- **Tag:** [vv14]

- **Fact:** Module SIM800L yêu cầu nguồn cấp ổn định với dòng điện tức thời lên đến 2A khi phát tín hiệu và nên sử dụng thêm tụ lọc (khoảng 1000µF) để tránh nhiễu.
- **Source:** [vv14] - Section: Phần cứng mở rộng & Phần cứng (hệ thống 24/24).
- **Tag:** [vv14]

- **Fact:** ESP32 được khuyến nghị cho các dự án IoT phức tạp vì hỗ trợ nhiều cổng UART phần cứng (HardwareSerial), cho phép giao tiếp đồng thời với nhiều module GSM.
- **Source:** [vv14] - Section: Phần cứng mở rộng - Mục 2.
- **Tag:** [vv14]

- **Fact:** Để đảm bảo hệ thống IoT hoạt động ổn định 24/24, cần thiết lập cơ chế tự khởi động lại định kỳ và sử dụng Watchdog Timer để reset hệ thống khi phát hiện treo phần mềm.
- **Source:** [vv14] - Section: Phần mềm (hệ thống 24/24) - Mục 2.
- **Tag:** [vv14]

- **Fact:** Các modem GSM công nghiệp như Teltonika TRM240/TRM250 thường có vỏ nhôm bền bỉ, hỗ trợ các chuẩn LTE Cat 1, NB-IoT và được thiết kế cho môi trường vận hành khắc nghiệt.
- **Source:** [vv14] - Section: HÃY CHO TÔI BIẾT GIÁ CỦA MODEM GSM CÔNG NGHIỆP.
- **Tag:** [vv14]

- **Fact:** Hầu hết các modem GSM công nghiệp phổ thông chỉ hỗ trợ 1 SIM hoạt động tại một thời điểm; để dùng nhiều SIM đồng thời (từ 4 đến 32 SIM), cần sử dụng thiết bị chuyên dụng gọi là GSM Gateway.
- **Source:** [vv14] - Section: Ghi chú (Bảng danh sách modem).
- **Tag:** [vv14]
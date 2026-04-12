---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v14_12
  title: CONV_atoms_v14_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được chưng cất từ nguồn dữ liệu **Volume v14** liên quan đến IoT, Arduino và hệ thống GSM:

### 1. Bluetooth Module (HC-05 & HC-06)
- **Fact:** [CONV] Để truy cập chế độ lệnh AT trên module HC-06 nhằm thay đổi cấu hình, người dùng cần đưa chân EN (Enable) xuống mức LOW (nối với GND) và khởi động lại thiết bị.
- **Source:** [vv14] - Section: 1. Chuyển HC-06 sang chế độ AT.
- **Tag:** [vv14]

- **Fact:** [CONV] Module HC-05 và HC-06 không thể nhận lệnh AT khi đang ở chế độ kết nối (Connected Mode) với điện thoại; thiết bị phải được ngắt kết nối và đưa về chế độ AT chuyên biệt.
- **Source:** [vv14] - Section: Chế độ AT vs Chế độ kết nối Bluetooth.
- **Tag:** [vv14]

- **Fact:** [CONV] Để vào chế độ AT trên HC-05, cần giữ chân Key (hoặc chân EN) ở mức HIGH trong quá trình khởi động module.
- **Source:** [vv14] - Section: Chế độ AT (AT Command Mode).
- **Tag:** [vv14]

- **Fact:** [CONV] Cấu hình SoftwareSerial phổ biến để giao tiếp với module Bluetooth trên Arduino là sử dụng chân 10 (RX) và chân 11 (TX) với tốc độ baud mặc định thường là 9600.
- **Source:** [vv14] - Section: 4. Kiểm Tra Mã Arduino.
- **Tag:** [vv14]

### 2. Hệ thống GSM & OTP
- **Fact:** [CONV] Module GSM SIM800L yêu cầu dòng điện tức thời lên đến 2A khi phát tín hiệu; việc thiếu hụt dòng điện là nguyên nhân phổ biến gây mất ổn định hệ thống.
- **Source:** [vv14] - Section: 3. Nguồn cấp phù hợp (Phần cứng mở rộng).
- **Tag:** [vv14]

- **Fact:** [CONV] Vi điều khiển ESP32 được ưu tiên cho các hệ thống nhận OTP đa SIM vì hỗ trợ nhiều cổng UART phần cứng (HardwareSerial), cho phép giao tiếp đồng thời với nhiều module GSM.
- **Source:** [vv14] - Section: 2. Vi điều khiển hỗ trợ nhiều cổng UART.
- **Tag:** [vv14]

- **Fact:** [CONV] Để đảm bảo hệ thống IoT hoạt động 24/7, cần sử dụng Watchdog Timer trong lập trình để tự động khởi động lại vi điều khiển nếu xảy ra hiện tượng treo máy hoặc lỗi bộ nhớ.
- **Source:** [vv14] - Section: 2. Cơ chế khởi động lại (Phần mềm).
- **Tag:** [vv14]

- **Fact:** [CONV] Tụ lọc nguồn có trị số từ 1000µF trở lên được khuyến nghị sử dụng cho module GSM để giảm nhiễu và bù áp khi module truyền tải dữ liệu.
- **Source:** [vv14] - Section: 3. Nguồn cấp (Phần cứng - hệ thống bền).
- **Tag:** [vv14]

### 3. Thiết bị GSM Công nghiệp
- **Fact:** [CONV] Modem công nghiệp F2103 GPRS IP hỗ trợ các chuẩn giao tiếp RS232/RS485, sử dụng CPU 16/32 bit và có vỏ sắt bảo vệ đạt chuẩn IP30.
- **Source:** [vv14] - Section: 2. F2103 GPRS IP Modem.
- **Tag:** [vv14]

- **Fact:** [CONV] Các dòng modem công nghiệp phổ biến như Teltonika TRM240 (LTE Cat 1) và TRM250 (NB-IoT) thường chỉ hỗ trợ 1 SIM hoạt động tại một thời điểm.
- **Source:** [vv14] - Section: Bảng danh sách modem GSM công nghiệp.
- **Tag:** [vv14]

- **Fact:** [CONV] Hệ thống GSM Gateway chuyên dụng có khả năng hỗ trợ từ 4 đến 32 SIM hoạt động đồng thời, thường có giá thành từ 5 triệu VNĐ trở lên.
- **Source:** [vv14] - Section: Ghi chú (Bảng modem).
- **Tag:** [vv14]

---
**Ghi chú từ @scout:** Các thông tin về giá cả trong tài liệu là giá tham khảo tại thị trường Việt Nam thời điểm năm 2024. [Unverified_Source]: Các chân RX/TX trên Arduino Uno không chịu được mức logic 5V từ module GSM trong thời gian dài, nên sử dụng mạch chia áp nếu cần thiết.
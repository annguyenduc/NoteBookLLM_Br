---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_11
  title: atoms_v14_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v14) về IoT và Arduino:

- **Fact:** Để vào chế độ AT cho module HC-05, người dùng cần nhấn và giữ nút "KEY" hoặc nối chân EN với mức HIGH khi khởi động; đèn LED sẽ nhấp nháy chậm khoảng 2 giây/lần.
- **Source:** [vv14] - Section 1: Đảm bảo rằng HC-05 đang ở chế độ AT.
- **Tag:** [vv14]

- **Fact:** Module HC-06 tự động kích hoạt chế độ AT khi không có thiết bị nào đang kết nối Bluetooth với nó.
- **Source:** [vv14] - Section 1: Đối với HC-06.
- **Tag:** [vv14]

- **Fact:** Baud rate mặc định ở chế độ AT của module HC-05 thường là 38400, trong khi HC-06 là 9600.
- **Source:** [vv14] - Section 2: Baud rate đúng.
- **Tag:** [vv14]

- **Fact:** Module HC-06 chỉ hỗ trợ chế độ Slave (phụ), không hỗ trợ chế độ Master (chủ) hoặc thay đổi vai trò qua lệnh AT+ROLE.
- **Source:** [vv14] - Section: Các lệnh AT của HC 06 và phản hồi & Lưu ý.
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+NAME<tên>` dùng để đặt tên cho HC-06, nhưng nhiều phiên bản firmware của HC-06 không hỗ trợ lệnh truy vấn tên `AT+NAME?`.
- **Source:** [vv14] - Section: Nguyên nhân có thể (vấn đề phản hồi OKsetname).
- **Tag:** [vv14]

- **Fact:** Phân biệt phần cứng: HC-05 thường có 6 chân (STATE, EN, VCC, GND, TXD, RXD) và có nút nhấn; HC-06 thường chỉ có 4 chân (VCC, GND, TXD, RXD) và không có nút nhấn.
- **Source:** [vv14] - Section: Làm sao biết được blutooth thuộc HC 05 hay HC 06.
- **Tag:** [vv14]

- **Fact:** Khi kết nối module Bluetooth với Arduino Uno, nên sử dụng thư viện `SoftwareSerial` (ví dụ chân 10, 11) để tránh xung đột với cổng Serial cứng (chân 0, 1) đang dùng để giao tiếp với máy tính (Serial Monitor).
- **Source:** [vv14] - Section: Sử dụng SoftwareSerial.
- **Tag:** [vv14]

- **Fact:** Để bảo vệ module Bluetooth khi giao tiếp với Arduino dùng mức tín hiệu 5V, nên sử dụng mạch chia áp (voltage divider) cho chân RXD của module.
- **Source:** [vv14] - Section: Kiểm tra phần cứng.
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+VERSION` trên HC-06 thường trả về phản hồi chứa chuỗi "linvor" để nhận diện phiên bản firmware.
- **Source:** [vv14] - Section 6: Kiểm tra với lệnh mã nguồn.
- **Tag:** [vv14]

- **Fact:** Trạng thái đèn LED của HC-05: nhấp nháy nhanh (chưa kết nối), nhấp nháy chậm (chế độ AT), sáng liên tục (đã kết nối).
- **Source:** [vv14] - Section 4: Phản hồi đèn LED.
- **Tag:** [vv14]

- **Fact:** Các ứng dụng phổ biến để giao tiếp với HC-05/HC-06 trên điện thoại bao gồm: Serial Bluetooth Terminal, Bluetooth Electronics, Blynk, và nRF Connect.
- **Source:** [vv14] - Table: Danh sách các ứng dụng phổ biến.
- **Tag:** [vv14]

- **Fact:** Để thay đổi mã PIN ghép đôi cho HC-06, sử dụng lệnh `AT+PIN<mã>` (ví dụ: `AT+PIN1234`), module sẽ phản hồi `OKsetPIN`.
- **Source:** [vv14] - Section 3: Đặt lại mật khẩu ghép đôi.
- **Tag:** [vv14]
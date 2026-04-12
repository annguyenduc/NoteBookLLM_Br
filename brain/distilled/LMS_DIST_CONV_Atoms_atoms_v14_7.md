---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_7
  title: atoms_v14_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v14) về IoT, Arduino và Bluetooth:

- **Fact:** Trạng thái đèn LED trên HC-06: Nhấp nháy nhanh nghĩa là module đang ở chế độ AT; nhấp nháy chậm hoặc sáng liên tục nghĩa là module đã kết nối với một thiết bị.
- **Source:** [vv14] - Mục 2: Kiểm tra lại đèn LED trên HC-06.
- **Tag:** [vv14]

- **Fact:** Sơ đồ kết nối HC-06 với Arduino: TX (HC-06) → Pin 10 (RX SoftwareSerial); RX (HC-06) → Pin 11 (TX SoftwareSerial); VCC → 5V; GND → GND.
- **Source:** [vv14] - Mục 3: Kiểm tra Kết Nối Phần Cứng.
- **Tag:** [vv14]

- **Fact:** Chân RX của module HC-06 cần được cấp điện áp 3.3V qua bộ chia áp để bảo vệ module vì Arduino cung cấp mức logic 5V tại các chân TX/RX.
- **Source:** [vv14] - Mục 3: Kiểm tra Kết Nối Phần Cứng (Lưu ý).
- **Tag:** [vv14]

- **Fact:** Để gửi lệnh AT chính xác từ Serial Monitor, cần thiết lập chế độ kết thúc dòng là "Both NL & CR".
- **Source:** [vv14] - Mục 4: Kiểm tra Serial Monitor.
- **Tag:** [vv14]

- **Fact:** Tốc độ baud mặc định của module HC-06 thường là 9600, nhưng có thể thay đổi sang các mức khác như 38400, 19200, 4800 tùy cấu hình.
- **Source:** [vv14] - Mục 4 & Giải thích Code.
- **Tag:** [vv14]

- **Fact:** Lệnh AT cơ bản cho HC-06: `AT` (kiểm tra kết nối - phản hồi OK), `AT+NAME?` (kiểm tra tên), `AT+VERSION?` (kiểm tra phiên bản), `AT+NAME=NewName` (đổi tên).
- **Source:** [vv14] - Mục 6 & Các Lệnh AT Mà Bạn Có Thể Gửi.
- **Tag:** [vv14]

- **Fact:** Lỗi "Port busy" (jssc.SerialPortException) xảy ra khi cổng COM (ví dụ COM4) đang bị một ứng dụng khác chiếm dụng hoặc chưa được giải phóng.
- **Source:** [vv14] - Phần phản hồi lỗi "Port busy".
- **Tag:** [vv14]

- **Fact:** HC-05 sử dụng Bluetooth 2.0 (Classic), trong khi iPhone chủ yếu hỗ trợ Bluetooth 4.0 trở lên (BLE), dẫn đến việc khó kết nối trực tiếp trừ khi dùng ứng dụng bên thứ ba hỗ trợ Bluetooth Classic.
- **Source:** [vv14] - Phần giải đáp về kết nối HC-05 với iPhone.
- **Tag:** [vv14]

- **Fact:** Module HM-10 (hỗ trợ BLE) được khuyến khích sử dụng thay cho HC-05/HC-06 để có độ tương thích và ổn định cao hơn khi kết nối với iPhone.
- **Source:** [vv14] - Phần giải đáp về kết nối HC-05 với iPhone.
- **Tag:** [vv14]

- **Fact:** Nếu danh sách quét Bluetooth chỉ hiện mã ID thay vì tên, có thể do module chưa được cấu hình tên qua lệnh `AT+NAME` hoặc ứng dụng quét không hỗ trợ hiển thị tên Bluetooth Classic.
- **Source:** [vv14] - Phần giải đáp về hiển thị mã ID Bluetooth.
- **Tag:** [vv14]

- **Fact:** Trong code Arduino, `Serial.begin` (giao tiếp với máy tính) và `bluetooth.begin` (giao tiếp với module) không bắt buộc phải có cùng tốc độ baud, miễn là mỗi lệnh khớp với thiết bị tương ứng.
- **Source:** [vv14] - Phần giải đáp về Baud Rate.
- **Tag:** [vv14]

- **Fact:** Để vào chế độ AT trên một số module Bluetooth, người dùng cần nhấn giữ nút "KEY" (nếu có) trong khi cấp nguồn cho module.
- **Source:** [vv14] - Phần giải đáp về tìm baud rate (Bước 2).
- **Tag:** [vv14]
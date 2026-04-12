---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_6
  title: atoms_v14_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v14** liên quan đến IoT, Arduino và module Bluetooth HC-06:

- **Fact:** [Tên sketch Arduino phải bắt đầu bằng chữ cái hoặc số, tiếp theo là chữ cái, số, dấu gạch ngang, dấu chấm hoặc dấu gạch dưới; độ dài tối đa là 63 ký tự.]
- **Source:** [Section: Issue with Sketch Name]
- **Tag:** [vv14]

- **Fact:** [Thư viện SoftwareSerial cho phép Arduino sử dụng các chân kỹ thuật số khác làm cổng giao tiếp Serial thay vì chỉ dùng chân RX (0) và TX (1) mặc định.]
- **Source:** [Section: Giải thích chi tiết code]
- **Tag:** [vv14]

- **Fact:** [Module HC-06 chỉ có thể hoạt động ở chế độ Slave (thiết bị phụ), không có khả năng tự khởi tạo kết nối.]
- **Source:** [Section: Một số lưu ý]
- **Tag:** [vv14]

- **Fact:** [Hệ điều hành iOS không hỗ trợ giao thức Bluetooth 2.0 thông thường trong hệ thống mặc định, do đó cần ứng dụng chuyên dụng hoặc module BLE (như HM-10) để tương thích.]
- **Source:** [Section: Một số lưu ý]
- **Tag:** [vv14]

- **Fact:** [Chân RX của module HC-06 chỉ chấp nhận mức tín hiệu 3.3V; cần sử dụng bộ chia áp khi kết nối với chân TX của Arduino (5V) để bảo vệ module.]
- **Source:** [Section: Kết nối phần cứng]
- **Tag:** [vv14]

- **Fact:** [Để truy cập và thực hiện các lệnh AT (AT Commands), module HC-06 bắt buộc phải ở trạng thái chưa kết nối với bất kỳ thiết bị Bluetooth nào khác.]
- **Source:** [Section: Sử dụng Serial Monitor để kiểm tra tên module]
- **Tag:** [vv14]

- **Fact:** [Trạng thái đèn LED trên HC-06: Nhấp nháy nhanh (khoảng 2 lần/giây) khi ở chế độ chờ kết nối hoặc AT mode; nhấp nháy chậm hoặc sáng liên tục khi đã kết nối thành công.]
- **Source:** [Section: Kiểm tra trạng thái đèn LED của HC-06]
- **Tag:** [vv14]

- **Fact:** [Lệnh `AT+NAME?` dùng để kiểm tra tên hiện tại của module và `AT+NAME=NewName` dùng để thay đổi tên hiển thị của HC-06.]
- **Source:** [Section: Gửi lệnh AT để kiểm tra tên]
- **Tag:** [vv14]

- **Fact:** [Việc nhận được ký tự lạ (như ⸮) trên Serial Monitor khi gửi lệnh AT thường là dấu hiệu của việc thiết lập sai tốc độ Baud (Baud rate mismatch).]
- **Source:** [Section: Kiểm Tra Tốc Độ Baud]
- **Tag:** [vv14]

- **Fact:** [Tốc độ Baud mặc định của module HC-06 thường được thiết lập là 9600.]
- **Source:** [Section: Code setup / Cấu hình giao diện của Serial Monitor]
- **Tag:** [vv14]

- **Fact:** [Mã PIN mặc định để kết nối với HC-06 thường là "1234" hoặc "0000".]
- **Source:** [Section: Bước 3: Kết nối với HC-06]
- **Tag:** [vv14]
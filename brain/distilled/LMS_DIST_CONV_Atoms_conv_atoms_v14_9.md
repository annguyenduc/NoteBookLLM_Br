---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v14_9
  title: CONV_atoms_v14_9
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v14) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Hàm `macToUUID` được sử dụng để mô phỏng việc chuyển đổi địa chỉ MAC (12 ký tự hex) thành định dạng UUID bằng cách loại bỏ dấu ":" và chèn dấu "-" vào các vị trí quy định.
- **Source:** [vv14 - Section: Giải thích về macToUUID]
- **Tag:** [vv14]

- **Fact:** [CONV] Các module Bluetooth HC-05 và HC-06 không cung cấp UUID chính thức; địa chỉ MAC là thông tin duy nhất có thể lấy được để giả lập UUID cho các ứng dụng Bluetooth.
- **Source:** [vv14 - Section: Lưu ý về HC-05 và HC-06]
- **Tag:** [vv14]

- **Fact:** [CONV] Lệnh AT được sử dụng để truy vấn địa chỉ MAC của module HC-05 là `AT+ADDR?`.
- **Source:** [vv14 - Section: Các bước thực hiện lệnh AT]
- **Tag:** [vv14]

- **Fact:** [CONV] Trong lập trình Arduino, thư viện `SoftwareSerial` cho phép thiết lập giao tiếp Serial trên các chân kỹ thuật số (ví dụ chân 10 làm RX và chân 11 làm TX) để kết nối với module Bluetooth.
- **Source:** [vv14 - Section: Mã Arduino]
- **Tag:** [vv14]

- **Fact:** [CONV] Để đưa module HC-05 vào chế độ nhận lệnh AT (AT Mode), người dùng cần nhấn và giữ nút **KEY** trên module trong khi cấp nguồn.
- **Source:** [vv14 - Section: Lưu ý về chế độ AT]
- **Tag:** [vv14]

- **Fact:** [CONV] Phản hồi từ HC-05 cho lệnh địa chỉ thường có tiền tố `+ADDR:` hoặc `+`, cần được xử lý bằng các hàm như `trim()` và `replace()` để lấy được chuỗi MAC sạch.
- **Source:** [vv14 - Section: Giải thích chi tiết về các thay đổi / Phản hồi từ người dùng]
- **Tag:** [vv14]

- **Fact:** [CONV] Cấu trúc UUID giả lập được tạo ra trong mã nguồn có định dạng: `xxxxxxxx-xxxx-3xxx-2xxx-xxxxxxxxxxxx`.
- **Source:** [vv14 - Section: Hàm macToUUID]
- **Tag:** [vv14]

- **Fact:** [CONV] Tốc độ Baud (Baud rate) phổ biến được sử dụng để giao tiếp giữa Serial Monitor và Arduino trong các ví dụ điều khiển Bluetooth là 9600.
- **Source:** [vv14 - Section: Mã Arduino - setup()]
- **Tag:** [vv14]

- **Fact:** [CONV] Việc đọc dữ liệu từ module Bluetooth trong Arduino thường sử dụng hàm `bluetooth.readStringUntil('\n')` để đảm bảo nhận trọn vẹn một dòng phản hồi.
- **Source:** [vv14 - Section: Mã Arduino - loop()]
- **Tag:** [vv14]

- **Fact:** [Unverified_Source] Tốc độ baud mặc định của module HC-05 khi ở chế độ cấu hình AT hoàn toàn (full AT mode) thường là 38400, khác với tốc độ 9600 thường dùng trong chế độ truyền dữ liệu thông thường.
- **Source:** [Kiến thức bổ sung]
- **Tag:** [Unverified_Source]
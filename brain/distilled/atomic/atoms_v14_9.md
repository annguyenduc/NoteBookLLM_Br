Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v14) theo quy tắc LOM v4.1:

- **Fact:** Phương pháp chuyển đổi địa chỉ MAC (12 ký tự hex) sang định dạng UUID giả lập thường được thực hiện bằng cách loại bỏ dấu ":" và chèn dấu "-" vào các vị trí cố định để tạo cấu trúc 8-4-4-4-12.
- **Source:** [vv14] - Section: Giải thích (macToUUID).
- **Tag:** [vv14]

- **Fact:** Lệnh AT dùng để truy vấn địa chỉ MAC của module Bluetooth HC-05 hoặc HC-06 là `AT+ADDR?`.
- **Source:** [vv14] - Section: ASSISTANT (Để sử dụng lệnh AT+ADDR?...).
- **Tag:** [vv14]

- **Fact:** Để HC-05 vào chế độ nhận lệnh AT (AT Mode), người dùng cần nhấn giữ nút **KEY** trên module trong khi cấp nguồn.
- **Source:** [vv14] - Section: Lưu ý (Đảm bảo HC-05 đã ở chế độ AT...).
- **Tag:** [vv14]

- **Fact:** Thư viện `SoftwareSerial` trong Arduino cho phép thiết lập giao tiếp Serial trên các chân kỹ thuật số khác (ví dụ: chân 10 làm RX, chân 11 làm TX) để kết nối với module Bluetooth.
- **Source:** [vv14] - Section: Mã Arduino (SoftwareSerial bluetooth(10, 11)).
- **Tag:** [vv14]

- **Fact:** Phản hồi từ lệnh `AT+ADDR?` của HC-05 thường có định dạng chứa tiền tố `+ADDR:` hoặc `ADDR:` trước địa chỉ MAC thực tế.
- **Source:** [vv14] - Section: Ví dụ về cách thức hoạt động & Giải thích các thay đổi.
- **Tag:** [vv14]

- **Fact:** Trong lập trình Arduino, hàm `trim()` được sử dụng để loại bỏ các ký tự khoảng trắng và ký tự xuống dòng (`\r`, `\n`) ở đầu và cuối chuỗi dữ liệu nhận được từ Serial.
- **Source:** [vv14] - Section: Giải thích các thay đổi (Hàm macAddress.trim()).
- **Tag:** [vv14]

- **Fact:** Việc chuyển đổi MAC sang UUID bằng cách cắt chuỗi (substring) và nối chuỗi chỉ là phương pháp mô phỏng (giả lập) cho các ứng dụng Bluetooth, không phải là phương pháp chuyển đổi chính thức trên tất cả thiết bị.
- **Source:** [vv14] - Section: Lưu ý (Đây chỉ là một cách mô phỏng...).
- **Tag:** [vv14]

- **Fact:** Để trích xuất địa chỉ MAC từ chuỗi phản hồi của HC-05, có thể sử dụng hàm `startsWith("+ADDR")` để nhận diện và `substring(6)` để cắt bỏ phần tiền tố.
- **Source:** [vv14] - Section: Giải thích về các thay đổi (Kiểm tra phản hồi chứa +ADDR).
- **Tag:** [vv14]

- **Fact:** Tốc độ Baud mặc định thường dùng để giao tiếp với HC-05 trong các ví dụ mẫu là 9600.
- **Source:** [vv14] - Section: Mã Arduino (Serial.begin(9600)).
- **Tag:** [vv14]
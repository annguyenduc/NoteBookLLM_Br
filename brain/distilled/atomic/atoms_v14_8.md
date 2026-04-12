Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** Tốc độ baud mặc định của module Bluetooth HC-06 là 9600.
- **Source:** [v14 - Section: Tóm lại (đầu file)]
- **Tag:** [vv14]

- **Fact:** Để thay đổi tốc độ baud của HC-06 sang 38400, sử dụng lệnh `AT+BAUD4`; để chuyển sang 115200, sử dụng lệnh `AT+BAUD8`.
- **Source:** [v14 - Section: Thay đổi tốc độ baud của HC-06, mục 3]
- **Tag:** [vv14]

- **Fact:** Khi kết nối HC-06 trực tiếp vào chân TX (1) và RX (0) của Arduino, cần phải ngắt kết nối module khi nạp code để tránh xung đột vì các chân này được dùng để giao tiếp với máy tính.
- **Source:** [v14 - Section: Lưu ý khi dùng Serial mặc định / Khắc phục xung đột khi nạp code]
- **Tag:** [vv14]

- **Fact:** Sử dụng thư viện `SoftwareSerial` cho phép Arduino giao tiếp với module Bluetooth qua các chân kỹ thuật số khác (ví dụ chân 10, 11), giúp vừa có thể dùng Serial Monitor vừa giao tiếp được với Bluetooth.
- **Source:** [v14 - Section: Cách 2: Dùng SoftwareSerial trên các chân khác]
- **Tag:** [vv14]

- **Fact:** Thời gian phản hồi lệnh AT của module HC-06 thường dao động trong khoảng từ 100ms đến 500ms.
- **Source:** [v14 - Section: THỜI GIAN HC GỬI PHÀN HỒI VỀ LỆNH AT LÀ BAO LÂU]
- **Tag:** [vv14]

- **Fact:** Module HC-05 có khả năng hoạt động ở cả hai chế độ Master (chủ) và Slave (tớ), trong khi HC-06 chỉ hỗ trợ chế độ Slave.
- **Source:** [v14 - Section: Nếu là HC 05 thì sao / Lưu ý]
- **Tag:** [vv14]

- **Fact:** Để đưa HC-05 vào chế độ AT (để cấu hình), người dùng cần giữ nút "key" hoặc cấp nguồn cho chân "key/en" ở mức HIGH (3.3V) trong khi cấp nguồn cho module.
- **Source:** [v14 - Section: Kiểm tra địa chỉ mac của HC 05, mục 2]
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+ADDR?` được sử dụng để yêu cầu module Bluetooth trả về địa chỉ MAC của nó.
- **Source:** [v14 - Section: 9. Lệnh đọc bộ nhớ / Kiểm tra địa chỉ mac của HC 05, mục 3]
- **Tag:** [vv14]

- **Fact:** Địa chỉ MAC Bluetooth chuẩn thường có định dạng 6 cặp ký tự hex (ví dụ: 13:EF:DE:0F), trong khi UUID (Universally Unique Identifier) có định dạng chuỗi dài hơn (ví dụ: 6A536DD9-61E0-3998-291D-D7CF2EFA03E0).
- **Source:** [v14 - Section: địa chỉ như trên gọi là định dạng địa chỉ gì / ASSISTANT phản hồi về UUID]
- **Tag:** [vv14]

- **Fact:** Các module Bluetooth Classic như HC-05/06 sử dụng giao thức SPP (Serial Port Profile) và không hỗ trợ trực tiếp UUID như các thiết bị Bluetooth Low Energy (BLE).
- **Source:** [v14 - Section: Kết luận (cuối file)]
- **Tag:** [vv14]

- **Fact:** Khi gửi lệnh AT từ Serial Monitor của Arduino IDE, cần thiết lập chế độ Line Ending là "Newline" hoặc "Both NL & CR" để module có thể nhận diện được lệnh.
- **Source:** [v14 - Section: 5. Kiểm tra cài đặt Serial Monitor]
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+ROLE=0` thiết lập module ở chế độ Slave, và `AT+ROLE=1` thiết lập module ở chế độ Master.
- **Source:** [v14 - Section: 3. Lệnh kiểm tra và thay đổi chế độ]
- **Tag:** [vv14]
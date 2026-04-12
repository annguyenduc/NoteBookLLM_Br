Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** [CONV] Tốc độ baud mặc định của module Bluetooth HC-06 là 9600.
- **Source:** [vv14 - Section: Tóm lại]
- **Tag:** [vv14]

- **Fact:** [CONV] Để thay đổi tốc độ baud của HC-06, cần kết nối ở chế độ AT và sử dụng lệnh AT+BAUD4 (cho 38400) hoặc AT+BAUD8 (cho 115200).
- **Source:** [vv14 - Section: Thay đổi tốc độ baud]
- **Tag:** [vv14]

- **Fact:** [CONV] Khi kết nối HC-06 trực tiếp vào chân TX (1) và RX (0) của Arduino, phải ngắt kết nối module khi nạp code để tránh xung đột Serial.
- **Source:** [vv14 - Section: Lưu ý khi dùng Serial mặc định / Khắc phục xung đột]
- **Tag:** [vv14]

- **Fact:** [CONV] Thư viện SoftwareSerial cho phép giao tiếp với module Bluetooth qua các chân kỹ thuật số khác (ví dụ chân 10, 11) để có thể sử dụng đồng thời Serial Monitor.
- **Source:** [vv14 - Section: Cách 2: Dùng SoftwareSerial trên các chân khác]
- **Tag:** [vv14]

- **Fact:** [CONV] Thời gian phản hồi lệnh AT của module HC-06 thường dao động từ 100ms đến 500ms.
- **Source:** [vv14 - Section: THỜI GIAN HC GỬI PHÀN HỒI VỀ LỆNH AT]
- **Tag:** [vv14]

- **Fact:** [CONV] Module HC-05 có khả năng hoạt động ở cả hai chế độ Master (chủ) và Slave (tớ), trong khi HC-06 thường chỉ hỗ trợ chế độ Slave.
- **Source:** [vv14 - Section: Nếu là HC 05 thì sao / Lưu ý]
- **Tag:** [vv14]

- **Fact:** [CONV] Lệnh `AT+ADDR?` được sử dụng để kiểm tra địa chỉ MAC của module Bluetooth HC-05/HC-06.
- **Source:** [vv14 - Section: kiểm tra địa chỉ mac của HC 05]
- **Tag:** [vv14]

- **Fact:** [CONV] Địa chỉ MAC Bluetooth chuẩn có định dạng 6 cặp ký tự thập lục phân (ví dụ: 13:EF:DE:0F), trong khi UUID là định dạng định danh duy nhất dài hơn (ví dụ: 6A536DD9-61E0-3998-291D-D7CF2EFA03E0).
- **Source:** [vv14 - Section: địa chỉ như trên gọi là định dạng địa chỉ gì / Phản hồi từ HC-05]
- **Tag:** [vv14]

- **Fact:** [CONV] Các module Bluetooth Classic như HC-05/HC-06 sử dụng giao thức SPP (Serial Port Profile) và không hỗ trợ trực tiếp UUID như các thiết bị Bluetooth Low Energy (BLE).
- **Source:** [vv14 - Section: Kết luận (về UUID)]
- **Tag:** [vv14]

- **Fact:** [CONV] Để đưa HC-05 vào chế độ AT, người dùng cần giữ nút "key" hoặc chân "en" trong khi cấp nguồn cho module.
- **Source:** [vv14 - Section: Cài đặt chế độ AT cho HC-05]
- **Tag:** [vv14]
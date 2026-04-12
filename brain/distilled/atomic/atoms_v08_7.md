Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v08 liên quan đến hệ sinh thái OhStem, YoloBit và framework Blockly:

- **Fact:** Nền tảng lập trình `app.ohstem.vn` là một triển khai tùy chỉnh dựa trên thư viện mã nguồn mở Google Blockly.
- **Source:** Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem.
- **Tag:** [vv08]

- **Fact:** Mọi thực thể trong không gian làm việc (khối lệnh, biến, bình luận) đều được định danh bằng một chuỗi ID duy nhất (UUID) tạo bởi hàm `Blockly.utils.idGenerator.genUid()`.
- **Source:** Chương 1: Engine Cốt lõi - Hệ thống Định danh Phổ quát của Google Blockly.
- **Tag:** [vv08]

- **Fact:** Bộ ký tự (`soup_`) dùng để tạo ID trong Blockly bao gồm 92 ký tự: 26 chữ hoa, 26 chữ thường, 10 chữ số và 30 ký tự đặc biệt (như `!@#$%^&*()_+-=[]{};':"|,.<>/?~`).
- **Source:** Bảng 2.1: Bộ ký tự Định nghĩa của Blockly.utils.idGenerator (soup_).
- **Tag:** [vv08]

- **Fact:** Độ dài cố định của một chuỗi ID được tạo bởi hàm `genUid` là 20 ký tự.
- **Source:** 2.2. Logic Thuật toán của genUid - Mục 1: Độ dài Cố định.
- **Tag:** [vv08]

- **Fact:** Các phần mở rộng (extensions) của OhStem như `yolobit_keypad_mpr121` hoặc `yolobit_carbit_v2` được phát triển để bổ sung khối lệnh cho phần cứng cụ thể trên nền engine Blockly.
- **Source:** Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem.
- **Tag:** [vv08]

- **Fact:** Robot Rover hỗ trợ các khối lệnh điều khiển tốc độ độc lập cho bánh trái (`left_wheel_speed`) và bánh phải (`right_wheel_speed`) thông qua khối `rover_move_motor`.
- **Source:** Dữ liệu RAW - Block type: `rover_move_motor`.
- **Tag:** [vv08]

- **Fact:** Hệ sinh thái Stemkit tích hợp nhiều loại cảm biến và thiết bị ngoại vi bao gồm: cảm biến siêu âm (`ultrasonic`), màn hình `LCD1602`, máy bơm mini (`mini_pump`), cảm biến độ ẩm đất (`soil_sensor`), cảm biến gas, cảm biến ánh sáng, cảm biến âm thanh và cảm biến nhiệt độ độ ẩm `DHT`.
- **Source:** Dữ liệu RAW - Các block type tiền tố `stemkit_`.
- **Tag:** [vv08]

- **Fact:** Cảm biến `MPR121` trong bộ Stemkit hỗ trợ các chức năng: kiểm tra kết nối (`check`), đọc giá trị (`read`), xóa trạng thái (`clear`), quét thiết bị (`scan`) và tắt âm thanh (`sound_off`).
- **Source:** Dữ liệu RAW - Các block type tiền tố `stemkit_mpr121_`.
- **Tag:** [vv08]

- **Fact:** Việc sử dụng các ký tự đặc biệt trong ID (như `$` hoặc dấu huyền) có thể gây lỗi cú pháp khi ID được chèn vào chuỗi mẫu (template string) hoặc biểu thức chính quy trong JavaScript nếu không được xử lý thoát (escape) đúng cách.
- **Source:** 2.3. Cảnh báo Quan trọng: Xử lý Ký tự Đặc biệt trong các Quy trình Hạ nguồn.
- **Tag:** [vv08]

- **Fact:** Trong cấu trúc lưu trữ (XML/JSON), khối lệnh tham chiếu đến biến thông qua thuộc tính `id` của biến đó, đảm bảo tính nhất quán ngay cả khi tên biến thay đổi.
- **Source:** Chương 3: Phân biệt Biến và Khối lệnh trong Cấu trúc JSON.
- **Tag:** [vv08]

- **Fact:** Để tái tạo chính xác ID tương thích với OhStem bằng Python, thư viện `secrets` được khuyến nghị sử dụng để đảm bảo tính ngẫu nhiên cao.
- **Source:** 4.1. Triển khai genUid bằng Python.
- **Tag:** [vv08]
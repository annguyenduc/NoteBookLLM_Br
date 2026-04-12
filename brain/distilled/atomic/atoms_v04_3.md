Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu **Volume v04** về IoT, Robotics và lập trình điều khiển:

### 1. Quy chuẩn Sơ đồ khối và Lập trình IoT
- **Fact:** Một sơ đồ khối IoT đầy đủ tiêu chuẩn phải bao gồm 5 khối chức năng chính: Nguồn (5V/USB-C) -> Cảm biến (Input) -> Bộ điều khiển trung tâm (Yolo:Bit/UNO) -> Cơ cấu chấp hành (Output) -> Giao diện người dùng (UI/Hiển thị).
- **Source:** [vv04] - Section: Barem chi tiết – Bạn Lập trình (35đ) & Sơ đồ khối mẫu.
- **Tag:** [vv04]

- **Fact:** Logic điều khiển IoT chuyên sâu yêu cầu thiết lập ngưỡng (threshold) đi kèm với Hysteresis (độ trễ) và lọc nhiễu theo thời gian để tránh tình trạng thiết bị bật/tắt liên tục khi tín hiệu dao động quanh ngưỡng.
- **Source:** [vv04] - Section: Barem chi tiết – Bạn Lập trình (35đ) - Mục 2. Luồng quyết định.
- **Tag:** [vv04]

- **Fact:** Các cơ chế an toàn (Fail-safe) bắt buộc cho hệ thống IoT có cơ cấu chấp hành mạnh (như máy bơm) bao gồm: Timeout (thời gian chạy tối đa), Lockout (thời gian nghỉ bắt buộc giữa các lần kích hoạt), và Manual override (chế độ điều khiển thủ công).
- **Source:** [vv04] - Section: Barem chi tiết – Bạn Lập trình (35đ) - Mục 3. Fail-safe & An toàn.
- **Tag:** [vv04]

- **Fact:** Một kế hoạch kiểm thử (Test plan) cho sản phẩm IoT cần tối thiểu 5 ca kiểm thử (test cases) mô tả rõ điều kiện đầu vào định lượng và kết quả đầu ra mong đợi để xác định trạng thái Pass/Fail.
- **Source:** [vv04] - Section: Barem chi tiết – Bạn Lập trình (35đ) - Mục 4. Kế hoạch kiểm thử.
- **Tag:** [vv04]

### 2. Thông số kỹ thuật và Linh kiện (Kit Yolo:Bit/UNO)
- **Fact:** Các cảm biến tiêu chuẩn trong bộ kit hỗ trợ phát triển IoT bao gồm: DHT20 (đo nhiệt độ, độ ẩm không khí), cảm biến ánh sáng, cảm biến siêu âm/hồng ngoại (đo khoảng cách/phát hiện người), và cảm biến độ ẩm đất.
- **Source:** [vv04] - Section: Gợi ý “bảng thành phần” để HS lựa chọn từ kit.
- **Tag:** [vv04]

- **Fact:** Các cơ cấu chấp hành (actuators) phổ biến để thực hiện hóa giải pháp Robotics/IoT gồm: Relay (kích hoạt bơm/đèn), động cơ Servo (điều khiển góc quay van/cửa), quạt mini và hệ thống LED đơn hoặc LED RGB.
- **Source:** [vv04] - Section: Gợi ý “bảng thành phần” để HS lựa chọn từ kit.
- **Tag:** [vv04]

- **Fact:** Ngưỡng vận hành mẫu cho hệ thống tưới cây thông minh: Kích hoạt bơm khi độ ẩm đất < 35% và ánh sáng > 200 lux; tự động ngắt bơm nếu phát hiện có người trong khoảng cách < 30cm.
- **Source:** [vv04] - Section: Gợi ý nhanh cho thí sinh (không cần phần cứng).
- **Tag:** [vv04]

### 3. Thiết kế 3D và Sản xuất (Printability)
- **Fact:** Một file thiết kế 3D (STL) đạt chuẩn in ấn kỹ thuật cần đảm bảo tính "Watertight" (kín nước/khối đặc), không có các thành phần rời rạc (shells) không dính liền và không có các cạnh suy biến (cạnh bằng 0mm).
- **Source:** [vv04] - Section: Phân tích mô hình 3D “skibidi – Viet Nguyễn”.
- **Tag:** [vv04]

- **Fact:** Trong in ấn 3D FDM, các bề mặt có góc nhô (overhang) lớn hơn 60 độ so với trục thẳng đứng (Z) sẽ yêu cầu cấu trúc hỗ trợ (support) để có thể in thành công.
- **Source:** [vv04] - Section: Phân tích mô hình 3D “skibidi – Viet Nguyễn”.
- **Tag:** [vv04]

- **Fact:** Thiết kế vỏ hộp cho thiết bị IoT cần tính toán dung sai lắp ráp (thường từ 0.3mm đến 0.4mm) tại các khớp nối và phải có khoang chờ sẵn cho các linh kiện tiêu chuẩn như LCD 1602 hoặc board mạch điều khiển.
- **Source:** [vv04] - Section: Gợi ý nâng điểm - Smart focus lamp.
- **Tag:** [vv04]

### 4. Hệ thống IoT mở rộng
- **Fact:** Hệ thống đèn học thông minh (Smart Focus Lamp) có thể mở rộng tính năng bằng cách sử dụng vi điều khiển ESP32 để kết nối Internet, đồng bộ dữ liệu với ứng dụng di động (App) và lưu trữ lịch sử vận hành trên Database.
- **Source:** [vv04] - Section: Sơ đồ 3 (Smart focus lamp system).
- **Tag:** [vv04]

--------------------------------------------------
**Ghi chú từ @scout:** Các thông số về ngưỡng (35%, 200 lux, 30cm) là các giá trị mẫu được đề xuất trong tài liệu hướng dẫn thí sinh để đảm bảo tính khả thi của logic điều khiển.
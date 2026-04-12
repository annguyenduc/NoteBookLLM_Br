Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu **Volume v08** về các chủ đề IoT, Arduino, YoloBit, Robotics và AI:

- **Fact:** Chiến thuật "cắm trại 48 giờ" là khung thời gian tiêu chuẩn để triển khai các dự án AI Hackathon, chia làm 2 lộ trình chính: phần mềm thuần AI và AI kết hợp Robot Ohstem.
- **Source:** [v08 - Section: Conversation: Chiến thuật AI Hackathon]
- **Tag:** [vv08]

- **Fact:** Hệ sinh thái phần cứng Ohstem phục vụ Robotics bao gồm các thiết bị: xBot, Rover V2 và mạch vi điều khiển Yolo:Bit V2.
- **Source:** [v08 - Section: Conversation: Chiến thuật AI Hackathon]
- **Tag:** [vv08]

- **Fact:** Trong kiến trúc AI + Robot, các mô hình AI "nặng" nên được chạy trên máy tính hoặc điện thoại, trong khi Yolo:Bit V2 đóng vai trò xử lý điều khiển thời gian thực (đèn, còi, động cơ) thông qua giao tiếp BLE hoặc UART.
- **Source:** [v08 - Section: Lộ trình (B) AI + Robot Ohstem]
- **Tag:** [vv08]

- **Fact:** Các chỉ số thành công (KPI) quan trọng cho dự án AI bao gồm: độ chính xác (≥ 85%), thời gian xử lý (< 200ms) và khả năng tiết kiệm thời gian thao tác (khoảng 30%).
- **Source:** [v08 - Section: 1) Đặt mục tiêu đúng (3–4 giờ đầu)]
- **Tag:** [vv08]

- **Fact:** Để đảm bảo an toàn trong Robotics AI, hệ thống cần có cơ chế "failsafe": khi độ tin cậy (confidence) của mô hình AI thấp, robot phải tự động giảm tốc hoặc dừng lại.
- **Source:** [v08 - Section: Kiến trúc kỹ thuật]
- **Tag:** [vv08]

- **Fact:** Công cụ chuyển đổi mô tả hành vi robot sang Blockly hỗ trợ xuất định dạng file .json tương thích hoàn toàn với nền tảng app.ohstem.vn.
- **Source:** [v08 - Section: Conversation: Tạo prompt chuyển đổi code]
- **Tag:** [vv08]

- **Fact:** Các khối lệnh Blockly đặc thù cho Robot Rover bao gồm: `rover_move_delay` (di chuyển theo hướng và thời gian), `rover_stop` (dừng chuyển động) và `rover_servo_write_angle` (điều khiển góc quay servo).
- **Source:** [v08 - Section: Block cần sinh]
- **Tag:** [vv08]

- **Fact:** Việc lập trình robot Ohstem có thể thực hiện thông qua ngôn ngữ MicroPython hoặc Arduino, hỗ trợ chuyển đổi từ lập trình khối (Blockly) sang mã nguồn.
- **Source:** [v08 - Section: Conversation: Chiến thuật AI Hackathon - Assistant's additional note]
- **Tag:** [vv08]

- **Fact:** Cảm biến siêu âm (`yolobit_ultrasonic_read`) được sử dụng trong Blockly để đo khoảng cách, phục vụ các logic điều kiện như tránh vật cản hoặc dừng khẩn cấp.
- **Source:** [v08 - Section: Block cần sinh - Khối điều kiện (if)]
- **Tag:** [vv08]

- **Fact:** Thư viện YoloBit/Ohstem cung cấp các khối điều khiển vòng lặp như `controls_repeat_ext` (lặp số lần cố định) và `controls_whileUntil` (lặp theo điều kiện) để tối ưu hóa kịch bản hành động của robot.
- **Source:** [v08 - Section: Block cần sinh - Khối vòng lặp]
- **Tag:** [vv08]
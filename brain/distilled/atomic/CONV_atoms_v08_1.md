Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v08** về chủ đề IoT, Robotics, và AI:

- **Fact:** [CONV] Chiến thuật AI Hackathon thường được thiết kế theo khung thời gian "cắm trại 48 giờ" với các mốc cứng từ chốt bài toán đến nộp bài.
- **Source:** [v08 - Section: Conversation: Chiến thuật AI Hackathon]
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ sinh thái phần cứng Ohstem phục vụ AI Hackathon bao gồm các thiết bị chính: xBot, Rover V2 và Yolo:Bit V2.
- **Source:** [v08 - Section: Conversation: Chiến thuật AI Hackathon]
- **Tag:** [vv08]

- **Fact:** [CONV] Tiêu chí chấm điểm phổ biến trong các cuộc thi AI Hackathon: Sáng tạo (25–30%), Tác động (20–25%), Kỹ thuật (30–35%), Khả thi/hoàn thiện (15–20%).
- **Source:** [v08 - Section: Khung chiến thuật tổng quát]
- **Tag:** [vv08]

- **Fact:** [CONV] Trong kiến trúc AI kết hợp Robot, mô hình AI "nặng" nên chạy trên PC hoặc điện thoại, trong khi Yolo:Bit V2 đóng vai trò điều khiển thời gian thực (đèn, còi, I/O).
- **Source:** [v08 - Section: Lộ trình (B) AI + Robot Ohstem]
- **Tag:** [vv08]

- **Fact:** [CONV] Giao tiếp giữa ứng dụng AI trên máy tính/điện thoại và mạch Yolo:Bit V2 thường thông qua giao thức BLE (Bluetooth Low Energy) hoặc UART.
- **Source:** [v08 - Section: Lộ trình (B) AI + Robot Ohstem]
- **Tag:** [vv08]

- **Fact:** [CONV] Cơ chế an toàn (failsafe) cho robot AI: Khi độ tin cậy (confidence) của mô hình thấp, robot cần được lập trình để giảm tốc độ hoặc dừng lại.
- **Source:** [v08 - Section: Kiến trúc tham khảo (AI + Ohstem)]
- **Tag:** [vv08]

- **Fact:** [CONV] Công cụ chuyển đổi mô tả hành vi robot sang Blockly hỗ trợ xuất định dạng file `.json` tương thích với nền tảng `app.ohstem.vn`.
- **Source:** [v08 - Section: Conversation: Tạo prompt chuyển đổi code]
- **Tag:** [vv08]

- **Fact:** [CONV] Các khối lệnh Blockly (Block) đặc thù cho hệ sinh thái Ohstem bao gồm: `rover_move_delay` (di chuyển có thời gian), `rover_stop` (dừng), và `rover_servo_write_angle` (điều khiển góc servo).
- **Source:** [v08 - Section: Block cần sinh]
- **Tag:** [vv08]

- **Fact:** [CONV] Trong lập trình điều khiển robot, việc sử dụng biến vận tốc (ví dụ biến `v`) thay vì giá trị số cố định giúp tối ưu hóa việc điều chỉnh tốc độ toàn cục.
- **Source:** [v08 - Section: Block cần sinh]
- **Tag:** [vv08]

- **Fact:** [CONV] Cấu trúc điều kiện trong Blockly cho AI Robot sử dụng khối `controls_if` kết hợp với các khối đọc cảm biến như `yolobit_ultrasonic_read` (cảm biến siêu âm).
- **Source:** [v08 - Section: Block cần sinh]
- **Tag:** [vv08]

- **Fact:** [CONV] Thư viện YoloBit/Ohstem hỗ trợ các ngôn ngữ lập trình MicroPython và Arduino để triển khai các dự án AI và Robotics.
- **Source:** [v08 - Section: Conversation: Tạo prompt chuyển đổi code]
- **Tag:** [vv08]

- **Fact:** [CONV] Hành động phức tạp như "trồng cây" của robot có thể được module hóa thành hàm (`procedures_callnoreturn`) điều khiển chuỗi hạ cần, chờ và nâng cần.
- **Source:** [v08 - Section: Block cần sinh]
- **Tag:** [vv08]
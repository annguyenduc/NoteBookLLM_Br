Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v08 về IoT, Robotics và lập trình robot Rover:

- **Fact:** Thư viện mở rộng `olobit_extension_events` hỗ trợ việc sử dụng các sự kiện (events) trong chương trình lập trình cho thiết bị YoloBit.
- **Source:** [vv08 - Section: DỮ LIỆU RAW]
- **Tag:** [vv08]

- **Fact:** Thư viện "ROBOCON" (`yolobit_extension_robocon_rover`) là phần mở rộng chuyên dụng cung cấp các khối lệnh bổ sung cho robot Rover khi tham gia thi đấu Robocon.
- **Source:** [vv08 - Section: DỮ LIỆU RAW]
- **Tag:** [vv08]

- **Fact:** Cấu hình chuẩn cho thuật toán PID trên robot Rover bao gồm các tham số: `Kp` (tỉ lệ), `Ki` (tích phân), `Kd` (đạo hàm) và `base_speed` (tốc độ cơ sở).
- **Source:** [vv08 - Section: Có gì bên trong (khung Robotcon chuẩn)]
- **Tag:** [vv08]

- **Fact:** Robot Rover sử dụng cảm biến line 4 kênh (L1, L2, R1, R2) để thực hiện nhiệm vụ dò đường (line following) thông qua việc đọc giá trị đơn lẻ từ các chân CH1 đến CH4.
- **Source:** [vv08 - Section: Có gì bên trong (khung Robotcon chuẩn)]
- **Tag:** [vv08]

- **Fact:** Công thức tính sai số (error) trong PID cho robot 4 mắt line dựa trên trọng số: `LW = (L1*3) + L2` và `RW = (R2*3) + R1`, sau đó `error = LW - RW`.
- **Source:** [vv08 - Section: Có gì bên trong (khung Robotcon chuẩn)]
- **Tag:** [vv08]

- **Fact:** Việc phát hiện giao lộ (intersection) có thể được thực hiện bằng cách tính tổng giá trị của 4 kênh cảm biến line (`INTER = L1+L2+R1+R2`).
- **Source:** [vv08 - Section: Có gì bên trong (khung Robotcon chuẩn)]
- **Tag:** [vv08]

- **Fact:** Cuộc thi AI Hackathon 2023 do KDI Education tổ chức sử dụng robot Rover của OhStem làm nền tảng thi đấu chính cho các bảng THCS và THPT.
- **Source:** [vv08 - Section: AI Hackathon 2023]
- **Tag:** [vv08]

- **Fact:** Robot Rover có khả năng tích hợp các module Camera AI như HuskyLens hoặc K210 để thực hiện các nhiệm vụ nhận diện hình ảnh, màu sắc và ký hiệu.
- **Source:** [vv08 - Section: AI Hackathon 2023 - Phần cứng Rover]
- **Tag:** [vv08]

- **Fact:** Các môi trường lập trình hỗ trợ cho robot Rover bao gồm OhStem App (Blockly), Arduino C/C++ và MicroPython.
- **Source:** [vv08 - Section: AI Hackathon 2023 - Phần mềm]
- **Tag:** [vv08]

- **Fact:** Chiến lược điều khiển robot tại giao lộ 90 độ bao gồm việc quay tại chỗ cho đến khi hai mắt cảm biến giữa (S1, S2) bám lại vào line và hai mắt ngoài (S0, S3) rời khỏi line.
- **Source:** [vv08 - Section: Rẽ tại giao lộ (90°)]
- **Tag:** [vv08]

- **Fact:** Để căn chỉnh robot dừng chính xác tại ô nhiệm vụ (End-of-Line), thuật toán thường kết hợp việc bám line đến khi mất tín hiệu, sau đó lùi chậm cho đến khi cảm biến giữa chạm lại vạch đen.
- **Source:** [vv08 - Section: Căn chỉnh ô dừng]
- **Tag:** [vv08]

- **Fact:** Việc sử dụng State Machine (máy trạng thái) giúp quản lý các tiến trình của robot như: `FOLLOW` (dò line), `TURN` (rẽ), và `TASK` (thực hiện nhiệm vụ) một cách tuần tự và ổn định.
- **Source:** [vv08 - Section: State machine (scheduler)]
- **Tag:** [vv08]
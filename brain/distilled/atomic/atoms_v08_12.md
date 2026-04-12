Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v08:

- **Fact:** Ứng dụng OhStem (app.ohstem.vn) hỗ trợ lập trình cho robot Rover bằng cả ngôn ngữ Python và lập trình kéo khối (Blockly).
- **Source:** [vv08] - Section: nhanh (OhStem App)
- **Tag:** [vv08]

- **Fact:** Cảm biến dò đường 4 mắt trên robot Rover được kết nối qua chip mở rộng PCF8574 trên giao tiếp I2C (chân P19/P20) với địa chỉ quét tự động từ 0x20 đến 0x27.
- **Source:** [vv08] - Section: nhanh (OhStem App) - Đọc cảm biến dò đường 4 mắt
- **Tag:** [vv08]

- **Fact:** Giá trị cảm biến dò đường của Rover được chuẩn hóa theo quy tắc: vạch đen trả về giá trị 1 và nền trắng trả về giá trị 0.
- **Source:** [vv08] - Section: nhanh (OhStem App) - Chuẩn hóa giá trị cảm biến
- **Tag:** [vv08]

- **Fact:** Thông số PID mặc định cho thuật toán dò line của Rover là Kp=22, Ki=0, Kd=12 với tốc độ nền (base_speed) đề xuất từ 35 đến 55.
- **Source:** [vv08] - Section: Bạn cần chỉnh gì?
- **Tag:** [vv08]

- **Fact:** File dự án dành cho YoloBit trên OhStem App có định dạng `.json`, bao gồm các thông tin về thiết bị (`device: "yolobit"`), các thư viện mở rộng (`extensions`) và nội dung mã khối (`xmlText`).
- **Source:** [vv08] - Section: USER: yOLOBIT của ohstem chỉ chấp file .json / ASSISTANT: Bản .json mới
- **Tag:** [vv08]

- **Fact:** Trong Minecraft Education Edition, lệnh `builder.tracePath(block)` được dùng để đặt các khối dọc theo lộ trình di chuyển của Builder tính từ vị trí được đánh dấu (`builder.mark()`) gần nhất.
- **Source:** [vv08] - Section: Conversation: Giải thích trace path
- **Tag:** [vv08]

- **Fact:** Để Hopper (phễu) tự động kết nối và đổ vật phẩm vào Trapped Chest trong Minecraft, phương pháp đơn giản nhất là đặt Hopper ngay phía trên Chest (hướng xuống).
- **Source:** [vv08] - Section: USER: Có câu lệnh nào... đặt trapped chest và hopper
- **Tag:** [vv08]

- **Fact:** Trong Minecraft Education phiên bản v1.21.91 (nền Bedrock), hướng của Hopper được điều khiển qua thuộc tính `facing_direction` với các mã số: 0 (Xuống), 2 (Bắc), 3 (Nam), 4 (Tây), 5 (Đông).
- **Source:** [vv08] - Section: ASSISTANT: phiên bản của tôi là minecraft edu v1.21.91
- **Tag:** [vv08]

- **Fact:** Tính năng `agent.setAssist` trong Minecraft cho phép kích hoạt các quyền năng cho Agent bao gồm: `place on move` (đặt khối khi di chuyển), `place from any slot` (tự tìm khối từ mọi ô đồ) và `destroy obstacles` (tự phá vật cản).
- **Source:** [vv08] - Section: Conversation: Giải thích setAssist Minecraft
- **Tag:** [vv08]

- **Fact:** Khi lập trình PID bằng khối cho Rover, việc tăng `Kd` giúp giảm rung lắc trên line, tăng `Kp` giúp robot vào cua nhạy hơn và điều chỉnh `Ki` để xử lý sai số tích lũy khi robot lệch về một phía.
- **Source:** [vv08] - Section: Cách tinh chỉnh nhanh (PID blocks)
- **Tag:** [vv08]
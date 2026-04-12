Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v02**:

**1. Về In 3D (Neptune 4/Robotics):**
- **Fact:** Đầu filament cần được cắt vát nhọn 45° để dễ dàng đưa vào bộ đùn (extruder).
- **Source:** [vv02] - Bước 4: Nạp mực mới lại.
- **Tag:** [vv02]

- **Fact:** Tiếng kêu "tạch tạch" tại extruder là dấu hiệu của việc đầu phun bị tắc hoặc lò xo ép bánh răng quá chặt.
- **Source:** [vv02] - Bước 5: Kiểm tra extruder.
- **Tag:** [vv02]

- **Fact:** Nhựa PLA để lâu cần được làm khô ở nhiệt độ 50–55 °C trong khoảng 3–4 giờ để đảm bảo chất lượng in.
- **Source:** [vv02] - 6. Mẹo phòng tránh tắc mực.
- **Tag:** [vv02]

- **Fact:** Khi tháo hoặc lắp nozzle, bắt buộc phải làm nóng đầu phun (khoảng 200 °C) để tránh làm hỏng ren hoặc rò rỉ nhựa.
- **Source:** [vv02] - Bước 5: Tháo đầu nozzle & 4. Lắp lại.
- **Tag:** [vv02]

- **Fact:** Cụm extruder của Neptune 4 là loại truyền động trực tiếp (direct drive), nắp che thường được cố định bằng 2 ốc lục giác 2mm.
- **Source:** [vv02] - 3. Tháo đầu in (Hotend) từng bước & 3. Các bước tháo nắp che extruder.
- **Tag:** [vv02]

**2. Về IoT và Yolo:Bit:**
- **Fact:** Cảm biến IR Receiver trên Yolo:Bit hoạt động ở mức logic 3.3V; việc cấp nguồn 5V có thể gây sai lệch hoặc hư hỏng.
- **Source:** [vv02] - 1. Kiểm tra phần cứng cơ bản (IR).
- **Tag:** [vv02]

- **Fact:** Khi sử dụng đồng thời Wi-Fi/MQTT và IR, có thể xảy ra xung đột tài nguyên (timer/interrupt) khiến cảm biến IR không nhận được tín hiệu.
- **Source:** [vv02] - 2) Thử “tách IoT” để chắc IR hoạt động.
- **Tag:** [vv02]

- **Fact:** Để tránh nghẽn hệ thống khi dùng IoT, không nên thực hiện lệnh Publish MQTT trực tiếp bên trong hàm callback của IR; thay vào đó nên sử dụng biến trung gian hoặc hàng đợi (queue).
- **Source:** [vv02] - 3) Ghép lại với IoT theo “mẫu không xung đột”.
- **Tag:** [vv02]

- **Fact:** Trong giao thức MQTT, "Topic" là tên kênh dữ liệu và nó sẽ tự động được tạo trên Broker khi thiết bị thực hiện lệnh Publish lần đầu tiên.
- **Source:** [vv02] - 1️⃣ Hiểu rõ: “topic” là gì trong MQTT? & 2️⃣ Cách “tạo” ir/code trong thực tế.
- **Tag:** [vv02]

- **Fact:** Việc thêm tụ điện từ 10–47µF giữa chân VCC và GND của module IR có thể giúp lọc nhiễu nguồn do sóng Wi-Fi phát ra.
- **Source:** [vv02] - 4) Lý do hay gặp khiến “IoT bật là IR câm”.
- **Tag:** [vv02]

**3. Về Lập trình (AI/Robotics):**
- **Fact:** Thư viện `ir_rx` trong MicroPython hỗ trợ giải mã các giao thức remote phổ biến như NEC (NEC_8).
- **Source:** [vv02] - Cách 2: Dùng Python (MicroPython REPL hoặc code).
- **Tag:** [vv02]
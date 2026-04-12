Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu về IoT, Yolo UNO và hệ sinh thái OhStem (Volume v02):

- **Fact:** Combo Ánh sáng + Relay được ứng dụng làm đèn tiết kiệm năng lượng tự bật khi trời tối.
- **Source:** [vv02 - Chủ đề: Năng lượng]
- **Tag:** [vv02]

- **Fact:** Combo Ánh sáng + Servo được ứng dụng làm tấm pin mặt trời tự xoay theo hướng ánh sáng.
- **Source:** [vv02 - Chủ đề: Năng lượng]
- **Tag:** [vv02]

- **Fact:** Combo Siêu âm + LCD1602 được ứng dụng làm cảm biến đo mức nước bồn rửa.
- **Source:** [vv02 - Chủ đề: Sinh hoạt / Đời sống]
- **Tag:** [vv02]

- **Fact:** Template dự án IoT tiêu chuẩn trên app.ohstem.vn gồm 5 phần: Khởi động (WiFi/MQTT/NTP), Đọc & xử lý cảm biến (200ms), Gửi dữ liệu & Log (1s), Nhận lệnh MQTT, và Khối an toàn (Fail-safe).
- **Source:** [vv02 - Sơ đồ khối Template chung]
- **Tag:** [vv02]

- **Fact:** Thuật toán EMA (Exponential Moving Average) dùng để làm mượt dữ liệu cảm biến, tính theo công thức: `ema = alpha * giá_trị_mới + (1 - alpha) * ema_cũ`.
- **Source:** [vv02 - Nhiệm vụ A – Đọc cảm biến và xử lý nhiễu]
- **Tag:** [vv02]

- **Fact:** Kỹ thuật Hysteresis (sử dụng hai ngưỡng T_high và T_low) giúp hệ thống tránh tình trạng bật/tắt thiết bị liên tục khi giá trị cảm biến dao động quanh một điểm ngưỡng.
- **Source:** [vv02 - Hàm_UpdateState(v)]
- **Tag:** [vv02]

- **Fact:** Chế độ Fail-safe (An toàn) trong lập trình IoT giúp tự động ngắt thiết bị (tắt relay, quạt, đóng servo) và gửi cảnh báo khi cảm biến lỗi hoặc mất kết nối WiFi.
- **Source:** [vv02 - Khối an toàn (Fail-safe & Reconnect)]
- **Tag:** [vv02]

- **Fact:** Biến `INPUT_TYPE` không phải là khối lệnh có sẵn mà là một biến kiểu Chuỗi (Text) do người dùng tự tạo để định danh loại cảm biến đang sử dụng trong code.
- **Source:** [vv02 - Giải thích biến INPUT_TYPE]
- **Tag:** [vv02]

- **Fact:** App.ohstem.vn cho phép chạy nhiều vòng lặp "Lặp lại mỗi ... giây" song song để xử lý đa nhiệm (đọc sensor, gửi data, kiểm tra an toàn).
- **Source:** [vv02 - Gợi ý hoàn thiện trước khi thi]
- **Tag:** [vv02]

- **Fact:** Cảm biến ánh sáng (LDR) trên Yolo UNO trả về giá trị ADC trong khoảng từ 0 đến 4095.
- **Source:** [vv02 - Tham số sẵn cho 6 chủ đề]
- **Tag:** [vv02]

- **Fact:** Cảm biến siêu âm trả về giá trị khoảng cách đơn vị cm và trả về giá trị lỗi (-1 hoặc 0) khi không xác định được vật cản.
- **Source:** [vv02 - Hàm_ReadSensor() / Khối an toàn]
- **Tag:** [vv02]

- **Fact:** Quạt DC kết nối với Yolo UNO có thể điều chỉnh tốc độ thông qua lệnh ghi giá trị Analog (PWM) từ 0 đến 255.
- **Source:** [vv02 - Hàm_ParseCmd(cmd)]
- **Tag:** [vv02]

- **Fact:** Việc xử lý nhiều đầu vào (Multi-input) đồng thời yêu cầu tạo các biến EMA riêng biệt cho từng cảm biến và sử dụng logic hợp nhất như AND/OR để ra quyết định điều khiển.
- **Source:** [vv02 - Cách tổ chức tổng quát cho nhiều input]
- **Tag:** [vv02]

- **Fact:** Dữ liệu IoT gửi qua MQTT thường được đóng gói dưới dạng chuỗi CSV (ví dụ: "thời_gian,trạng_thái,giá_trị") để tối ưu băng thông.
- **Source:** [vv02 - Hàm_ToCSV]
- **Tag:** [vv02]

- **Fact:** Để đồng bộ thời gian thực cho các bản tin log dữ liệu, Yolo UNO cần lấy thời gian từ máy chủ NTP sau khi kết nối WiFi thành công.
- **Source:** [vv02 - Khởi động hệ thống]
- **Tag:** [vv02]
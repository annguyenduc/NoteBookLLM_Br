Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **v02** về IoT, Robotics và thuật toán cảm biến:

- **Fact:** [CONV] Cảm biến ánh sáng LDR trên Yolo UNO trả về giá trị analog trong dải từ 0 đến 4095, với đặc điểm giá trị thấp tương ứng với môi trường tối.
- **Source:** [vv02 - Section: 2) Nhiệm vụ đọc & lọc / Section: 🧠 1️⃣ Lý thuyết cơ bản]
- **Tag:** [vv02]

- **Fact:** [CONV] Để tối ưu độ ổn định cho cảm biến siêu âm, nên sử dụng phương pháp lấy giá trị trung vị (median) từ 3 mẫu đo liên tiếp thay vì lấy giá trị đơn lẻ.
- **Source:** [vv02 - Section: Gợi ý nhanh / Section: B. Siêu âm]
- **Tag:** [vv02]

- **Fact:** [CONV] Thuật toán lọc nhiễu EMA (Exponential Moving Average) được tính theo công thức: $EMA_{mới} = \alpha \times Giá\_trị_{mới} + (1 - \alpha) \times EMA_{cũ}$.
- **Source:** [vv02 - Section: 🧠 1️⃣ Công thức nhắc lại]
- **Tag:** [vv02]

- **Fact:** [CONV] Hệ số $\alpha = 0.2$ trong thuật toán EMA được khuyến nghị cho các cảm biến môi trường như LDR hoặc DHT20 để cân bằng giữa khả năng lọc nhiễu và tốc độ phản ứng.
- **Source:** [vv02 - Section: 🧩 4️⃣ Vì sao chọn α = 0.2]
- **Tag:** [vv02]

- **Fact:** [CONV] Kỹ thuật Hysteresis sử dụng hai ngưỡng (T_high và T_low) giúp hệ thống tránh tình trạng thiết bị đầu ra (như LED, Relay) bị bật/tắt liên tục (nhấp nháy) khi tín hiệu cảm biến dao động quanh điểm biên.
- **Source:** [vv02 - Section: 🧠 1️⃣ Lý thuyết “Hysteresis”]
- **Tag:** [vv02]

- **Fact:** [CONV] Đối với dải giá trị ADC 12-bit (0-4095), khoảng chênh lệch (gap) giữa hai ngưỡng Hysteresis hợp lý thường nằm trong khoảng từ 150 đến 300 đơn vị.
- **Source:** [vv02 - Section: ✅ Kết luận nhanh]
- **Tag:** [vv02]

- **Fact:** [CONV] Có 4 phương pháp phổ biến để hợp nhất dữ liệu cảm biến (Sensor Fusion): AND (đủ điều kiện), OR (một trong các điều kiện), WEIGHT (tính điểm theo trọng số) và MAJORITY (bỏ phiếu đa số).
- **Source:** [vv02 - Section: 3) Hợp nhất nhiều cảm biến (Fusion)]
- **Tag:** [vv02]

- **Fact:** [CONV] Trong chế độ điều khiển Servo, cần thêm khoảng thời gian chờ từ 300ms đến 500ms sau lệnh điều khiển để chống giật và đảm bảo cơ cấu cơ khí kịp di chuyển đến vị trí.
- **Source:** [vv02 - Section: 4) Điều khiển output tức thời]
- **Tag:** [vv02]

- **Fact:** [CONV] Trạng thái FAILSAFE sẽ được kích hoạt để tắt toàn bộ đầu ra nếu mất kết nối Wi-Fi/MQTT quá 3 lần hoặc cảm biến không trả về giá trị hợp lệ trong hơn 10 giây.
- **Source:** [vv02 - Section: 6) An toàn]
- **Tag:** [vv02]

- **Fact:** [CONV] Để tránh hiện tượng EMA hội tụ chậm khi bắt đầu chương trình, nên khởi tạo giá trị EMA bằng chính giá trị đọc thực tế đầu tiên của cảm biến thay vì mặc định bằng 0.
- **Source:** [vv02 - Section: 🟨 (3) Nếu bạn muốn EMA “bắt đầu nhanh hơn”]
- **Tag:** [vv02]

- **Fact:** [CONV] Tần suất lấy mẫu tối ưu đề xuất cho cảm biến ánh sáng là mỗi 0.2 giây và cảm biến siêu âm là mỗi 0.08 giây để đảm bảo hệ thống hoạt động mượt mà.
- **Source:** [vv02 - Section: 2) Nhiệm vụ đọc & lọc]
- **Tag:** [vv02]
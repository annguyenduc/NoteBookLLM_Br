Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu về IoT, Arduino, YoloBit và Robotics trong nguồn cung cấp:

- **Fact:** Cảm biến ánh sáng (LDR) trên Yolo UNO trả về giá trị analog trong dải từ 0 đến 4095, trong đó giá trị thấp tương ứng với môi trường tối.
- **Source:** [vv02 - Section: 1) Gợi ý nhanh & 1) Lý thuyết cơ bản]
- **Tag:** [vv02]

- **Fact:** Để ổn định dữ liệu từ cảm biến siêu âm, phương pháp tối ưu là lấy giá trị trung vị (median) của 3 mẫu đo liên tiếp để loại bỏ nhiễu.
- **Source:** [vv02 - Section: 1) Gợi ý nhanh & 3) Siêu âm]
- **Tag:** [vv02]

- **Fact:** Thuật toán EMA (Exponential Moving Average) được sử dụng để lọc mượt tín hiệu cảm biến với công thức: $L_{ema} = \alpha \cdot L_x + (1 - \alpha) \cdot L_{ema}$.
- **Source:** [vv02 - Section: 2) Nhiệm vụ đọc & lọc]
- **Tag:** [vv02]

- **Fact:** Hệ số $\alpha$ (alpha) trong thuật toán EMA quyết định độ mượt; giá trị $\alpha = 0.2$ thường được chọn cho cảm biến ánh sáng để cân bằng giữa khả năng lọc nhiễu và tốc độ phản ứng.
- **Source:** [vv02 - Section: 6) Tổng kết (Assistant)]
- **Tag:** [vv02]

- **Fact:** Cơ chế Hysteresis (trễ) sử dụng hai ngưỡng ($T_{high}$ và $T_{low}$) để ngăn chặn hiện tượng thiết bị bật/tắt liên tục (nhấp nháy) khi tín hiệu dao động quanh một ngưỡng duy nhất.
- **Source:** [vv02 - Section: 2) Nhiệm vụ đọc & lọc & 1) Lý thuyết Hysteresis]
- **Tag:** [vv02]

- **Fact:** Khoảng chênh lệch (Hysteresis gap) khuyến nghị cho cảm biến ánh sáng trong môi trường nhà ở ổn định thường nằm trong khoảng 100–150 đơn vị trên thang đo 4095.
- **Source:** [vv02 - Section: 2) Khoảng chênh hợp lý (Assistant)]
- **Tag:** [vv02]

- **Fact:** Có 4 phương pháp hợp nhất dữ liệu cảm biến (Sensor Fusion) phổ biến: AND (đủ điều kiện), OR (chỉ cần 1 điều kiện), WEIGHT (tính điểm theo trọng số) và MAJORITY (bỏ phiếu đa số).
- **Source:** [vv02 - Section: 3) Hợp nhất nhiều cảm biến]
- **Tag:** [vv02]

- **Fact:** Trong phương pháp tính điểm WEIGHT, công thức gợi ý là $Score = 0.6 \cdot L_{dark} + 0.4 \cdot U_{close}$, với ngưỡng kích hoạt thường đặt ở mức 0.55.
- **Source:** [vv02 - Section: 3) Hợp nhất nhiều cảm biến - Cách 3]
- **Tag:** [vv02]

- **Fact:** Khi điều khiển Servo, cần thêm khoảng thời gian chờ từ 300–500ms sau lệnh di chuyển để chống giật và bảo vệ thiết bị.
- **Source:** [vv02 - Section: 4) Điều khiển output tức thời]
- **Tag:** [vv02]

- **Fact:** Chế độ an toàn (FAILSAFE) sẽ tự động tắt mọi output và báo lỗi nếu mất kết nối Wi-Fi/MQTT quá 3 lần hoặc cảm biến không trả về giá trị hợp lệ quá 10 giây.
- **Source:** [vv02 - Section: 6) An toàn]
- **Tag:** [vv02]

- **Fact:** Để tránh việc giá trị EMA mất thời gian "hội tụ" từ 0, nên khởi tạo giá trị `ema` bằng chính giá trị đọc thực tế đầu tiên của cảm biến.
- **Source:** [vv02 - Section: 3) Lý do chính dẫn đến sự khác biệt (Assistant)]
- **Tag:** [vv02]

- **Fact:** Việc sử dụng các vòng lặp "lặp lại mỗi ... giây" thay cho lệnh `delay` giúp hệ thống có thể xử lý đa nhiệm (song song) nhiều cảm biến và tác vụ cùng lúc.
- **Source:** [vv02 - Section: Mẹo khi dựng khối]
- **Tag:** [vv02]
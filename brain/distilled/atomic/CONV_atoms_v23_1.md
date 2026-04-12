Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v23:

**1. Robot & Thám hiểm Sao Hoả**
- **Fact:** [CONV] Robot Perseverance đã thực hiện thử nghiệm di chuyển quãng đường 6,5m trên bề mặt Sao Hoả với các thao tác: tiến lên, quay tại chỗ và đi lùi.
- **Source:** [v23 - Section: Conversation: Robot Khám Phá Sao Hoả]
- **Tag:** [vv23]

- **Fact:** [CONV] Quy trình EDL (Entry, Descent, and Landing - Nhập cảnh, hạ cánh và đáp xuống) là quá trình di chuyển từ đỉnh khí quyển xuống bề mặt Sao Hoả, bao gồm hàng ngàn bước kỹ thuật chính xác.
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Tàu thăm dò đi vào khí quyển Sao Hoả ở góc nghiêng 12 độ với vận tốc gần 13.000 dặm/giờ; góc quá dốc sẽ làm tàu bị cháy, góc quá nông sẽ khiến tàu bật khỏi khí quyển.
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Tàu InSight sử dụng 6 thiết bị nổ (pyrotechnic devices) để loại bỏ mảng chắn nhiệt sau khi dù siêu thanh (supersonic parachute) bung được 15 giây.
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Động cơ của tàu đổ bộ phải tắt ngay lập tức tại thời điểm tiếp xúc bề mặt Sao Hoả để tránh tình trạng tàu bị lật úp.
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

**2. Cảm biến & Thuật toán điều khiển**
- **Fact:** [CONV] Thuật toán thoát khỏi mê cung hang đá cho robot sử dụng kết hợp cảm biến ánh sáng (để tìm lối ra dựa trên cường độ sáng > 50) và cảm biến siêu âm (để phát hiện và né vật cản).
- **Source:** [v23 - Section: Conversation: Robot Khám Phá Sao Hoả]
- **Tag:** [vv23]

- **Fact:** [CONV] Trong logic điều khiển ưu tiên tránh vật cản: Nếu phát hiện vật cản bằng cảm biến siêu âm, robot sẽ quay đầu hoặc quay trái/phải bất kể điều kiện ánh sáng có đạt ngưỡng tìm lối ra hay không.
- **Source:** [v23 - Section: Conversation: Robot Khám Phá Sao Hoả]
- **Tag:** [vv23]

- **Fact:** [CONV] Radar hạ cánh trên tàu vũ trụ (như InSight) sử dụng tần số vô tuyến (radio frequency) thay vì sóng siêu âm vì sóng vô tuyến có thể truyền trong chân không, trong khi sóng siêu âm cần môi trường vật chất (không khí, nước).
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

- **Fact:** [CONV] Sóng cơ học (âm thanh và sóng đàn hồi) có thể ứng dụng trên Sao Hoả để khảo sát địa hình, cấu trúc vỏ đất đá và khám phá các tầng địa chất dưới lòng đất.
- **Source:** [v23 - Section: Conversation: Mars Landing Process Explanation]
- **Tag:** [vv23]

**3. Lập trình (Python)**
- **Fact:** [CONV] Cấu trúc lập trình điều khiển robot cơ bản thường bao gồm các hàm khởi tạo cảm biến (`__init__`), các hàm hành động (`move_forward`, `turn_left`, `turn_right`) và vòng lặp kiểm tra điều kiện thoát (`while not is_exit_reached`).
- **Source:** [v23 - Section: Conversation: Robot Khám Phá Sao Hoả]
- **Tag:** [vv23]
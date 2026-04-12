Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** MQTT broker sẽ tự động tạo topic khi có dữ liệu được publish đến topic đó lần đầu tiên, người dùng không cần tạo thủ công.
- **Source:** [vv02 - Bước 2: Tạo chương trình khối]
- **Tag:** [vv02]

- **Fact:** Các công cụ như MQTT Explorer (web) và MQTT Dash (mobile) có thể dùng để kiểm tra và theo dõi dữ liệu MQTT với Host `test.mosquitto.org` và Port `1883`.
- **Source:** [vv02 - Bước 3: Kiểm tra trên MQTT Explorer]
- **Tag:** [vv02]

- **Fact:** Trên thiết bị Yolo:Bit, chân P1 thường được sử dụng để kết nối module cảm biến hồng ngoại (IR).
- **Source:** [vv02 - 1. Điểm đúng (rất tốt)]
- **Tag:** [vv02]

- **Fact:** Để tránh tình trạng nghẽn mạng hoặc spam dữ liệu lên MQTT broker, nên thêm khoảng trễ (ví dụ 0.2 giây) sau mỗi lần gửi dữ liệu.
- **Source:** [vv02 - 2. Điểm cần chỉnh nhỏ]
- **Tag:** [vv02]

- **Fact:** Hệ thống OhStem IoT Dashboard sử dụng khái niệm "Kênh thông tin" (V1, V2, V3...) tương ứng với các topic con trong giao thức MQTT.
- **Source:** [vv02 - 🧠 Giải thích nhanh (Dashboard IoT)]
- **Tag:** [vv02]

- **Fact:** Trên Yolo UNO (sử dụng ESP32), không nên sử dụng chân D3 cho cảm biến IR vì trùng với chân UART/TX; thay vào đó nên sử dụng chân D6 hoặc D7.
- **Source:** [vv02 - 1. Chân cắm IR (Yolo UNO)]
- **Tag:** [vv02]

- **Fact:** Các vi điều khiển ESP32 (như trên Yolo UNO) không chịu được điện áp 5V ở các chân đầu vào, do đó cảm biến IR nên được cấp nguồn 3.3V.
- **Source:** [vv02 - 1. Chân cắm IR & 6. Những lỗi thường gặp khác trên UNO]
- **Tag:** [vv02]

- **Fact:** Hầu hết các remote hồng ngoại phổ thông (như remote TV) sử dụng giao thức truyền tin NEC.
- **Source:** [vv02 - 3. Các chỉnh nhỏ khác (khuyến nghị)]
- **Tag:** [vv02]

- **Fact:** Trong khối lệnh MQTT của OhStem "gửi ... đến chủ đề ...", tham số thứ nhất là dữ liệu (message) và tham số thứ hai là kênh/chủ đề (channel/topic).
- **Source:** [vv02 - 1. Bạn đang gửi sai kênh và đảo ngược tham số publish]
- **Tag:** [vv02]

- **Fact:** Biến `tín hiệu` là biến hệ thống tự động sinh ra bên trong khối sự kiện "khi nhận được tín hiệu từ remote", chứa mã IR vừa nhận được.
- **Source:** [vv02 - 1. “tín hiệu” là gì?]
- **Tag:** [vv02]

- **Fact:** Khối lệnh "đọc tín hiệu thu từ remote" là hàm đọc chủ động (polling), thường được đặt trong vòng lặp "lặp lại mãi" để kiểm tra dữ liệu IR mới.
- **Source:** [vv02 - 2. “đọc tín hiệu từ remote” là gì?]
- **Tag:** [vv02]

- **Fact:** Việc sử dụng biến bổ trợ (như `last_published`) để so sánh với giá trị hiện tại (`latest_code`) là kỹ thuật cần thiết để tránh gửi trùng lặp dữ liệu lên server MQTT.
- **Source:** [vv02 - 1. Điểm đúng (rất tốt) & 2. Điểm cần chỉnh nhỏ]
- **Tag:** [vv02]

- **Fact:** Để điều khiển thiết bị từ xa qua IR, chương trình cần so sánh mã nhận được với mã định danh của từng nút bấm trên remote (ví dụ: mã 162 để bật, mã 98 để tắt).
- **Source:** [vv02 - 2. Ví dụ: Điều khiển đèn (relay hoặc LED)]
- **Tag:** [vv02]
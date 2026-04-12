Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (v02) về IoT, Arduino, YoloBit, Robotics và AI theo quy tắc LOM v4.1:

- Fact: [CONV] Hiệu chỉnh (calibrate) cảm biến giúp mô hình học được đặc trưng thực tế thay vì lỗi hệ thống.
- Source: [v02 - Section: Hiệu chỉnh cảm biến]
- Tag: [vv02]

- Fact: [CONV] Trích xuất đặc trưng (feature extraction) như MFCC cho âm thanh hoặc FFT cho rung động giúp giảm khối lượng tính toán và nhiễu cho mô hình chính.
- Source: [v02 - Section: Trích xuất đặc trưng (feature extraction)]
- Tag: [vv02]

- Fact: [CONV] Nền tảng Edge Impulse và TinyML cho phép định nghĩa khối DSP để xử lý dữ liệu cảm biến trước khi đưa vào mạng neural.
- Source: [v02 - Section: Trích xuất đặc trưng (feature extraction)]
- Tag: [vv02]

- Fact: [CONV] Tăng cường dữ liệu (data augmentation) bằng cách xoay ảnh, thay đổi độ sáng hoặc thêm nhiễu nhân tạo giúp mô hình tổng quát tốt hơn và tránh overfit.
- Source: [v02 - Section: Tăng cường dữ liệu (data augmentation)]
- Tag: [vv02]

- Fact: [CONV] Giao thức MQTT nhanh hơn HTTP REST từ 20–25 lần trong việc truyền dữ liệu IoT liên tục.
- Source: [v02 - Section: Sử dụng giao thức nhẹ (MQTT) thay vì HTTP]
- Tag: [vv02]

- Fact: [CONV] Thư viện PubSubClient trên Arduino hỗ trợ MQTT với các tính năng hữu ích như QoS (Chất lượng dịch vụ) và Last Will (Di chúc cuối cùng).
- Source: [v02 - Section: Sử dụng giao thức nhẹ (MQTT) thay vì HTTP]
- Tag: [vv02]

- Fact: [CONV] ESP-NOW là giao thức không dây riêng của Espressif cho phép truyền dữ liệu trực tiếp giữa các chip ESP32 rất nhanh và nhẹ, bỏ qua tầng TCP/IP.
- Source: [v02 - Section: Lựa chọn công nghệ truyền phù hợp]
- Tag: [vv02]

- Fact: [CONV] Chip ESP32-S3 hỗ trợ tập lệnh vector giúp tăng tốc tính toán AI/DSP thông qua các thư viện ESP-DSP và ESP-NN.
- Source: [v02 - Section: Tận dụng tăng tốc phần cứng của ESP32-S3]
- Tag: [vv02]

- Fact: [CONV] ESP32-S3 sở hữu lõi phụ ULP (ultra-low-power) có khả năng theo dõi cảm biến trong khi CPU chính đang ở chế độ Deep Sleep.
- Source: [v02 - Section: Quản lý năng lượng thông minh]
- Tag: [vv02]

- Fact: [CONV] TensorFlow Lite Micro trên ESP32-S3 tích hợp các kernel tối ưu (ESP-NN) để tăng tốc các phép tính ma trận và tích chập.
- Source: [v02 - Section: Nền tảng TinyML (TensorFlow Lite Micro và Edge Impulse)]
- Tag: [vv02]

- Fact: [CONV] Module Camera AI V2 của OhStem có khả năng tự xử lý các tác vụ nặng như nhận diện khuôn mặt, giúp giảm tải cho vi điều khiển chính Yolo UNO.
- Source: [v02 - Section: OhStem AI Camera và ứng dụng kèm theo]
- Tag: [vv02]

- Fact: [CONV] Lọc mũ (exponential smoothing) là phương pháp làm mượt dữ liệu cảm biến hiệu quả với công thức: ema = α*đọc_mới + (1-α)*ema.
- Source: [v02 - Section: 1) Lấy mẫu & làm sạch tín hiệu (độ chính xác)]
- Tag: [vv02]

- Fact: [CONV] Kỹ thuật Hysteresis với 2 ngưỡng (T_high, T_low) giúp hệ thống ra quyết định ổn định, tránh tình trạng chập chờn khi dữ liệu sát ngưỡng.
- Source: [v02 - Section: 2) Quyết định không “giật” (hysteresis & bỏ phiếu)]
- Tag: [vv02]

- Fact: [CONV] Sử dụng khối lệnh "mỗi ... ms" thay vì "delay" giúp thực hiện đa nhiệm (multitasking) mượt mà trên app.ohstem.vn.
- Source: [v02 - Section: 3) Vòng lặp không chặn & nhịp lấy mẫu hợp lý (hiệu suất)]
- Tag: [vv02]

- Fact: [CONV] Các thiết bị đầu vào (Input) phổ biến trong hackathon gồm: Cảm biến ánh sáng (LDR), siêu âm (HC-SR04), DHT20 và Nút nhấn.
- Source: [v02 - Section: ⚙️ 1. Danh sách cảm biến (Input)]
- Tag: [vv02]

- Fact: [CONV] Các thiết bị đầu ra (Output) phổ biến gồm: LED đơn, LED RGB, Servo, Relay, LCD 1602 và Động cơ DC.
- Source: [v02 - Section: 💡 2. Danh sách thiết bị điều khiển (Output)]
- Tag: [vv02]

- Fact: [CONV] Các chủ đề thực tế thường gặp trong thi đấu IoT AI gồm: Môi trường, Y tế, Giáo dục, Giao thông/An toàn, Năng lượng.
- Source: [v02 - Section: 🌱 Chủ đề: Môi trường / 🏥 Chủ đề: Y tế / 🏫 Chủ đề: Giáo dục / 🚦 Chủ đề: Giao thông / An toàn]
- Tag: [vv02]
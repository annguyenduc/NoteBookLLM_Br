Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v14) về IoT, Arduino và lập trình:

- **Fact**: [CONV] Cảm biến DHT11 phiên bản 3 chân có sơ đồ kết nối tiêu chuẩn: chân VCC nối nguồn 3.3V hoặc 5V, chân OUT (Data) nối với chân Digital của vi điều khiển, và chân GND nối cực âm.
- **Source**: [v14] - Section: 1. Chuẩn bị phần cứng (Hướng dẫn lập trình DHT11 3 PIN)
- **Tag**: [vv14]

- **Fact**: [CONV] Để lập trình DHT11 trên môi trường Arduino IDE, người dùng cần cài đặt hai thư viện bắt buộc là "DHT sensor library by Adafruit" và "Adafruit Unified Sensor".
- **Source**: [v14] - Section: 2. Lập trình trên Arduino - Bước 1: Cài thư viện
- **Tag**: [vv14]

- **Fact**: [CONV] Lỗi nạp code "stk500_cmd(): programmer is out of sync" trên Arduino thường do các nguyên nhân: cáp USB hỏng, chọn sai cổng COM/Board, hoặc chân TX/RX đang bị chiếm dụng bởi linh kiện khác.
- **Source**: [v14] - Section: Lỗi mà bạn gặp phải ("avrdude: stk500_cmd(): programmer is out of sync")
- **Tag**: [vv14]

- **Fact**: [CONV] Đối với các dòng board Arduino không chính hãng (clone), khi gặp lỗi nạp code, người dùng thường phải chọn tùy chọn Processor là "ATmega328P (Old Bootloader)" trong menu Tools.
- **Source**: [v14] - Section: 4. Xử lý trong IDE (Hướng dẫn khắc phục lỗi kết nối)
- **Tag**: [vv14]

- **Fact**: [CONV] Cảm biến DHT11 có thông số hoạt động: điện áp 3.3V - 5.5V DC, dòng tiêu thụ khi đo là 0.3 mA, và chu kỳ lấy mẫu tối thiểu là 1 giây (1Hz).
- **Source**: [v14] - Section: Hãy cho tôi biết thông số hoạt động thông thường của DHT11 - 1. Thông số chung
- **Tag**: [vv14]

- **Fact**: [CONV] Phạm vi đo lường của DHT11 giới hạn trong khoảng 0°C đến 50°C (sai số ±2°C) về nhiệt độ và 20% đến 90% RH (sai số ±5%) về độ ẩm.
- **Source**: [v14] - Section: Hãy cho tôi biết thông số hoạt động thông thường của DHT11 - 2. Phạm vi đo
- **Tag**: [vv14]

- **Fact**: [CONV] DHT11 sử dụng giao thức truyền thông một dây (Single-Wire Digital Signal) với tốc độ truyền khoảng 1 kHz và có thể truyền xa tối đa 20m nếu có điện trở pull-up 10kΩ phù hợp.
- **Source**: [v14] - Section: Hãy cho tôi biết thông số hoạt động thông thường của DHT11 - 3. Giao tiếp
- **Tag**: [vv14]

- **Fact**: [CONV] So với DHT11, cảm biến DHT22 có hiệu suất cao hơn với dải đo nhiệt độ từ -40 đến 80°C (sai số ±0.5°C) và độ ẩm từ 0 đến 100% (sai số ±2%).
- **Source**: [v14] - Section: Hãy cho tôi biết thông số hoạt động thông thường của DHT11 - 7. So sánh nhanh với DHT22
- **Tag**: [vv14]

- **Fact**: [CONV] Để giải phóng cổng Serial đang bị chiếm dụng trên Arduino IDE, người dùng có thể đóng Serial Monitor/Plotter hoặc sử dụng lệnh `Serial.end()` trực tiếp trong mã nguồn để ngắt kết nối phần mềm.
- **Source**: [v14] - Section: NGẮT PORT TRÊN ARDUINO IDE
- **Tag**: [vv14]

- **Fact**: [CONV] Trong thiết kế giao diện (UI) cho ứng dụng/game, màu xanh lá (green) và vàng (yellow) được phân loại là màu sáng, do đó nên sử dụng màu chữ tối (như đen) để đảm bảo độ tương phản và dễ đọc.
- **Source**: [v14] - Section: Cập nhật mã (Phần phản hồi về màu xanh lá)
- **Tag**: [vv14]
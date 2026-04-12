Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Cảm biến DHT11 phiên bản 3 chân có sơ đồ kết nối: Chân VCC nối nguồn 3.3V hoặc 5V, chân OUT (Data) nối với chân Digital của vi điều khiển, và chân GND nối với cực âm.
- **Source:** [v14 - Section: 1. Chuẩn bị phần cứng (Lập trình DHT11 Arduino)]
- **Tag:** [vv14]

- **Fact:** Để lập trình DHT11 trên Arduino IDE, cần cài đặt hai thư viện là "DHT sensor library by Adafruit" và "Adafruit Unified Sensor".
- **Source:** [v14 - Section: Bước 1: Cài thư viện (Lập trình DHT11 Arduino)]
- **Tag:** [vv14]

- **Fact:** Cảm biến DHT11 có độ chính xác hạn chế với sai số nhiệt độ khoảng ±2°C và sai số độ ẩm khoảng ±5%.
- **Source:** [v14 - Section: 4. Ghi chú (Lập trình DHT11 Arduino)]
- **Tag:** [vv14]

- **Fact:** Lỗi "avrdude: stk500_cmd(): programmer is out of sync" thường do kết nối USB kém, chọn sai Board/Port, hoặc có thiết bị kết nối vào chân TX (0) và RX (1) gây nhiễu khi nạp code.
- **Source:** [v14 - Section: 1. Kiểm tra phần cứng & 2. Kiểm tra trong Arduino IDE (Lỗi nạp code)]
- **Tag:** [vv14]

- **Fact:** Đối với các bo mạch Arduino không chính hãng (clone), đôi khi cần chọn tùy chọn "ATmega328P (Old Bootloader)" trong menu Processor để có thể nạp code thành công.
- **Source:** [v14 - Section: 4. Xử lý trong IDE (Lỗi nạp code)]
- **Tag:** [vv14]

- **Fact:** Thông số hoạt động của DHT11: Điện áp 3.3V - 5.5V DC; Dòng tiêu thụ khi đo là 0.3 mA; Chu kỳ lấy mẫu tối thiểu là 1 giây (1Hz).
- **Source:** [v14 - Section: 1. Thông số chung (Thông số hoạt động của DHT11)]
- **Tag:** [vv14]

- **Fact:** Phạm vi đo của DHT11: Nhiệt độ từ 0°C đến 50°C (độ phân giải 1°C); Độ ẩm từ 20% đến 90% RH (độ phân giải 1% RH).
- **Source:** [v14 - Section: 2. Phạm vi đo (Thông số hoạt động của DHT11)]
- **Tag:** [vv14]

- **Fact:** DHT11 sử dụng giao thức truyền thông một dây (Single-Wire Digital Signal) và có thể truyền xa tối đa 20m nếu sử dụng điện trở pull-up 10kΩ phù hợp.
- **Source:** [v14 - Section: 3. Giao tiếp (Thông số hoạt động của DHT11)]
- **Tag:** [vv14]

- **Fact:** Trong lập trình giao diện (như Pygame), để đảm bảo độ tương phản, nên sử dụng màu chữ sáng (White) cho nền tối (Red, Blue) và màu chữ tối (Black) cho nền sáng (Green, Yellow).
- **Source:** [v14 - Section: 2. Chọn màu chữ dựa trên màu khối (Cập nhật mã)]
- **Tag:** [vv14]

- **Fact:** Máy lạnh làm mát bằng cách ngưng tụ hơi nước, thường khiến độ ẩm trong phòng giảm xuống mức 40% - 60% RH.
- **Source:** [v14 - Section: 2. Độ ẩm (Khi bật máy lạnh 16 độ C)]
- **Tag:** [vv14]

- **Fact:** Cảm biến DHT11 cần khoảng 1-2 phút để ổn định và đưa ra số đo chính xác khi thay đổi môi trường nhiệt độ/độ ẩm.
- **Source:** [v14 - Section: 3. Thời gian thích nghi (Khi bật máy lạnh 16 độ C)]
- **Tag:** [vv14]

- **Fact:** Lệnh `Serial.end()` trong code Arduino được sử dụng để ngắt kết nối Serial Port từ phía phần mềm.
- **Source:** [v14 - Section: 5. Ngắt kết nối Serial bằng Code]
- **Tag:** [vv14]
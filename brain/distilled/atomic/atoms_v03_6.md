Dưới đây là các sự kiện kỹ thuật được trích xuất từ nội dung bạn cung cấp, tuân thủ quy tắc LOM v4.1:

- **Fact**: Board Yolo UNO (chip ESP32-S3) sử dụng bộ chuyển đổi ADC 12-bit, do đó giá trị cảm biến ánh sáng đọc được sẽ nằm trong khoảng từ 0 đến 4095 thay vì 0-1023 như các dòng Arduino cũ (10-bit).
- **Source**: [vv03] - Section: 🧩 1. Vì sao không phải 0–1023?
- **Tag**: [vv03]

- **Fact**: Lỗi E10 (biến `PORTS_DIGITAL` chưa được khởi tạo) xảy ra khi sử dụng extension `xbot_extension_tiny_rgb` trên Yolo UNO mà không có board mở rộng XBot, do extension này được thiết kế riêng cho hệ sinh thái robot XBot.
- **Source**: [vv03] - Section: 🔍 Giải thích lỗi E10 (PORTS_DIGITAL)
- **Tag**: [vv03]

- **Fact**: Sơ đồ ánh xạ (mapping) giữa Cổng (Port) và Chân (Pin) Digital trên Yolo UNO: Cổng 1 (D13), Cổng 2 (D2), Cổng 3 (D15), Cổng 4 (D4), Cổng 5 (D16), Cổng 6 (D17).
- **Source**: [vv03] - Section: 🧩 2. Phân biệt Cổng và Chân
- **Tag**: [vv03]

- **Fact**: Để điều khiển LED NeoPixel (Tiny RGB) trên Yolo UNO bằng MicroPython, cần sử dụng thư viện `neopixel` với cấu trúc: `np = neopixel.NeoPixel(Pin(PIN), NUM)`.
- **Source**: [vv03] - Section: Cách 1: Dùng trực tiếp thư viện neopixel
- **Tag**: [vv03]

- **Fact**: Công thức làm mượt dữ liệu cảm biến (Smoothing) để tránh đèn nhấp nháy: `ema = int(0.8 * ema + 0.2 * raw)`.
- **Source**: [vv03] - Section: A) MicroPython
- **Tag**: [vv03]

- **Fact**: Để thực hiện hiệu ứng "tối thì đèn sáng" (đảo chiều), giá trị độ sáng LED (0-255) được tính từ giá trị cảm biến (0-4095) theo công thức: `level = 255 - (raw * 255 // 4096)`.
- **Source**: [vv03] - Section: A) MicroPython
- **Tag**: [vv03]

- **Fact**: Khi sử dụng dải LED RGB, bắt buộc phải nối chung chân GND giữa nguồn cấp ngoài, dải LED và board điều khiển (Yolo UNO).
- **Source**: [vv03] - Section: 5) Lưu ý hay gặp
- **Tag**: [vv03]

- **Fact**: Để xem dữ liệu Serial trên phiên bản web của app.ohstem.vn, người dùng cần tìm các biểu tượng hoặc tab có tên "Console", "Serial Monitor", hoặc "Terminal" trong giao diện lập trình.
- **Source**: [vv03] - Section: 2. Mở giao diện Serial trong app.ohstem.vn
- **Tag**: [vv03]

- **Fact**: Để tắt sạch các LED RGB khi khởi động (tránh nhấp nháy ngẫu nhiên), nên gọi lệnh `np.fill((0,0,0))` và `np.write()` ở đầu chương trình.
- **Source**: [vv03] - Section: 5) Lưu ý hay gặp
- **Tag**: [vv03]

- **Fact**: Nếu không có khối "Chèn mã Python" và extension Tiny RGB bị lỗi, phương án khả thi nhất để lập trình đèn theo môi trường trên Yolo UNO là chuyển sang chế độ lập trình Arduino (C++) sử dụng thư viện `Adafruit_NeoPixel`.
- **Source**: [vv03] - Section: Cách A (khuyên dùng nếu vẫn muốn dùng Tiny RGB/WS2812)
- **Tag**: [vv03]
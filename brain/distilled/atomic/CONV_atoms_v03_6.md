Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v03) về IoT, Arduino, YoloBit, Robotics và AI:

- Fact: [CONV] Thư viện `Adafruit_NeoPixel.h` được sử dụng trong môi trường Arduino để điều khiển LED RGB (WS2812).
- Source: (v03 - Section: Arduino code snippet)
- Tag: [vv03]

- Fact: [CONV] Khi kết nối LED với Yolo UNO, bắt buộc phải nối chung cực âm (GND) giữa board mạch và dải LED, ngay cả khi sử dụng nguồn 5V ngoài cho LED.
- Source: (v03 - Section: 5) Lưu ý hay gặp)
- Tag: [vv03]

- Fact: [CONV] Để xử lý hiện tượng LED nhấp nháy ngẫu nhiên khi khởi động trong MicroPython, cần gọi lệnh `np.fill((0,0,0))` và `np.write()` ở đầu chương trình để tắt sạch các điểm ảnh.
- Source: (v03 - Section: 5) Lưu ý hay gặp)
- Tag: [vv03]

- Fact: [CONV] Khối lệnh "Tiny RGB" trong giao diện lập trình của OhStem thuộc extension `xbot_extension_tiny_rgb`, là một wrapper cho hàm Python `tiny_rgb.show(port, (R, G, B))`.
- Source: (v03 - Section: 1. Cấu trúc của khối)
- Tag: [vv03]

- Fact: [CONV] Trên Yolo UNO, các cổng kết nối Grove/RJ11 được ánh xạ (mapping) tới các chân Digital cụ thể: Cổng 1 (D13), Cổng 2 (D2), Cổng 3 (D15), Cổng 4 (D4), Cổng 5 (D16), Cổng 6 (D17).
- Source: (v03 - Section: 2. Phân biệt Cổng và Chân)
- Tag: [vv03]

- Fact: [CONV] Lỗi mã E10 (biến `PORTS_DIGITAL` chưa được khởi tạo) xảy ra khi sử dụng extension Tiny RGB trên Yolo UNO vì extension này được thiết kế riêng cho hệ sinh thái robot XBot.
- Source: (v03 - Section: 🔍 Giải thích lỗi E10 (PORTS_DIGITAL))
- Tag: [vv03]

- Fact: [CONV] Yolo UNO sử dụng chip ESP32-S3 với bộ chuyển đổi Analog-to-Digital (ADC) có độ phân giải 12-bit, trả về giá trị trong khoảng từ 0 đến 4095.
- Source: (v03 - Section: 🧩 1. Vì sao không phải 0–1023?)
- Tag: [vv03]

- Fact: [CONV] Trong lập trình MicroPython cho ESP32-S3, lệnh `light_adc.atten(ADC.ATTN_11DB)` được sử dụng để cấu hình ADC đọc dải điện áp rộng nhất (khoảng 0 đến 3.3V).
- Source: (v03 - Section: A) MicroPython - 2) Code)
- Tag: [vv03]

- Fact: [CONV] Để điều khiển LED RGB (WS2812/NeoPixel) trên Yolo UNO mà không dùng extension, người dùng có thể sử dụng trực tiếp thư viện `neopixel` có sẵn trong MicroPython hoặc thư viện `Adafruit_NeoPixel` trong Arduino.
- Source: (v03 - Section: Cách 1: Dùng trực tiếp thư viện neopixel)
- Tag: [vv03]

- Fact: [CONV] Các chân hỗ trợ điều chế độ rộng xung (PWM) trên Yolo UNO bao gồm D3, D5, D6, D9, D10, D11, cho phép điều khiển độ sáng LED mượt mà thay vì chỉ bật/tắt.
- Source: (v03 - Section: A. Phần cứng cần có)
- Tag: [vv03]

- Fact: [CONV] Chân D13 trên Yolo UNO thường không hỗ trợ chức năng PWM, do đó không thể thực hiện các hiệu ứng làm mờ (dimming) mượt mà cho LED.
- Source: (v03 - Section: A. Phần cứng cần có)
- Tag: [vv03]

- Fact: [CONV] Thuật toán làm mượt dữ liệu cảm biến (Smoothing) đơn giản có thể thực hiện bằng công thức trung bình trượt: `ema = (0.8 * ema + 0.2 * raw)`.
- Source: (v03 - Section: A) MicroPython - 2) Code)
- Tag: [vv03]
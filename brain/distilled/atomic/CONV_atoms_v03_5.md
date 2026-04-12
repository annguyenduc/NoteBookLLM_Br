Chào bạn, tôi là **@scout**. Dưới đây là các sự kiện kỹ thuật đã được trích xuất và chưng cất từ nguồn dữ liệu **Volume v03** liên quan đến IoT, Arduino, YoloBit, Robotics và AI.

--------------------------------------------------

- **Fact:** [CONV] Lỗi `ValueError: duty must be from 0 to 1023` trên Yolo UNO xảy ra khi hàm `write_analog()` nhận giá trị nằm ngoài khoảng 0-1023 hoặc nhận giá trị không phải số nguyên (float).
- **Source:** [vv03 - Section: Lỗi ValueError & 1) Cô lập nguyên nhân]
- **Tag:** [vv03]

- **Fact:** [CONV] Board Yolo UNO tích hợp chip ESP32S3 và chạy firmware MicroPython (phiên bản v1.22.2).
- **Source:** [vv03 - Section: Raw REPL Log]
- **Tag:** [vv03]

- **Fact:** [CONV] Các chân hỗ trợ xuất xung PWM trên Yolo UNO bao gồm: D3, D5, D6, D9, D10 và D11.
- **Source:** [vv03 - Section: 5) Kiểm tra chân & phần cứng]
- **Tag:** [vv03]

- **Fact:** [CONV] Bộ chuyển đổi Analog-to-Digital (ADC) trên ESP32 mặc định có độ phân giải 12-bit, trả về giá trị trong dải từ 0 đến 4095.
- **Source:** [vv03 - Section: Thông số ADC của ESP32 / MicroPython]
- **Tag:** [vv03]

- **Fact:** [CONV] Tổ hợp phím `Ctrl + D` trong giao diện REPL của OhStem thực hiện lệnh "Soft Reboot", giúp khởi động lại board, xóa biến và dừng các tác vụ (tasks) đang chạy mà không cần ngắt nguồn.
- **Source:** [vv03 - Section: ⚙️ 2. Các phím điều khiển chính trong REPL]
- **Tag:** [vv03]

- **Fact:** [CONV] Tổ hợp phím `Ctrl + B` dùng để thoát khỏi chế độ "raw REPL" để quay lại chế độ nhập lệnh tương tác bình thường.
- **Source:** [vv03 - Section: ⚙️ 2. Các phím điều khiển chính trong REPL]
- **Tag:** [vv03]

- **Fact:** [CONV] Module LED Tiny RGB (WS2812/NeoPixel) sử dụng 3 chân kết nối: VCC (5V), GND và DIN (Data). Trên Yolo UNO, chân DIN thường được kết nối vào chân D13.
- **Source:** [vv03 - Section: 1) Nhận dạng module & 2) Cắm dây với Yolo UNO]
- **Tag:** [vv03]

- **Fact:** [CONV] Để chuyển đổi an toàn giá trị cảm biến ánh sáng (0-4095) sang giá trị PWM (0-1023) mà không bị lỗi vượt biên (1024), nên sử dụng phép chia lấy phần nguyên cho 4096: `(light * 1023) // 409
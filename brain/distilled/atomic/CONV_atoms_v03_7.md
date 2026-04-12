Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v03:

- Fact: [CONV] Yolo UNO và các board sử dụng ESP32 có độ phân giải ADC là 12-bit, trả về giá trị trong khoảng từ 0 đến 4095.
- Source: [Phần 1: 32): 0–4095 (12-bit) và Phần 4: Bảng so sánh Board]
- Tag: [vv03]

- Fact: [CONV] Arduino UNO có độ phân giải ADC là 10-bit, trả về giá trị trong khoảng từ 0 đến 1023.
- Source: [Phần 4: Bảng so sánh Board]
- Tag: [vv03]

- Fact: [CONV] Giá trị cảm biến ánh sáng đọc được tương ứng với môi trường: Ánh sáng yếu khoảng 100–500; Ánh sáng mạnh khoảng 3500–4095.
- Source: [Phần 2: Cách hiểu kết quả của bạn]
- Tag: [vv03]

- Fact: [CONV] Công thức toán học tổng quát để ánh xạ (map) một giá trị x từ khoảng [in_min, in_max] sang khoảng [out_min, out_max] là: y = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min.
- Source: [Phần 1: Công thức “map” tổng quát]
- Tag: [vv03]

- Fact: [CONV] Để chuyển đổi nhanh giá trị từ 12-bit (Yolo UNO) sang 10-bit (Arduino UNO), có thể sử dụng công thức: x10bit = x / 4.
- Source: [Phần 2: Các công thức nhanh thường dùng - mục a]
- Tag: [vv03]

- Fact: [CONV] Công thức điều khiển độ sáng LED (PWM 0-255) nghịch với cường độ ánh sáng (0-4095) để trời tối thì LED sáng mạnh: pwm = round( (4095 - x) * 255 / 4095 ).
- Source: [Phần 2: Các công thức nhanh thường dùng - mục c]
- Tag: [vv03]

- Fact: [CONV] Trên Yolo UNO, các chân hỗ trợ xuất tín hiệu PWM bao gồm: D3, D5, D6, D9, D10, và D11.
- Source: [Phần 2: Các công thức nhanh thường dùng - mục c và Phần 3: Lưu ý]
- Tag: [vv03]

- Fact: [CONV] Trên giao diện app.ohstem.vn, khối lệnh để điều khiển PWM nằm trong nhóm "Chân I/O" (hoặc "Đầu vào/ra"), mục "Analog", có tên là "Ghi giá trị analog (PWM)" hoặc "Xuất ra giá trị analog...".
- Source: [Phần 3: Cách tạo khối “ghi PWM chân D5 = pwm”]
- Tag: [vv03]

- Fact: [CONV] Việc hiệu chuẩn (calibration) cảm biến thực tế giúp xác định khoảng giá trị thực (dark_min và bright_max) để tính toán PWM chính xác hơn, tránh sai số khi cảm biến không đạt mức 0 hoặc 4095 tuyệt đối.
- Source: [Phần 3: Map theo calibration thực tế]
- Tag: [vv03]

- Fact: [CONV] Trong giáo dục STEM, các dự án phổ biến bao gồm lập trình Robot Rover, ứng dụng AI cơ bản, và tổ chức các cuộc thi như AI Hackathon.
- Source: [Phần CV: Kinh nghiệm làm việc và Dự án & Thành tựu]
- Tag: [vv03]
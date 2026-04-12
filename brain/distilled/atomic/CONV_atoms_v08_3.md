Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu **Volume v08** về chủ đề IoT, YoloBit và Robotics:

- **Fact:** [CONV] Để tệp JSON có thể import thành công vào nền tảng `app.ohstem.vn`, cấu trúc dữ liệu bắt buộc phải bao gồm trường `"mode": "block"`.
- **Source:** [v08 - Section: Vấn đề và Giải pháp]
- **Tag:** [vv08]

- **Fact:** [CONV] Khối lệnh điều khiển motor đặc thù của Rover (`rover_move_motor`) cho phép điều chỉnh tốc độ độc lập cho bánh trái (`left_wheel_speed`) và bánh phải (`right_wheel_speed`).
- **Source:** [v08 - Section: 3. Cập nhật rover_converter.py]
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ thống YoloBit hỗ trợ các khối lệnh MQTT chuyên dụng bao gồm: kết nối WiFi (`yolobit_mqtt_connect_wifi`), kết nối server MQTT mặc định (`yolobit_mqtt_connect_default_servers`), xử lý sự kiện nhận tin nhắn (`yolobit_mqtt_on_receive_message`) và kiểm tra tin nhắn mới (`yolobit_mqtt_check_message`).
- **Source:** [v08 - Section: 3. Cập nhật rover_converter.py]
- **Tag:** [vv08]

- **Fact:** [CONV] Các khối lệnh sự kiện (Events) trên YoloBit cho phép lập trình theo cơ chế gửi tin nhắn quảng bá (`yolobit_events_broadcast_message`) và kích hoạt hành động khi nhận tin nhắn (`yolobit_events_message`).
- **Source:** [v08 - Section: 3. Cập nhật rover_converter.py]
- **Tag:** [vv08]

- **Fact:** [CONV] Trong quá trình chuyển đổi từ MicroPython sang Blockly, các hàm Python cơ bản được ánh xạ tương ứng: `print()` chuyển thành `text_print`, gán biến chuyển thành `variables_set`, và cấu trúc `if/else` chuyển thành `controls_if`.
- **Source:** [v08 - Section: Lộ trình (Plan-first)]
- **Tag:** [vv08]

- **Fact:** [CONV] YoloBit hỗ trợ các khối hiển thị (Display) cơ bản để tương tác với người dùng bao gồm hiển thị chuỗi văn bản (`yolobit_basic_show_string`) và hiển thị hình ảnh (`yolobit_basic_show_image`).
- **Source:** [v08 - Section: 3. Cập nhật rover_converter.py]
- **Tag:** [vv08]

- **Fact:** [CONV] Cấu trúc `xmlText` trong tệp cấu hình Blockly phải tuân thủ định dạng XML của Google Blockly, bắt đầu bằng thẻ `<xml xmlns="https://developers.google.com/blockly/xml">` và kết thúc bằng thẻ `</xml>`.
- **Source:** [v08 - Section: 4. Khung file mẫu để Agent tạo]
- **Tag:** [vv08]

- **Fact:** [CONV] Khối lệnh điều khiển logic nâng cao trên Rover bao gồm lệnh "Chờ cho đến khi" (`block_wait_until`), cho phép tạm dừng luồng chương trình cho tới khi một điều kiện (`condition`) cụ thể được thỏa mãn.
- **Source:** [v08 - Section: 3. Cập nhật rover_converter.py]
- **Tag:** [vv08]
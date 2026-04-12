Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu cung cấp:

- **Fact:** Để tệp JSON có thể import thành công vào nền tảng `app.ohstem.vn`, bắt buộc phải có trường dữ liệu `"mode": "block"`.
- **Source:** [vv08] - Section: Vấn đề và Giải pháp (Mục 1).
- **Tag:** [vv08]

- **Fact:** Cấu trúc tệp JSON của OhStem yêu cầu trường `xmlText` phải chứa nội dung XML hợp lệ, bắt đầu bằng thẻ `<xml ...>` và kết thúc bằng `</xml>`.
- **Source:** [vv08] - Section: 5) Checklist xác minh.
- **Tag:** [vv08]

- **Fact:** Dự án Rover trên YoloBit yêu cầu các khối lệnh (extensions) chuyên biệt để xử lý MQTT, Events và điều khiển motor nâng cao.
- **Source:** [vv08] - Section: Vấn đề và Giải pháp (Mục 2).
- **Tag:** [vv08]

- **Fact:** Các khối lệnh MQTT cho YoloBit bao gồm: `yolobit_mqtt_connect_wifi` (kết nối WiFi), `yolobit_mqtt_connect_default_servers` (kết nối server), `yolobit_mqtt_on_receive_message` (nhận tin nhắn) và `yolobit_mqtt_check_message`.
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Các khối lệnh sự kiện (Events) cho YoloBit gồm: `yolobit_events_broadcast_message` (gửi tin nhắn broadcast), `yolobit_events_message` (tin nhắn event) và `yolobit_events_run` (chạy events).
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Khối lệnh `rover_move_motor` được sử dụng để điều khiển tốc độ riêng biệt cho từng bánh xe của robot Rover.
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Khối lệnh hiển thị cơ bản trên YoloBit bao gồm `yolobit_basic_show_string` (hiển thị chuỗi) và `yolobit_basic_show_image` (hiển thị hình ảnh).
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Khối lệnh `yolobit_input_button_is_pressed` dùng để kiểm tra trạng thái nhấn nút trên thiết bị YoloBit.
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Trong Cursor, các quy tắc dự án (Project Rules) được lưu trữ trong thư mục `.cursor/rules/` với định dạng file `.mdc` hoặc `.md`.
- **Source:** [vv08] - Section: 0) Quy ước nhanh & 5) Lỗi thường gặp.
- **Tag:** [vv08]

- **Fact:** Việc thiết lập model "Auto" trong Cursor giúp tối ưu hóa chi phí sử dụng (cost-safe) bằng cách tránh sử dụng các frontier model đắt đỏ khi không cần thiết.
- **Source:** [vv08] - Section: 1) Mục tiêu & mô hình (Usage Guardian).
- **Tag:** [vv08]

- **Fact:** Khối lệnh `block_wait_until` thuộc nhóm điều khiển (Control), dùng để tạm dừng chương trình cho đến khi một điều kiện cụ thể được thỏa mãn.
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Khối lệnh `math_change` được sử dụng để thay đổi giá trị của một biến (tăng hoặc giảm).
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Khối lệnh `logic_operation` thực hiện các phép toán logic cơ bản như AND, OR, và NOT.
- **Source:** [vv08] - Section: 3. Cập nhật tools/converters/rover_converter.py (Hàm _define_rover_blocks).
- **Tag:** [vv08]

- **Fact:** Custom Mode trong Cursor cho phép người dùng cấu hình riêng biệt về Model, công cụ (Tools) được phép sử dụng (Search, Codebase, Read/Edit file, Run, Web) và hướng dẫn (Instructions) cho từng loại tác vụ.
- **Source:** [vv08] - Section: Tạo custom mode như thế nào?.
- **Tag:** [vv08]
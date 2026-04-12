Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** [CONV] Công cụ **Rover Converter Tool** hỗ trợ chuyển đổi mã nguồn (MicroPython) sang định dạng tệp JSON chính xác để có thể import thành công vào giao diện lập trình `app.ohstem.vn`.
- **Source:** [vv08] - Section: Kết luận.
- **Tag:** [vv08]

- **Fact:** [CONV] Thiết bị **YoloBit** sử dụng phần mở rộng (extension) dành riêng cho xe điều khiển Rover với ID là `yolobit-AITT-VN-yolobit_extension_rover`, được lưu trữ trên GitHub của AITT-VN.
- **Source:** [vv08] - Section: extensions.
- **Tag:** [vv08]

- **Fact:** [CONV] Các khối lệnh (blocks) cơ bản để điều khiển xe Rover bao gồm: `rover_stop` (dừng lại), `rover_move_motor` (điều khiển tốc độ bánh trái/phải), `rover_move_delay` (di chuyển theo thời gian), và `rover_show_rgb_led_all` (hiển thị màu đèn LED RGB).
- **Source:** [vv08] - Section: xmlText.
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ sinh thái **Stemkit** tích hợp với YoloBit cung cấp các khối lệnh cho nhiều loại cảm biến và module: siêu âm (`stemkit_ultrasonic`), màn hình `stemkit_lcd1602`, máy bơm mini (`stemkit_mini_pump`), cảm biến độ ẩm đất (`stemkit_soil_sensor`), cảm biến gas, cảm biến chạm `mpr121`, cảm biến ánh sáng, âm thanh và cảm biến nhiệt độ độ ẩm DHT.
- **Source:** [vv08] - Section: xmlText.
- **Tag:** [vv08]

- **Fact:** [CONV] Cấu trúc tệp cấu hình cho YoloBit trên OhStem App yêu cầu các trường thông tin bắt buộc: `mode` (thường đặt là "block"), `xmlText` (chứa mã XML của Blockly), `python` (chứa mã nguồn Python tương ứng), và khai báo `device` là "yolobit".
- **Source:** [vv08] - Section: template_base.json.
- **Tag:** [vv08]

- **Fact:** [CONV] Trong cấu trúc XML của Blockly, các biến được quản lý trong thẻ `<variables>` với mỗi biến có một `id` duy nhất và tên biến (ví dụ: var1, var2).
- **Source:** [vv08] - Section: xmlText.
- **Tag:** [vv08]
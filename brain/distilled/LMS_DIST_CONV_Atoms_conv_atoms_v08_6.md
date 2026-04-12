---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v08_6
  title: CONV_atoms_v08_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v08) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Thiết bị phần cứng mục tiêu được xác định trong template là YoloBit.
- **Source:** [Dữ liệu RAW - dòng: "device": "yolobit"]
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ thống tích hợp phần mở rộng "ROVER" (yolobit-AITT-VN-yolobit_extension_rover) chuyên dụng cho bộ kit xe điều khiển Rover.
- **Source:** [Dữ liệu RAW - Section: "extensions"]
- **Tag:** [vv08]

- **Fact:** [CONV] Các khối lệnh điều khiển chuyển động của Rover bao gồm: di chuyển motor với tốc độ tùy chỉnh (`rover_move_motor`), dừng xe (`rover_stop`), di chuyển theo thời gian trễ (`rover_move_delay`) và di chuyển cơ bản (`rover_move`).
- **Source:** [Dữ liệu RAW - xmlText: các block type rover_move_motor, rover_stop, rover_move_delay, rover_move]
- **Tag:** [vv08]

- **Fact:** [CONV] Rover hỗ trợ cảm biến dò đường (line sensor) với hai chế độ: đọc toàn bộ các mắt cảm biến (`rover_line_sensor_read_all`) hoặc đọc đơn lẻ (`rover_line_sensor_read_single`).
- **Source:** [Dữ liệu RAW - xmlText: các block type rover_line_sensor_read_all, rover_line_sensor_read_single]
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ thống hỗ trợ điều khiển LED RGB trên xe Rover (`rover_show_rgb_led_all`) và hệ thống LED tích hợp trên YoloBit (`yolobit_led_set_all`).
- **Source:** [Dữ liệu RAW - xmlText: các block type rover_show_rgb_led_all, yolobit_led_set_all]
- **Tag:** [vv08]

- **Fact:** [CONV] Bộ Stemkit cung cấp các khối lệnh cho cảm biến môi trường: cảm biến độ ẩm đất (`stemkit_soil_sensor`), cảm biến gas (`stemkit_gas_sensor`), cảm biến ánh sáng (`stemkit_light_sensor`), cảm biến âm thanh (`stemkit_sound_sensor`) và cảm biến nhiệt độ/độ ẩm DHT (`stemkit_dht_measure`, `stemkit_dht_read`).
- **Source:** [Dữ liệu RAW - xmlText: các block type stemkit_soil_sensor, stemkit_gas_sensor, stemkit_light_sensor, stemkit_sound_sensor, stemkit_dht_measure]
- **Tag:** [vv08]

- **Fact:** [CONV] Các thiết bị chấp hành và hiển thị trong Stemkit bao gồm: màn hình LCD1602 (`stemkit_lcd1602_clear`), máy bơm mini (`stemkit_mini_pump`), và module phát âm thanh theo track (`stemkit_sound_playtrack`).
- **Source:** [Dữ liệu RAW - xmlText: các block type stemkit_lcd1602_clear, stemkit_mini_pump, stemkit_sound_playtrack]
- **Tag:** [vv08]

- **Fact:** [CONV] Cảm biến siêu âm (ultrasonic) hỗ trợ hai chức năng chính: đọc giá trị khoảng cách (`stemkit_ultrasonic_read`) và kiểm tra điều kiện khoảng cách so với một ngưỡng xác định (`stemkit_ultrasonic_checkdistance`).
- **Source:** [Dữ liệu RAW - xmlText: các block type stemkit_ultrasonic_read, stemkit_ultrasonic_checkdistance]
- **Tag:** [vv08]

- **Fact:** [CONV] Module cảm biến chạm MPR121 được tích hợp đầy đủ các lệnh: kiểm tra trạng thái (`check`), đọc giá trị (`read`), xóa trạng thái (`clear`), quét thiết bị (`scan`) và tắt âm thanh cảnh báo (`sound_off`).
- **Source:** [Dữ liệu RAW - xmlText: các block type stemkit_mpr121_check, stemkit_mpr121_read, stemkit_mpr121_clear, stemkit_mpr121_scan, stemkit_mpr121_sound_off]
- **Tag:** [vv08]

- **Fact:** [CONV] Ngôn ngữ lập trình khối hỗ trợ các cấu trúc logic phức tạp: định nghĩa hàm (`procedures_defnoreturn`), vòng lặp `while` (`controls_whileUntil`), câu lệnh điều kiện `if` (`controls_if`) và quản lý biến số (`variables_set`, `variables_get`).
- **Source:** [Dữ liệu RAW - xmlText: các block type procedures_defnoreturn, controls_whileUntil, controls_if, variables_set]
- **Tag:** [vv08]

- **Fact:** [CONV] File `template_base.json` được tạo ra thông qua quá trình hợp nhất tự động từ hai nguồn: `yolobit_blocks_template.json` và `template_tri.json`.
- **Source:** [Dữ liệu RAW - Section: "metadata" -> "source_templates"]
- **Tag:** [vv08]
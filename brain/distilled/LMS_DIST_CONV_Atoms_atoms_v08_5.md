---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v08_5
  title: atoms_v08_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cấu hình của hệ thống YoloBit và robot Rover:

- **Fact:** Thiết bị trung tâm được sử dụng trong cấu hình này là YoloBit.
- **Source:** (Dữ liệu RAW - dòng: `"device": "yolobit"`)
- **Tag:** [vv08]

- **Fact:** Hệ thống tích hợp phần mở rộng dành riêng cho robot Rover (ROVER) có mã định danh là `yolobit-AITT-VN-yolobit_extension_rover`, được cung cấp bởi AITT-VN.
- **Source:** (Dữ liệu RAW - Section: extensions)
- **Tag:** [vv08]

- **Fact:** Robot Rover hỗ trợ các tập lệnh di chuyển cơ bản bao gồm: dừng lại (`rover_stop`), di chuyển với tốc độ tùy chỉnh (`rover_move`), di chuyển kèm thời gian chờ (`rover_move_delay`) và điều khiển độc lập tốc độ hai bánh xe (`rover_move_motor`).
- **Source:** (Dữ liệu RAW - xmlText: block type="rover_stop", "rover_move", "rover_move_delay", "rover_move_motor")
- **Tag:** [vv08]

- **Fact:** Khả năng dò đường của Rover được thực hiện qua các khối lệnh đọc cảm biến line, cho phép đọc toàn bộ các mắt cảm biến (`rover_line_sensor_read_all`) hoặc đọc từng mắt đơn lẻ (`rover_line_sensor_read_single`).
- **Source:** (Dữ liệu RAW - xmlText: block type="rover_line_sensor_read_all", "rover_line_sensor_read_single")
- **Tag:** [vv08]

- **Fact:** Hệ thống hỗ trợ đa dạng các cảm biến môi trường thuộc bộ StemKit như: cảm biến siêu âm (`ultrasonic`), cảm biến độ ẩm đất (`soil_sensor`), cảm biến khí gas (`gas_sensor`), cảm biến ánh sáng (`light_sensor`), cảm biến âm thanh (`sound_sensor`) và cảm biến nhiệt độ, độ ẩm DHT (`dht_measure`).
- **Source:** (Dữ liệu RAW - xmlText: block type="stemkit_ultrasonic_read", "stemkit_soil_sensor", "stemkit_gas_sensor", "stemkit_light_sensor", "stemkit_sound_sensor", "stemkit_dht_measure")
- **Tag:** [vv08]

- **Fact:** Các thiết bị ngoại vi và cơ cấu chấp hành được hỗ trợ bao gồm: máy bơm mini (`stemkit_mini_pump`), màn hình LCD1602 (`stemkit_lcd1602_clear`), module phát nhạc (`stemkit_sound_playtrack`) và hệ thống đèn LED RGB trên cả YoloBit và Rover.
- **Source:** (Dữ liệu RAW - xmlText: block type="stemkit_mini_pump", "stemkit_lcd1602_clear", "stemkit_sound_playtrack", "yolobit_led_set_all", "rover_show_rgb_led_all")
- **Tag:** [vv08]

- **Fact:** Module cảm biến chạm MPR121 được tích hợp với đầy đủ các chức năng: kiểm tra trạng thái chạm, đọc giá trị, xóa bộ nhớ đệm, quét thiết bị và tắt âm thanh cảnh báo.
- **Source:** (Dữ liệu RAW - xmlText: block type="stemkit_mpr121_check", "stemkit_mpr121_read", "stemkit_mpr121_clear", "stemkit_mpr121_scan", "stemkit_mpr121_sound_off")
- **Tag:** [vv08]

- **Fact:** Môi trường lập trình Blockly cho YoloBit hỗ trợ các cấu trúc logic lập trình tiêu chuẩn như: định nghĩa hàm (`procedures_defnoreturn`), vòng lặp (`controls_whileUntil`), câu lệnh điều kiện (`controls_if`) và quản lý biến số.
- **Source:** (Dữ liệu RAW - xmlText: block type="procedures_defnoreturn", "controls_whileUntil", "controls_if", "variables_set")
- **Tag:** [vv08]
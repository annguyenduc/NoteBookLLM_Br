---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v08_6
  title: atoms_v08_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v08):

- **Fact:** YoloBit hỗ trợ phần mở rộng (extension) chuyên dụng cho bộ kit xe điều khiển Rover với tên gọi "ROVER".
- **Source:** JSON field "extensions", name: "ROVER".
- **Tag:** [vv08]

- **Fact:** Phần mở rộng Rover cho YoloBit được phát triển bởi AITT-VN và lưu trữ mã nguồn trên GitHub tại địa chỉ: `https://github.com/AITT-VN/yolobit_extension_rover`.
- **Source:** JSON field "extensions", id: "yolobit-AITT-VN-yolobit_extension_rover", src: "https://github.com/AITT-VN/yolobit_extension_rover".
- **Tag:** [vv08]

- **Fact:** Hệ thống khối lệnh của xe Rover bao gồm các chức năng điều khiển động cơ bánh trái/phải độc lập (rover_move_motor), dừng xe (rover_stop), di chuyển với tốc độ và thời gian xác định (rover_move_delay).
- **Source:** xmlText, block types: "rover_move_motor", "rover_stop", "rover_move_delay".
- **Tag:** [vv08]

- **Fact:** Xe Rover tích hợp cảm biến dò đường (line sensor) cho phép đọc giá trị của từng cảm biến đơn lẻ hoặc toàn bộ các mắt đọc cùng lúc.
- **Source:** xmlText, block types: "rover_line_sensor_read_all", "rover_line_sensor_read_single".
- **Tag:** [vv08]

- **Fact:** Bộ kit xe Rover hỗ trợ hiển thị màu sắc thông qua hệ thống đèn LED RGB tích hợp.
- **Source:** xmlText, block type: "rover_show_rgb_led_all".
- **Tag:** [vv08]

- **Fact:** Hệ sinh thái Stem kit cho YoloBit bao gồm đa dạng các cảm biến: siêu âm (ultrasonic), độ ẩm đất (soil sensor), khí gas (gas sensor), ánh sáng (light sensor), âm thanh (sound sensor) và cảm biến nhiệt độ, độ ẩm (DHT).
- **Source:** xmlText, block types: "stemkit_ultrasonic_read", "stemkit_soil_sensor", "stemkit_gas_sensor", "stemkit_light_sensor", "stemkit_sound_sensor", "stemkit_dht_measure".
- **Tag:** [vv08]

- **Fact:** Stem kit hỗ trợ các thiết bị chấp hành và hiển thị như máy bơm mini (mini pump), màn hình LCD1602 và module cảm biến chạm MPR121 (hỗ trợ quét, đọc và kiểm tra trạng thái chạm).
- **Source:** xmlText, block types: "stemkit_mini_pump", "stemkit_lcd1602_clear", "stemkit_mpr121_scan", "stemkit_mpr121_read".
- **Tag:** [vv08]

- **Fact:** YoloBit sử dụng giao diện lập trình kéo thả dựa trên Blockly XML để quản lý các biến, hàm (procedures) và logic điều khiển.
- **Source:** xmlText, xmlns="https://developers.google.com/blockly/xml".
- **Tag:** [vv08]

- **Fact:** Cấu trúc dữ liệu của template lập trình YoloBit (template_base.json) được hợp nhất từ hai nguồn chính là `yolobit_blocks_template.json` và `template_tri.json`.
- **Source:** JSON field "metadata", "source_templates".
- **Tag:** [vv08]
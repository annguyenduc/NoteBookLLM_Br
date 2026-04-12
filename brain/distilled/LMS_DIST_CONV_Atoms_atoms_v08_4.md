---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v08_4
  title: atoms_v08_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v08):

- **Fact:** Bộ công cụ **Rover Converter Tool** được thiết kế để tạo ra các tệp JSON có định dạng tương thích để import vào nền tảng `app.ohstem.vn`.
- **Source:** (vv08 - Section: Kết luận)
- **Tag:** [vv08]

- **Fact:** Cấu trúc của tệp JSON cấu hình cho YoloBit bao gồm các trường dữ liệu chính: `mode` (thường là "block"), `xmlText` (chứa mã XML của Blockly), `python` (mã nguồn Python tương ứng), `name`, `extensions`, và `device`.
- **Source:** (vv08 - Section: Dữ liệu mẫu JSON)
- **Tag:** [vv08]

- **Fact:** Thiết bị mục tiêu được xác định trong cấu hình là `yolobit`.
- **Source:** (vv08 - Section: Dữ liệu mẫu JSON - trường device)
- **Tag:** [vv08]

- **Fact:** Extension dành cho xe Rover có ID là `yolobit-AITT-VN-yolobit_extension_rover`, được lưu trữ tại GitHub của AITT-VN.
- **Source:** (vv08 - Section: Dữ liệu mẫu JSON - trường extensions)
- **Tag:** [vv08]

- **Fact:** Các khối lệnh (blocks) đặc thù cho Rover bao gồm: `rover_stop` (dừng xe), `rover_move_motor` (điều khiển tốc độ 2 bánh), `rover_line_sensor_read_all` (đọc cảm biến dò đường), `rover_move_delay` (di chuyển có thời gian chờ), `rover_move` (di chuyển với tốc độ xác định), `rover_line_sensor_read_single`, và `rover_show_rgb_led_all`.
- **Source:** (vv08 - Section: xmlText content)
- **Tag:** [vv08]

- **Fact:** Hệ thống hỗ trợ các khối lệnh mở rộng từ Stemkit như: cảm biến siêu âm (`stemkit_ultrasonic_read`), màn hình LCD (`stemkit_lcd1602_clear`), máy bơm mini (`stemkit_mini_pump`), cảm biến đất (`stemkit_soil_sensor`), cảm biến gas (`stemkit_gas_sensor`), cảm biến chạm (`stemkit_mpr121`), và cảm biến môi trường DHT (`stemkit_dht_measure`).
- **Source:** (vv08 - Section: xmlText content - các block type stemkit_*)
- **Tag:** [vv08]

- **Fact:** Trong cấu trúc XML của Blockly, các biến được quản lý trong thẻ `<variables>` với mỗi biến có một `id` duy nhất và tên hiển thị (ví dụ: `var1`, `var2`, `var3`).
- **Source:** (vv08 - Section: xmlText content - thẻ variables)
- **Tag:** [vv08]

- **Fact:** Khối lệnh điều khiển logic và vòng lặp bao gồm `controls_if` (cấu trúc điều kiện) và `controls_whileUntil` (vòng lặp while).
- **Source:** (vv08 - Section: xmlText content - block type controls_*)
- **Tag:** [vv08]
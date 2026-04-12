Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu raw về hệ sinh thái YoloBit, Rover và Stemkit:

- **Fact:** [CONV] Hệ sinh thái YoloBit hỗ trợ các khối lệnh điều khiển xe Rover bao gồm: dừng xe (`rover_stop`), di chuyển với tốc độ xác định (`rover_move`) và di chuyển kèm thời gian chờ (`rover_move_delay`).
- **Source:** Raw XML blocks: `rover_stop`, `rover_move`, `rover_move_delay`.
- **Tag:** [vv08]

- **Fact:** [CONV] Xe Rover được trang bị cảm biến dò đường (line sensor) với hai chế độ đọc: đọc tất cả các mắt cảm biến (`rover_line_sensor_read_all`) hoặc đọc từng mắt cảm biến đơn lẻ (`rover_line_sensor_read_single`).
- **Source:** Raw XML blocks: `rover_line_sensor_read_all`, `rover_line_sensor_read_single`.
- **Tag:** [vv08]

- **Fact:** [CONV] Bộ Stemkit tích hợp đa dạng cảm biến phục vụ IoT và Robotics bao gồm: cảm biến siêu âm (`stemkit_ultrasonic_read`), độ ẩm đất (`stemkit_soil_sensor`), cảm biến gas (`stemkit_gas_sensor`), ánh sáng (`stemkit_light_sensor`), âm thanh (`stemkit_sound_sensor`) và cảm biến DHT để đo nhiệt độ, độ ẩm (`stemkit_dht_measure`).
- **Source:** Raw XML blocks: `stemkit_ultrasonic_read`, `stemkit_soil_sensor`, `stemkit_gas_sensor`, `stemkit_light_sensor`, `stemkit_sound_sensor`, `stemkit_dht_measure`.
- **Tag:** [vv08]

- **Fact:** [CONV] Các thiết bị chấp hành (actuators) và hiển thị trong Stemkit bao gồm: máy bơm mini (`stemkit_mini_pump`), đèn LED nhỏ (`stemkit_led_tiny`), loa phát nhạc (`stemkit_sound_playtrack`) và màn hình LCD1602 (`stemkit_lcd1602_clear`).
- **Source:** Raw XML blocks: `stemkit_mini_pump`, `stemkit_led_tiny`, `stemkit_sound_playtrack`, `stemkit_lcd1602_clear`.
- **Tag:** [vv08]

- **Fact:** [CONV] YoloBit hỗ trợ module cảm biến chạm MPR121 với đầy đủ các tập lệnh: kiểm tra (`check`), đọc giá trị (`read`), quét thiết bị (`scan`) và xóa dữ liệu (`clear`).
- **Source:** Raw XML blocks: `stemkit_mpr121_check`, `stemkit_mpr121_read`, `stemkit_mpr121_scan`, `stemkit_mpr121_clear`.
- **Tag:** [vv08]

- **Fact:** [CONV] Khối lệnh `rover_move_delay` cho phép người dùng lập trình xe di chuyển với tham số tốc độ (speed) và thời gian (time) cụ thể (ví dụ: tốc độ 50 trong 1 giây).
- **Source:** Raw XML block: `rover_move_delay` với các value name "speed" và "time".
- **Tag:** [vv08]

- **Fact:** [CONV] Phần mở rộng dành cho xe Rover (ROVER extension) có ID là `yolobit-AITT-VN-yolobit_extension_rover`, được lưu trữ chính thức tại GitHub của AITT-VN.
- **Source:** JSON content - extensions: `id`, `src`.
- **Tag:** [vv08]

- **Fact:** [CONV] Cảm biến siêu âm trong bộ kit có khả năng kiểm tra khoảng cách so với một ngưỡng định trước thông qua khối lệnh `stemkit_ultrasonic_checkdistance`.
- **Source:** Raw XML block: `stemkit_ultrasonic_checkdistance`.
- **Tag:** [vv08]
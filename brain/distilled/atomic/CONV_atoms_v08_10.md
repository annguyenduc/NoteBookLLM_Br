Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu lập trình robot Rover trên nền tảng YoloBit:

- Fact: [CONV] Chương trình sử dụng thuật toán PID để điều khiển robot Rover bám line (follow line) với các tham số khởi tạo: Kp=18, Ki=0, Kd=8 và tốc độ cơ sở là 30.
- Source: [xmlText - block id="proc_setup" và "proc_pid"]
- Tag: [vv08]

- Fact: [CONV] Robot Rover thực hiện đọc dữ liệu từ 4 cảm biến line đơn lẻ thông qua các kênh (CH) 1, 2, 3 và 4 để xác định vị trí trên đường line.
- Source: [xmlText - block type="rover_line_sensor_read_single"]
- Tag: [vv08]

- Fact: [CONV] Công thức tính sai số (error) để bám line dựa trên trọng số của 4 cảm biến: `e = (L1*3 + L2*1) - (R1*1 + R2*3)`.
- Source: [xmlText - block id="b_set_e"]
- Tag: [vv08]

- Fact: [CONV] Hệ thống quản lý hành vi robot bằng cấu trúc máy trạng thái (State Machine) trong hàm `scheduler`, bao gồm các trạng thái: `FOLLOW` (bám line), `TASK1` (do_task_trong_cay), và `TASK2` (do_task_tai_che).
- Source: [xmlText - block id="proc_sched"]
- Tag: [vv08]

- Fact: [CONV] YoloBit hỗ trợ giao tiếp MQTT cho các ứng dụng IoT thông qua thư viện mở rộng có ID `yolobit-AITT-VN-yolobit_extension_mqtt`.
- Source: [extensions - id: "yolobit-AITT-VN-yolobit_extension_mqtt"]
- Tag: [vv08]

- Fact: [CONV] Thư viện mở rộng `ROBOCON` (yolobit_extension_robocon_rover) cung cấp các khối lệnh bổ sung chuyên dụng cho việc thi đấu Robocon với robot Rover.
- Source: [extensions - id: "yolobit-AITT-VN-yolobit_extension_robocon_rover"]
- Tag: [vv08]

- Fact: [CONV] Robot thực hiện hiệu chỉnh tốc độ động cơ trái và phải dựa trên giá trị `correction` từ bộ điều khiển PID: Động cơ trái = `base_speed + correction`, Động cơ phải = `base_speed - correction`.
- Source: [xmlText - block id="b_move_pid"]
- Tag: [vv08]

- Fact: [CONV] Hàm `detect_intersection` (phát hiện giao lộ) thực hiện tính tổng giá trị của cả 4 cảm biến line (L1, L2, R1, R2) để lưu vào biến `INTER`.
- Source: [xmlText - block id="proc_detect"]
- Tag: [vv08]
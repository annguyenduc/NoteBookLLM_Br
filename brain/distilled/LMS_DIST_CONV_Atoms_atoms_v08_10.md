---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v08_10
  title: atoms_v08_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu raw về dự án lập trình robot Rover trên nền tảng YoloBit:

- **Fact:** Dự án có tên "Rover_Robotcon_PID_SM", được thiết kế chuyên biệt cho thiết bị YoloBit để thực hiện các nhiệm vụ thi đấu Robocon.
- **Source:** "name": "Rover_Robotcon_PID_SM", "device": "yolobit"
- **Tag:** [vv08]

- **Fact:** Hệ thống sử dụng 4 thư viện mở rộng (extensions) chính: ROVER (điều khiển kit xe), MQTT (giao tiếp IoT), SỰ KIỆN (xử lý event) và ROBOCON (khối lệnh bổ sung cho thi đấu).
- **Source:** "extensions": [...] (dòng cuối của dữ liệu raw)
- **Tag:** [vv08]

- **Fact:** Các tham số PID khởi tạo cho robot bao gồm: Kp = 18, Ki = 0, Kd = 8 và tốc độ cơ bản (base_speed) được đặt là 30.
- **Source:** block id="proc_setup" (statement name="STACK")
- **Tag:** [vv08]

- **Fact:** Thuật toán dò line sử dụng 4 cảm biến hồng ngoại (L1, L2, R1, R2) tương ứng với các kênh đọc 1, 2, 3, và 4 trên robot Rover.
- **Source:** block type="rover_line_sensor_read_single" (CH 1, 2, 3, 4)
- **Tag:** [vv08]

- **Fact:** Công thức tính sai số (error - e) để điều hướng dựa trên trọng số các cảm biến là: $e = (L1 \times 3 + L2 \times 1) - (R1 \times 1 + R2 \times 3)$.
- **Source:** block id="b_set_e" (math_arithmetic)
- **Tag:** [vv08]

- **Fact:** Robot điều khiển động cơ thông qua giá trị hiệu chỉnh (correction) từ bộ PID: Motor trái = $base\_speed + correction$; Motor phải = $base\_speed - correction$.
- **Source:** block id="b_move_pid" (value name="LEFT" và "RIGHT")
- **Tag:** [vv08]

- **Fact:** Robot hoạt động theo mô hình máy trạng thái (State Machine) với các trạng thái chính: FOLLOW (dò line), TASK1 (trồng cây), TASK2 (tái chế).
- **Source:** block id="proc_sched" (field name="NAME": scheduler)
- **Tag:** [vv08]

- **Fact:** Thủ tục `detect_intersection` xác định giao lộ bằng cách tính tổng giá trị đọc được từ cả 4 cảm biến line ($L1 + L2 + R1 + R2$).
- **Source:** block id="proc_detect" (field name="NAME": detect_intersection)
- **Tag:** [vv08]

- **Fact:** Trạng thái mặc định khi khởi tạo chương trình của robot được thiết lập là "FOLLOW".
- **Source:** block id="b_init_state" (field name="TEXT": FOLLOW)
- **Tag:** [vv08]

- **Fact:** Các nhiệm vụ phụ trợ như "trồng cây" (do_task_trong_cay) và "tái chế" (do_task_tai_che) hiện tại được cấu hình với thời gian chờ (sleep) là 300ms.
- **Source:** block id="proc_t1" và "proc_t2"
- **Tag:** [vv08]
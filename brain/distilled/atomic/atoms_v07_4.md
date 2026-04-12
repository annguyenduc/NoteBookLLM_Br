Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn cung cấp Volume v07 theo quy tắc LOM v4.1:

- **Fact:** Trong cấu hình điều khiển PID cho Rover, các tham số mặc định được thiết lập là Kp = 0.4, Ki = 0.02, Kd = 0.15 và tốc độ cơ bản (base_speed) là 40.
- **Source:** v07 - Section: Setup procedure (khối b1 đến b4)
- **Tag:** [vv07]

- **Fact:** Công thức tính sai số vị trí (e) cho robot sử dụng 4 cảm biến line (L1, L2, R1, R2) dựa trên trọng số là: e = (-3 * L1) + (-1 * L2) + (1 * R1) + (3 * R2).
- **Source:** v07 - Section: Forever follow line with PID (khối calc_e)
- **Tag:** [vv07]

- **Fact:** Giá trị hiệu chỉnh (correction) trong thuật toán PID được tính bằng tổng của ba thành phần: (Kp * sai số hiện tại) + (Ki * tổng sai số tích lũy) + (Kd * tốc độ thay đổi sai số).
- **Source:** v07 - Section: Forever follow line with PID (khối calc_corr)
- **Tag:** [vv07]

- **Fact:** Để điều chỉnh hướng di chuyển của Rover, giá trị hiệu chỉnh được trừ vào tốc độ động cơ trái và cộng vào tốc độ động cơ phải.
- **Source:** v07 - Section: Forever follow line with PID (khối mleft, mright)
- **Tag:** [vv07]

- **Fact:** Khi robot có hiện tượng rung lắc mạnh hoặc đánh lái quá đà (overshoot), quy tắc hiệu chỉnh là giảm thông số Kp và tăng thông số Kd.
- **Source:** v07 - Section: Heuristics tuning rules
- **Tag:** [vv07]

- **Fact:** Nếu robot phản ứng chậm hoặc lừ đừ (sluggish), cần tăng thông số Kp hoặc tăng nhẹ tốc độ cơ bản (speed_base).
- **Source:** v07 - Section: Heuristics tuning rules
- **Tag:** [vv07]

- **Fact:** Để khắc phục lỗi lệch quỹ đạo kéo dài (drift), người lập trình nên thêm một lượng Ki rất nhỏ (từ 0.01 đến 0.05) kèm theo bộ giới hạn tích phân (I_clamp).
- **Source:** v07 - Section: Heuristics tuning rules / Checklist thử nghiệm tại lớp
- **Tag:** [vv07]

- **Fact:** Hệ sinh thái OhStem hỗ trợ lập trình robot Rover thông qua ứng dụng app.ohstem.vn với hai chế độ: lập trình kéo thả (Blockly) và lập trình văn bản (MicroPython).
- **Source:** v07 - Section: Assistant's Workflow / Gợi ý dạy học
- **Tag:** [vv07]

- **Fact:** Một quy trình thử nghiệm PID chuẩn (experiment_loop) bao gồm 5 bước: Quan sát (Observe), Quyết định (Decide), Hành động (Act), Ghi nhật ký (Log), và Kiểm tra điều kiện dừng (StopCriteria).
- **Source:** v07 - Section: experiment_loop
- **Tag:** [vv07]

- **Fact:** Việc giới hạn (clamp) giá trị đầu ra của bộ điều khiển PID là cần thiết để đảm bảo tốc độ động cơ không vượt quá giới hạn vật lý (ví dụ: tối đa 100%).
- **Source:** v07 - Section: Heuristics tuning rules (safety) / Code mẫu MicroPython
- **Tag:** [vv07]

- **Fact:** Cảm biến line cần được hiệu chuẩn (calibrate) trên nền trắng và line đen trước khi thực hiện thuật toán PID để đảm bảo giá trị đọc về chính xác.
- **Source:** v07 - Section: Checklist thử nghiệm tại lớp
- **Tag:** [vv07]

- **Fact:** YoloBit là nền tảng điều khiển chính được sử dụng trong các dự án robot giáo dục STEM của OhStem để thực hiện các bài toán IoT và Robotics.
- **Source:** v07 - Section: Assistant's Workflow (inputs_schema)
- **Tag:** [vv07]
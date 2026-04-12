Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn cung cấp (v07) theo quy tắc LOM v4.1:

--------------------------------------------------

- **Fact:** [CONV] Cấu trúc file JSON để import vào app.ohstem.vn cho YoloBit/Rover yêu cầu trường `"mode": "python"` và trường `"python"` chứa mã nguồn đã được chuẩn hóa.
- **Source:** [vv07] - Phần: Nội dung file `rover_standardized.json`.
- **Tag:** [vv07]

- **Fact:** [CONV] Trong lập trình Rover, trạng thái cảm biến line `(0,0,0,0)` xác định robot đã ra ngoài vạch ("Out"), trong khi `(1,1,1,1)` xác định robot đang ở ngã tư ("N4").
- **Source:** [vv07] - Hàm `read_line()` trong mã nguồn Python.
- **Tag:** [vv07]

- **Fact:** [CONV] Thuật toán PID (Proportional-Integral-Derivative) sử dụng sai số (error) để tính toán lệnh điều khiển thông qua ba thành phần: Tỷ lệ (P), Tích phân (I) và Đạo hàm (D).
- **Source:** [vv07] - Bảng giải thích thuật ngữ PID.
- **Tag:** [vv07]

- **Fact:** [CONV] Kỹ thuật "Anti-windup" trong điều khiển PID giúp ngăn chặn thành phần Tích phân (I) tích lũy sai số quá lớn khi hệ thống bị bão hòa hoặc không phản hồi.
- **Source:** [vv07] - Bảng giải thích thuật ngữ Anti-windup.
- **Tag:** [vv07]

- **Fact:** [CONV] Phương pháp "Trung bình có trọng số" (Weighted Average) được dùng để tính toán vị trí sai số của robot so với line bằng cách gán giá trị (weight) cho từng cảm biến (ví dụ: -3, -1, 1, 3).
- **Source:** [vv07] - Phần 2: Phiên bản Robotcon-standard PID.
- **Tag:** [vv07]

- **Fact:** [CONV] Agent trong Minecraft Education Edition có thể đặt các khối (blocks) hoặc vật phẩm có thể đặt thành khối (đuốc, đường ray, cửa) bằng lệnh `agent.place()`.
- **Source:** [vv07] - Phần: Agent làm được gì.
- **Tag:** [vv07]

- **Fact:** [CONV] Agent trong Minecraft Education Edition không thể đặt trực tiếp các thực thể (entities) như Minecart bằng lệnh `agent.place()`; thay vào đó phải dùng Dispenser hoặc lệnh `/summon`.
- **Source:** [vv07] - Phần: Ví dụ về đặt minecart hopper.
- **Tag:** [vv07]

- **Fact:** [CONV] Để điều khiển servo (cánh tay robot) di chuyển mượt mà, cần sử dụng vòng lặp để thay đổi góc từng độ một kết hợp với khoảng thời gian chờ ngắn (ví dụ: `time.sleep_ms(20)`).
- **Source:** [vv07] - Hàm `lift_arm_smooth(action)` trong mã nguồn Python.
- **Tag:** [vv07]

- **Fact:** [CONV] Trong điều khiển PID, thành phần Đạo hàm (D) có vai trò dự đoán xu hướng thay đổi của sai số để giảm hiện tượng dao động (oscillation) hoặc vượt ngưỡng (overshoot).
- **Source:** [vv07] - Bảng giải thích thuật ngữ Derivative (D).
- **Tag:** [vv07]

- **Fact:** [CONV] Việc sử dụng biến `dt` (delta time) trong PID giúp chuẩn hóa các thành phần tích phân và đạo hàm, đảm bảo thuật toán hoạt động ổn định ngay cả khi tần số vòng lặp thay đổi.
- **Source:** [vv07] - Phần 3: Giải thích những điểm quan trọng (dt-aware).
- **Tag:** [vv07]

- **Fact:** [CONV] Agent trong Minecraft Education Edition không thể thực hiện các hành động "chuột phải" đặc biệt như đổ nước từ xô, bón bột xương hoặc sử dụng bật lửa.
- **Source:** [vv07] - Phần: Giới hạn quan trọng của Agent.
- **Tag:** [vv07]

- **Fact:** [CONV] Khi robot mất line hoàn toàn, một chiến lược phổ biến là sử dụng giá trị sai số cuối cùng (`last_error`) để dự đoán hướng quay lại tìm line.
- **Source:** [vv07] - Phần 2: Phiên bản Robotcon-standard PID (logic `seen == 0`).
- **Tag:** [vv07]

--------------------------------------------------
**Scout Note:** Dữ liệu tập trung vào việc tối ưu hóa robot Rover qua thuật toán PID và các giới hạn tương tác của Agent trong môi trường Minecraft Education. Các thông số cấu hình servo và cảm biến được trích xuất trực tiếp từ mã nguồn chuẩn hóa.
---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v08_9
  title: CONV_atoms_v08_9
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v08) về chủ đề Robotics và YoloBit:

- **Fact:** [CONV] Robot Rover của Ohstem được sử dụng trong cuộc thi AI Hackathon 2023 với các nhiệm vụ thi đấu như trồng cây, tái chế và đẩy khối sản xuất.
- **Source:** [Dữ liệu Raw - Conversation: Chuẩn hoá code Rover]
- **Tag:** [vv08]

- **Fact:** [CONV] Giải thuật điều khiển Robotcon tiêu chuẩn bao gồm bốn thành phần chính: PID đi line, nhận dạng giao lộ, căn ô dừng và bộ lập lịch nhiệm vụ dựa trên máy trạng thái (state machine).
- **Source:** [Dữ liệu Raw - Assistant response regarding Robotcon structure]
- **Tag:** [vv08]

- **Fact:** [CONV] Để tệp JSON Blockly có thể import thành công vào giao diện app.ohstem.vn, phần `xmlText` phải sử dụng namespace chuẩn `<xml xmlns="https://developers.google.com/blockly/xml">` và không được chứa các tiền tố tên miền như `ns0:`.
- **Source:** [Dữ liệu Raw - Assistant response regarding XML namespace issue]
- **Tag:** [vv08]

- **Fact:** [CONV] Công thức tính sai số (e) cho giải thuật PID từ 4 cảm biến line thường sử dụng trọng số (ví dụ: 3-1-1-3) theo cấu trúc: `e = (wL3 + wL2 - wR2 - wR3)`.
- **Source:** [Dữ liệu Raw - Ghi chú tinh chỉnh]
- **Tag:** [vv08]

- **Fact:** [CONV] Các biến cốt lõi trong giải thuật PID cho Robot Rover bao gồm: `Kp` (tỷ lệ), `Ki` (tích phân), `Kd` (đạo hàm), `base_speed` (tốc độ cơ sở), `last_error` (sai số trước đó) và `sum_error` (tổng sai số).
- **Source:** [Dữ liệu Raw - Assistant response regarding Robotcon structure]
- **Tag:** [vv08]

- **Fact:** [CONV] Tốc độ của hai động cơ trong giải thuật PID được điều chỉnh theo công thức: `left_speed = base_speed + correction` và `right_speed = base_speed - correction`, trong đó `correction` là giá trị hiệu chỉnh từ bộ PID.
- **Source:** [Dữ liệu Raw - Ghi chú tinh chỉnh]
- **Tag:** [vv08]

- **Fact:** [CONV] Các khối lệnh (blocks) đặc thù để lập trình Rover trên nền tảng YoloBit bao gồm: `rover_line_sensor_read_all`, `rover_move_motor`, `rover_stop`, và `rover_line_sensor_read_single`.
- **Source:** [Dữ liệu Raw - Assistant response regarding block types]
- **Tag:** [vv08]

- **Fact:** [CONV] Máy trạng thái (State Machine) trong lập trình robot thi đấu thường điều hướng qua các trạng thái: `WAIT_START` (chờ bắt đầu), `FOLLOW_LINE` (dò line), `AT_INTERSECTION` (tại giao lộ) và các trạng thái thực hiện nhiệm vụ cụ thể.
- **Source:** [Dữ liệu Raw - Assistant response regarding Robotcon structure]
- **Tag:** [vv08]

- **Fact:** [CONV] Việc căn chỉnh robot dừng chính xác tại ô nhiệm vụ có thể thực hiện bằng cách giảm tốc độ, nhích từng bước nhỏ (`rover_move_delay`) sau khi nhận diện được vạch ngang (marker) hoặc giao lộ.
- **Source:** [Dữ liệu Raw - Ghi chú tinh chỉnh]
- **Tag:** [vv08]

- **Fact:** [CONV] Trong lập trình Blockly cho YoloBit, các biến cảm biến line thường được gán cho các biến định danh như `L1`, `L2`, `R1`, `R2` tương ứng với các kênh đọc từ cảm biến hồng ngoại.
- **Source:** [Dữ liệu Raw - JSON snippet at the end]
- **Tag:** [vv08]
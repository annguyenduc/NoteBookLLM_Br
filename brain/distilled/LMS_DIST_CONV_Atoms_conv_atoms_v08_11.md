---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v08_11
  title: CONV_atoms_v08_11
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v08 liên quan đến IoT, Robotics và lập trình điều khiển robot Rover:

- **Fact:** [CONV] Thư viện mở rộng `yolobit_extension_robocon_rover` (nguồn từ GitHub AITT-VN) cung cấp các khối lệnh bổ sung chuyên dụng cho thi đấu Robocon của robot Rover trên nền tảng YoloBit.
- **Source:** [vv08 - Section: DỮ LIỆU RAW]
- **Tag:** [vv08]

- **Fact:** [CONV] Lỗi khiến file import vào môi trường lập trình bị "trống" thường do cấu trúc XML không hợp lệ (mismatched tag), đặc biệt hay xảy ra ở các khối tính toán toán học (`math_arithmetic`) lồng nhau nhiều tầng.
- **Source:** [vv08 - Section: ASSISTANT response regarding XML error]
- **Tag:** [vv08]

- **Fact:** [CONV] Giải thuật PID (Proportional, Integral, Derivative) được sử dụng để điều khiển robot bám line (follow line) mượt mà bằng cách tính toán giá trị hiệu chỉnh (`correction`) dựa trên sai số vị trí.
- **Source:** [vv08 - Section: ASSISTANT response "PID lái vi sai"]
- **Tag:** [vv08]

- **Fact:** [CONV] Công thức tính lỗi (error) cho cảm biến line 4 kênh thường sử dụng trọng số (weights) cho từng mắt cảm biến, ví dụ: mắt ngoài cùng bên trái là -3, mắt trong trái là -1, mắt trong phải là 1, và mắt ngoài cùng bên phải là 3.
- **Source:** [vv08 - Section: ASSISTANT response "TÍNH LỖI VỊ TRÍ LINE (weighted)"]
- **Tag:** [vv08]

- **Fact:** [CONV] Nhận diện giao lộ (Intersection Detection) được xác định khi tổng số mắt cảm biến phát hiện vạch đen vượt quá một ngưỡng nhất định (thường là >= 3 mắt trên hệ thống 4 mắt).
- **Source:** [vv08 - Section: ASSISTANT response "Nhận diện giao lộ/ngã ba"]
- **Tag:** [vv08]

- **Fact:** [CONV] Phân loại các loại giao lộ dựa trên trạng thái mắt cảm biến: Ngã tư (mắt ngoài cùng bên trái và phải đều thấy đen), Ngã ba chữ T trái (mắt trái thấy đen, mắt phải thấy trắng) và ngược lại cho chữ T phải.
- **Source:** [vv08 - Section: ASSISTANT response "DetectIntersection()"]
- **Tag:** [vv08]

- **Fact:** [CONV] Kỹ thuật rẽ 90 độ tại giao lộ: Robot thực hiện quay tại chỗ cho đến khi hai mắt cảm biến giữa (S1, S2) bắt lại được vạch line và hai mắt ngoài (S0, S3) nằm ngoài vạch.
- **Source:** [vv08 - Section: ASSISTANT response "Rẽ tại giao lộ (90°)"]
- **Tag:** [vv08]

- **Fact:** [CONV] Trạng thái "Hết vạch" (End-of-Line - EOL) được xác định khi tất cả các mắt cảm biến đều đọc được giá trị màu trắng trong một khoảng thời gian liên tục (ví dụ: 150ms).
- **Source:** [vv08 - Section: ASSISTANT response "AlignStop()"]
- **Tag:** [vv08]

- **Fact:** [CONV] Cơ chế State Machine (Scheduler) giúp quản lý lộ trình robot theo từng bước (Step), cho phép thực hiện các chuỗi hành động phức tạp như: "đi qua N giao lộ", "rẽ tại giao lộ kế tiếp", "dừng và căn chỉnh".
- **Source:** [vv08 - Section: ASSISTANT response "State machine (scheduler)"]
- **Tag:** [vv08]

- **Fact:** [CONV] Hiệu chuẩn cảm biến (Calibration) thực hiện bằng cách lấy giá trị trung bình giữa giá trị đọc được tại nền trắng và vạch đen để làm ngưỡng (threshold) phân biệt.
- **Source:** [vv08 - Section: ASSISTANT response "QuickCalibrate"]
- **Tag:** [vv08]

- **Fact:** [CONV] Để tránh hiện tượng "đếm trùng" giao lộ do cảm biến đọc quá nhanh, cần thiết lập một khoảng thời gian chờ (cooldown), thường từ 250ms đến 450ms sau mỗi lần phát hiện giao lộ.
- **Source:** [vv08 - Section: ASSISTANT response "Nhận diện giao lộ/ngã ba"]
- **Tag:** [vv08]

- **Fact:** [CONV] Robot Rover trong cuộc thi AI Hackathon thường tích hợp thêm Camera AI (như HuskyLens hoặc K210) để thực hiện các nhiệm vụ nhận diện nhãn (tag), màu sắc hoặc ký hiệu môi trường.
- **Source:** [vv08 - Section: ASSISTANT response regarding AI Hackathon 2023]
- **Tag:** [vv08]
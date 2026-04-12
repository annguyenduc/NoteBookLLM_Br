---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v02_8
  title: atoms_v02_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v02:

- **Fact:** Kiến trúc lập trình IoT tối ưu trên Blockly (app.ohstem.vn) nên được tổ chức theo mô hình "sự kiện + định kỳ" để đảm bảo tính ổn định và phản hồi nhanh.
- **Source:** [vv02] - Section: Sơ đồ khối tổng thể (Blockly)
- **Tag:** [vv02]

- **Fact:** Công thức tính EMA (Exponential Moving Average) để làm mượt dữ liệu cảm biến là: `ema_t = ema_{t-1} + α * (x_t - ema_{t-1})`, trong đó α là hệ số làm mượt từ 0 đến 1.
- **Source:** [vv02] - Section: EMA (Exponential Moving Average) dùng để làm gì?
- **Tag:** [vv02]

- **Fact:** Hệ số α trong EMA có thể được xác định dựa trên chu kỳ lấy mẫu (Δt) và hằng số thời gian mong muốn (τ) qua công thức: `α = 1 - exp(-Δt / τ)`.
- **Source:** [vv02] - Section: Chọn α theo thời gian lấy mẫu
- **Tag:** [vv02]

- **Fact:** Trên board Yolo UNO (ESP32-S3), các chân I2C mặc định cho thiết bị như DHT20 và LCD 16x2 thường là SDA (D21) và SCL (D22).
- **Source:** [vv02] - Section: Sơ đồ phần cứng (có thể đổi)
- **Tag:** [vv02]

- **Fact:** Kỹ thuật Hysteresis (trễ) được sử dụng để chống tình trạng thiết bị (như bơm hoặc đèn) bật/tắt liên tục khi cảm biến dao động quanh một ngưỡng cố định.
- **Source:** [vv02] - Section: 4) Khối định kỳ “mỗi 100 ms” — Logic + Hysteresis + Thực thi thiết bị
- **Tag:** [vv02]

- **Fact:** Để tối ưu hóa việc gửi dữ liệu lên Dashboard IoT, nên thiết lập điều kiện Publish chỉ khi dữ liệu thay đổi vượt ngưỡng sai số (ví dụ: Temp >= 0.3°C, Light >= 15 đơn vị) hoặc sau một khoảng thời gian cố định (ví dụ: 10 giây).
- **Source:** [vv02] - Section: 5) Khối định kỳ “mỗi 1 s” — Quyết định publish (chỉ khi đổi)
- **Tag:** [vv02]

- **Fact:** Cảm biến siêu âm HC-SR04 kết nối với Yolo UNO thường sử dụng chân D12 cho tín hiệu Trig và D13 cho tín hiệu Echo.
- **Source:** [vv02] - Section: Sơ đồ phần cứng (có thể đổi)
- **Tag:** [vv02]

- **Fact:** Khi máy in 3D (như Neptune 4) bị kẹt mực, kỹ thuật "Cold Pull" được thực hiện bằng cách làm nóng nozzle lên nhiệt độ in (210°C), sau đó hạ nhiệt xuống khoảng 90°C (đối với PLA) rồi rút mạnh sợi nhựa để kéo theo cặn bẩn.
- **Source:** [vv02] - Section: Bước 3: Làm sạch nozzle (cold pull)
- **Tag:** [vv02]

- **Fact:** Độ phân giải ADC của Yolo UNO thường là 12-bit, tương ứng với dải giá trị từ 0 đến 4095.
- **Source:** [vv02] - Section: Định kỳ mỗi 500 ms — Đọc cảm biến + EMA
- **Tag:** [vv02]

- **Fact:** Để điều khiển Servo SG90/MG90S ổn định, cần sử dụng nguồn 5V riêng và phải kết nối chung cực âm (GND) với board điều khiển.
- **Source:** [vv02] - Section: Sơ đồ phần cứng (có thể đổi)
- **Tag:** [vv02]

- **Fact:** Trạng thái Idempotent trong lập trình thiết bị là việc chỉ ra lệnh điều khiển (DigitalWrite/ServoWrite) khi trạng thái mong muốn (desired) khác với trạng thái thực tế (actual) của thiết bị.
- **Source:** [vv02] - Section: 4) Khối định kỳ “mỗi 100 ms” — Logic + Hysteresis + Thực thi thiết bị
- **Tag:** [vv02]
---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v02_8
  title: CONV_atoms_v02_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v02 theo quy tắc LOM v4.1:

- **Fact:** [CONV] Kiến trúc lập trình Blockly tối ưu cho Yolo UNO trên app.ohstem.vn nên được tổ chức theo mô hình "sự kiện + định kỳ" (event-driven + periodic) để đảm bảo tính thời gian thực và ổn định.
- **Source:** [vv02] - Section: Sơ đồ khối tổng thể (Blockly)
- **Tag:** [vv02]

- **Fact:** [CONV] Cấu hình chân kết nối (pinout) mặc định cho hệ thống AIoT dùng Yolo UNO: I2C (SDA D21, SCL D22), Cảm biến ánh sáng (A0), Siêu âm HC-SR04 (Trig D12, Echo D13), LED đơn (D2), RGB PWM (D5, D18, D19), Servo (D4).
- **Source:** [vv02] - Section: Sơ đồ phần cứng (có thể đổi)
- **Tag:** [vv02]

- **Fact:** [CONV] Công thức EMA (Exponential Moving Average) dùng để lọc nhiễu cảm biến: `ema_t = ema_{t-1} + α * (x_t - ema_{t-1})`. Trong đó, α nhỏ giúp mượt hơn nhưng phản ứng chậm, α lớn giúp phản ứng nhanh nhưng ít mượt.
- **Source:** [vv02] - Section: EMA (Exponential Moving Average)
- **Tag:** [vv02]

- **Fact:** [CONV] Kỹ thuật điều khiển "Idempotent" được áp dụng bằng cách so sánh trạng thái mong muốn (`des_*`) với trạng thái thực tế (`act_*`), chỉ thực thi lệnh điều khiển phần cứng khi có sự thay đổi.
- **Source:** [vv02] - Section: 4) Khối định kỳ “mỗi 100 ms”
- **Tag:** [vv02]

- **Fact:** [CONV] Cơ chế "Smart Publish" giúp giảm tải băng thông MQTT bằng cách chỉ gửi dữ liệu khi: (1) Quá 10 giây chưa gửi, hoặc (2) Giá trị thay đổi vượt ngưỡng sai số (Nhiệt độ >= 0.3°C, Độ ẩm >= 1.0%, Ánh sáng >= 15).
- **Source:** [vv02] - Section: 5) Khối định kỳ “mỗi 1 s” — Quyết định publish
- **Tag:** [vv02]

- **Fact:** [CONV] Khi sử dụng Servo (SG90/MG90S) với Yolo UNO, bắt buộc phải sử dụng nguồn 5V riêng và nối chung chân GND với board điều khiển để tránh sụt áp và nhiễu.
- **Source:** [vv02] - Section: Sơ đồ phần cứng (có thể đổi)
- **Tag:** [vv02]

- **Fact:** [CONV] Phương pháp "Cold Pull" để xử lý tắc đầu phun máy in 3D: Nung nóng nozzle lên 200°C (cho PLA), nạp nhựa, hạ nhiệt xuống khoảng 90°C rồi kéo mạnh sợi nhựa ra để lôi cặn bẩn và nhựa cháy.
- **Source:** [vv02] - Section: Bước 3: Làm sạch nozzle (cold pull)
- **Tag:** [vv02]

- **Fact:** [CONV] Hysteresis (trễ) được sử dụng trong logic tự động để chống hiện tượng thiết bị bật/tắt liên tục tại ngưỡng. Ví dụ: Bật bơm khi độ ẩm đất >= 520 và chỉ tắt khi độ ẩm < 380.
- **Source:** [vv02] - Section: 4) Khối định kỳ “mỗi 100 ms”
- **Tag:** [vv02]

- **Fact:** [CONV] Hệ số làm mượt α trong EMA có thể tính toán dựa trên chu kỳ lấy mẫu Δt và hằng số thời gian τ mong muốn qua công thức: `α = 1 - exp(-Δt / τ)`.
- **Source:** [vv02] - Section: Chọn α theo thời gian lấy mẫu
- **Tag:** [vv02]

- **Fact:** [CONV] Để phòng tránh kẹt mực trên máy in Neptune 4, cần cắt đầu sợi nhựa (filament) một góc 45 độ trước khi nạp và luôn rút mực khi đầu phun còn nóng.
- **Source:** [vv02] - Section: 💡 Mẹo phòng tránh kẹt mực lần sau
- **Tag:** [vv02]
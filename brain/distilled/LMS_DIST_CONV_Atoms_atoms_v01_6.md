---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v01_6
  title: atoms_v01_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v01) theo quy tắc LOM v4.1:

- **Fact:** Các cảm biến tương thích cho TinyML trên ESP32-S3 bao gồm DHT20, LDR, PIR, siêu âm và mic I2S (nhận biết 3–4 loại âm thanh).
- **Source:** v01 - Section: 1) TinyML on-device (Edge Impulse)
- **Tag:** [vv01]

- **Fact:** Quy trình triển khai TinyML: Thu dữ liệu & train trên Edge Impulse -> Build TensorFlow Lite Micro cho ESP32-S3 -> Flash firmware vào UNO (Arduino/C++).
- **Source:** v01 - Section: 1) TinyML on-device (Edge Impulse)
- **Tag:** [vv01]

- **Fact:** Kỹ thuật ổn định đầu ra model AI sử dụng EMA (Exponential Moving Average) kết hợp hysteresis (ví dụ: chỉ đổi trạng thái khi xác suất p > 0.8 trong 5 mẫu liên tiếp).
- **Source:** v01 - Section: 1) TinyML on-device (Edge Impulse)
- **Tag:** [vv01]

- **Fact:** Phương pháp "HTTP Pull" cho phép UNO lấy kết quả AI từ trình duyệt/laptop thông qua một URL JSON (dùng Google Apps Script hoặc Flask/Node-RED) để tránh hạn chế của app.ohstem về khối MQTT tùy ý.
- **Source:** v01 - Section: 2) AI chạy trên điện thoại/laptop → UNO “kéo” (pull) kết quả qua HTTP
- **Tag:** [vv01]

- **Fact:** Web Serial Bridge cho phép truyền dữ liệu AI (nhãn và độ tin cậy) từ trình duyệt qua cáp USB vào UNO, phù hợp cho môi trường không có Wi-Fi.
- **Source:** v01 - Section: 3) “Web Serial Bridge” (USB)
- **Tag:** [vv01]

- **Fact:** Để mã hóa nhiều trạng thái trên app.ohstem (vốn chỉ có nút 2 trạng thái), có thể dùng 2-3 toggle làm bitfield (0-7 lớp) hoặc dùng slider để đẩy mã lớp (0-5).
- **Source:** v01 - Section: Cách mã hoá nhiều trạng thái khi app.ohstem chỉ có nút 2 trạng thái
- **Tag:** [vv01]

- **Fact:** Công thức lọc nhiễu EMA cho cảm biến: $L_{ema} = \alpha \cdot L_{new} + (1 - \alpha) \cdot L_{ema}$ với hệ số $\alpha \approx 0.2$.
- **Source:** v01 - Section: A3. Ổn định tín hiệu
- **Tag:** [vv01]

- **Fact:** Kỹ thuật "AI-lite" tự hiệu chỉnh ngưỡng (Calibration) hoạt động bằng cách ghi nhận $L_{min}$ và $L_{max}$ trong một khoảng thời gian (8-10s), sau đó tính toán ngưỡng $LOW\_TH$ và $HIGH\_TH$ dựa trên dải giá trị thu được.
- **Source:** v01 - Section: A+. “AI-lite” (tự học ngưỡng theo môi trường)
- **Tag:** [vv01]

- **Fact:** Phương pháp "First-sample seeding" trong lập trình hiệu chỉnh: Gán mẫu đầu tiên cho cả $L_{min}$ và $L_{max}$, các mẫu sau đó mới thực hiện so sánh để cập nhật cực trị.
- **Source:** v01 - Section: Cách khuyên dùng: “first-sample seeding”
- **Tag:** [vv01]

- **Fact:** Thông số thiết kế Pulley cho động cơ vàng TT: Đường kính ngoài 36mm, lỗ trục 2mm kèm rãnh dẹt (D-flat) sâu khoảng 0.8mm, rãnh dây rộng 3.5mm phù hợp cho dây thun hoặc dây diều.
- **Source:** v01 - Section: Thiết kế pulley 3D
- **Tag:** [vv01]

- **Fact:** Để in 3D Pulley chịu lực tốt, nên sử dụng vật liệu PLA/PETG, độ dày lớp 0.2mm, 3-4 lớp tường (walls) và độ lấp đầy (infill) từ 60-80%.
- **Source:** v01 - Section: Gợi ý chọn & lắp
- **Tag:** [vv01]
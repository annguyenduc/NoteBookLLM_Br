---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v01_6
  title: CONV_atoms_v01_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v01:

- **Fact:** [CONV] Triển khai TinyML trên ESP32-S3 bằng cách thu thập dữ liệu và huấn luyện trên Edge Impulse, sau đó biên dịch TensorFlow Lite Micro để nạp firmware vào thiết bị.
- **Source:** (v01 - Section: 1) TinyML chạy trực tiếp trên UNO (ESP32-S3))
- **Tag:** [vv01]

- **Fact:** [CONV] Kỹ thuật ổn định đầu ra cho mô hình AI bao gồm sử dụng bộ lọc EMA (Exponential Moving Average) và trễ (hysteresis), ví dụ chỉ đổi trạng thái khi xác suất p > 0.8 trong 5 mẫu liên tiếp.
- **Source:** (v01 - Section: 1) TinyML chạy trực tiếp trên UNO (ESP32-S3))
- **Tag:** [vv01]

- **Fact:** [CONV] Phương pháp "HTTP pull" cho phép Yolo UNO lấy kết quả nhận diện (label, p) từ AI chạy trên trình duyệt/laptop thông qua một URL JSON trung gian (dùng Google Apps Script hoặc Flask).
- **Source:** (v01 - Section: 2) AI chạy trên điện thoại/laptop → UNO “kéo” (pull) kết quả qua HTTP)
- **Tag:** [vv01]

- **Fact:** [CONV] Web Serial Bridge cho phép truyền dữ liệu nhận diện từ Teachable Machine trực tiếp qua cáp USB đến UNO, giúp demo ổn định khi không có Wi-Fi hoặc mạng yếu.
- **Source:** (v01 - Section: 3) “Web Serial Bridge” (USB) – nhanh gọn cho demo camera)
- **Tag:** [vv01]

- **Fact:** [CONV] Để điều khiển nhiều trạng thái trên app.ohstem (vốn chỉ có nút 2 trạng thái), có thể dùng 2-3 nút gạt làm bitfield (mã nhị phân) hoặc dùng slider để gửi mã lớp (0-5).
- **Source:** (v01 - Section: Cách mã hoá nhiều trạng thái khi app.ohstem chỉ có nút 2 trạng thái)
- **Tag:** [vv01]

- **Fact:** [CONV] Công thức lọc nhiễu EMA phổ biến cho cảm biến là: `L_ema = alpha * L_new + (1 - alpha) * L_ema` với hệ số alpha thường chọn khoảng 0.2.
- **Source:** (v01 - Section: A3. Ổn định tín hiệu (45’))
- **Tag:** [vv01]

- **Fact:** [CONV] Cơ chế Hysteresis (ngưỡng kép) giúp chống chớp nháy thiết bị: ví dụ đèn chỉ bật khi độ sáng < 30 và chỉ tắt khi độ sáng > 40.
- **Source:** (v01 - Section: A3. Ổn định tín hiệu (45’))
- **Tag:** [vv01]

- **Fact:** [CONV] Phương pháp "AI-lite" tự hiệu chỉnh (Calibrate) cho phép máy tự học dải giá trị môi trường (Lmin, Lmax) trong khoảng 8-10 giây để tự động tính toán ngưỡng hoạt động tối ưu.
- **Source:** (v01 - Section: A+. “AI-lite” (tự học ngưỡng theo môi trường))
- **Tag:** [vv01]

- **Fact:** [CONV] Trục động cơ vàng TT có đặc điểm là trục tròn 2mm với một mặt dẹt (D-shaft); khi thiết kế pulley in 3D cần tạo lỗ bore khoảng 2.05mm kèm rãnh dẹt tương ứng để ép khít.
- **Source:** (v01 - Section: Conversation: Thiết kế pulley 3D)
- **Tag:** [vv01]

- **Fact:** [CONV] Lộ trình tập huấn IoT/AI cho học sinh gồm 12 bước, bắt đầu từ an toàn điện, Digital/Analog I/O, đến lọc nhiễu, máy trạng thái và cuối cùng là tích hợp TinyML hoặc HTTP pull.
- **Source:** (v01 - Section: Lộ trình 12 bước (từ cơ bản → AI))
- **Tag:** [vv01]
---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v02_2
  title: CONV_atoms_v02_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ nguồn cung cấp Volume v02 theo quy tắc LOM v4.1:

- **Fact:** [CONV] Khi sử dụng Server IoT MQTT bên thứ ba cho thiết bị, có thể sử dụng broker `test.mosquitto.org` qua cổng (port) `1883`.
- **Source:** (v02 - Sơ đồ B — Dùng Server IoT khác (MQTT topic) - Mục 1)
- **Tag:** [vv02]

- **Fact:** [CONV] Quy ước topic MQTT phổ biến cho điều khiển thiết bị IoT: Topic nhận lệnh kết thúc bằng `/cmd` và topic gửi trạng thái phản hồi kết thúc bằng `/state`.
- **Source:** (v02 - Sơ đồ B — Dùng Server IoT khác (MQTT topic) - Mục 2 & Gợi ý topic)
- **Tag:** [vv02]

- **Fact:** [CONV] Các biến cơ bản cần thiết để lập trình hệ thống đèn thông minh gồm: `mode` (chế độ), `L_off`/`L_on` (ngưỡng ánh sáng), `L_ema` (giá trị lọc nhiễu cảm biến), `brightness_manual` (độ sáng tay).
- **Source:** (v02 - Ghi chú ráp khối nhanh (cả 2 sơ đồ) - Biến cần có)
- **Tag:** [vv02]

- **Fact:** [CONV] Nguyên lý Hysteresis trong điều khiển thiết bị theo cảm biến yêu cầu ngưỡng bật (`L_on`) và ngưỡng tắt (`L_off`) phải có khoảng chênh lệch (thường 10-20% dải đo) để tránh hiện tượng thiết bị bật/tắt liên tục (nhấp nháy) tại điểm ngưỡng.
- **Source:** (v02 - Ghi chú ráp khối nhanh - Hysteresis)
- **Tag:** [vv02]

- **Fact:** [CONV] Trên nền tảng OhStem IoT (app.ohstem.vn), các widget Dashboard thường chỉ hỗ trợ gửi 2 trạng thái (0 và 1). Để điều khiển đa trạng thái (ví dụ: AUTO, MANUAL ON, MANUAL OFF), giải pháp tối ưu là sử dụng Slider (thanh trượt) gán các giá trị số tương ứng hoặc nhiều nút nhấn gửi chuỗi lệnh cố định.
- **Source:** (v02 - ASSISTANT phản hồi về giao diện iot của app ohstem & Cách 1, Cách 2 điều khiển đa trạng thái)
- **Tag:** [vv02]

- **Fact:** [CONV] Đối với Yolo Uno trên app.ohstem.vn, khi khối lệnh "đổi trạng thái chân số" không cho phép chèn biến trực tiếp, lập trình viên có thể sử dụng khối "xuất ra giá trị analog" với công thức `biến_trạng_thái * 100` để điều khiển bật/tắt (0 hoặc 100).
- **Source:** (v02 - Cách 1 (khuyên dùng): Dùng xuất ra giá trị analog để ON/OFF theo biến)
- **Tag:** [vv02]

- **Fact:** [CONV] Giá trị ngưỡng ADC tham khảo cho cảm biến ánh sáng: Với dải đo 0-4095 (Yolo Uno), ngưỡng tối là `~1800` và ngưỡng sáng là `~1950`. Với dải đo 0-1023, ngưỡng tương ứng là `~450` và `~500`.
- **Source:** (v02 - Thuật toán tối giản (10 bước) - Mục 9)
- **Tag:** [vv02]

- **Fact:** [CONV] Trong ngôn ngữ Python, biểu thức điều kiện `if msg == '1':` và `if (msg) == '1':` có chức năng và kết quả thực thi hoàn toàn giống nhau; dấu ngoặc đơn chỉ có tác dụng nhóm các thành phần biểu thức.
- **Source:** (v02 - ASSISTANT phản hồi về so sánh biểu thức Python)
- **Tag:** [vv02]

- **Fact:** [CONV] Trong Python, phép so sánh giữa một chuỗi ký tự và một số nguyên (ví dụ: `'1' == 1`) luôn trả về kết quả `False` do khác biệt về kiểu dữ liệu.
- **Source:** (v02 - ASSISTANT phản hồi về so sánh biểu thức Python - Mục lưu ý hay nhầm)
- **Tag:** [vv02]

- **Fact:** [CONV] Chứng chỉ Oracle Certified Foundations Associate (như OCI hoặc Data Platform) là cấp độ khởi đầu dành cho người mới. Một số bài thi như Oracle Data Platform 2025 Foundations Associate (1Z0-1195-25) có thể được cung cấp miễn phí lệ phí thi tùy theo chương trình của Oracle.
- **Source:** (v02 - ASSISTANT phản hồi về Thông tin chứng chỉ Oracle - Mục Học phí & chi phí)
- **Tag:** [vv02]

- **Fact:** [CONV] Thuật toán lọc nhiễu EMA (Exponential Moving Average) đơn giản cho cảm biến ánh sáng có thể được viết dưới dạng công thức: `L_ema = alpha * L_x + (1 - alpha) * L_ema_cũ`.
- **Source:** [Unverified_Source] (Dựa trên logic biến `alpha` và `L_ema` được đề cập trong phần "Ghi chú ráp khối nhanh" và "Vòng lặp 0.3s").
- **Tag:** [vv02]
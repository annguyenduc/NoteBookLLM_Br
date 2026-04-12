---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v02_2
  title: atoms_v02_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v02) theo quy tắc LOM v4.1:

- **Fact:** Quy ước đặt tên kênh (topic) phổ biến trong IoT: V1 dành cho lệnh điều khiển (cmd), V2 dành cho trạng thái thiết bị (state), và V3 dành cho các thông số đo lường (metrics).
- **Source:** [v02 - Section: Sơ đồ B — Dùng Server IoT khác (MQTT topic)]
- **Tag:** [vv02]

- **Fact:** Kỹ thuật Hysteresis (trễ) trong điều khiển ánh sáng yêu cầu ngưỡng bật (L_on) phải lớn hơn ngưỡng tắt (L_off), thường chênh lệch khoảng 10-20% dải đo để chống hiện tượng nhấp nháy đèn khi cường độ sáng ở vùng biên.
- **Source:** [v02 - Section: Ghi chú ráp khối nhanh (cả 2 sơ đồ)]
- **Tag:** [vv02]

- **Fact:** Trên nền tảng OhStem Cloud, để điều khiển thiết bị với nhiều hơn 2 trạng thái (ngoài Bật/Tắt), có thể sử dụng widget Slider (Thanh trượt) gán giá trị số (0, 1, 2...) hoặc dùng nhiều nút nhấn gửi các chuỗi lệnh cố định (ví dụ: "AUTO", "M1", "M0").
- **Source:** [v02 - Section: Assistant response về widget OhStem IoT]
- **Tag:** [vv02]

- **Fact:** Giải pháp thay thế khi khối lệnh "Ghi chân số" (Digital Write) không cho phép chèn biến: Sử dụng khối "Xuất ra giá trị analog" (PWM) với công thức toán học `biến_trạng_thái * 100`. Nếu biến là 0 thì đèn tắt, nếu là 1 thì đèn sáng 100%.
- **Source:** [v02 - Section: Assistant response về khối lệnh OhStem]
- **Tag:** [vv02]

- **Fact:** Trong lập trình Python cho Yolo Uno, biểu thức `if msg == '1':` và `if (msg) == '1':` có giá trị logic tương đương hoàn toàn; dấu ngoặc đơn chỉ có tác dụng nhóm biểu thức hoặc tăng tính rõ ràng, không thay đổi kết quả so sánh.
- **Source:** [v02 - Section: Conversation: So sánh biểu thức Python]
- **Tag:** [vv02]

- **Fact:** Giá trị ADC (Analog-to-Digital Converter) trên Yolo Uno thường có dải từ 0 đến 4095 (độ phân giải 12-bit). Các ngưỡng đề xuất cho cảm biến ánh sáng thường là L_dark ≈ 1800 và L_bright ≈ 1950.
- **Source:** [v02 - Section: Thuật toán tối giản (10 bước)]
- **Tag:** [vv02]

- **Fact:** Chứng chỉ Oracle Certified Foundations Associate (ví dụ: OCI hoặc Data Platform) là cấp độ khởi đầu, tập trung vào kiến thức nền tảng. Một số mã thi như 1Z0-1195-25 có thể được Oracle cung cấp miễn phí tùy theo chương trình và thời điểm.
- **Source:** [v02 - Section: Thông tin chứng chỉ Oracle]
- **Tag:** [vv02]

- **Fact:** Để tránh xung đột lệnh trong hệ thống IoT, khi thiết bị ở chế độ AUTO (tự động), các lệnh điều khiển trực tiếp từ Dashboard (như bật/tắt thủ công) nên được lập trình để bị bỏ qua.
- **Source:** [v02 - Section: Thiết kế gọn – chạy được ngay trên app.ohstem.vn]
- **Tag:** [vv02]

- **Fact:** Tần suất gửi dữ liệu (Publish) từ thiết bị IoT lên Dashboard được khuyến nghị là từ 2-3 giây/lần để đảm bảo cập nhật trạng thái mà không gây quá tải cho server hoặc băng thông.
- **Source:** [v02 - Section: Ghi chú ráp khối nhanh - Publish định kỳ]
- **Tag:** [vv02]
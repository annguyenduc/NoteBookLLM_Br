---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v02_1
  title: atoms_v02_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ **DỮ LIỆU RAW: Volume 02** theo quy tắc LOM v4.1:

- **Fact:** Nội dung chính của Volume 02 bao gồm: Thuật toán đèn IoT, so sánh biểu thức Python, chứng chỉ Oracle, sửa lỗi đùn/kẹt mực máy in Neptune 4, kiểm tra IR receiver và tối ưu hệ thống.
- **Source:** v02 - Section: Nội dung quyển 2
- **Tag:** [vv02]

- **Fact:** Thuật toán đèn IoT tiêu chuẩn cần tích hợp các tính năng: lọc nhiễu (noise filtering), chống nhấp nháy (hysteresis), chế độ AUTO/MANUAL, hiệu chuẩn nhanh và đồng bộ MQTT.
- **Source:** v02 - Section: Thuật toán đèn IoT - ASSISTANT
- **Tag:** [vv02]

- **Fact:** Phương pháp lọc nhiễu cho cảm biến ánh sáng (LDR/ALS) được khuyến nghị là dùng trung bình trượt với cửa sổ mẫu `N=10` hoặc lọc EMA (Exponential Moving Average) với `alpha=0.2`.
- **Source:** v02 - Section: 1) Kiến trúc & trạng thái / Section: 5) Thuật toán chi tiết
- **Tag:** [vv02]

- **Fact:** Cơ chế Hysteresis chống nhấp nháy sử dụng hai ngưỡng: `L_on` (ngưỡng bật) và `L_off` (ngưỡng tắt), trong đó `L_on > L_off`. Khi giá trị ánh sáng nằm trong khoảng giữa hai ngưỡng, đèn sẽ giữ nguyên trạng thái hiện tại.
- **Source:** v02 - Section: 1) Kiến trúc & trạng thái / Section: 2.2. Vòng lặp đọc cảm biến
- **Tag:** [vv02]

- **Fact:** Chế độ MANUAL trong hệ thống IoT cho phép ghi đè (Override) tạm thời với thời hạn TTL (Time-to-Live), ví dụ 600 giây (10 phút). Sau khi hết TTL, hệ thống tự động quay lại chế độ AUTO.
- **Source:** v02 - Section: 1) Kiến trúc & trạng thái / Section: 2) Tham số khuyến nghị
- **Tag:** [vv02]

- **Fact:** Các tham số vận hành khuyến nghị cho thiết bị IoT: khoảng thời gian lấy mẫu (`sample_interval_ms`) là 200ms, khoảng thời gian gửi dữ liệu (`publish_interval_ms`) là 3000ms (3 giây).
- **Source:** v02 - Section: 2) Tham số khuyến nghị
- **Tag:** [vv02]

- **Fact:** Để tránh vùng phi tuyến tính của LED, thuật toán nên thiết lập độ sáng PWM tối thiểu (`pwm_min`) khoảng 20%.
- **Source:** v02 - Section: 2) Tham số khuyến nghị / Section: Bạn nên thêm
- **Tag:** [vv02]

- **Fact:** Cấu trúc Topic MQTT tối ưu cho thiết bị bao gồm: `.../cmd` để nhận lệnh điều khiển (JSON) và `.../state` để báo cáo trạng thái hoạt động.
- **Source:** v02 - Section: 4) MQTT topic & payload
- **Tag:** [vv02]

- **Fact:** Trên nền tảng OhStem IoT (app.ohstem.vn), quy ước phân chia kênh dữ liệu thường là: V1 dành cho lệnh (cmd), V2 dành cho trạng thái (state), và V3 dành cho các số đo kỹ thuật (metrics).
- **Source:** v02 - Section: 1) Hiểu đúng các khối trong ảnh / Section: 5) Quy ước tối thiểu
- **Tag:** [vv02]

- **Fact:** Thuật toán làm mượt độ sáng LED sử dụng kỹ thuật "lerp" (tuyến tính hóa) hoặc alpha smoothing để thay đổi giá trị PWM dần dần, tránh việc thay đổi độ sáng đột ngột gây khó chịu.
- **Source:** v02 - Section: 5) Thuật toán chi tiết / Section: Bạn nên sửa
- **Tag:** [vv02]

- **Fact:** Hiệu chuẩn nhanh (Fast Calibration) có thể thực hiện bằng cách đo môi trường hiện tại làm mốc: đặt `L_off = lux_hien_tai + 20` và `L_on = L_off + 120`.
- **Source:** v02 - Section: 5) Thuật toán chi tiết / Section: Sơ đồ A
- **Tag:** [vv02]

- **Fact:** Đối với phần cứng Yolo Uno (ESP32), dải ADC thường là 0–4095, cần lưu ý chuẩn hóa giá trị này tương ứng với thang đo PWM của firmware (thường là 0–100 hoặc 0–1023).
- **Source:** v02 - Section: 6) Mapping sang khối app.ohstem.vn / Section: Bạn nên sửa
- **Tag:** [vv02]
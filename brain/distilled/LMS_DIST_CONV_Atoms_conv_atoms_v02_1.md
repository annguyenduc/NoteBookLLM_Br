---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v02_1
  title: CONV_atoms_v02_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume 02 liên quan đến IoT, Arduino, YoloBit và Robotics:

- **Fact:** [CONV] Thuật toán đèn IoT sử dụng bộ lọc trung bình trượt (Moving Average) với cửa sổ N=10 mẫu để lọc nhiễu cảm biến ánh sáng.
- **Source:** v02 - Section: Thuật toán đèn IoT - 1) Kiến trúc & trạng thái
- **Tag:** [vv02]

- **Fact:** [CONV] Cơ chế Hysteresis với hai ngưỡng (L_on > L_off) được áp dụng để chống hiện tượng nhấp nháy đèn khi ánh sáng ở ngưỡng biên.
- **Source:** v02 - Section: Thuật toán đèn IoT - 1) Kiến trúc & trạng thái
- **Tag:** [vv02]

- **Fact:** [CONV] Hệ thống IoT hỗ trợ chế độ "Override": Khi đang ở chế độ AUTO nhưng nhận lệnh MANUAL, hệ thống sẽ ghi đè trong một khoảng thời gian (TTL), sau đó tự động quay lại AUTO.
- **Source:** v02 - Section: Thuật toán đèn IoT - 1) Kiến trúc & trạng thái
- **Tag:** [vv02]

- **Fact:** [CONV] Các tham số vận hành khuyến nghị cho hệ thống đèn IoT: lấy mẫu mỗi 200ms, gửi dữ liệu MQTT mỗi 3000ms, và duy trì PWM tối thiểu 20% để tránh vùng phi tuyến của LED.
- **Source:** v02 - Section: Thuật toán đèn IoT - 2) Tham số khuyến nghị
- **Tag:** [vv02]

- **Fact:** [CONV] Cấu trúc MQTT chuẩn cho thiết bị gồm topic `.../cmd` để nhận lệnh JSON (mode, state, brightness) và topic `.../state` để phản hồi trạng thái hệ thống.
- **Source:** v02 - Section: Thuật toán đèn IoT - 4) MQTT topic & payload
- **Tag:** [vv02]

- **Fact:** [CONV] Thuật toán làm mượt độ sáng (lerp) sử dụng hệ số alpha từ 0.1 đến 0.3 giúp LED chuyển đổi trạng thái mượt mà, không bị nhảy gắt.
- **Source:** v02 - Section: Thuật toán đèn IoT - 7) Mẹo chống nhấp nháy & độ bền
- **Tag:** [vv02]

- **Fact:** [CONV] Trên nền tảng Yolo Uno (ESP32), cần sử dụng chân hỗ trợ PWM và lệnh `write_analog` thay vì `write_digital` để điều khiển cường độ sáng của đèn.
- **Source:** v02 - Section: Bạn nên sửa - 1) Đưa PWM vào chân hỗ trợ PWM
- **Tag:** [vv02]

- **Fact:** [CONV] Lọc ngoại lệ (Outlier filtering) được thực hiện bằng cách kẹp giá trị đo (`L_x`) nếu độ lệch so với giá trị trung bình (`L_ema`) vượt quá ngưỡng cho phép (`L_outlier`).
- **Source:** v02 - Section: Bạn nên thêm - 3) Giới hạn nhiễu & ngoại lệ đo
- **Tag:** [vv02]

- **Fact:** [CONV] Quy ước kênh truyền trên OhStem IoT: V1 dùng cho lệnh điều khiển (cmd), V2 dùng báo cáo trạng thái (state), và V3 dùng cho số liệu đo lường (metrics).
- **Source:** v02 - Section: 1) Hiểu đúng các khối trong ảnh & 5) Quy ước tối thiểu
- **Tag:** [vv02]

- **Fact:** [CONV] Tính năng hiệu chuẩn nhanh (Fast Calibration) cho phép tự động thiết lập ngưỡng `L_off = ema + 20` và `L_on = L_off + 120` dựa trên môi trường ánh sáng hiện tại.
- **Source:** v02 - Section: Bạn nên thêm - 5) Hiệu chuẩn nhanh
- **Tag:** [vv02]
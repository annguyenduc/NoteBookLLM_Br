---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v01_8
  title: atoms_v01_8
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** Để chống lag hoặc nhấp nháy trong điều khiển, chỉ nên thay đổi trạng thái khi có từ 3–5 khung hình liên tiếp cùng nhãn (cơ chế debounce).
- **Source:** (v01 - Section: Gợi ý chống lag/nhấp nháy)
- **Tag:** [vv01]

- **Fact:** Chu kỳ thực hiện lệnh GET của Arduino UNO nên duy trì ở mức ≥ 300 ms (khuyến nghị 500 ms) để đảm bảo độ mượt và tránh nghẽn mạng.
- **Source:** (v01 - Section: Gợi ý chống lag/nhấp nháy)
- **Tag:** [vv01]

- **Fact:** Đối với các thiết bị cơ cấu chấp hành như servo hoặc động cơ, cần thêm khoảng thời gian "giữ tối thiểu" từ 1–2 giây sau mỗi lần chuyển trạng thái.
- **Source:** (v01 - Section: Gợi ý chống lag/nhấp nháy)
- **Tag:** [vv01]

- **Fact:** ESP8266 là vi điều khiển tích hợp Wi-Fi 2.4 GHz (802.11 b/g/n), sử dụng CPU 32-bit Tensilica (80–160 MHz), RAM khả dụng khoảng 50 KB và Flash từ 512 KB đến 4 MB.
- **Source:** (v01 - Section: ⚙️ 1. ESP8266 là gì?)
- **Tag:** [vv01]

- **Fact:** Các chân GPIO D0, D3, D4 trên ESP8266 không nên sử dụng cho cảm biến khởi động vì chúng ảnh hưởng đến quá trình boot của vi điều khiển.
- **Source:** (v01 - Section: ⚠️ 5. Lưu ý khi dùng ESP8266 cho IoT)
- **Tag:** [vv01]

- **Fact:** ESP8266 yêu cầu nguồn điện 3.3V ổn định; nếu sử dụng nhiều cảm biến hoặc relay, cần thiết kế nguồn cấp riêng để tránh sụt áp.
- **Source:** (v01 - Section: ⚠️ 5. Lưu ý khi dùng ESP8266 cho IoT)
- **Tag:** [vv01]

- **Fact:** Yolo UNO sử dụng chip vi điều khiển ESP32-S3.
- **Source:** (v01 - Section: ⚠️ 5. Lưu ý khi dùng ESP8266 cho IoT)
- **Tag:** [vv01]

- **Fact:** Để tối ưu hóa băng thông MQTT, nên gom nhiều dữ liệu cảm biến vào một gói tin định dạng JSON thay vì gửi riêng lẻ trên nhiều topic.
- **Source:** (v01 - Section: 1) Giảm “bão” dữ liệu từ thiết bị)
- **Tag:** [vv01]

- **Fact:** Trong giao thức MQTT cho IoT, nên sử dụng QoS=0 cho dữ liệu dòng (telemetry) và QoS=1 cho các lệnh điều khiển quan trọng (command).
- **Source:** (v01 - Section: 2) MQTT cấu hình “chống nghẽn”)
- **Tag:** [vv01]

- **Fact:** Cơ chế "Exponential Backoff" (tăng dần thời gian chờ: 1s, 2s, 4s... đến 32s) giúp tránh tình trạng "reconnect storm" khi thiết bị cố gắng kết nối lại máy chủ đồng loạt.
- **Source:** (v01 - Section: 2) MQTT cấu hình “chống nghẽn”)
- **Tag:** [vv01]

- **Fact:** Khi triển khai Wi-Fi cho dự án IoT, nên cố định các kênh sạch như 1, 6 hoặc 11 trên băng tần 2.4 GHz để giảm nhiễu.
- **Source:** (v01 - Section: 3) Mạng & nguồn)
- **Tag:** [vv01]

- **Fact:** ThingsBoard Community Edition là nền tảng IoT mã nguồn mở hỗ trợ các giao thức MQTT, HTTP, CoAP và cho phép tự vận hành trên máy chủ riêng.
- **Source:** (v01 - Section: 🎯 Gợi ý lựa chọn nhanh cho bạn)
- **Tag:** [vv01]

- **Fact:** AWS IoT Core cung cấp gói miễn phí (Free-tier) cho phép gửi 250,000 bản tin mỗi tháng trong vòng 12 tháng đầu tiên.
- **Source:** (v01 - Section: 🎯 Gợi ý lựa chọn nhanh cho bạn)
- **Tag:** [vv01]

- **Fact:** Hiện tượng "ô cam" (Text Log) trên giao diện OhStem bị nhảy dòng liên tục thường do thiết bị gửi dữ liệu định kỳ (ví dụ mỗi 300ms) ngay cả khi giá trị không thay đổi.
- **Source:** (v01 - Section: Conversation: Khắc phục ô cam liên tục)
- **Tag:** [vv01]

- **Fact:** Tại thời điểm khởi động (boot), thiết bị IoT thường nhận hàng loạt bản tin do Broker gửi lại giá trị cuối (retained messages) hoặc do Dashboard đồng bộ giá trị mặc định.
- **Source:** (v01 - Section: Tôi thấy khởi động là gửi nhận được nhiều thông tin có sao không)
- **Tag:** [vv01]

- **Fact:** Sử dụng biến cờ `booting` kết hợp với bộ hẹn giờ (Timer) khoảng 1 giây sau khi kết nối MQTT giúp chặn việc gửi dữ liệu phản hồi ngược lên server trong giai đoạn khởi tạo, tránh gây vòng lặp spam.
- **Source:** (v01 - Section: B. Bỏ qua “đợt bản tin đầu” khi boot)
- **Tag:** [vv01]
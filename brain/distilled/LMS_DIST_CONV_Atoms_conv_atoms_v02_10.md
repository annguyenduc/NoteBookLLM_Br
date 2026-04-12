---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v02_10
  title: CONV_atoms_v02_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v02) về chủ đề IoT, Yolo:Bit, Yolo UNO và cảm biến IR, tuân thủ quy tắc LOM v4.1:

- **Fact:** [CONV] Broker MQTT sẽ tự động tạo topic (chủ đề) ngay khi có thiết bị thực hiện hành động "publish" (gửi dữ liệu) đến topic đó lần đầu tiên, người dùng không cần tạo thủ công trên server.
- **Source:** [vv02] - Bước 2: Tạo chương trình khối như sau.
- **Tag:** [vv02]

- **Fact:** [CONV] Để kiểm tra dữ liệu MQTT trên web hoặc ứng dụng điện thoại (như MQTT Explorer/Dash), cấu hình tiêu chuẩn thường dùng Host là `test.mosquitto.org` và Port là `1883`.
- **Source:** [vv02] - Bước 3: Kiểm tra trên MQTT Explorer (hoặc MQTT Dash).
- **Tag:** [vv02]

- **Fact:** [CONV] Trên thiết bị Yolo:Bit, chân cắm P1 thường được sử dụng để khởi tạo và nhận tín hiệu từ cảm biến hồng ngoại (IR).
- **Source:** [vv02] - 1️⃣ Điểm đúng (rất tốt) - Khởi tạo cảm biến IR.
- **Tag:** [vv02]

- **Fact:** [CONV] Trong lập trình IoT MQTT, để tránh việc gửi dữ liệu lặp lại liên tục gây nghẽn mạng (spam), nên sử dụng biến phụ (ví dụ: `last_published`) để so sánh và chỉ gửi dữ liệu khi giá trị mới khác với giá trị vừa gửi.
- **Source:** [vv02] - 2️⃣ Điểm cần chỉnh nhỏ (để chắc chắn chạy ổn hơn).
- **Tag:** [vv02]

- **Fact:** [CONV] Hệ thống Dashboard IoT của OhStem quy ước các "Kênh thông tin" (V1, V2, V3...) tương ứng với các topic MQTT; ví dụ: cấu hình widget ở kênh V1 trên Dashboard thì trong code phải gửi dữ liệu đến chủ đề "V1".
- **Source:** [vv02] - 🧠 Giải thích nhanh - Dashboard IoT của OhStem.
- **Tag:** [vv02]

- **Fact:** [CONV] Đối với Yolo UNO (dựa trên chip ESP32), không nên kết nối cảm biến IR vào chân D3 vì chân này trùng với chức năng UART/TX, dễ gây xung đột; thay vào đó nên sử dụng chân D6 hoặc D7.
- **Source:** [vv02] - 1) Chân cắm IR: đừng dùng D3.
- **Tag:** [vv02]

- **Fact:** [CONV] Các chân tín hiệu của ESP32 (trên Yolo UNO) không chịu được điện áp 5V; do đó cảm biến IR và các module ngoại vi nên được cấp nguồn 3.3V (3V3) để đảm bảo an toàn cho vi điều khiển.
- **Source:** [vv02] - 6) Những lỗi thường gặp khác trên UNO.
- **Tag:** [vv02]

- **Fact:** [CONV] Hầu hết các loại remote hồng ngoại phổ thông (như remote TV) sử dụng giao thức NEC để mã hóa tín hiệu.
- **Source:** [vv02] - 6) Những lỗi thường gặp khác trên UNO.
- **Tag:** [vv02]

- **Fact:** [CONV] Trong môi trường lập trình khối của OhStem, biến "tín hiệu" là biến hệ thống tự sinh ra bên trong khối sự kiện "Khi nhận được tín hiệu từ remote", chứa mã số định danh của nút bấm vừa nhận được.
- **Source:** [vv02] - 🧠 1️⃣ “tín hiệu” là gì?.
- **Tag:** [vv02]

- **Fact:** [CONV] Để nhận tín hiệu IR một cách chủ động trong vòng lặp "Lặp lại mãi" (thay vì dùng khối sự kiện), người dùng cần sử dụng khối lệnh "đọc tín hiệu thu từ remote" và gán vào một biến số.
- **Source:** [vv02] - ⚙️ 2️⃣ “đọc tín hiệu từ remote” là gì?.
- **Tag:** [vv02]

- **Fact:** [CONV] Một số mã nút bấm phổ biến trên remote hồng ngoại (loại NEC) thường gặp là 162 (thường dùng cho lệnh Bật) và 98 (thường dùng cho lệnh Tắt). [Unverified_Source] (Dựa trên ví dụ minh họa trong văn bản).
- **Source:** [vv02] - ⚙️ 2️⃣ Ví dụ: Điều khiển đèn (relay hoặc LED).
- **Tag:** [vv02]
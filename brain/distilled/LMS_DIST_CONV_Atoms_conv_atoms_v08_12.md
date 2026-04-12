---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v08_12
  title: CONV_atoms_v08_12
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn cung cấp (Volume v08) về IoT, Robotics và lập trình Minecraft:

- Fact: [CONV] Cảm biến dò đường 4 mắt của robot Rover sử dụng chip PCF8574 kết nối qua giao tiếp I2C tại chân P19/P20, hỗ trợ tự động quét địa chỉ trong dải từ 0x20 đến 0x27.
- Source: [v08 - Section: Rover THCS PID FSM]
- Tag: [vv08]

- Fact: [CONV] Trong lập trình điều khiển Rover, giá trị cảm biến dò đường được chuẩn hóa theo quy tắc: phát hiện vạch đen tương ứng với giá trị 1 và nền trắng tương ứng với giá trị 0.
- Source: [v08 - Section: Rover THCS PID FSM]
- Tag: [vv08]

- Fact: [CONV] Thông số cấu hình PID mặc định cho Rover chạy Python thường là Kp=22, Ki=0, Kd=12, với tốc độ cơ bản (base_speed) đề xuất từ 35 đến 55.
- Source: [v08 - Section: Bạn cần chỉnh gì?]
- Tag: [vv08]

- Fact: [CONV] Hệ thống điều khiển Rover sử dụng mô hình trạng thái (State Machine) bao gồm các trạng thái: FOLLOW (dò line), JUNCTION (xử lý giao lộ), STOP_ALIGN (căn chỉnh dừng) và LOST (cứu hộ khi mất line).
- Source: [v08 - Section: State machine đã có]
- Tag: [vv08]

- Fact: [CONV] File dự án YoloBit (.json) khi import vào app.ohstem.vn yêu cầu phải khai báo đúng thông tin thiết bị "device: yolobit" và các thư viện mở rộng (extensions) như ROVER, ROBOCON, và EVENTS.
- Source: [v08 - Section: ASSISTANT (YoloBit .json)]
- Tag: [vv08]

- Fact: [CONV] Lệnh `builder.tracePath(block)` trong Minecraft Education Edition dùng để đặt các khối dọc theo lộ trình di chuyển của Builder tính từ vị trí được đánh dấu (`builder.mark()`) gần nhất.
- Source: [v08 - Section: Giải thích trace path]
- Tag: [vv08]

- Fact: [CONV] Trong Minecraft Education v1.21.91 (nền Bedrock), hướng của Hopper được điều khiển qua thuộc tính `facing_direction` với các mã số: 0 (Down), 2 (North), 3 (South), 4 (West), 5 (East).
- Source: [v08 - Section: phiên bản của tôi là minecraft edu v1.21.91]
- Tag: [vv08]

- Fact: [CONV] Tính năng `agent.setAssist` trong Minecraft cung cấp 3 quyền năng cho Agent: `place on move` (tự đặt khối khi đi), `place from any slot` (tự tìm khối trong kho đồ) và `destroy obstacles` (tự phá vật cản).
- Source: [v08 - Section: Giải thích setAssist Minecraft]
- Tag: [vv08]

- Fact: [CONV] Để đảm bảo Hopper kết nối chính xác vào Trapped Chest bằng Agent mà không cần dùng lệnh phức tạp, phương pháp tối ưu là cho Agent di chuyển lên trên nóc Chest và thực hiện lệnh `agent.place(DOWN)`.
- Source: [v08 - Section: Cách 1 (dễ & chuẩn): Cho hopper đổ xuống trapped chest]
- Tag: [vv08]

- Fact: [CONV] Thuật toán PID thuần bằng khối lệnh (Blockly) cho robot được tính theo công thức: `boost = Kp*err + Ki*integ + Kd*(err - lastErr)`, sau đó điều chỉnh tốc độ bánh trái bằng `baseSpeed - boost` và bánh phải bằng `baseSpeed + boost`.
- Source: [v08 - Section: Bên trong có gì (đều là khối Blockly)]
- Tag: [vv08]
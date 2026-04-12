---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v03_1
  title: CONV_atoms_v03_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu Volume 03:

- Fact: [CONV] Nhiệt độ vòi phun tối đa của máy in 3D Neptune 4 (bao gồm các dòng Plus, Max, Pro) là 300 °C.
- Source: [v03 - Section: Nhiệt độ sấy mực ẩm]
- Tag: [vv03]

- Fact: [CONV] Nhựa PLA bắt đầu mềm ở nhiệt độ chuyển thủy tinh (glass transition temperature) khoảng 55 °C; nếu sấy vượt quá mức này dây nhựa sẽ biến dạng hoặc dính lại.
- Source: [v03 - Section: Nhiệt độ sấy mực ẩm - 1. Hiểu về giới hạn của PLA]
- Tag: [vv03]

- Fact: [CONV] Khi sấy cuộn nhựa PLA bằng bàn nhiệt (heatbed) của máy in 3D, nhiệt độ khuyến nghị là 45 °C – 50 °C trong khoảng 4 – 8 giờ.
- Source: [v03 - Section: Nhiệt độ sấy mực ẩm - 2. Thiết lập an toàn trên Neptune 4]
- Tag: [vv03]

- Fact: [CONV] Trong G-code, lệnh M140 dùng để đặt nhiệt độ bàn nhiệt, M190 dùng để chờ bàn nhiệt đạt nhiệt độ mục tiêu, và G4 S[giây] dùng để duy trì trạng thái (dwell) trong một khoảng thời gian tính bằng giây.
- Source: [v03 - Section: Nhiệt độ sấy mực ẩm - G-code file]
- Tag: [vv03]

- Fact: [CONV] Cảm biến PIR (hồng ngoại thụ động) cần thời gian khởi động (warm-up) từ 20 – 60 giây sau khi cấp nguồn; trong giai đoạn này, cảm biến thường trả về giá trị 1 (HIGH) liên tục.
- Source: [v03 - Section: Giải thích cảm biến PIR - 1) Cách PIR “đúng”]
- Tag: [vv03]

- Fact: [CONV] Cảm biến PIR hoạt động theo logic active-HIGH: khi có chuyển động trả về 1 (True), khi không có chuyển động trả về 0 (False).
- Source: [v03 - Section: 0 là true, 1 là false đúng hay sai]
- Tag: [vv03]

- Fact: [CONV] Cảm biến vật cản hồng ngoại (IR Obstacle Sensor) hoạt động theo logic active-LOW: trả về giá trị 0 khi có vật cản và giá trị 1 khi không có vật cản do cơ chế mạch transistor đảo.
- Source: [v03 - Section: Tại sao trong mblock thì 0 là có vật cản]
- Tag: [vv03]

- Fact: [CONV] Cảm biến ánh sáng (LDR) trên Yolo Uno trả về giá trị Analog trong khoảng 0 – 4095, trong đó giá trị thấp tương ứng với ánh sáng mạnh và giá trị cao tương ứng với bóng tối.
- Source: [v03 - Section: Bảng tổng hợp logic tín hiệu cảm biến]
- Tag: [vv03]

- Fact: [CONV] Cảm biến va chạm (Touch/Collision) thường trả về giá trị 0 khi bị nhấn và 1 khi được thả ra (active-LOW).
- Source: [v03 - Section: Bảng tổng hợp logic tín hiệu cảm biến]
- Tag: [vv03]

- Fact: [CONV] Để chống nhiễu cho cảm biến PIR trên app.ohstem.vn, nên sử dụng bộ lọc yêu cầu giá trị đọc được phải giống nhau liên tiếp ít nhất 5 lần (mỗi 50-100ms) trước khi xác nhận trạng thái.
- Source: [v03 - Section: Vì sao “cùng code, cảm biến A luôn 1 – cảm biến B nhấp nháy?”]
- Tag: [vv03]
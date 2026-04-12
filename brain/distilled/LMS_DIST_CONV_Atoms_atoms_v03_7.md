---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v03_7
  title: atoms_v03_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v03 liên quan đến IoT, Arduino, YoloBit, Robotics và AI:

- **Fact:** Yolo UNO (dựa trên chip ESP32) có độ phân giải ADC là 12-bit, trả về giá trị trong khoảng từ 0 đến 4095.
- **Source:** Mục 1. Tại sao lại là 4095? / Bảng tóm tắt cuối mục 4.
- **Tag:** [vv03]

- **Fact:** Arduino UNO truyền thống có độ phân giải ADC là 10-bit, trả về giá trị trong khoảng từ 0 đến 1023.
- **Source:** Mục 3. Nếu bạn muốn dùng tỉ lệ 0–1023 / Bảng tóm tắt cuối mục 4.
- **Tag:** [vv03]

- **Fact:** Công thức toán học tổng quát để thay thế khối "map" khi chuyển đổi giá trị x từ khoảng [in_min, in_max] sang [out_min, out_max] là: `y = (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min`.
- **Source:** Mục 1) Công thức “map” tổng quát.
- **Tag:** [vv03]

- **Fact:** Để chuyển đổi nhanh giá trị analog từ 12-bit (Yolo UNO) sang 10-bit (Arduino UNO), ta có thể sử dụng công thức: `giá trị 10-bit = giá trị 12-bit / 4`.
- **Source:** Mục 2) Các công thức nhanh thường dùng - phần a.
- **Tag:** [vv03]

- **Fact:** Giá trị điều khiển độ sáng LED qua xung PWM trên các board mạch này thường nằm trong khoảng từ 0 (tắt hoàn toàn) đến 255 (sáng tối đa).
- **Source:** Mục 2) Các công thức nhanh thường dùng - phần c / Mục 💡 Lưu ý.
- **Tag:** [vv03]

- **Fact:** Các chân hỗ trợ xuất tín hiệu PWM trên Yolo UNO bao gồm: D3, D5, D6, D9, D10 và D11.
- **Source:** Mục 2) Các công thức nhanh thường dùng - phần c / Mục 💡 Lưu ý.
- **Tag:** [vv03]

- **Fact:** Để lập trình điều khiển LED sáng dần khi môi trường tối dần (PWM nghịch), công thức tính là: `pwm = round( (4095 - light_sensor_value) * 255 / 4095 )`.
- **Source:** Mục 2) Các công thức nhanh thường dùng - phần c.
- **Tag:** [vv03]

- **Fact:** Trên giao diện app.ohstem.vn, khối lệnh để xuất tín hiệu PWM nằm trong nhóm "Chân I/O" (hoặc Đầu vào/ra) với tên gọi "Ghi giá trị analog (PWM)" hoặc "xuất ra giá trị analog... cho chân...".
- **Source:** Mục 🔶 Cách tạo khối “ghi PWM chân D5 = pwm” / Mục ✅ Cách chỉnh lại khối đúng.
- **Tag:** [vv03]

- **Fact:** KDI Education là đơn vị triển khai giảng dạy STEM và biên soạn chương trình đào tạo về công nghệ, robot, lập trình cho học sinh khối THCS và THPT tại TP.HCM.
- **Source:** Phần KINH NGHIỆM LÀM VIỆC và DỰ ÁN & THÀNH TỰU trong mẫu CV.
- **Tag:** [vv03]

- **Fact:** Việc sử dụng khối "làm tròn" (round) và khối "min/max" là cần thiết khi tự xây dựng công thức map để đảm bảo giá trị PWM không vượt quá khoảng 0-255 và tránh lỗi dữ liệu.
- **Source:** Mục 2) Các công thức nhanh thường dùng - phần c và d.
- **Tag:** [vv03]
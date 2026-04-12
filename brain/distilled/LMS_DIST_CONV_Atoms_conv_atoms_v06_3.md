---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_3
  title: CONV_atoms_v06_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v06) liên quan đến lĩnh vực in 3D (một nhánh của Robotics/Prototyping):

- **Fact:** [CONV] Phần mềm Elegoo Cura 5.6 yêu cầu các profile (.curaprofile) phải khớp chính xác các thông số metadata như `definition`, `quality_type`, và `setting_version` để có thể import thành công.
- **Source:** [vv06] - Đoạn hội thoại hướng dẫn fix lỗi import profile.
- **Tag:** [vv06]

- **Fact:** [CONV] Cấu hình in PLA tiêu chuẩn cho máy Elegoo Neptune 4 bao gồm: Nhiệt độ đầu in 206°C, nhiệt độ bàn in 55°C, tốc độ in tường ngoài 25mm/s và tốc độ in layer đầu tiên 20mm/s.
- **Source:** [vv06] - Biến `base_values` trong mã nguồn Python và mục "Profile BASE".
- **Tag:** [vv06]

- **Fact:** [CONV] Để xử lý hiện tượng "chân voi" (elephant's foot) và giúp các khớp nối cơ khí (như chân robot Strandbeest) lắp ráp dễ dàng, thông số `Initial Layer Horizontal Expansion` nên được đặt ở mức -0.20 mm.
- **Source:** [vv06] - Mục "D) Mẹo để chạy mượt" và biến `base_values`.
- **Tag:** [vv06]

- **Fact:** [CONV] Các bộ phận chịu lực hoặc truyền động cơ khí (như bánh răng gear60) được khuyến nghị sử dụng mật độ lấp đầy (Infill) từ 40% đến 50% với kiểu Grid để đảm bảo độ bền.
- **Source:** [vv06] - Biến `gear_values` và mục "B) Dùng profile nào cho file nào".
- **Tag:** [vv06]

- **Fact:** [CONV] Thông số rút sợi (Retraction) tối ưu cho dòng Neptune 4 (sử dụng máy đùn trực tiếp) là 0.7 mm với tốc độ 35 mm/s.
- **Source:** [vv06] - Biến `base_values` trong script tạo profile.
- **Tag:** [vv06]

- **Fact:** [CONV] Trong Elegoo Cura, nếu không thể import trực tiếp file cấu hình, người dùng có thể tạo profile tùy biến bằng cách sử dụng tính năng "Duplicate" từ một profile gốc, sau đó dùng "Update profile with current settings".
- **Source:** [vv06] - Hướng dẫn tại "Bước 1 — Tạo profile CUSTOM".
- **Tag:** [vv06]

- **Fact:** [CONV] Metadata của máy in Elegoo Neptune 4 sử dụng Klipper thường định danh `definition` là `elegoo_base_klipper` và `quality_type` theo định dạng `Elegoo_klipper_layer_020`.
- **Source:** [vv06] - Dữ liệu RAW cuối file (đoạn mã máy in test).
- **Tag:** [vv06]

- **Fact:** [CONV] Đối với các chi tiết có diện tích tiếp xúc bàn in nhỏ hoặc hình dáng phức tạp (như trục khuỷu - crank), việc sử dụng Brim 6mm và bật Support Interface (độ dày 0.8mm, khoảng cách Z 0.2mm) là cần thiết để đảm bảo độ ổn định khi in.
- **Source:** [vv06] - Biến `crank_values` và mục "2) Profile CRANK – Support + Brim".
- **Tag:** [vv06]
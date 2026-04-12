---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v04_13
  title: atoms_v04_13
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dựa trên dữ liệu raw từ Volume v04, tôi xin trích xuất các sự kiện kỹ thuật về chế tạo (liên quan đến vỏ thiết bị Robotics/IoT) như sau:

- **Fact:** Thông số in 3D (Slicer settings) cơ bản cho các bộ phận kỹ thuật bao gồm Layer Height 0.20 mm và Line Width 0.42 mm.
- **Source:** Section: 4) Bộ thông số “cắt tơ” mình gợi ý sẵn
- **Tag:** [vv04]

- **Fact:** Cấu hình nhiệt độ in tiêu chuẩn: Đầu phun (Printing Temp) 200 °C (lớp đầu 205 °C) và Bàn in (Bed) từ 60 °C giảm dần về 55 °C.
- **Source:** Section: 4) Bộ thông số “cắt tơ” mình gợi ý sẵn
- **Tag:** [vv04]

- **Fact:** Thiết lập Retraction (rút nhựa) để chống hiện tượng "tơ" là 1.0 mm với tốc độ 40 mm/s; tính năng Retract at Layer Change được kích hoạt.
- **Source:** Section: 4) Bộ thông số “cắt tơ” mình gợi ý sẵn
- **Tag:** [vv04]

- **Fact:** Tốc độ di chuyển (Travel speed) của đầu in được thiết lập ở mức cao 230 mm/s; hệ thống làm mát (Fan) hoạt động 100% công suất từ layer thứ 3.
- **Source:** Section: 4) Bộ thông số “cắt tơ” mình gợi ý sẵn
- **Tag:** [vv04]

- **Fact:** Các kỹ thuật tối ưu hóa đường in và bề mặt bao gồm: Combing (Within Infill), Outer Wall Wipe Distance (0.3 mm) và Coasting (0.12 mm³).
- **Source:** Section: 4) Bộ thông số “cắt tơ” mình gợi ý sẵn
- **Tag:** [vv04]

- **Fact:** Các thông số cấu hình này được tối ưu hóa để sử dụng và nhập (import) vào phần mềm Elegoo Cura thông qua định dạng file `.curaprofile`.
- **Source:** Đoạn cuối văn bản raw
- **Tag:** [vv04]
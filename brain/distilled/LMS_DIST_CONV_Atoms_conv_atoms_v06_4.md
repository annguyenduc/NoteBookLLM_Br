---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_4
  title: CONV_atoms_v06_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v06):

- **Fact:** [CONV] Cấu hình định danh (definition) cho máy in Elegoo Neptune 4 sử dụng firmware Klipper trong phần mềm Elegoo Cura là `elegoo_base_klipper` với `quality_type` tương ứng là `Elegoo_klipper_layer_020`.
- **Source:** [Đoạn hội thoại đầu tiên của Assistant - Section: Elegoo Cura của bạn đang dùng]
- **Tag:** [vv06]

- **Fact:** [CONV] Thông số in cơ bản (BASE) cho các bộ phận robot (Strandbeest) bao gồm: Layer height 0.2mm, 3 Walls, Top/Bottom layers là 4/4, Infill 20% Grid, và tốc độ in thành ngoài (Outer wall) là 25mm/s.
- **Source:** [Section: Bước B — Điền thông số cho Strandbeest_BASE]
- **Tag:** [vv06]

- **Fact:** [CONV] Để tối ưu hóa việc tháo gỡ support cho các chi tiết cơ khí phức tạp (như crank), cần bật Support Interface với độ dày 0.8mm, mật độ 100% (Density), và khoảng cách Z (Support Z Distance) là 0.20mm.
- **Source:** [Section: Bước A — Tạo profile CUSTOM nền 0.2 mm & Code block tweak_ini cho crank]
- **Tag:** [vv06]

- **Fact:** [CONV] Các chi tiết chịu lực hoặc khớp nối như bánh răng (gear) và kẹp (clip) yêu cầu mật độ lấp đầy (Infill) cao hơn, từ 40% đến 50% với kiểu Grid để đảm bảo độ bền.
- **Source:** [Section: Bước C — Tạo 2 profile còn lại & Code block tweak_container cho GEAR_STRONG]
- **Tag:** [vv06]

- **Fact:** [CONV] Để xử lý sai số kích thước lớp đầu tiên (hiện tượng chân voi), thông số "Initial Layer Horizontal Expansion" nên được thiết lập ở giá trị âm, ví dụ -0.20 mm.
- **Source:** [Section: Bước B — Điền thông số cho Strandbeest_BASE]
- **Tag:** [vv06]

- **Fact:** [CONV] Lỗi `KeyError: 'id'` khi import profile trong Elegoo Cura thường do file `.curaprofile` thiếu khóa ID trong metadata; cách khắc phục triệt để là reset thư mục cấu hình trong `%APPDATA%\ELEGOOCura\5.6\`.
- **Source:** [Section: 1) Khôi phục Cura (xóa profile hỏng)]
- **Tag:** [vv06]

- **Fact:** [CONV] Thông số rút nhựa (Retraction) tối ưu cho dòng máy Neptune 4 (Direct Drive) khi in PLA là 0.7 mm với tốc độ 35 mm/s.
- **Source:** [Section: Bước B — Điền thông số cho Strandbeest_BASE]
- **Tag:** [vv06]

- **Fact:** [CONV] File định dạng `.curaprofile` thực chất là một tệp nén (ZIP) chứa các tệp cấu hình `.ini` quy định các giá trị (values) và thông tin chung (general) của profile máy in.
- **Source:** [Section: Inspect the uploaded .curaprofile as a ZIP & Code blocks xử lý zipfile]
- **Tag:** [vv06]
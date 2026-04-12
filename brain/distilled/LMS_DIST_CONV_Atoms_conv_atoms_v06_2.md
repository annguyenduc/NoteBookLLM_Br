---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_2
  title: CONV_atoms_v06_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu về cấu hình in 3D cho mô hình Strandbeest trên máy Elegoo Neptune 4:

- Fact: [CONV] Cấu hình in 3D cho Strandbeest được tối ưu hóa cho máy Neptune 4, sử dụng nhựa PLA và vòi phun (nozzle) 0.4mm.
- Source: [v06 - base_settings: metadata]
- Tag: [vv06]

- Fact: [CONV] Profile "BASE" (không support) được dùng cho phần lớn chi tiết: 8 chân (leg), 2 đầu (end), 2 thanh nối (siderod), giá đỡ (stand) và thân quạt (fan body).
- Source: [v06 - README instructions & CSV mapping]
- Tag: [vv06]

- Fact: [CONV] Chi tiết trục khuỷu (beest3-crank.stl) yêu cầu profile "CRANK_SUPPORT" với các thiết lập: Support Everywhere, Support Interface và Brim 6mm để đảm bảo độ bám.
- Source: [v06 - README instructions & crank_support_settings]
- Tag: [vv06]

- Fact: [CONV] Các chi tiết chịu lực như bánh răng (gear60) và kẹp quạt (fanclip) sử dụng profile "GEAR_STRONG" với mật độ lấp đầy (infill) từ 40% đến 50% và Brim 4mm.
- Source: [v06 - README instructions & gear_strong_settings]
- Tag: [vv06]

- Fact: [CONV] Thông số in cơ bản: Chiều cao lớp (layer height) 0.2mm, độ rộng đường in 0.4mm, 3 lớp tường (wall line count), 4 lớp trên/dưới (top/bottom layers).
- Source: [v06 - base_settings: settings]
- Tag: [vv06]

- Fact: [CONV] Tốc độ in được thiết lập 60mm/s cho Infill, 25-35mm/s cho tường (wall) và 20mm/s cho lớp đầu tiên.
- Source: [v06 - base_settings: settings]
- Tag: [vv06]

- Fact: [CONV] Nhiệt độ in khuyến nghị cho PLA là 206°C (đầu phun) và 55°C (bàn nhiệt); quạt làm mát chạy 100% từ lớp thứ 3.
- Source: [v06 - base_settings: settings & README]
- Tag: [vv06]

- Fact: [CONV] Thiết lập rút sợi (retraction) cho đầu đùn trực tiếp (direct drive) của Neptune 4 là 0.7mm với tốc độ 35mm/s.
- Source: [v06 - base_settings: settings]
- Tag: [vv06]

- Fact: [CONV] Để các khớp nối (pivots) chuyển động mượt mà, có thể giảm lưu lượng nhựa (Flow) xuống 98% và đặt Initial Layer Horizontal Expansion là -0.2mm để tránh hiện tượng "chân voi".
- Source: [v06 - README instructions: Tuning for moving joints]
- Tag: [vv06]

- Fact: [CONV] File cấu hình `.curaprofile` cho Elegoo Cura 5.x phải tuân thủ định dạng INI với các phân đoạn `[general]`, `[metadata]`, và `[values]`.
- Source: [v06 - Assistant's explanation in v2 response]
- Tag: [vv06]

- Fact: [CONV] Các định danh máy in (definition) thường gặp cho Neptune 4 trong phần mềm Cura bao gồm: `elegoo_neptune_4`, `ELEGOO_Neptune_4`, và `neptune_4`.
- Source: [v06 - definitions list in v3 Python block]
- Tag: [vv06]

- Fact: [CONV] Thiết lập gia tốc (Acceleration) khuyến nghị: tường trong 500 mm/s², tường ngoài 1000 mm/s², và infill 1500 mm/s².
- Source: [v06 - base_settings: settings]
- Tag: [vv06]

- Fact: [CONV] Cấu hình Support Interface được đặt độ cao 0.8mm và khoảng cách Z (support_z_distance) là 0.2mm để hỗ trợ việc tháo gỡ vật liệu chống dễ dàng hơn.
- Source: [v06 - base_settings: settings]
- Tag: [vv06]
Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu về cấu hình in 3D cho robot Strandbeest trên máy Neptune 4:

- **Fact:** Cấu hình in 3D tiêu chuẩn cho nhựa PLA trên máy Neptune 4 (vòi phun 0.4mm) bao gồm: Layer height 0.2mm, Line width 0.4mm, Wall line count 3, Top/Bottom layers 4, và Infill 20% dạng Grid.
- **Source:** (v06 - Section: base_settings)
- **Tag:** [vv06]

- **Fact:** Thông số tốc độ in tối ưu cho độ chi tiết của robot: Tường ngoài (Wall 0) 25mm/s, Tường trong (Wall X) 35mm/s, Infill và tốc độ in chung 60mm/s, lớp đầu tiên (Layer 0) 20mm/s.
- **Source:** (v06 - Section: base_settings - Speeds)
- **Tag:** [vv06]

- **Fact:** Cài đặt nhiệt độ cho vật liệu PLA trên Neptune 4: Đầu đùn (Nozzle) 206°C và Bàn nhiệt (Bed) 55°C. Quạt tản nhiệt (Cooling fan) nên đạt 100% công suất từ lớp thứ 3.
- **Source:** (v06 - Section: base_settings - Temperatures & README instructions)
- **Tag:** [vv06]

- **Fact:** Đối với hệ thống đùn trực tiếp (Direct Drive) của Neptune 4, thông số rút sợi (Retraction) được thiết lập: Khoảng cách 0.7mm, Tốc độ 35mm/s và bật chế độ Combing trong vùng Infill.
- **Source:** (v06 - Section: base_settings - Retraction)
- **Tag:** [vv06]

- **Fact:** Để đảm bảo các khớp nối cơ khí (pivots) của chân robot Strandbeest không bị dính và chuyển động mượt mà, cần thiết lập Initial Layer Horizontal Expansion là -0.2mm và có thể giảm lưu lượng nhựa (Flow) xuống 98%.
- **Source:** (v06 - Section: README instructions - Tuning for moving joints)
- **Tag:** [vv06]

- **Fact:** Chi tiết trục khuỷu (Crank) yêu cầu cài đặt hỗ trợ (Support Everywhere), có lớp đệm (Support Interface) cao 0.8mm và sử dụng Brim 6mm để tăng diện tích bám dính bàn in.
- **Source:** (v06 - Section: crank_support_settings & CSV mapping)
- **Tag:** [vv06]

- **Fact:** Các bộ phận chịu lực như bánh răng (Gear60) và kẹp quạt (Fanclip) cần tăng mật độ Infill lên 40% - 50% để đảm bảo độ bền cơ học.
- **Source:** (v06 - Section: gear_strong_settings & CSV mapping)
- **Tag:** [vv06]

- **Fact:** Phần mềm Elegoo Cura 5.x yêu cầu file `.curaprofile` phải ở định dạng INI (chứa các header [general], [metadata], [values]) thay vì định dạng JSON thuần túy để có thể nhập (import) vào hệ thống.
- **Source:** (v06 - Assistant response regarding INI-style profiles)
- **Tag:** [vv06]

- **Fact:** Lỗi "Unable to add the profile" khi import vào Cura thường do sự không tương thích của định danh máy in (definition ID). Các ID phổ biến cho Neptune 4 bao gồm: `elegoo_neptune_4`, `ELEGOO_Neptune_4`, hoặc `neptune_4`.
- **Source:** (v06 - Assistant response after second error)
- **Tag:** [vv06]

- **Fact:** Strandbeest là cơ cấu cơ khí mô phỏng sinh học (Kinetic Sculpture) sử dụng hệ thống chân khớp phức tạp để di chuyển bằng sức gió hoặc động cơ.
- **Source:** [Unverified_Source]
- **Tag:** [vv06]
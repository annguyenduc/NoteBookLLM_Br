---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_6
  title: CONV_atoms_v06_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v06:

- **Fact:** [CONV] File `beest3-leg.stl` (thuộc dự án Strandbeest) là một cụm khớp in-place, cho phép in các thanh liên kết và bản lề liền khối trong một lần in mà vẫn có thể chuyển động sau khi xử lý.
- **Source:** [v06 - Section: Assistant response regarding beest3-leg.stl]
- **Tag:** [vv06]

- **Fact:** [CONV] Để tránh dính khớp khi in 3D các cơ cấu chuyển động (in-place), nên thiết lập `Initial Layer Horizontal Expansion = -0.20 mm` hoặc `Horizontal Expansion = -0.05` đến `-0.10 mm`.
- **Source:** [v06 - Section: Cách in & “khai thông” khớp]
- **Tag:** [vv06]

- **Fact:** [CONV] Máy in 3D Elegoo Neptune 4 có kích thước bàn in (Build Volume) là 225 x 225 x 265 mm, sử dụng đầu phun (Nozzle) mặc định 0.4 mm và nhựa (Filament) đường kính 1.75 mm.
- **Source:** [v06 - Section: 1. Thêm máy in Neptune 4 vào Cura]
- **Tag:** [vv06]

- **Fact:** [CONV] Thông số in PLA khuyến nghị cho Neptune 4 bao gồm: Nhiệt độ đầu phun 200-210°C, nhiệt độ bàn nhiệt 55-60°C, tốc độ in từ 100-150 mm/s.
- **Source:** [v06 - Section: 2. Thông số in khuyến nghị cho Neptune 4 (PLA)]
- **Tag:** [vv06]

- **Fact:** [CONV] Trong phần mềm Cura, việc thay đổi kích thước Nozzle và đường kính nhựa (Compatible material diameter) phải được thực hiện trong tab `Machine Settings -> Extruder 1`.
- **Source:** [v06 - Section: Cách chỉnh nozzle trong Cura (cho Neptune 4)]
- **Tag:** [vv06]

- **Fact:** [CONV] File G-code là tập hợp các lệnh điều khiển máy in đã được tính toán sẵn; người dùng không thể thay đổi các thông số như Layer Height, Infill hay Support trực tiếp trên file này bằng phần mềm Slicer (Cura) mà phải dùng file gốc (STL/OBJ/3MF).
- **Source:** [v06 - Section: 2. Muốn chỉnh sửa thông số in]
- **Tag:** [vv06]

- **Fact:** [CONV] Mã lệnh G-code `G28` được dùng để đưa tất cả các trục về vị trí gốc (Home all axes), và `G92 E0` dùng để thiết lập lại vị trí của bộ đùn nhựa (Reset Extruder).
- **Source:** [v06 - Section: Start G-code (đề xuất cho Neptune 4)]
- **Tag:** [vv06]

- **Fact:** [CONV] Chế độ Preview trong Cura sử dụng bảng màu (Color Scheme) để phân biệt các thành phần: màu đỏ thường đại diện cho vỏ ngoài (Outer Wall), màu vàng cho vỏ trong (Inner Wall) và màu xanh cho phần Infill hoặc Support.
- **Source:** [v06 - Section: Tại sao lại có màu đỏ?]
- **Tag:** [vv06]

- **Fact:** [CONV] Có thể sử dụng Python (thư viện `struct`, `math`) để xử lý file STL binary: đọc dữ liệu tam giác (triangles), tính toán vector pháp tuyến (normal vector) và thực hiện scale tọa độ các đỉnh (vertices).
- **Source:** [v06 - Python code blocks: read_stl_triangles, scale_tris, write_binary_stl]
- **Tag:** [vv06]

- **Fact:** [CONV] Khi scale nhỏ mô hình (ví dụ xuống 85%), các khe hở cơ khí (clearance) sẽ bị thu hẹp lại, đòi hỏi phải điều chỉnh giảm Flow (lưu lượng nhựa) xuống khoảng 96-98% để đảm bảo các khớp không bị dính.
- **Source:** [v06 - Section: Khi bạn đã scale 85%]
- **Tag:** [vv06]
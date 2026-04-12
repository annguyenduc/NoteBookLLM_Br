---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v06_6
  title: atoms_v06_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v06):

- **Fact:** [Mô hình `beest3-leg.stl` (thuộc dự án Strandbeest) là một cụm khớp in-place, trong đó các thanh liên kết được in liền khối với các bản lề/pivot bên trong và có thể xoay tự do sau khi tác động lực nhẹ.]
- **Source:** [Đoạn: Beest3-Leg.STL, chân này có khớp chuyển động không?]
- **Tag:** [vv06]

- **Fact:** [Khi thực hiện scale mô hình có khớp chuyển động xuống 85%, khe hở (clearance) giữa các bộ phận sẽ bị thu hẹp, đòi hỏi phải điều chỉnh giảm Flow (96–98%) hoặc tăng giá trị âm cho Horizontal Expansion để tránh dính khớp.]
- **Source:** [Đoạn: Khi bạn đã scale 85%]
- **Tag:** [vv06]

- **Fact:** [Máy in 3D Elegoo Neptune 4 có kích thước vùng in (build volume) là 225 x 225 x 265 mm, sử dụng sợi nhựa (filament) đường kính 1.75 mm và đầu phun (nozzle) tiêu chuẩn 0.4 mm.]
- **Source:** [Đoạn: 1. Thêm máy in Neptune 4 vào Cura và 2. Tab Extruder 1]
- **Tag:** [vv06]

- **Fact:** [Thông số in PLA tối ưu cho Neptune 4 bao gồm: nhiệt độ đầu phun 200-210°C, nhiệt độ bàn nhiệt 55-60°C, và tốc độ in có thể đạt từ 100-150 mm/s.]
- **Source:** [Đoạn: 2. Thông số in khuyến nghị cho Neptune 4 (PLA)]
- **Tag:** [vv06]

- **Fact:** [Phần mềm Ultimaker Cura 5.2.2 là công cụ cắt lớp (slicer) dùng để chuyển đổi các định dạng file 3D như .STL, .OBJ, .3MF thành mã lệnh G-code cho máy in.]
- **Source:** [Đoạn: 1. Cài đặt và chuẩn bị và 2. Nạp mô hình 3D]
- **Tag:** [vv06]

- **Fact:** [Trong cấu trúc mã G-code, lệnh M104/M109 được dùng để quản lý nhiệt độ đầu phun (hotend), M140/M190 quản lý nhiệt độ bàn in (bed) và M106 điều khiển tốc độ quạt làm mát.]
- **Source:** [Đoạn: b. Nếu chỉ có G-code, không có STL]
- **Tag:** [vv06]

- **Fact:** [Để xử lý lỗi "elephant's foot" hoặc khớp bị dính ở lớp in đầu tiên, có thể thiết lập thông số Initial Layer Horizontal Expansion về giá trị âm (ví dụ: -0.20 mm).]
- **Source:** [Đoạn: Cách in & “khai thông” khớp]
- **Tag:** [vv06]

- **Fact:** [Cấu trúc file STL định dạng Binary bao gồm phần tiêu đề (header) 80 bytes, tiếp theo là 4 bytes lưu số lượng tam giác, và mỗi tam giác được mô tả trong 50 bytes dữ liệu (bao gồm vector pháp tuyến và tọa độ 3 đỉnh).]
- **Source:** [Đoạn: Python code - hàm read_stl_triangles và write_binary_stl]
- **Tag:** [vv06]

- **Fact:** [AI (ChatGPT) được ứng dụng như một trợ lý lập trình để viết các kịch bản Python tự động hóa việc đọc, tính toán vector pháp tuyến và thay đổi tỉ lệ (scale) cho các tệp tin đồ họa 3D STL.]
- **Source:** [Đoạn: Python code và phản hồi của Assistant]
- **Tag:** [vv06]

- **Fact:** [Dự án robot cơ khí Strandbeest bao gồm các thành phần chính: chân (leg), thanh nối (siderod), trục khuỷu (crank), bánh răng (gear60), quạt (fan) và khung đỡ (stand).]
- **Source:** [Đoạn: Đã scale tất cả STL xuống 85%...]
- **Tag:** [vv06]
---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_5
  title: CONV_atoms_v06_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v06 liên quan đến Robotics và kỹ thuật in 3D (phục vụ chế tạo robot Strandbeest):

- **Fact:** [CONV] Các thành phần cơ khí chính của robot Strandbeest (phiên bản beest3) bao gồm: chân (leg), khớp nối (end), thanh bên (siderod), trục quay (crank), bánh răng (gear60), kẹp quạt (fanclip) và cánh quạt (fan).
- **Source:** [v06 - Section: Assistant's summary table of STL files]
- **Tag:** [vv06]

- **Fact:** [CONV] Profile in 3D "GEAR_STRONG" được tối ưu cho các chi tiết chịu lực như bánh răng với thông số: Infill 40% (Grid), Adhesion Brim 4mm, Walls 3 lớp, tốc độ in từ 20-60 mm/s và nhiệt độ đầu phun/bàn nhiệt là 206/55 °C.
- **Source:** [v06 - Section: GEAR_STRONG profile changes]
- **Tag:** [vv06]

- **Fact:** [CONV] Chi tiết trục quay (beest3-crank.stl) yêu cầu chế độ hỗ trợ đặc biệt (Support Everywhere) với lớp đệm (Interface) dày 0.8mm, mật độ 100%, kiểu Lines và khoảng cách Z là 0.20mm để đảm bảo độ chính xác cơ khí.
- **Source:** [v06 - Section: Profile CRANK_SUPPORT details]
- **Tag:** [vv06]

- **Fact:** [CONV] Thời gian in 3D tỉ lệ thuận với lập phương của tỉ lệ thu phóng (scale³). Ví dụ, khi scale mô hình xuống 85%, thời gian in sẽ giảm khoảng 38%.
- **Source:** [v06 - Section: Scaling and time estimation]
- **Tag:** [vv06]

- **Fact:** [CONV] Để tránh hiện tượng dính khớp (fuse) khi in các bộ phận robot có khớp nối in-place (in liền khối), cần thiết lập Initial Layer Horizontal Expansion ở mức -0.20 mm hoặc giảm lưu lượng nhựa (Flow) xuống 96-98%.
- **Source:** [v06 - Section: Scaling and clearance advice]
- **Tag:** [vv06]

- **Fact:** [CONV] Trong cấu trúc in 3D của các bộ phận robot dạng thanh (như chân Strandbeest), phần tường (Walls) có thể chiếm tới 79% tổng thời gian in, trong khi phần bù (Infill) chỉ chiếm tỉ lệ rất nhỏ (khoảng 6%).
- **Source:** [v06 - Section: Analysis of print time by line type]
- **Tag:** [vv06]

- **Fact:** [CONV] Việc tăng tốc độ in cho lớp tường trong (Inner Wall Speed) và giảm thời gian tối thiểu cho mỗi lớp (Minimum Layer Time) xuống 5 giây là những kỹ thuật hiệu quả để giảm thời gian in mà vẫn giữ được chất lượng bề mặt robot.
- **Source:** [v06 - Section: Optimization packages A & B]
- **Tag:** [vv06]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v05_2
  title: atoms_v05_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v05 liên quan đến cấu hình in 3D (Robotics/Prototyping) và xử lý dữ liệu (AI/Data Processing):

- **Fact:** Độ dày lớp in (Layer Height) tối ưu để in nhanh mô hình tháp Eiffel là 0.24 mm.
- **Source:** (v05 - Section: Độ dày lớp & tường)
- **Tag:** [vv05]

- **Fact:** Số lượng lớp tường (Wall Line Count) được thiết lập bằng 2 và độ rộng đường in (Line Width) dao động từ 0.40–0.42 mm.
- **Source:** (v05 - Section: Độ dày lớp & tường)
- **Tag:** [vv05]

- **Fact:** Chế độ "Fill Gaps Between Walls" đặt ở mức "Everywhere" để đảm bảo không có khoảng hở giữa các bức tường của mô hình.
- **Source:** (v05 - Section: Độ dày lớp & tường)
- **Tag:** [vv05]

- **Fact:** Tốc độ di chuyển của đầu in (Travel Speed) được cấu hình ở mức cao là 200 mm/s.
- **Source:** (v05 - Section: Tốc độ & di chuyển)
- **Tag:** [vv05]

- **Fact:** Kiểm soát gia tốc (Acceleration Control) bao gồm gia tốc tường (Wall Acceleration) là 1500 mm/s² và gia tốc di chuyển (Travel Acceleration) là 3000 mm/s².
- **Source:** (v05 - Section: Tốc độ & di chuyển)
- **Tag:** [vv05]

- **Fact:** Hệ thống làm mát (Print Cooling) được kích hoạt 100% công suất bắt đầu từ lớp thứ 3 (layer 3).
- **Source:** (v05 - Section: Làm mát & chi tiết nhỏ)
- **Tag:** [vv05]

- **Fact:** Thời gian tối thiểu cho mỗi lớp (Minimum Layer Time) được đặt từ 10–12 giây để đảm bảo nhựa kịp đông đặc ở các chi tiết nhỏ.
- **Source:** (v05 - Section: Làm mát & chi tiết nhỏ)
- **Tag:** [vv05]

- **Fact:** Thông số rút sợi (Retraction) bao gồm khoảng cách rút (Retraction Distance) 0.6–0.8 mm và tốc độ rút (Retraction Speed) từ 35–45 mm/s.
- **Source:** (v05 - Section: Rút sợi & tránh va quệt)
- **Tag:** [vv05]

- **Fact:** Tính năng Z-hop khi rút sợi được kích hoạt với độ cao (Z Hop Height) là 0.3 mm để tránh va chạm với các phần đã in.
- **Source:** (v05 - Section: Rút sợi & tránh va quệt)
- **Tag:** [vv05]

- **Fact:** Để tăng độ bám bàn in cho chân đế, sử dụng Brim với độ rộng (Brim Width) từ 8–10 mm hoặc số đường Brim (Brim Line Count) từ 12–15 đường.
- **Source:** (v05 - Section: Bám bàn in)
- **Tag:** [vv05]

- **Fact:** Thư viện Pandas trong Python được sử dụng để tự động hóa việc gộp dữ liệu vật tư từ nhiều sheet Excel dựa trên các cột "Tên Vật tư" và "Mã Vật tư".
- **Source:** (v05 - Section: Conversation: Gộp vật tư theo tên)
- **Tag:** [vv05]

- **Fact:** Kỹ thuật sử dụng "Modifier" (khối lập phương) trong phần mềm cắt lớp (Slicer) cho phép tùy chỉnh mật độ lấp đầy (Infill Density) riêng biệt cho phần chân đế (khoảng 15%) trong khi phần còn lại của mô hình là 0%.
- **Source:** (v05 - Section: Đáy (phần chân đế))
- **Tag:** [vv05]
Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v05 liên quan đến IoT, Robotics, 3D Printing và AI:

**1. Thiết kế 3D (Tinkercad cho Robotics)**
- **Fact:** Trong Tinkercad, **Bundle group** là dạng nhóm "mềm" dùng để gom các hình khối nhằm mục đích tổ chức và di chuyển dễ dàng mà không làm thay đổi cấu trúc hình học hay thực hiện phép toán boolean.
- **Source:** [vv05] - Section: Phân biệt group Tinkercad (Bảng so sánh).
- **Tag:** [vv05]

- **Fact:** **Union group** trong Tinkercad là nhóm "cứng" thực hiện phép toán boolean (hợp nhất các khối Solid hoặc dùng khối Hole để trừ vật liệu), tạo ra một mesh thống nhất cần thiết trước khi xuất file (STL/OBJ) để in 3D.
- **Source:** [vv05] - Section: Phân biệt group Tinkercad (Bảng so sánh & Bước 3).
- **Tag:** [vv05]

**2. Kỹ thuật in 3D (Robotics/Hardware)**
- **Fact:** Thông số in nhựa PLA tối ưu trên máy Elegoo Neptune 4 cho các mô hình cơ khí (như Strandbeest) bao gồm: Nhiệt độ đầu phun 210-220°C, nhiệt độ bàn in 60°C, và độ điền đầy (infill) khoảng 15%.
- **Source:** [vv05] - Section: Tìm thông số in PLA (Bảng thông số in đề xuất).
- **Tag:** [vv05]

- **Fact:** Đối với các chi tiết in 3D nhỏ hoặc trục đứng của robot, việc giảm tốc độ in xuống khoảng 20mm/s và giảm chiều cao lớp (layer height) xuống 0.12mm giúp tăng độ chính xác và khả năng bám dính giữa các lớp nhựa.
- **Source:** [vv05] - Section: Tìm thông số in PLA (Bảng thông số & Tối ưu tốc độ).
- **Tag:** [vv05]

- **Fact:** Các mô hình cơ khí dạng "in liền" (print-in-place) yêu cầu xử lý hậu kỳ bằng cách bẻ nhẹ các khớp dính sau khi in và có thể sử dụng dầu bôi trơn để đảm bảo các bộ phận chuyển động trơn tru.
- **Source:** [vv05] - Section: Tìm thông số in PLA (Mẹo in và lưu ý theo tỷ lệ kích thước).
- **Tag:** [vv05]

- **Fact:** Khi in 3D các chi tiết chân robot hoặc mô hình có diện tích tiếp xúc nhỏ, việc sử dụng tính năng **Brim** và tăng nhiệt độ bàn in lên 60°C giúp ngăn chặn hiện tượng cong vênh (warping) hoặc bong khỏi bàn in.
- **Source:** [vv05] - Section: Tìm thông số in PLA (Độ bám và biến dạng).
- **Tag:** [vv05]

**3. Ứng dụng AI (AI in Healthcare/Education)**
- **Fact:** Các mô hình AI tạo hình ảnh (như DALL-E) có khả năng mô phỏng trực quan sự khác biệt giữa các trạng thái bệnh lý (ví dụ: viêm họng do virus vs vi khuẩn) để hỗ trợ giáo dục y khoa và chẩn đoán sơ bộ.
- **Source:** [vv05] - Section: Hình ảnh cổ họng trẻ (Phần Assistant & Tool).
- **Tag:** [vv05]

**4. Tự động hóa và Xử lý dữ liệu (Data Engineering)**
- **Fact:** Thư viện Pandas trong Python được sử dụng để tự động hóa việc gộp dữ liệu từ nhiều sheet Excel, làm sạch dữ liệu (dropna), và thực hiện các phép toán thống kê (sum, mode) để tổng hợp vật tư kỹ thuật.
- **Source:** [vv05] - Section: DỮ LIỆU RAW (Phần code Python).
- **Tag:** [vv05]
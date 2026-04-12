Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu về dự án Robotics (Strandbeest) và kỹ thuật in 3D:

- **Fact:** Thông số thiết lập cho profile **GEAR_STRONG** (dùng cho bánh răng) bao gồm: Infill 40% (Grid), Adhesion Brim 4 mm, Support Off, giữ nguyên độ dày lớp 0.2 mm và tốc độ in từ 20-60 mm/s.
- **Source:** [vv06] - Section: Assistant's first response on GEAR_STRONG.
- **Tag:** [vv06]

- **Fact:** Profile **BASE** dành cho các chi tiết khung (leg, end, siderod) sử dụng Infill 20% Grid, Adhesion Skirt 3 lines và không cần Support.
- **Source:** [vv06] - Section: Print Plan Table.
- **Tag:** [vv06]

- **Fact:** Chi tiết **crank** (trục khuỷu) yêu cầu profile **CRANK_SUPPORT** với thiết lập Support On (Everywhere), Interface dày 0.8 mm, Density 100%, Pattern Lines, khoảng cách Z 0.20 mm và Brim 6 mm.
- **Source:** [vv06] - Section: Print Plan Table.
- **Tag:** [vv06]

- **Fact:** Để xử lý vấn đề khớp nối bị chặt trên chi tiết chân (leg), có thể điều chỉnh Flow xuống 98% và thiết lập Initial Layer Horizontal Expansion ở mức -0.20 mm.
- **Source:** [vv06] - Section: Print Plan Table (Ghi chú).
- **Tag:** [vv06]

- **Fact:** Lưu lượng đùn nhựa trung bình (Average volumetric flow) để đảm bảo chất lượng in trên máy Neptune 4 với nhựa PLA được ước tính là Q_avg ≈ 3.5 mm³/s.
- **Source:** [vv06] - Section: Python script for estimation.
- **Tag:** [vv06]

- **Fact:** Khối lượng riêng tiêu chuẩn của nhựa PLA sử dụng trong tính toán vật liệu in là 1.24 g/cm³ (tương đương 0.00124 g/mm³).
- **Source:** [vv06] - Section: Python script for estimation.
- **Tag:** [vv06]

- **Fact:** Thời gian in 3D tỷ lệ thuận với lập phương của tỷ lệ scale; ví dụ khi scale mô hình xuống 80%, thời gian in có thể giảm khoảng 49%.
- **Source:** [vv06] - Section: Scaling explanation.
- **Tag:** [vv06]

- **Fact:** Trong cấu trúc in của chi tiết chân Strandbeest, các đường vách (Inner và Outer Walls) có thể chiếm tới 79% tổng thời gian in.
- **Source:** [vv06] - Section: Analysis of print time distribution.
- **Tag:** [vv06]

- **Fact:** Khi scale mô hình xuống dưới 85%, nên giảm độ dày lớp (Layer Height) xuống 0.16 mm để đảm bảo độ chính xác của các bánh răng và khớp nối nhỏ.
- **Source:** [vv06] - Section: Scaling recommendations.
- **Tag:** [vv06]

- **Fact:** Việc giảm thông số "Minimum Layer Time" từ 10 giây xuống 5 giây giúp tối ưu hóa thời gian in cho các lớp có diện tích nhỏ mà vẫn đảm bảo khả năng làm mát.
- **Source:** [vv06] - Section: Optimization Package A.
- **Tag:** [vv06]
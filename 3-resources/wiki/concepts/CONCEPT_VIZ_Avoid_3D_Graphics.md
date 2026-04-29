---
title: "Tránh sử dụng đồ họa 3D (Avoid 3D Graphics)"
source_id: SOURCE_VIZ_10_Visualization_Tips
category: VIZ
status: verified
created: "2026-04-29"
---

# Tránh sử dụng đồ họa 3D (Avoid 3D Graphics)

Trong trực quan hóa dữ liệu 2D (trên màn hình hoặc giấy), việc sử dụng các hiệu ứng 3D thường gây hại nhiều hơn lợi.

## 核心 (Core Principle)
Hiệu ứng 3D làm sai lệch (distort) dữ liệu và khiến người xem khó diễn giải chính xác các giá trị.
- Phối cảnh (perspective) trong đồ họa 3D thay đổi kích thước tương đối của các phần tử dựa trên vị trí của chúng, dẫn đến việc so sánh sai lệch.
- 3D thường tạo ra "mực" dư thừa (chartjunk) không đóng góp vào việc hiểu dữ liệu.

## [X]. Ví dụ đối chiếu (Rule 17: Double Examples)

### 1. Ví dụ từ sách (Original)
Theo tài liệu "10 Visualization Tips" (Tip 6), chiều sâu giả lập trong biểu đồ 3D làm cho việc xác định điểm dừng của một cột hoặc kích thước của một miếng bánh (pie slice) trở nên mơ hồ, gây khó khăn cho việc đọc trị số chính xác.

### 2. Ứng dụng sư phạm (Pedagogical Application)
Trong bài thực hành thiết kế Dashboard, nếu một giáo viên thấy học sinh sử dụng biểu đồ tròn 3D (3D Pie Chart), hãy giải thích rằng miếng bánh ở phía trước trông sẽ to hơn miếng bánh ở phía sau dù giá trị thực tế của chúng bằng nhau. Giải pháp là chuyển về biểu đồ tròn 2D hoặc biểu đồ cột (Bar chart) để đảm bảo tính trung thực.

---
Nguồn: [[SOURCE_VIZ_10_Visualization_Tips]] (Xác nhận Rule 14 từ: `VIZ_10_Visualization_Tips`)

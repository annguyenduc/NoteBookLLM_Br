---
ID: CONCEPT_VIZ_Dashboard_Design_Best_Practices
Type: Concept
Topic: Data Visualization
Status: verified
Created: 2026-04-29
Tags: [Dashboard, Design, ACES, Framework, Best_Practices]
---

# Nguyên tắc Thiết kế Dashboard (Dashboard Design Best Practices)

> Dashboard là một màn hình hiển thị thông tin động nhằm hỗ trợ việc ra quyết định nhanh chóng và chính xác. Một Dashboard tốt không chỉ đẹp mà còn phải giải quyết được bài toán kinh doanh cụ thể.

## 1. Khung ACES (Các tiêu chuẩn vàng)
Để một Dashboard thực sự hiệu quả, nó cần đạt được 4 tiêu chí ACES:
- **Chính xác (Accurate):** Dữ liệu phải tin cậy 100%. Nếu người xem nghi ngờ tính chính xác, họ sẽ không dùng nó. Cần hiển thị thời gian cập nhật lần cuối và định nghĩa rõ ràng các chỉ số (metrics).
- **Rõ ràng (Clear):** Tốc độ thấu cảm (Speed to insight) là ưu tiên số 1. Sử dụng phông chữ không chân (sans-serif), màu sắc có độ tương phản tốt nhưng không gây xao nhãng.
- **Trao quyền (Empowering):** Dashboard phải thúc đẩy hành động. Một bài kiểm tra đơn giản: "Nếu con số này tăng gấp đôi hoặc về 0, bạn có thay đổi hành động của mình không?"
- **Súc tích (Succinct):** Chỉ hiển thị những gì thực sự cần thiết. Tránh việc cuộn trang quá nhiều (giữ thông tin quan trọng "above the fold" - trên nếp gấp màn hình).

## 2. Quy trình thiết kế 4 Bước
1. **Xác định (Define):** Xác định các bên liên quan (Người thiết kế, Khán giả, Người phụ trách chính). Hiểu rõ mục tiêu cụ thể và các quyết định cần được hỗ trợ.
2. **Tạo mẫu (Prototype):** Chọn biểu đồ phù hợp (So sánh, Thành phần, Phân phối, Mối quan hệ). Phác thảo bố cục (layout) trước khi bắt tay vào code/công cụ.
3. **Xây dựng (Build):** Kết nối nguồn dữ liệu, viết truy vấn, chuyển đổi dữ liệu thành các thành phần trực quan.
4. **Triển khai (Deploy):** Chia sẻ Dashboard kèm theo hướng dẫn sử dụng. Thiết lập cơ chế bảo trì và nhận phản hồi để cải tiến liên tục.

## 3. Lựa chọn Trực quan hóa (Visualization Selection)
Dựa trên mục tiêu của dữ liệu:
- **So sánh (Comparison):** Bar chart, Line chart (theo thời gian).
- **Thành phần (Composition):** Stacked bar chart, Pie chart (chỉ khi có rất ít danh mục).
- **Mối quan hệ (Relationship):** Scatter plot, Bubble chart.
- **Phân phối (Distribution):** Histogram, Box plot.

## 4. Những lỗi cần tránh (Common Pitfalls)
- **Biểu đồ 3D:** Khó so sánh kích thước và thể tích một cách chính xác.
- **Quá nhiều danh mục:** Tránh hiển thị quá 5-7 danh mục trong một biểu đồ (nên nhóm vào mục "Other").
- **Trục Y sai:** Biểu đồ cột (Bar chart) **bắt buộc** phải bắt đầu từ 0 để tránh gây hiểu lầm về tỷ lệ.
- **Mất cân đối (Alignment):** Các biểu đồ không thẳng hàng sẽ gây xao nhãng và tạo cảm giác không chuyên nghiệp.

## 5. Bố cục tối ưu
Tuân theo thói quen đọc hình chữ Z (Z-Pattern):
- **Góc trên bên trái:** Thông tin quan trọng nhất, các chỉ số chính (KPIs).
- **Góc dưới bên phải:** Chi tiết bổ sung hoặc dữ liệu ít quan trọng hơn.
- **Nhóm dữ liệu:** Đặt các biểu đồ có liên quan sát cạnh nhau để dễ so sánh.

## 6. Ví dụ đối chiếu (Rule 17: Double Examples)

### 6.1. Ví dụ từ sách (Original)
*Tình huống: Áp dụng tính Súc tích (Succinct) cho Dashboard Bán hàng.*
- **Cách giải quyết:** Một Dashboard bán hàng nhồi nhét 15 biểu đồ để "khoe" dữ liệu. Thay vì để 15 biểu đồ, designer gom các chỉ số phụ vào một tab báo cáo chi tiết riêng (ẩn đi), và chỉ giữ lại 3 chỉ số quan trọng nhất (Doanh thu, Lợi nhuận, Số khách hàng mới) trên màn hình chính để Giám đốc có thể nắm bắt chỉ trong 5 giây đầu.

### 6.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Lựa chọn biểu đồ (Visualization Selection) cho bảng điểm của lớp.*
- **Cách giải quyết:** Giáo viên muốn hiển thị tỷ lệ học sinh đạt điểm Giỏi, Khá, Trung bình, Yếu của 8 lớp khối 10. Nếu dùng Pie chart (Biểu đồ tròn), người xem sẽ rất khó phân biệt các lát cắt có kích thước gần bằng nhau. Chuyển sang Bar chart (Biểu đồ cột) giúp giáo viên dễ dàng so sánh độ dài của các thanh, từ đó nhận diện ngay lớp nào đang có tỷ lệ học sinh Yếu cao nhất để can thiệp kịp thời.

---
Nguồn: [[SOURCE_VIZ_How_to_Design_a_Dashboard]] (Xác nhận Rule 14 từ: `VIZ_How_to_Design_a_Dashboard`)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

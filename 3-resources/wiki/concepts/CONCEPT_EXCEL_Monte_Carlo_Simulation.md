---
file_id: CONCEPT_EXCEL_Monte_Carlo_Simulation
title: Mô phỏng Monte Carlo trong Excel
category: CONCEPT
domain: Excel
status: verified
---

# Monte Carlo Simulation (Excel)

Mô phỏng Monte Carlo là một kỹ thuật toán học sử dụng việc lấy mẫu ngẫu nhiên lặp đi lặp lại để mô hình hóa xác suất của các kết quả khác nhau trong một quá trình không thể dự đoán dễ dàng.

## 1. Cách thực hiện trong Excel
1.  **Xác định biến ngẫu nhiên:** Ví dụ: Doanh thu, Chi phí biến đổi (sử dụng các hàm như `RAND()` hoặc `NORM.INV()`).
2.  **Thiết lập mô hình:** Viết công thức tính kết quả (ví dụ: Lợi nhuận) dựa trên các biến ngẫu nhiên.
3.  **Lặp lại (Iteration):** Sử dụng **Data Tables** để chạy mô hình hàng nghìn lần với các giá trị ngẫu nhiên khác nhau.
4.  **Phân tích kết quả:** Sử dụng Histogram hoặc Descriptive Statistics để xem phân phối kết quả (Xác suất đạt mục tiêu là bao nhiêu %).

## 2. Ví dụ đối chiếu (Rule 17: Double Examples)

### 2.1. Ví dụ từ sách (Original)
*Tình huống: Quản trị rủi ro và ra quyết định sản phẩm tại General Motors (GM) / Sears.*
- **Đầu vào:** Biến ngẫu nhiên là lợi nhuận, chi phí, hoặc nhu cầu đặt hàng (vd: bao nhiêu quần Dockers cần nhập).
- **Cách giải quyết:** Các công ty lớn như GM hoặc Sears sử dụng Monte Carlo để chạy hàng nghìn kịch bản giả lập các yếu tố thị trường biến động (dùng hàm ngẫu nhiên phân phối chuẩn/đều). Kết quả cho ra rủi ro lỗ vốn, giúp CEO quyết định sản phẩm nào nên được ra mắt hoặc số lượng tối ưu để nhập kho.

### 2.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Dự báo xác suất hoàn thành chương trình học dựa trên thời gian thực hành biến động.*
- **Đầu vào:** Một khóa học lập trình Robot có 5 học phần. Thời gian hoàn thành mỗi học phần của học sinh giao động theo phân phối chuẩn (vd: trung bình 4 tiết, độ lệch chuẩn 1 tiết).
- **Cách giải quyết:** Giáo viên thiết lập mô hình tính tổng thời gian khóa học trong Excel. Sử dụng Data Table để chạy mô phỏng 5000 lần với các thời gian ngẫu nhiên. Dựa trên phân phối kết quả (Histogram), giáo viên có thể tự tin kết luận "Có 90% khả năng toàn bộ lớp sẽ hoàn thành khóa học trong giới hạn 22 tiết", từ đó thiết kế giáo án phù hợp rủi ro.

---
 Nguồn: [[SOURCE_TOOL_Excel_Data_Analysis]] — Chapter 73
[AUDITOR] Rule 14: Đã xác nhận quy trình 4 bước mô phỏng. Ví dụ ứng dụng thực tế trong quản trị rủi ro.

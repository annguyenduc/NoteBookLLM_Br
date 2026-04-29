---
file_id: CONCEPT_EXCEL_Data_Modeling_PowerPivot
title: Mô hình hóa dữ liệu với PowerPivot và Data Model
category: CONCEPT
domain: Excel
status: verified
---

# ️ Excel Data Modeling & PowerPivot

Excel không chỉ là bảng tính phẳng; với Data Model, nó trở thành một cơ sở dữ liệu quan hệ thu nhỏ (Self-service BI).

## 1. Data Model là gì?
- Là một tập hợp các bảng dữ liệu được kết nối với nhau qua các mối quan hệ (Relationships).
- Cho phép phân tích dữ liệu từ nhiều nguồn mà không cần dùng hàm `VLOOKUP` (giúp file nhẹ hơn và tránh lỗi).

## 2. PowerPivot
- Là công cụ tích hợp để quản lý Data Model.
- **Dung lượng lớn:** Xử lý hàng triệu dòng dữ liệu (vượt qua giới hạn 1,048,576 dòng của sheet thông thường).
- **DAX (Data Analysis Expressions):** Ngôn ngữ công thức mạnh mẽ hơn Excel Formula để tính toán các Measure (độ đo) phức tạp.

## Ứng dụng
- Phân tích doanh thu từ bảng "Sales" kết hợp với thông tin từ bảng "Products" và "Customers" thông qua Relationship.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Tổng hợp doanh số theo Bang (State) từ 2 bảng dữ liệu riêng biệt.*
- **Đầu vào:** Bảng `Reps` (gồm Salesperson ID và State) và bảng `Sales` (gồm Salesperson ID và Unit Sales). Dữ liệu lên đến hàng trăm nghìn dòng.
- **Cách giải quyết:** Thay vì dùng hàm VLOOKUP để kéo tên Bang vào bảng Sales (làm chậm file nghiêm trọng), sử dụng chức năng *Add this data to the Data Model*. Tạo một Relationship (1-nhiều) giữa cột Salesperson ID của 2 bảng, sau đó có thể dùng PivotTable để thống kê trực tiếp Unit Sales theo State.

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Báo cáo kết quả học tập đa môn của học sinh toàn trường.*
- **Đầu vào:** Bảng `Học_Sinh` (Mã HS, Họ tên, Lớp) và 3 bảng điểm riêng biệt `Toán`, `Văn`, `Anh` (đều có cột Mã HS và Điểm).
- **Cách giải quyết:** Để theo dõi tiến độ, giáo viên không cần tạo thêm các cột VLOOKUP khổng lồ nối 3 bảng điểm vào bảng Học_Sinh. Bằng cách đưa cả 4 bảng vào PowerPivot Data Model và tạo Relationship qua `Mã HS`, giáo viên có thể tạo ngay PivotTable báo cáo điểm trung bình các môn theo từng Lớp hoặc từng Học Sinh, giữ cho file Excel nhẹ và không bị lag.

---
 Nguồn: [[SOURCE_TOOL_Excel_Data_Analysis]] — Chapter 44 & 45
[AUDITOR] Rule 14: Nguồn được xác nhận từ [[SOURCE_TOOL_Excel_Data_Analysis]], định nghĩa về Data Model và PowerPivot.

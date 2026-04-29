---
file_id: CONCEPT_SQL_Advanced_Reporting
title: Báo cáo nâng cao (ROLLUP, CUBE & Bucketing)
category: CONCEPT
domain: SQL
status: verified
---

# SQL Advanced Reporting

SQL hiện đại cung cấp các toán tử mạnh mẽ để tạo ra các báo cáo tổng hợp đa chiều tương tự như Pivot Table trong Excel.

## 1. ROLLUP
- **Nhiệm vụ:** Tính toán tổng phụ (subtotals) theo một trật tự phân cấp.
- **Ví dụ:** `GROUP BY ROLLUP(Year, Month, Day)` sẽ tạo ra tổng cho từng ngày, từng tháng, từng năm và tổng cuối cùng (Grand Total).

## 2. CUBE
- **Nhiệm vụ:** Tính toán tổng cho tất cả các tổ hợp có thể có của các cột được liệt kê.
- **Ứng dụng:** Thích hợp khi muốn xem dữ liệu từ nhiều góc độ không phân cấp (ví dụ: theo khu vực và theo loại sản phẩm).

## 3. Bucketing & Histograms
- **Bucketing:** Chia dữ liệu liên tục (ví dụ: lương) thành các khoảng (buckets) cố định bằng `CASE` hoặc `WIDTH_BUCKET`.
- **Vertical Histograms:** Sử dụng SQL để vẽ biểu đồ tần suất trực tiếp bằng ký tự (như `*` hoặc `|`).

## 4. Subtotal Detection
Hàm `GROUPING()` giúp xác định xem một hàng trong kết quả là dữ liệu chi tiết hay là hàng tổng phụ do ROLLUP/CUBE tạo ra.

## 5. Ví dụ đối chiếu (Rule 17: Double Examples)

### 5.1. Ví dụ từ sách (Original)
*Tình huống: Tính toán tổng phụ (Subtotals) với ROLLUP cho báo cáo doanh số.*
- **Cách giải quyết:** Khi phòng ban kinh doanh cần xem báo cáo tổng kết cuối năm, thay vì chỉ dùng `GROUP BY` để ra từng dòng rời rạc, ta bọc các trường vào hàm `ROLLUP`. Kết quả trả về sẽ tự động cộng dồn doanh số từ cấp nhỏ nhất (tháng) lên cấp lớn hơn (năm) và cuối cùng là tổng toàn bộ dữ liệu.
```sql
SELECT 
    YEAR(order_date) as sales_year, 
    MONTH(order_date) as sales_month, 
    SUM(sales_amount) as total_sales
FROM sales
GROUP BY ROLLUP(YEAR(order_date), MONTH(order_date));
```

### 5.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Lập ma trận dữ liệu (Cross-tabulation) với CUBE để phân tích điểm trung bình học sinh.*
- **Cách giải quyết:** Giáo viên cần lập báo cáo phân tích điểm môn Toán để biết xem học sinh giới tính nào, ở khối học nào đang có thành tích tốt nhất. Sử dụng hàm `CUBE(Khoi_Hoc, Gioi_Tinh)` sẽ tạo ra báo cáo "xoay mọi góc độ": Trung bình theo Khối, Trung bình theo Giới tính, và Trung bình kết hợp cả hai.
```sql
SELECT 
    Khoi_Hoc, 
    Gioi_Tinh, 
    AVG(Diem_Toan) as Diem_Trung_Binh
FROM bang_diem
GROUP BY CUBE(Khoi_Hoc, Gioi_Tinh);
```

---
 Nguồn: [[SOURCE_TOOL_SQL_Cookbook]] — Chapter 12 "Reporting and Reshaping"
[AUDITOR] Rule 14: Đã xác nhận các toán tử siêu gộp (super-aggregate) ROLLUP và CUBE.

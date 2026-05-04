---
file_id: CONCEPT_SQL_Window_Functions_Advanced
title: Hàm cửa sổ nâng cao (Advanced Window Functions)
category: CONCEPT
domain: [[ENTITY_SQL|SQL]]
status: verified
---

# [[CONCEPT_SQL_Window_Functions|SQL Window Functions]]

Window functions cho phép thực hiện các phép tính trên một tập hợp các hàng liên quan đến hàng hiện tại mà không cần gộp (collapse) các hàng đó lại như `GROUP BY`.

## 1. Cấu trúc cơ bản
```sql
FUNCTION(field) OVER (PARTITION BY group_field ORDER BY sort_field)
```

## 2. Các hàm phân tích quan trọng
- **`LAG(field, n)`:** Lấy giá trị của cột ở `n` hàng phía trước. Cực kỳ hữu ích để tính mức tăng trưởng (growth) hoặc điền dữ liệu thiếu (Fill forward).
- **`LEAD(field, n)`:** Lấy giá trị của cột ở `n` hàng phía sau.
- **`NTILE(n)`:** Chia tập dữ liệu thành `n` phần bằng nhau (quartiles, deciles, percentiles). Dùng để phân nhóm khách hàng theo chi tiêu hoặc hiệu suất.
- **`RANK()` / `DENSE_RANK()`:** Xếp hạng các bản ghi.

## 3. Ứng dụng trong phân tích
- **Tính toán lũy kế (Running Total):** `SUM(sales) OVER (ORDER BY date)`.
- **So sánh cùng kỳ (Period-over-period):** Sử dụng `LAG` để lấy doanh số tháng trước và so sánh với tháng này.
- **Xử lý dữ liệu thưa:** Dùng `LAG` để điền giá trị gần nhất vào các ô bị NULL.

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Sử dụng LAG để tính toán so sánh cùng kỳ (MoM Growth).*
- **Cách giải quyết:** Báo cáo tăng trưởng doanh số (revenue) giữa tháng này so với tháng ngay trước đó. Hàm `LAG(revenue, 1)` sẽ trích xuất doanh thu của dòng kề trước (prev_month_revenue). Nhờ đó, ta lấy `revenue` hiện tại trừ đi sẽ có mức tăng trưởng.
```sql
SELECT 
    sales_month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY sales_month) AS prev_month_revenue,
    revenue - LAG(revenue, 1) OVER (ORDER BY sales_month) AS revenue_diff
FROM monthly_sales;
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Sử dụng NTILE để phân nhóm thành tích sinh viên (Tạo Quartiles).*
- **Cách giải quyết:** Nhà trường có hàng ngàn sinh viên, muốn chia thành 4 nhóm (Quartiles) dựa trên tổng điểm để xét trao học bổng cho nhóm Top 25% đầu tiên. Hàm `NTILE(4)` chia đều lượng sinh viên thành 4 "rổ" điểm. Nhóm điểm cao nhất sẽ vào rổ 1, giảm dần đến rổ 4.
```sql
-- Chia sinh viên thành 4 nhóm để dễ dàng xét học bổng
SELECT 
    ma_sinh_vien,
    tong_diem,
    NTILE(4) OVER (ORDER BY tong_diem DESC) as spending_quartile
FROM danh_sach_diem_tong_ket;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_for_Data_Analysis]] — Section "Window Functions"
[AUDITOR] Rule 14: Đã xác nhận các hàm NTILE, LAG, LEAD là trọng tâm của chương Advanced SQL. Ví dụ được minh họa bám sát tính ứng dụng trong Data Analysis.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

---
file_id: CONCEPT_SQL_Data_Preparation_Workflow
title: Quy trình chuẩn bị dữ liệu phân tích với [[ENTITY_SQL|SQL]]
category: CONCEPT
domain: SQL
status: verified
---

# SQL Data Preparation Workflow

Chuẩn bị dữ liệu chiếm 50-80% thời gian của một Data Analyst. Quy trình này gồm 5 giai đoạn lặp lại:

## 1. Explore (Khám phá)
- Hiểu cấu trúc bảng, quan hệ giữa các bảng.
- Đọc Data Dictionary (nếu có).

## 2. Profile (Phác họa chân dung)
- Kiểm tra phân phối giá trị bằng Histogram và Frequencies.
- Xác định dữ liệu thưa (Sparse data) và các giá trị null.
- Kỹ thuật: `COUNT(*)`, `GROUP BY`, `NTILE()`, `LOG()`.

## 3. Clean (Làm sạch)
- Xử lý giá trị Null: `COALESCE`, `NULLIF`, `CASE WHEN`.
- Sửa lỗi logic hoặc dữ liệu bị thiếu (Imputation).
- Chuyển đổi kiểu dữ liệu (Casting).

## 4. Shape (Định hình)
- Quyết định độ hạt (Granularity) của dữ liệu.
- Làm phẳng (Flattening) dữ liệu qua Aggregation.
- Chuyển đổi cấu trúc: Pivoting (hàng -> cột) và Unpivoting (cột -> hàng).

## 5. Analyze (Phân tích)
- Trích xuất insight, xu hướng từ tập dữ liệu đã sạch và được định hình đúng.

## 6. Ví dụ đối chiếu (Rule 17: Double Examples)

### 6.1. Ví dụ từ sách (Original)
*Tình huống: Khám phá và Làm sạch (Profile & Clean) để thay thế giá trị Null.*
- **Cách giải quyết:** Khi tính toán tổng doanh thu, một số đơn hàng không có chiết khấu (lưu dưới dạng `NULL`). Nếu dùng phép trừ trực tiếp `price - NULL`, kết quả sẽ luôn ra `NULL`. Giải pháp là dùng `COALESCE` để "làm sạch", đưa các giá trị `NULL` về 0.
```sql
-- Sử dụng COALESCE để đảm bảo không có giá trị NULL
SELECT 
    order_id,
    price,
    COALESCE(discount, 0) AS clean_discount,
    price - COALESCE(discount, 0) AS final_price
FROM orders;
```

### 6.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Làm sạch dữ liệu điểm khuyết (Imputation) trước khi tính trung bình.*
- **Cách giải quyết:** Cuối kỳ, hệ thống cần tính điểm trung bình cho học sinh. Một số em vắng thi bị để trống điểm (NULL). Giáo viên sử dụng `COALESCE` trong bước "Clean" để gán giá trị mặc định là 0 cho bài thi bị bỏ trống, đảm bảo hàm `AVG` tính toán chính xác tổng chia cho số đầu điểm.
```sql
-- Điền 0 vào các bài thi bị vắng (NULL) trước khi tính trung bình
SELECT 
    Hoc_Sinh,
    AVG(COALESCE(Diem_Toan, 0)) AS TB_Toan,
    AVG(COALESCE(Diem_Van, 0)) AS TB_Van
FROM bang_diem_tong_ket
GROUP BY Hoc_Sinh;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_for_Data_Analysis]] — Chapter 2 "Preparing Data for Analysis"
[AUDITOR] Rule 14: Quy trình 5 bước được trích dẫn trực tiếp từ sơ đồ workflow của tác giả.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

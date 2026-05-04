---
file_id: CONCEPT_SQL_Data_Shaping_Techniques
title: Kỹ thuật định hình dữ liệu (Pivoting & Unpivoting)
category: CONCEPT
domain: [[ENTITY_SQL|SQL]]
status: verified
---

# Data Shaping: Pivoting & Unpivoting

Định hình dữ liệu là việc thay đổi cách biểu diễn dữ liệu giữa hàng và cột để phục vụ các mục đích báo cáo (BI) hoặc mô hình hóa (ML).

## 1. Pivoting (Hàng -> Cột)
- **Mục tiêu:** Tổng hợp dữ liệu thành dạng bảng chéo (Cross-tab).
- **Cách làm:** Sử dụng `CASE WHEN` kết hợp với các hàm gộp (`SUM`, `COUNT`).
- **Ví dụ:** Chuyển danh sách các giao dịch sản phẩm thành bảng có mỗi cột là một loại sản phẩm (Shirts, Shoes, Hats).

## 2. Unpivoting (Cột -> Hàng)
- **Mục tiêu:** Đưa dữ liệu về dạng "Tidy Data" (mỗi biến là một cột, mỗi quan sát là một hàng).
- **Cách làm:**
    - Sử dụng `UNION ALL` để "chồng" các cột lên nhau.
    - Sử dụng hàm `unnest(array[...])` (Postgres) để giải nén mảng thành các hàng.
- **Ví dụ:** Chuyển bảng dân số có các cột `year_1980`, `year_1990` thành bảng có cột `Year` và `Population`.

## 3. Khi nào cần Shaping?
- **BI/Visualization:** Thường cần dữ liệu đã được Pivot để vẽ biểu đồ so sánh.
- **Machine Learning:** Luôn cần dữ liệu ở dạng Tidy (Unpivoted) để làm đầu vào cho mô hình.

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Pivoting bằng CASE WHEN (Từ Hàng sang Cột).*
- **Cách giải quyết:** Dữ liệu bán hàng đang ở dạng dọc với 1 cột `category` (Shirts, Shoes). Data Analyst muốn chuyển thành 2 cột riêng biệt để so sánh trực quan. Bằng cách kết hợp `SUM` và `CASE WHEN`, họ đã biến mỗi loại sản phẩm thành một cột (Pivoting).
```sql
SELECT 
    year,
    SUM(CASE WHEN category = 'Shirts' THEN revenue ELSE 0 END) AS shirts_rev,
    SUM(CASE WHEN category = 'Shoes' THEN revenue ELSE 0 END) AS shoes_rev
FROM sales
GROUP BY year;
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Unpivoting bảng điểm (Từ Cột sang Hàng) để chuẩn bị dữ liệu thi trắc nghiệm AI.*
- **Cách giải quyết:** Hệ thống chấm điểm cũ xuất ra file [[ENTITY_EXCEL|Excel]] dạng Wide (Cột Toán, Cột Văn, Cột Anh). Nền tảng học tập AI thế hệ mới lại yêu cầu dữ liệu dạng Tidy/Long (Một cột "Môn_Hoc", một cột "Diem_So"). Kỹ sư dữ liệu giáo dục sử dụng `UNION ALL` để "Unpivot" 3 cột này thành 1 hàng duy nhất cho mỗi môn.
```sql
SELECT Hoc_Sinh, 'Toan' AS Mon_Hoc, Diem_Toan AS Diem_So FROM Bang_Diem_Cu
UNION ALL
SELECT Hoc_Sinh, 'Van' AS Mon_Hoc, Diem_Van AS Diem_So FROM Bang_Diem_Cu
UNION ALL
SELECT Hoc_Sinh, 'Anh' AS Mon_Hoc, Diem_Anh AS Diem_So FROM Bang_Diem_Cu;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_for_Data_Analysis]] — Section "Preparing: Shaping Data"
[AUDITOR] Rule 14: Đã xác nhận các kỹ thuật CASE-based pivoting và UNION-based unpivoting.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

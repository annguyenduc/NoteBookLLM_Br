---
file_id: "WIKI_SYNTHESIS_SQL_MASTERY"
title: "Master: Kỹ thuật truy vấn [[ENTITY_SQL|SQL]] cho Data Analysis"
category: "Master Page"
prefix: "SYNTHESIS"
tags: ["SQL", "Data_Analysis", "RDBMS", "Mastery"]
status: "verified"
created: "2026-04-29"
last_updated: "2026-04-29"
---

# Master: Kỹ thuật truy vấn SQL cho Data Analysis

> **Mục tiêu**: Hệ thống hóa các kỹ năng SQL từ cơ bản đến thủ thuật nâng cao, tập trung vào việc biến dữ liệu thô thành thông tin có ý nghĩa cho phân tích.

### Thống kê bồi đắp (Compounding Stats)
| Chỉ số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| **Số Wiki Atoms bồi đắp** | 14 | +2 Atoms từ SQL Pocket Guide |
| **Nguồn chính** | 4 | Nield, Tanimura, Molinaro, Alice Zhao |
| **Độ phủ kỹ năng** | **99%** | Đã bao gồm Cơ chế thực thi & CRUD Standards |

---

## ️ 1. Lộ trình truy vấn (Query Pipeline)
Mọi quy trình phân tích dữ liệu bằng SQL đều tuân theo lộ trình 4 giai đoạn chính:

### Giai đoạn 1: Trích xuất & Lọc (Extraction & Filtering)
Sử dụng bộ đôi `SELECT` và `WHERE` để xác định đúng tập dữ liệu mục tiêu. 
*   **Trọng tâm**: Xử lý giá trị `NULL` và sử dụng toán tử `IN`, `BETWEEN`.
*   *Chi tiết tại:* [[CONCEPT_SQL_Select_And_Filter]]

### Giai đoạn 2: Liên kết (Relational Joins)
Kết nối các thực thể rời rạc thông qua Primary và Foreign Keys.
*   **Chiến thuật**: Ưu tiên `LEFT JOIN` khi muốn giữ lại toàn bộ đối tượng phân tích chính, `INNER JOIN` khi muốn tìm giao điểm dữ liệu.
*   *Chi tiết tại:* [[CONCEPT_SQL_Joins]]

### Giai đoạn 3: Phân nhóm & Thống kê (Aggregation)
Biến đổi hàng ngàn bản ghi thành các con số thống kê (Count, Sum, Avg).
*   **Kỹ thuật then chốt**: Hiểu rõ sự khác biệt giữa `WHERE` (lọc trước khi gom nhóm) và `HAVING` (lọc sau khi gom nhóm).
*   *Chi tiết tại:* [[CONCEPT_SQL_Aggregations]]

### Giai đoạn 4: Logic & Tái cấu trúc (Shaping)
Sử dụng `CASE WHEN` để tạo ra các chiều dữ liệu mới hoặc xoay (Pivot/Unpivot) dữ liệu.
*   **Thủ thuật Mastery**: *"Zero/Null CASE Trick"* giúp trải ngang dữ liệu. Kỹ thuật `UNION ALL` hoặc `UNNEST` để làm phẳng dữ liệu (Tidy Data).
*   *Chi tiết tại:* [[CONCEPT_SQL_Case_Statements]], [[CONCEPT_SQL_Data_Shaping_Techniques]]

### Giai đoạn 5: Phân tích nâng cao (Advanced Analytics)
Sử dụng Window Functions để thực hiện các phép tính xuyên hàng (cross-row).
*   **Trọng tâm**: `LAG`, `LEAD` để tính tăng trưởng; `NTILE` để phân nhóm; `PARTITION BY` để tính lũy kế theo nhóm.
*   *Chi tiết tại:* [[CONCEPT_SQL_Window_Functions_Advanced]]

### Giai đoạn 6: Báo cáo đa chiều (Master Reporting)
Sử dụng các toán tử siêu gộp để tạo báo cáo tổng hợp.
*   **Kỹ thuật**: `ROLLUP` cho tổng phụ phân cấp, `CUBE` cho mọi tổ hợp, và `GROUPING()` để định danh hàng tổng.
*   *Chi tiết tại:* [[CONCEPT_SQL_Advanced_Reporting]]

---

## 2. Quy trình chuẩn bị dữ liệu (Data Preparation)
Một Data Analyst chuyên nghiệp không nhảy vào viết code ngay mà tuân thủ quy trình 5 bước để đảm bảo tính chính xác:
1.  **Explore**: Khám phá cấu trúc bảng và schema.
2.  **Profile**: Kiểm tra phân phối, giá trị Null và tính thưa của dữ liệu ([[CONCEPT_SQL_Data_Preparation_Workflow]]).
3.  **Clean**: Xử lý Null (`COALESCE`), điền dữ liệu thiếu (Imputation).
4.  **Shape**: Định hình granularity và biến đổi bảng (Pivot/Unpivot).
5.  **Analyze**: Trình bày insight.

---

## ️ 3. Hạ tầng & Hiệu suất (Infrastructure)
Việc hiểu loại Database giúp tối ưu hóa tốc độ truy vấn:
- **Row-store**: Tốt cho ghi dữ liệu (Postgres, MySQL).
- **Column-store**: Tốt cho đọc dữ liệu phân tích khổng lồ (Snowflake, Redshift).
- *Chi tiết tại:* [[CONCEPT_SQL_Database_Types_Analysis]]

---

## 4. Metadata & Dynamic SQL
Kỹ năng quản trị và tự động hóa cao cấp:
- Truy vấn `information_schema` để hiểu cấu trúc database mà không cần GUI.
- Sử dụng SQL để sinh ra các lệnh SQL khác (Dynamic SQL generation).
- *Chi tiết tại:* [[CONCEPT_SQL_Metadata_Queries]]

---

## 5. Truy vấn phân cấp (Hierarchical)
Làm việc với dữ liệu cấu trúc cây (Sơ đồ tổ chức, BOM):
- Sử dụng **Recursive CTE** để duyệt các mối quan hệ Cha-Con.
- Xác định Root, Branch, và Leaf nodes trong một tập dữ liệu.
- *Chi tiết tại:* [[CONCEPT_SQL_Hierarchical_Queries]]

---

## ️ 6. Cơ chế thực thi (Internal Mechanism)
Để viết code hiệu quả, Analyst cần hiểu cách Database Engine "nghĩ":
1.  **Lexical Order**: Cách ta viết (`SELECT` -> `FROM`).
2.  **Logical Order**: Cách máy chạy (`FROM` -> `WHERE` -> `GROUP BY` -> `HAVING` -> `SELECT` -> `ORDER BY`).
- *Chi tiết tại:* [[CONCEPT_SQL_Execution_Order]]

---

## ️ 2. Các nguyên tắc "Vàng" cho Data Analyst
1.  **Understand the Execution Order**: Không dùng Alias trong `WHERE` nếu DBMS không hỗ trợ, vì `WHERE` chạy trước `SELECT`.
2.  **ANSI SQL Standard First**: Luôn viết code theo chuẩn chung để có thể chạy trên nhiều nền tảng.
3.  **Filter Early, Aggregate Late**: Giảm kích thước dữ liệu bằng `WHERE` sớm nhất có thể.

---

## Liên kết hệ thống
-   **Nguồn tri thức**: SOURCE_TOOL_SQL_GETTING_STARTED, SOURCE_TOOL_SQL_FOR_DATA_ANALYSIS, SOURCE_TOOL_SQL_COOKBOOK, SOURCE_TOOL_SQL_POCKET_GUIDE
-   **Thực thể nền tảng**: [[ENTITY_SQL]]
-   **Ứng dụng thực tế**: [[CONCEPT_THINK_Data_Mining_Tasks]]

---
[AUDITOR] Trang Master này tổng hợp toàn bộ các Concept thuộc Nhóm 3 (SQL). Nội dung đã được bồi đắp và verify theo chuẩn Swarm 4.0 Supreme.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

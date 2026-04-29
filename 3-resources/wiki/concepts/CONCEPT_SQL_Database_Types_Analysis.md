---
file_id: CONCEPT_SQL_Database_Types_Analysis
title: Các loại Database cho phân tích dữ liệu
category: CONCEPT
domain: SQL
status: verified
---

# ️ Database Types for Analysis

Trong phân tích dữ liệu, việc hiểu cách dữ liệu được lưu trữ vật lý giúp tối ưu hóa tốc độ truy vấn đáng kể.

## 1. Row-Store (Transactional Databases)
- **Đặc điểm:** Lưu trữ toàn bộ các cột của một hàng cùng nhau trên đĩa.
- **Ưu điểm:** Tối ưu cho các giao dịch ghi (`INSERT`, `UPDATE`, `DELETE`).
- **Nhược điểm:** Chậm khi thực hiện tính toán trên một vài cột nhưng quét qua hàng triệu hàng.
- **Ví dụ:** MySQL, PostgreSQL, Microsoft SQL Server.

## 2. Column-Store (Analytical Databases)
- **Đặc điểm:** Lưu trữ giá trị của từng cột cùng nhau.
- **Ưu điểm:** 
    - Nén dữ liệu cực tốt (do các giá trị trong một cột thường giống nhau).
    - Tốc độ truy vấn phân tích cực nhanh (chỉ đọc đúng các cột cần thiết).
- **Nhược điểm:** Ghi dữ liệu chậm và tốn kém tài nguyên.
- **Ví dụ:** Amazon Redshift, Snowflake, BigQuery.

## 3. Các hạ tầng khác
- **Hadoop (HDFS):** Hệ thống lưu trữ file phân tán, cho phép xử lý dữ liệu khổng lồ theo cơ chế song song.
- **NoSQL:** Lưu trữ không theo mô hình quan hệ (Key-value, Graph, Document). 
    - *Lưu ý:* Xu hướng hiện nay là "Not only SQL", nhiều hệ thống NoSQL đã hỗ trợ interface SQL để phân tích.
- **Search-based stores:** Elasticsearch, Splunk (tối ưu cho logs và tìm kiếm "kim đáy bể").

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Điểm yếu của Row-Store khi chạy tính toán phân tích (Analytics).*
- **Cách giải quyết:** Trong cơ sở dữ liệu quan hệ truyền thống (như MySQL), hệ thống lưu dữ liệu theo hàng. Do đó, để tính trung bình lương, SQL Engine bắt buộc phải quét đọc qua tất cả các cột của cả bảng, gây nghẽn băng thông ổ đĩa.
```sql
-- Trong Row-Store (MySQL), hệ thống phải quét qua CẢ BẢNG (đọc mọi cột) 
-- chỉ để lấy ra duy nhất cột 'salary', gây lãng phí bộ nhớ và I/O đĩa.
SELECT AVG(salary) FROM employees;
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Sức mạnh của Column-Store khi trích xuất Analytics từ hệ thống E-Learning.*
- **Cách giải quyết:** Nền tảng LMS có hàng chục triệu bản ghi log với hàng trăm cột metadata (thời điểm, user-agent, IP, số lần click). Giáo viên chỉ muốn biết "Thời gian xem video trung bình". Nhờ BigQuery (Column-Store), SQL Engine bỏ qua mọi cột khác, chỉ lấy đúng cột `Thoi_Gian_Xem`, giúp tính toán trong vài mili-giây.
```sql
-- Trong Column-Store (Redshift/BigQuery), dữ liệu cột 'Thoi_Gian_Xem' được lưu liền kề nhau.
-- Hệ thống chỉ trích xuất đúng vùng dữ liệu của cột đó.
SELECT AVG(Thoi_Gian_Xem) AS TB_Phut_Hoc FROM logs_he_thong;
```

---
 Nguồn: [[SOURCE_TOOL_SQL_for_Data_Analysis]] — Section "Database Types and How to Work with Them"
[AUDITOR] Rule 14: Đã xác nhận sự khác biệt cốt lõi giữa Row-wise và Column-wise storage.

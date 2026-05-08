---
file_id: CONCEPT_SQL_CTEs
title: CONCEPT Biểu thức Bảng Tạm thời (Common Table Expressions - CTE)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Biểu thức Bảng Tạm thời (Common Table Expressions - CTE)

## 1. Định nghĩa
**CTE** là một tập kết quả tạm thời được định nghĩa trong phạm vi thực thi của một câu lệnh SELECT, INSERT, UPDATE hoặc DELETE. CTE giúp làm cho các truy vấn phức tạp trở nên dễ đọc và dễ bảo trì hơn bằng cách chia nhỏ chúng thành các logic tuần tự.

## 2. Cú pháp
```sql
WITH Ten_CTE AS (
    SELECT ...
)
SELECT * FROM Ten_CTE;
```

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Tính toán doanh thu trung bình của các khách hàng có hơn 5 đơn hàng.
> **Ứng dụng**:
> ```sql
> WITH High_Volume_Users AS (
>     SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(*) > 5
> )
> SELECT AVG(amount) 
> FROM orders 
> WHERE user_id IN (SELECT user_id FROM High_Volume_Users);
> ```
> **Nguồn**: [[SOURCE_TOOL_SQL_for_Data_Analysis]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Phân tích điểm số học sinh.
> **Tư duy CTE**: Giống như việc bạn tạo ra một danh sách phụ "Các học sinh giỏi" trước khi tính điểm trung bình cho riêng nhóm đó. Thay vì viết một câu lệnh lồng nhau (Subquery) khó hiểu, bạn đặt tên cho danh sách phụ đó bằng `WITH`, giúp người khác đọc code của bạn như đọc một câu chuyện logic.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_TOOL_SQL_for_Data_Analysis]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

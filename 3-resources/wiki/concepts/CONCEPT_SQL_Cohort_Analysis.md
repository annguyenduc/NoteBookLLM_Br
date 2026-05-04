---
file_id: CONCEPT_SQL_Cohort_Analysis
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
tags: ["SQL", "Data_Analysis", "Cohort", "Retention"]
source: "[[SOURCE_SQL_Cohort_Analysis]]"
created: "2026-05-03"
---

# Concept: SQL Cohort Analysis

## 1. Core Principle (Bản chất cốt lõi)
Phân tích Cohort là kỹ thuật chia người dùng thành các nhóm có chung đặc điểm (thường là thời điểm bắt đầu sử dụng sản phẩm) để theo dõi hành vi của họ theo thời gian. Trong SQL, điều này được thực hiện bằng cách tính toán khoảng cách giữa **Ngày đầu tiên (Cohort Date)** và **Ngày hoạt động (Activity Date)**.

## 2. Ví dụ đối chiếu (Rule 17 - Double Examples)

### Ví dụ 1: Trích dẫn kỹ thuật (Original Context)
Sử dụng CTE để xác định tháng đầu tiên của mỗi khách hàng và tính toán chỉ số tháng (0, 1, 2...):
```sql
WITH user_cohorts AS (
    SELECT user_id, MIN(purchase_date) as first_purch
    FROM sales GROUP BY 1
)
SELECT 
    DATE_TRUNC('month', first_purch) as cohort,
    DATEDIFF(month, first_purch, s.purchase_date) as month_idx,
    COUNT(DISTINCT s.user_id)
FROM sales s
JOIN user_cohorts uc ON s.user_id = uc.user_id
GROUP BY 1, 2;
```
**Nguồn**: `WEBSITE_SQL_Cohort_Analysis` — Section "Standard Query Pattern"

### Ví dụ 2: Ẩn dụ sư phạm (Pedagogical Application)
Hãy tưởng tượng bạn đang theo dõi **"Một nhóm học sinh cùng nhập học vào tháng 9"** (Cohort tháng 9).
- **Tháng 0**: 100% học sinh đi học.
- **Tháng 1**: Có 5 bạn nghỉ học (Retention 95%).
- **Tháng 2**: Có thêm 10 bạn nghỉ (Retention 85%).
Phân tích Cohort giúp bạn biết được "lớp học" nào bền vững hơn (ví dụ lớp tháng 9 vs lớp tháng 10) thay vì chỉ nhìn vào tổng số học sinh đang có.

## 3. 4F Reflection
- **Facts**: Kết quả SQL thường trả về dạng "Long format", cần Pivot để tạo Heatmap.
- **Feelings**: Truy vấn Cohort thường trông rất đáng sợ vì nhiều tầng JOIN/CTE nhưng logic thực ra rất tuyến tính.
- **Findings**: Luôn cần `COUNT(DISTINCT user_id)` vì một người dùng có thể có nhiều hành động trong cùng một tháng.
- **Futures**: Cần mở rộng sang "Behavioral Cohorts" (ví dụ: nhóm người dùng từng sử dụng tính năng X).

---
Nguồn: [[SOURCE_SQL_Cohort_Analysis]]
[[CONCEPT_SQL_Aggregations]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

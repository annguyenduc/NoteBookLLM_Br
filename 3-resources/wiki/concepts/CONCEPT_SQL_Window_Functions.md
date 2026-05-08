---
file_id: CONCEPT_SQL_Window_Functions
title: CONCEPT Hàm Cửa sổ trong SQL (Window Functions)
type: concept
status: VERIFIED
tags:
ai-first: true
confidence: 0.8
last_reconciled: 2026-05-08
created: 2026-05-01
last_updated: 2026-05-07
---

# Hàm Cửa sổ trong SQL (Window Functions)

## 1. Định nghĩa
Hàm Cửa sổ cho phép thực hiện các tính toán trên một tập hợp các hàng có liên quan đến hàng hiện tại. Khác với `GROUP BY`, hàm cửa sổ không gộp các hàng lại mà giữ nguyên chi tiết của từng hàng trong kết quả trả về.

## 2. Các hàm phổ biến
- **`ROW_NUMBER()`**: Đánh số thứ tự các hàng.
- **`RANK()` / `DENSE_RANK()`**: Xếp hạng dữ liệu.
- **`SUM() OVER()`**: Tính tổng lũy kế (Running total).
- **`LAG()` / `LEAD()`**: Truy cập dữ liệu của hàng trước hoặc hàng sau.

## 3. Ví dụ đối chiếu (R18: Double Examples)

### Ví dụ từ sách (Original)
> **Bối cảnh**: Tính tổng lũy kế doanh thu theo ngày.
> **Ứng dụng**:
> ```sql
> SELECT date, revenue,
>        SUM(revenue) OVER (ORDER BY date) as running_total
> FROM sales;
> ```
> **Nguồn**: [[SOURCE_TOOL_SQL_for_Data_Analysis]].

### Ứng dụng sư phạm (Pedagogical Application)
> **Bối cảnh**: Xếp hạng học sinh trong lớp dựa trên điểm số.
> **Tư duy Window Function**: Giống như việc bạn yêu cầu học sinh đứng thành một hàng dọc theo điểm từ cao đến thấp, sau đó bạn đi dọc hàng và đánh số thứ tự cho từng em. Bạn vẫn nhìn thấy từng học sinh (không gộp nhóm), nhưng mỗi em giờ đây đã có thêm một chỉ số "Xếp hạng" đi kèm.

## 4. Trích dẫn nguồn
- **Nguồn**: [[SOURCE_TOOL_SQL_for_Data_Analysis]].


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

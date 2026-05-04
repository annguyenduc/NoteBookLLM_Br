---
entity: concept
type: technical
tags: [[ENTITY_SQL|sql]], window_functions, analytics]
source: [[SOURCE_TOOL_SQL_Cookbook]]
status: verified
last_updated: 2026-04-29
---

# Window Functions (Hàm cửa sổ)

## 1. Định nghĩa
Window Functions (còn gọi là hàm phân tích - analytic functions) cho phép thực hiện các phép tính toán trên một tập hợp các dòng có liên quan đến dòng hiện tại. Khác với `GROUP BY`, Window Functions không làm gộp (collapse) các dòng vào một dòng duy nhất; mỗi dòng trong kết quả truy vấn vẫn giữ nguyên định danh của nó trong khi vẫn mang theo kết quả tính toán của "cửa sổ" đó.

**Nguồn**: [[SOURCE_TOOL_SQL_Cookbook]] — Phụ lục A (Xác nhận Rule 14 từ: [[SOURCE_TOOL_SQL_Cookbook]])

## 2. Cấu trúc cơ bản
```sql
<function_name>(<expression>) OVER (
    [PARTITION BY <column_list>]
    [ORDER BY <column_list>]
    [ROWS/RANGE <frame_clause>]
)
```

### Các thành phần chính:
- **PARTITION BY**: Chia tập kết quả thành các nhóm (cửa sổ) nhỏ hơn (tương tự GROUP BY nhưng không gộp dòng).
- **ORDER BY**: Xác định thứ tự các dòng bên trong mỗi nhóm.
- **Frame Clause (ROWS/RANGE)**: Xác định giới hạn cụ thể của các dòng trong cửa sổ so với dòng hiện tại (ví dụ: "3 dòng trước và 3 dòng sau").

## 3. So sánh với GROUP BY
| Đặc điểm | GROUP BY | Window Functions |
| :--- | :--- | :--- |
| **Số lượng dòng trả về** | Bằng số lượng nhóm (gộp dòng). | Giữ nguyên số dòng gốc của bảng. |
| **Tính linh hoạt** | Chỉ truy cập được dữ liệu đã gộp. | Truy cập đồng thời dữ liệu chi tiết dòng hiện tại và dữ liệu tổng hợp của nhóm. |
| **Khả năng xếp hạng** | Khó thực hiện (cần join phức tạp). | Rất mạnh (ROW_NUMBER, RANK, DENSE_RANK). |

<!-- [AUDITOR] Rule 14: Đối soát từ trang 530, dòng 23117-23130. -->

## 4. Các hàm phổ biến
### Hàm xếp hạng (Ranking)
- **ROW_NUMBER()**: Đánh số thứ tự duy nhất cho mỗi dòng trong nhóm.
- **RANK()**: Đánh số thứ tự có để lại khoảng trống nếu có giá trị trùng lặp (1, 2, 2, 4).
- **DENSE_RANK()**: Đánh số thứ tự liên tục kể cả khi có giá trị trùng lặp (1, 2, 2, 3).

### Hàm giá trị (Value)
- **LAG()**: Truy cập giá trị của dòng phía trước dòng hiện tại.
- **LEAD()**: Truy cập giá trị của dòng phía sau dòng hiện tại.
- **FIRST_VALUE() / LAST_VALUE()**: Lấy giá trị đầu tiên hoặc cuối cùng trong cửa sổ.

### Hàm tổng hợp (Aggregate)
- **SUM(...) OVER(...)**: Tính tổng lũy kế hoặc tổng nhóm.
- **AVG(...) OVER(...)**: Tính trung bình trượt hoặc trung bình nhóm.

## 5. Ví dụ đối chiếu (Rule 17: Double Examples)

### 5.1. Ví dụ từ sách (Original)
*Tình huống: Tính lương cao nhất/thấp nhất và tổng lương theo phòng ban (Hàm Aggregate).*
- **Cách giải quyết:** Ta muốn lấy danh sách tất cả nhân viên nhưng kế bên lại có cột tổng lương và mức lương cao nhất của toàn phòng ban đó. Nhờ có cấu trúc `OVER(PARTITION BY deptno)`, ta không bị bắt gộp dòng như `GROUP BY`.
```sql
SELECT 
    ename, 
    sal,
    deptno,
    MAX(sal) OVER(PARTITION BY deptno) as HiDpt,
    MIN(sal) OVER(PARTITION BY deptno) as LoDpt,
    SUM(sal) OVER(PARTITION BY deptno) as DptSum,
    SUM(sal) OVER() as TotalSum
FROM emp;
```

### 5.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Xếp hạng học sinh theo điểm số thi từng môn (Hàm Ranking).*
- **Cách giải quyết:** Giáo viên cần lập danh sách xếp hạng học sinh từ trên xuống dưới cho TỪNG môn học riêng biệt (Ví dụ: Đứa nhất môn Toán, đứa nhất môn Văn). Hàm `ROW_NUMBER` (hoặc `RANK`/`DENSE_RANK`) đi cùng `PARTITION BY mon_hoc ORDER BY diem DESC` xử lý vấn đề này rất gọn gàng.
```sql
-- Xếp hạng học sinh theo từng môn học
SELECT 
    ho_ten, 
    diem_thi,
    mon_hoc,
    RANK() OVER(PARTITION BY mon_hoc ORDER BY diem_thi DESC) as Thu_Hang_Mon
FROM ket_qua_thi_hoc_ky;
```

## 6. Lưu ý quan trọng
- Window Functions được tính toán **sau** khi các mệnh đề `WHERE`, `GROUP BY`, và `HAVING` đã được thực thi.
- Không thể sử dụng Window Functions trực tiếp trong mệnh đề `WHERE`. Để lọc theo kết quả hàm cửa sổ, cần sử dụng Subquery hoặc CTE.

---
**Xem thêm:**
- [[CONCEPT_SQL_CTEs]]
- [[CONCEPT_SQL_Advanced_Reporting]]


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

---
title: Các cấu trúc dữ liệu cốt lõi của [[ENTITY_PANDAS|pandas]]
status: DRAFT
file_id: CONCEPT_PY_pandas_Data_Structures
---

---
file_id: CONCEPT_PY_pandas_Data_Structures
title: Các cấu trúc dữ liệu cốt lõi của [[ENTITY_PANDAS|pandas]]
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# pandas Data Structures

Thư viện `pandas` cung cấp hai cấu trúc dữ liệu chính được thiết kế để làm việc với dữ liệu bảng và chuỗi thời gian một cách trực quan.

## 1. Series (1 chiều)
- Là một mảng 1 chiều chứa các phần tử cùng loại, kèm theo một mảng các nhãn dữ liệu gọi là **Index**.
- Có thể coi như một cột trong bảng hoặc một danh sách có đánh chỉ mục tùy chỉnh.

## 2. DataFrame (2 chiều)
- Là cấu trúc dữ liệu quan trọng nhất, đại diện cho một bảng dữ liệu (giống [[ENTITY_EXCEL|Excel]] Sheet hoặc [[ENTITY_SQL|SQL]] Table).
- Gồm nhiều Series có chung một Index.
- Có cả **Index** (hàng) và **Columns** (cột).

## Đặc điểm quan trọng: Data Alignment
- Khi thực hiện phép toán giữa hai đối tượng pandas, dữ liệu sẽ tự động căn chỉnh dựa trên nhãn (Label) của Index. Nếu nhãn không khớp, pandas sẽ điền `NaN` thay vì gây lỗi.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Theo dõi số lượng nhân sự của từng phòng ban bằng Series.*
- **Cách giải quyết:** Khi bạn có một tập dữ liệu 1 chiều gồm các nhãn và giá trị tương ứng, khởi tạo pandas `Series` là phương pháp chuẩn nhất.
```python
import pandas as pd

# Khởi tạo Series với dữ liệu và index (nhãn)
staff_counts = pd.Series([10, 25, 15], index=['HR', 'Engineering', 'Sales'])
print(staff_counts['Engineering']) # Output: 25
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Tạo một bảng dữ liệu chứa thông tin điểm thi học sinh (DataFrame).*
- **Cách giải quyết:** Giáo viên thu thập điểm Toán, Văn, Anh của các học sinh. Thay vì dùng danh sách lồng nhau (nested list) của Python, giáo viên dùng `DataFrame` để tạo bảng dữ liệu 2 chiều. Điều này cho phép tính điểm trung bình từng môn hoặc lấy thông tin từng học sinh dễ dàng.
```python
import pandas as pd

# Khởi tạo DataFrame từ một Dictionary
data_diem = {
    'Ho_Ten': ['Alice', 'Bob', 'Charlie'],
    'Toan': [8.5, 9.0, 7.5],
    'Van': [7.0, 8.5, 8.0]
}
df_diem = pd.DataFrame(data_diem)

# Truy xuất cột điểm Toán (trả về một Series)
print(df_diem['Toan'])
```

---
 Nguồn: [[SOURCE_TOOL_Python_for_Data_Analysis]] — Chapter 5
[AUDITOR] Rule 14: Đã xác nhận định nghĩa Series và DataFrame. Cấu trúc ví dụ phản ánh rõ đặc tính mảng 1 chiều và 2 chiều của thư viện.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

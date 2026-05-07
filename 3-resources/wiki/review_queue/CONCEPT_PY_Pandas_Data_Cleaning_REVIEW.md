---
title: "Pandas Data Cleaning (Làm sạch dữ liệu)"
status: DRAFT
file_id: CONCEPT_PY_Pandas_Data_Cleaning
---

---
file_id: CONCEPT_PY_Pandas_Data_Cleaning
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
title: "Pandas Data Cleaning (Làm sạch dữ liệu)"
source: "[[SOURCE_TOOL_Python_for_Data_Analysis]]"
created: "2026-05-03"
---

# CONCEPT: [[ENTITY_PANDAS|Pandas]] Data Cleaning (Làm sạch dữ liệu)

> [!NOTE]
> Làm sạch dữ liệu là bước chiếm 80% thời gian của một Data Analyst. Trong Pandas, các thao tác này tập trung vào xử lý giá trị thiếu (NA), dữ liệu trùng lặp và chuẩn hóa giá trị.

## 1. Xử lý dữ liệu thiếu (Missing Data)
Pandas sử dụng `NaN` (Not a Number) làm giá trị sentinel để biểu diễn dữ liệu thiếu cho cả kiểu số và không phải số.

### Kiểm tra dữ liệu thiếu
- `isnull()`: Trả về mặt nạ boolean (True nếu là NA).
- `notnull()`: Ngược lại với `isnull()`.

### Loại bỏ dữ liệu thiếu (`dropna`)
- **Series**: `s.dropna()` loại bỏ tất cả các dòng có giá trị NA.
- **DataFrame**:
  - `df.dropna()`: Loại bỏ bất kỳ dòng nào chứa ít nhất một giá trị NA.
  - `df.dropna(how='all')`: Chỉ loại bỏ dòng nếu *tất cả* các giá trị đều là NA.
  - `df.dropna(axis=1)`: Loại bỏ các *cột* chứa NA.
  - `df.dropna(thresh=n)`: Giữ lại các dòng có ít nhất `n` giá trị không phải NA.

### Điền giá trị thiếu (`fillna`)
- `df.fillna(value)`: Thay thế NA bằng một giá trị cố định (ví dụ: 0).
- `df.fillna({'col1': 0, 'col2': 0.5})`: Điền giá trị khác nhau cho từng cột.
- **Interpolation**:
  - `method='ffill'` (forward fill): Lấy giá trị phía trước đè lên NA.
  - `method='bfill'` (backward fill): Lấy giá trị phía sau đè lên NA.

---

## 2. Xử lý dữ liệu trùng lặp (Duplicate Data)
Thường xảy ra khi gộp nhiều nguồn dữ liệu hoặc lỗi nhập liệu.

- `df.duplicated()`: Trả về Series boolean cho biết dòng đó có bị trùng với một dòng xuất hiện trước đó hay không.
- `df.drop_duplicates()`: Trả về DataFrame đã loại bỏ các dòng trùng lặp.
- **Tùy chọn nâng cao**:
  - `df.drop_duplicates(['k1'])`: Chỉ kiểm tra trùng lặp dựa trên cột `k1`.
  - `take_last=True` (hoặc `keep='last'` trong các bản mới): Giữ lại bản ghi cuối cùng thay vì bản ghi đầu tiên.

---

## 3. Thay thế giá trị (`replace`)
Dùng để sửa lỗi dữ liệu hoặc chuẩn hóa các sentinel khác (ví dụ: -999 thành NaN).

```[[ENTITY_Python|python]]
# Thay thế đơn lẻ
df.replace(-999, np.nan)

# Thay thế nhiều giá trị
df.replace([-999, -1000], np.nan)

# Thay thế tương ứng bằng dict
df.replace({-999: np.nan, -1000: 0})
```

---

## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Xử lý missing values (giá trị thiếu) trong tập dữ liệu bằng cách điền giá trị đặc trưng (fillna).*
- **Cách giải quyết:** Trong thực tế, việc xóa dòng chứa giá trị thiếu (`dropna`) có thể làm mất thông tin quan trọng. Sử dụng `fillna` với giá trị trung bình (`mean`) của cột là một kỹ thuật Data Cleaning rất phổ biến.
```python
# Điền giá trị thiếu bằng trung bình của từng cột
df.fillna(df.mean(), inplace=True)
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Làm sạch danh sách học sinh tham gia ngoại khóa bị trùng lặp.*
- **Cách giải quyết:** Khi tổng hợp danh sách đăng ký câu lạc bộ từ nhiều nguồn (Google Form, File [[ENTITY_EXCEL|Excel]] lớp), nhiều học sinh điền tên nhiều lần. Giáo viên sử dụng `drop_duplicates` trên cột Mã HS và dùng `keep='last'` để lấy thông tin đăng ký mới nhất.
```python
# data chứa danh sách đăng ký
# Loại bỏ trùng lặp dựa trên cột 'Ma_HS' và giữ lại bản ghi cuối (mới nhất)
data_cleaned = data.drop_duplicates(['Ma_HS'], keep='last')
```

---

## 5. Tóm tắt các phương thức cốt lõi

| Phương thức | Mô tả |
|:---|:---|
| `dropna` | Lọc axis labels dựa trên việc có chứa dữ liệu thiếu hay không. |
| `fillna` | Điền giá trị vào các vị trí thiếu. |
| `isnull` | Trả về các giá trị boolean chỉ thị vị trí thiếu. |
| `notnull` | Ngược lại với `isnull`. |
| `duplicated` | Kiểm tra dòng trùng lặp. |
| `drop_duplicates` | Xóa dòng trùng lặp. |

---
Nguồn: [[SOURCE_TOOL_Python_for_Data_Analysis]] — Chapter 7 (Data Cleaning and Preparation)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

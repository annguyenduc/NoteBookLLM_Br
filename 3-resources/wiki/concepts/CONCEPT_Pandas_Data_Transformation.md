# CONCEPT: Pandas Data Transformation (Biến đổi dữ liệu)

> [!NOTE]
> Biến đổi dữ liệu bao gồm các thao tác thay đổi cấu trúc giá trị, phân đoạn dữ liệu liên tục thành các nhóm rời rạc, và chuẩn hóa dữ liệu cho các mô hình thống kê/ML.

## 1. Ánh xạ và Chuyển đổi (Mapping)
Sử dụng `map` để thực hiện biến đổi trên từng phần tử dựa trên một hàm hoặc một từ điển ánh xạ.

```python
meat_to_animal = {'bacon': 'pig', 'pastrami': 'cow', ...}
# Chuyển về chữ thường trước khi map
df['animal'] = df['food'].str.lower().map(meat_to_animal)
```

## 2. Thay thế giá trị (`replace`)
Đã đề cập trong phần Cleaning, nhưng cần lưu ý khả năng thay thế hàng loạt bằng list hoặc dict.
- `df.replace([-999, -1000], np.nan)`
- `df.replace({-999: np.nan, -1000: 0})`

## 3. Đổi tên trục (Renaming Axis)
- `df.index.map(str.upper)`: Biến đổi chỉ mục trực tiếp.
- `df.rename(index=..., columns=...)`: Tạo bản sao mới với tên trục đã đổi (hoặc dùng `inplace=True`).
- Rất hữu ích khi muốn đổi tên một vài cột cụ thể: `df.rename(columns={'old_name': 'new_name'})`.

## 4. Phân đoạn và Băm nhỏ (Discretization & Binning)
Chuyển đổi dữ liệu liên tục (như Tuổi) thành các nhóm (như Trẻ em, Người lớn).

### `pd.cut`: Chia theo các khoảng xác định
- `cats = pd.cut(ages, [18, 25, 35, 60, 100])`: Chia theo danh sách các điểm biên.
- `pd.cut(ages, 4)`: Chia thành 4 khoảng có độ dài bằng nhau.

### `pd.qcut`: Chia theo phân vị (Quantiles)
- Đảm bảo số lượng phần tử trong mỗi thùng (bin) là xấp xỉ bằng nhau.
- `pd.qcut(data, 4)`: Chia thành các tứ phân vị (quartiles).

## 5. Phát hiện và Lọc giá trị ngoại lệ (Outliers)
Chủ yếu dựa trên các thao tác mảng (array operations) và lọc boolean.
- Tìm giá trị có trị tuyệt đối > 3: `data[(np.abs(data) > 3).any(1)]`.
- Chặn giá trị (Capping): `data[np.abs(data) > 3] = np.sign(data) * 3`.

## 6. Lấy mẫu ngẫu nhiên (Sampling)
- `np.random.permutation(n)`: Tạo một hoán vị ngẫu nhiên của các chỉ số.
- `df.take(sampler)`: Sắp xếp lại DataFrame theo sampler.
- `df.sample(n=3)` (trong các bản Pandas mới): Cách lấy mẫu nhanh nhất.

## 7. Biến giả/Biến chỉ thị (Dummy Variables)
Chuyển đổi biến phân loại thành ma trận 0-1 cho mô hình ML.
- `pd.get_dummies(df['key'], prefix='key')`.
- Thường dùng kết hợp với `join` để gộp vào dữ liệu gốc.

---

## 8. Ví dụ đối chiếu (Rule 17: Double Examples)

### 8.1. Ví dụ từ sách (Original)
*Tình huống: Ánh xạ và chuẩn hóa dữ liệu bằng hàm `map`.*
- **Cách giải quyết:** Trước khi map từ điển, giá trị trong cột danh mục (ví dụ thức ăn) không đồng nhất về in hoa/in thường. Ta phải dùng `.str.lower()` để chuẩn hóa dữ liệu trước khi ánh xạ sang phân loại cấp cao hơn. Kỹ thuật này thường dùng để gán nhãn lại danh mục.
```python
meat_to_animal = {'bacon': 'pig', 'pulled pork': 'pig', 'pastrami': 'cow', 'nova lox': 'salmon'}

# Chuẩn hóa về chữ thường trước khi ánh xạ
data['animal'] = data['food'].str.lower().map(meat_to_animal)
```

### 8.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Phân đoạn dữ liệu liên tục thành xếp loại học lực (Discretization).*
- **Cách giải quyết:** Hàm `cut` rất mạnh mẽ để chuyển đổi các biến số liên tục (ví dụ: Điểm tổng kết) thành các biến phân loại (Categorical) để lập báo cáo thành tích. Giáo viên chia điểm từ 0-10 thành các mốc: Kém, Trung bình, Khá, Giỏi.
```python
diem_thi = [4.5, 6.0, 8.5, 9.2, 5.5, 7.8]
bins = [0, 5.0, 6.5, 8.0, 10.0]
nhan_xep_loai = ['Yếu/Kém', 'Trung bình', 'Khá', 'Giỏi']

# Chia dữ liệu điểm thành các nhóm rời rạc và gắn nhãn
xeploai = pd.cut(diem_thi, bins, labels=nhan_xep_loai)
```

---
Nguồn: [[SOURCE_d:\NoteBookLLM_Br\3-resources\raw\sources\PY_Python_for_Data_Analysis]] (Xác nhận Rule 14 từ: [[\d:\NoteBookLLM_Br\3-resources\raw\sources\PY_Python_for_Data_Analysis]])

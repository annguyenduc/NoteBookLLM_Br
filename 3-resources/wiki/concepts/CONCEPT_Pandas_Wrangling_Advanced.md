# CONCEPT: Pandas Advanced Wrangling (Hợp nhất và Tái cấu trúc)

> [!NOTE]
> Hợp nhất (Merging) và Nối (Concatenation) là các thao tác kết hợp nhiều nguồn dữ liệu. Tái cấu trúc (Reshaping) giúp thay đổi cách trình bày dữ liệu từ dạng bảng dài (long) sang bảng rộng (wide) và ngược lại.

## 1. Hợp nhất dữ liệu (Merging/Joining)
Tương tự như phép JOIN trong SQL, kết nối các dòng dựa trên các khóa (keys).

### `pd.merge`: Hợp nhất kiểu cơ sở dữ liệu
- `pd.merge(df1, df2, on='key')`: Mặc định là **Inner Join**.
- **Các kiểu Join (`how`)**:
  - `left`: Giữ tất cả các khóa ở bảng trái.
  - `right`: Giữ tất cả các khóa ở bảng phải.
  - `outer`: Lấy hợp (union) các khóa từ cả hai bảng.
  - `inner`: Lấy giao (intersection) các khóa.
- **Khóa khác tên**: `pd.merge(df1, df2, left_on='lkey', right_on='rkey')`.
- **Hợp nhất trên Index**: `left_index=True`, `right_index=True`.

### `df.join`: Hợp nhất dựa trên Index
Mặc định thực hiện Left Join trên Index. Tiện lợi khi gộp nhiều DataFrame có cùng Index.

## 2. Nối dữ liệu (Concatenation)
"Dán" các đối tượng lại với nhau dọc theo một trục.

- `pd.concat([s1, s2, s3])`: Mặc định nối theo dòng (`axis=0`).
- `pd.concat([df1, df2], axis=1)`: Nối theo cột.
- **Tùy chọn quan trọng**:
  - `keys`: Tạo chỉ mục phân cấp để phân biệt nguồn dữ liệu gốc.
  - `ignore_index=True`: Không giữ lại index cũ, tạo index mới từ 0 đến n-1.

## 3. Tái cấu trúc (Reshaping)

### Stack & Unstack
Sử dụng cho dữ liệu có chỉ mục phân cấp (Hierarchical Indexing).
- `stack`: "Xoay" dữ liệu từ cột vào dòng (làm bảng dài hơn).
- `unstack`: "Xoay" dữ liệu từ dòng ra cột (làm bảng rộng hơn).

### Pivot & Melt
- `df.pivot('date', 'item', 'value')`: Chuyển từ định dạng "dài" (long) sang "rộng" (wide). Thường dùng cho dữ liệu chuỗi thời gian.
- `pd.melt`: Ngược lại với pivot, chuyển bảng từ dạng "rộng" sang "dài".

---
## 4. Ví dụ đối chiếu (Rule 17: Double Examples)

### 4.1. Ví dụ từ sách (Original)
*Tình huống: Hợp nhất (merge) dữ liệu có tên khóa khác biệt.*
- **Cách giải quyết:** Trong thực tế, các bảng đến từ các hệ thống khác nhau thường không đặt tên cột ID giống nhau. Ta dùng `left_on` và `right_on` để định tuyến chính xác. Sử dụng `how='left'` giúp không làm mất thông tin gốc ở bảng bên trái.
```python
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'], 'data2': range(3)})

# Nối 2 bảng khi tên cột khóa khác nhau
merged_df = pd.merge(df3, df4, left_on='lkey', right_on='rkey', how='left')
```

### 4.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Tái cấu trúc bảng điểm từ định dạng dọc (Long) sang ngang (Wide) để lập báo cáo cuối kỳ.*
- **Cách giải quyết:** Hệ thống thi trắc nghiệm thường xuất dữ liệu ở định dạng Dài (Mỗi dòng là 1 lượt thi: Mã HS, Môn, Điểm). Để in báo cáo cho phụ huynh, giáo viên dùng `pivot` để xoay ngang dữ liệu: Mã HS làm Index, các Môn học thành các cột.
```python
# df_diem chứa: Ma_HS, Mon_Hoc, Diem
# Chuyển đổi để mỗi môn học thành một cột riêng, index là Ma_HS
bang_diem_tong_hop = df_diem.pivot(index='Ma_HS', columns='Mon_Hoc', values='Diem')
```

---

## 5. Tóm tắt các đối số của `merge`

| Đối số | Mô tả |
|:---|:---|
| `left`, `right` | Các DataFrame cần hợp nhất. |
| `how` | 'left', 'right', 'outer', hoặc 'inner'. |
| `on` | Tên cột dùng làm khóa (phải có ở cả hai bảng). |
| `left_on`, `right_on` | Tên cột khóa ở bảng trái và phải (khi chúng khác tên). |
| `suffixes` | Tuple các chuỗi để thêm vào tên cột bị trùng (mặc định `_x`, `_y`). |

---
Nguồn: [[SOURCE_d:\NoteBookLLM_Br\3-resources\raw\sources\PY_Python_for_Data_Analysis]] (Xác nhận Rule 14 từ: [[\d:\NoteBookLLM_Br\3-resources\raw\sources\PY_Python_for_Data_Analysis]])

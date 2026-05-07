---
title: "Pandas Aggregation (Gom nhóm và Tổng hợp)"
status: DRAFT
file_id: CONCEPT_PY_Pandas_Aggregation
---

---
file_id: CONCEPT_PY_Pandas_Aggregation
category: "Wiki Page"
prefix: "WIKI"
agent_id: "@engineer"
status: "verified"
title: "Pandas Aggregation (Gom nhóm và Tổng hợp)"
source: "[[SOURCE_TOOL_Python_for_Data_Analysis]]"
created: "2026-05-03"
---

# CONCEPT: [[ENTITY_PANDAS|Pandas]] Aggregation (Gom nhóm và Tổng hợp)

> [!NOTE]
> Gom nhóm dữ liệu dựa trên mô hình **Split-Apply-Combine**: Chia nhỏ dữ liệu thành các nhóm, áp dụng một hàm lên từng nhóm, và kết hợp các kết quả lại.

## 1. Cơ chế GroupBy
Dữ liệu có thể được gom nhóm theo nhiều cách:
- Theo cột: `df.groupby('key1')`.
- Theo nhiều cột: `df.groupby(['key1', 'key2'])`.
- Theo mảng/Series: `df.groupby(states)`.
- Theo hàm: `df.groupby(len)`.
- Theo từ điển/ánh xạ: `df.groupby(mapping, axis=1)`.

## 2. Các hàm tổng hợp tối ưu
Pandas cung cấp các hàm được tối ưu hóa cho GroupBy, tự động bỏ qua giá trị NA.

| Hàm | Mô tả |
|:---|:---|
| `count` | Số lượng giá trị không phải NA trong nhóm. |
| `sum`, `mean`, `median` | Tổng, Trung bình, Trung vị của các giá trị. |
| `min`, `max` | Giá trị nhỏ nhất, lớn nhất. |
| `std`, `var` | Độ lệch chuẩn và Phương sai. |
| `first`, `last` | Giá trị không phải NA đầu tiên và cuối cùng. |

## 3. Tổng hợp nâng cao với `agg`
Cho phép áp dụng các hàm tùy chỉnh hoặc nhiều hàm cùng lúc.

```[[ENTITY_Python|python]]
# Một hàm tùy chỉnh
def peak_to_peak(arr):
    return arr.max() - arr.min()
grouped.agg(peak_to_peak)

# Nhiều hàm cùng lúc
grouped.agg(['mean', 'std', peak_to_peak])

# Đặt tên cho các cột kết quả
grouped.agg([('trung_binh', 'mean'), ('do_lech', np.std)])

# Áp dụng hàm khác nhau cho từng cột
grouped.agg({'tip': np.max, 'size': 'sum'})
```

## 4. Thao tác trên từng nhóm (Iteration)
Đối tượng GroupBy hỗ trợ vòng lặp, trả về tuple gồm `(tên_nhóm, khối_dữ_liệu)`.
```python
for name, group in df.groupby('key1'):
    print(name)
    print(group)
```

---
## 5. Các điểm lưu ý
- **Nuisance columns**: Các cột không phải số (như chuỗi) sẽ tự động bị loại bỏ khi thực hiện các phép toán số học như `mean()`.
- **Level keyword**: Dùng để gom nhóm theo một cấp độ trong MultiIndex: `df.groupby(level='cty', axis=1)`.

---

## 6. Ví dụ đối chiếu (Rule 17: Double Examples)

### 6.1. Ví dụ từ sách (Original)
*Tình huống: Tính nhiều chỉ số thống kê cùng lúc trên tập dữ liệu Tips (tiền boa tại nhà hàng).*
- **Cách giải quyết:** Khi làm Exploratory Data Analysis (EDA), dùng `agg` với danh sách các hàm giúp ta nhanh chóng có một bảng tóm tắt đầy đủ về phân phối của dữ liệu theo từng phân khúc khách hàng.
```python
# Gom nhóm hóa đơn theo Ngày và Tình trạng hút thuốc của khách
grouped = tips.groupby(['day', 'smoker'])

# Trích xuất 4 hàm tổng hợp cùng lúc trên cột tỷ lệ tiền boa (tip_pct)
result = grouped['tip_pct'].agg(['mean', 'std', 'max', 'min'])
```

### 6.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Tổng hợp báo cáo chất lượng điểm thi theo Khối Lớp và Môn Học.*
- **Cách giải quyết:** Thay vì phải dùng [[ENTITY_EXCEL|Excel]] PivotTable thủ công cho từng khối, giáo viên dùng Pandas để gom nhóm (`groupby`) học sinh theo Khối Lớp và Môn Học, sau đó dùng `agg` để tính ra Điểm trung bình, Điểm cao nhất và Số lượng học sinh đi thi chỉ trong 2 dòng code.
```python
# df chứa dữ liệu điểm thi toàn trường
grouped_scores = df.groupby(['Khoi_Lop', 'Mon_Hoc'])

# Lấy ra các chỉ số quan trọng để báo cáo cho Ban Giám Hiệu
report = grouped_scores['Diem_Thi'].agg(['mean', 'max', 'count'])
```

---
Nguồn: [[SOURCE_TOOL_Python_for_Data_Analysis]] — Chapter 10 (Data Aggregation and Group Operations)


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

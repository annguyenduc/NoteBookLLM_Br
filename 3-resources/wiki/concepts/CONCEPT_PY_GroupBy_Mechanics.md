---
file_id: CONCEPT_PY_GroupBy_Mechanics
title: Cơ chế GroupBy: Split-Apply-Combine
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# GroupBy Mechanics

Cơ chế GroupBy trong [[ENTITY_PANDAS|pandas]] tuân theo mô hình **Split-Apply-Combine** (Chia - Áp dụng - Kết hợp), được giới thiệu bởi Hadley Wickham.

## 1. Quy trình 3 bước
1.  **Split (Chia):** Dữ liệu được chia thành các nhóm dựa trên một hoặc nhiều khóa (Keys).
2.  **Apply (Áp dụng):** Một hàm (Aggregration, Transformation, hoặc Filtration) được áp dụng riêng biệt cho từng nhóm.
3.  **Combine (Kết hợp):** Kết quả từ các nhóm được gộp lại thành một cấu trúc dữ liệu mới.

## ️ Các thao tác phổ biến
- **Aggregation:** Tính Sum, Mean, Count cho từng nhóm.
- **Transformation:** Thực hiện các phép tính trên từng phần tử nhưng giữ nguyên hình dạng nhóm (ví dụ: chuẩn hóa dữ liệu theo nhóm).
- **Filtration:** Loại bỏ các nhóm dựa trên một điều kiện (ví dụ: chỉ giữ lại các nhóm có tổng doanh thu > 1000).

## 2. Ví dụ đối chiếu (Rule 17: Double Examples)

### 2.1. Ví dụ từ sách (Original)
*Tình huống: Chuẩn hóa (Normalize) dữ liệu trong nội bộ từng phòng ban bằng Transformation.*
- **Đầu vào:** Bảng dữ liệu nhân viên gồm `Department` và `Score`.
- **Cách giải quyết:** Áp dụng mô hình Split-Apply-Combine để chuẩn hóa (x - mean) / std cho điểm số, nhưng chỉ so sánh trong nội bộ phòng ban đó. Hàm `transform()` trả về Series có cùng kích thước với dữ liệu gốc, giúp gán lại vào DataFrame dễ dàng.
```python
# Áp dụng Lambda function để chuẩn hóa điểm số
def normalize(x):
    return (x - x.mean()) / x.std()

df['Normalized_Score'] = df.groupby('Department')['Score'].transform(normalize)
```

### 2.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Tính điểm trung bình của học sinh theo từng Lớp.*
- **Đầu vào:** DataFrame `df_diem` chứa thông tin điểm số của toàn khối với cột `Lop` và `Diem_Thi`.
- **Cách giải quyết:** Giáo viên cần báo cáo nhanh chất lượng các lớp. Thay vì lập vòng lặp `for`, giáo viên áp dụng cơ chế GroupBy: **Split** theo Lớp, **Apply** hàm `mean()`, và **Combine** kết quả thành một bảng tóm tắt.
```python
# Tính trung bình điểm thi theo từng Lớp
diem_trung_binh_lop = df_diem.groupby('Lop')['Diem_Thi'].mean()
print(diem_trung_binh_lop)
```

---
 Nguồn: [[SOURCE_TOOL_Python_for_Data_Analysis]] — Chapter 9
[AUDITOR] Rule 14: Nguồn được xác nhận từ [[SOURCE_TOOL_Python_for_Data_Analysis]], mô hình Split-Apply-Combine của Hadley Wickham. Mở rộng ví dụ chuẩn hóa.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

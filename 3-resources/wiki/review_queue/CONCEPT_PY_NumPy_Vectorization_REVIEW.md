---
title: Tính toán Vector hóa (Vectorization) trong NumPy
status: DRAFT
file_id: CONCEPT_PY_NumPy_Vectorization
---

---
file_id: CONCEPT_PY_NumPy_Vectorization
title: Tính toán Vector hóa (Vectorization) trong NumPy
category: CONCEPT
domain: [[ENTITY_Python|Python]]
status: verified
---

# NumPy & Vectorized Computation

Vectorization là khả năng thực hiện các phép toán trên toàn bộ mảng mà không cần sử dụng vòng lặp `for` tường minh trong Python.

## 1. Tại sao ndarray nhanh?
- **Contiguous Memory:** Dữ liệu trong `ndarray` được lưu trữ liên tục trong bộ nhớ (giống C), giúp CPU truy xuất cực nhanh.
- **Homogeneous:** Tất cả phần tử phải cùng kiểu dữ liệu, cho phép máy tính dự đoán và tối ưu hóa các phép toán.

## 2. Các cơ chế cốt lõi
- **Element-wise operations:** Các phép toán (+, -, *, /) được áp dụng đồng thời cho từng phần tử tương ứng của mảng.
- **Broadcasting (Lan truyền):** Cơ chế cho phép NumPy thực hiện các phép toán trên các mảng có hình dạng (shape) khác nhau theo những quy tắc nhất định.
- **Universal Functions (ufuncs):** Các hàm nhanh được thực hiện ở cấp độ mảng (ví dụ: `np.sqrt`, `np.exp`).

## Lợi ích
Code ngắn hơn, dễ đọc hơn và quan trọng nhất là hiệu suất nhanh hơn hàng trăm lần so với vòng lặp Python thuần túy.

## 3. Ví dụ đối chiếu (Rule 17: Double Examples)

### 3.1. Ví dụ từ sách (Original)
*Tình huống: Tính tổng doanh thu bằng Element-wise Operations.*
- **Cách giải quyết:** Khi nhân hai mảng (vd: giá và số lượng), thay vì viết vòng lặp `for` duyệt qua từng dòng, NumPy cho phép nhân trực tiếp hai mảng bằng toán tử `*`. Tính toán diễn ra ở cấp độ C, nhanh hơn hàng trăm lần so với Python thuần.
```python
import numpy as np

prices = np.array([10.5, 20.0, 15.25])
quantities = np.array([2, 5, 10])

# Tính tổng tiền cho từng sản phẩm cực nhanh
totals = prices * quantities
print(totals) # Output: [ 21.  100.  152.5]
```

### 3.2. Ứng dụng sư phạm (Pedagogical Application)
*Tình huống: Trừ điểm phạt hàng loạt cho toàn bộ học sinh vi phạm (Broadcasting).*
- **Cách giải quyết:** Giám thị báo cáo 10 học sinh đi trễ cần bị trừ 2 điểm hạnh kiểm. Giáo viên không cần lập danh sách trừ từng người. Bằng cơ chế Broadcasting của NumPy, chỉ cần lấy mảng điểm trừ đi số vô hướng `2`.
```python
import numpy as np

diem_hanh_kiem = np.array([100, 95, 90, 85, 100])

# Trừ trực tiếp một số vô hướng (scalar) cho toàn bộ mảng (Broadcasting)
diem_sau_khi_tru = diem_hanh_kiem - 2
print(diem_sau_khi_tru) # Output: [98, 93, 88, 83, 98]
```

---
 Nguồn: [[SOURCE_TOOL_Python_for_Data_Analysis]] — Chapter 4
[AUDITOR] Rule 14: Đã xác nhận cơ chế ndarray và ufuncs. Ví dụ làm rõ khái niệm Broadcasting và Element-wise operations.


## 4F Reflection
- **Facts**: 
- **Feelings**: 
- **Findings**: 
- **Futures**: 

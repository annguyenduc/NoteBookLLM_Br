---
file_id: CONV_Atoms_conv_atoms_v23_13
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v23 13

# Tài liệu Học tập: Xử lý Lỗi Feature Names và Thứ tự Đặc trưng trong Scikit-learn

## Thông tin Tài liệu
| Thuộc tính | Giá trị |
|------------|---------|
| Mã tài liệu | LOM-v4.4-Supreme-ML-001 |
| Loại nội dung | Bài học lập trình máy học |
| Mức độ | Trung cấp |
| Thời lượng ước tính | 45 phút |
| Ngôn ngữ | Tiếng Việt |

---

## Mục tiêu Học tập

Sau khi hoàn thành bài học này, người học sẽ có thể:

- **Hiểu rõ** nguyên nhân gây ra lỗi `ValueError: Unknown label type: continuous` và cảnh báo `UserWarning: X does not have valid feature names`
- **Phân tích** sự không đồng nhất về thứ tự đặc trưng trong quá trình huấn luyện và dự đoán
- **Áp dụng** giải pháp chuyển đổi dữ liệu đầu vào thành DataFrame có tên cột chính xác
- **Triển khai** mô hình hồi quy tuyến tính đa biến mà không gặp lỗi liên quan đến tên đặc trưng

---

## Nội dung Học tập

### 1. Giới thiệu Vấn đề

Trong quá trình phát triển mô hình học máy, việc gặp phải các lỗi liên quan đến định dạng dữ liệu đầu vào là điều phổ biến. Hai lỗi thường gặp nhất là:

- **Lỗi phân loại với dữ liệu liên tục**: `ValueError: Unknown label type: continuous`
- **Cảnh báo thiếu tên đặc trưng**: `UserWarning: X does not have valid feature names`

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 2. Phân tích Chi tiết Các Sự kiện Kỹ thuật

#### 2.1 Lỗi `ValueError: Unknown label type: continuous`

| Chi tiết | Mô tả |
|----------|-------|
| **Loại lỗi** | ValueError |
| **Nguyên nhân** | Sử dụng mô hình phân loại cho biến mục tiêu có giá trị liên tục |
| **Ví dụ cụ thể** | Dùng `LogisticRegression` cho biến mục tiêu như điểm số GPA hoặc S10 |
| **Nguồn** | [vv23] |

#### 2.2 Cảnh báo `UserWarning: X does not have valid feature names`

| Chi tiết | Mô tả |
|----------|-------|
| **Loại cảnh báo** | UserWarning |
| **Nguyên nhân** | Huấn luyện mô hình với DataFrame có tên cột nhưng dự đoán với mảng NumPy không có tên cột |
| **Vị trí lỗi** | `sklearn/base.py` |
| **Nguồn** | [vv23] |

#### 2.3 Sự không đồng nhất về thứ tự đặc trưng

| Giai đoạn | Thứ tự đặc trưng |
|-----------|------------------|
| **Huấn luyện** | `['S-AVG', 'S6']` |
| **Dự đoán** | `np.c_[s6_plane.ravel(), s_avg_plane.ravel()]` (đảo ngược) |
| **Hệ quả** | Kết quả dự đoán sai lệch |
| **Nguồn** | [vv23] |

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

### 3. Giải pháp Toàn diện

#### 3.1 Chuyển đổi dữ liệu đầu vào thành DataFrame

```python
# SỬA LỖI: Tạo DataFrame để có feature names và đúng thứ tự
X_plane = pd.DataFrame(
    np.c_[s_avg_mesh.ravel(), s6_mesh.ravel()],
    columns=feature_cols
)
```

#### 3.2 Đảm bảo thứ tự đặc trưng nhất quán

- **Huấn luyện**: `features = data[['S-AVG', 'S6']]`
- **Dự đoán**: `X_plane` với cùng thứ tự cột `['S-AVG', 'S6']`

#### 3.3 Kiểm tra và xác thực dữ liệu

```python
# Kiểm tra shape và column names
print(f"Training features shape: {X_train.shape}")
print(f"Training features columns: {X_train.columns.tolist()}")
print(f"Prediction features shape: {X_plane.shape}")
print(f"Prediction features columns: {X_plane.columns.tolist()}")
```

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Bảng So sánh Trước và Sau Khi Sửa Lỗi

| Vấn đề | Trước khi sửa | Sau khi sửa | Kết quả |
|--------|---------------|-------------|---------|
| Feature names | NumPy array → cảnh báo | DataFrame có tên cột | Không còn cảnh báo |
| Thứ tự đặc trưng | Không nhất quán | Nhất quán `['S-AVG', 'S6']` | Kết quả chính xác |
| Hiệu suất | Giảm do cảnh báo | Tối ưu hóa | Cải thiện hiệu suất |
| Độ chính xác | Sai lệch do đảo thứ tự | Chính xác theo thiết kế | Đúng như mong đợi |

---

## Bài tập Thực hành

### Worksheet: Xử lý Lỗi Feature Names

#### Bài 1: Phân tích mã nguồn
Xem xét đoạn mã sau và xác định lỗi tiềm ẩn:

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dữ liệu mẫu
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [2, 4, 6, 8, 10],
    'target': [1.1, 2.2, 3.3, 4.4, 5.5]  # Giá trị liên tục
})

X = data[['feature1', 'feature2']]
y = data['target']

model = LogisticRegression()  # Sai: dùng mô hình phân loại cho dữ liệu liên tục
model.fit(X, y)
```

**Câu hỏi:**
1. Lỗi nào sẽ xảy ra khi chạy đoạn mã trên?
2. Giải pháp thay thế phù hợp là gì?

#### Bài 2: Sửa lỗi thứ tự đặc trưng
Hoàn thành đoạn mã sau để đảm bảo thứ tự đặc trưng nhất quán:

```python
import numpy as np
import pandas as pd

# Dữ liệu mẫu
X_train = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Tạo dữ liệu dự đoán - sửa lỗi thứ tự
X_predict_array = np.array([[1, 2, 3]])  # Sai thứ tự
X_predict_correct = pd.DataFrame(        # Đúng cách
    X_predict_array,
    columns=['A', 'B', 'C']  # Đảm bảo thứ tự đúng
)
```

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Câu hỏi Trắc nghiệm

### Quiz: Xử lý Lỗi Feature Names và Thứ tự Đặc trưng

**Câu 1:** Lỗi `ValueError: Unknown label type: continuous` xảy ra khi:
- A) Sử dụng mô hình hồi quy cho dữ liệu phân loại
- B) Sử dụng mô hình phân loại cho dữ liệu liên tục
- C) Dữ liệu có giá trị bị thiếu
- D) Số lượng đặc trưng quá nhiều

**Câu 2:** Cảnh báo `UserWarning: X does not have valid feature names` xuất hiện khi:
- A) Tên cột chứa ký tự đặc biệt
- B) Huấn luyện với DataFrame nhưng dự đoán với NumPy array
- C) Số lượng mẫu quá ít
- D) Dữ liệu không được chuẩn hóa

**Câu 3:** Để đảm bảo thứ tự đặc trưng nhất quán, bạn nên:
- A) Chỉ sử dụng mảng NumPy
- B) Luôn chuyển đổi dữ liệu dự đoán thành DataFrame với tên cột đúng
- C) Thay đổi thứ tự cột ngẫu nhiên
- D) Không cần quan tâm đến thứ tự

**Câu 4:** Giải pháp tốt nhất để tránh cảnh báo feature names là:
- A) Tắt cảnh báo bằng `warnings.filterwarnings`
- B) Chuyển dữ liệu dự đoán thành DataFrame có tên cột phù hợp
- C) Sử dụng mô hình khác
- D) Thay đổi cấu trúc dữ liệu

**Câu 5:** Khi tạo lưới dự đoán cho biểu đồ 3D, bạn nên:
- A) Sử dụng trực tiếp mảng NumPy
- B) Chuyển đổi thành DataFrame với tên cột đúng thứ tự
- C) Đảo ngược thứ tự đặc trưng
- D) Chỉ giữ lại một đặc trưng

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Tình huống Ứng dụng Thực tế

### Scenario: Dự đoán điểm số học sinh

Bạn là kỹ sư dữ liệu tại một trường học, được yêu cầu xây dựng mô hình dự đoán điểm S10 dựa trên điểm trung bình (S-AVG) và điểm môn 6 (S6). Tuy nhiên, bạn gặp phải các lỗi sau:

1. **Lỗi phân loại**: Mô hình cố gắng phân loại điểm số liên tục
2. **Cảnh báo feature names**: Dữ liệu huấn luyện và dự đoán có định dạng khác nhau
3. **Sai thứ tự đặc trưng**: Gây ra kết quả dự đoán không chính xác

**Yêu cầu:**
- Xây dựng mô hình hồi quy tuyến tính đa biến
- Đảm bảo không có cảnh báo hoặc lỗi
- Hiển thị kết quả dự đoán và biểu đồ 3D
- Giải thích các bước xử lý lỗi

**Mã mẫu bắt đầu:**
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict_scores(data):
    # Hoàn thành chức năng xử lý dữ liệu
    # Đảm bảo không có lỗi feature names và thứ tự đặc trưng
    pass
```

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Tài nguyên Hỗ trợ

### Video Hướng dẫn
![Video Demo](../../brain/raw/lms_multi_media_dump/assets/scenario_image1.png)

### Tài liệu Tham khảo
- Tài liệu Scikit-learn về Feature Names: https://scikit-learn.org/stable/modules/compose.html
- Pandas DataFrame documentation: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- Best practices for ML data preprocessing: https://machinelearningmastery.com/data-preparation-best-practices/

### Mã nguồn Hoàn chỉnh
```python
# Đã bao gồm trong phần giải pháp ở đầu tài liệu
# Xem phần "GIẢI PHÁP MÃ NGUỒN HOÀN CHỈNH"
```

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Đánh giá và Phản hồi

### Tiêu chí đánh giá
- **Hiểu biết lý thuyết**: Nhận diện và giải thích các lỗi phổ biến
- **Kỹ năng thực hành**: Áp dụng giải pháp vào mã nguồn thực tế
- **Tư duy phân tích**: Phát hiện vấn đề trong mã nguồn chưa hoàn chỉnh
- **Khả năng giải quyết vấn đề**: Triển khai giải pháp toàn diện

### Phản hồi sau bài học
Sau khi hoàn thành bài học, người học nên có thể:
- ✅ Giải thích được nguyên nhân và giải pháp cho lỗi feature names
- ✅ Đảm bảo thứ tự đặc trưng nhất quán trong quá trình ML
- ✅ Xây dựng mô hình hồi quy tuyến tính đa biến không lỗi
- ✅ Áp dụng kiến thức vào các tình huống thực tế khác

[MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
---
file_id: LMS_DIST_CONV_Atoms_atoms_v25_2
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# LMS DIST CONV Atoms atoms v25 2

# Tài liệu Học Tập: Lập Trình Mô Phỏng và Xử Lý Dữ Liệu với NumPy & Matplotlib

## Thông tin chung
- **Môn học:** Lập trình AI và Xử lý Dữ liệu
- **Chủ đề:** Ứng dụng NumPy và Matplotlib trong mô phỏng thống kê và trực quan hóa dữ liệu
- **Độ khó:** Trung bình đến nâng cao
- **Thời lượng:** 90 phút

---

## Mục tiêu học tập

Sau khi hoàn thành bài học này, người học sẽ có khả năng:

1. Áp dụng các hàm ngẫu nhiên của NumPy để mô phỏng các phân phối xác suất
2. Sử dụng kỹ thuật lọc dữ liệu và xử lý mảng hiệu quả không dùng vòng lặp
3. Trực quan hóa dữ liệu và mô hình AI bằng Matplotlib và Plotly
4. Xử lý lỗi phổ biến trong lập trình mô phỏng

---

## Nội dung chính

### 1. Hàm max() trong lập trình mô phỏng

Trong lập trình mô phỏng, đặc biệt là các bài toán di chuyển hoặc tìm kiếm, việc đảm bảo giá trị không âm là rất quan trọng.

```python
position = max(position - k, 0)
```

Hàm `max(position - k, 0)` đảm bảo rằng giá trị vị trí không bao giờ nhỏ hơn 0 khi thực hiện các bước lùi. Điều này ngăn ngừa lỗi truy cập chỉ số âm trong mảng hoặc các trạng thái không hợp lệ trong mô phỏng [vv25].

**Ví dụ minh họa:**
- Nếu `position = 7`, `k = 3`: kết quả là `max(4, 0) = 4`
- Nếu `position = 2`, `k = 5`: kết quả là `max(-3, 0) = 0`

### 2. Mô phỏng phân phối xác suất với NumPy

#### 2.1. Phân phối đa thức (Multinomial Distribution)

Hàm `np.random.multinomial(n, pvals)` được sử dụng để mô phỏng các biến ngẫu nhiên đa thức, ví dụ như việc tung xúc xắc với các xác suất mặt khác nhau [vv25].

```python
import numpy as np
# Mô phỏng 10 lần tung xúc xắc 6 mặt với xác suất không đồng đều
result = np.random.multinomial(10, [0.1, 0.2, 0.3, 0.15, 0.15, 0.1])
print(result)  # Ví dụ: [1 2 3 1 2 1]
```

#### 2.2. Phân phối hạng mục (Categorical Distribution)

Để mô phỏng phân phối hạng mục, sử dụng `np.random.choice()` với tham số `p=probabilities` để chỉ định xác suất cho từng phần tử [vv25].

```python
# Chọn ngẫu nhiên từ danh sách với xác suất khác nhau
choices = ['A', 'B', 'C']
probabilities = [0.5, 0.3, 0.2]
selected = np.random.choice(choices, p=probabilities)
```

#### 2.3. Phân phối chuẩn (Normal/Gaussian Distribution)

Hàm `np.random.normal(mu, sigma, n)` tạo ra mảng dữ liệu tuân theo quy luật phân phối chuẩn với giá trị trung bình μ và độ lệch chuẩn σ [vv25].

```python
# Tạo 1000 điểm dữ liệu theo phân phối chuẩn
data = np.random.normal(0, 1, 1000)  # mean=0, std=1
```

### 3. Kỹ thuật lọc dữ liệu hiệu quả

NumPy cho phép lọc dữ liệu bằng indexing mà không cần vòng lặp `for`, giúp tối ưu hiệu suất xử lý dữ liệu lớn [vv25].

```python
# Lọc các điểm số >= d mà không dùng vòng lặp
scores = np.array([85, 92, 78, 96, 88, 73, 91])
d = 80
passing_scores = scores[scores >= d]  # Kết quả: [85, 92, 96, 88, 91]
```

### 4. Kết hợp dữ liệu với zip()

Hàm `zip(x_1, x_2)` kết hợp các phần tử từ hai mảng thành các cặp tương ứng, thường dùng để duyệt song song các tọa độ hoặc thuộc tính dữ liệu [vv25].

```python
x_coords = [1, 2, 3, 4]
y_coords = [10, 20, 30, 40]
for x, y in zip(x_coords, y_coords):
    print(f"Tọa độ: ({x}, {y})")
```

### 5. Trực quan hóa dữ liệu

#### 5.1. Biểu đồ phân tán với Matplotlib

Thư viện `matplotlib.pyplot` sử dụng hàm `plt.scatter()` để vẽ biểu đồ phân tán, cho phép trực quan hóa sự phân bố của các lớp dữ liệu trong không gian hai chiều [vv25].

```python
import matplotlib.pyplot as plt

# Vẽ biểu đồ phân tán với màu sắc theo nhãn
plt.scatter(X[:, 0], X[:, 1], c=y)  # c=y để ánh xạ màu theo nhãn
plt.colorbar()
plt.show()
```

Tham số `c=y` trong hàm `plt.scatter` được dùng để ánh xạ màu sắc của các điểm dữ liệu dựa trên giá trị của mảng nhãn `y` [vv25].

#### 5.2. Trực quan hóa 3D với Plotly

Để trực quan hóa bề mặt dự đoán của một mô hình AI trong không gian 3D, sử dụng `go.Surface()` từ `plotly.graph_objects` [vv25].

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Surface(z=z_surface)])
fig.show()
```

### 6. Công cụ hỗ trợ xử lý lưới dữ liệu

#### 6.1. Tạo lưới tọa độ với meshgrid()

Hàm `np.meshgrid()` tạo ra một lưới tọa độ từ các mảng một chiều, là bước chuẩn bị quan trọng để vẽ biểu đồ bề mặt [vv25].

```python
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
```

#### 6.2. Kết hợp mảng theo cột với np.c_[]

`np.c_[]` là công cụ của NumPy dùng để kết hợp các mảng theo chiều ngang (theo cột), thường dùng để tạo mảng tọa độ `(x, y)` từ các lưới giá trị riêng biệt [vv25].

```python
# Tạo mảng tọa độ từ lưới
coordinates = np.c_[xx.ravel(), yy.ravel()]
```

#### 6.3. Làm phẳng mảng với ravel()

Phương thức `ravel()` trong NumPy được dùng để "làm phẳng" một mảng đa chiều thành mảng một chiều theo thứ tự hàng [vv25].

```python
matrix = np.array([[1, 2], [3, 4]])
flattened = matrix.ravel()  # Kết quả: [1, 2, 3, 4]
```

### 7. Tạo dãy số cách đều với linspace()

Hàm `np.linspace(start, stop, num)` tạo ra một dãy số cách đều nhau trong một khoảng xác định, thường dùng để tạo các trục tọa độ cho việc mô phỏng [vv25].

```python
# Tạo 50 điểm cách đều từ 0 đến 10
points = np.linspace(0, 10, 50)
```

### 8. Xử lý lỗi phổ biến

Lỗi `TypeError: 'float' object cannot be interpreted as an integer` thường xảy ra khi truyền một số thực vào tham số yêu cầu số nguyên (như số lượng mẫu `n`) trong các hàm sinh số ngẫu nhiên của NumPy [vv25].

```python
# Sai: truyền float cho tham số số lượng mẫu
# samples = np.random.normal(0, 1, 100.5)  # Lỗi!

# Đúng: chuyển đổi sang integer
samples = np.random.normal(0, 1, int(100.5))
```

### 9. Xác định giá trị lớn nhất với argmax()

Trong lập trình mô phỏng trò chơi hoặc robot, việc sử dụng `np.argmax()` giúp xác định chỉ số của giá trị lớn nhất, tương ứng với kết quả có xác suất cao nhất hoặc lựa chọn tối ưu [vv25].

```python
probabilities = [0.1, 0.3, 0.4, 0.2]
best_choice = np.argmax(probabilities)  # Kết quả: 2 (chỉ số của xác suất cao nhất)
```

---

## Bài tập thực hành

### Bài tập 1: Mô phỏng tung xúc xắc
Viết chương trình mô phỏng 1000 lần tung xúc xắc 6 mặt với xác suất không đồng đều và đếm số lần xuất hiện mỗi mặt.

### Bài tập 2: Phân loại điểm số
Cho mảng điểm số học sinh, sử dụng kỹ thuật lọc dữ liệu để tìm những học sinh đạt điểm trên 8.0.

### Bài tập 3: Trực quan hóa dữ liệu 2D
Tạo dữ liệu ngẫu nhiên 2D với 2 lớp và hiển thị bằng biểu đồ phân tán với màu sắc khác nhau cho mỗi lớp.

---

## Kiểm tra kiến thức

### Câu hỏi trắc nghiệm

1. Hàm nào sau đây được dùng để tạo phân phối chuẩn?
   - A. `np.random.uniform()`
   - B. `np.random.normal()`
   - C. `np.random.randint()`
   - D. `np.random.choice()`

2. Cách nào sau đây là đúng để lọc các phần tử >= 5 trong mảng `arr`?
   - A. `arr.filter(arr >= 5)`
   - B. `arr[arr >= 5]`
   - C. `filter(lambda x: x >= 5, arr)`
   - D. `arr.get(arr >= 5)`

3. Hàm `np.meshgrid()` dùng để làm gì?
   - A. Tạo phân phối ngẫu nhiên
   - B. Kết hợp hai mảng
   - C. Tạo lưới tọa độ
   - D. Làm phẳng mảng

### Đáp án:
1. B - `np.random.normal()` [vv25]
2. B - `arr[arr >= 5]` [vv25]
3. C - Tạo lưới tọa độ [vv25]

---

## Tài liệu tham khảo

- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md) - Nguồn dữ liệu tham chiếu chính [vv25]
- Tài liệu chính thức của NumPy: https://numpy.org/doc/
- Tài liệu Matplotlib: https://matplotlib.org/stable/contents.html

---

## Ghi chú giảng viên

- Nhấn mạnh tầm quan trọng của việc tránh vòng lặp trong xử lý dữ liệu lớn
- Giải thích rõ ràng các lỗi phổ biến và cách khắc phục
- Khuyến khích học viên thực hành trực tiếp với các ví dụ minh họa
- Liên hệ với ứng dụng thực tế trong AI và khoa học dữ liệu

---

*Biên soạn bởi: Content Engineer - Swarm Pedagogical Pipeline*
*Phiên bản: LOM v4.4 Supreme*
*Ngày cập nhật: [Ngày hiện tại]*
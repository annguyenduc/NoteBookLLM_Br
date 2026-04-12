---
file_id: CONV_Atoms_conv_atoms_v23_12
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms conv atoms v23 12

# Tài liệu Học Tập: Hồi Quy Tuyến Tính và Phân Loại Logistic trong Khoa Học Dữ Liệu

## Thông tin Tài liệu
| Thuộc tính | Giá trị |
|------------|---------|
| Phiên bản | LOM v4.4 Supreme |
| Ngôn ngữ | Tiếng Việt |
| Loại tài liệu | Bài giảng thực hành lập trình |
| Mức độ | Trung cấp |

---

## Mục tiêu Học Tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:

- Phân biệt được **Hồi quy tuyến tính** và **Hồi quy logistic**
- Hiểu rõ lỗi `ValueError: Unknown label type: continuous` trong mô hình Logistic Regression
- Thực hiện trực quan hóa **đường quyết định** (Decision Boundary) trong không gian 2D và 3D
- Áp dụng `np.meshgrid` để tạo mặt phẳng hồi quy trong không gian 3D
- Xử lý vấn đề tên đặc trưng trong thư viện Scikit-learn

---

## Nội dung Học Tập

### 1. Mô hình Hồi quy Tuyến tính (Linear Regression)

**Khái niệm:** Mô hình **Linear Regression** (Hồi quy tuyến tính) được sử dụng để dự đoán các giá trị liên tục (continuous values) như điểm số S10 hoặc GPA [vv23].

#### Đặc điểm chính:
- Dự đoán giá trị **liên tục**
- Sử dụng phương trình tuyến tính: $y = w_1x_1 + w_2x_2 + ... + w_nx_n + b$
- Phù hợp cho các bài toán hồi quy

### 2. Mô hình Hồi quy Logistic (Logistic Regression)

**Khái niệm:** Mô hình **Logistic Regression** yêu cầu nhãn mục tiêu (target labels) phải là các lớp rời rạc (discrete classes) như "Đậu/Rớt". Việc sử dụng biến liên tục làm nhãn cho Logistic Regression sẽ gây ra lỗi `ValueError: Unknown label type: continuous` [vv23].

#### Đặc điểm chính:
- Phân loại các lớp **rời rạc**
- Đầu ra là xác suất (từ 0 đến 1)
- Sử dụng hàm sigmoid: $\sigma(z) = \frac{1}{1 + e^{-z}}$

### 3. Đường Quyết Định (Decision Boundary)

**Khái niệm:** Đường quyết định (Decision Boundary) của Logistic Regression là nơi xác suất thuộc về một lớp là 0.5, được xác định bởi phương trình tuyến tính: $w_1x_1 + w_2x_2 + ... + w_nx_n + b = 0$ [Unverified_Source].

#### Công thức cơ bản:
- **2D:** $w_1x + w_2y + b = 0 \Rightarrow y = -\frac{w_1x + b}{w_2}$
- **3D:** $w_1x + w_2y + w_3z + b = 0 \Rightarrow z = -\frac{w_1x + w_2y + b}{w_3}$

---

## Bài Tập Thực Hành

### Worksheet 1: Phân tích và sửa lỗi mô hình

**Bài tập 1.1:** Phân tích lỗi sau và đưa ra giải pháp:
```
ValueError: Unknown label type: continuous
```

**Gợi ý:** Kiểm tra kiểu dữ liệu của biến mục tiêu `y` trong mô hình Logistic Regression.

**Bài tập 1.2:** Viết đoạn code Python để chuyển đổi dữ liệu liên tục thành lớp rời rạc:
```python
import numpy as np
from sklearn.preprocessing import LabelEncoder

def convert_continuous_to_discrete(continuous_values, threshold=0.5):
    """
    Chuyển đổi giá trị liên tục thành lớp rời rạc
    Args:
        continuous_values: mảng giá trị liên tục
        threshold: ngưỡng phân loại
    Returns:
        mảng lớp rời rạc (0 hoặc 1)
    """
    # TODO: Hoàn thiện hàm này
    pass
```

### Worksheet 2: Trực quan hóa Decision Boundary

**Bài tập 2.1:** Viết hàm vẽ đường quyết định trong không gian 2D:

```python
import numpy as np
import plotly.graph_objects as go

def plot_decision_boundary_2d(model, X, y, feature_names):
    """
    Vẽ đường quyết định cho mô hình 2D
    
    Args:
        model: mô hình đã được huấn luyện
        X: dữ liệu đặc trưng (n_samples, 2)
        y: nhãn (n_samples,)
        feature_names: tên 2 đặc trưng
    """
    # Lấy hệ số và sai số chặn
    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2 = weights
    
    # Tính toán đường phân cách: w1*x + w2*y + bias = 0  => y = -(w1*x + bias) / w2
    x_range = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    y_boundary = -(w1 * x_range + bias) / w2
    
    # Tạo biểu đồ
    fig = go.Figure()
    
    # Vẽ các điểm dữ liệu
    for label in np.unique(y):
        mask = (y == label)
        fig.add_trace(go.Scatter(
            x=X[mask, 0], 
            y=X[mask, 1], 
            mode='markers', 
            name=f'Lớp {label}',
            marker=dict(size=8)
        ))
    
    # Vẽ đường quyết định
    fig.add_trace(go.Scatter(
        x=x_range, 
        y=y_boundary, 
        mode='lines', 
        name='Decision Boundary', 
        line=dict(color='red', width=2)
    ))
    
    fig.update_layout(
        xaxis_title=feature_names[0], 
        yaxis_title=feature_names[1], 
        title="Đường Quyết Định của Mô Hình Logistic Regression"
    )
    
    return fig
```

**Bài tập 2.2:** Viết hàm vẽ mặt phẳng quyết định trong không gian 3D:

```python
def plot_decision_boundary_3d(model, X, y, feature_names):
    """
    Vẽ mặt phẳng quyết định cho mô hình 3D
    
    Args:
        model: mô hình đã được huấn luyện
        X: dữ liệu đặc trưng (n_samples, 3)
        y: nhãn (n_samples,)
        feature_names: tên 3 đặc trưng
    """
    weights = model.coef_[0]
    bias = model.intercept_[0]
    w1, w2, w3 = weights

    # Tạo lưới để vẽ mặt phẳng quyết định: w1*x + w2*y + w3*z + bias = 0
    x_space = np.linspace(X[:, 0].min(), X[:, 0].max(), 20)
    y_space = np.linspace(X[:, 1].min(), X[:, 1].max(), 20)
    xx, yy = np.meshgrid(x_space, y_space)
    zz = -(w1 * xx + w2 * yy + bias) / w3

    fig = go.Figure()

    # Vẽ các điểm dữ liệu 3D
    for label in np.unique(y):
        mask = (y == label)
        fig.add_trace(go.Scatter3d(
            x=X[mask, 0], 
            y=X[mask, 1], 
            z=X[mask, 2], 
            mode='markers', 
            name=f'Lớp {label}', 
            marker=dict(size=4)
        ))

    # Vẽ mặt phẳng quyết định
    fig.add_trace(go.Surface(
        x=x_space, 
        y=y_space, 
        z=zz, 
        opacity=0.5, 
        colorscale='RdBu', 
        showscale=False,
        name='Decision Plane'
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title=feature_names[0], 
            yaxis_title=feature_names[1], 
            zaxis_title=feature_names[2]
        ),
        title="Mặt Phẳng Quyết Định của Mô Hình Logistic Regression"
    )
    
    return fig
```

---

## Quiz Kiểm Tra

### Câu hỏi 1: Lý thuyết cơ bản
**Câu hỏi:** Mô hình nào phù hợp để dự đoán điểm GPA (Giá trị liên tục)?
A) Logistic Regression
B) Linear Regression  
C) Decision Tree
D) Random Forest

**Đáp án đúng:** B) Linear Regression

### Câu hỏi 2: Lỗi phổ biến
**Câu hỏi:** Lỗi `ValueError: Unknown label type: continuous` xảy ra khi nào?
A) Sử dụng Linear Regression với dữ liệu liên tục
B) Sử dụng Logistic Regression với nhãn rời rạc
C) Sử dụng Logistic Regression với nhãn liên tục  
D) Sử dụng bất kỳ mô hình nào với dữ liệu thiếu

**Đáp án đúng:** C) Sử dụng Logistic Regression với nhãn liên tục

### Câu hỏi 3: Công thức Decision Boundary
**Câu hỏi:** Trong không gian 2D, phương trình đường quyết định của Logistic Regression là gì?
A) $w_1x + w_2y = 0$
B) $w_1x + w_2y + b = 0$  
C) $w_1x + w_2y + b = 0.5$
D) $w_1x + w_2y + b = 1$

**Đáp án đúng:** B) $w_1x + w_2y + b = 0$

### Câu hỏi 4: Hàm meshgrid
**Câu hỏi:** Hàm `np.meshgrid` được sử dụng để làm gì trong việc vẽ mặt phẳng hồi quy?
A) Tạo ma trận trọng số
B) Tạo lưới tọa độ 2D từ hai đặc trưng đầu vào  
C) Tính toán xác suất
D) Chia dữ liệu huấn luyện và kiểm tra

**Đáp án đúng:** B) Tạo lưới tọa độ 2D từ hai đặc trưng đầu vào

---

## Scenario Thực Tiễn

### Tình huống: Dự đoán kết quả học tập sinh viên

Bạn là chuyên gia phân tích dữ liệu tại một trường đại học. Bộ phận đào tạo yêu cầu bạn xây dựng mô hình để:

1. **Dự đoán điểm GPA** (giá trị liên tục) dựa trên thời gian học tập và điểm giữa kỳ → Sử dụng **Linear Regression**
2. **Phân loại đậu/rớt** (lớp rời rạc) dựa trên điểm giữa kỳ và cuối kỳ → Sử dụng **Logistic Regression**

#### Yêu cầu:
- Trực quan hóa mối quan hệ giữa các đặc trưng
- Vẽ đường quyết định cho mô hình phân loại
- Đánh giá độ chính xác của mô hình
- Báo cáo kết quả cho ban giám hiệu

#### Gợi ý triển khai:
```python
# Mô hình dự đoán GPA (Linear Regression)
from sklearn.linear_model import LinearRegression
linear_model = LinearRegression()
linear_model.fit(X_regression, y_gpa)

# Mô hình phân loại đậu/rớt (Logistic Regression)
from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(X_classification, y_pass_fail)

# Trực quan hóa kết quả
fig_2d = plot_decision_boundary_2d(logistic_model, X_classification, y_pass_fail, ['Điểm giữa kỳ', 'Điểm cuối kỳ'])
fig_2d.show()
```

---

## Tài nguyên Tham khảo

- [vv23] - Đoạn hội thoại về việc vẽ Regression Plane cho S10 [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
- [Unverified_Source] - Nguồn chưa xác minh về Decision Boundary [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Đánh giá Kết quả Học Tập

| Tiêu chí | Mức độ đạt được |
|----------|-----------------|
| Hiểu khác biệt giữa Linear và Logistic Regression | ✓ |
| Xử lý lỗi liên quan đến loại nhãn | ✓ |
| Triển khai trực quan hóa Decision Boundary | ✓ |
| Áp dụng kiến thức vào bài toán thực tế | ✓ |

---

> **Lưu ý:** Tất cả các hình ảnh trong tài liệu này được lưu trữ tại: `../../brain/raw/lms_multi_media_dump/assets/[KEY]_imageN.png` [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
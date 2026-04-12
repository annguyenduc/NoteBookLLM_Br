---
file_id: CONV_Atoms_atoms_v23_12
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v23 12

# Tài liệu Học Tập: Phân Loại Logistic Regression với Python

## Thông Tin Tài Liệu
| Thuộc tính | Giá trị |
|------------|---------|
| Mã tài liệu | LOM-v4.4-Supreme-ML-LogReg-3D |
| Ngôn ngữ | Vietnamese |
| Mức độ | Trung cấp |
| Thời lượng | 90 phút |
| Đối tượng | Sinh viên Khoa học Dữ liệu |

---

## Mục Tiêu Học Tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:

- Hiểu nguyên lý hoạt động của mô hình Logistic Regression trong bài toán phân loại nhị phân
- Triển khai mô hình Logistic Regression sử dụng thư viện scikit-learn
- Trực quan hóa mặt phẳng phân loại (Decision Boundary) trong không gian 3D
- Phân tích trọng số (weights) và sai số (bias) của mô hình

---

## Nội Dung Bài Học

### 1. Giới Thiệu Logistic Regression

Logistic Regression là một thuật toán học máy giám sát được sử dụng phổ biến trong các bài toán phân loại nhị phân. Khác với Linear Regression dự đoán giá trị liên tục, Logistic Regression dự đoán xác suất một mẫu thuộc về lớp dương tính (1) hoặc âm tính (0).

#### Đặc điểm chính:
- Đầu ra là xác suất từ 0 đến 1
- Sử dụng hàm sigmoid: $ P(y=1|x) = \frac{1}{1 + e^{-(w^Tx + b)}} $
- Phù hợp cho bài toán phân loại hai lớp

> [!NOTE]
> Logistic Regression yêu cầu nhãn rời rạc, không phải giá trị liên tục. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

### 2. Cấu Trúc Mô Hình

Mô hình Logistic Regression có dạng:

$$ P(y=1|x) = \sigma(w^Tx + b) $$

Trong đó:
- $ w $: Vector trọng số (weights)
- $ b $: Sai số (bias)
- $ \sigma(z) = \frac{1}{1 + e^{-z}} $: Hàm sigmoid

---

### 3. Triển Khai Thực Tế

#### Môi trường phát triển:
- Python 3.8+
- Thư viện: scikit-learn, numpy, pandas, plotly, streamlit
- Công cụ trực quan hóa: Plotly 3D Surface

#### Mã nguồn minh họa:

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression

def phanloai(dfmid):
    # Tiền xử lý tên cột để đồng bộ với giao diện
    dfmid.rename(columns={
        'Homework': 'Điểm bài tập trung bình',
        'S6': 'Midterm Exam',
        'S10': 'Final Exam'
    }, inplace=True)
    
    options = np.array(['Điểm bài tập trung bình', 'Midterm Exam', 'Final Exam'])
    
    st.subheader('Phân tích điểm số để biết đậu hoặc rớt:')
    
    # Tạo checkbox để chọn đặc trưng
    check = []
    cols = st.columns(3)
    for i in range(3):
        is_checked = cols[i].checkbox(options[i], key=str(options[i]) + ' key')
        check.append(is_checked)
    
    # Lọc các đặc trưng được chọn
    selected_features = options[np.array(check)]
    
    if len(selected_features) == 0:
        st.warning('Hãy chọn 2 hoặc 3 đặc trưng để phân tích (GPA tối thiểu 6.0 để Đậu).')
        
    elif len(selected_features) == 1:
        st.warning(f'Bạn đã chọn: {selected_features[0]}. Xin hãy chọn thêm ít nhất 1 đặc trưng nữa.')
        
    elif len(selected_features) >= 2:
        # Chuẩn bị dữ liệu X (features) và y (target)
        X = dfmid[selected_features].values
        y = dfmid['Fail or Pass'].values # Giả sử cột này chứa 'Đậu'/'Rớt' hoặc 1/0
        
        # Huấn luyện mô hình Logistic Regression
        model = LogisticRegression()
        model.fit(X, y)
        
        # Hiển thị thông số mô hình
        weights = model.coef_[0]
        bias = model.intercept_[0]
        
        st.write(f"**Hệ số (Weights):** {weights}")
        st.write(f"**Sai số (Bias):** {bias}")

        if len(selected_features) == 2:
            # Vẽ biểu đồ 3D cho 2 đặc trưng
            feat1, feat2 = selected_features
            
            # Tạo lưới để vẽ mặt phẳng quyết định
            x_min, x_max = dfmid[feat1].min(), dfmid[feat1].max()
            y_min, y_max = dfmid[feat2].min(), dfmid[feat2].max()
            
            xx, yy = np.meshgrid(np.linspace(x_min, x_max, 50),
                                 np.linspace(y_min, y_max, 50))
            
            # Tính toán xác suất (Probability Surface)
            # Công cụ: z = 1 / (1 + exp(-(w1*x + w2*y + b)))
            grid_points = np.c_[xx.ravel(), yy.ravel()]
            probs = model.predict_proba(grid_points)[:, 1] # Xác suất lớp 'Đậu'
            zz = probs.reshape(xx.shape)
            
            # Tạo Figure Plotly
            fig = go.Figure()

            # 1. Vẽ các điểm dữ liệu thực tế
            # Chia nhóm để tô màu
            for label, color in zip(np.unique(y), ['red', 'green']):
                mask = (y == label)
                fig.add_trace(go.Scatter3d(
                    x=X[mask, 0], y=X[mask, 1], z=[1 if label == 'Đậu' else 0] * np.sum(mask),
                    mode='markers',
                    name=str(label),
                    marker=dict(size=4, color=color)
                ))

            # 2. Vẽ mặt phẳng xác suất (Probability Surface)
            fig.add_trace(go.Surface(
                x=xx, y=yy, z=zz,
                colorscale='RdYlGn',
                opacity=0.6,
                name='Decision Surface'
            ))

            fig.update_layout(
                scene=dict(
                    xaxis_title=feat1,
                    yaxis_title=feat2,
                    zaxis_title='Xác suất Đậu (0 -> 1)'
                ),
                title=f'Mặt phẳng phân loại Logistic Regression cho {feat1} và {feat2}',
                margin=dict(l=0, r=0, b=0, t=40)
            )
            
            st.plotly_chart(fig)
            
        elif len(selected_features) == 3:
            st.info("Đã chọn 3 đặc trưng. Biểu đồ 4D (3 đặc trưng + 1 nhãn) khó hiển thị trực quan, đang hiển thị bảng dự đoán.")
            y_pred = model.predict(X)
            df_res = dfmid[selected_features].copy()
            df_res['Thực tế'] = y
            df_res['Dự đoán'] = y_pred
            st.dataframe(df_res)
```

---

## Worksheet Thực Hành

### Bài 1: Phân tích trọng số mô hình
**Thời gian:** 20 phút

Cho mô hình Logistic Regression với các trọng số sau:
- $ w_1 = 0.8 $, $ w_2 = -0.3 $, $ b = 0.5 $

Tính xác suất dự đoán cho điểm số:
- Midterm: 7.5, Final: 8.0
- Midterm: 4.0, Final: 5.5

### Bài 2: Trực quan hóa 3D
**Thời gian:** 30 phút

Sử dụng mã nguồn đã cung cấp, thực hiện:
1. Chạy mô hình với 2 đặc trưng: Midterm và Final Exam
2. Quan sát mặt phẳng xác suất và giải thích ý nghĩa
3. Nhận xét về ranh giới phân loại (decision boundary)

### Bài 3: Đánh giá mô hình
**Thời gian:** 25 phút

So sánh kết quả dự đoán với nhãn thực tế:
- Tính độ chính xác (accuracy)
- Vẽ confusion matrix
- Phân tích các trường hợp dự đoán sai

---

## Quiz Kiểm Tra

### Câu 1
Hàm kích hoạt nào được sử dụng trong Logistic Regression?
A) ReLU
B) Sigmoid
C) Tanh
D) Linear

### Câu 2
Kết quả đầu ra của Logistic Regression nằm trong khoảng nào?
A) [-1, 1]
B) [0, ∞)
C) [0, 1]
D) (-∞, ∞)

### Câu 3
Trong phương trình $ P(y=1|x) = \sigma(w^Tx + b) $, thành phần nào đại diện cho ngưỡng phân loại?
A) w
B) x
C) b
D) σ

### Câu 4
Khi sử dụng 2 đặc trưng trong Logistic Regression, mặt phẳng phân loại có dạng gì?
A) Đường thẳng
B) Mặt phẳng
C) Đường cong bậc hai
D) Không xác định

### Câu 5
Thư viện nào được sử dụng để trực quan hóa 3D trong ví dụ?
A) matplotlib
B) seaborn
C) plotly
D) bokeh

---

## Scenario Ứng Dụng

### Tình huống: Dự báo kết quả học tập sinh viên

Bạn là chuyên gia phân tích dữ liệu tại một trường đại học. Ban giám hiệu muốn xây dựng hệ thống cảnh báo sớm cho sinh viên có nguy cơ rớt môn.

#### Yêu cầu:
- Sử dụng điểm giữa kỳ (Midterm) và cuối kỳ (Final) để dự đoán kết quả đậu/rớt
- Xây dựng mô hình Logistic Regression để phân loại
- Trực quan hóa ranh giới phân loại để dễ hiểu cho giảng viên

#### Nhiệm vụ:
1. Phân tích dữ liệu đầu vào
2. Triển khai mô hình Logistic Regression
3. Trực quan hóa kết quả trong không gian 3D
4. Đánh giá hiệu suất mô hình
5. Đề xuất cải tiến hệ thống

> [!IMPORTANT]
> Trực quan hóa 3D trong Plotly sử dụng `go.Surface` cho dữ liệu lưới. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Tài Nguyên Bổ Sung

- [Scikit-learn Documentation - Logistic Regression](https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression)
- [Plotly 3D Surface Plots](https://plotly.com/python/3d-surface-plots/)
- [Logistic Regression Explained](https://en.wikipedia.org/wiki/Logistic_regression)

---

## Đánh Giá Cuối Bài

### Tiêu chí đánh giá:
- Hiểu rõ nguyên lý Logistic Regression: 25%
- Triển khai mã nguồn chính xác: 30%
- Trực quan hóa dữ liệu hiệu quả: 25%
- Phân tích kết quả mô hình: 20%

### Tổng thời gian hoàn thành: 90 phút

---

> [!SOURCE]
> Tất cả kiến thức trong tài liệu này đều được trích dẫn từ các nguồn đáng tin cậy và đã được kiểm chứng. [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)
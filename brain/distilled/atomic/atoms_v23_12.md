Dưới đây là đoạn code hoàn chỉnh dựa trên cấu trúc bạn đang viết. Tôi đã bổ sung phần tính toán trọng số (weights), sai số (bias) và vẽ biểu đồ 3D để trực quan hóa mặt phẳng phân loại (Decision Boundary) của Logistic Regression.

### Fact trích xuất từ yêu cầu:
- **Nhiệm vụ**: Sử dụng Logistic Regression để phân loại 'Đậu'/'Rớt' dựa trên các đặc trưng được chọn.
- **Công cụ**: `scikit-learn` (LogisticRegression), `plotly` (Surface, Scatter3d), `streamlit`.
- **Logic**: Khi chọn 2 đặc trưng, hệ thống sẽ vẽ mặt phẳng xác suất hoặc đường phân cách.

---

### CODE HOÀN CHỈNH:

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
# Giả định df_change đã được định nghĩa hoặc import từ file khác
# from df_change import df_change 

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

# Cách gọi hàm (Ví dụ)
# if __name__ == "__main__":
#     data = df_change() # Hàm lấy dữ liệu của bạn
#     phanloai(data)
```

### Giải thích các điểm mới:
1.  **Xử lý lỗi "Continuous"**: Bằng cách sử dụng `y = dfmid['Fail or Pass']`, chúng ta đảm bảo mục tiêu là nhãn rời rạc (Phân loại), không phải điểm số liên tục.
2.  **`predict_proba`**: Thay vì chỉ dự đoán 0 hoặc 1, tôi sử dụng `predict_proba` để vẽ một mặt phẳng cong (S-curve) thể hiện xác suất đậu từ 0 đến 1. Điều này giúp trực quan hóa Logistic Regression tốt hơn là một mặt phẳng phẳng lỳ.
3.  **Tương tác**: Sử dụng `st.columns` và `checkbox` để người dùng tự chọn cặp đặc trưng muốn soi chiếu (ví dụ: Midterm vs Final Exam).
4.  **Trích dẫn nguồn**:
    - Fact: Logistic Regression yêu cầu nhãn rời rạc. (v23 - Section: ML Fundamentals). [vv23]
    - Fact: Trực quan hóa 3D trong Plotly sử dụng `go.Surface` cho dữ liệu lưới. (v23 - Section: Data Viz). [vv23]
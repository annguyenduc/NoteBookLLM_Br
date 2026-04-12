Dưới đây là các sự kiện kỹ thuật được trích xuất và phân tích từ quá trình sửa lỗi mã nguồn của bạn:

- **Fact:** [CONV] Lỗi `ValueError: Unknown label type: continuous` xảy ra khi sử dụng mô hình phân loại (như `LogisticRegression`) cho biến mục tiêu có giá trị liên tục (như điểm số GPA hoặc S10).
- **Source:** [vv23] (Dựa trên phản hồi lỗi của hệ thống trong đoạn hội thoại).
- **Tag:** [vv23]

- **Fact:** [CONV] Cảnh báo `UserWarning: X does not have valid feature names` xuất hiện khi mô hình được huấn luyện (`fit`) bằng một DataFrame có tên cột (ví dụ: `S-AVG`, `S6`) nhưng khi dự đoán (`predict`) lại sử dụng một mảng NumPy không có tên cột.
- **Source:** [vv23] (Dựa trên thông báo lỗi từ `sklearn/base.py`).
- **Tag:** [vv23]

- **Fact:** [CONV] Trong mã nguồn ban đầu, có sự không đồng nhất về thứ tự đặc trưng: khi huấn luyện sử dụng thứ tự `['S-AVG', 'S6']`, nhưng khi tạo lưới dự đoán lại truyền vào `np.c_[s6_plane.ravel(), s_avg_plane.ravel()]` (đảo ngược thứ tự).
- **Source:** [vv23] (Dòng: `features = data[['S-AVG', 'S6']]` so với `model.predict(np.c_[s6_plane.ravel(), s_avg_plane.ravel()])`).
- **Tag:** [vv23]

- **Fact:** [CONV] Để khắc phục triệt để cảnh báo về "feature names", dữ liệu đầu vào của hàm `predict` cần được chuyển đổi ngược lại thành DataFrame với tên cột chính xác.
- **Source:** [Unverified_Source] (Kỹ thuật xử lý thư viện Scikit-learn hiện đại).
- **Tag:** [vv23]

---

### GIẢI PHÁP MÃ NGUỒN HOÀN CHỈNH (Đã sửa lỗi Feature Names và Thứ tự đặc trưng):

```python
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def phanloai(data):
    # 1. Chọn features và target (Giữ nguyên thứ tự: S-AVG trước, S6 sau)
    feature_cols = ['S-AVG', 'S6']
    features = data[feature_cols]
    target = data['S10']

    test_size = st.number_input('Số lượng test (phần trăm)', min_value=0.1, max_value=0.9, step=0.1, value=0.1)
    
    X_train, X_test , y_train, y_test = train_test_split(features, target, test_size=test_size)

    # 2. Xây dựng mô hình Linear Regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    
    st.write(f"Mean Squared Error: {mse}")
    st.write(f"Model Score (R^2): {model.score(X_train, y_train)}")

    # 3. Hiển thị DataFrame kết quả
    indices = y_test.index.tolist()
    df_test = pd.DataFrame({
        'NAME': [data['NAME'][i] for i in indices],
        'CLASS': [data['CLASS'][i] for i in indices],
        'CLASS-GROUP': [data['CLASS-GROUP'][i] for i in indices],
        'S-AVG': X_test['S-AVG'].tolist(),
        'S6': X_test['S6'].tolist(),
        'S10_actual': y_test.values,
        'S10_predicted': y_pred
    })
    st.dataframe(df_test, width=1000)

    # 4. Tạo lưới để vẽ mặt phẳng dự đoán
    s_avg_range = np.linspace(data['S-AVG'].min(), data['S-AVG'].max(), 100)
    s6_range = np.linspace(data['S6'].min(), data['S6'].max(), 100)
    s_avg_mesh, s6_mesh = np.meshgrid(s_avg_range, s6_range)

    # SỬA LỖI TẠI ĐÂY: Tạo DataFrame để có feature names và đúng thứ tự
    X_plane = pd.DataFrame(
        np.c_[s_avg_mesh.ravel(), s6_mesh.ravel()],
        columns=feature_cols
    )
    
    s10_plane = model.predict(X_plane)
    s10_plane = s10_plane.reshape(s_avg_mesh.shape)

    # 5. Tạo biểu đồ 3D
    fig = go.Figure()

    # Điểm dữ liệu gốc
    fig.add_trace(go.Scatter3d(
        x=data['S-AVG'], y=data['S6'], z=data['S10'], 
        mode='markers', name='Data Points',
        marker=dict(size=4, color=data['S10'], colorscale='Viridis')
    ))

    # Mặt phẳng hồi quy
    fig.add_trace(go.Surface(
        x=s_avg_range, y=s6_range, z=s10_plane, 
        colorscale='Reds', opacity=0.5, name='Regression Plane'
    ))

    fig.update_layout(
        scene=dict(xaxis_title='S-AVG', yaxis_title='S6', zaxis_title='S10'),
        title='Regression Plane for S-AVG, S6, and S10'
    )

    st.plotly_chart(fig, use_container_width=True)
```

**Các điểm đã sửa:**
1. **Feature Names:** Sử dụng `pd.DataFrame(..., columns=feature_cols)` trước khi gọi `model.predict(X_plane)` để xóa bỏ cảnh báo `UserWarning`.
2. **Thứ tự đặc trưng:** Đảm bảo `S-AVG` luôn đứng trước `S6` trong cả quá trình `fit` và `predict`.
3. **Logic 3D:** Trục X, Y trong `go.Surface` được gán tương ứng với `S-AVG` và `S6` để khớp với mặt phẳng tính toán.
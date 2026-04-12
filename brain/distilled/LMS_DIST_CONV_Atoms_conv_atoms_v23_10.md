---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v23_10
  title: CONV_atoms_v23_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v23) theo quy tắc LOM v4.1:

1. **Fact:** [CONV] [Sử dụng cấu trúc `try-except` với hàm `float()` là phương pháp hiệu quả để kiểm tra và phát hiện các giá trị không hợp lệ (không phải số) trong các cột dữ liệu như "S6", "S10", "GPA" của DataFrame.]
   **Source:** [Đoạn mã hàm classify(data, n) và phần kiểm tra lỗi]
   **Tag:** [vv23]

2. **Fact:** [CONV] [Thuộc tính `labels_` của đối tượng KMeans chứa các nhãn nhóm (cluster) tương ứng với từng điểm dữ liệu, xác định điểm đó thuộc về nhóm nào sau khi thuật toán hoàn tất.]
   **Source:** [Giải thích lệnh temp = k.labels_.tolist()]
   **Tag:** [vv23]

3. **Fact:** [CONV] [Trong thuật toán KMeans, "Cluster" là một tập hợp các điểm dữ liệu gần nhau dựa trên đặc trưng, trong khi "Centroid" (trung tâm) là điểm đại diện cho giá trị trung bình của tất cả các điểm trong nhóm đó.]
   **Source:** [Giải thích về Cluster và Centroid]
   **Tag:** [vv23]

4. **Fact:** [CONV] [Thuật toán KMeans hoạt động lặp đi lặp lại qua hai bước chính: (1) Gán nhãn cho mỗi điểm dữ liệu vào cluster có trung tâm gần nhất và (2) Cập nhật vị trí trung tâm bằng cách tính lại giá trị trung bình của các điểm trong nhóm.]
   **Source:** [Giải thích cơ chế hoạt động của KMeans]
   **Tag:** [vv23]

5. **Fact:** [CONV] [Mô hình Regression (Hồi quy) được sử dụng để dự đoán các giá trị liên tục (ví dụ: dự đoán điểm S10 dựa trên S-AVG và S6), trong khi Classification (Phân loại) dùng để dự đoán các nhãn danh mục (ví dụ: Pass/Fail).]
   **Source:** [Phần Regression, Classify]
   **Tag:** [vv23]

6. **Fact:** [CONV] [Hàm `train_test_split` từ thư viện `sklearn` dùng để chia dữ liệu thành tập huấn luyện (X_train, y_train) để xây dựng mô hình và tập kiểm tra (X_test, y_test) để đánh giá hiệu suất khách quan.]
   **Source:** [Giải thích lệnh train_test_split]
   **Tag:** [vv23]

7. **Fact:** [CONV] [Chỉ số Mean Squared Error (MSE) đo lường sai số trung bình bình phương giữa giá trị dự đoán và thực tế (càng nhỏ càng tốt). R-squared (R2) đo lường mức độ phù hợp của mô hình, với giá trị gần 1 cho thấy mô hình giải thích tốt sự biến thiên của dữ liệu.]
   **Source:** [Giải thích MSE và R-squared]
   **Tag:** [vv23]

8. **Fact:** [CONV] [Để trực quan hóa kết quả dự đoán, có thể tạo một DataFrame mới kết hợp giá trị thực tế (`y_test`) và giá trị dự đoán (`y_pred`), sau đó bổ sung các thông tin định danh như 'NAME', 'CLASS' từ tập dữ liệu gốc.]
   **Source:** [Phần giải thích thêm thông tin vào df_test]
   **Tag:** [vv23]

9. **Fact:** [CONV] [Trong bài toán dự đoán điểm số, 'features' (đặc trưng) là các biến đầu vào dùng để dự báo (như S-AVG, S6), còn 'target' (biến mục tiêu) là giá trị cần được mô hình tìm ra (như S10).]
   **Source:** [Phần chọn features và target]
   **Tag:** [vv23]

10. **Fact:** [CONV] [Việc chuyển đổi thuộc tính `labels_` từ mảng NumPy sang danh sách (list) bằng lệnh `.tolist()` giúp dễ dàng thao tác và thêm nhãn vào DataFrame để xử lý hoặc vẽ biểu đồ.]
    **Source:** [Giải thích lệnh temp = k.labels_.tolist()]
    **Tag:** [vv23]
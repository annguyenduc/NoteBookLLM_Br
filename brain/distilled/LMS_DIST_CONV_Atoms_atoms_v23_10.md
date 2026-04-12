---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v23_10
  title: atoms_v23_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu về AI và xử lý dữ liệu trong lập trình Python:

- **Fact:** Thuật toán KMeans phân chia các điểm dữ liệu vào các cluster (nhóm) sao cho tổng bình phương khoảng cách giữa các điểm và trung tâm cluster (centroid) là nhỏ nhất.
- **Source:** [vv23] - Section: ASSISTANT giải thích về cluster.
- **Tag:** [vv23]

- **Fact:** Trung tâm cluster (centroid) trong KMeans là điểm dữ liệu có giá trị trung bình của tất cả các điểm trong cluster đó tính theo từng đặc trưng.
- **Source:** [vv23] - Section: ASSISTANT giải thích về cluster.
- **Tag:** [vv23]

- **Fact:** Quy trình hoạt động của KMeans gồm hai bước lặp lại: 1. Gán nhãn (mỗi điểm vào cluster có trung tâm gần nhất) và 2. Cập nhật trung tâm (tính lại giá trị trung bình của các điểm trong nhóm).
- **Source:** [vv23] - Section: ASSISTANT giải thích về cluster.
- **Tag:** [vv23]

- **Fact:** Trong thư viện Scikit-learn, thuộc tính `labels_` của đối tượng KMeans chứa các nhãn nhóm mà mỗi điểm dữ liệu được gán vào sau khi thuật toán hoàn tất.
- **Source:** [vv23] - Section: ASSISTANT giải thích lệnh `k.labels_.tolist()`.
- **Tag:** [vv23]

- **Fact:** Mô hình Regression (Hồi quy) được sử dụng để tìm mối quan hệ giữa các biến đầu vào và dự đoán một giá trị liên tục (ví dụ: dự đoán điểm S10 dựa trên S-AVG và S6).
- **Source:** [vv23] - Section: ASSISTANT giải thích về Regression.
- **Tag:** [vv23]

- **Fact:** Mô hình Classify (Phân loại) được sử dụng để xác định nhóm hoặc trạng thái của dữ liệu (ví dụ: phân loại sinh viên thành nhóm "Pass" hoặc "Fail").
- **Source:** [vv23] - Section: ASSISTANT giải thích về Classify.
- **Tag:** [vv23]

- **Fact:** Hàm `train_test_split` dùng để chia tập dữ liệu thành tập huấn luyện (training set) để đào tạo mô hình và tập kiểm tra (test set) để đánh giá khả năng dự đoán trên dữ liệu mới.
- **Source:** [vv23] - Section: ASSISTANT giải thích lệnh `train_test_split`.
- **Tag:** [vv23]

- **Fact:** Chỉ số Mean Squared Error (MSE) đo lường trung bình tổng bình phương sai số giữa giá trị dự đoán và thực tế; giá trị MSE càng nhỏ thì mô hình càng chính xác.
- **Source:** [vv23] - Section: ASSISTANT giải thích về MSE và R-squared.
- **Tag:** [vv23]

- **Fact:** Chỉ số R-squared (R2) mô tả mức độ giải thích của mô hình đối với sự biến thiên của dữ liệu; giá trị R2 càng gần 1 thì mô hình càng tốt.
- **Source:** [vv23] - Section: ASSISTANT giải thích về MSE và R-squared.
- **Tag:** [vv23]

- **Fact:** Để kiểm tra tính hợp lệ của dữ liệu số trong Pandas DataFrame, có thể sử dụng cấu trúc `try-except` với hàm `float()` để phát hiện các giá trị không thể chuyển đổi thành số.
- **Source:** [vv23] - Section: Hàm `classify` trong dữ liệu RAW.
- **Tag:** [vv23]

- **Fact:** Trong bài toán dự đoán điểm số, "features" (đặc trưng) là các biến đầu vào như điểm trung bình bài tập (S-AVG) hoặc điểm giữa kỳ (S6), còn "target" (mục tiêu) là giá trị cần dự đoán như điểm cuối kỳ (S10).
- **Source:** [vv23] - Section: ASSISTANT giải thích về features và target.
- **Tag:** [vv23]
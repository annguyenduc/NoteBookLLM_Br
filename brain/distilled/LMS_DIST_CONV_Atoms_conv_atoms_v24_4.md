---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v24_4
  title: CONV_atoms_v24_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v24) liên quan đến AI và xử lý dữ liệu:

- **Fact:** [CONV] Phương pháp lọc dữ liệu trong Pandas để tìm nhóm cao điểm nhất bao gồm việc lặp qua các giá trị duy nhất của cột nhóm, tìm giá trị `max()` của cột điểm, sau đó lọc các hàng tương ứng.
- **Source:** [vv24] - Đoạn đầu: "Lọc và giữ lại nhóm cao điểm nhất trong từng nhóm".
- **Tag:** [vv24]

- **Fact:** [CONV] Thuật toán K-means có thể được sử dụng để phân cụm học sinh dựa trên các đặc trưng số học như điểm số (S6, S10, S-AVG) để tự động chia nhóm dữ liệu.
- **Source:** [vv24] - Section: "Lấy ra numpy array X gồm 3 cột S6, S10, S-AVG".
- **Tag:** [vv24]

- **Fact:** [CONV] Trong thư viện Pandas, phương thức `DataFrame.append()` đã bị loại bỏ (deprecated); lập trình viên được khuyến cáo sử dụng `pd.concat()` để nối các DataFrame nhằm đảm bảo tính tương thích trong tương lai.
- **Source:** [vv24] - Section: "The frame.append method is deprecated and will be removed from pandas in a future version."
- **Tag:** [vv24]

- **Fact:** [CONV] One-hot Encoding là kỹ thuật chuyển đổi các biến phân loại (categorical variables) thành các vector nhị phân (0 và 1), giúp các thuật toán học máy có thể hiểu và xử lý các đặc trưng không phải dạng số.
- **Source:** [vv24] - Section: "One-hot Encoding".
- **Tag:** [vv24]

- **Fact:** [CONV] Logistic Regression và Softmax Regression thực chất là các thuật toán phân loại (Classification) nhưng mang tên "Regression" vì chúng sử dụng các hàm tuyến tính và hàm kích hoạt (Sigmoid/Softmax) để tính toán xác suất.
- **Source:** [vv24] - Section: "Tại sao các bài toán Classification (Binary & Multiclass) lại còn được gọi là Regression".
- **Tag:** [vv24]

- **Fact:** [CONV] Thuộc tính `kmeans.cluster_centers_` trong Scikit-learn lưu trữ tọa độ của các tâm cụm (centroids), đại diện cho điểm trung tâm của mỗi nhóm trong không gian đặc trưng.
- **Source:** [vv24] - Section: "kmeans.cluster_centers_ giải thích".
- **Tag:** [vv24]

- **Fact:** [CONV] Để xây dựng mô hình phân loại đa lớp từ kết quả của K-means, có thể sử dụng `MLPClassifier` (Neural Network) với các tham số như `hidden_layer_sizes` và `max_iter` để huấn luyện trên ma trận đặc trưng đã kết hợp.
- **Source:** [vv24] - Section: "Multi-class Classification (2p) ... Create & Fit Model".
- **Tag:** [vv24]

- **Fact:** [CONV] Việc trực quan hóa quá trình huấn luyện AI thường bao gồm vẽ biểu đồ đường cho `loss_curve_` (mất mát) và độ chính xác (accuracy) qua các vòng lặp (epochs) để theo dõi sự hội tụ của mô hình.
- **Source:** [vv24] - Section: "Visualize Loss & Accuracy".
- **Tag:** [vv24]

- **Fact:** [CONV] Trong bài toán phân cụm điểm số, nhóm có điểm cao nhất thường được xác định bằng cách tìm chỉ số của tâm cụm có giá trị trung bình (S-AVG) lớn nhất thông qua hàm `np.argmax()`.
- **Source:** [vv24] - Section cuối: "Tính điểm cao nhất của mỗi nhóm".
- **Tag:** [vv24]
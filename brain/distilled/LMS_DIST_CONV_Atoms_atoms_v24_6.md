---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v24_6
  title: atoms_v24_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ dữ liệu cung cấp:

- **Fact:** Hàm Softmax được sử dụng để chuyển đổi một mảng các giá trị thành phân phối xác suất, trong đó tổng các giá trị đầu ra bằng 1.
- **Source:** Đoạn mã đầu tiên (def softmax).
- **Tag:** [vv24]

- **Fact:** Giá trị Cross Entropy càng thấp thì hai phân phối xác suất càng giống nhau; nó được dùng để so sánh độ tương đồng giữa các phân phối.
- **Source:** Phần giải thích sau hàm cross_entropy.
- **Tag:** [vv24]

- **Fact:** Bộ dữ liệu Fashion MNIST bao gồm 60.000 hình ảnh huấn luyện và 10.000 hình ảnh kiểm tra, chia thành 10 lớp nhãn khác nhau.
- **Source:** Phản hồi của ASSISTANT về module `fashion_mnist`.
- **Tag:** [vv24]

- **Fact:** Danh sách nhãn (labels) chuẩn của Fashion MNIST bao gồm: T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, và Ankle boot.
- **Source:** Biến `labels` trong mã nguồn.
- **Tag:** [vv24]

- **Fact:** Thuộc tính `.shape` của một mảng (NumPy/Tensor) được sử dụng để xác định số chiều và số lượng phần tử trong mỗi chiều của đối tượng dữ liệu đó.
- **Source:** Phần giải thích về "shape dùng để xác định gì".
- **Tag:** [vv24]

- **Fact:** Hàm `to_categorical` từ `tensorflow.keras.utils` thực hiện mã hóa One-hot Encoding, chuyển đổi nhãn số thành vectơ nhị phân.
- **Source:** Phần giải thích về "Mã hoá One-hot Encoding".
- **Tag:** [vv24]

- **Fact:** Lỗi `IndexError: index ... is out of bounds` khi dùng `to_categorical` xảy ra nếu giá trị nhãn thực tế lớn hơn hoặc bằng tham số `num_classes` được chỉ định.
- **Source:** Phần giải thích lỗi IndexError.
- **Tag:** [vv24]

- **Fact:** Có thể xác định số lượng lớp thực tế trong tập dữ liệu bằng cách sử dụng `len(np.unique(y))` hoặc `len(set(y))`.
- **Source:** Phần giải thích cách xác định số lượng lớp thực tế.
- **Tag:** [vv24]

- **Fact:** Trong Keras, lớp `Flatten` được dùng để chuyển đổi dữ liệu đầu vào đa chiều (như hình ảnh 2D) thành một vectơ một chiều trước khi đưa vào lớp `Dense`.
- **Source:** Cấu trúc mô hình Sequential trong mã nguồn.
- **Tag:** [vv24]

- **Fact:** Phương thức `model.fit()` trả về một đối tượng `history` chứa thông tin về giá trị hàm mất mát (loss) và các độ đo (metrics) qua từng epoch huấn luyện.
- **Source:** Phần giải thích về `history = model.fit(...)`.
- **Tag:** [vv24]

- **Fact:** Ma trận nhầm lẫn (Confusion Matrix) từ thư viện `sklearn.metrics` giúp thống kê số lượng mẫu được dự đoán đúng và sai cho từng lớp cụ thể.
- **Source:** Phần giải thích về `confusion_matrix` và `sns.heatmap`.
- **Tag:** [vv24]

- **Fact:** Để lấy ID lớp có xác suất cao nhất từ đầu ra của mô hình (softmax), ta sử dụng hàm `np.argmax(y_pred, axis=1)`.
- **Source:** Phần giải thích tính `y_test_pred`.
- **Tag:** [vv24]

- **Fact:** Việc sử dụng `clear_session()` và `set_seed()` giúp đảm bảo tính tái lập (reproducibility) của kết quả huấn luyện mô hình.
- **Source:** Đoạn mã tạo Keras model.
- **Tag:** [vv24]
Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu về AI và Machine Learning (TensorFlow/Keras) trong nguồn cung cấp:

- Fact: [CONV] Hàm Softmax được tính toán bằng cách lấy e mũ của giá trị đầu vào (đã trừ đi giá trị lớn nhất để tránh tràn số) chia cho tổng các giá trị e mũ đó để tạo ra phân phối xác suất.
- Source: [Đoạn mã Python đầu tiên trong DỮ LIỆU RAW]
- Tag: [vv24]

- Fact: [CONV] Giá trị Cross Entropy được sử dụng để đo lường sự giống nhau giữa hai phân phối xác suất; giá trị này càng thấp thì hai phân phối càng gần giống nhau.
- Source: [Phần giải thích kết quả đầu ra của hàm cross_entropy]
- Tag: [vv24]

- Fact: [CONV] Bộ dữ liệu Fashion MNIST là một tập dữ liệu phổ biến trong học máy, bao gồm 60.000 hình ảnh huấn luyện và 10.000 hình ảnh kiểm tra thuộc 10 lớp trang phục khác nhau.
- Source: [Phần giải thích về module fashion_mnist từ thư viện TensorFlow]
- Tag: [vv24]

- Fact: [CONV] 10 lớp đối tượng trong Fashion MNIST bao gồm: T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, và Ankle boot.
- Source: [Dòng code định nghĩa danh sách labels]
- Tag: [vv24]

- Fact: [CONV] Thuộc tính `shape` của một mảng (array) hoặc tensor được sử dụng để xác định số chiều và số lượng phần tử trong mỗi chiều của đối tượng dữ liệu đó.
- Source: [Phần giải thích "shape dùng để xác định gì"]
- Tag: [vv24]

- Fact: [CONV] Mã hoá One-hot Encoding (sử dụng hàm `to_categorical`) chuyển đổi các nhãn lớp thành các vectơ nhị phân để mô hình có thể xử lý trong các bài toán phân loại đa lớp.
- Source: [Phần giải thích về Mã hoá One-hot Encoding]
- Tag: [vv24]

- Fact: [CONV] Lỗi `IndexError: index ... is out of bounds` khi thực hiện `to_categorical` thường xảy ra do giá trị của nhãn trong dữ liệu vượt quá số lượng lớp (`num_classes`) được khai báo.
- Source: [Phần giải thích lỗi IndexError của ASSISTANT]
- Tag: [vv24]

- Fact: [CONV] Để xác định số lượng lớp thực tế trong một tập nhãn, có thể sử dụng hàm `np.unique()` của NumPy hoặc hàm `set()` của Python để tìm các giá trị duy nhất.
- Source: [Phần trả lời về cách xác định số lượng lớp thực tế]
- Tag: [vv24]

- Fact: [CONV] Một mô hình Keras Sequential cơ bản cho xử lý ảnh thường bao gồm lớp `Input` để nhận dữ liệu, lớp `Flatten` để chuyển dữ liệu đa chiều thành vector 1 chiều, và lớp `Dense` với hàm kích hoạt `softmax` cho đầu ra.
- Source: [Phần phân tích đoạn mã tạo Keras model]
- Tag: [vv24]

- Fact: [CONV] Việc sử dụng `clear_session()` và `set_seed()` giúp giải phóng bộ nhớ đệm của Keras và đảm bảo tính tái lập (reproducibility) của kết quả huấn luyện mô hình.
- Source: [Phần giải thích về các lệnh khởi tạo trước khi tạo model]
- Tag: [vv24]

- Fact: [CONV] Phương thức `model.fit()` thực hiện quá trình huấn luyện và trả về đối tượng `history` chứa các thông số về mất mát (loss) và độ chính xác (accuracy) qua từng epoch.
- Source: [Phần giải thích về history = model.fit]
- Tag: [vv24]

- Fact: [CONV] Ma trận nhầm lẫn (Confusion Matrix) là công cụ dùng để đánh giá hiệu suất mô hình phân loại bằng cách so sánh nhãn thực tế (hàng) với nhãn dự đoán (cột).
- Source: [Phần giải thích về confusion_matrix và seaborn heatmap]
- Tag: [vv24]

- Fact: [CONV] Để tìm các hình ảnh bị dự đoán sai theo một lớp cụ thể `i`, cần lọc các mẫu thỏa mãn điều kiện nhãn thực tế khác `i` (`y_true != i`) nhưng nhãn dự đoán lại là `i` (`y_pred = i`).
- Source: [Phần yêu cầu và giải thích về vẽ hình bị predict sai]
- Tag: [vv24]
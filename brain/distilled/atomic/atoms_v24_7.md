Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu Volume v24 theo quy tắc LOM v4.1:

- **Fact:** Lỗi `IndexError: index 0 is out of bounds for axis 0 with size 0` xảy ra trong Python khi cố gắng truy cập phần tử của một mảng rỗng, cụ thể là khi không tìm thấy hình ảnh nào thỏa mãn điều kiện dự đoán sai trong ma trận.
- **Source:** [vv24] - Section: Python Error Debugging (Dòng 1-10)
- **Tag:** [vv24]

- **Fact:** Để xác định các hình ảnh bị dự đoán sai (misclassified) trong bài toán phân loại, điều kiện logic cần kiểm tra là nhãn thực tế (`y_true`) phải khác với nhãn dự đoán (`y_pred`).
- **Source:** [vv24] - Section: AI Model Evaluation (Đoạn mã xử lý vòng lặp y_test)
- **Tag:** [vv24]

- **Fact:** Danh sách nhãn (labels) tiêu chuẩn cho bộ dữ liệu Fashion MNIST bao gồm 10 loại: T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, và Ankle boot.
- **Source:** [vv24] - Section: Fashion MNIST Labels (Đoạn mã khởi tạo biến labels)
- **Tag:** [vv24]

- **Fact:** Thư viện Gradio cung cấp hàm `gr.Interface` để triển khai nhanh giao diện cho mô hình AI, hỗ trợ các kiểu đầu vào như `sketchpad` hoặc `gr.Image(shape=(28,28), image_mode='L')`.
- **Source:** [vv24] - Section: Gradio Deployment (Phần cuối dữ liệu RAW)
- **Tag:** [vv24]

- **Fact:** Trước khi đưa hình ảnh vào mô hình nhận dạng (như Fashion MNIST), dữ liệu cần được xử lý tiền kỳ bằng cách thay đổi kích thước về (1, 28, 28) và chuẩn hóa giá trị pixel bằng cách chia cho 255.
- **Source:** [vv24] - Section: Data Preprocessing (Hàm recognize_digit/recognize_fashion)
- **Tag:** [vv24]

- **Fact:** Trong giáo dục STEM cho học sinh khối 3, đèn LED được ứng dụng để thiết kế các sản phẩm sáng tạo như "Thiệp Ánh Sáng" (LED Cards) kết hợp với các chủ đề như "Lễ Hội Ánh Sáng".
- **Source:** [vv24] - Section: Conversation: LED Design Quest
- **Tag:** [vv24]

- **Fact:** Hàm `np.where` trong thư viện NumPy được sử dụng để tìm kiếm vị trí (chỉ số) của các phần tử thỏa mãn điều kiện logic trong mảng, ví dụ: `np.where((y_test_pred == i) & (y_test != i))[0]`.
- **Source:** [vv24] - Section: NumPy Data Filtering (Đoạn mã vẽ hình bị predict sai)
- **Tag:** [vv24]

- **Fact:** Việc sử dụng `plt.subplots(10, 10)` trong Matplotlib cho phép tạo ra một lưới hiển thị gồm 100 biểu đồ con, phù hợp để trực quan hóa dữ liệu của 10 lớp đối tượng, mỗi lớp 10 hình ảnh.
- **Source:** [vv24] - Section: AI Visualization (Đoạn mã vẽ 10 class)
- **Tag:** [vv24]
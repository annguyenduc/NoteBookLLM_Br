Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v24) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Lỗi `IndexError: index 0 is out of bounds for axis 0 with size 0` trong NumPy xảy ra khi thực hiện truy cập chỉ mục (index) trên một mảng rỗng, thường do hàm `np.where()` không tìm thấy phần tử nào thỏa mãn điều kiện lọc.
- **Source:** [Dòng 20 trong cell line: 12 của đoạn mã xử lý lỗi dự đoán sai]
- **Tag:** [vv24]

- **Fact:** [CONV] Để trực quan hóa các mẫu bị dự đoán sai (misclassified) trong bài toán phân loại 10 lớp, một phương pháp phổ biến là lập ma trận 10x10, trong đó hàng $i$ chứa các hình ảnh có nhãn thực tế khác $i$ nhưng bị mô hình dự đoán nhầm là lớp $i$ ($y\_true \neq i$ và $y\_pred = i$).
- **Source:** [Yêu cầu số 2 và 3 trong phần "vẽ các hình bị predict sai trên tập test"]
- **Tag:** [vv24]

- **Fact:** [CONV] Trong thư viện Gradio, để xây dựng giao diện nhận diện hình ảnh (như Fashion MNIST), đầu vào `gr.Image` có thể được cấu hình với tham số `shape=(28,28)` và `image_mode='L'` (Grayscale) để khớp với định dạng đầu vào của mô hình.
- **Source:** [Đoạn mã khởi tạo gr.Interface trong phần deploy Gradio App]
- **Tag:** [vv24]

- **Fact:** [CONV] Quy trình tiền xử lý dữ liệu hình ảnh từ Gradio trước khi đưa vào mô hình Keras/TensorFlow bao gồm việc thay đổi hình dạng mảng (reshape) về kích thước `(1, 28, 28)` và chuẩn hóa giá trị pixel bằng cách chia cho 255.
- **Source:** [Hàm recognize_fashion: input = input.reshape((1,28,28))/255]
- **Tag:** [vv24]

- **Fact:** [CONV] Bộ dữ liệu Fashion MNIST bao gồm 10 lớp nhãn tương ứng với các loại trang phục: T-shirt, Trouser, Pullover, Dress, Coat, Sandal, Shirt, Sneaker, Bag, và Ankle boot.
- **Source:** [Biến labels trong đoạn mã Python vẽ hình ảnh bị dự đoán sai]
- **Tag:** [vv24]

- **Fact:** [CONV] Các dự án STEM dành cho học sinh tiểu học (khối 3) có thể tích hợp linh kiện điện tử cơ bản như đèn LED vào các sản phẩm thủ công (như thiệp chúc mừng) để giảng dạy về mạch điện đơn giản và sáng tạo nghệ thuật.
- **Source:** [Phần hội thoại "LED Design Quest" - yêu cầu cho học sinh khối 3]
- **Tag:** [vv24]

- **Fact:** [CONV] Việc sử dụng hàm `np.random.choice(ids)` cho phép chọn ngẫu nhiên các chỉ mục hình ảnh từ một danh sách các mẫu thỏa mãn điều kiện (ví dụ: danh sách các hình ảnh bị dự đoán sai) để hiển thị trên biểu đồ Matplotlib.
- **Source:** [Đoạn mã Python: target = np.random.choice(ids)]
- **Tag:** [vv24]
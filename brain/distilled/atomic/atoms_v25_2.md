Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v25) về các chủ đề AI, lập trình mô phỏng và xử lý dữ liệu:

- **Fact:** Hàm `max(position - k, 0)` được sử dụng trong lập trình để đảm bảo giá trị vị trí không bao giờ nhỏ hơn 0 khi thực hiện các bước lùi.
- **Source:** Đoạn mở đầu về cấu trúc hàm `max()`.
- **Tag:** [vv25]

- **Fact:** Hàm `np.random.multinomial(n, pvals)` của thư viện NumPy được sử dụng để mô phỏng các biến ngẫu nhiên đa thức, ví dụ như việc tung xúc xắc với các xác suất mặt khác nhau.
- **Source:** Section: ASSISTANT - Hướng dẫn dùng hàm np.random.multinomial.
- **Tag:** [vv25]

- **Fact:** Để mô phỏng phân phối hạng mục (Categorical Distribution), có thể sử dụng hàm `np.random.choice()` với tham số `p=probabilities` để chỉ định xác suất cho từng phần tử.
- **Source:** Section: ASSISTANT - Sử dụng Categorical Distribution.
- **Tag:** [vv25]

- **Fact:** Trong các bài toán AI và thống kê, hàm `np.random.normal(mu, sigma, n)` được dùng để tạo ra mảng dữ liệu tuân theo quy luật phân phối chuẩn (Gaussian distribution) với giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$.
- **Source:** Section: ASSISTANT - Lớp Python4AI.
- **Tag:** [vv25]

- **Fact:** NumPy cho phép lọc dữ liệu bằng indexing (ví dụ: `scores[scores >= d]`) để trích xuất các phần tử thỏa mãn điều kiện mà không cần sử dụng vòng lặp `for`, giúp tối ưu hiệu suất xử lý dữ liệu lớn trong AI.
- **Source:** Section: ASSISTANT - count_passing_students.
- **Tag:** [vv25]

- **Fact:** Hàm `zip(x_1, x_2)` kết hợp các phần tử từ hai mảng thành các cặp tương ứng, thường dùng để duyệt song song các tọa độ hoặc thuộc tính dữ liệu.
- **Source:** Section: ASSISTANT - zip(x_1, x_2) giải thích cấu trúc.
- **Tag:** [vv25]

- **Fact:** Thư viện `matplotlib.pyplot` sử dụng hàm `plt.scatter()` để vẽ biểu đồ phân tán, cho phép trực quan hóa sự phân bố của các lớp dữ liệu (Class) trong không gian hai chiều.
- **Source:** Section: ASSISTANT - giải thích cấu trúc plt.scatter.
- **Tag:** [vv25]

- **Fact:** Tham số `c=y` trong hàm `plt.scatter` được dùng để ánh xạ màu sắc của các điểm dữ liệu dựa trên giá trị của mảng nhãn `y`.
- **Source:** Section: ASSISTANT - plt.scatter(X[:, 0], X[:, 1], c=y).
- **Tag:** [vv25]

- **Fact:** Để trực quan hóa bề mặt dự đoán của một mô hình AI trong không gian 3D, thư viện `plotly.graph_objects` cung cấp hàm `go.Surface()`.
- **Source:** Section: ASSISTANT - visualize().
- **Tag:** [vv25]

- **Fact:** Hàm `np.meshgrid()` tạo ra một lưới tọa độ từ các mảng một chiều, là bước chuẩn bị quan trọng để vẽ biểu đồ bề mặt hoặc tính toán trên lưới không gian.
- **Source:** Section: ASSISTANT - np.meshgrid() giải thích.
- **Tag:** [vv25]

- **Fact:** `np.c_[]` là công cụ của NumPy dùng để kết hợp các mảng theo chiều ngang (theo cột), thường dùng để tạo mảng tọa độ `(x, y)` từ các lưới giá trị riêng biệt.
- **Source:** Section: ASSISTANT - np.c_[] giải thích.
- **Tag:** [vv25]

- **Fact:** Phương thức `ravel()` trong NumPy được dùng để "làm phẳng" một mảng đa chiều thành mảng một chiều theo thứ tự hàng.
- **Source:** Section: ASSISTANT - xx.ravel() là gì.
- **Tag:** [vv25]

- **Fact:** Hàm `np.linspace(start, stop, num)` tạo ra một dãy số cách đều nhau trong một khoảng xác định, thường dùng để tạo các trục tọa độ cho việc mô phỏng.
- **Source:** Section: ASSISTANT - visualize().
- **Tag:** [vv25]

- **Fact:** Lỗi `TypeError: 'float' object cannot be interpreted as an integer` thường xảy ra khi truyền một số thực vào tham số yêu cầu số nguyên (như số lượng mẫu `n`) trong các hàm sinh số ngẫu nhiên của NumPy.
- **Source:** Section: ASSISTANT - Lỗi TypeError.
- **Tag:** [vv25]

- **Fact:** Trong lập trình mô phỏng trò chơi hoặc robot, việc sử dụng `np.argmax()` giúp xác định chỉ số của giá trị lớn nhất, tương ứng với kết quả có xác suất cao nhất hoặc lựa chọn tối ưu.
- **Source:** Section: ASSISTANT - simulate_game (đoạn mã đầu tiên).
- **Tag:** [vv25]
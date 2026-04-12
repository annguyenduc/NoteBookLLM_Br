---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v25_2
  title: CONV_atoms_v25_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu Volume v25 liên quan đến lập trình Python, xử lý dữ liệu (Numpy) và trực quan hóa (Matplotlib/Plotly) - những nền tảng quan trọng trong AI và Robotics:

- **Fact:** [CONV] Hàm `max(position - k, 0)` trong Python thường được sử dụng để đảm bảo một giá trị không bao giờ nhỏ hơn 0, bằng cách trả về 0 nếu kết quả phép trừ là số âm.
- **Source:** [vv25 - Đoạn mở đầu về hàm max()]
- **Tag:** [vv25]

- **Fact:** [CONV] Để mô phỏng việc tung xúc xắc hoặc các biến ngẫu nhiên rời rạc với xác suất cho trước, có thể sử dụng hàm `np.random.multinomial(n, pvals)` hoặc `np.random.choice()` với tham số `p`.
- **Source:** [vv25 - Section: ASSISTANT response to Tí & Tèo game]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `np.random.normal(mu, sigma, n)` được sử dụng để tạo ra một mảng gồm `n` phần tử tuân theo quy luật phân phối chuẩn với giá trị trung bình là `mu` ($\mu$) và độ lệch chuẩn là `sigma` ($\sigma$).
- **Source:** [vv25 - Section: Lớp Python4AI GPA]
- **Tag:** [vv25]

- **Fact:** [CONV] Trong thư viện Numpy, tham số kích thước mẫu (size/n) trong các hàm tạo số ngẫu nhiên (như `np.random.normal`) bắt buộc phải là kiểu số nguyên (integer); nếu truyền vào kiểu số thực (float) sẽ gây ra lỗi `TypeError`.
- **Source:** [vv25 - Section: Giải thích lỗi TypeError]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `zip(x_1, x_2)` trong Python kết hợp các phần tử từ hai hoặc nhiều mảng thành các cặp (tuple) tương ứng, cho phép duyệt song song nhiều danh sách trong cùng một vòng lặp.
- **Source:** [vv25 - Section: zip(x_1, x_2) giải thích]
- **Tag:** [vv25]

- **Fact:** [CONV] Để trực quan hóa dữ liệu phân loại trong không gian hai chiều, hàm `plt.scatter()` có thể sử dụng tham số `c=y` để tự động gán màu sắc cho các điểm dữ liệu dựa trên nhãn (label) của chúng.
- **Source:** [vv25 - Section: plt.scatter(X[:, 0], X[:, 1], c=y)]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `ravel()` trong Numpy được dùng để làm phẳng (flatten) một mảng đa chiều thành mảng một chiều (1D) theo thứ tự hàng (từ trái qua phải, từ trên xuống dưới).
- **Source:** [vv25 - Section: xx.ravel() là gì]
- **Tag:** [vv25]

- **Fact:** [CONV] `np.c_[]` là một đối tượng trong Numpy dùng để kết hợp các mảng theo chiều ngang (theo trục cột/axis 1), thường dùng để tạo ma trận đặc trưng từ các mảng tọa độ riêng lẻ.
- **Source:** [vv25 - Section: np.c_[] giải thích]
- **Tag:** [vv25]

- **Fact:** [CONV] Hàm `np.meshgrid()` tạo ra một lưới tọa độ (coordinate grid) từ các mảng 1D, là bước chuẩn bị cần thiết để vẽ các biểu đồ bề mặt 3D hoặc bản đồ nhiệt (heatmap).
- **Source:** [vv25 - Section: np.meshgrid() giải thích]
- **Tag:** [vv25]

- **Fact:** [CONV] Thư viện `plotly.graph_objects` cung cấp hàm `go.Surface(x, y, z)` để tạo biểu đồ bề mặt 3D tương tác, cho phép trực quan hóa các hàm số hoặc kết quả dự đoán của mô hình AI trên một không gian lưới.
- **Source:** [vv25 - Section: visualize() function using plotly]
- **Tag:** [vv25]
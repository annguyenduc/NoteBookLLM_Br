---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v26_4
  title: atoms_v26_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v26) về AI và lập trình bổ trợ cho AI/Data Science:

- **Fact:** Thuật toán Gradient Descent có thể được cải tiến điều kiện dừng bằng cách lặp cho đến khi giá trị tuyệt đối của đạo hàm bé hơn một sai số dương $\epsilon$ (epsilon) cố định cho trước, thay vì lặp theo số lần cố định.
- **Source:** Section: Cải tiến thuật toán Gradient Descent.
- **Tag:** [vv26]

- **Fact:** Gradient của hàm số $f(x, y) = x^2 + \sin(y)$ được xác định bởi vector đạo hàm riêng $[\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}] = [2x, \cos(y)]$.
- **Source:** Section: ASSISTANT (Giải thích hàm gradient).
- **Tag:** [vv26]

- **Fact:** Trong lập trình Python, thư viện `plotly.graph_objects` cung cấp các hàm `go.Surface` để vẽ bề mặt đồ thị 3D và `go.Scatter3d` để vẽ các điểm dữ liệu trong không gian 3 chiều.
- **Source:** Section: ASSISTANT (Đoạn mã sử dụng Plotly).
- **Tag:** [vv26]

- **Fact:** Trong hệ thống gợi ý (Recommender System), độ tương quan (relevance) giữa người dùng và sản phẩm có thể được tính toán nhanh bằng phép nhân ma trận (dot product) giữa ma trận sở thích người dùng và ma trận đặc trưng sản phẩm chuyển vị.
- **Source:** Section: Movie Recommender System (ASSISTANT giải thích dot product similarity).
- **Tag:** [vv26]

- **Fact:** Công thức tính Cosine Similarity giữa vector người dùng ($u$) và vector sản phẩm ($v$) bằng NumPy là: `np.dot(u, v.T) / (np.linalg.norm(u) * np.linalg.norm(v, axis=1))`.
- **Source:** Section: USER/ASSISTANT (Dùng công thức cosine).
- **Tag:** [vv26]

- **Fact:** Trong thư viện Pandas, thuộc tính `df.shape[0]` trả về số lượng hàng (rows) của DataFrame, tương ứng với `axis=0`.
- **Source:** Section: ASSISTANT (df.shape[0] nghĩa là gì).
- **Tag:** [vv26]

- **Fact:** Khi sử dụng hàm `np.linalg.norm` với tham số `axis=1`, NumPy sẽ tính định mức (norm) của từng vector theo hàng (chiều ngang) trong một ma trận.
- **Source:** Section: ASSISTANT (Tại sao lại lấy axis = 1).
- **Tag:** [vv26]

- **Fact:** Hàm `np.where(condition)` trả về một tuple chứa các chỉ mục (indices) của các phần tử thỏa mãn điều kiện; ví dụ `np.where(similarity >= 0.9)[1]` được dùng để lấy chỉ mục cột của các bộ phim có độ tương đồng cao.
- **Source:** Section: ASSISTANT (similar_movies = np.where(similarity >= 0.9)[1] giải thích).
- **Tag:** [vv26]

- **Fact:** Một vector đặc trưng (feature vector) cho phim có thể được xây dựng bằng phương pháp One-hot encoding thủ công: tạo mảng zero và gán giá trị 1 tại chỉ mục tương ứng với thể loại phim (genres) mà phim đó sở hữu.
- **Source:** Section: Movie Recommender System (Đoạn mã khởi tạo movie_pts).
- **Tag:** [vv26]
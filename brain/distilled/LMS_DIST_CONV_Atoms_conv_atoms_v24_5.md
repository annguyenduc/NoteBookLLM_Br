---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v24_5
  title: CONV_atoms_v24_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v24:

- **Fact:** [CONV] Trong thuật toán K-Means (thư viện Scikit-learn), thuộc tính `kmeans.cluster_centers_` lưu trữ tọa độ các tâm cụm, và `kmeans.labels_` chứa nhãn nhóm của từng điểm dữ liệu.
- **Source:** [vv24] - Section: Python Code Explanation
- **Tag:** [vv24]

- **Fact:** [CONV] Để tìm nhóm có giá trị trung bình cao nhất trong một cột dữ liệu cụ thể (ví dụ S-AVG hoặc GPA) của tâm cụm, ta sử dụng kết hợp `np.max()` để lấy giá trị và `np.argmax()` để lấy chỉ số (index) của nhóm đó.
- **Source:** [vv24] - Section: Python Code Explanation
- **Tag:** [vv24]

- **Fact:** [CONV] Việc lọc danh sách đối tượng thuộc một cụm cụ thể trong DataFrame được thực hiện bằng cú pháp Boolean indexing: `df[kmeans.labels_ == index]`.
- **Source:** [vv24] - Section: Python Code Explanation
- **Tag:** [vv24]

- **Fact:** [CONV] "Interactive Fiction" hoặc "Narrative Games" là thể loại trò chơi cho phép người chơi đưa ra quyết định để thay đổi diễn biến câu chuyện, tiêu biểu như các tựa game: Life is Strange, Detroit: Become Human, và Until Dawn.
- **Source:** [vv24] - Section: Bandersnatch Trò tương tác
- **Tag:** [vv24]

- **Fact:** [CONV] Pygame là thư viện Python phổ biến được sử dụng để thiết kế giao diện đồ họa 2D, xử lý sự kiện (phím, chuột) và xây dựng vòng lặp trò chơi (game loop) cho các ứng dụng giáo dục STEM.
- **Source:** [vv24] - Section: AI Game Development
- **Tag:** [vv24]

- **Fact:** [CONV] Quy trình thiết lập môi trường lập trình game Python trên VSCode bao gồm: Cài đặt Python, tạo môi trường ảo (`venv`), kích hoạt môi trường và cài đặt các thư viện bổ trợ như `pygame`, `numpy`, `matplotlib` thông qua `pip`.
- **Source:** [vv24] - Section: AI Game Development
- **Tag:** [vv24]

- **Fact:** [CONV] Cấu trúc cơ bản của một vòng lặp Pygame bao gồm việc kiểm tra sự kiện `pygame.QUIT`, xóa màn hình bằng `screen.fill()`, vẽ đối tượng và cập nhật hiển thị bằng `pygame.display.update()` hoặc `pygame.display.flip()`.
- **Source:** [vv24] - Section: AI Game Development
- **Tag:** [vv24]

- **Fact:** [CONV] Cross Entropy (Entropy chéo) là hàm mất mát dùng để đo lường sự khác biệt giữa hai phân phối xác suất P (thực tế) và Q (ước lượng) theo công thức: $H(P, Q) = - \sum P(x) \log(Q(x))$.
- **Source:** [vv24] - Section: Cross Entropy in ML
- **Tag:** [vv24]

- **Fact:** [CONV] Hàm Softmax biến đổi một vector số thực thành một vector xác suất có tổng bằng 1, trong đó mỗi phần tử $x_i$ được tính theo công thức $e^{x_i} / \sum e^{x_j}$.
- **Source:** [vv24] - Section: Cross Entropy in ML
- **Tag:** [vv24]

- **Fact:** [CONV] Để tránh lỗi tràn số (overflow) khi tính toán Softmax trong lập trình, kỹ thuật phổ biến là trừ giá trị lớn nhất của vector đầu vào (`x - np.max(x)`) trước khi tính hàm mũ.
- **Source:** [vv24] - Section: Cross Entropy in ML
- **Tag:** [vv24]
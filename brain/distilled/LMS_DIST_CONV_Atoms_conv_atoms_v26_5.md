---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v26_5
  title: CONV_atoms_v26_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v26 liên quan đến lập trình Python, xử lý dữ liệu (Data Science) và AI:

**1. Sự khác biệt về Axis giữa NumPy và Pandas**
- Fact: [CONV] Trong NumPy, `axis=0` đại diện cho trục dọc (hàng) và `axis=1` đại diện cho trục ngang (cột). Ngược lại, trong Pandas, khi sử dụng các hàm như `.sum()`, `axis=0` dùng để tính toán theo cột và `axis=1` dùng để tính toán theo hàng.
- Source: [vv26 - Section: ASSISTANT response 1 & 2]
- Tag: [vv26]

**2. Khởi tạo mảng NumPy từ hình dạng (shape)**
- Fact: [CONV] Câu lệnh `np.zeros(shape=(df.shape[0], 20))` tạo ra một mảng chứa toàn số 0 với số dòng bằng số lượng hàng của DataFrame `df` và có 20 cột.
- Source: [vv26 - Section: USER: movie_pts = np.zeros...]
- Tag: [vv26]

**3. Xử lý chuỗi dữ liệu trong Pandas**
- Fact: [CONV] Phương thức `.split('|')` kết hợp với `.iloc[i]` được sử dụng để tách một chuỗi văn bản (ví dụ: các thể loại phim "History|Drama") tại một hàng cụ thể thành một danh sách (list) các phần tử riêng biệt.
- Source: [vv26 - Section: ASSISTANT response 3]
- Tag: [vv26]

**4. Định nghĩa và tính chất của Tích vô hướng (Dot Product)**
- Fact: [CONV] Dot product là phép toán giữa hai vector cùng chiều, kết quả là một số vô hướng (scalar) bằng tổng của tích các thành phần tương ứng: $A[0]*B[0] + A[1]*B[1] + ... + A[n-1]*B[n-1]$.
- Source: [vv26 - Section: ASSISTANT response 6]
- Tag: [vv26]

**5. Quy tắc nhân ma trận (Matrix Dot Product)**
- Fact: [CONV] Để thực hiện dot product giữa hai ma trận A và B, số cột của ma trận A phải bằng số hàng của ma trận B. Nếu A có shape (m, n) và B có shape (n, p), ma trận kết quả C sẽ có shape (m, p).
- Source: [vv26 - Section: ASSISTANT response 7 & 10]
- Tag: [vv26]

**6. Công thức toán học của phần tử trong ma trận tích**
- Fact: [CONV] Phần tử tại vị trí (i, j) của ma trận kết quả $C$ được tính bằng công thức: $C(i, j) = \sum_{k=1}^{n} (A(i, k) \times B(k, j))$.
- Source: [vv26 - Section: ASSISTANT response 10]
- Tag: [vv26]

**7. Sử dụng hàm np.where để truy vấn chỉ mục**
- Fact: [CONV] Hàm `np.where(condition)` trả về một tuple chứa các mảng chỉ mục của các phần tử thỏa mãn điều kiện. Trong mảng 2 chiều, `np.where(condition)[0]` trả về chỉ mục hàng và `np.where(condition)[1]` trả về chỉ mục cột.
- Source: [vv26 - Section: ASSISTANT response 12, 14 & 16]
- Tag: [vv26]

**8. Chuyển đổi chỉ mục np.where thành tọa độ 2D**
- Fact: [CONV] Để chuyển đổi kết quả từ `np.where` thành một mảng 2 chiều chứa các cặp tọa độ (hàng, cột), có thể sử dụng hàm `np.column_stack((row_indexes, col_indexes))`.
- Source: [vv26 - Section: ASSISTANT response 14]
- Tag: [vv26]

**9. Kỹ thuật lọc dữ liệu nâng cao (Fancy Indexing)**
- Fact: [CONV] Biểu thức `movie_relevance[i][relevant_movies]` cho phép truy cập đồng thời nhiều phần tử tại các cột cụ thể (được định nghĩa trong mảng `relevant_movies`) của hàng thứ `i` trong ma trận.
- Source: [vv26 - Section: ASSISTANT response 17]
- Tag: [vv26]

**10. Khởi tạo mảng số nguyên ngẫu nhiên bằng vòng lặp**
- Fact: [CONV] Có thể khởi tạo mảng 2 chiều chứa các số nguyên ngẫu nhiên (0 hoặc 1) bằng cách tạo mảng `np.zeros` với `dtype=np.int32` trước, sau đó dùng 2 vòng lặp lồng nhau để gán giá trị từ `np.random.randint(0, 2)`.
- Source: [vv26 - Section: ASSISTANT response 5]
- Tag: [vv26]
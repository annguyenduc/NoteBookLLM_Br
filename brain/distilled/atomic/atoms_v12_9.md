Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v12):

- **Fact:** VS Code không hỗ trợ trực tiếp cờ `--file-write` trong cấu hình task; việc sử dụng cờ này sẽ dẫn đến lỗi "invalid arguments".
- **Source:** [Phần phản hồi của ASSISTANT về lỗi --file-write]
- **Tag:** [vv12]

- **Fact:** Có thể sử dụng script Python kết hợp với thư viện `json` và `pathlib` để tự động hóa việc chỉnh sửa file cấu hình `settings.json` trong VS Code.
- **Source:** [Mục 2. Tạo script Python]
- **Tag:** [vv12]

- **Fact:** Trong file `tasks.json` của VS Code, biến `${workspaceFolder}` được sử dụng để tự động trỏ đến thư mục gốc của dự án.
- **Source:** [Mục 2. Chạy lại task với đúng đường dẫn]
- **Tag:** [vv12]

- **Fact:** Việc tối ưu hóa hiệu suất mã nguồn (Code Efficiency) tập trung vào hai yếu tố chính: độ phức tạp thời gian (Time Complexity) và độ phức tạp không gian (Space Complexity).
- **Source:** [Mục 2. Phân tích độ phức tạp]
- **Tag:** [vv12]

- **Fact:** Các độ phức tạp thời gian phổ biến trong phân tích thuật toán bao gồm $O(1)$, $O(\log n)$, $O(n)$, và $O(n^2)$.
- **Source:** [Mục 2. Phân tích độ phức tạp]
- **Tag:** [vv12]

- **Fact:** Kỹ thuật ghi nhớ (memoization) giúp tối ưu thuật toán bằng cách lưu trữ kết quả của các phép tính để tránh việc tính toán lại không cần thiết.
- **Source:** [Mục 3. Tối ưu thuật toán]
- **Tag:** [vv12]

- **Fact:** Bảng băm (hash table) được sử dụng để tối ưu hóa việc tìm kiếm nhanh, trong khi cấu trúc dữ liệu heap hiệu quả cho việc quản lý giá trị lớn nhất hoặc nhỏ nhất.
- **Source:** [Mục 3. Tối ưu thuật toán]
- **Tag:** [vv12]

- **Fact:** Phương pháp chia để trị (divide and conquer) là kỹ thuật chia bài toán lớn thành các bài toán con nhỏ hơn để giải quyết (ví dụ: quicksort, mergesort).
- **Source:** [Mục 3. Tối ưu thuật toán]
- **Tag:** [vv12]

- **Fact:** Thư viện `timeit` trong Python là công cụ dùng để đo lường thời gian thực thi và xác định các điểm nghẽn (bottlenecks) về hiệu suất trong mã nguồn.
- **Source:** [Mục 6. Kiểm tra và đo lường hiệu suất]
- **Tag:** [vv12]

- **Fact:** Việc sử dụng "short-circuit" trong các câu lệnh điều kiện giúp tránh các tính toán không cần thiết, từ đó cải thiện tốc độ xử lý của vòng lặp và logic điều kiện.
- **Source:** [Mục 5. Tối ưu hóa vòng lặp và điều kiện]
- **Tag:** [vv12]

- **Fact:** Người dùng có thể gán phím tắt tùy chỉnh cho các task trong VS Code thông qua file cấu hình `keybindings.json`.
- **Source:** [Mục Mẹo sử dụng Task - 2. Phím tắt cho Task]
- **Tag:** [vv12]

- **Fact:** Pylint và Flake8 là các công cụ linter phổ biến cho Python, giúp phát hiện lỗi và cảnh báo trực tiếp trong Problems Panel của VS Code.
- **Source:** [Mục 3. Kiểm tra lại code với linter]
- **Tag:** [vv12]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_30
  title: atoms_v10_30
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dựa trên nguồn cung cấp **Volume v10** (bao gồm nội dung bài học và các câu hỏi trắc nghiệm về Python/Linux Automation), dưới đây là các sự kiện kỹ thuật được trích xuất:

- **Fact:** Lệnh `diff` được sử dụng để tìm ra sự khác biệt giữa hai tệp tin, trong khi `diff -u` (unified format) giúp hiển thị các dòng khác biệt một cách dễ đọc hơn.
- **Source:** (v10 - Section: Study guide: diff and patch)
- **Tag:** [vv10]

- **Fact:** Lệnh `patch` kết hợp với một tệp tin Diff (chứa các thay đổi) để áp dụng các sửa đổi đó vào một tệp gốc.
- **Source:** (v10 - Question 1 & 5: diff and patch)
- **Tag:** [vv10]

- **Fact:** Lệnh `wdiff` (word diff) có khả năng làm nổi bật các từ cụ thể bị thay đổi trong một tệp thay vì chỉ so sánh theo từng dòng như lệnh `diff` thông thường.
- **Source:** (v10 - Question 3: diff and patch)
- **Tag:** [vv10]

- **Fact:** Trong lập trình Python (thường dùng trong Robotics và AI), module `re` (Regular Expression) được sử dụng để tìm kiếm, trích xuất (parsing) và thao tác với văn bản dựa trên các biểu thức mẫu.
- **Source:** (v10 - Question 1 & 6: Log Analysis)
- **Tag:** [vv10]

- **Fact:** Để kiểm soát giá trị trả về (exit code) của một script Python khi kết thúc, lập trình viên sử dụng lệnh `exit` từ module `sys`.
- **Source:** (v10 - Question 4: diff and patch)
- **Tag:** [vv10]

- **Fact:** Trong môi trường dòng lệnh Linux (như Ubuntu/WSL), lệnh `nano [tên_file]` sẽ tự động tạo một tệp mới nếu tệp đó chưa tồn tại trong hệ thống.
- **Source:** (v10 - Question 10: ticky_check.py)
- **Tag:** [vv10]

- **Fact:** Một trong những rủi ro của tự động hóa (Automation) là nó có thể làm hạn chế khả năng thích ứng của hệ thống đối với những thay đổi bất ngờ.
- **Source:** (v10 - Question 5: Automation Pitfalls)
- **Tag:** [vv10]

- **Fact:** Để sắp xếp một từ điển (dictionary) trong Python theo giá trị (value) giảm dần, ta sử dụng hàm `sorted()` kết hợp với tham số `key=lambda x: x[1]` và `reverse=True`.
- **Source:** (v10 - Question 9: Dictionary Sorting)
- **Tag:** [vv10]

- **Fact:** Python là ngôn ngữ nền tảng được sử dụng rộng rãi để điều khiển robot và triển khai các mô hình AI nhờ vào khả năng xử lý dữ liệu và thư viện phong phú.
- **Source:** [Nội dung suy luận từ ngữ cảnh lập trình trong tài liệu]
- **Tag:** [Unverified_Source]

- **Fact:** Việc sử dụng Symbolic Link (`ln -s`) trong Linux giúp tạo các lối tắt (shortcuts) để truy cập nhanh vào các thư mục dự án phức tạp mà không cần di chuyển cấu trúc tệp tin gốc.
- **Source:** [Dựa trên hội thoại hướng dẫn thực hành trong Raw Data]
- **Tag:** [Unverified_Source]
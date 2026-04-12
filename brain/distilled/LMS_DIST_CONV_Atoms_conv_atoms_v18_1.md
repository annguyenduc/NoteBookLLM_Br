---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v18_1
  title: CONV_atoms_v18_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật về IoT, Python và lập trình điều khiển được trích xuất từ nguồn dữ liệu Volume 18:

- Fact: [CONV] Python có thể được sử dụng để lập trình hệ thống chuông trường học tự động bằng cách sử dụng thư viện `time` để kiểm tra thời gian thực từ hệ thống.
- Source: (v18 - Conversation: Chuông tự động Python)
- Tag: [vv18]

- Fact: [CONV] Trong lập trình điều khiển thời gian, hàm `time.sleep()` nhận tham số tính bằng giây; do đó, để tạm dừng theo phút, cần nhân giá trị với 60.
- Source: (v18 - Conversation: Chuông tự động Python - Code block 1)
- Tag: [vv18]

- Fact: [CONV] Cấu trúc vòng lặp `while True` tạo ra một vòng lặp vô hạn, thường được ứng dụng trong các tác vụ giám sát liên tục như hệ thống báo động hoặc đồng hồ thời gian thực.
- Source: (v18 - Conversation: Chuông tự động Python - Assistant's explanation)
- Tag: [vv18]

- Fact: [CONV] Để ngăn chặn vòng lặp `while` vô hạn, lập trình viên có thể thay đổi giá trị của biến điều kiện hoặc sử dụng từ khóa `break` để thoát khỏi vòng lặp.
- Source: (v18 - Conversation: Chuông tự động Python - Question: Which techniques can prevent an infinite while loop?)
- Tag: [vv18]

- Fact: [CONV] Các thói quen lập trình tốt (Coding Style) bao gồm: thêm chú thích (comments), viết mã tự giải thích (self-documenting code) và khử mã trùng lặp bằng cách tạo các hàm có thể tái sử dụng.
- Source: (v18 - Conversation: Coding Style Best Practices)
- Tag: [vv18]

- Fact: [CONV] Trong Python, việc so sánh chuỗi (ví dụ: `"big" > "small"`) được thực hiện theo phương pháp so sánh từ điển (lexicographical comparison) dựa trên giá trị Unicode của từng ký tự.
- Source: (v18 - Conversation: Coding Style Best Practices - Assistant's explanation on string comparison)
- Tag: [vv18]

- Fact: [CONV] Các giá trị được truyền vào hàm khi gọi hàm được định nghĩa kỹ thuật là các "tham số" (parameters).
- Source: (v18 - Conversation: Coding Style Best Practices - Question: What are the values passed into functions as input called?)
- Tag: [vv18]

- Fact: [CONV] Cấu trúc `if-elif-else` cho phép kiểm tra một chuỗi các điều kiện tuần tự và thực thi khối mã tương ứng với điều kiện đúng đầu tiên được tìm thấy.
- Source: (v18 - Conversation: Coding Style Best Practices - Cấu trúc if elif)
- Tag: [vv18]

- Fact: [CONV] Trong tính toán lưu trữ hệ thống tệp (filesystem), toán tử chia lấy phần nguyên `//` và chia lấy dư `%` được sử dụng để xác định tổng số khối (blocks) cần thiết nhằm tối ưu hóa không gian lưu trữ.
- Source: (v18 - Conversation: Coding Style Best Practices - Question 5: calculate_storage)
- Tag: [vv18]

- Fact: [CONV] Để lấy phần thập phân của một phép chia trong Python, có thể sử dụng công thức `(tử_số % mẫu_số) / mẫu_số`.
- Source: (v18 - Conversation: Coding Style Best Practices - Question 9: fractional_part)
- Tag: [vv18]

- Fact: [CONV] Việc sử dụng tên biến chỉ gồm một ký tự (như `i`, `j`) chỉ được khuyến khích khi phạm vi biến hạn chế và mục đích rõ ràng, chẳng hạn như làm biến đếm trong vòng lặp.
- Source: (v18 - Conversation: Coding Style Best Practices - Assistant's explanation on variable names)
- Tag: [vv18]

- Fact: [CONV] Toán tử lũy thừa trong Python được ký hiệu là `**`, ví dụ `n**2` tương đương với $n^2$.
- Source: (v18 - Conversation: Coding Style Best Practices - Code snippet: if n*6 > n**2)
- Tag: [vv18]

- Fact: [CONV] Hàm `time.localtime()` trả về một đối
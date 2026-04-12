---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v15_6
  title: CONV_atoms_v15_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu RAW (Volume v15) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Trong Python, cú pháp `value_if_true if condition else value_if_false` được gọi là "conditional expression" hoặc "ternary operator", giúp viết mã ngắn gọn trên một dòng.
- **Source:** [vv15 - Section: Giải thích Conditional Expression]
- **Tag:** [vv15]

- **Fact:** [CONV] Thư viện `unittest` là một framework tích hợp sẵn trong Python; các phương thức kiểm tra bên trong lớp kế thừa từ `unittest.TestCase` phải bắt đầu bằng tiền tố `test_`.
- **Source:** [vv15 - Section: Giải thích Chi Tiết unittest & Quy Trình Kiểm Tra]
- **Tag:** [vv15]

- **Fact:** [CONV] Khác với `unittest`, `pytest` cho phép viết các bài kiểm tra dưới dạng hàm đơn giản, không bắt buộc dùng lớp, và cung cấp thông báo lỗi chi tiết, dễ đọc hơn.
- **Source:** [vv15 - Section: giải thích về pytest & so sánh]
- **Tag:** [vv15]

- **Fact:** [CONV] Lệnh `echo $?` trong shell được sử dụng để hiển thị giá trị thoát (exit value) của lệnh hoặc script vừa thực hiện trước đó.
- **Source:** [vv15 - Section: Lệnh và mã thoát - Câu 1]
- **Tag:** [vv15]

- **Fact:** [CONV] Mã thoát (exit code) có giá trị bằng 0 biểu thị chương trình đã kết thúc thành công mà không có lỗi.
- **Source:** [vv15 - Section: Lệnh và mã thoát - Câu 4]
- **Tag:** [vv15]

- **Fact:** [CONV] Trong Python 2, hàm `raw_input` nhận dữ liệu vào dưới dạng chuỗi (string), trong khi hàm `input` sẽ thực hiện các phép toán cơ bản trên dữ liệu nhập vào.
- **Source:** [vv15 - Section: Lệnh và mã thoát - Câu 5]
- **Tag:** [vv15]

- **Fact:** [CONV] Hàm `subprocess.run()` trả về một đối tượng kiểu `CompletedProcess`. Khi tham số `capture_output` được đặt là `True`, nó cho phép lưu trữ đầu ra của lệnh hệ thống.
- **Source:** [vv15 - Section: Subprocess - Câu 1 & Câu 4]
- **Tag:** [vv15]

- **Fact:** [CONV] Tham số `cwd` (current working directory) trong module `subprocess` được sử dụng để thay đổi thư mục thực thi lệnh.
- **Source:** [vv15 - Section: Subprocess - Câu 2]
- **Tag:** [vv15]

- **Fact:** [CONV] Khi một tiến trình con (child process) chạy bằng module `subprocess`, tiến trình cha (parent process) sẽ bị chặn (blocked) cho đến khi tiến trình con kết thúc.
- **Source:** [vv15 - Section: Subprocess - Câu 3]
- **Tag:** [vv15]

- **Fact:** [CONV] Để nhận đối số từ dòng lệnh (command line argument) trong Python, lập trình viên sử dụng danh sách `sys.argv` (ví dụ: `sys.argv[1]` để lấy tham số đầu tiên).
- **Source:** [vv15 - Section: Scripting & Log Processing - Câu 1]
- **Tag:** [vv15]

- **Fact:** [CONV] Từ khóa `continue` được sử dụng trong vòng lặp để bỏ qua các câu lệnh còn lại trong lần lặp hiện tại và quay trở lại đầu vòng lặp.
- **Source:** [vv15 - Section: Scripting & Log Processing - Câu 3]
- **Tag:** [vv15]

- **Fact:** [CONV] Cấu trúc dữ liệu Dictionary (từ điển) thường được sử dụng để đếm số lần xuất hiện của một lỗi cụ thể trong các tệp nhật ký (logs).
- **Source:** [vv15 - Section: Scripting & Log Processing - Câu 2]
- **Tag:** [vv15]
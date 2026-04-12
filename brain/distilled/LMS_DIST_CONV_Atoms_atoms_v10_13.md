---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_13
  title: atoms_v10_13
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v10) theo quy tắc LOM v4.1:

- **Fact:** Bash có thể viết hoa chữ cái đầu của mỗi từ bằng cách lặp qua kết quả của lệnh `cat`, sử dụng `tr "[:lower:]" "[:upper:]"` để chuyển đổi ký tự đầu tiên và nối lại với phần còn lại của chuỗi thông qua cú pháp `${i:1}`.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Bash code block)
- **Tag:** [vv10]

- **Fact:** Script Python `capitalize_words.py` sử dụng module `sys` và đọc dữ liệu từ `sys.stdin` để xử lý văn bản theo từng dòng.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Python code block)
- **Tag:** [vv10]

- **Fact:** Trong Python, phương thức `.capitalize()` được sử dụng để tự động viết hoa chữ cái đầu tiên của một chuỗi và chuyển các chữ cái còn lại thành chữ thường.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Python code block)
- **Tag:** [vv10]

- **Fact:** Để thực thi một script Python xử lý dữ liệu từ một file văn bản hiện có, có thể sử dụng cơ chế pipe trong terminal: `cat [tên_file] | ./[tên_script].py`.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Execution command)
- **Tag:** [vv10]

- **Fact:** Cấu trúc của script Python xử lý văn bản bao gồm việc loại bỏ khoảng trắng thừa bằng `.strip()`, chia nhỏ dòng thành danh sách các từ bằng `.split()`, và tái hợp các từ bằng `" ".join()`.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Python code block)
- **Tag:** [vv10]

- **Fact:** Bash sử dụng cú pháp `${biến:vị_trí:độ_dài}` để cắt chuỗi, ví dụ `${i:0:1}` lấy ký tự đầu tiên của biến `i`.
- **Source:** (v10 - Section: Choosing Between Bash and Python - Bash code block)
- **Tag:** [vv10]
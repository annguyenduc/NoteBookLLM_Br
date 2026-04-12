---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v16_6
  title: atoms_v16_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu (v16) về chủ đề Biểu thức chính quy (Regex) và Python:

- **Fact**: Hàm `re.sub(pattern, repl, string)` trong Python được sử dụng để tìm kiếm một mẫu biểu thức chính quy trong chuỗi và thay thế nó bằng một chuỗi khác.
- **Source**: (v16 - Section: Python re.sub)
- **Tag**: [vv16]

- **Fact**: Để thêm mã vùng "+1-" vào trước số điện thoại trong một bản ghi dạng CSV, có thể sử dụng nhóm bắt (capturing group) để xác định số điện thoại và dùng `\1` trong chuỗi thay thế để
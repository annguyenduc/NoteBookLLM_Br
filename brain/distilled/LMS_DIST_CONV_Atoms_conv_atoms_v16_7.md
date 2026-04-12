---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v16_7
  title: CONV_atoms_v16_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp, tập trung vào các kỹ thuật xử lý dữ liệu (AI/Data Processing) bằng Python:

- **Fact:** [CONV] Biểu thức chính quy (Regular Expression) là một chuỗi các ký tự tạo thành một mẫu tìm kiếm (search pattern), được sử dụng để tìm kiếm, thay thế và xử lý các chuỗi dữ liệu văn bản.
- **Source:** (v16 - Section: Biểu thức chính quy là gì?)
- **Tag:** [vv16]

- **Fact:** [CONV] Trong xử lý dữ liệu văn bản (AI/NLP), phương thức `groups()` của module `re` trong Python trả về một `tuple` chứa tất cả các nhóm (captured groups) đã được trích xuất từ một kết quả khớp.
- **Source:** (v16 - Section: When capturing regex groups, what datatype does the groups method return?)
- **Tag:** [vv16]

- **Fact:** [CONV] Để trích xuất tự động các URL bắt đầu bằng "https://" và kết thúc bằng các tên miền cấp cao (như .com, .org) từ văn bản, có thể sử dụng mẫu Regex `r'https://\S+\.\w+'`.
- **Source:** (v16 - Section: Complete the function find_url)
- **Tag:** [vv16]

- **Fact:** [CONV] Việc trích xuất các mã định danh nhân viên (Employee ID) có định dạng cụ thể (ví dụ: một chữ cái hoa, dấu gạch ngang và 7-8 chữ số) được thực hiện hiệu quả bằng mẫu Regex `r'\b[A-Z]-\d{7,8}\b'`.
- **Source:** (v16 - Section: Complete the find_eid function)
- **Tag:** [vv16]

- **Fact:** [CONV] Trong xử lý ngôn ngữ tự nhiên (AI/NLP), để tìm tất cả các từ có chứa đúng 3 nguyên âm liên tiếp, mẫu biểu thức chính quy phù hợp là `r'\b\w*[aeiouAEIOU]{3}\w*\b'`.
- **Source:** (v16 - Section: tôi muốn trả về hết các chữ chứa 3 nguyên âm liên tiếp)
- **Tag:** [vv16]

- **Fact:** [CONV] Kỹ thuật sử dụng nhóm bắt giữ (capturing groups) bằng dấu ngoặc đơn `()` trong Regex cho phép định dạng lại dữ liệu (như số điện thoại) thông qua các tham chiếu ngược (backreferences) như `\1`, `\2`, `\3` trong hàm `re.sub`.
- **Source:** (v16 - Section: Sửa lỗi hàm convert_phone_number)
- **Tag:** [vv16]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v22_6
  title: atoms_v22_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật về xử lý dữ liệu và tự động hóa (Google Apps Script) được trích xuất từ nguồn cung cấp:

- **Fact:** Phương thức `getRange(a1Notation)` và `getRangeList(a1Notation)` trong Google Apps Script đều có thể sử dụng để truy xuất và xử lý dữ liệu từ các ô chứa nhiều dòng văn bản (multi-line cells).
- **Source:** [Đoạn đầu - So sánh getRange và getRangeList]
- **Tag:** [vv22]

- **Fact:** Để tách nội dung của một ô tính nhiều dòng thành một mảng các chuỗi riêng biệt, sử dụng phương thức `.split("\n")` dựa trên ký tự xuống dòng.
- **Source:** [Phần ASSISTANT trả lời USER về việc thêm '-' mỗi đầu dòng]
- **Tag:** [vv22]

- **Fact:** Việc kiểm tra một dòng văn bản đã có tiền tố cụ thể hay chưa (ví dụ: dấu gạch ngang "- ") được thực hiện thông qua phương thức `.startsWith("- ")`.
- **Source:** [Phần ASSISTANT trả lời USER về việc kiểm tra dấu '-']
- **Tag:** [vv22]

- **Fact:** Biểu thức chính quy (Regular Expression) `/[a-zA-Z]/` được sử dụng để xác định xem một dòng văn bản có chứa bất kỳ ký tự chữ cái nào hay không trước khi thực hiện xử lý.
- **Source:** [Phần ASSISTANT trả lời USER về việc dòng không có chữ cái]
- **Tag:** [vv22]

- **Fact:** Để cập nhật dữ liệu hiệu quả cho một vùng (Range) gồm nhiều hàng và nhiều cột, cần sử dụng vòng lặp lồng nhau để duyệt mảng hai chiều và dùng phương thức `.setValues(values)` thay vì cập nhật từng ô đơn lẻ.
- **Source:** [Phần mã nguồn xử lý phạm vi H24:K26 và A1:B8]
- **Tag:** [vv22]

- **Fact:** Phương thức `.join("\n")` được dùng để gộp mảng các chuỗi văn bản lại thành một chuỗi duy nhất có định dạng xuống dòng trước khi ghi ngược lại vào ô tính.
- **Source:** [Các đoạn mã JavaScript xử lý chuỗi trong văn bản]
- **Tag:** [vv22]

- **Fact:** Kiểm tra kiểu dữ liệu `typeof cellValue === 'string'` là một bước an toàn để đảm bảo các phương thức xử lý chuỗi (như `.split` hoặc `.startsWith`) không gây lỗi khi gặp ô tính chứa dữ liệu số hoặc ô trống.
- **Source:** [Phần mã nguồn xử lý phạm vi H24:K26 và A1:B8]
- **Tag:** [vv22]

- **Fact:** Có thể thiết lập logic loại trừ xử lý cho các dòng bắt đầu bằng các từ khóa cụ thể (như "Toán", "Công nghệ", "Mỹ thuật") bằng cách kết hợp nhiều điều kiện phủ định với toán tử logic `&&`.
- **Source:** [Phần ASSISTANT trả lời về việc loại trừ các môn học]
- **Tag:** [vv22]
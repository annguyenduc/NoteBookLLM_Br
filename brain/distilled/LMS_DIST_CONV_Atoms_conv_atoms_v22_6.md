---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v22_6
  title: CONV_atoms_v22_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu về Google Apps Script (GAS) trong xử lý bảng tính:

- Fact: [CONV] Trong Google Apps Script, phương thức `getRange(a1Notation)` và `getRangeList(a1Notation)` đều có thể sử dụng để truy xuất và xử lý dữ liệu từ các ô chứa nội dung đa dòng (multi-line cell).
- Source: [Đoạn đầu: Sử dụng getRange(a1Notation) và getRangeList(a1Notation)]
- Tag: [vv22]

- Fact: [CONV] Để tách nội dung của một ô đa dòng thành các dòng riêng biệt để xử lý trong mảng, lập trình viên sử dụng phương thức `.split("\n")`.
- Source: [Phần ASSISTANT: "Tách các dòng thành mảng"]
- Tag: [vv22]

- Fact: [CONV] Phương thức `.startsWith("- ")` được sử dụng để kiểm tra xem một chuỗi văn bản đã bắt đầu bằng một tiền tố cụ thể hay chưa, giúp tránh việc lặp lại các ký tự điều khiển khi tự động hóa định dạng.
- Source: [Phần ASSISTANT: "Kiểm tra nếu dòng chưa có dấu '-'"]
- Tag: [vv22]

- Fact: [CONV] Biểu thức chính quy (Regular Expression) `/[a-zA-Z]/` được dùng để xác định xem một dòng văn bản có chứa bất kỳ ký tự chữ cái nào hay không, phục vụ việc lọc các dòng trống hoặc dòng chỉ chứa ký tự đặc biệt.
- Source: [Phần ASSISTANT: "Sử dụng biểu thức chính quy /[a-zA-Z]/"]
- Tag: [vv22]

- Fact: [CONV] Khi xử lý dữ liệu trên một phạm vi (Range) gồm nhiều hàng và nhiều cột, cần sử dụng hai vòng lặp lồng nhau để duyệt qua mảng hai chiều được trả về từ phương thức `getValues()`.
- Source: [Phần ASSISTANT: "Duyệt qua từng ô trong phạm vi H24:K26 bằng hai vòng lặp lồng nhau"]
- Tag: [vv22]

- Fact: [CONV] Để tối ưu hóa hiệu suất khi cập nhật dữ liệu cho nhiều ô cùng lúc, nên sử dụng `setValues(values)` với tham số là một mảng hai chiều thay vì cập nhật từng ô đơn lẻ bằng `setValue()`.
- Source: [Các đoạn mã xử lý Range A1:A8 và A1:B8]
- Tag: [vv22]

- Fact: [CONV] Việc kiểm tra kiểu dữ liệu `typeof cellValue === 'string'` là một bước kiểm soát lỗi để đảm bảo các phương thức xử lý chuỗi như `.split()` hoặc `.startsWith()` chỉ thực thi trên các ô chứa văn bản.
- Source: [Phần ASSISTANT: "Kiểm tra xem ô có phải là một chuỗi"]
- Tag: [vv22]
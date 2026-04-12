Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v22) liên quan đến lập trình điều khiển và quản lý dữ liệu (nền tảng cho các hệ thống IoT/Robotics):

- Fact: [CONV] Sử dụng biểu thức chính quy `new RegExp("^" + word + "\\b", "gm")` để tìm kiếm và thay thế một từ cụ thể chỉ khi nó xuất hiện ở đầu mỗi dòng trong một chuỗi văn bản đa dòng.
- Source: [Phần giải thích hàm addHyphenAtLineStart]
- Tag: [vv22]

- Fact: [CONV] Trong JavaScript/Apps Script, cờ `g` (global matching) cho phép tìm kiếm tất cả các kết quả khớp trong chuỗi; cờ `m` (multiline) cho phép các ký tự bắt đầu `^` và kết thúc `$` khớp với ranh giới của từng dòng thay vì toàn bộ chuỗi.
- Source: [Phần giải thích sự khác biệt giữa 'g' và 'gm']
- Tag: [vv22]

- Fact: [CONV] Ký tự đặc biệt `\b` (word boundary) trong biểu thức chính quy được sử dụng để đảm bảo từ cần tìm kiếm là một từ độc lập, không phải là một phần của một từ khác.
- Source: [Phần giải thích về biến regex]
- Tag: [vv22]

- Fact: [CONV] Phương thức `sheet.getDataRange()` tự động xác định và trả về toàn bộ phạm vi có chứa dữ liệu trong một bảng tính Google Sheets.
- Source: [Phần giải thích hàm addHyphenAtLineStartForRange]
- Tag: [vv22]

- Fact: [CONV] Hệ tọa độ R1C1 đại diện cho vị trí ô bằng số thứ tự hàng (Row) và cột (Column). Ví dụ: R2C3 tương ứng với ô C2 trong định dạng A1 truyền thống.
- Source: [Phần giải thích về R1C1]
- Tag: [vv22]

- Fact: [CONV] Trong Google Apps Script, `getRange()` trả về một đối tượng `Range` đơn lẻ (một ô hoặc một khối ô liên tục), trong khi `getRangeList()` trả về đối tượng `RangeList` chứa danh sách nhiều phạm vi ô khác nhau.
- Source: [Phần so sánh getRange và getRangeList]
- Tag: [vv22]

- Fact: [CONV] Để kiểm tra một chuỗi có bắt đầu bằng một từ cụ thể hay không mà không dùng Regex, có thể sử dụng phương thức `indexOf(word) === 0`.
- Source: [Phần sửa lỗi code sử dụng indexOf]
- Tag: [vv22]

- Fact: [CONV] Toán tử `==` trong JavaScript thực hiện so sánh giá trị (có thể ép kiểu), trong khi `===` thực hiện so sánh nghiêm ngặt cả về giá trị và kiểu dữ liệu.
- Source: [Phần giải thích về toán tử === và ==]
- Tag: [vv22]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v15_2
  title: Định nghĩa hàm LetterCompiler đã sửa Regex
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dựa trên lỗi `AssertionError: Lists differ: [] != ['a']` mà bạn gặp phải, tôi sẽ giải thích nguyên nhân và cung cấp mã nguồn hoàn chỉnh đã được sửa lỗi.

### PHÂN TÍCH LỖI
Lỗi xảy ra do biểu thức chính quy (Regex) bạn đang dùng là `r'([a-c]).'`.
- `([a-c])`: Tìm ký tự 'a', 'b', hoặc 'c'.
- `.`: **Bắt buộc** phải có một ký tự bất kỳ theo sau ký tự vừa tìm được.

Trong trường hợp `test_single_match` với đầu vào là `"a"`, sau chữ 'a' không còn ký tự nào khác, nên dấu `.` không tìm thấy đối tượng khớp. Do đó, hàm trả về danh sách rỗng `[]` thay vì `['a']`.

**Giải pháp:** Loại bỏ dấu `.` nếu bạn chỉ muốn tìm các ký tự trong khoảng từ a đến c.

---

### MÃ NGUỒN HOÀN THIỆN (FIXED)

```python
import unittest
import re

# Định nghĩa hàm LetterCompiler đã sửa Regex
def LetterCompiler(txt):
    # Loại bỏ dấu '.' để khớp chính xác từng ký tự đơn lẻ
    result = re.findall(r'[a-c]', txt)
    return result

class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_empty_string(self):
        testcase = ""
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_no_match(self):
        testcase = "d e f g"
        expected = []
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_single_match(self):
        testcase = "a"
        expected = ['a']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_mixed_case(self):
        testcase = "A b C D a B c"
        expected = ['b', 'a', 'b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# Chạy kiểm thử
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
```

--------------------------------------------------
### TRÍCH XUẤT TRI THỨC (FACTS) - [vv15]

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

| STT | Fact | Source | Tag |
|:---:|:---|:---|:---:|
| 1 | Các dịch vụ như SMS-Activate và 5SIM cung cấp API để tự động hóa quy trình thuê số điện thoại và nhận tin nhắn OTP. | [vv15] - Section: Ví dụ sử dụng API từ dịch vụ thuê số | [vv15] |
| 2 | Thư viện `requests` trong Python là công cụ phổ biến để thực hiện các yêu cầu HTTP (GET, POST) khi tích hợp API. | [vv15] - Section: 3. Sử dụng thư viện Python requests để gọi API | [vv15] |
| 3 | API Key là chuỗi ký tự duy nhất dùng để xác thực danh tính, kiểm soát quyền truy cập và theo dõi hoạt động của người dùng trên hệ thống. | [vv15] - Section: Giải thích rõ API Key? | [vv15] |
| 4 | `unittest` là một framework tích hợp sẵn trong Python hỗ trợ viết và chạy các bài kiểm thử tự động để đảm bảo tính đúng đắn của mã nguồn. | [vv15] - Section: Giải thích code (unittest) | [vv15] |
| 5 | Trong biểu thức chính quy (Regex), ký tự `.` đại diện cho bất kỳ ký tự đơn lẻ nào ngoại trừ ký tự xuống dòng. | [vv15] - Section: 4. Giải thích mẫu biểu thức chính quy | [vv15] |
| 6 | Phương thức `self.assertEqual(a, b)` trong `unittest` được dùng để so sánh giá trị thực tế và giá trị mong đợi; nếu khác nhau sẽ gây ra lỗi `AssertionError`. | [vv15] - Section: 3. Định nghĩa phương thức kiểm thử test_basic | [vv15] |
| 7 | Việc sử dụng `argv=['first-arg-is-ignored']` và `exit=False` trong `unittest.main()` giúp chạy kiểm thử trong các môi trường tương tác như Jupyter Notebook mà không làm dừng chương trình. | [vv15] - Section: 3. Chạy tất cả các bài kiểm thử | [vv15] |

**Ghi chú:** Các thông tin về Regex và Unittest được trích xuất trực tiếp từ phần giải thích mã nguồn trong dữ liệu RAW.
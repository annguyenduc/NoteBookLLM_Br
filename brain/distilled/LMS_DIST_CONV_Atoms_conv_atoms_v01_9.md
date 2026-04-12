---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v01_9
  title: CONV_atoms_v01_9
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- Fact: [CONV] Sử dụng biến kiểm soát (ví dụ: `booting`) để bọc các lệnh `publish` dữ liệu; chỉ cho phép gửi dữ liệu khi thiết bị đã khởi động xong (`booting == 0`) để tránh gửi thông tin rác hoặc sai lệch.
- Source: Section: Khối `nếu (booting == 0) thì ...`
- Tag: [vv01]

- Fact: [CONV] Google Forms API chính thức không hỗ trợ phương thức để tạo (submit) câu trả lời, chỉ hỗ trợ lấy danh sách hoặc chi tiết các phản hồi đã có.
- Source: Section: Chính sách & rủi ro
- Tag: [vv01]

- Fact: [CONV] Apps Script cho phép tự động gửi phản hồi Google Form bằng lệnh `FormResponse.submit()` hoặc tạo các đường dẫn điền sẵn dữ liệu (pre-filled URL).
- Source: Section: Chính sách & rủi ro
- Tag: [vv01]

- Fact: [CONV] Để tự động hóa điền form của người khác mà không có quyền editor, có thể gửi HTTP POST trực tiếp tới endpoint `.../formResponse` bằng cách giả lập các tham số `entry.<id>`.
- Source: Section: Lộ trình ngắn gọn (không cần editor)
- Tag: [vv01]

- Fact: [CONV] ID của các trường dữ liệu trong Google Form (`entry.<id>`) có thể tìm thấy trong mã nguồn trang (View page source) bằng cách tìm kiếm thuộc tính `name` của các thẻ input/textarea.
- Source: Section: Bước 1: Lấy FORM_ID và các trường entry.<id>
- Tag: [vv01]

- Fact: [CONV] Các loại câu hỏi trắc nghiệm (Multiple Choice) hoặc danh sách (List) trong Google Form yêu cầu dữ liệu gửi lên phải khớp chính xác nguyên văn với các tùy chọn đã thiết lập.
- Source: Section: Bước 1: Lấy FORM_ID và các trường entry.<id>
- Tag: [vv01]

- Fact: [CONV] Việc gửi hàng loạt phản hồi tự động cần sử dụng kỹ thuật "throttle" (nghỉ ngẫu nhiên giữa các lần gửi) và cơ chế "exponential backoff" để tránh bị hệ thống Google chặn (lỗi 429 hoặc 403).
- Source: Section: Bản an toàn hơn (tự lấy token fbzx, retry, backoff)
- Tag: [vv01]

- Fact: [CONV] Token `fbzx` là một tham số bảo mật trong Google Form thường cần được trích xuất từ HTML của form và gửi kèm trong payload POST để tăng tỷ lệ thành công khi submit bằng script.
- Source: Section: Bản an toàn hơn (tự lấy token fbzx, retry, backoff)
- Tag: [vv01]

- Fact: [CONV] Các nội dung giáo dục STEM phổ biến bao gồm: Sáng chế (Tinkering), Arduino, Halocode, Thiết kế 3D, AI (Chat GPT), Yolobit, Lập trình robot (Rover/Gbot), Robot DIY và ngôn ngữ Python.
- Source: Section: USER: Form có các Head như sau
- Tag: [vv01]

- Fact: [CONV] Trong Apps Script, để tạo một Google Form mới, sử dụng `FormApp.create()`; để thêm câu hỏi thang đo sử dụng `addScaleItem()` và câu hỏi tự luận sử dụng `addParagraphTextItem()`.
- Source: Section: Cách làm nhanh (không cần add-on)
- Tag: [vv01]

- Fact: [CONV] Phương thức `setChoiceValues()` được dùng để thiết lập danh sách lựa chọn cho các câu hỏi dạng Dropdown (List) hoặc Multiple Choice trong Apps Script.
- Source: Section: Apps Script đã sửa
- Tag: [vv01]

- Fact: [CONV] Google Forms không hỗ trợ trực tiếp kiểu câu hỏi nối ý (matching); giải pháp kỹ thuật là tách nội dung nối thành nhiều câu hỏi trắc nghiệm đơn lẻ để chấm điểm.
- Source: Section: Cách A (khuyên dùng): Tạo Form tự động từ Google Sheet
- Tag: [vv01]

- Fact: [CONV] Khi xử lý dữ liệu tiếng Việt cho Google Form qua file CSV, cần sử dụng encoding `utf-8-sig` để đảm bảo các ký tự có dấu không bị lỗi hiển thị.
- Source: Section: ASSISTANT: # Create Excel and CSV templates
- Tag: [vv01]

- Fact: [CONV] Các form có tính năng reCAPTCHA, yêu cầu đăng nhập tổ chức, hoặc tải tệp lên (file upload) thường không thể tự động hóa bằng phương thức gửi HTTP POST đơn giản.
- Source: Section: Bước 1: Lấy FORM_ID và các trường entry.<id>
- Tag: [vv01]
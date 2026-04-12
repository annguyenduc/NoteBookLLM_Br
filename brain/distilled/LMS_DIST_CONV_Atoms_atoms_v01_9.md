---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v01_9
  title: atoms_v01_9
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp, tuân thủ quy tắc LOM v4.1:

- **Fact:** Trong lập trình điều khiển thiết bị IoT (như YoloBit/Arduino), việc sử dụng biến trạng thái `booting` giúp ngăn chặn thiết bị gửi dữ liệu (publish) lên server ngay khi vừa khởi động, tránh gây nhiễu hoặc lỗi logic hệ thống.
- **Source:** [v01 - Section: hối `nếu (booting == 0) thì ...`]
- **Tag:** [vv01]

- **Fact:** YoloBit, Arduino và Halocode là các nền tảng phần cứng phổ biến được sử dụng để giảng dạy STEM, tích hợp các ứng dụng IoT và Trí tuệ nhân tạo (AI).
- **Source:** [v01 - Section: USER: Form có các Head như sau]
- **Tag:** [vv01]

- **Fact:** Robot Rover, Gbot và Robot DIY là các dòng robot giáo dục được sử dụng để dạy lập trình điều khiển và thực hành lắp ráp trong các khóa học Robotics.
- **Source:** [v01 - Section: USER: Form có các Head như sau]
- **Tag:** [vv01]

- **Fact:** Lập trình AI trong giáo dục hiện nay bao gồm việc tương tác với các mô hình ngôn ngữ lớn như Chat GPT hoặc lập trình xử lý trực tiếp trên các vi điều khiển như Arduino.
- **Source:** [v01 - Section: USER: Form có các Head như sau]
- **Tag:** [vv01]

- **Fact:** Google Forms API chính thức chỉ hỗ trợ lấy danh sách phản hồi (get/list), không hỗ trợ tạo mới (submit) câu trả lời thông qua REST API cho người dùng bên ngoài.
- **Source:** [v01 - Section: Chính sách & rủi ro]
- **Tag:** [vv01]

- **Fact:** Để tự động hóa việc nộp dữ liệu lên Google Form mà không có quyền Editor, có thể sử dụng phương thức gửi HTTP POST đến endpoint `/formResponse` với các tham số định danh trường dữ liệu có dạng `entry.<id>`.
- **Source:** [v01 - Section: Bước 1: Lấy FORM_ID và các trường entry.<id>]
- **Tag:** [vv01]

- **Fact:** Tham số `fbzx` là một token bảo mật trong Google Form, thường cần được trích xuất từ mã nguồn HTML của trang `viewform` để gửi kèm trong yêu cầu POST khi thực hiện nộp form tự động nhằm tăng độ tin cậy.
- **Source:** [v01 - Section: Bản an toàn hơn (tự lấy token fbzx, retry, backoff)]
- **Tag:** [vv01]

- **Fact:** Khi thực hiện automation với số lượng lớn (ví dụ 1000 phản hồi), cần áp dụng cơ chế "Exponential Backoff" và "Jitter" (nghỉ ngẫu nhiên) để tránh bị hệ thống chặn do lỗi vượt quá tần suất yêu cầu (Error 429).
- **Source:** [v01 - Section: Bản an toàn hơn (tự lấy token fbzx, retry, backoff)]
- **Tag:** [vv01]

- **Fact:** Trong môi trường Google Apps Script, `createChoice` là phương thức thuộc các đối tượng Item cụ thể (như List, MultipleChoice, Checkbox), không phải là phương thức trực tiếp của đối tượng `FormApp` hay `Form`.
- **Source:** [v01 - Section: ASSISTANT: Đúng rồi—lỗi do mình gọi form.createChoice(...)]
- **Tag:** [vv01]

- **Fact:** Để thiết lập danh sách lựa chọn cho câu hỏi dạng Dropdown trong Apps Script, lập trình viên sử dụng phương thức `setChoiceValues([...])` truyền vào một mảng các giá trị chuỗi.
- **Source:** [v01 - Section: ASSISTANT: Đúng rồi—lỗi do mình gọi form.createChoice(...)]
- **Tag:** [vv01]

- **Fact:** Google Forms không hỗ trợ mặc định kiểu câu hỏi "Nối" (Matching); giải pháp kỹ thuật thường dùng là tách thành nhiều câu hỏi trắc nghiệm đơn (Multiple Choice) để có thể chấm điểm tự động.
- **Source:** [v01 - Section: ASSISTANT: Cách A (khuyên dùng): Tạo Form tự động từ Google Sheet]
- **Tag:** [vv01]

- **Fact:** Thiết kế 3D và lập trình Python là các học phần bổ trợ quan trọng trong hệ sinh thái giáo dục STEM, hỗ trợ cho việc phát triển các dự án Robotics và AI.
- **Source:** [v01 - Section
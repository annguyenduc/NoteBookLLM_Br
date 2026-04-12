---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v12_5
  title: CONV_atoms_v12_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ dữ liệu RAW (Volume v12) theo quy tắc LOM v4.1:

- **Fact:** [CONV] Thư mục **Arduino15** là nơi lưu trữ các thư viện (libraries), trình quản lý bo mạch (board manager) và dữ liệu cấu hình của phần mềm Arduino IDE.
- **Source:** [v12 - Section: 1. Thư mục Arduino15 (4.27 GB)]
- **Tag:** [vv12]

- **Fact:** [CONV] Để giảm dung lượng cho thư mục Arduino15, người dùng có thể thực hiện xóa các thư viện hoặc các gói bo mạch (boards) đã cài đặt nhưng không còn nhu cầu sử dụng.
- **Source:** [v12 - Section: 1. Thư mục Arduino15 (4.27 GB)]
- **Tag:** [vv12]

- **Fact:** [CONV] Các thư mục như **mblock-updater** và **@mblockbuilder-updater** chứa dữ liệu cập nhật cho phần mềm mBlock, một nền tảng lập trình Robotics và AI phổ biến cho giáo dục.
- **Source:** [v12 - Section: 2. Các thư mục nên xem xét xóa]
- **Tag:** [vv12]

- **Fact:** [CONV] Có thể sử dụng ngôn ngữ lập trình **Python** kết hợp với thư viện `os` và `pandas` để tự động hóa việc quét dung lượng các thư mục hệ thống và xuất kết quả so sánh ra file Excel (.xlsx).
- **Source:** [v12 - Section: Mã Python (get_folder_sizes)]
- **Tag:** [vv12]

- **Fact:** [CONV] Trong hệ điều hành Windows, các ứng dụng thường lưu trữ cache, dữ liệu tạm và logs tại đường dẫn `C:\Users\[Tên_User]\AppData\Local`.
- **Source:** [v12 - Section: 1. Kiểm tra thư mục cài đặt chính của Gods Unchained]
- **Tag:** [vv12]

- **Fact:** [CONV] Lệnh `DISM /Online /Get-OSUninstallWindow` được sử dụng trong Command Prompt (quyền Admin) để kiểm tra số ngày còn lại mà hệ thống cho phép người dùng quay về phiên bản Windows trước đó thông qua thư mục **Windows.old**.
- **Source:** [v12 - Section: 2. Dùng lệnh kiểm tra thời hạn lưu trữ]
- **Tag:** [vv12]

- **Fact:** [CONV] Người dùng có thể kéo dài thời gian lưu trữ bản sao hệ điều hành cũ (Windows.old) lên đến 30 ngày bằng lệnh `DISM /Online /Set-OSUninstallWindow /Value:30`.
- **Source:** [v12 - Section: 3. Tùy chỉnh thời hạn lưu trữ]
- **Tag:** [vv12]

- **Fact:** [CONV] Thư mục **pip** trong AppData\Local chứa bộ nhớ đệm (cache) của trình quản lý gói Python, giúp tăng tốc quá trình cài đặt các thư viện lập trình trong các dự án AI và Robotics.
- **Source:** [v12 - Section: Dữ liệu từ file Excel]
- **Tag:** [vv12]

- **Fact:** [CONV] Arduino IDE và mBlock là những công cụ quan trọng trong hệ sinh thái IoT và Robotics, hỗ trợ nạp code cho các mạch điều khiển như Arduino, YoloBit hoặc mBot.
- **Source:** [Nội dung suy luận từ sự xuất hiện của Arduino15 và mblock-updater]
- **Tag:** [Unverified_Source]

- **Fact:** [CONV] Khi cài đặt các thư viện Python, nếu thư mục `Scripts` không được thêm vào biến môi trường **PATH**, người dùng sẽ gặp cảnh báo và không thể gọi trực tiếp các lệnh thực thi như `f2py` từ Terminal.
- **Source:** [v12 - Section: ASSISTANT (Thông báo này xuất hiện khi bạn cài đặt một gói Python...)]
- **Tag:** [vv12]
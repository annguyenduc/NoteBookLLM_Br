Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v07) về IoT, Arduino, YoloBit, Robotics và AI, tuân thủ nghiêm ngặt quy tắc LOM v4.1:

- **Fact:** Nền tảng lập trình app.ohstem.vn là một bản triển khai tùy chỉnh dựa trên thư viện mã nguồn mở Google Blockly.
- **Source:** (v07 - Section: Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem)
- **Tag:** [vv07]

- **Fact:** Mọi thực thể trong không gian làm việc của Blockly (khối lệnh, biến, bình luận) đều được định danh bằng một ID duy nhất (UUID) tạo bởi hàm `Blockly.utils.idGenerator.genUid()`.
- **Source:** (v07 - Chương 1: Engine Cốt lõi - Hệ thống Định danh Phổ quát của Google Blockly)
- **Tag:** [vv07]

- **Fact:** Thuật toán tạo ID của Blockly sử dụng một bộ ký tự nội bộ gọi là `soup_` (bao gồm cả các ký tự đặc biệt như `$` và dấu huyền) để mở rộng không gian ID và giảm thiểu xác suất xung đột.
- **Source:** (v07 - Chương 2: Giải phẫu một Định danh - Hàm genUid và Bộ ký tự soup_)
- **Tag:** [vv07]

- **Fact:** Các phần mở rộng (extensions) cho YoloBit (như `yolobit_extension_veml6040`) được cấu trúc gồm file `config.json` để khai báo, `definition.js` để định nghĩa khối và `toolbox.xml` để hiển thị giao diện.
- **Source:** (v07 - Section: Khám phá các kho mã nguồn AITT-VN)
- **Tag:** [vv07]

- **Fact:** File `definition.js` trong các extension quy định cách ánh xạ giữa khối lệnh trực quan (`Blockly.Blocks`) và mã Python tương ứng (`Blockly.Python`).
- **Source:** (v07 - Section: Khám phá các kho mã nguồn AITT-VN)
- **Tag:** [vv07]

- **Fact:** Cấu trúc tệp dự án `.json` của OhStem chứa các trường dữ liệu quan trọng: `mode` (chế độ block), `xmlText` (cấu trúc XML của Blockly), `python` (mã MicroPython), và thông tin thiết bị (`yolobit`).
- **Source:** (v07 - Section: Phân tích file mẫu Sample_tri.json)
- **Tag:** [vv07]

- **Fact:** Chiến lược chuyển đổi từ script Python sang khối lệnh Blockly bao gồm việc sử dụng module `ast` (Abstract Syntax Tree) của Python để phân tích cú pháp và ánh xạ các node sang loại khối tương ứng.
- **Source:** (v07 - Section: Chiến lược xây dựng công cụ chuyển đổi Python -> JSON và xuất hình ảnh khối)
- **Tag:** [vv07]

- **Fact:** Để xuất hình ảnh khối lệnh từ JSON, có thể sử dụng thư viện Node.js `@blockly/blockly` để nạp workspace ảo và dùng `Blockly.utils.svgToPng` để chuyển đổi.
- **Source:** (v07 - Section: Chiến lược xây dựng công cụ chuyển đổi Python -> JSON và xuất hình ảnh khối - Mục 5)
- **Tag:** [vv07]

- **Fact:** Trong cấu trúc XML của OhStem, các khối lệnh tuần tự được kết nối thông qua thẻ `<next>`, trong khi các biểu thức logic được đặt trong thẻ `<value>` và các khối lệnh con được đặt trong thẻ `<statement>`.
- **Source:** (v07 - Section: Phân tích file mẫu Sample_tri.json)
- **Tag:** [vv07]

- **Fact:** Các dịch vụ hỗ trợ của iSpring như "iSpring RioSvr" và "iSpring Media Conversion Service" cần ở trạng thái **Running** và **Automatic** để hoạt động bình thường trên Windows.
- **Source:** (v07 - Section: Dịch vụ bằng lệnh)
- **Tag:** [vv07]

- **Fact:** Khi gặp lỗi thiếu file `.msi` khi gỡ cài đặt iSpring, có thể sử dụng công cụ "Program Install and Uninstall troubleshooter" của Microsoft hoặc dùng PowerShell để chạy lệnh gỡ cưỡng bức `msiexec /x {GUID}`.
- **Source:** (v07 - Section: ASSISTANT response regarding iSpring error)
- **Tag:** [vv07]

- **Fact:** Windows Defender nhận diện các công cụ bẻ khóa (keygen/crack) đi kèm bộ cài phần mềm là mối đe dọa mức cao với nhãn `HackTool:Win32/Keygen!rfn`.
- **Source:** (v07 - Section: ASSISTANT response regarding Windows Defender)
- **Tag:** [vv07]
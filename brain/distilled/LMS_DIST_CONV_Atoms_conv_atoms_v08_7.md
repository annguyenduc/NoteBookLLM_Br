---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v08_7
  title: CONV_atoms_v08_7
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ tài liệu **Volume v08** về hệ sinh thái OhStem, YoloBit và Google Blockly:

- **Fact:** [CONV] Nền tảng lập trình `app.ohstem.vn` là một phiên bản tùy chỉnh được xây dựng dựa trên thư viện mã nguồn mở Google Blockly.
- **Source:** [v08 - Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem]
- **Tag:** [vv08]

- **Fact:** [CONV] Mọi thực thể trong không gian làm việc của Blockly (khối lệnh, biến, bình luận) đều được định danh bằng một ID duy nhất tạo bởi hàm `Blockly.utils.idGenerator.genUid()`.
- **Source:** [v08 - Chương 1: Engine Cốt lõi - Hệ thống Định danh Phổ quát của Google Blockly]
- **Tag:** [vv08]

- **Fact:** [CONV] Chuỗi ID do Blockly tạo ra có độ dài cố định là 20 ký tự, được chọn ngẫu nhiên từ một bộ ký tự xác định.
- **Source:** [v08 - Mục 2.2: Logic Thuật toán của genUid]
- **Tag:** [vv08]

- **Fact:** [CONV] Bộ ký tự dùng để tạo ID (biến `soup_`) bao gồm 92 ký tự, trong đó có 26 chữ hoa, 26 chữ thường, 10 chữ số và 30 ký tự đặc biệt (như `!@#$%^&*()_+-=[]{};':"|,.<>/?~` và dấu huyền).
- **Source:** [v08 - Bảng 2.1: Bộ ký tự Định nghĩa của Blockly.utils.idGenerator (soup_)]
- **Tag:** [vv08]

- **Fact:** [CONV] Các ký tự đặc biệt trong ID như `$`, `'`, `"`, và dấu huyền (backtick) có thể gây lỗi cú pháp nếu không được bao bọc (quoted) hoặc thoát chuỗi (escaped) khi xử lý trong các hệ thống bên ngoài.
- **Source:** [v08 - Mục 2.3: Cảnh báo Quan trọng: Xử lý Ký tự Đặc biệt trong các Quy trình Hạ nguồn]
- **Tag:** [vv08]

- **Fact:** [CONV] Blockly sử dụng hệ thống ID phổ quát; cả biến và khối lệnh đều dùng chung một quy tắc tạo ID và chia sẻ cùng một không gian ID.
- **Source:** [v08 - Chương 3: Phân biệt Biến và Khối lệnh trong Cấu trúc JSON]
- **Tag:** [vv08]

- **Fact:** [CONV] Trong cấu trúc tệp JSON của OhStem, sự phân biệt giữa biến và khối lệnh dựa vào vị trí ngữ nghĩa (ví dụ: mảng "variables" hoặc đối tượng "blocks"), không dựa vào định dạng của ID.
- **Source:** [v08 - Chương 3: Phân biệt Biến và Khối lệnh trong Cấu trúc JSON]
- **Tag:** [vv08]

- **Fact:** [CONV] Để tái tạo ID tương thích với Blockly bằng Python, nên sử dụng mô-đun `secrets` để đảm bảo tính ngẫu nhiên cao và an toàn về mặt mật mã.
- **Source:** [v08 - Mục 4.1: Triển khai genUid bằng Python]
- **Tag:** [vv08]

- **Fact:** [CONV] Hệ sinh thái YoloBit hỗ trợ các khối lệnh điều khiển phần cứng chuyên biệt như: cảm biến siêu âm (`stemkit_ultrasonic_read`), cảm biến gas (`stemkit_gas_sensor`), cảm biến đất (`stemkit_soil_sensor`), và điều khiển động cơ robot (`rover_move_motor`).
- **Source:** [v08 - Dữ liệu RAW: XML blocks]
- **Tag:** [vv08]

- **Fact:** [CONV] Thư viện mở rộng của OhStem (AITT-VN) bao gồm các module hỗ trợ phần cứng như bàn phím `yolobit_keypad_mpr121` và xe robot `yolobit_carbit_v2`.
- **Source:** [v08 - Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem]
- **Tag:** [vv08]

- **Fact:** [CONV] Khối lệnh `math_change` trong Blockly thực hiện việc thay đổi giá trị của một biến dựa trên ID của biến đó được tham chiếu trong trường `FIELD`.
- **Source:** [v08 - Chương 3: Phân biệt Biến và Khối lệnh trong Cấu trúc JSON - Ví dụ XML]
- **Tag:** [vv08]
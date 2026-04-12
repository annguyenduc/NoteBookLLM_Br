---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v07_6
  title: atoms_v07_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v07) về IoT, Robotics và cơ chế chuyển đổi ngôn ngữ lập trình:

**1. Ánh xạ biến và hàm sang Blockly**
- Fact: Để gán biến (ví dụ `x = 5`), cần tạo block `variables_set` với trường `VAR` chứa tên biến và đầu vào `VALUE` chứa block biểu thức. Khi gọi hàm tự định nghĩa, sử dụng block `procedures_defnoreturn` cho định nghĩa và `procedures_callnoreturn` cho lệnh gọi.
- Source: v07 - Mục 2: Biến và hàm.
- Tag: [vv07]

**2. Chuyển đổi cấu trúc điều khiển và vòng lặp**
- Fact: Lệnh điều kiện `if` tương ứng với block `controls_if`, trong đó `else if` và `else` được cấu hình qua thẻ `<mutation>`. Vòng lặp `while` dùng block `controls_whileUntil` (MODE: WHILE), còn `for i in range(n)` dùng block `controls_repeat_ext`.
- Source: v07 - Mục 3: Khối điều khiển và toán học.
- Tag: [vv07]

**3. Ánh xạ thư viện Robot Rover**
- Fact: Các hàm trong thư viện `rover` (như `move`, `stop`, `servo.write_angle`) được ánh xạ trực tiếp sang các block tương ứng như `rover_move`, `rover_stop`, `rover_servo_write_angle` dựa trên định nghĩa trong file `definition.js` của extension.
- Source: v07 - Mục 4: Khối điều khiển robot và extension.
- Tag: [vv07]

**4. Định danh (ID) và tọa độ khối**
- Fact: Mỗi block và biến trong Blockly yêu cầu một ID duy nhất, có thể sinh bằng `Blockly.utils.idGenerator.genUid()`. Tọa độ `x`, `y` của khối có thể để trống để app.ohstem.vn tự động sắp xếp khi nhập file.
- Source: v07 - Mục 5: Sinh ID và vị trí khối.
- Tag: [vv07]

**5. Cấu trúc tệp JSON xuất bản cho Ohstem**
- Fact: Tệp JSON hoàn chỉnh để import vào app.ohstem.vn bao gồm các trường: `xmlText` (chứa cây XML Blockly), `python` (mã nguồn), `mode`, `name`, `extensions`, và `device`. XML phải bao bọc trong namespace `https://developers.google.com/blockly/xml`.
- Source: v07 - Mục 6: Tạo chuỗi XML/JSON hoàn chỉnh.
- Tag: [vv07]

**6. Kiến trúc đa ngôn ngữ của Microsoft MakeCode**
- Fact: MakeCode (sử dụng trong Minecraft Education Edition) sử dụng một lõi chung là Static TypeScript. Cả ngôn ngữ khối (Blocks) và Static Python đều được chuyển đổi về Static TypeScript trước khi biên dịch xuống mã máy.
- Source: v07 - Phần nghiên cứu: Kiến trúc ngôn ngữ MakeCode.
- Tag: [vv07]

**7. Cơ chế "Khối xám" (Grey Blocks)**
- Fact: Trong quá trình chuyển đổi từ code sang khối, nếu gặp cấu trúc mã không thể biểu diễn bằng block tiêu chuẩn, hệ thống sẽ chèn một "khối xám" (grey block) để giữ nguyên đoạn mã đó dưới dạng văn bản trong giao diện khối.
- Source: v07 - Phần nghiên cứu: Cơ chế đồng bộ và chuyển đổi.
- Tag: [vv07]

**8. Lưu trữ dự án trong MakeCode**
- Fact: Một dự án MakeCode thường gồm file mã nguồn (`main.ts` hoặc `main.py`) và file cấu trúc khối `main.blocks` (định dạng XML Blockly) để duy trì trạng thái workspace và vị trí các khối.
- Source: v07 - Phần nghiên cứu: Định dạng lưu trữ dự án.
- Tag: [vv07]

**9. Giới hạn của Static Python**
- Fact: Static Python trong MakeCode không phải là MicroPython đầy đủ mà là một tập con (subset) được thiết kế để ánh xạ một-một với các API TypeScript, do đó các tính năng Python phức tạp hoặc thư viện ngoài có thể không được hỗ trợ chuyển đổi sang khối.
- Source: v07 - Phần nghiên cứu: Cơ chế đồng bộ và chuyển đổi.
- Tag: [vv07]

**10. Quy trình chuyển đổi MicroPython sang Blockly**
- Fact: Quy trình đề xuất bao gồm: (1) Sử dụng bộ Parser/AST để phân tích mã Python thành cây cú pháp, (2) Duyệt cây AST để ánh xạ sang các node block tương ứng, (3) Serialize kết quả ra định dạng XML/JSON của Blockly.
- Source: v07 - Phần nghiên cứu: Đề xuất áp dụng.
- Tag: [vv07]
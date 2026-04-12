Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v07) về việc chuyển đổi mã nguồn sang khối lệnh (Blockly) cho YoloBit và Robot Rover trên nền tảng Ohstem.

### I. Ánh xạ cú pháp Python sang Blockly XML
- **Fact:** [CONV] Lệnh gán biến (`x = 5`) được chuyển thành block `variables_set`; trường `VAR` chứa tên biến và đầu vào `VALUE` chứa block biểu thức.
- **Source:** [vv07] - Mục 2: Biến và hàm.
- **Tag:** [vv07]

- **Fact:** [CONV] Việc sử dụng biến trong biểu thức được thực hiện qua block `variables_get` với trường `VAR` khớp với định danh (ID) của biến đó.
- **Source:** [vv07] - Mục 2: Biến và hàm.
- **Tag:** [vv07]

- **Fact:** [CONV] Hàm tự định nghĩa sử dụng block `procedures_defnoreturn`; tên hàm đặt tại trường `NAME` và nội dung thân hàm nằm trong thẻ `<statement name="STACK">`.
- **Source:** [vv07] - Mục 2: Biến và hàm.
- **Tag:** [vv07]

- **Fact:** [CONV] Cấu trúc điều kiện `if` sử dụng block `controls_if`; điều kiện đặt trong `<value name="IF0">` và thân lệnh trong `<statement name="DO0">`. Các nhánh `else if` và `else` được định nghĩa qua thuộc tính `mutation`.
- **Source:** [vv07] - Mục 3: Khối điều khiển và toán học.
- **Tag:** [vv07]

- **Fact:** [CONV] Vòng lặp `while` tương ứng với block `controls_whileUntil` (trường `MODE` là `WHILE`); vòng lặp `for i in range(n)` tương ứng với `controls_repeat_ext` với đầu vào `TIMES` là khối `math_number`.
- **Source:** [vv07] - Mục 3: Khối điều khiển và toán học.
- **Tag:** [vv07]

- **Fact:** [CONV] Các phép toán số học sử dụng block `math_arithmetic` (trường `OP` gồm ADD, SUB, MUL, DIV...); các phép so sánh sử dụng block `logic_compare` (trường `OP` gồm EQ, NEQ, GT, LT...).
- **Source:** [vv07] - Mục 3: Khối điều khiển và toán học.
- **Tag:** [vv07]

### II. Điều khiển Robot và Extension
- **Fact:** [CONV] Các hàm thư viện `rover` (như `move`, `stop`, `servo.write_angle`) được ánh xạ trực tiếp sang các block tương ứng như `rover_move`, `rover_stop`, `rover_servo_write_angle` theo định nghĩa trong `definition.js`.
- **Source:** [vv07] - Mục 4: Khối điều khiển robot và extension.
- **Tag:** [vv07]

- **Fact:** [CONV] Các khối cảm biến (dò line, siêu âm) trả về giá trị thường được đặt bên trong khối `logic_compare` hoặc gán vào biến.
- **Source:** [vv07] - Mục 4: Khối điều khiển robot và extension.
- **Tag:** [vv07]

### III. Cấu trúc tệp và Định dạng dữ liệu
- **Fact:** [CONV] Mỗi block và biến bắt buộc phải có một ID duy nhất, có thể sinh bằng `Blockly.utils.idGenerator.genUid()` hoặc thuật toán sinh chuỗi ngẫu nhiên tương đương.
- **Source:** [vv07] - Mục 5: Sinh ID và vị trí khối.
- **Tag:** [vv07]

- **Fact:** [CONV] Tệp JSON xuất ra để import vào app.ohstem.vn bao gồm các trường: `xmlText` (chứa chuỗi XML Blockly), `python`, `mode`, `name`, `extensions`, và `device`.
- **Source:** [vv07] - Mục 6: Tạo chuỗi XML/JSON hoàn chỉnh.
- **Tag:** [vv07]

- **Fact:** [CONV] Chuỗi XML Blockly phải được bao bọc trong thẻ `<xml>` với namespace `https://developers.google.com/blockly/xml` và có phần khai báo `<variables>` ở đầu.
- **Source:** [vv07] - Mục 6: Tạo chuỗi XML/JSON hoàn chỉnh.
- **Tag:** [vv07]

### IV. Cơ chế chuyển đổi (Tham chiếu Minecraft Education/MakeCode)
- **Fact:** [CONV] Hệ thống MakeCode (sử dụng trong Minecraft Education) chuyển đổi cả Blocks và Static Python về mã trung gian Static TypeScript trước khi biên dịch.
- **Source:** [vv07] - Phần nghiên cứu Minecraft Education Edition.
- **Tag:** [vv07]

- **Fact:** [CONV] "Khối xám" (grey block) được sử dụng để hiển thị các đoạn mã text không thể chuyển đổi trực tiếp sang khối lệnh chuẩn, giúp duy trì tính toàn vẹn của chương trình khi chuyển đổi hai chiều.
- **Source:** [vv07] - Phần nghiên cứu Minecraft Education Edition.
- **Tag:** [vv07]

- **Fact:** [CONV] Static Python trong MakeCode thực chất là một tập con (subset) của Python được ánh xạ một-một tới các API TypeScript, không phải là MicroPython đầy đủ.
- **Source:** [vv07] - Phần nghiên cứu Minecraft Education Edition.
- **Tag:** [vv07]
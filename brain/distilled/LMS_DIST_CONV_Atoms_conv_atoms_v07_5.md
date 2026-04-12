---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v07_5
  title: CONV_atoms_v07_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu về hệ sinh thái OhStem, YoloBit và nền tảng Blockly:

- **Fact:** [CONV] Nền tảng lập trình trực quan app.ohstem.vn là một triển khai tùy chỉnh dựa trên thư viện mã nguồn mở Google Blockly.
- **Source:** Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem
- **Tag:** [vv07]

- **Fact:** [CONV] Mọi thực thể trong không gian làm việc (khối lệnh, biến, bình luận) đều được quản lý bằng một định danh duy nhất (ID) để phục vụ việc tuần tự hóa sang định dạng XML hoặc JSON.
- **Source:** Chương 1: Engine Cốt lõi - Hệ thống Định danh Phổ quát của Google Blockly
- **Tag:** [vv07]

- **Fact:** [CONV] Hàm `Blockly.utils.idGenerator.genUid()` chịu trách nhiệm tạo ra các định danh duy nhất toàn cục (UUID) ngẫu nhiên trong môi trường OhStem.
- **Source:** Chương 1: Engine Cốt lõi - Hệ thống Định danh Phổ quát của Google Blockly
- **Tag:** [vv07]

- **Fact:** [CONV] Hệ thống tạo ID của Blockly sử dụng một bộ ký tự nội bộ gọi là `soup_`, bao gồm các ký tự đa dạng và ký tự đặc biệt để mở rộng không gian ID và giảm xác suất xung đột.
- **Source:** Chương 2: Giải phẫu một Định danh - Hàm genUid và Bộ ký tự soup_
- **Tag:** [vv07]

- **Fact:** [CONV] Các phần mở rộng (extensions) cho thiết bị YoloBit như `yolobit_keypad_mpr121` hoặc `yolobit_carbit_v2` được phát triển và quản lý bởi tổ chức AITT-VN trên GitHub.
- **Source:** Giới thiệu: Phân tích Chuyên sâu về Kiến trúc Môi trường Lập trình OhStem
- **Tag:** [vv07]

- **Fact:** [CONV] Cấu trúc một phần mở rộng của OhStem bao gồm file `config.json` (khai báo thư viện và cấu hình), `definition.js` (định nghĩa khối lệnh) và `toolbox.xml` (cấu trúc hiển thị khối).
- **Source:** Khám phá các kho mã nguồn AITT‑VN
- **Tag:** [vv07]

- **Fact:** [CONV] File `definition.js` trong các extension quy định cách ánh xạ giữa giao diện khối lệnh trực quan và mã nguồn MicroPython tương ứng thông qua `Blockly.Python`.
- **Source:** Khám phá các kho mã nguồn AITT‑VN
- **Tag:** [vv07]

- **Fact:** [CONV] Tệp dự án của OhStem (.json) chứa thuộc tính `xmlText`, lưu trữ toàn bộ cấu trúc các khối lệnh dưới dạng chuỗi XML theo tiêu chuẩn của Google Blockly.
- **Source:** Phân tích file mẫu (Sample_tri.json)
- **Tag:** [vv07]

- **Fact:** [CONV] Trong cấu trúc XML của dự án OhStem, tất cả các biến được khai báo tập trung trong thẻ `<variables>`, mỗi biến đi kèm với một `id` và tên hiển thị.
- **Source:** Phân tích file mẫu (Sample_tri.json)
- **Tag:** [vv07]

- **Fact:** [CONV] Các khối lệnh điều khiển Robot Rover phổ biến trên nền tảng bao gồm: `rover_move_motor` (điều khiển động cơ
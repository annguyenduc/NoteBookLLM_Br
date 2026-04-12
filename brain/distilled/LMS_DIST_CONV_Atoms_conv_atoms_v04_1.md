---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v04_1
  title: CONV_atoms_v04_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v04:

- **Fact:** [CONV] Bo mạch YoloBit sử dụng driver USB-SERIAL CH340 để thiết lập giao tiếp Serial với máy tính.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (D. Kiểm tra nhanh phần cứng/driver)]
- **Tag:** [vv04]

- **Fact:** [CONV] Lỗi cổng COM bị chiếm dụng (busy) thường do các phần mềm như Arduino IDE, VS Code (PlatformIO), các công cụ flash ESP (esptool), hoặc các tab trình duyệt khác đang mở kết nối Serial.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Giải phóng COM5)]
- **Tag:** [vv04]

- **Fact:** [CONV] Để xác định tiến trình (process) đang giữ cổng COM trên Windows, có thể sử dụng **Resource Monitor** -> tab **CPU** -> ô **Associated Handles** và gõ tên cổng (ví dụ: COM5).
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Giải phóng COM5)]
- **Tag:** [vv04]

- **Fact:** [CONV] Các cổng Bluetooth ảo (Standard Serial over Bluetooth link) thường gây nhiễu danh sách thiết bị khi kết nối các bo mạch IoT qua Web Serial.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (B. Giảm nhiễu vì cổng Bluetooth)]
- **Tag:** [vv04]

- **Fact:** [CONV] Nền tảng app.ohstem.vn sử dụng Web Serial API trên Chrome/Edge để tương tác với phần cứng; người dùng cần cấp quyền "Serial ports" trong Site Settings của trình duyệt.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (C. Thiết lập trên trình duyệt cho app.ohstem.vn)]
- **Tag:** [vv04]

- **Fact:** [CONV] Để đưa YoloBit vào chế độ Download/Bootloader (khi máy nhận nhầm driver CDC): giữ nút **BOOT (IO0)**, nhấn **RESET**, nhả **RESET**, đợi 1-2 giây rồi mới nhả **BOOT**.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (B. Khôi phục đúng giao diện USB)]
- **Tag:** [vv04]

- **Fact:** [CONV] Hiện tượng "COM ma" (ghost COM) xảy ra khi Windows lưu giữ các cổng đã từng kết nối; có thể dọn dẹp bằng cách chọn **Show hidden devices** trong Device Manager và Uninstall các mục màu xám.
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (1. Dọn các COM “ma” và hoàn nguyên nhận diện)]
- **Tag:** [vv04]

- **Fact:** [CONV] YoloBit có thể hiển thị dưới tên "Espressif CDC Device" thay vì CH340 tùy thuộc vào trạng thái firmware hoặc loại chip (như ESP32-S3).
- **Source:** [v04 - Section: Giải quyết lỗi COM5 - ASSISTANT (A. Lấy lại cổng “sạch” để web thấy được)]
- **Tag:** [vv04]

- **Fact:** [CONV] Ứng dụng KidsUp tích hợp phương pháp Montessori và AI để dạy trẻ tư duy toán học, bao gồm số đếm, so sánh lượng và phép tính trong phạm vi 50.
- **Source:** [v04 - Section: Hướng dẫn học toán trẻ 3 tuổi - ASSISTANT (Tích hợp đa phương tiện)]
- **Tag:** [vv04]

- **Fact:** [CONV] Phương pháp Glenn Doman trong giáo dục sớm sử dụng Dot Cards (thẻ chấm) để kích thích khả năng chụp hình ảnh và tư duy tính nhẩm của não phải trước khi học ký hiệu số.
- **Source:** [v04 - Section: Hướng dẫn học toán trẻ 3 tuổi - ASSISTANT (Phương pháp Glenn Doman)]
- **Tag:** [vv04]
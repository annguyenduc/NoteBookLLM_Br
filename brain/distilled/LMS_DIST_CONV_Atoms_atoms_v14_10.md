---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_10
  title: atoms_v14_10
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) kỹ thuật được trích xuất từ nguồn dữ liệu Volume v14 về IoT và module Bluetooth HC-05:

- **Fact:** Có 5 phương pháp chính để reset module HC-05: ngắt nguồn cấp, sử dụng chân EN (Enable), sử dụng lệnh AT (`AT+RESET`), nạp lại chương trình cho Arduino, hoặc gửi lệnh AT trực tiếp từ code Arduino.
- **Source:** [vv14] - Section: Cách 1 đến Cách 5.
- **Tag:** [vv14]

- **Fact:** Để reset HC-05 bằng phần cứng, chân EN (hoặc KEY) cần được kéo xuống mức LOW trong vài giây (khoảng 2 giây) và sau đó đưa lên mức HIGH.
- **Source:** [vv14] - Section: Cách 2: Sử dụng chân EN (Enable) & Giải thích mã code reset.
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+ADDR?` (hoặc `AT+ADDR`) được sử dụng để yêu cầu module HC-05 trả về địa chỉ MAC duy nhất của nó.
- **Source:** [vv14] - Section: Code Arduino để gửi lệnh AT và lưu lại địa chỉ MAC.
- **Tag:** [vv14]

- **Fact:** Địa chỉ MAC chuẩn là một mã định danh duy nhất gồm 6 byte (48 bit), biểu diễn bằng 6 cặp ký tự Hex (hệ 16), ví dụ: `XX:XX:XX:XX:XX:XX`.
- **Source:** [vv14] - Section: Cấu trúc của địa chỉ MAC chuẩn.
- **Tag:** [vv14]

- **Fact:** Một địa chỉ MAC (ví dụ: `13:EF:DE:0F`) có thể được chuyển đổi thành một chuỗi UUID giả định bằng cách kết hợp phần địa chỉ MAC với chuỗi chuẩn Bluetooth (ví dụ: `13EFDE0F-0000-1000-8000-00805F9B34FB`).
- **Source:** [vv14] - Section: Định dạng MAC và UUID.
- **Tag:** [vv14]

- **Fact:** Lệnh `AT+STATE?` cho phép kiểm tra trạng thái kết nối hiện tại của HC-05; phản hồi `+STATE:CONNECTED` nghĩa là đã kết nối, và `+STATE:DISCONNECTED` nghĩa là chưa kết nối.
- **Source:** [vv14] - Section: 1. Kiểm tra bằng cách gửi lệnh AT (phần kết nối điện thoại).
- **Tag:** [vv14]

- **Fact:** Trạng thái kết nối của HC-05 có thể quan sát qua đèn LED: LED chớp nhanh khi đang chờ kết nối và chớp chậm hoặc sáng liên tục khi đã kết nối thành công.
- **Source:** [vv14] - Section: 2. Dùng LED trạng thái.
- **Tag:** [vv14]

- **Fact:** Các lệnh AT cơ bản để cấu hình HC-05 bao gồm: `AT` (kiểm tra kết nối), `AT+NAME` (đổi tên), `AT+ROLE` (đặt chế độ Master/Slave), và `AT+PSWD` (đặt mật khẩu).
- **Source:** [vv14] - Section: Các lệnh AT cơ bản.
- **Tag:** [vv14]

- **Fact:** Để HC-05 nhận lệnh AT, module phải được đưa vào chế độ AT (thường bằng cách nhấn nút trên module khi cấp nguồn hoặc điều khiển qua chân EN/KEY).
- **Source:** [vv14] - Section: Một số lưu ý (phần lệnh AT).
- **Tag:** [vv14]
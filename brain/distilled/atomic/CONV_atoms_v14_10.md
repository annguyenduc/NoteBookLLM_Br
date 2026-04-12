Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v14 về IoT, Arduino và module Bluetooth HC-05:

- **Fact:** [CONV] Có 5 phương pháp chính để reset module HC-05: ngắt/cấp lại nguồn, sử dụng chân EN (Enable), gửi lệnh `AT+RESET`, nạp lại chương trình cho Arduino, hoặc gửi lệnh AT trực tiếp từ code Arduino.
- **Source:** [vv14] - Section: Cách 1 đến Cách 5.
- **Tag:** [vv14]

- **Fact:** [CONV] Để reset HC-05 bằng phần cứng, chân EN (hoặc KEY/STATE) cần được kéo xuống mức LOW trong vài giây rồi đưa lên mức HIGH.
- **Source:** [vv14] - Section: Cách 2: Sử dụng chân EN (Enable).
- **Tag:** [vv14]

- **Fact:** [CONV] Sơ đồ kết nối chân EN để reset: Chân EN của HC-05 nối với một chân GPIO của Arduino (ví dụ chân 7), đồng thời cần một điện trở kéo lên (pull-up resistor) nối giữa chân EN và nguồn VCC (5V).
- **Source:** [vv14] - Section: Sơ đồ kết nối (phần hướng dẫn chân EN).
- **Tag:** [vv14]

- **Fact:** [CONV] Lệnh `AT+ADDR?` (hoặc `AT+ADDR`) được sử dụng để yêu cầu module HC-05 trả về địa chỉ MAC duy nhất của nó.
- **Source:** [vv14] - Section: Code Arduino (phần lưu địa chỉ MAC).
- **Tag:** [vv14]

- **Fact:** [CONV] Địa chỉ MAC chuẩn gồm 6 byte (48 bit), định dạng bằng các cặp ký tự Hex (00-FF) cách nhau bởi dấu hai chấm, ví dụ: `XX:XX:XX:XX:XX:XX`.
- **Source:** [vv14] - Section: Cấu trúc của địa chỉ MAC chuẩn.
- **Tag:** [vv14]

- **Fact:** [CONV] Một phương pháp tạo UUID từ địa chỉ MAC của HC-05 là lấy chuỗi MAC (đã loại bỏ dấu ":") làm phần đầu và nối với hậu tố chuẩn Bluetooth (ví dụ: `13EFDE0F-0000-1000-8000-00805F9B34FB`).
- **Source:** [vv14] - Section: Định dạng MAC và UUID / Hàm macAddressToUUID.
- **Tag:** [vv14]

- **Fact:** [CONV] Lệnh `AT+STATE?` cho phép kiểm tra trạng thái kết nối hiện tại của module; trả về `+STATE:CONNECTED` nếu đã kết nối và `+STATE:DISCONNECTED` nếu chưa.
- **Source:** [vv14] - Section: Kiểm tra bằng cách gửi lệnh AT (phần xác định kết nối).
- **Tag:** [vv14]

- **Fact:** [CONV] Trạng thái đèn LED trên module HC-05 giúp nhận biết kết nối: LED chớp nhanh nghĩa là đang chờ kết nối; LED chớp chậm hoặc sáng liên tục nghĩa là đã kết nối thành công.
- **Source:** [vv14] - Section: Dùng LED trạng thái.
- **Tag:** [vv14]

- **Fact:** [CONV] Các lệnh cấu hình vai trò (Role) cho HC-05: `AT+ROLE=0` thiết lập chế độ Slave (chỉ nhận kết nối), `AT+ROLE=1` thiết lập chế độ Master (có thể tìm và kết nối thiết bị khác).
- **Source:** [vv14] - Section: Các lệnh AT cơ bản.
- **Tag:** [vv14]

- **Fact:** [CONV] Để đưa HC-05 vào chế độ nhận lệnh AT, người dùng có thể nhấn giữ nút cứng trên module khi cấp nguồn hoặc điều khiển mức logic qua chân EN/KEY.
- **Source:** [vv14] - Section: Một số lưu ý (phần GỌI LẠI CÁC LỆNH AT).
- **Tag:** [vv14]

- **Fact:** [CONV] Tốc độ Baud mặc định phổ biến để giao tiếp giữa Arduino và HC-05 qua SoftwareSerial là 9600.
- **Source:** [vv14] - Section: Code mẫu / Lưu ý về tốc độ baud.
- **Tag:** [vv14]
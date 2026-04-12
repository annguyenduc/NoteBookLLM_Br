Nếu bạn đã chỉnh **TTL = 65** mà `ping 8.8.8.8` vẫn báo **Request timed out** (trong khi `ping 172.19.176.1` vẫn thành công), điều này xác nhận 100% là: **Kết nối Laptop ↔ iPhone đã thông, nhưng iPhone không đẩy dữ liệu ra mạng Mobifone.**

Dưới đây là 3 bước cuối cùng để xử lý dứt điểm:

### 1. Kiểm tra APN "Điểm truy cập cá nhân" (Quan trọng nhất)
Với Mobifone, nếu mục này trống, iPhone sẽ phát được WiFi nhưng không có Internet.
- Trên iPhone: Vào **Cài đặt** → **Di động** → **Mạng dữ liệu di động**.
- Kéo xuống dưới cùng tìm mục **ĐIỂM TRUY CẬP CÁ NHÂN** (Personal Hotspot).
- Nhập chính xác vào ô APN: `m-wap` (hoặc `m3-world`).
- Phần Tên người dùng và Mật khẩu: **Để trống**.
- **Sau đó:** Tắt/Bật lại Dữ liệu di động và Điểm truy cập cá nhân trên iPhone.

### 2. Thử kết nối bằng cáp USB (USB Tethering)
Cách này thường ổn định hơn và đôi khi vượt qua được các lớp chặn WiFi của nhà mạng:
- Cắm cáp Lightning kết nối iPhone với Laptop.
- Trên iPhone: Vào **Điểm truy cập cá nhân** → Bật **Cho phép người khác kết nối**.
- Trên Laptop: Tắt WiFi. Windows sẽ nhận một card mạng mới qua cổng USB (thường tên là *Apple Mobile Device Ethernet*).
- Thử `ping 8.8.8.8` lại. Nếu cách này được thì card WiFi laptop hoặc cấu hình WiFi đang bị xung đột.

### 3. Xác nhận gói MBF30 có bị chặn "cứng" không
Gói **MBF30** là gói dung lượng lớn giá rẻ (30GB/7 ngày), thường được bán dưới dạng **Data Code**. Một số lô Data Code của Mobifone bị cấu hình **chặn hoàn toàn tính năng Tethering** (phát mạng) từ phía tổng đài.

**Cách kiểm tra cuối cùng:**
- Lấy một chiếc điện thoại khác (không phải laptop) kết nối vào WiFi của iPhone đó.
- Nếu điện thoại kia **cũng không vào được mạng** → Gói MBF30 này đã bị Mobifone chặn phát hotspot ở cấp độ SIM. Bạn không thể can thiệp bằng phần mềm trên laptop được nữa.
- Nếu điện thoại kia **vào được mạng** → Lỗi nằm ở Windows/Driver của laptop.

**Lời khuyên:** 
Nếu kết quả là do gói cước bị chặn (test với điện thoại khác không được), bạn nên đăng ký các gói chính thống như **D10** (10k/ngày) hoặc **ED90** để phát WiFi ổn định hơn.

Bạn có máy điện thoại nào khác ở đó để test thử bước 3 không?
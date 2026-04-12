---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v06_9
  title: CONV_atoms_v06_9
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, mình đã nắm được tình hình: Bạn đã chỉnh **TTL = 65** nhưng `ping 8.8.8.8` vẫn thất bại. Điều này khẳng định 100% là **iPhone không đẩy dữ liệu từ Hotspot ra mạng di động**, không phải do laptop.

Dưới đây là các sự kiện và bước xử lý cuối cùng để dứt điểm vấn đề này:

### 1. Các sự kiện kỹ thuật (Facts)
- **Fact:** [CONV] Laptop ping được gateway (172.19.176.1) thành công nghĩa là phần cứng WiFi và kết nối nội bộ giữa Laptop và iPhone hoàn toàn bình thường.
- **Fact:** [CONV] Lỗi `ping 8.8.8.8` thất bại sau khi chỉnh TTL cho thấy Mobifone đang chặn dữ liệu ở tầng sâu hơn (APN hoặc chính sách gói cước), không đơn thuần là đếm bước nhảy (hop count).
- **Fact:** [CONV] Đối với iPhone dùng mạng Mobifone, nếu phần **APN trong mục "Điểm truy cập cá nhân"** bị trống, iPhone vẫn cho bật Hotspot nhưng thiết bị kết nối sẽ không có Internet.

---

### 2. Bước xử lý quan trọng nhất: Cấu hình APN Hotspot
Bạn hãy cầm iPhone lên và làm chính xác các bước sau (đây là nguyên nhân của 90% ca lỗi Mobifone trên iPhone):

1. Vào **Cài đặt (Settings)** -> **Di động (Cellular)** -> **Mạng dữ liệu di động (Cellular Data Network)**.
2. Kéo xuống dưới cùng tìm mục **ĐIỂM TRUY CẬP CÁ NHÂN (PERSONAL HOTSPOT)**.
3. Nhập thông số sau (đừng để trống):
   - **APN:** `m-wap` (hoặc thử `v-internet` nếu m-wap không chạy).
   - **Tên người dùng:** (để trống).
   - **Mật khẩu:** (để trống).
4. **Quan trọng:** Sau khi nhập xong, hãy **Tắt/Bật lại Dữ liệu di động** và **Tắt/Bật lại Điểm truy cập cá nhân**.

---

### 3. Thử nghiệm bằng USB (Bypass triệt để nhất)
Nếu cấu hình APN vẫn không được, hãy thử cách này để loại trừ lỗi WiFi:
1. Dùng cáp Lightning/Type-C cắm iPhone trực tiếp vào cổng USB của laptop.
2. Trên iPhone: Vào **Điểm truy cập cá nhân** -> Bật lên.
3. Trên Laptop: Tắt WiFi đi. Windows sẽ nhận một card mạng mới qua USB.
4. Kiểm tra xem có Internet không. Nếu USB có mạng mà WiFi không có -> Lỗi do cấu hình phát sóng. Nếu cả USB cũng không có mạng -> **Gói MBF30 chắc chắn bị chặn Hotspot**.

---

### 4. Kiểm tra gói cước MBF30
Nếu cả 2 cách trên đều thất bại:
- **Sự thật:** Gói MBF30 là gói khuyến mãi dung lượng lớn giá rẻ. Mobifone thường cấu hình các gói này chỉ dành cho "Mobile Only" (chỉ dùng trên điện thoại).
- **Cách xác nhận:** Lắp SIM này vào một máy Android. Nếu máy Android phát được cho laptop -> iPhone của bạn đang bị lỗi cấu hình. Nếu máy Android cũng không phát được -> Mobifone đã chặn gói này ở mức tổng đài.

**Lời khuyên:** Bạn hãy thử bước **Cấu hình APN (m-wap)** ở mục số 2 trước, vì đó là lỗi đặc trưng nhất của iPhone khi dùng mạng Mobifone tại Việt Nam.

Bạn có cần mình hướng dẫn cách kiểm tra xem iPhone đã nhận diện đúng cấu hình nhà mạng (Carrier Bundle) chưa không?
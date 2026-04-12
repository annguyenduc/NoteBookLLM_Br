---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v14_4
  title: atoms_v14_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp:

- **Fact:** Cảm biến nhiệt độ/độ ẩm nên được đặt cách xa luồng gió trực tiếp của máy lạnh từ 1-2m và đo tại trung tâm phòng để đảm bảo tính chính xác.
- **Source:** [vv14] - Section: Gợi ý để kiểm tra.
- **Tag:** [vv14]

- **Fact:** Để xác minh sai số của cảm biến DHT11, cần so sánh kết quả đo với các thiết bị kiểm chứng khác như nhiệt kế hoặc máy đo độ ẩm chuyên dụng.
- **Source:** [vv14] - Section: Gợi ý để kiểm tra.
- **Tag:** [vv14]

- **Fact:** Trong lập trình Arduino, thư viện "DHT.h" là thư viện phổ biến được sử dụng để điều khiển và đọc dữ liệu từ cảm biến DHT11.
- **Source:** [vv14] - Section: Code Arduino (dòng #include "DHT.h").
- **Tag:** [vv14]

- **Fact:** Hàm `isnan(temperature)` hoặc `isnan(humidity)` được sử dụng để kiểm tra lỗi đọc dữ liệu từ cảm biến DHT (trả về true nếu không phải là số).
- **Source:** [vv14] - Section: Code Arduino (phần kiểm tra lỗi khi đọc dữ liệu).
- **Tag:** [vv14]

- **Fact:** Để tính giá trị trung bình tích lũy của cảm biến, cần sử dụng các biến toàn cục để lưu trữ tổng giá trị (`totalSum`) và tổng số lần đọc (`totalCount`).
- **Source:** [vv14] - Section: Giải thích Code (mục 1: Lưu tổng số lần đọc...).
- **Tag:** [vv14]

- **Fact:** Sử dụng hàm `millis()` thay vì `delay()` cho phép Arduino thực hiện các tác vụ song song (như đọc dữ liệu liên tục mỗi giây) trong khi vẫn kiểm soát được khoảng thời gian hiển thị kết quả (ví dụ: 5 giây một lần).
- **Source:** [vv14] - Section: Code Arduino (phần sử dụng millis() và interval).
- **Tag:** [vv14]

- **Fact:** Tốc độ Baud 9600 là cấu hình chuẩn thường dùng để khởi tạo giao tiếp Serial (`Serial.begin(9600)`) giữa Arduino và Serial Monitor.
- **Source:** [vv14] - Section: Code Arduino (phần setup).
- **Tag:** [vv14]

- **Fact:** Các hoạt động lắp ráp (Lego, khối gỗ) và trò chơi ghép tranh (puzzle) giúp phát triển tư duy logic, khả năng giải quyết vấn đề và kỹ năng vận động tinh – những kỹ năng nền tảng trong Robotics.
- **Source:** [vv14] - Section: Bảng Lợi ích và Khả năng Phát triển (Thứ Hai, Thứ Bảy).
- **Tag:** [vv14]

- **Fact:** Việc xem các chương trình giáo dục trên TV cho trẻ nhỏ được khuyến nghị giới hạn dưới 15 phút để đảm bảo sự tập trung và tránh tác động tiêu cực.
- **Source:** [vv14] - Section: Giải thích thêm (mục Thời gian sử dụng TV).
- **Tag:** [vv14]
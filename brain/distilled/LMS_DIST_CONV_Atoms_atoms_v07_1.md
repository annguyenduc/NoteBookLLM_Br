---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v07_1
  title: atoms_v07_1
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) về IoT, Arduino, mBlock và AI được trích xuất từ nguồn cung cấp:

- **Fact:** Trong mBlock 5, chế độ **Live mode** cho phép các biến toàn cục (For all sprites) được chia sẻ giữa nhân vật (Sprite) và thiết bị (Device/Arduino), giúp UI điều khiển được phần cứng. Ngược lại, **Upload mode** chạy độc lập trên board và không tương tác được với Sprite.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: Cách làm đúng (Live mode) & Lỗi hay gặp)
- **Tag:** [vv07]

- **Fact:** Khối lệnh `digital write pin [pin] [HIGH/LOW]` trong mBlock 5 sử dụng menu chọn cố định, không cho phép chèn trực tiếp biến số vào vị trí trạng thái HIGH/LOW.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: D3 = (blinkState) không lồng các khối block này vào nhau được)
- **Tag:** [vv07]

- **Fact:** mBlock 5 không có khối lệnh `else if` chuyên biệt; lập trình viên phải thực hiện cấu trúc này bằng cách lồng các khối `if` vào trong nhánh `else` của khối lệnh trước đó.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: mblock cũng không có khối else if mà chỉ có if - else)
- **Tag:** [vv07]

- **Fact:** Để tạo hiệu ứng chớp tắt LED mà không làm trễ (block) việc nhận diện các sự kiện khác (như click chuột), nên sử dụng biến `timer` và lệnh `reset timer` thay vì dùng lệnh `wait`.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: Lý do dùng timer thay vì wait)
- **Tag:** [vv07]

- **Fact:** Lỗi không mở được cửa sổ **Training model** trong extension Teachable Machine thường do trình duyệt chặn pop-up, chưa cấp quyền Camera, hoặc do phiên bản mBlock cũ (Makeblock đã sửa lỗi này từ bản 5.4.x).
- **Source:** (v07 - Conversation: Teachable Machine extension in mBlock - Section: 1, 2, 4)
- **Tag:** [vv07]

- **Fact:** Extension **Machine Learning 2.0** (hỗ trợ Image/Audio/Pose) là phương án thay thế cho Teachable Machine trong mBlock, cho phép huấn luyện mô hình trực tiếp trong ứng dụng và ít phụ thuộc vào cửa sổ pop-up trình duyệt.
- **Source:** (v07 - Conversation: Teachable Machine extension in mBlock - Section: 7)
- **Tag:** [vv07]

- **Fact:** Hệ thống AI điều khiển đèn LED bằng cử chỉ có thể lập trình dựa trên số lượng ngón tay: 0 ngón (tắt hết), 1 ngón (1 đèn chớp), 2 ngón (2 đèn chớp luân phiên), 3 ngón (3 đèn cùng chớp).
- **Source:** (v07 - Conversation: Bài tập 4: Lập trình hệ thống điều khiển 3 đèn LED tắt/mở bằng cử chỉ tay)
- **Tag:** [vv07]

- **Fact:** Khi kết nối LED với Arduino, cần sử dụng điện trở có giá trị từ **220–330Ω** nối tiếp với chân dương của LED để bảo vệ linh kiện.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: Mục tiêu & chế độ chạy)
- **Tag:** [vv07]

- **Fact:** Để Arduino nhận lệnh từ Sprite trong mBlock 5, các biến điều khiển phải được tạo ở chế độ **"For all sprites"**.
- **Source:** (v07 - Conversation: Thuật toán mBlock5 LED - Section: Lỗi hay gặp & cách tránh)
- **Tag:** [vv07]
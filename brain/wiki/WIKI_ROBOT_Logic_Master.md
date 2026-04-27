---
file_id: "WIKI_ROBOT_Logic_Master"
title: "Trụ cột Tư duy Lập trình Robot (xBot & Rover)"
category: "Robot"
sub_category: "Logic"
prefix: "WIKI"
tags: ["Logic", "Programming", "Algorithm", "OhStem", "mBlock"]
status: "verified"
created: "2026-04-26"
last_updated: "2026-04-26"
---

# 🧠 Trụ cột Tư duy Lập trình Robot (xBot & Rover)

Tài liệu này hệ thống hóa các mô thức lập trình (Design Patterns) và thuật toán điều khiển áp dụng cho hệ sinh thái Robot OhStem.

---

## 🔄 1. Cấu trúc Chương trình Cơ bản

Chương trình Robot thường được chia thành hai phần chính:

### A. Khởi tạo (Initialization)
- **Khối lệnh:** "Khi khởi động".
- **Nhiệm vụ:** Thiết lập giá trị ban đầu cho biến, tốc độ động cơ, màu đèn LED mặc định hoặc hiệu chuẩn cảm biến.

### B. Vòng lặp chính (Main Loop)
- **Khối lệnh:** "Vòng lặp mãi mãi" hoặc "Lặp lại cho đến khi".
- **Nhiệm vụ:** Liên tục đọc giá trị cảm biến và đưa ra phản ứng (Ví dụ: Đọc khoảng cách siêu âm -> Quyết định di chuyển).

---

## 🛤️ 2. Thuật toán Dò đường (Line Following)

Đây là bài toán kinh điển trong Robotics, sử dụng cảm biến hồng ngoại.

### Thuật toán Cơ bản (2 Mắt đọc)
- **Nếu Mắt trái thấy đen:** Rẽ trái.
- **Nếu Mắt phải thấy đen:** Rẽ phải.
- **Nếu cả hai thấy trắng:** Đi thẳng (hoặc xoay tìm vạch).

### Thuật toán Nâng cao (4 Mắt đọc - V2)
- **Ngã tư:** Cả 4 mắt đều thấy đen.
- **Lệch quỹ đạo:** Sử dụng mắt ngoài cùng để điều chỉnh góc rẽ gắt hơn (tăng tốc độ rẽ).
- **Trạng thái:** 
    - `0000`: Cả 4 mắt trên nền trắng.
    - `1111`: Cả 4 mắt trên vạch đen.

---

## 🦇 3. Thuật toán Né vật cản (Obstacle Avoidance)

Sử dụng cảm biến siêu âm để đo khoảng cách (đơn vị: cm).

### Phân vùng phản ứng
- **Vùng nguy hiểm (< 10cm):** Dừng khẩn cấp, lùi lại hoặc rẽ 90 độ.
- **Vùng cảnh báo (10cm - 30cm):** Giảm tốc độ, bật đèn LED đỏ/còi báo hiệu.
- **Vùng an toàn (> 30cm):** Di chuyển tốc độ tối đa, đèn xanh.

### Logic kết hợp
- Sử dụng cấu trúc `Nếu... thì... không thì nếu...` để xử lý nhiều ngưỡng khoảng cách khác nhau.

---

## 🛠️ 4. Cấu trúc Lập trình Chuyên sâu

### A. Hàm (My Blocks - Khối của tôi)
- **Mục đích:** Tái sử dụng đoạn mã (Ví dụ: Hàm `Dò line`, Hàm `Xoay tại chỗ`).
- **Lợi ích:** Giúp chương trình chính gọn gàng, dễ debug.

### B. Biến số (Variables)
- **Biến trạng thái:** Lưu trữ chế độ hiện tại (Ví dụ: `mode = 1` là tự động, `mode = 2` là điều khiển).
- **Biến đếm:** Đếm số lần gặp vạch ngang hoặc số lần va chạm.

### C. Đa nhiệm giả lập (Simulated Multitasking)
- Hạn chế sử dụng khối lệnh "Chờ... giây" vì nó sẽ làm treo toàn bộ logic cảm biến.
- Khuyến khích sử dụng so sánh thời gian hệ thống hoặc các khối lệnh không chặn (Non-blocking).

---

## 🎮 5. Giao tiếp & Sự kiện (Events)

- **Sự kiện Nút nhấn:** `Khi nút A được nhấn` -> Thực hiện hành động.
- **Sự kiện Remote IR:** Sử dụng cấu trúc `Nếu phím [Lên] được nhấn` trong vòng lặp chính.
- **Sự kiện Nhận tin nhắn:** Đồng bộ hóa giữa hai robot hoặc giữa Yolobit và xController.

---

## 🔗 Liên kết Wiki & Nguồn
- [[WIKI_ROBOT_Hardware_Master]] — Cấu trúc phần cứng tương ứng.
- [[KB_ROBOT_Master]] — Bản tóm tắt tri thức Robotics.
- [[WIKI_Python_Control_Structures]] — Nếu chuyển sang lập trình văn bản.

**📖 Nguồn xác thực:**
- [[brain/raw/Robot_xBot_de_trac_nghiem_1_-_xbot.md]] (Câu 18-30)
- [[brain/raw/Robot_Rover_de_trac_nghiem_1_-_rover.md]] (Câu 3-13)
- `WIKI_mBot_Programming_and_Modes.md` (Đối chiếu thuật toán)

---
**Xác nhận bởi @auditor: 2026-04-26**

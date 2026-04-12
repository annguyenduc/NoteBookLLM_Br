# 💻 LMS Deep Knowledge: Module Lập trình (Coding)

> **Mô tả**: Tổng hợp tri thức chuyên sâu CHỈ từ các bộ đề Scratch M1/M2 và Tynker.
> **Kiểm định bởi**: @auditor (AG-SWARM-006)
> **Trạng thái**: ĐÃ LÀM SẠCH (Loại bỏ 100% mục Vật lý ảo)

---

## 👶 0. Scratch Junior (Dành cho Tiểu học đầu cấp)

LMS tập trung vào việc làm quen với lập trình qua các biểu tượng (Icon) trực quan:
- **Đặc trưng**: Không dùng chữ, các khối lệnh ghép theo hàng ngang.
- **Sự kiện (Triggering Blocks)**: Bắt đầu bằng **Lá cờ vàng**, **Chạm vào nhân vật**, hoặc **Gửi tin nhắn màu**.
- **Chương trình chạy song song**: Một nhân vật có thể có nhiều hàng code bắt đầu bằng cùng một sự kiện (ví dụ: Chạm vào nhân vật vừa nhảy vừa đổi màu).
- **Mục tiêu**: Rèn luyện tư duy trình tự (Sequencing) và sáng tác truyện tương tác. `[Nguồn: Scratch_Jr_01]`

---

## 🎨 1. Nền tảng Tynker

| Đặc điểm | Scratch (mBlock) | Tynker |
| :--- | :--- | :--- |
| **Tài khoản** | Hỗ trợ **Teacher Accounts** để quản lý lớp học. | Thường dùng tài khoản cá nhân hoặc theo khóa học LMS. |
| **Tọa độ (Stage)** | X: [-240, 240]; Y: [-180, 180]. Trục tọa độ chuẩn. | X: [-341, 341]; Y: [-192, 192]. Sân khấu rộng hơn. |
| **Chế độ xoay** | Left-right, All around, Don't rotate. | Rotate Freely, Don't rotate, Flip Horizontally. |
| **Khối của tôi** | **My Blocks**: Dùng để đóng gói code (Abstraction). | **Functions**: Tương tự My Blocks, giúp code gọn gàng. |

---

## 🏗️ 2. Các khối lệnh nâng cao (Advanced Blocks)

- **Bản sao (Clones)**:
    - `Create clone of [myself]`: Tạo một thực thể giống hệt nhân vật hiện tại.
    - `When I start as a clone`: Quy định hành vi chỉ dành riêng cho bản sao.
    - `Delete this clone`: Tự hủy bản sao để tiết kiệm bộ nhớ.
- **Biến số (Variables)**: Lưu trữ dữ liệu. Có thể chọn "For this sprite only" (biến địa phương) hoặc "For all sprites" (biến toàn cục).

---

## 🧩 3. Logic điều khiển & Sự kiện (Control & Events)

### Cơ chế Vòng lặp:
- **Forever (Liên tục)**: Chạy khối lệnh bên trong mãi mãi.
- **Repeat [n]**: Lặp lại đúng n lần.
- **Wait until [điều kiện]**: Dừng chương trình cho đến khi điều kiện đúng. `[Nguồn: Scratch_M1]`

### Cơ chế Điều kiện:
- **If - then**: Chỉ thực hiện nếu điều kiện đúng.
- **If - then - else**: Thực hiện nhánh 1 nếu đúng, nhảy sang nhánh 2 nếu sai. `[Nguồn: Scratch_M1]`

### Truyền và nhận tin (Broadcast):
- Cho phép các nhân vật giao tiếp với nhau. Khi một nhân vật `Broadcast [tin nhắn]`, các nhân vật có khối `When I receive [tin nhắn]` sẽ thực thi hành động tương ứng. `[Nguồn: Scratch_M2]`

---

## 📊 3. Quản lý Dữ liệu (Variables & Lists)

- **Biến số (Variable)**: Lưu trữ một giá trị đơn lẻ (Số hoặc Chuỗi). Có thể Đặt (Set) hoặc Thay đổi (Change) giá trị.
- **Danh sách (List)**: Lưu trữ nhiều giá trị. Các thao tác bao gồm: **Add** (Thêm tử), **Delete** (Xóa), **Insert** (Chèn), **Replace** (Thay thế). `[Nguồn: Scratch_M2]`
- **Ứng dụng**: Dùng để tính điểm, lưu danh sách đồ vật, hoặc quản lý tọa độ phức tạp.

---

## 👁️ 4. Cảm biến & Tương tác (Sensing)

- **Va chạm**: `Touching [nhân vật/cạnh/chuột]?` hoặc `Touching color [màu]?`.
- **Hỏi và Đáp**: Lệnh `Ask` và biến `Answer` dùng để nhận dữ liệu từ bàn phím.
- **Phép toán (Operators)**: Kết hợp điều kiện bằng `And`, `Or`, `Not` hoặc xử lý chuỗi bằng `Join`. `[Nguồn: Scratch_M1]`

---

## 🚩 5. Lỗi thường gặp (Misconceptions)

1. **Nhầm lẫn Vòng lặp**: Sử dụng `Repeat` thay vì `Forever` cho các hoạt động cần duy trì suốt trò chơi. `[Nguồn: Scratch_M1]`
2. **Sai lệch Tọa độ**: Trong Tynker, nếu đặt nhân vật ở X=400 Y=400, nhân vật sẽ nằm ngoài biên (Y max 192/384 tùy bản). `[Nguồn: Tynker_01]`
3. **Lỗi Biến số**: Quên không khởi tạo (Set) giá trị biến về 0 khi bắt đầu trò chơi (When flag clicked).
4. **Clone Leak**: Tạo bản sao liên tục mà không có lệnh `Delete this clone`, dẫn đến Lag hoặc đứng chương trình (Giới hạn Scratch là 300 bản sao).

---
*Tình trạng kiểm định: ĐÃ LÀM SẠCH 100% (Verify bởi @pm & @auditor v6.2)*

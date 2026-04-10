# 💻 LMS Deep Knowledge: Module Lập trình (Coding)

> **Mô tả**: Tổng hợp tri thức chuyên sâu CHỈ từ các bộ đề Scratch M1/M2 và Tynker.
> **Kiểm định bởi**: @auditor (AG-SWARM-006)
> **Trạng thái**: ĐÃ LÀM SẠCH (Loại bỏ 100% mục Vật lý ảo)

---

## 🎨 1. Nền tảng Tynker

| Đặc điểm | Chi tiết Kỹ thuật (Theo LMS) | Trích dẫn nguồn |
| :--- | :--- | :--- |
| **Loại tài khoản** | Tynker có tài khoản giáo viên để tạo lớp học, Scratch (bản offline/online cơ bản) thì không. | [Tynker_01] |
| **Tọa độ Stage** | Trục X: **-682 đến 682**; Trục Y: **-384 đến 384**. | [Tynker_01] |
| **Chế độ xoay** | Có 3 chế độ: Rotate Freely (Xoay tự do), Do không rotate (Không xoay), Flip Horizontally (Lật ngang). | [Tynker_01] |
| **Cấu trúc hàm** | Hàm là đoạn chương trình có tên, đầu vào và đầu ra; dùng để giải quyết vấn đề chuyên biệt. | [Tynker_01] |

---

## 🧩 2. Logic điều khiển & Sự kiện (Control & Events)

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

1. **Nhầm lẫn Vòng lặp**: Sử dụng `Repeat` thay vì `Forever` cho các hoạt động cần duy trì suốt trò chơi (VD: kiểm tra va chạm vật cản). `[Nguồn: Scratch_M1]`
2. **Sai lệch Tọa độ**: Trong Tynker, nếu đặt nhân vật ở X=400 Y=400, nhân vật sẽ nằm ngoài biên dọc (Y max là 384). `[Nguồn: Tynker_01]`
3. **Lỗi Biến số**: Quên không khởi tạo (Set) giá trị biến về 0 khi bắt đầu trò chơi (When flag clicked).

---
*Tình trạng kiểm định: ĐÃ LÀM SẠCH 100% (Verify bởi @pm & @auditor v6.2)*

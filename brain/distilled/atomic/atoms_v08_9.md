Chào bạn, rất xin lỗi vì sự cố ngắt quãng khiến file JSON bị lỗi cấu trúc (thiếu ngoặc và thẻ đóng). Đây là lỗi do giới hạn ký tự khi hiển thị đoạn mã quá dài.

Để khắc phục triệt để, mình đã viết lại toàn bộ cấu trúc **Robotcon Standard** (PID + State Machine) vào một file duy nhất, đảm bảo tính toàn vẹn của dữ liệu để bạn import vào `app.ohstem.vn`.

### 1. Tải file cấu trúc chuẩn (Đã fix lỗi)
Bạn hãy tải file này về máy và thực hiện **Import** lại:
[**Download Rover_Robotcon_PID_Final.json**](sandbox:/mnt/data/Rover_Robotcon_PID_Final.json)

---

### 2. Giải thuật đã được tinh chỉnh trong file:

Dựa trên yêu cầu "đúng cấu trúc giải thuật robotcon", mình đã thiết lập các khối lệnh như sau:

*   **Hàm `setup_robot`**: Khởi tạo các thông số PID.
    *   `base_speed`: Tốc độ cơ sở (khuyên dùng 25-35).
    *   `Kp`: Phản ứng nhanh với sai số (thử nghiệm từ 15-25).
    *   `Kd`: Giảm rung lắc khi bám line (thử nghiệm từ 5-10).
*   **Hàm `pid_follow_line`**: 
    *   Sử dụng 4 kênh cảm biến (L1, L2, R1, R2).
    *   Tính toán sai số `e` theo trọng số: `e = (L1*3 + L2*1) - (R1*1 + R2*3)`.
    *   Điều khiển motor bằng công thức: `Trái = base + correction` và `Phải = base - correction`.
*   **Hàm `detect_intersection`**:
    *   Sử dụng biến `INTER` để đếm số mắt đọc nhận vạch đen.
    *   Nếu `INTER >= 3` (vạch ngang hoặc ngã tư), robot sẽ chuyển trạng thái.
*   **Hàm `scheduler` (Bộ lập lịch)**:
    *   Quản lý bằng biến `STATE`.
    *   Mặc định là `FOLLOW_LINE`. Khi gặp giao lộ, chuyển sang `DO_TASK` hoặc `TURN`.
    *   Cấu trúc này giúp bạn dễ dàng thêm các nhiệm vụ (Trạm 1, Trạm 2...) mà không làm rối code chính.

### 3. Cách kiểm tra sau khi Import:
1.  Mở **app.ohstem.vn** -> **YoloBit** -> **Blockly**.
2.  Chọn biểu tượng **Import** (hình mũi tên tải lên) -> Chọn file `Rover_Robotcon_PID_Final.json`.
3.  Kiểm tra xem các nhóm khối lệnh sau đã xuất hiện chưa:
    *   Khối **Bắt đầu**: Gọi `setup_robot` và đặt `STATE = "FOLLOW"`.
    *   Khối **Lặp mãi mãi**: Gọi `scheduler`.
    *   Các hàm bổ trợ nằm bên cạnh.

**Lưu ý kỹ thuật:** Nếu robot rẽ ngược hướng khi lệch line, bạn chỉ cần vào hàm `pid_follow_line` và đổi dấu ở khối `correction` (từ `+` thành `-` và ngược lại) trong lệnh điều khiển motor.

Nếu bạn cần tinh chỉnh thêm về logic rẽ tại ngã tư (rẽ trái/phải theo số lần gặp vạch), hãy cho mình biết nhé!
Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn cung cấp liên quan đến tự động hóa và lập trình Agent trong môi trường Minecraft Education (Robotics/AI):

- **Fact:** [CONV] Lệnh `agent.place(direction)` trong MakeCode chỉ có tác dụng đặt khối vào ô trống (không khí); nó không thể thực hiện thao tác "Shift-click" để gắn khối (như hopper) vào mặt cạnh của một khối khác đang tồn tại.
- **Source:** [vv08] - Đoạn phản hồi của ASSISTANT về lỗi "could not place this block".
- **Tag:** [vv08]

- **Fact:** [CONV] Trapped chest (rương bẫy) phát ra tín hiệu redstone khi mở, điều này có thể gây ra hiện tượng "khóa" hopper đặt cạnh nó, khiến vật phẩm không thể di chuyển qua hopper.
- **Source:** [vv08] - Phần "Lưu ý quan trọng với trapped chest".
- **Tag:** [vv08]

- **Fact:** [CONV] Để đảm bảo hopper kết nối đúng vào rương bằng mã lệnh Agent, phương pháp ổn định nhất là đưa Agent lên vị trí trên nóc rương và sử dụng lệnh `agent.place(DOWN)`.
- **Source:** [vv08] - Phần "Cách xử lý chuẩn (1)".
- **Tag:** [vv08]

- **Fact:** [CONV] Cú pháp lệnh `/setblock` để ép hướng hopper trong Minecraft Education Edition yêu cầu sử dụng block states trong dấu ngoặc vuông với định dạng: `hopper ["facing_direction" = giá_trị]`.
- **Source:** [vv08] - Đoạn hội thoại về lỗi syntax và xác nhận thành công của USER.
- **Tag:** [vv08]

- **Fact:** [CONV] Quy ước giá trị hướng `facing_direction` cho hopper trên phiên bản Bedrock/Education là: 2 (North/Bắc), 3 (South/Nam), 4 (West/Tây), 5 (East/Đông).
- **Source:** [vv08] - Phần "Bản lệnh nhanh (dùng số dữ liệu)".
- **Tag:** [vv08]

- **Fact:** [CONV] Hàm `agent.interact(direction)` cho phép Agent thực hiện hành động tương tác tương đương với việc người chơi nhấp chuột phải vào một khối (ví dụ: mở cửa, gạt cần gạt, bấm nút).
- **Source:** [vv08] - Phần giải thích về hàm "interact".
- **Tag:** [vv08]

- **Fact:** [CONV] Khi sử dụng `player.execute()` trong MakeCode JavaScript để chạy các lệnh chứa dấu ngoặc kép (như block states), cần bao bọc toàn bộ chuỗi lệnh bằng dấu nháy đơn `'...'` để tránh lỗi trình phân tích cú pháp.
- **Source:** [vv08] - Phần "Cách viết đúng trong MakeCode (JS)".
- **Tag:** [vv08]

- **Fact:** [CONV] Agent không có trạng thái "sneak" (đi rón rén/Shift) như người chơi, do đó không thể đặt hopper trực tiếp vào cạnh rương theo cách thủ công thông thường mà phải dùng giải pháp đặt từ trên xuống hoặc dùng lệnh `/setblock`.
- **Source:** [vv08] - Phần "Chuẩn luôn: khi player đặt hopper...".
- **Tag:** [vv08]
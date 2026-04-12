Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW (Volume v08) về Robotics và lập trình Agent trong Minecraft Education Edition:

- **Fact:** Để đặt Hopper (phễu) vào Rương (Chest) bằng Agent, cần chọn ô chứa Hopper và sử dụng lệnh `agent.place(FORWARD)`. Nếu vòi phễu không chĩa đúng hướng, cần phá bỏ, thay đổi vị trí Agent và đặt lại.
- **Source:** [vv08] - Section: MakeCode JavaScript/Python.
- **Tag:** [vv08]

- **Fact:** Trapped Chest (rương bẫy) phát ra tín hiệu Redstone khi mở, điều này có thể gây ra hiện tượng "khóa" Hopper kế bên, khiến vật phẩm không thể lưu thông.
- **Source:** [vv08] - Section: Lưu ý quan trọng với trapped chest.
- **Tag:** [vv08]

- **Fact:** Lệnh `agent.place(direction)` của Agent chỉ thực hiện đặt block vào ô trống (không khí); nó không có khả năng "gắn lên mặt khối đang chiếm chỗ" (Shift-click) như người chơi.
- **Source:** [vv08] - Assistant response: "Bị lỗi không đặt được hopper".
- **Tag:** [vv08]

- **Fact:** Phương pháp đáng tin cậy nhất để Agent kết nối Hopper vào Chest là di chuyển Agent lên trên nóc rương và sử dụng lệnh `agent.place(DOWN)`.
- **Source:** [vv08] - Assistant response: "Cách xử lý chuẩn".
- **Tag:** [vv08]

- **Fact:** Trong Minecraft Bedrock/Education Edition, hướng của Hopper được xác định bởi thuộc tính `facing_direction` với các giá trị: 0=Down, 2=North, 3=South, 4=West, 5=East.
- **Source:** [vv08] - Assistant response: "Bản lệnh nhanh".
- **Tag:** [vv08]

- **Fact:** Cú pháp lệnh `/setblock` hiện đại trong Minecraft Education yêu cầu khai báo block states trong dấu ngoặc vuông, ví dụ: `minecraft:hopper[facing_direction=5]`. Việc sử dụng số tile data cũ (ví dụ: `hopper 5`) sẽ gây lỗi syntax.
- **Source:** [vv08] - Assistant response: "Cú pháp đúng".
- **Tag:** [vv08]

- **Fact:** Khi sử dụng `player.execute()` trong MakeCode để chạy lệnh có chứa dấu ngoặc kép (block states), nên sử dụng dấu nháy đơn bao ngoài toàn bộ chuỗi để tránh lỗi parser: `player.execute('setblock ... ["facing_direction" = 3] ...')`.
- **Source:** [vv08] - Assistant response: "Cách viết đúng trong MakeCode (JS)".
- **Tag:** [vv08]

- **Fact:** Lệnh `agent.interact(direction)` mô phỏng hành động nhấp chuột phải của người chơi, cho phép Agent tương tác với các đối tượng như cửa, nút bấm, cần gạt, hoặc rương.
- **Source:** [vv08] - Section: interact.
- **Tag:** [vv08]

- **Fact:** Chế độ `PlaceOnMove` của Agent nếu bật khi đang căn hướng có thể gây ra việc đặt block lung tung; trong khi `PlaceFromAnySlot` cho phép Agent tự lấy vật phẩm từ các ô khác nếu ô đang chọn bị trống.
- **Source:** [vv08] - Section: Lưu ý quan trọng với trapped chest.
- **Tag:** [vv08]

- **Fact:** Một Hopper sẽ bị ngừng hoạt động (không hút/đẩy đồ) nếu nó nhận được tín hiệu Redstone từ các nguồn lân cận hoặc từ chính Trapped Chest đang mở.
- **Source:** [vv08] - Assistant response: "Checklist nhanh nếu vẫn lỗi".
- **Tag:** [vv08]
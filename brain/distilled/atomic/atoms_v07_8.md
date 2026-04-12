Chào bạn, tôi là @scout. Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu v07 liên quan đến lập trình robot (Agent) và tự động hóa trong môi trường Minecraft Education:

- **Fact:** Nhóm lệnh `builder` trong Minecraft Education Edition chỉ có thể đặt các khối (blocks) như STONE, RAIL, CHEST; không thể đặt các thực thể (entities) như minecart.
- **Source:** Đoạn trả lời của ASSISTANT về nhóm lệnh builder.
- **Tag:** [vv07]

- **Fact:** Agent trong Code Builder không thể đặt minecart trực tiếp từ ô đồ lên đường ray vì minecart là thực thể (entity), trong khi lệnh `agent.place` bị giới hạn ở các khối có thể đặt được.
- **Source:** Mục "ASSISTANT: Ngắn gọn: Không có cách nào đặt minecart trực tiếp...".
- **Tag:** [vv07]

- **Fact:** Để tạo minecart thông qua Code Builder, lập trình viên có thể sử dụng hàm `player.execute` để chạy lệnh `/summon minecart` hoặc `/summon hopper_minecart` tại vị trí chỉ định.
- **Source:** Mục "Cách làm đúng để có minecart (Bedrock/Education)".
- **Tag:** [vv07]

- **Fact:** Một phương pháp tự động hóa không dùng lệnh để đặt minecart là sử dụng Dispenser chứa item minecart hướng vào đường ray; khi có tín hiệu kích hoạt, Dispenser sẽ thực hiện việc đặt minecart lên ray.
- **Source:** Mục "2) Dùng Dispenser + redstone".
- **Tag:** [vv07]

- **Fact:** Đường ray kích hoạt (activator rail) có khả năng điều khiển trạng thái của hopper minecart: khóa khả năng hút đồ khi đường ray đang bật và mở lại khi đường ray tắt.
- **Source:** Mục "Lưu ý cho hopper minecart".
- **Tag:** [vv07]

- **Fact:** Khi sử dụng lệnh `/setblock` để đặt Dispenser, trạng thái hướng (block state) được xác định qua tham số `facing_direction` với các giá trị: 2 (Bắc), 3 (Nam), 4 (Tây), 5 (Đông).
- **Source:** Mục "Mẹo: nếu hướng của Dispenser chưa đúng".
- **Tag:** [vv07]
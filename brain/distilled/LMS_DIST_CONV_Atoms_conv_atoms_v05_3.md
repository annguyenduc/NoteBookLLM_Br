---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v05_3
  title: CONV_atoms_v05_3
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu Volume v05 liên quan đến Robotics và thiết kế 3D:

- **Fact:** [CONV] Trong Tinkercad 3D Editor, **Bundle group** là loại nhóm "mềm" dùng để gom các hình khối lại nhằm thuận tiện cho việc di chuyển và tổ chức mà không làm hợp nhất hình học hay thực hiện các phép tính toán boolean (như khoan lỗ).
- **Source:** Conversation: Phân biệt group Tinkercad - Assistant response (Bảng so sánh).
- **Tag:** [vv05]

- **Fact:** [CONV] **Union group** trong Tinkercad là nhóm "cứng" thực hiện phép toán boolean để hợp nhất các khối (Solid) hoặc sử dụng khối rỗng (Hole) để cắt vật liệu, tạo ra một mesh thống nhất phục vụ cho việc in 3D.
- **Source:** Conversation: Phân biệt group Tinkercad - Assistant response (Bảng so sánh).
- **Tag:** [vv05]

- **Fact:** [CONV] Khi thực hiện lệnh Union trên Tinkercad, phần mềm sẽ hiển thị **viền đỏ** xung quanh đối tượng để báo hiệu hệ thống đang thực hiện các bước tính toán hình học phức tạp.
- **Source:** Conversation: Phân biệt group Tinkercad - Assistant response (Bảng so sánh).
- **Tag:** [vv05]

- **Fact:** [CONV] Để giữ lại màu sắc riêng biệt của từng khối sau khi đã thực hiện lệnh Union trong Tinkercad, người dùng cần kích hoạt tính năng **Multicolor** trong bảng thuộc tính.
- **Source:** Conversation: Phân biệt group Tinkercad - Assistant response (Bước 3 & 4).
- **Tag:** [vv05]

- **Fact:** [CONV] Thông số nhiệt độ khuyến nghị khi in nhựa **PLA** trên máy **Elegoo Neptune 4** là khoảng 210°C - 220°C cho đầu phun (Nozzle) và 60°C cho bàn in (Bed) để tối ưu độ bám dính.
- **Source:** Conversation: Tìm thông số in PLA - Bảng thông số in đề xuất.
- **Tag:** [vv05]

- **Fact:** [CONV] Đối với các máy in 3D sử dụng hệ thống đùn trực tiếp (Direct Drive) như Elegoo Neptune 4, thông số **rút sợi (Retraction)** tối ưu thường được thiết lập ở mức 0,5 mm với tốc độ 45 mm/s.
- **Source:** Conversation: Tìm thông số in PLA - Bảng thông số in đề xuất.
- **Tag:** [vv05]

- **Fact:** [CONV] Mô hình cơ học **Easy Strandbeest** sử dụng các khớp nối dạng **in liền (print-in-place)**; sau khi hoàn tất quá trình in, cần thực hiện thao tác bẻ nhẹ hoặc dùng dao mỏng lách vào khe hở để tách các phần nhựa thừa bị dính.
- **Source:** Conversation: Tìm thông số in PLA - Mẹo in và lưu ý theo tỷ lệ kích thước.
- **Tag:** [vv05]

- **Fact:** [CONV] Việc sử dụng một giọt **dầu bôi trơn** nhỏ vào các khớp nối của mô hình robot sau khi in 3D giúp cơ cấu vận hành trơn tru và giảm ma sát.
- **Source:** Conversation: Tìm thông số in PLA - Mẹo in và lưu ý theo tỷ lệ kích thước.
- **Tag:** [vv05]

- **Fact:** [CONV] Để cân bằng giữa tốc độ in và chất lượng chi tiết, có thể thiết lập **chiều cao lớp (layer height)** 0,2 mm cho các bộ phận lớn và giảm xuống 0,12 mm cho các chi tiết đòi hỏi độ chính xác cao như trục khớp.
- **Source:** Conversation: Tìm thông số in PLA - Tối ưu tốc độ vs. chất lượng.
- **Tag:** [vv05]

- **Fact:** [CONV] Khi in các chi tiết có diện tích tiếp xúc nhỏ hoặc dễ bị bong khỏi bàn in (như chân của Strandbeest), việc sử dụng tính năng **Brim** và tăng nhiệt độ bàn in là giải pháp hiệu quả để chống cong vênh.
- **Source:** Conversation: Tìm thông số in PLA - Độ bám và biến dạng khi in nhiều chi tiết.
- **Tag:** [vv05]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v11_5
  title: atoms_v11_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nội dung thảo luận về lập trình HaloCode trên mBlock (Volume v11):

- **Fact:** Trong môi trường mBlock, việc sử dụng biến số bên trong khối lấy số ngẫu nhiên có thể khiến hàm tự động chuyển từ `random.randint()` (số nguyên) sang `random.uniform()` (số thực), gây lỗi khi so sánh vị trí đèn LED.
- **Source:** [v11 - Section: Dùng random.randint() thay vì random.uniform()]
- **Tag:** [vv11]

- **Fact:** mBlock không hỗ trợ kiểu dữ liệu Boolean (`True`/`False`) một cách trực tiếp trong một số ngữ cảnh lập trình thiết bị; do đó, nên sử dụng số nguyên (0 và 1) để làm biến cờ (flag) kiểm tra trạng thái thắng/thua.
- **Source:** [v11 - Section: ✅ Sửa lại để chạy tốt trên mBlock]
- **Tag:** [vv11]

- **Fact:** Để tạo hiệu ứng vòng lặp đèn LED chạy tròn như kim đồng hồ (từ 1 đến 12), công thức toán học tối ưu là `((vị trí hiện tại + bước nhảy - 1) mod 12) + 1`.
- **Source:** [v11 - Section: Tôi muốn xây dựng một hàm số chỉ chạy từ 1-12 trên vòng tròn như kim đồng hồ]
- **Tag:** [vv11]

- **Fact:** Khi lập trình HaloCode bằng Python, chỉ số (index) của đèn LED chạy từ 0 đến 11. Để bật nhiều LED mục tiêu liền kề mà không bị lỗi khi vượt quá giới hạn, cần sử dụng phép toán chia lấy dư: `(Target_LED + i) % 12`.
- **Source:** [v11 - Section: 🛑 Lỗi 2: So sánh sai trong check_result()]
- **Tag:** [vv11]

- **Fact:** Do mBlock thiếu khối ép kiểu số nguyên (`int`), người dùng có thể sử dụng khối `round()` (làm tròn) hoặc phép toán `// 1` (chia lấy phần nguyên) để đảm bảo biến số không bị hiểu lầm là số thực khi thực hiện các vòng lặp hoặc chọn số ngẫu nhiên.
- **Source:** [v11 - Section: Tôi không có chỗ nào để chuyển được thành số nguyên]
- **Tag:** [vv11]

- **Fact:** Trong cấu trúc vòng lặp `count with i from 0 to difficult` của mBlock, vòng lặp sẽ thực hiện `difficult + 1` lần. Để lặp đúng số lần mong muốn, giá trị kết thúc nên được đặt là `difficult - 1`.
- **Source:** [v11 - Section: 🚀 Tối ưu hàm show_target_leds()]
- **Tag:** [vv11]

- **Fact:** Cơ chế điều chỉnh độ khó tự động trong trò chơi Cyclone trên HaloCode được thực hiện bằng cách giảm số lượng LED mục tiêu sáng (biến `difficulty`) sau mỗi lần người chơi thắng, cho đến khi đạt mức tối thiểu là 1 LED.
- **Source:** [v11 - Section: 1️⃣ Tạo nhiều cấp độ khó]
- **Tag:** [vv11]

- **Fact:** Để tránh lỗi không bao giờ thắng khi nạp code vào HaloCode, giá trị mục tiêu (`Target_LED`) phải được đảm bảo là số nguyên để khớp hoàn toàn với vị trí hiện tại của LED (`LED_pos`).
- **Source:** [v11 - Section: 🛑 Lỗi 1: random.uniform(0, 12 - difficult) (Sai kiểu dữ liệu)]
- **Tag:** [vv11]
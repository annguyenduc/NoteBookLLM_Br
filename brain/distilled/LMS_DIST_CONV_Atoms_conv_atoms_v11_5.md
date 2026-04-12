---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v11_5
  title: CONV_atoms_v11_5
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v11) về IoT và lập trình HaloCode/mBlock:

- **Fact:** [CONV] HaloCode tích hợp vòng tròn gồm 12 đèn LED RGB, thường được lập trình với chỉ số từ 0 đến 11.
- **Source:** [vv11] - Section: Mã hoàn chỉnh (Tương thích hoàn toàn với mBlock)
- **Tag:** [vv11]

- **Fact:** [CONV] mBlock không hỗ trợ kiểu dữ liệu Boolean (`True`/`False`) một cách trực tiếp trong một số ngữ cảnh lập trình thiết bị, do đó nên sử dụng số nguyên (ví dụ: `win_flag = 1` cho thắng, `0` cho thua) để thay thế.
- **Source:** [vv11] - Section: Sửa lại để chạy tốt trên mBlock
- **Tag:** [vv11]

- **Fact:** [CONV] Để tạo hiệu ứng vòng lặp LED (khi vượt quá LED số 11 sẽ quay lại LED số 0), sử dụng toán tử modulo: `(vị trí hiện tại + bước nhảy) % 12`.
- **Source:** [vv11] - Section: Sửa check_result() để kiểm tra thắng/thua đúng cấp độ
- **Tag:** [vv11]

- **Fact:** [CONV] Trong môi trường mBlock, hàm `random.randint()` có thể bị tự động chuyển thành `random.uniform()` (trả về số thực) nếu tham số truyền vào chứa biến số không được xác định rõ là số nguyên.
- **Source:** [vv11] - Section: Lỗi 1: random.uniform(0, 12 - difficult) (Sai kiểu dữ liệu)
- **Tag:** [vv11]

- **Fact:** [CONV] Để ép kiểu số nguyên (integer casting) trong mBlock khi không có khối lệnh `int()`, có thể sử dụng các giải pháp thay thế như hàm `round()`, phép chia lấy phần nguyên `// 1`, hoặc thực hiện phép tính `(biến - 0)`.
- **Source:** [vv11] - Section: Cách sửa lỗi random.uniform() trong mBlock & Tôi không có chỗ nào để chuyển được thành số nguyên
- **Tag:** [vv11]

- **Fact:** [CONV] Công thức để ánh xạ một dãy số tăng dần vào vòng tròn 12 vị trí (tương tự kim đồng hồ từ 1-12) là: `((giá trị - 1) mod 12) + 1`.
- **Source:** [vv11] - Section: Tôi muốn xây dựng một hàm số chỉ chạy từ 1-12 trên vòng tròn như kim đồng hồ
- **Tag:** [vv11]

- **Fact:** [CONV] Trong lập trình kéo thả mBlock, vòng lặp "count i from 0 to n" sẽ thực hiện `n + 1` lần (bao gồm cả giá trị n); để lặp đúng `n` lần, cần đặt giới hạn là `n - 1`.
- **Source:** [vv11] - Section: Tối ưu hàm show_target_leds()
- **Tag:** [vv11]

- **Fact:** [CONV] Cảm biến chạm trên HaloCode (ví dụ: `touchpad0`) được sử dụng để bắt sự kiện tương tác người dùng trong các trò chơi yêu cầu phản xạ nhanh như Cyclone.
- **Source:** [vv11] - Section: Mã hoàn chỉnh (Tương thích hoàn toàn với mBlock)
- **Tag:** [vv11]
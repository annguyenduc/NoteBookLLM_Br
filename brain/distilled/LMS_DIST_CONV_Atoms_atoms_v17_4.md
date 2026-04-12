---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v17_4
  title: atoms_v17_4
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật về lập trình Python (nền tảng cho AI, YoloBit và Robotics) được trích xuất từ dữ liệu RAW của Volume v17:

- **Fact:** Các nền tảng trực tuyến phổ biến để chạy và kiểm tra mã Python mà không cần cài đặt bao gồm: Repl.it, Ideone, PythonAnywhere và Trinket.
- **Source:** [vv17] - Section: ASSISTANT (Phần liệt kê các trang web chạy thử code).
- **Tag:** [vv17]

- **Fact:** Cơ chế hoạt động của các trình biên dịch Python trực tuyến: Mã nguồn được gửi đến máy chủ (server), thực thi trong môi trường Python tại đó và trả kết quả về trình duyệt người dùng.
- **Source:** [vv17] - Section: ASSISTANT (Giải thích về cách code chạy trên web).
- **Tag:** [vv17]

- **Fact:** Có 3 phương pháp chính để theo dõi từng bước (debug) chương trình Python: Sử dụng công cụ gỡ lỗi trong IDE (như PyCharm, VS Code), sử dụng tính năng Debug của các trang web (như Trinket), hoặc thêm câu lệnh `print` để in giá trị biến.
- **Source:** [vv17] - Section: ASSISTANT (Phần hướng dẫn xem từng bước đoạn lệnh).
- **Tag:** [vv17]

- **Fact:** Python Tutor là công cụ chuyên biệt cho phép "Visualize Execution" (trực quan hóa quá trình thực thi), giúp người dùng xem biểu đồ thay đổi của các biến qua từng dòng lệnh.
- **Source:** [vv17] - Section: ASSISTANT (Hướng dẫn về Python Tutor).
- **Tag:** [vv17]

- **Fact:** Đệ quy (Recursion) là kỹ thuật định nghĩa hàm bằng cách gọi lại chính nó. Một hàm đệ quy cần có "Base case" (điều kiện dừng, ví dụ: `n < 1`) để tránh vòng lặp vô hạn.
- **Source:** [vv17] - Section: ASSISTANT (Giải thích về hàm sum_positive_numbers và factorial).
- **Tag:** [vv17]

- **Fact:** Hàm `range(start, stop, step)` trong Python tạo ra một dãy số bắt đầu từ `start`, kết thúc trước `stop` (không bao gồm `stop`) và nhảy theo khoảng cách `step`.
- **Source:** [vv17] - Section: ASSISTANT (Giải thích về range(1, 10, 3) và range(6, 18, 3)).
- **Tag:** [vv17]

- **Fact:** Sự khác biệt cơ bản giữa vòng lặp `while` và `for`: `while` lặp dựa trên một điều kiện logic còn đúng (True), trong khi `for` lặp qua một chuỗi các phần tử (sequence).
- **Source:** [vv17] - Section: ASSISTANT (Conversation: Loop Differences).
- **Tag:** [vv17]

- **Fact:** Trong kỹ thuật cắt chuỗi (Slicing strings), nếu chỉ số bắt đầu (starting index) là số âm, Python sẽ đếm ngược từ cuối chuỗi trở về trước.
- **Source:** [vv17] - Section: ASSISTANT (Câu hỏi về slicing strings).
- **Tag:** [vv17]

- **Fact:** Lỗi vòng lặp vô hạn (Infinite loop) thường xảy ra trong vòng lặp `while` khi biến điều kiện không được cập nhật (ví dụ: quên tăng giá trị biến đếm `x += 1`) bên trong thân vòng lặp.
- **Source:** [vv17] - Section: ASSISTANT (Giải thích lỗi count_to_ten).
- **Tag:** [vv17]

- **Fact:** YoloBit và các hệ thống Robotics thường sử dụng ngôn ngữ MicroPython (một biến thể của Python) để điều khiển thiết bị, do đó các logic về vòng lặp và điều kiện trong Python là kiến thức nền tảng bắt buộc.
- **Source:** [Nội dung suy luận từ ngữ cảnh lập trình thiết bị]
- **Tag:** [Unverified_Source]
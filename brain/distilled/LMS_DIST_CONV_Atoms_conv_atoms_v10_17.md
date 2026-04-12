---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_17
  title: CONV_atoms_v10_17
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp (Volume v10) theo quy tắc LOM v4.1:

- Fact: [CONV] Thư viện `shutil` trong Python cung cấp hàm `disk_usage` để kiểm tra các thông số về dung lượng ổ đĩa (tổng dung lượng, dung lượng đã dùng, dung lượng trống).
- Source: (vv10 - Section: Practical Application of diff and patch - Code block 1)
- Tag: [vv10]

- Fact: [CONV] Việc sử dụng từ khóa `return` bên ngoài một hàm (function) trong Python sẽ gây ra lỗi `SyntaxError: 'return' outside function`.
- Source: (vv10 - Section: Practical Application of diff and patch - SyntaxError output)
- Tag: [vv10]

- Fact: [CONV] Để kết thúc một script Python và trả về mã trạng thái (exit status) cho hệ điều hành, lập trình viên sử dụng `sys.exit(0)` cho thành công hoặc `sys.exit(1)` cho lỗi, thay vì dùng `return`.
- Source: (vv10 - Section: Practical Application of diff and patch - Instructor notes)
- Tag: [vv10]

- Fact: [CONV] Lệnh `diff -u` được sử dụng để tạo ra một file bản vá (patch file) dưới định dạng "unified diff", ghi lại sự khác biệt giữa file gốc và file đã sửa đổi.
- Source: (vv10 - Section: Practical Application of diff and patch - Command output)
- Tag: [vv10]

- Fact: [CONV] Lệnh `patch` kết hợp với toán tử `<` (ví dụ: `patch file.py < file.diff`) được dùng để tự động áp dụng các thay đổi từ file diff vào file nguồn.
- Source: (vv10 - Section: Practical Application of diff and patch - Final command)
- Tag: [vv10]

- Fact: [CONV] Trong các hệ thống nhúng hoặc Robotics chạy Linux, việc giám sát tài nguyên hệ thống (như disk usage) thông qua script Python là một kỹ thuật phổ biến để đảm bảo tính ổn định của thiết bị.
- Source: [Unverified_Source] (Dựa trên ngữ cảnh ứng dụng thực tế của script disk_usage.py trong bài học).
- Tag: [vv10]

--------------------------------------------------
Tôi đã lưu các sự kiện này vào hệ thống tri thức. Bạn có muốn tôi trích xuất thêm thông tin nào từ các đoạn mã nguồn cụ thể trong dữ liệu này không?
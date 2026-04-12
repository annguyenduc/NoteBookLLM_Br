---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_30
  title: CONV_atoms_v10_30
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v10) liên quan đến kỹ thuật hệ thống và lập trình (nền tảng cho IoT, Robotics và AI), tuân thủ nghiêm ngặt quy tắc LOM v4.1:

| Fact | Source | Tag |
|:---|:---|:---|
| [CONV] Lệnh `diff` được sử dụng để tìm sự khác biệt giữa hai tệp tin. | [v10 - Section: The diff command] | [vv10] |
| [CONV] Sử dụng tham số `-u` với lệnh `diff` (`diff -u`) để tìm các dòng khác biệt giữa hai tệp tin theo định dạng dễ đọc hơn (unified format). | [v10 - Section: Using diff -u] | [vv10] |
| [CONV] Lệnh `patch` được sử dụng để áp dụng các thay đổi từ một tệp bản vá (patch file) vào một tệp cấu hình hoặc tệp mã nguồn gốc. | [v10 - Question 1] | [vv10] |
| [CONV] Cú pháp chuẩn để áp dụng bản vá là: `patch file_can_sua < file_patch`. | [v10 - Question 1] | [vv10] |
| [CONV] Để tạo một tệp bản vá (diff file) chứa sự khác biệt giữa tệp gốc và tệp đã chỉnh sửa, sử dụng cú pháp: `diff file_goc file_da_sua > ten_file.diff`. | [v10 - Question 2] | [vv10] |
| [CONV] Lệnh `wdiff` có khả năng làm nổi bật các từ cụ thể bị thay đổi trong một tệp thay vì chỉ so sánh theo từng dòng như lệnh `diff` thông thường. | [v10 - Question 3] | [vv10] |
| [CONV] Trong Python, module `sys` cung cấp lệnh `exit` (`sys.exit()`) để xác định giá trị trả về (exit code) của một kịch bản khi kết thúc chương trình. | [v10 - Question 4] | [vv10] |
| [CONV] Để sử dụng lệnh `patch`, ngoài tệp gốc, người dùng bắt buộc phải có tệp Diff (Diff file). | [v10 - Question 5] | [vv10] |
| [CONV] Trong môi trường Linux (như Ubuntu/WSL thường dùng cho Robotics), lệnh `ln -s` tạo liên kết tượng trưng (symbolic link) để rút gọn đường dẫn truy cập thư mục mà không làm nhân đôi dữ liệu. | [v10 - Assistant Context/User Interaction] | [Unverified_Source] |
| [CONV] Việc quản lý các bản vá (patching) là kỹ năng quan trọng trong việc bảo trì mã nguồn cho các hệ thống nhúng và robot khi cần cập nhật các thay đổi nhỏ mà không cần gửi lại toàn bộ mã nguồn lớn. | [Nghiệm lý kỹ thuật hệ thống] | [Unverified_Source] |

--------------------------------------------------
**Ghi chú hệ thống:** Các thông tin về `diff` và `patch` là công cụ nền tảng trong việc quản lý mã nguồn (Version Control) cho các dự án Robotics và AI chạy trên nền tảng Linux.
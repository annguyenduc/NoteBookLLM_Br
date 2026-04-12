---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_20
  title: CONV_atoms_v10_20
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn dữ liệu cung cấp (Volume v10), tập trung vào các kiến thức nền tảng về quản lý mã nguồn (Git) - một kỹ năng thiết yếu trong phát triển AI, Robotics và IoT.

- **Fact:** [CONV] Một dự án Git tiêu chuẩn bao gồm ba phần chính: Git directory (cơ sở dữ liệu lưu trữ lịch sử), working tree (các file đang làm việc hiện tại) và staging area (vùng đệm chứa thông tin cho lần commit tiếp theo).
- **Source:** Section: Study guide: Git
- **Tag:** [vv10]

- **Fact:** [CONV] Một commit message chuẩn cần có tiêu đề dưới 50 ký tự, cách một dòng trống trước phần mô tả chi tiết (mỗi dòng mô tả không quá 72 ký tự) và tập trung vào lý do tại sao thay đổi thay vì chỉ nêu đã làm gì.
- **Source:** Section: Một commit message chuẩn thường bao gồm & Guidelines for writing commit messages
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git commit -a -m` cho phép bỏ qua bước `git add` thủ công bằng cách tự động đưa tất cả các thay đổi của các file đã được theo dõi (tracked files) vào staging area trước khi commit.
- **Source:** Section: Review: Skipping the staging area
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git add -p` (patch mode) cho phép người dùng kiểm tra và chọn lọc từng đoạn thay đổi (hunk) cụ thể trong một file để đưa vào staging area thay vì đưa toàn bộ file.
- **Source:** Section: Review: Getting more information from the user
- **Tag:** [vv10]

- **Fact:** [CONV] Để thoát khỏi giao diện hiển thị của lệnh `git log` (thường mở bằng chương trình `less` trong terminal), người dùng cần nhấn phím `q` (viết tắt của Quit).
- **Source:** Section: Cách thoát ra khỏi màn hình có (END)
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git log -p` hiển thị lịch sử commit kèm theo nội dung thay đổi chi tiết (diff), trong khi `git log --stat` hiển thị thống kê về số lượng dòng thay đổi và file bị tác động.
- **Source:** Section: Review: Getting more information from the user
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git mv` được sử dụng để đổi tên file trong kho lưu trữ Git, giúp Git theo dõi lịch sử thay đổi của file đó một cách liên tục dưới tên mới.
- **Source:** Section: Review: Deleting and Renaming Files
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git rm` thực hiện việc xóa file khỏi cả thư mục làm việc thực tế và khỏi sự theo dõi của Git (staging area).
- **Source:** Section: Review: Deleting and Renaming Files
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git diff --staged` được sử dụng để xem sự khác biệt giữa các thay đổi đã nằm trong vùng đệm (staged) và commit gần nhất.
- **Source:** Section: Review: Getting more information from the user
- **Tag:** [vv10]

- **Fact:** [CONV] Việc thiết lập danh tính người dùng qua `git config --global user.email` và `user.name` là bắt buộc để xác định ai là người thực hiện các thay đổi trong kho lưu trữ.
- **Source:** Section: Git config command
- **Tag:** [vv10]

--------------------------------------------------
*Lưu ý: Dữ liệu cung cấp chủ yếu tập trung vào quy trình Git (Version Control), vốn là nền tảng quản lý mã nguồn cho các dự án AI, Robotics và IoT. Không có dữ liệu trực tiếp về phần cứng Arduino hay YoloBit trong đoạn text này.*
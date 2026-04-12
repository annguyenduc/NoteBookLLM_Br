Chào bạn, tôi là **@scout**. Dưới đây là danh sách các sự kiện (Facts) kỹ thuật được trích xuất và chưng cất từ nguồn dữ liệu **Volume v10** liên quan đến Git và quản lý phiên bản.

--------------------------------------------------

- **Fact:** Lệnh `diff -u` (Unified Diff) cho phép xem cả dòng cũ và dòng mới cùng lúc, sử dụng ký hiệu `+` cho nội dung thêm mới và `-` cho nội dung bị xóa.
- **Source:** Section: 1. Lệnh diff
- **Tag:** [vv10]

- **Fact:** Lệnh `patch` được sử dụng để áp dụng các thay đổi từ file `.diff` hoặc `.patch` vào file gốc để cập nhật nội dung.
- **Source:** Section: 2. Lệnh patch
- **Tag:** [vv10]

- **Fact:** Hệ thống quản lý phiên bản (VCS) cho phép khôi phục (revert) về phiên bản hoạt động trước đó nếu có thay đổi gây lỗi.
- **Source:** Question 1 (VCS benefits)
- **Tag:** [vv10]

- **Fact:** Linus Torvalds là người sáng tạo ban đầu và là nhà phát triển chính của công cụ Git.
- **Source:** Question 2 (Git Creator)
- **Tag:** [vv10]

- **Fact:** "Commit" là một tập hợp các chỉnh sửa đã được gửi vào hệ thống quản lý phiên bản để lưu trữ an toàn.
- **Source:** Question 4 (Commit definition)
- **Tag:** [vv10]

- **Fact:** "Repositories" (kho lưu trữ) là các vị trí tập trung nơi các file dự án được tổ chức và có thể gọi lại sau này.
- **Source:** Question 5 (Repositories)
- **Tag:** [vv10]

- **Fact:** Lệnh `git add` thông báo cho Git theo dõi (track) một file và đưa nó vào danh sách các thay đổi chuẩn bị được commit.
- **Source:** Question 1 & 3 (Git tracking)
- **Tag:** [vv10]

- **Fact:** Lệnh `git log` được sử dụng để xem lại lịch sử commit của một dự án.
- **Source:** Question 2 (Commit history)
- **Tag:** [vv10]

- **Fact:** Lệnh `git status` dùng để xem các thay đổi đang chờ xử lý (pending changes) và trạng thái của các file trong staging area.
- **Source:** Question 5 (Pending changes)
- **Tag:** [vv10]

- **Fact:** Staging area là khu vực trung gian nơi các file được tập hợp và chuẩn bị cho Git trước khi thực hiện lệnh commit.
- **Source:** Question 7 (Staging area)
- **Tag:** [vv10]

- **Fact:** Khi sử dụng nhiều cờ `-m` trong lệnh `git commit`, các giá trị thông điệp sẽ được nối lại với nhau thành các đoạn văn riêng biệt.
- **Source:** Question 10 (Multiple -m flags)
- **Tag:** [vv10]

- **Fact:** File `.gitignore` chứa danh sách các file hoặc mẫu tên file mà Git sẽ bỏ qua, không theo dõi trong kho lưu trữ.
- **Source:** Question 2 (gitignore)
- **Tag:** [vv10]

- **Fact:** Lệnh `git commit -a` sẽ không thực hiện commit đối với các file mới (chưa được track).
- **Source:** Question 3 (git commit -a)
- **Tag:** [vv10]

- **Fact:** `HEAD` trong Git đại diện cho snapshot hiện đang được check-out của dự án.
- **Source:** Question 4 (HEAD representation)
- **Tag:** [vv10]

- **Fact:** Lệnh `git revert` là lựa chọn tốt nhất để sửa lỗi trên một nhánh công khai (public branch) vì nó tạo ra một commit mới đảo ngược thay đổi mà không làm hỏng lịch sử.
- **Source:** Question 1 (Fixing mistakes on public branch)
- **Tag:** [vv10]

- **Fact:** Git sử dụng các khóa băm mã hóa (cryptographic hash keys) để định danh duy nhất cho các commit.
- **Source:** Question 3 (Hash keys)
- **Tag:** [vv10]

- **Fact:** Lệnh `git commit --amend` được sử dụng để ghi đè (overwrite) lên commit gần nhất.
- **Source:** Question 4 (git commit --amend)
- **Tag:** [vv10]

- **Fact:** Thuật toán "three-way merge" được sử dụng khi hợp nhất hai nhánh đã có sự phân nhánh (diverged).
- **Source:** Question 1 (Merge algorithms)
- **Tag:** [vv10]

- **Fact:** Lệnh `git merge --abort` được sử dụng để hủy bỏ quá trình hợp nhất đang diễn ra và quay lại trạng thái trước đó.
- **Source:** Question 3 (Abort merge)
- **Tag:** [vv10]

- **Fact:** Lệnh `git log --graph --oneline` hiển thị chế độ xem tóm tắt lịch sử commit với mỗi commit trên một dòng kèm theo đồ thị nhánh.
- **Source:** Question 4 (Summarized history)
- **Tag:** [vv10]

--------------------------------------------------
**@scout** | Kết thúc trích xuất từ Volume v10.
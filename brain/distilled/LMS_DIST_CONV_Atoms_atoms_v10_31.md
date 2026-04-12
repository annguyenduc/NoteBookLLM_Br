---
file_id: CONV_Atoms_atoms_v10_31
category: Atomic Note
trainer_level: Entry
bloom_level: Remember/Understand
source: '[[MASTER_SOURCE_INDEX.md]]'
status: Verified
last_audit: '2026-04-12'
---

# CONV Atoms atoms v10 31

# Tài liệu học tập: Git và Quản lý phiên bản (LOM v4.4 Supreme)

## Thông tin chung

| Thuộc tính | Giá trị |
|------------|---------|
| **Tiêu đề** | Git và Quản lý phiên bản nâng cao |
| **Mô tả** | Tài liệu này cung cấp kiến thức chuyên sâu về hệ thống quản lý phiên bản Git, bao gồm các lệnh cơ bản và nâng cao, quy trình làm việc, và chiến lược xử lý lỗi. |
| **Đối tượng học viên** | Sinh viên ngành Công nghệ thông tin, lập trình viên mới vào nghề |
| **Thời lượng** | 4 giờ học |
| **Ngôn ngữ** | Tiếng Việt |
| **Phiên bản** | 4.4 Supreme |

---

## Mục tiêu học tập

Sau khi hoàn thành bài học này, học viên sẽ có khả năng:

- Hiểu rõ các khái niệm cốt lõi của hệ thống quản lý phiên bản (VCS)
- Sử dụng thành thạo các lệnh Git cơ bản và nâng cao
- Áp dụng các kỹ thuật quản lý nhánh và hợp nhất an toàn
- Giải quyết các tình huống phát sinh trong môi trường làm việc nhóm

---

## Nội dung bài học

### # Khái niệm cơ bản về Git

Git là một hệ thống quản lý phiên bản phân tán do **Linus Torvalds** sáng tạo và phát triển chính [vv10]. Nó cho phép người dùng theo dõi mọi thay đổi trong mã nguồn, khôi phục về phiên bản trước nếu có lỗi xảy ra [vv10].

#### ## Kho lưu trữ (Repository)

**Repository** là nơi tập trung lưu trữ tất cả các file dự án và lịch sử thay đổi của chúng. Có thể được gọi lại bất kỳ lúc nào để phục hồi hoặc kiểm tra [vv10].

#### ## Commit và Staging Area

- **Commit**: Là tập hợp các chỉnh sửa được gửi vào hệ thống để lưu trữ an toàn [vv10].
- **Staging Area**: Là khu vực trung gian nơi các file được tập hợp trước khi commit [vv10].

Lệnh `git add` giúp thông báo cho Git theo dõi một file và đưa nó vào staging area [vv10].

---

### # Các lệnh Git cơ bản

| Lệnh | Chức năng |
|------|-----------|
| `git status` | Xem các thay đổi đang chờ xử lý và trạng thái staging area [vv10] |
| `git log` | Xem lịch sử commit của dự án [vv10] |
| `git log --graph --oneline` | Hiển thị lịch sử dưới dạng đồ thị gọn nhẹ [vv10] |
| `git commit -a` | Commit tất cả các file đã được theo dõi (không bao gồm file mới) [vv10] |
| `git commit --amend` | Ghi đè lên commit gần nhất [vv10] |
| `git revert` | Tạo commit mới để đảo ngược thay đổi (phù hợp với nhánh công khai) [vv10] |

---

### # So sánh và áp dụng thay đổi

#### ## Unified Diff (`diff -u`)

Lệnh `diff -u` cho phép xem cả dòng cũ và dòng mới cùng lúc, sử dụng ký hiệu `+` cho nội dung thêm mới và `-` cho nội dung bị xóa [vv10].

#### ## Áp dụng bản vá (`patch`)

Lệnh `patch` được sử dụng để áp dụng các thay đổi từ file `.diff` hoặc `.patch` vào file gốc để cập nhật nội dung [vv10].

---

### # Quản lý nhánh và hợp nhất

#### ## Hợp nhất ba chiều (Three-way merge)

Khi hai nhánh có sự phân nhánh, thuật toán **three-way merge** được sử dụng để hợp nhất [vv10].

#### ## Hủy bỏ quá trình hợp nhất

Lệnh `git merge --abort` giúp hủy bỏ quá trình hợp nhất đang diễn ra và quay lại trạng thái trước đó [vv10].

---

### # Cấu hình và bảo mật

#### ## File `.gitignore`

File `.gitignore` chứa danh sách các file hoặc mẫu tên file mà Git sẽ bỏ qua, không theo dõi trong kho lưu trữ [vv10].

#### ## Mã hóa khóa băm

Git sử dụng các **khóa băm mã hóa** để định danh duy nhất cho các commit [vv10].

#### ## HEAD trong Git

`HEAD` đại diện cho snapshot hiện đang được check-out của dự án [vv10].

---

## Bài tập thực hành

### Worksheet 1: Làm quen với Git cơ bản

1. Tạo một repository mới và thực hiện commit đầu tiên.
2. Thêm một số file, sử dụng `git add` và `git status` để kiểm tra.
3. Commit các thay đổi và xem lịch sử bằng `git log`.

### Worksheet 2: Quản lý nhánh và hợp nhất

1. Tạo hai nhánh song song và thực hiện thay đổi trên từng nhánh.
2. Sử dụng `git merge` để hợp nhất và quan sát kết quả.
3. Gây xung đột thủ công và giải quyết bằng cách chỉnh sửa thủ công.

---

## Kiểm tra đánh giá

### Quiz: Kiến thức Git tổng hợp

1. Ai là người sáng tạo Git?
   - A. Steve Jobs
   - B. Linus Torvalds
   - C. Bill Gates
   - D. Mark Zuckerberg  
   **Đáp án đúng:** B [vv10]

2. Lệnh nào dùng để xem lịch sử commit?
   - A. `git show`
   - B. `git log`
   - C. `git status`
   - D. `git diff`  
   **Đáp án đúng:** B [vv10]

3. Lệnh nào sau đây **không** commit file mới?
   - A. `git commit -a`
   - B. `git commit -m "message"`
   - C. `git commit file.txt`
   - D. `git commit *`  
   **Đáp án đúng:** A [vv10]

---

## Tình huống thực tế (Scenario)

> Bạn là thành viên trong nhóm phát triển phần mềm. Một đồng đội vô tình commit một đoạn mã gây lỗi nghiêm trọng vào nhánh `main`. Nhánh này đang được sử dụng bởi nhiều người khác. Bạn cần xử lý như thế nào?

**Hướng dẫn giải quyết:**

- Sử dụng lệnh `git revert` để tạo commit mới đảo ngược thay đổi, đảm bảo không làm hỏng lịch sử cho những người khác [vv10].
- Thông báo cho nhóm về lỗi và hướng khắc phục.

---

## Tài nguyên tham khảo

- [Git Documentation](https://git-scm.com/doc)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [MASTER_SOURCE_INDEX.md](../raw/MASTER_SOURCE_INDEX.md)

---

## Ghi chú bản quyền

Tài liệu này thuộc sở hữu nội bộ của chương trình đào tạo. Mọi hành vi sao chép, phân phối trái phép đều bị nghiêm cấm.  
© 2025 Content Engineering Team - LOM v4.4 Supreme Standard.
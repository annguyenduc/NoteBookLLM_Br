---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v10_31
  title: CONV_atoms_v10_31
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dựa trên dữ liệu bạn cung cấp về Git và quản lý phiên bản, tôi xin trích xuất các sự kiện kỹ thuật như sau:

- **Fact:** [CONV] Khi thực hiện gộp (merge) hai nhánh đã phân tách (diverged), Git sử dụng thuật toán **three-way merge** để kết hợp các thay đổi.
- **Source:** [Question 1 - Merging algorithms]
- **Tag:** [vv10]

- **Fact:** [CONV] Để giải quyết xung đột (merge conflict) và giữ lại phiên bản của nhánh hiện tại (HEAD), người dùng cần xóa các thẻ đánh dấu xung đột (`<<<<<<<`, `=======`, `>>>>>>>`) và chỉ để lại đoạn mã thuộc phần `HEAD`.
- **Source:** [Question 2 - Conflict resolution]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git merge --abort` được sử dụng để dừng quá trình merge đang xảy ra xung đột và khôi phục lại trạng thái của tập tin trước khi thực hiện lệnh merge.
- **Source:** [Question 3 - Throw away a merge]
- **Tag:** [vv10]

- **Fact:** [CONV] Để xem tóm tắt lịch sử commit với mỗi commit hiển thị trên một dòng duy nhất kèm theo sơ đồ nhánh, sử dụng lệnh `git log --graph --oneline`.
- **Source:** [Question 4 - Summarized history view]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git revert` là phương án tốt nhất để sửa lỗi trên một nhánh công khai (public branch) vì nó tạo ra một commit mới đảo ngược các thay đổi mà không làm thay đổi lịch sử đã có.
- **Source:** [Question 1 (Previous set) - Fixing public branch mistakes]
- **Tag:** [vv10]

- **Fact:** [CONV] Git sử dụng các mã băm mật mã (cryptographic hash keys - SHA-1) để định danh duy nhất cho mỗi commit và đảm bảo tính toàn vẹn của kho lưu trữ.
- **Source:** [Question 3 (Previous set) - Cryptographic hash keys]
- **Tag:** [vv10]

- **Fact:** [CONV] Lệnh `git commit --amend` được sử dụng để ghi đè lên commit gần nhất, cho phép sửa đổi nội dung hoặc thông điệp commit đó.
- **Source:** [Question 4 (Previous set) - Git commit amend]
- **Tag:** [vv10]

- **Fact:** [CONV] Tệp `.gitignore` chứa danh sách các tệp tin hoặc mẫu tên tệp mà Git sẽ bỏ qua, không theo dõi trong kho lưu trữ hiện tại.
- **Source:** [Question 2 (VCS set) - Gitignore definition]
- **Tag:** [vv10]

--------------------------------------------------
**Ghi chú bổ sung [Unverified_Source]:**
- Trong thực tế, `git log --oneline` chỉ hiển thị danh sách rút gọn, còn `--graph` mới là tham số vẽ sơ đồ nhánh trực quan.
- Khi giải quyết xung đột thủ công, việc quên xóa các dòng `=======` hoặc `>>>>>>>` sẽ gây lỗi cú pháp trong mã nguồn.
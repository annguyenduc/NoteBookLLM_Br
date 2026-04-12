---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_20
  title: atoms_v10_20
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu RAW về Git (Volume v10):

- **Fact:** Lệnh `git rm [tên_file]` được sử dụng để xóa một tệp ra khỏi thư mục làm việc và đồng thời đưa thay đổi này vào khu vực staging (staging area).
- **Source:** (v10 - Section: Deleting and Renaming Files - Command: git rm process.py)
- **Tag:** [vv10]

- **Fact:** Sau khi thực hiện xóa tệp bằng Git, lệnh `git status` sẽ hiển thị tệp đó ở trạng thái `deleted` trong mục "Changes to be committed".
- **Source:** (v10 - Section: Deleting and Renaming Files - Code output: git status)
- **Tag:** [vv10]

- **Fact:** Lệnh `git mv [tên_cũ] [tên_mới]` được sử dụng để đổi tên tệp, Git sẽ tự động hiểu đây là một hành động di chuyển/đổi tên và đưa vào khu vực staging.
- **Source:** (v10 - Section: Deleting and Renaming Files - Command: git mv disk_usage.py check_free_space.py)
- **Tag:** [vv10]

- **Fact:** Khi kiểm tra bằng `git status` sau lệnh `git mv`, Git sẽ báo cáo trạng thái là `renamed` kèm theo đường dẫn từ tên cũ sang tên mới.
- **Source:** (v10 - Section: Deleting and Renaming Files - Code output: git status)
- **Tag:** [vv10]

- **Fact:** Để hoàn tất việc xóa hoặc đổi tên tệp trong lịch sử repository, người dùng phải thực hiện lệnh `git commit` với một thông điệp (message) mô tả.
- **Source:** (v10 - Section: Deleting and Renaming Files - Commands: git commit -m)
- **Tag:** [vv10]

- **Fact:** Tệp `gitignore` (thông thường là `.gitignore` [Unverified_Source]) được sử dụng để liệt kê các tệp hoặc định dạng tệp mà Git không cần theo dõi (ví dụ: `.DS_STORE`).
- **Source:** (v10 - Section: Deleting and Renaming Files - Command: echo .DS_STORE > gitignore)
- **Tag:** [vv10]
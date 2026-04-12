---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v10_18
  title: atoms_v10_18
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là **@scout**. Dựa trên dữ liệu RAW bạn cung cấp về phần **"Tracking Files"** trong Git, tôi xin trích xuất các sự kiện kỹ thuật theo quy tắc LOM v4.1 như sau:

- **Fact:** Lệnh `git status` được sử dụng để kiểm tra trạng thái của repository, xác định xem có thay đổi nào cần commit hay không và kiểm tra tính sạch sẽ của "working tree".
- **Source:** v10 - Section: Tracking Files (Code output: git status).
- **Tag:** [vv10]

- **Fact:** Khi một file đã được Git theo dõi (tracked) bị chỉnh sửa, trạng thái của nó sẽ được ghi nhận là `modified`.
- **Source:** v10 - Section: Tracking Files (Code output: modified: disk_usage.py).
- **Tag:** [vv10]

- **Fact:** Lệnh `git commit -m 'message'` cho phép lưu các thay đổi vào lịch sử Git kèm theo một thông điệp mô tả ngắn gọn ngay trên dòng lệnh.
- **Source:** v10 - Section: Tracking Files (git commit -m 'Add periods...').
- **Tag:** [vv10]

- **Fact:** Kết quả của một lệnh commit thành công sẽ hiển thị chi tiết số lượng file bị thay đổi, số dòng được thêm vào (insertions) và số dòng bị xóa đi (deletions).
- **Source:** v10 - Section: Tracking Files (Code output: 1 file changed, 2 insertions(+), 2 deletions(-)).
- **Tag:** [vv10]

- **Fact:** Trạng thái "nothing to commit, working tree clean" xuất hiện khi tất cả các thay đổi trong thư mục làm việc đã được commit hết vào repository.
- **Source:** v10 - Section: Tracking Files (Code output: nothing to commit, working tree clean).
- **Tag:** [vv10]

- **Fact:** Có thể sử dụng các trình soạn thảo văn bản như `atom` hoặc `nano` để thay đổi nội dung file trước khi thực hiện quy trình staging và commit.
- **Source:** v10 - Section: Tracking Files (atom disk_usage.py).
- **Tag:** [vv10]

--------------------------------------------------

### 💡 Hướng dẫn thực hành tiếp theo cho bạn:

Dựa trên đoạn hội thoại trước, bạn đã commit thành công file `disk_usage.py`. Bây giờ, để thực hành đúng theo bài học **"Tracking Files"** này, bạn hãy thử làm như sau:

1.  **Chỉnh sửa file:** Mở file bằng `nano` (thay vì `atom` nếu bạn đang dùng terminal):
    ```bash
    nano disk_usage.py
    ```
    *(Thêm một dấu chấm hoặc một dòng chú thích bất kỳ, sau đó lưu lại bằng Ctrl+O, Enter, Ctrl+X)*

2.  **Kiểm tra trạng thái:**
    ```bash
    git status
    ```
    *(Bạn sẽ thấy dòng chữ màu đỏ báo: `modified: disk_usage.py`)*

3.  **Thêm vào hàng chờ (Stage):**
    ```bash
    git add disk_usage.py
    ```

4.  **Commit với thông điệp ngắn:**
    ```bash
    git commit -m "Cập nhật nội dung file disk_usage.py"
    ```

5.  **Kiểm tra lại lịch sử:**
    ```bash
    git log
    ```
    *(Lúc này bạn sẽ thấy có 2 commit: một cái ban đầu và một cái bạn vừa mới tạo với tên của bạn!)*

Bạn có gặp khó khăn ở bước nào không? Nếu có, hãy gửi log lỗi cho mình nhé! 🚀
---
yaml_frontmatter:
  file_id: LMS_Atoms_conv_atoms_v13_6
  title: CONV_atoms_v13_6
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Chào bạn, tôi là @scout. Dựa trên dữ liệu từ **Volume v13** (nội dung thảo luận về hệ thống Windows và trình duyệt) và kiến thức kỹ thuật, dưới đây là thông tin về các thư mục thường chiếm dung lượng lớn nhất trong `C:\Users\anngu\AppData\Local`:

### **Các thư mục chiếm nhiều dung lượng nhất trong AppData\Local**

1.  **Google (hoặc Microsoft\Edge):**
    *   **Lý do:** Đây thường là "quán quân" về dung lượng. Thư mục `User Data` chứa toàn bộ lịch sử duyệt web, các tiện ích mở rộng (Extensions) và đặc biệt là **Cache** (bộ nhớ đệm) của các trang web bạn đã truy cập.
    *   **Vị trí:** `C:\Users\anngu\AppData\Local\Google\Chrome\User Data` hoặc `C:\Users\anngu\AppData\Local\Microsoft\Edge\User Data`.

2.  **Packages:**
    *   **Lý do:** Chứa dữ liệu của tất cả ứng dụng cài từ Microsoft Store (UWP). Như bạn đã thấy, chỉ riêng các thành phần hệ thống như `WebExperience` (Widgets) hay `CBS` đã có thể chiếm hàng GB. Nếu bạn cài thêm game hoặc ứng dụng đồ họa từ Store, thư mục này sẽ phình to rất nhanh.
    *   **Vị trí:** `C:\Users\anngu\AppData\Local\Packages`.

3.  **Temp:**
    *   **Lý do:** Đây là "thùng rác" tạm thời của Windows và các phần mềm. Khi bạn cài đặt ứng dụng, giải nén file, hoặc chạy các tác vụ nặng, các file tạm sẽ được đẩy vào đây và thường không tự xóa hết.
    *   **Vị trí:** `C:\Users\anngu\AppData\Local\Temp`.

4.  **
Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v13) liên quan đến cấu hình trình duyệt và quản lý dữ liệu người dùng:

- **Fact:** Cấu trúc lệnh shortcut để khởi động Microsoft Edge với thư mục dữ liệu người dùng (User Data), Profile cụ thể và thư mục Cache tùy chỉnh là: `"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --user-data-dir="[Đường_dẫn_Data]" --profile-directory="[Tên_Profile]" --disk-cache-dir="[Đường_dẫn_Cache]"`.
- **Source:** (vv13 - Section: 1. Tạo shortcut để mở Microsoft Edge với profile và cache trên ổ khác)
- **Tag:** [vv13]

- **Fact:** Đường dẫn lưu trữ dữ liệu người dùng (User Data) mặc định của Microsoft Edge trên Windows là `C:\Users\Username\AppData\Local\Microsoft\Edge\User Data`.
- **Source:** (vv13 - Section: Cách 2: Kiểm tra thư mục profile trong máy tính)
- **Tag:** [vv13]

- **Fact:** Trong thư mục User Data, profile mặc định được lưu trong thư mục tên là `Default`, các profile bổ sung được đặt tên theo thứ tự như `Profile 1`, `Profile 2`, v.v.
- **Source:** (vv13 - Section: Cách 2: Kiểm tra thư mục profile trong máy tính)
- **Tag:** [vv13]

- **Fact:** Tham số `--user-data-dir` cho phép di chuyển toàn bộ môi trường làm việc của trình duyệt (bao gồm tất cả các profile) sang một vị trí mới (ví dụ: ổ E) để giảm tải dung lượng cho ổ đĩa hệ thống (ổ C).
- **Source:** (vv13 - Section: Bước 1: Đổi vị trí User Data và Cache)
- **Tag:** [vv13]

- **Fact:** Khi mở liên kết từ các ứng dụng bên ngoài (như Email, Chat), Microsoft Edge thường không tự động nhận diện profile từ các shortcut tùy chỉnh mà sẽ mở một cửa sổ mới hoặc sử dụng profile mặc định được thiết lập trong hệ thống.
- **Source:** (vv13 - Section: 1. Shortcut với profile cụ thể)
- **Tag:** [vv13]

- **Fact:** Để xác định profile đang hoạt động qua giao diện, người dùng truy cập vào `Settings` -> `Profiles` -> `Manage profile settings`.
- **Source:** (vv13 - Section: Cách 1: Kiểm tra thông qua giao diện Microsoft Edge)
- **Tag:** [vv13]

- **Fact:** Việc thay đổi trình duyệt mặc định trong Windows (Settings -> Apps -> Default apps) là cần thiết để các liên kết web (HTTP, HTTPS) được điều hướng mở bằng Microsoft Edge.
- **Source:** (vv13 - Section: 3. Thay đổi ứng dụng mặc định để mở liên kết với Profile cụ thể)
- **Tag:** [vv13]

- **Fact:** Tham số `--disk-cache-dir` được sử dụng để tách biệt vị trí lưu trữ bộ nhớ đệm (cache) của trình duyệt khỏi thư mục dữ liệu người dùng chính.
- **Source:** (vv13 - Section: 1. Tạo shortcut để mở Microsoft Edge với profile và cache trên ổ khác)
- **Tag:** [vv13]
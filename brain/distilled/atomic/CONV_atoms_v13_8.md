Dựa trên dữ liệu cung cấp từ Volume v13, dưới đây là các sự kiện kỹ thuật được trích xuất liên quan đến cấu hình trình duyệt (hỗ trợ môi trường làm việc cho AI/Robotics/IoT):

- **Fact:** [CONV] Sử dụng tham số `--user-data-dir` trong lệnh thực thi để chỉ định thư mục lưu trữ toàn bộ dữ liệu người dùng (User Data) của Microsoft Edge sang một vị trí tùy chỉnh (ví dụ: ổ E).
- **Source:** [v13 - Phần 1: Shortcut với profile cụ thể]
- **Tag:** [vv13]

- **Fact:** [CONV] Tham số `--disk-cache-dir` được sử dụng để di chuyển thư mục chứa dữ liệu đệm (cache) của trình duyệt sang một đường dẫn khác nhằm giảm tải dung lượng cho ổ đĩa hệ thống.
- **Source:** [v13 - Bước 1: Đổi vị trí User Data và Cache]
- **Tag:** [vv13]

- **Fact:** [CONV] Tham số `--profile-directory` cho phép người dùng chỉ định chính xác một profile cụ thể (ví dụ: "Profile 2") để khởi động cùng với trình duyệt.
- **Source:** [v13 - Cách 3: Sử dụng --profile-directory]
- **Tag:** [vv13]

- **Fact:** [CONV] Đường dẫn thực thi mặc định của Microsoft Edge trên hệ điều hành Windows thường là `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe`.
- **Source:** [v13 - Bước 1: Xác định đường dẫn Microsoft Edge...]
- **Tag:** [vv13]

- **Fact:** [CONV] Thư mục lưu trữ Profile mặc định của Edge trong hệ thống nằm tại đường dẫn: `C:\Users\Username\AppData\Local\Microsoft\Edge\User Data`.
- **Source:** [v13 - Cách 2: Kiểm tra thư mục profile trong máy tính]
- **Tag:** [vv13]

- **Fact:** [CONV] Để đồng bộ hóa cài đặt, dấu trang và lịch sử duyệt web trên nhiều thiết bị, người dùng cần cấu hình tính năng "Sync" trong phần Profile settings.
- **Source:** [v13 - ASSISTANT: 2. Sync]
- **Tag:** [vv13]

- **Fact:** [CONV] Khi mở liên kết từ ứng dụng bên ngoài, Microsoft Edge có xu hướng mở một cửa sổ mới hoặc profile mặc định nếu không được cấu hình rõ ràng trong Default Apps của Windows.
- **Source:** [v13 - 3. Thay đổi ứng dụng mặc định để mở liên kết...]
- **Tag:** [vv13]

- **Fact:** [CONV] Có thể kiểm tra thông tin lưu trữ của profile hiện tại thông qua công cụ Developer Tools (Ctrl+Shift+I) > tab Application > Local Storage.
- **Source:** [v13 - Cách 3: Kiểm tra Profile hiện tại thông qua đường dẫn Edge]
- **Tag:** [vv13]

*Lưu ý: Dữ liệu RAW cung cấp tập trung vào kỹ thuật cấu hình trình duyệt Microsoft Edge, không chứa thông tin trực tiếp về phần cứng IoT, Arduino, YoloBit hay Robotics.*
Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v12) liên quan đến quản lý thiết bị ngoại vi (COM ports), hệ thống và driver:

- **Fact:** [CONV] Có thể gỡ bỏ hàng loạt cổng COM ảo (Standard Serial over Bluetooth link) bằng ba cách chính: Device Manager (thủ công), lệnh `pnputil`, hoặc công cụ `DevCon`.
- **Source:** [v12 - Section: Cách gỡ bỏ hàng loạt các cổng COM]
- **Tag:** [vv12]

- **Fact:** [CONV] Để xóa driver bằng lệnh `pnputil`, cần xác định tên file INF gốc (thường có dạng `oemXX.inf`) thông qua lệnh `pnputil /enum-drivers`. Việc xóa trực tiếp file driver hệ thống (như `bthspp.inf`) sẽ báo lỗi "The specified file is not an installed OEM INF".
- **Source:** [v12 - Section: Cách 1: Xác định chính xác tên file driver và xóa đúng tên]
- **Tag:** [vv12]

- **Fact:** [CONV] Công cụ DevCon của Microsoft cho phép quản lý thiết bị bằng dòng lệnh; có thể dùng lệnh `devcon remove "bthspp*"` hoặc kết hợp vòng lặp `for` với `wmic` để xóa toàn bộ các cổng COM Bluetooth hiện có.
- **Source:** [v12 - Section: Cách 2: Gỡ bằng devcon (Chính xác hơn)]
- **Tag:** [vv12]

- **Fact:** [CONV] PowerShell có thể gỡ bỏ thiết bị theo Class Ports dựa trên tên hiển thị bằng lệnh: `Get-PnpDevice -Class Ports | Where-Object { $_.FriendlyName -like "*Bluetooth*" } | ForEach-Object { Remove-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }`.
- **Source:** [v12 - Section: Cách 3: Dùng PowerShell để xóa toàn bộ cổng COM Bluetooth]
- **Tag:** [vv12]

- **Fact:** [CONV] Thư mục Windows thông thường chiếm từ 15GB đến 30GB, nhưng có thể tăng lên 40-50GB hoặc hơn do các bản cập nhật, file tạm, driver và thư mục lưu trữ phiên bản cũ (Windows.old).
- **Source:** [v12 - Section: Dung lượng thư mục Windows]
- **Tag:** [vv12]

- **Fact:** [CONV] Thư mục `AppData\Roaming` lưu trữ dữ liệu cấu hình, tài khoản và cache riêng biệt cho từng người dùng của các ứng dụng; việc xóa thư mục này sẽ làm mất các tùy chỉnh cá nhân và có thể gây lỗi ứng dụng.
- **Source:** [v12 - Section: C:\Users\anngu\AppData\Roaming Thư mục này thì sao]
- **Tag:** [vv12]

- **Fact:** [CONV] Trình duyệt Microsoft Edge có thể được gỡ cài đặt cưỡng bức thông qua dòng lệnh bằng cách truy cập vào thư mục `Installer` của phiên bản tương ứng và chạy lệnh: `setup.exe --uninstall --system-level --verbose-logging --force-uninstall`.
- **Source:** [v12 - Section: 3. Cách xóa đúng cách Microsoft Edge]
- **Tag:** [vv12]

- **Fact:** [CONV] Hệ thống có thể tồn tại song song nhiều thư mục phiên bản của Microsoft Edge trong đường dẫn `C:\Program Files (x86)\Microsoft\Edge\Application` (ví dụ: bản .112 và .146); thông thường chỉ phiên bản mới nhất là cần thiết để hoạt động.
- **Source:** [v12 - Section: Tôi đang có 2 thư mục như trên]
- **Tag:** [vv12]
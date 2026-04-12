Dưới đây là các sự kiện kỹ thuật được trích xuất từ dữ liệu cung cấp (Volume v06):

- **Fact:** Để tránh việc tự động tạo lại các cổng COM ảo gây xung đột, cần hủy ghép đôi (unpair) các thiết bị Bluetooth có cấu hình Serial Port Profile (SPP) hoặc tắt tính năng "Serial Port" trong thuộc tính thiết bị.
- **Source:** [vv06] - Section: Lưu ý để không bị mọc lại.
- **Tag:** [vv06]

- **Fact:** Script PowerShell có thể được sử dụng để dọn dẹp các cổng COM Bluetooth "ma" (ghost devices) bằng cách lọc các thiết bị có InstanceId bắt đầu bằng `BTHENUM` hoặc tên chứa cụm "Standard Serial over Bluetooth link".
- **Source:** [vv06] - Section: Script cleanup_bt_com.ps1.
- **Tag:** [vv06]

- **Fact:** Lệnh `Get-PnpDevice -Class Ports -PresentOnly:$false` trong PowerShell cho phép liệt kê tất cả các cổng COM trong hệ thống, bao gồm cả những thiết bị không còn kết nối vật lý (ẩn).
- **Source:** [vv06] - Section: Script cleanup_bt_com.ps1.
- **Tag:** [vv06]

- **Fact:** Việc gỡ bỏ thiết bị phần cứng thông qua script trên Windows yêu cầu quyền quản trị viên (Administrator) và có thể thực hiện thông qua công cụ `pnputil.exe` với tham số `/remove-device`.
- **Source:** [vv06] - Section: Script cleanup_bt_com.ps1 (function Require-Admin).
- **Tag:** [vv06]

- **Fact:** Sau khi dọn dẹp các cổng COM thừa, người dùng có thể thay đổi số thứ tự cổng COM cho các mạch USB-Serial (như CH340, CP210x) tại mục: Device Manager -> Ports -> Properties -> Port Settings -> Advanced -> COM Port Number.
- **Source:** [vv06] - Section: Lưu ý (sau script 1).
- **Tag:** [vv06]

- **Fact:** Lệnh `Set-ExecutionPolicy -Scope Process Bypass` được sử dụng để tạm thời cho phép thực thi các script PowerShell trong phiên làm việc hiện tại mà không làm thay đổi chính sách bảo mật hệ thống lâu dài.
- **Source:** [vv06] - Section: Nếu vẫn lỗi khi chạy script.
- **Tag:** [vv06]

- **Fact:** Toán tử `??` (null-coalescing) chỉ tương thích với PowerShell 7 trở lên; sử dụng toán tử này trên PowerShell 5.1 sẽ gây ra lỗi cú pháp (ParserError).
- **Source:** [vv06] - Section: ASSISTANT (Giải thích lỗi v2).
- **Tag:** [vv06]

- **Fact:** Có thể truy cập nhanh vào bảng quản lý cổng COM của Bluetooth bằng cách sử dụng lệnh `bthprops.cpl` trong hộp thoại Run (Win+R).
- **Source:** [vv06] - Section: Nếu vẫn “No Bluetooth COM devices found”.
- **Tag:** [vv06]

- **Fact:** Để kiểm tra quyền Administrator trong PowerShell, có thể sử dụng lớp `[Security.Principal.WindowsPrincipal]` để xác thực vai trò `Administrator` của người dùng hiện tại.
- **Source:** [vv06] - Section: Kiểm tra đã là Admin chưa.
- **Tag:** [vv06]

- **Fact:** Khi lập trình cho ESP8266/MicroPython, việc dọn dẹp cổng COM Bluetooth giúp các công cụ như `mpremote` hoặc cấu hình `tasks.json` trong VS Code nhận diện đúng cổng nạp code.
- **Source:** [vv06] - Section: DỮ LIỆU RAW (mở đầu).
- **Tag:** [vv06]
Dưới đây là các sự kiện kỹ thuật được trích xuất từ nguồn dữ liệu cung cấp:

- Fact: [CONV] Các thiết bị Bluetooth sử dụng Serial Port Profile (SPP) thường tự động tạo ra nhiều cổng COM ảo (Standard Serial over Bluetooth link), gây xung đột hoặc làm đầy danh sách cổng COM trên Windows.
- Source: [vv06] - Section: Lưu ý để không bị mọc lại
- Tag: [vv06]

- Fact: [CONV] Công cụ `mpremote` và file cấu hình `tasks.json` trong VS Code thường được sử dụng để nạp code hoặc giao tiếp với các board mạch IoT (như ESP8266) qua cổng COM cụ thể.
- Source: [vv06] - Section: DỮ LIỆU RAW (dòng 1)
- Tag: [vv06]

- Fact: [CONV] Script PowerShell có thể tự động dọn dẹp các "ghost devices" (thiết bị ẩn/không còn hiện diện) bằng cách lọc các thiết bị có InstanceId chứa "BTHENUM" hoặc tên chứa "Standard Serial over Bluetooth link".
- Source: [vv06] - Section: Script cleanup_bt_com.ps1
- Tag: [vv06]

- Fact: [CONV] Để gỡ bỏ một thiết bị phần cứng qua dòng lệnh Windows, có thể sử dụng công cụ `pnputil.exe /remove-device [InstanceId]` hoặc lệnh `Remove-PnpDevice` trong PowerShell.
- Source: [vv06] - Section: Script cleanup_bt_com.ps1 (vòng lặp foreach)
- Tag: [vv06]

- Fact: [CONV] Việc thực thi các lệnh quản lý thiết bị (Get-PnpDevice, Remove-PnpDevice) bắt buộc phải chạy PowerShell với quyền quản trị viên (Run as Administrator).
- Source: [vv06] - Section: function Require-Admin
- Tag: [vv06]

- Fact: [CONV] Lệnh `Set-ExecutionPolicy -Scope Process Bypass` cho phép chạy các script PowerShell chưa được ký trong phiên làm việc hiện tại mà không bị hệ thống chặn.
- Source: [vv06] - Section: USER/ASSISTANT (Cách chạy script)
- Tag: [vv06]

- Fact: [CONV] Toán tử `??` (null-coalescing) và `?.` chỉ tương thích với PowerShell 7; nếu sử dụng trên PowerShell 5.1 (mặc định của Windows 10/11) sẽ gây lỗi cú pháp "Unexpected token".
- Source: [vv06] - Section: ASSISTANT (Giải thích lỗi V2)
- Tag: [vv06]

- Fact: [CONV] Người dùng có thể thay đổi số thứ tự cổng COM (ví dụ từ COM20 về COM5) cho các chip USB-Serial như CH340 hoặc CP210x thông qua: Device Manager -> Ports -> Properties -> Port Settings -> Advanced.
- Source: [vv06] - Section: Lưu ý / Sau khi dọn
- Tag: [vv06]

- Fact: [CONV] Lệnh `bthprops.cpl` (mở qua Win+R) cung cấp giao diện quản lý Bluetooth cổ điển, cho phép xóa các cổng COM SPP trong tab "COM Ports".
- Source: [vv06] - Section: Nếu vẫn “No Bluetooth COM devices found”
- Tag: [vv06]

- Fact: [CONV] Để liệt kê tất cả các thiết bị có định dạng tên chứa số cổng COM (COMxx) bằng PowerShell, có thể sử dụng lệnh: `Get-PnpDevice -PresentOnly:$false | Where-Object { $_.FriendlyName -match '\(COM\d+\)' }`.
- Source: [vv06] - Section: 1) Kiểm tra có thật là còn COM Bluetooth không
- Tag: [vv06]
---
yaml_frontmatter:
  file_id: LMS_Atoms_atoms_v12_2
  title: atoms_v12_2
  category: Atomic Note
  prefix: LMS
  source: MASTER_SOURCE_INDEX.md
  status: standardized
---

Dưới đây là các sự kiện (Facts) được trích xuất từ nguồn cung cấp (Volume v12) liên quan đến quản lý hệ thống, driver và thiết bị (nền tảng cho việc kết nối IoT/Arduino):

- **Fact:** Có thể gỡ bỏ hàng loạt các cổng COM ảo (Standard Serial over Bluetooth link) bằng Device Manager, lệnh `pnputil`, hoặc công cụ `DevCon`.
- **Source:** [vv12] - Section: Assistant: Cách gỡ bỏ hàng loạt các cổng COM.
- **Tag:** [vv12]

- **Fact:** Lệnh `pnputil /delete-driver <tên_file.inf> /uninstall /force` được sử dụng để xóa driver và gỡ cài đặt thiết bị khỏi hệ thống Windows.
- **Source:** [vv12] - Section: Cách 2: Gỡ hàng loạt bằng dòng lệnh (Nhanh hơn).
- **Tag:** [vv12]

- **Fact:** Để liệt kê danh sách driver của các cổng COM đang cài đặt trên máy tính, sử dụng lệnh: `wmic path Win32_PnPSignedDriver where "DeviceClass='Ports'" get DeviceName, InfName`.
- **Source:** [vv12] - Section: USER: C:\Windows\System32>wmic path Win32_PnPSignedDriver...
- **Tag:** [vv12]

- **Fact:** Lỗi "The specified file is not an installed OEM INF" xảy ra khi tệp .inf (như bthspp.inf) không phải là tệp cài đặt gốc (OEM) mà Windows có thể xóa trực tiếp qua tên gốc; cần tìm tên định danh `oemXX.inf` tương ứng.
- **Source:** [vv12] - Section: Assistant: Lỗi này có nghĩa là bthspp.inf không phải là INF cài đặt gốc.
- **Tag:** [vv12]

- **Fact:** PowerShell có thể gỡ bỏ các thiết bị cổng COM Bluetooth bằng lệnh: `Get-PnpDevice -Class Ports | Where-Object { $_.FriendlyName -like "*Bluetooth*" } | ForEach-Object { Remove-PnpDevice -InstanceId $_.InstanceId -Confirm:$false }`.
- **Source:** [vv12] - Section: Cách 3: Dùng PowerShell để xóa toàn bộ cổng COM Bluetooth.
- **Tag:** [vv12]

- **Fact:** Thư mục hệ điều hành Windows (Windows 10/11) thường chiếm dung lượng từ 20GB đến 50GB, có thể tăng lên nếu có thư mục `Windows.old` hoặc file tạm từ bản cập nhật.
- **Source:** [vv12] - Section: Dung lượng thư mục Windows.
- **Tag:** [vv12]

- **Fact:** Thư mục `AppData\Roaming` lưu trữ cấu hình, dữ liệu người dùng và cache của các ứng dụng; việc xóa thư mục này có thể gây mất cài đặt hoặc lỗi ứng dụng.
- **Source:** [vv12] - Section: Chức năng của thư mục Roaming.
- **Tag:** [vv12]

- **Fact:** Microsoft Edge cho phép cài đặt nhiều phiên bản song song trong thư mục `Application` (ví dụ: bản 131.0.2903.112 và 131.0.2903.146); phiên bản cũ có thể được xóa thủ công hoặc qua lệnh `setup.exe --uninstall` trong thư mục `Installer`.
- **Source:** [vv12] - Section: Assistant: Nếu bạn đang có hai thư mục như trên.
- **Tag:** [vv12]

- **Fact:** Việc xóa trực tiếp các thư mục trong `C:\Program Files (x86)\Microsoft` không được khuyến khích vì có thể chứa các thư viện chia sẻ (Microsoft Visual C++ Redistributable) cần thiết cho ứng dụng bên thứ ba (như Game, phần mềm kỹ thuật).
- **Source:** [vv12] - Section: Những gì KHÔNG NÊN xóa.
- **Tag:** [vv12]
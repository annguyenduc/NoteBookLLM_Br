---
description: Quy trình bảo trì Gateway, cập nhật model và kiểm tra sức khỏe hệ thống (Global SOP).
---

# /maintenance-gateway

Workflow này hỗ trợ kiểm tra sức khỏe và bảo trì định kỳ cho SmartProxyHub Gateway.

## Các bước thực hiện

1. **Kiểm tra kết nối Gateway**
Kiểm tra xem Gateway có đang phản hồi tại cổng 4000 không.
```powershell
curl http://localhost:4000/health
```

2. **Đồng bộ hóa lại cấu hình (Sync)**
Nếu có thay đổi trong `.env`, hãy đồng bộ hóa lại các key.
```powershell
// turbo
powershell.exe -ExecutionPolicy Bypass -File "D:\01_Workspaces\SmartProxyHub\apps\smart_proxy\start_proxy.ps1"
```

3. **Hướng dẫn bảo trì nâng cao**
Nếu Gateway vẫn báo OFFLINE sau khi restart, hãy đọc tài liệu hướng dẫn:
[MAINTENANCE_GUIDE.md](file:///D:/01_Workspaces/SmartProxyHub/apps/smart_proxy/MAINTENANCE_GUIDE.md)

> [!TIP]
> Luôn ưu tiên dùng `openrouter/free` trong file `litellm_config.yaml` để đạt độ ổn định cao nhất.

---
description: Khởi chạy Smart AI Router (Gateway Port 4000) phục vụ Swarm Agent.
---

// turbo
1. Chạy PowerShell script để khởi động Proxy Hub:
```powershell
powershell.exe -ExecutionPolicy Bypass -File "D:\01_Workspaces\SmartProxyHub\apps\smart_proxy\start_proxy.ps1"
```

2. Kiểm tra sức khỏe Gateway sau 5 giây:
```powershell
Start-Sleep -Seconds 5; curl http://localhost:4000/health
```

> [!NOTE]
> Sau khi chạy lệnh này, **@gateway** sẽ sẵn sàng tiếp nhận các yêu cầu điều phối AI từ bạn.

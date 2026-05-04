# migrate_to_d.ps1
# Script di chuyển thư mục sang ổ D và tạo Junction Points

$ErrorActionPreference = "Stop"

$sourceBase = "C:\Users\anngu"
$destBase = "D:\anngu"
$folders = @(".codex", ".platformio", ".antigravity", ".vscode", ".cache", ".gemini")

# 1. Tạo thư mục đích
if (!(Test-Path $destBase)) {
    Write-Host "[+] Creating destination base: $destBase" -ForegroundColor Cyan
    New-Item -ItemType Directory -Path $destBase | Out-Null
}

foreach ($folder in $folders) {
    $src = Join-Path $sourceBase $folder
    $dst = Join-Path $destBase $folder

    Write-Host "`n--- Processing $folder ---" -ForegroundColor Yellow

    if (!(Test-Path $src)) {
        Write-Host "[!] Source $src does not exist. Skipping." -ForegroundColor Gray
        continue
    }

    # Kiểm tra xem đây có phải là Junction Link không
    if (Test-Path $src) {
        $item = Get-Item $src
        if ($item.Attributes -match "ReparsePoint") {
            $currentTarget = $item.Target
            if ($currentTarget -ne $dst) {
                Write-Host "[!] $src is a Junction pointing to $currentTarget. Re-linking to $dst..." -ForegroundColor Yellow
                Remove-Item $src -Force
                # Không cần move dữ liệu ở đây vì có thể target cũ nằm ở chỗ khác, 
                # người dùng nên move thủ công hoặc để script xử lý ở bước robocopy sau
            } else {
                Write-Host "[v] $src is already a Junction pointing to the correct destination. Skipping." -ForegroundColor Green
                continue
            }
        }
    }

    Write-Host "[>] Sequential Sync/Move: $src -> $dst" -ForegroundColor Cyan
    
    # Sử dụng robocopy /COPY:DAT (Data, Attributes, Timestamps) thay vì /COPYALL để tránh lỗi Auditing
    $rc = robocopy $src $dst /E /MOVE /COPY:DAT /R:1 /W:1 /XF *.log *.lock /NFL /NDL
    
    # Robocopy exit code >= 8 có nghĩa là có lỗi nghiêm trọng
    if ($LASTEXITCODE -ge 8) {
        Write-Host "[!] Error moving $folder. Exit code: $LASTEXITCODE" -ForegroundColor Red
        Write-Host "[!] Make sure all applications (VS Code, etc.) are closed." -ForegroundColor Red
        continue
    }

    # Đảm bảo thư mục gốc đã được xóa (robocopy /MOVE đôi khi để lại thư mục gốc nếu có file bị khóa)
    if (Test-Path $src) {
        Remove-Item $src -Recurse -Force -ErrorAction SilentlyContinue
    }

    # Tạo Junction Point
    Write-Host "[+] Creating Junction Point for $folder" -ForegroundColor Green
    cmd /c "mklink /J ""$src"" ""$dst"""
}

Write-Host "`n[***] Migration Complete! You can now restart your applications." -ForegroundColor Magenta
pause

# repair_migration.ps1
# Script sửa lỗi Junction Point cho .gemini sau khi chuyển sang ổ D

$ErrorActionPreference = "Continue" # Cho phép tiếp tục nếu gặp file bị khóa

$source = "C:\Users\anngu\.gemini"
$dest = "D:\anngu\.gemini"

Write-Host "--- Repairing .gemini Junction ---" -ForegroundColor Cyan

# 1. Đồng bộ dữ liệu mới phát sinh từ C sang D
if (Test-Path $source) {
    Write-Host "[>] Syncing residual data: $source -> $dest" -ForegroundColor Yellow
    # Không dùng /MOVE ở đây để tránh lỗi nếu file bị khóa, chỉ COPY
    robocopy $source $dest /E /COPY:DAT /R:1 /W:1 /XF *.log *.lock /NFL /NDL | Out-Null
}

# 2. Thử xóa thư mục trên C
Write-Host "[>] Attempting to remove $source to create Junction..." -ForegroundColor Yellow
if (Test-Path $source) {
    # Thử xóa từng phần, bỏ qua các lỗi do file bị khóa
    Remove-Item $source -Recurse -Force -ErrorAction SilentlyContinue
}

# 3. Kiểm tra xem đã xóa sạch chưa
if (Test-Path $source) {
    $item = Get-Item $source
    if ($item.Attributes -match "ReparsePoint") {
        Write-Host "[v] $source is already a Junction. Target: $($item.Target)" -ForegroundColor Green
    } else {
        Write-Host "[!] $source still exists and is NOT a Junction. Some files might be locked." -ForegroundColor Red
        Write-Host "[!] ACTIONS REQUIRED:" -ForegroundColor White
        Write-Host "    1. Close VS Code and any other applications." -ForegroundColor White
        Write-Host "    2. Run this command manually in Admin PowerShell:" -ForegroundColor White
        Write-Host "       Remove-Item $source -Recurse -Force" -ForegroundColor Cyan
        Write-Host "       cmd /c mklink /J $source $dest" -ForegroundColor Cyan
    }
} else {
    # 4. Tạo Junction Point nếu thư mục đã biến mất thành công
    Write-Host "[+] Creating Junction Point for .gemini" -ForegroundColor Green
    cmd /c "mklink /J ""$source"" ""$dest"""
}

Write-Host "`n--- Verification ---" -ForegroundColor Cyan
if (Test-Path $source) {
    $item = Get-Item $source
    if ($item.Attributes -match "ReparsePoint") {
        Write-Host "[v] SUCCESS: .gemini is now a Junction pointing to $dest" -ForegroundColor Green
    } else {
        Write-Host "[x] FAILED: .gemini is still a regular folder." -ForegroundColor Red
    }
} else {
    Write-Host "[x] FAILED: .gemini path not found." -ForegroundColor Red
}

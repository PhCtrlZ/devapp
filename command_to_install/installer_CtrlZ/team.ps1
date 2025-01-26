# Kiểm tra nếu không chạy với quyền admin
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "Script không chạy dưới quyền admin. Đang khởi động lại với quyền admin..." -ForegroundColor Yellow
    
    # Lấy đường dẫn của chính script này
    $scriptPath = $MyInvocation.MyCommand.Path

    # Tự khởi chạy lại script với quyền admin
    Start-Process powershell.exe -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`"" -Verb RunAs

    # Thoát script hiện tại (vì phiên bản admin sẽ được mở)
    exit
}

# Nếu đã chạy với quyền admin, tiếp tục thực thi
Write-Host "Script đang chạy với quyền admin!" -ForegroundColor Green
Set-ExecutionPolicy RemoteSigned
choco install teamviewer
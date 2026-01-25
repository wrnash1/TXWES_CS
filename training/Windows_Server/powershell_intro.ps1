# powershell_intro.ps1 - Windows Server Labs Starter

# Note: This runs in PowerShell Core (pwsh) on Fedora

Write-Host "Welcome to Windows Server Concepts Lab!" -ForegroundColor Cyan

# 1. Get system information
Get-ComputerInfo | Select-Object OsName, OsVersion, CsCaption

# 2. List running services
Get-Service | Where-Object {$_.Status -eq "Running"} | Select-Object -First 5

# 3. Create a local log (Mocking Event Viewer)
"Lab Started at $(Get-Date)" | Out-File -FilePath "$PSScriptRoot/lab_audit.log" -Append

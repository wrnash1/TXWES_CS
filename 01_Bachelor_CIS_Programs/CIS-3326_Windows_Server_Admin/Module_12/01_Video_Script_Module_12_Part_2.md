# Video Script: Module 12 — PowerShell for Server Administration (Part 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 11–13 minutes

**Part 2 focus:** Functions, error handling, script files, exporting output,
PowerShell Remoting, scheduled tasks, and server health reporting scripts.
Exam tips and lab preview.

---

## Opening

Welcome back to Module 12. In Part 1 we covered the core language features.
Now let's write real scripts — reusable functions, error handling, output to
files, and remote management.

---

## Demo 1 — Writing Functions

Functions let you encapsulate logic and reuse it.

[SHOW SCREEN: PowerShell ISE or VS Code with a script file open]
[Alt-text: Visual Studio Code window with a PowerShell script containing a function definition.]

```powershell
# Basic function
function Get-ServerHealth {
    param(
        [Parameter(Mandatory=$true)]
        [string]$ComputerName
    )

    $cpu   = Get-WmiObject Win32_Processor -ComputerName $ComputerName |
                 Measure-Object -Property LoadPercentage -Average |
                 Select-Object -ExpandProperty Average

    $mem   = Get-WmiObject Win32_OperatingSystem -ComputerName $ComputerName
    $memFreeGB = [math]::Round($mem.FreePhysicalMemory / 1MB, 2)

    $disk  = Get-WmiObject Win32_LogicalDisk -ComputerName $ComputerName `
                 -Filter "DeviceID='C:'" |
                 Select-Object @{n='FreeGB';e={[math]::Round($_.FreeSpace/1GB,2)}}

    [PSCustomObject]@{
        ComputerName = $ComputerName
        CPU_Pct      = $cpu
        MemFree_GB   = $memFreeGB
        DiskC_FreeGB = $disk.FreeGB
        Timestamp    = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    }
}

# Call the function
Get-ServerHealth -ComputerName "DC1"
```

`[PSCustomObject]` creates a custom object with exactly the properties you
define. This is how you build structured output from a function.

`[Parameter(Mandatory=$true)]` means PowerShell will prompt for the value if
you forget to pass it.

---

## Demo 2 — Error Handling with Try/Catch

Without error handling, a script stops at the first error. With Try/Catch, you
control what happens when something goes wrong.

```powershell
function Test-ServiceStatus {
    param(
        [string]$ServiceName,
        [string]$ComputerName = "localhost"
    )

    try {
        $svc = Get-Service -Name $ServiceName -ComputerName $ComputerName -ErrorAction Stop

        [PSCustomObject]@{
            Computer = $ComputerName
            Service  = $ServiceName
            Status   = $svc.Status
            Error    = $null
        }
    }
    catch {
        [PSCustomObject]@{
            Computer = $ComputerName
            Service  = $ServiceName
            Status   = "ERROR"
            Error    = $_.Exception.Message
        }
    }
}

$servers = @("DC1", "FS01", "BADSERVER")

$results = foreach ($srv in $servers) {
    Test-ServiceStatus -ServiceName "Spooler" -ComputerName $srv
}

$results | Format-Table -AutoSize
```

`-ErrorAction Stop` converts non-terminating errors into terminating errors so
they can be caught. Without it, `Get-Service` would display an error in red
but continue — the catch block would never run.

---

## Demo 3 — Exporting Output to Files

```powershell
# Export to CSV
$results | Export-Csv -Path "C:\Reports\ServiceStatus.csv" -NoTypeInformation

# Export to text (plain)
$results | Out-File -FilePath "C:\Reports\ServiceStatus.txt"

# Export to HTML
$results | ConvertTo-Html -Title "Service Status Report" -PreContent "<h1>Service Status</h1>" |
    Out-File "C:\Reports\ServiceStatus.html"

# Append to an existing log file
"$(Get-Date) — Report generated" | Out-File -FilePath "C:\Logs\audit.log" -Append

# Import previously exported CSV
$imported = Import-Csv -Path "C:\Reports\ServiceStatus.csv"
$imported | Where-Object {$_.Status -eq "ERROR"}
```

`-NoTypeInformation` removes the `#TYPE` header that Export-Csv adds by
default. Always use this flag.

---

## Demo 4 — PowerShell Remoting

PowerShell Remoting lets you run cmdlets on remote servers. It uses WinRM
(Windows Remote Management) as the transport.

Enable remoting on the target server — run this as Administrator.

```powershell
Enable-PSRemoting -Force
```

This creates the WinRM listener, opens port 5985 in the firewall, and starts
the WinRM service.

Interactive session on a single remote server.

```powershell
Enter-PSSession -ComputerName "FS01"
# Your prompt changes to [FS01]: PS C:\>
# Run any command here and it executes on FS01

Get-Service | Where-Object {$_.Status -eq "Stopped"}
Exit-PSSession
```

Fan-out command to multiple servers.

```powershell
$servers = @("DC1", "FS01", "APP01")

Invoke-Command -ComputerName $servers -ScriptBlock {
    Get-EventLog -LogName System -EntryType Error -Newest 5 |
        Select-Object TimeGenerated, Source, Message
}
```

[SHOW SCREEN: Invoke-Command output with PSComputerName column]
[Alt-text: PowerShell table showing event log results from three servers, each row labeled with PSComputerName showing DC1, FS01, or APP01.]

The `PSComputerName` property on each result object tells you which server
returned that row. This is how you distinguish results when querying many
servers at once.

Save a reusable session for repeated commands.

```powershell
$session = New-PSSession -ComputerName "FS01"

Invoke-Command -Session $session -ScriptBlock { Get-Process | Measure-Object }
Invoke-Command -Session $session -ScriptBlock { Get-Service | Where-Object {$_.Status -eq "Running"} | Measure-Object }

Remove-PSSession -Session $session
```

---

## Demo 5 — Scheduled Tasks with PowerShell

You can create Windows Scheduled Tasks from PowerShell, which is useful for
automating recurring admin scripts.

```powershell
# Create a scheduled task to run a script every day at 6 AM
$action  = New-ScheduledTaskAction `
    -Execute "PowerShell.exe" `
    -Argument "-NonInteractive -File C:\Scripts\DailyHealthCheck.ps1"

$trigger = New-ScheduledTaskTrigger -Daily -At "06:00AM"

$settings = New-ScheduledTaskSettingsSet `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1) `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 5)

Register-ScheduledTask `
    -TaskName "DailyServerHealthCheck" `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -RunLevel Highest `
    -User "SYSTEM"
```

`-RunLevel Highest` runs the task with elevated privileges.
`-User "SYSTEM"` runs as the local system account without needing credentials.

---

## Demo 6 — Complete Server Health Report Script

Let's put it all together in a full script.

```powershell
# DailyHealthCheck.ps1
# Run daily to check service status and disk space on all domain servers

param(
    [string]$OutputPath = "C:\Reports",
    [int]$DiskWarningGB = 10
)

$servers = @("DC1", "FS01", "APP01")
$reportDate = Get-Date -Format "yyyy-MM-dd"

# Ensure output directory exists
New-Item -Path $OutputPath -ItemType Directory -Force | Out-Null

$results = foreach ($srv in $servers) {
    try {
        # Get critical services
        $services = @("DNS", "NTDS", "W32Time") | ForEach-Object {
            Get-Service -Name $_ -ComputerName $srv -ErrorAction Stop
        }

        $stoppedSvcs = ($services | Where-Object {$_.Status -ne "Running"}).Count

        # Get disk space
        $disk = Get-WmiObject Win32_LogicalDisk `
            -ComputerName $srv `
            -Filter "DeviceID='C:'" `
            -ErrorAction Stop

        $freeGB = [math]::Round($disk.FreeSpace / 1GB, 1)

        [PSCustomObject]@{
            Server        = $srv
            StoppedSvcs   = $stoppedSvcs
            DiskC_FreeGB  = $freeGB
            DiskWarning   = ($freeGB -lt $DiskWarningGB)
            Status        = if ($stoppedSvcs -gt 0 -or $freeGB -lt $DiskWarningGB) {"WARNING"} else {"OK"}
            Checked       = $reportDate
        }
    }
    catch {
        [PSCustomObject]@{
            Server        = $srv
            StoppedSvcs   = -1
            DiskC_FreeGB  = -1
            DiskWarning   = $true
            Status        = "UNREACHABLE"
            Checked       = $reportDate
        }
    }
}

# Export to CSV
$csvPath = "$OutputPath\Health_$reportDate.csv"
$results | Export-Csv -Path $csvPath -NoTypeInformation

# Display summary
$results | Format-Table -AutoSize

Write-Host "Report saved: $csvPath" -ForegroundColor Green
```

---

## Exam Tips

**Exam Tip 1** — `Get-EventLog` vs. `Get-WinEvent`: for the exam, know that
`Get-WinEvent -FilterHashtable` is more efficient than piping `Get-EventLog`
to `Where-Object` because filtering happens at the source (the event log
subsystem) rather than in memory.

**Exam Tip 2** — `-ErrorAction Stop` is required for try/catch to work on
non-terminating errors. Without it, errors from `Get-Service`, `Get-Process`,
and similar cmdlets go to the error stream but do not trigger the catch block.

**Exam Tip 3** — `Invoke-Command` fans out to multiple computers in parallel.
`Enter-PSSession` creates an interactive one-to-one session. For bulk
operations across servers, use `Invoke-Command`.

**Exam Tip 4** — `Export-Csv -NoTypeInformation` removes the `#TYPE` metadata
header. Always include this flag when creating CSV files for import into Excel
or other tools.

**Exam Tip 5** — PowerShell execution policy: scripts are blocked by default.
`Set-ExecutionPolicy RemoteSigned` allows local scripts and requires signed
scripts from remote sources. Know the four policies: Restricted, AllSigned,
RemoteSigned, Unrestricted.

---

## Lab Preview

In Lab 12, you will write and run PowerShell scripts that query services,
check disk space, query event logs with `Get-EventLog` and `Get-WinEvent`,
use `Invoke-Command` to query a remote server, export results to CSV, and
create a scheduled task to run a script automatically. Complete all parts and
submit the required screenshots.

See you in the quiz.

---

Module 12 Part 2 — End of Script

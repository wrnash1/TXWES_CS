# Lab Activity: Module 12 — PowerShell for Server Administration

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will practice core PowerShell skills for server administration:
querying and managing services, querying processes, querying event logs with
both `Get-EventLog` and `Get-WinEvent`, exporting results to CSV, writing a
function with error handling, and using PowerShell Remoting.

**Estimated Time:** 75–90 minutes

**Prerequisites:**

- DC1 is running Windows Server 2022 and is a domain controller for txwes.edu
- You are logged in as a Domain Administrator
- PowerShell console is open with Administrator privileges
- WinRM is enabled (run `Enable-PSRemoting -Force` if needed)

**Learning Objectives:**

- Use `Get-Service`, `Set-Service`, `Start-Service`, `Stop-Service`
- Use `Get-Process` with pipeline filtering and sorting
- Query event logs with `Get-EventLog` and `Get-WinEvent -FilterHashtable`
- Write a function with parameters, try/catch, and `[PSCustomObject]` output
- Export results to CSV with `Export-Csv -NoTypeInformation`
- Use `Invoke-Command` to query a remote computer

---

## Part 1 — Service Management

### Step 1.1 — Query All Services

```powershell
# Get all services sorted by status
Get-Service | Sort-Object Status | Select-Object Name, Status, StartType |
    Format-Table -AutoSize
```

### Step 1.2 — Filter Stopped Services

```powershell
Get-Service | Where-Object {$_.Status -eq "Stopped"} |
    Select-Object Name, DisplayName, StartType |
    Sort-Object Name
```

Take **Screenshot 1** — Stopped services list with Name, DisplayName, and
StartType columns.

### Step 1.3 — Query a Specific Service

```powershell
Get-Service -Name "W32Time" | Select-Object Name, DisplayName, Status, StartType
```

### Step 1.4 — Stop, Verify, and Restart a Service

```powershell
# Stop the Windows Time service (safe to stop in lab)
Stop-Service -Name "W32Time"

# Verify it stopped
Get-Service -Name "W32Time" | Select-Object Name, Status

# Restart it
Start-Service -Name "W32Time"

# Verify it started
Get-Service -Name "W32Time" | Select-Object Name, Status
```

### Step 1.5 — Find Services by Display Name Pattern

```powershell
Get-Service | Where-Object {$_.DisplayName -like "*Windows*"} |
    Select-Object Name, DisplayName, Status |
    Sort-Object DisplayName
```

Take **Screenshot 2** — Services matching the Windows display name pattern.

---

## Part 2 — Process Management

### Step 2.1 — List All Running Processes

```powershell
Get-Process | Sort-Object WorkingSet -Descending |
    Select-Object Name, Id, CPU, @{n="MemMB";e={[math]::Round($_.WorkingSet/1MB,1)}} |
    Select-Object -First 15
```

Take **Screenshot 3** — Top 15 processes by memory usage.

### Step 2.2 — Find Processes by Name

```powershell
Get-Process | Where-Object {$_.Name -like "power*"} |
    Select-Object Name, Id, CPU, StartTime
```

### Step 2.3 — Count Total Processes

```powershell
Get-Process | Measure-Object | Select-Object Count

# Count by name pattern
Get-Process | Where-Object {$_.Name -eq "svchost"} | Measure-Object | Select-Object Count
```

---

## Part 3 — Event Log Queries

### Step 3.1 — Get Recent System Log Events with Get-EventLog

```powershell
Get-EventLog -LogName System -Newest 20 |
    Select-Object TimeGenerated, EntryType, Source, Message |
    Format-Table -AutoSize -Wrap
```

### Step 3.2 — Filter by EntryType

```powershell
Get-EventLog -LogName System -EntryType Error,Warning -Newest 30 |
    Select-Object TimeGenerated, EntryType, Source, InstanceId |
    Sort-Object TimeGenerated -Descending
```

Take **Screenshot 4** — System log errors and warnings with timestamp and source.

### Step 3.3 — Filter by Time Range

```powershell
$since = (Get-Date).AddHours(-4)

Get-EventLog -LogName System -After $since |
    Select-Object TimeGenerated, EntryType, Source, Message |
    Sort-Object TimeGenerated -Descending
```

### Step 3.4 — Use Get-WinEvent with FilterHashtable

```powershell
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    Level     = 2          # 2=Error, 3=Warning, 4=Information
    StartTime = (Get-Date).AddHours(-24)
} | Select-Object TimeCreated, Id, LevelDisplayName, Message |
    Select-Object -First 10
```

Take **Screenshot 5** — `Get-WinEvent -FilterHashtable` output showing recent
errors from the System log.

### Step 3.5 — Search for Service Control Manager Events

```powershell
Get-WinEvent -FilterHashtable @{
    LogName  = 'System'
    ProviderName = 'Service Control Manager'
} | Select-Object TimeCreated, Id, Message -First 10
```

---

## Part 4 — Writing a Function with Error Handling

### Step 4.1 — Write the Function

In PowerShell, define the following function.

```powershell
function Get-ServiceReport {
    param(
        [Parameter(Mandatory=$true)]
        [string[]]$ServiceNames,

        [string]$ComputerName = "localhost"
    )

    foreach ($svcName in $ServiceNames) {
        try {
            $svc = Get-Service -Name $svcName -ComputerName $ComputerName -ErrorAction Stop

            [PSCustomObject]@{
                Computer   = $ComputerName
                Service    = $svcName
                Status     = $svc.Status
                StartType  = $svc.StartType
                Error      = $null
            }
        }
        catch {
            [PSCustomObject]@{
                Computer   = $ComputerName
                Service    = $svcName
                Status     = "NOT FOUND"
                StartType  = "N/A"
                Error      = $_.Exception.Message
            }
        }
    }
}
```

### Step 4.2 — Call the Function with Valid and Invalid Service Names

```powershell
$services = @("DNS", "W32Time", "Spooler", "FakeService123", "NTDS")

$report = Get-ServiceReport -ServiceNames $services -ComputerName "DC1"
$report | Format-Table -AutoSize
```

Take **Screenshot 6** — Function output showing mix of real services (with
Status) and the fake service (NOT FOUND with error message).

### Step 4.3 — Export the Report to CSV

```powershell
New-Item -Path "C:\PSReports" -ItemType Directory -Force | Out-Null

$report | Export-Csv -Path "C:\PSReports\ServiceReport.csv" -NoTypeInformation

# Verify the file was created
Get-Item "C:\PSReports\ServiceReport.csv" | Select-Object Name, Length, LastWriteTime

# View the CSV content
Import-Csv -Path "C:\PSReports\ServiceReport.csv"
```

Take **Screenshot 7** — `Import-Csv` output showing the exported report data.

---

## Part 5 — PowerShell Remoting

### Step 5.1 — Enable Remoting

Run the following on DC1 if not already enabled.

```powershell
Enable-PSRemoting -Force
```

Verify WinRM is running.

```powershell
Get-Service -Name WinRM | Select-Object Name, Status, StartType
```

### Step 5.2 — Use Invoke-Command

```powershell
Invoke-Command -ComputerName "DC1" -ScriptBlock {
    Get-Service | Where-Object {$_.Status -eq "Running"} | Measure-Object |
        Select-Object Count
}
```

### Step 5.3 — Fan Out to DC1 (Simulating Multi-Server)

In this lab, use the DC1 hostname as both the local and remote target to
demonstrate the Invoke-Command pattern.

```powershell
$servers = @("DC1", "localhost")

$results = Invoke-Command -ComputerName $servers -ScriptBlock {
    [PSCustomObject]@{
        Computer      = $env:COMPUTERNAME
        RunningProcs  = (Get-Process).Count
        RunningServices = (Get-Service | Where-Object {$_.Status -eq "Running"}).Count
    }
}

$results | Select-Object Computer, RunningProcs, RunningServices | Format-Table -AutoSize
```

Take **Screenshot 8** — `Invoke-Command` output showing results from both
targets with PSComputerName visible.

---

## Part 6 — Event Log Export and Analysis

```powershell
# Get last 50 System log errors and warnings
$events = Get-EventLog -LogName System -EntryType Error,Warning -Newest 50 |
    Select-Object TimeGenerated, EntryType, Source, InstanceId, Message

# Export to CSV
$events | Export-Csv -Path "C:\PSReports\SystemLogReport.csv" -NoTypeInformation

Write-Host "Exported $($events.Count) events to C:\PSReports\SystemLogReport.csv"

# Summary: count by EntryType
$events | Group-Object EntryType | Select-Object Name, Count | Format-Table -AutoSize

# Summary: count by Source (top 5)
$events | Group-Object Source | Sort-Object Count -Descending |
    Select-Object -First 5 Name, Count | Format-Table -AutoSize
```

Take **Screenshot 9** — Event source summary showing top 5 sources by count.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — Stopped services with Name, DisplayName, StartType.

**Screenshot 2** — Services matching "Windows" display name pattern.

**Screenshot 3** — Top 15 processes by memory usage.

**Screenshot 4** — System log errors and warnings from `Get-EventLog`.

**Screenshot 5** — `Get-WinEvent -FilterHashtable` output.

**Screenshot 6** — `Get-ServiceReport` function output with valid and invalid services.

**Screenshot 7** — `Import-Csv` showing the exported service report.

**Screenshot 8** — `Invoke-Command` output from two targets.

**Screenshot 9** — Event source summary grouped by source.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| Service management queries | 10 | Screenshots 1-2 show correct filtered service output |
| Process management queries | 10 | Screenshot 3 shows top processes by memory |
| Get-EventLog queries | 15 | Screenshot 4 shows filtered error/warning events |
| Get-WinEvent queries | 15 | Screenshot 5 shows FilterHashtable usage |
| Function with error handling | 25 | Screenshot 6 shows correct output with both valid and error rows |
| CSV export and import | 10 | Screenshot 7 shows Import-Csv reading the exported file |
| PowerShell Remoting | 10 | Screenshot 8 shows Invoke-Command results from two targets |
| Event export and analysis | 5 | Screenshot 9 shows grouped event source summary |

---

## Troubleshooting Notes

If `Invoke-Command` fails with "WinRM cannot complete the operation," run
`Enable-PSRemoting -Force` on the target server and ensure the Windows
Firewall allows WinRM (port 5985).

If `Get-EventLog -LogName Security` returns "Requested registry access is not
allowed," run PowerShell as Administrator.

If `Get-WinEvent -FilterHashtable` returns no results, try removing the
`StartTime` filter first to confirm events exist in the log.

```powershell
# Verify PowerShell remoting is configured
Test-WSMan -ComputerName "DC1"
```

If the output shows an XML response with `productVendor: Microsoft`, WinRM is
working correctly.

# Reading Guide: Module 12 — PowerShell for Server Administration

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 12 covers PowerShell as the primary tool for Windows Server automation
and administration. This reading guide provides reference tables for cmdlet
syntax, pipeline operations, service and process management, event log queries,
scripting constructs, and PowerShell Remoting. Includes a PowerShell command
reference, 8 exam tips, a glossary, and a study checklist.

---

## 1. PowerShell Fundamentals

### Cmdlet Naming Convention

All PowerShell cmdlets follow the Verb-Noun pattern.

| Verb | Meaning | Example |
|---|---|---|
| Get | Retrieve information | `Get-Service` |
| Set | Modify an existing object | `Set-Service` |
| New | Create a new object | `New-Item` |
| Remove | Delete an object | `Remove-Item` |
| Start | Start a process or service | `Start-Service` |
| Stop | Stop a process or service | `Stop-Service` |
| Enable | Enable a feature or rule | `Enable-PSRemoting` |
| Disable | Disable a feature or rule | `Disable-NetFirewallRule` |
| Invoke | Run a command or script | `Invoke-Command` |
| Export | Save data to a file | `Export-Csv` |
| Import | Load data from a file | `Import-Csv` |

### Key Pipeline Cmdlets

| Cmdlet | Purpose |
|---|---|
| `Where-Object` | Filter objects based on a condition |
| `Select-Object` | Choose specific properties |
| `Sort-Object` | Sort by one or more properties |
| `ForEach-Object` | Run a script block for each object |
| `Measure-Object` | Count, sum, average, min, max |
| `Group-Object` | Group objects by a property value |
| `Format-Table` | Display as table (use last in pipeline) |
| `Format-List` | Display as property list (use last in pipeline) |
| `Out-File` | Write output to a file |
| `Export-Csv` | Export objects to CSV |
| `ConvertTo-Html` | Convert objects to HTML table |

---

## 2. Service Management

```powershell
# ── Query ─────────────────────────────────────────────────────────────
Get-Service                                          # all services
Get-Service -Name "Spooler"                          # specific service
Get-Service | Where-Object {$_.Status -eq "Stopped"} # stopped services
Get-Service | Where-Object {$_.DisplayName -like "*Windows*"}

# ── Control ───────────────────────────────────────────────────────────
Start-Service   -Name "Spooler"
Stop-Service    -Name "Spooler"
Restart-Service -Name "Spooler"

# ── Configure ─────────────────────────────────────────────────────────
Set-Service -Name "Spooler" -StartupType Automatic
Set-Service -Name "Spooler" -StartupType Disabled
Set-Service -Name "Spooler" -StartupType Manual
```

### Service StartupType Values

| StartupType | Meaning |
|---|---|
| Automatic | Starts when Windows boots |
| Manual | Starts only when explicitly called |
| Disabled | Cannot be started until re-enabled |
| AutomaticDelayedStart | Starts after boot sequence completes (delayed) |

---

## 3. Process Management

```powershell
Get-Process                                          # all running processes
Get-Process -Name "notepad"                          # by name
Get-Process | Sort-Object WorkingSet -Descending |
    Select-Object -First 10 Name, Id, WorkingSet    # top 10 by memory
Stop-Process -Name "notepad" -Confirm
Stop-Process -Id 1234 -Force
Start-Process -FilePath "notepad.exe"
Start-Process -FilePath "powershell.exe" -Verb RunAs  # run as admin
```

---

## 4. Event Log Queries

### Get-EventLog (Classic Logs)

```powershell
Get-EventLog -LogName System -Newest 20
Get-EventLog -LogName Application -EntryType Error -Newest 50
Get-EventLog -LogName System -EntryType Error,Warning `
    -After (Get-Date).AddHours(-24)
Get-EventLog -LogName System -Source "Service Control Manager" -Newest 10
```

### Get-WinEvent (Modern — Recommended)

```powershell
Get-WinEvent -LogName "Application" -MaxEvents 20

# FilterHashtable — most efficient approach
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625
    StartTime = (Get-Date).AddDays(-1)
}

# Common Security Event IDs
# 4624 — Successful logon
# 4625 — Failed logon
# 4634 — Logoff
# 4648 — Logon using explicit credentials
# 4740 — Account locked out
# 7036 — Service state change (System log)
```

### EntryType Values for Get-EventLog

| EntryType | Meaning |
|---|---|
| Error | Critical failure requiring action |
| Warning | Potential issue; not immediately critical |
| Information | Normal operational event |
| SuccessAudit | Security audit event — success |
| FailureAudit | Security audit event — failure |

---

## 5. PowerShell Scripting Constructs

### Variables and Types

```powershell
$name    = "Server01"          # string
$count   = 42                  # integer
$size    = 100GB               # long (GB/MB/KB multipliers)
$enabled = $true               # boolean
$now     = Get-Date            # DateTime
$list    = @("A", "B", "C")    # array
$hash    = @{Key = "Value"}    # hashtable
```

### Conditional Logic

```powershell
if ($condition) { ... }
elseif ($otherCondition) { ... }
else { ... }

switch ($value) {
    "case1" { ... }
    "case2" { ... }
    default { ... }
}
```

### Loops

```powershell
foreach ($item in $collection) { ... }
for ($i = 0; $i -lt 10; $i++) { ... }
while ($condition) { ... }
$collection | ForEach-Object { ... }    # pipeline version
```

### Functions

```powershell
function Verb-Noun {
    param(
        [Parameter(Mandatory=$true)]
        [string]$RequiredParam,

        [string]$OptionalParam = "default"
    )

    # function body
    return $result
}
```

### Error Handling

```powershell
try {
    Get-Service -Name "Nonexistent" -ErrorAction Stop
}
catch {
    Write-Warning "Error: $($_.Exception.Message)"
}
finally {
    Write-Host "Runs whether success or failure"
}
```

`-ErrorAction Stop` is required to make non-terminating errors catchable.

### Custom Objects

```powershell
[PSCustomObject]@{
    Property1 = "Value1"
    Property2 = 42
    Property3 = Get-Date
}
```

---

## 6. File and Output Operations

```powershell
# Write output
Write-Host "Message" -ForegroundColor Cyan      # to console only
Write-Output "Message"                          # to pipeline
Write-Warning "Warning text"                    # yellow warning
Write-Error "Error text"                        # red error
Write-Verbose "Verbose" -Verbose                # only when -Verbose flag used

# File operations
Out-File -FilePath "C:\output.txt"
Out-File -FilePath "C:\log.txt" -Append         # append mode
Export-Csv -Path "C:\output.csv" -NoTypeInformation
Import-Csv -Path "C:\input.csv"
ConvertTo-Html | Out-File "C:\report.html"
Get-Content -Path "C:\file.txt"
Set-Content -Path "C:\file.txt" -Value "text"
Add-Content -Path "C:\file.txt" -Value "more text"
```

---

## 7. PowerShell Remoting

```powershell
# Enable remoting on the target server (run as admin on that server)
Enable-PSRemoting -Force

# Interactive session
Enter-PSSession -ComputerName "Server01"
Exit-PSSession

# Fan-out to multiple computers
Invoke-Command -ComputerName @("DC1","FS01","APP01") -ScriptBlock {
    Get-Service | Where-Object {$_.Status -eq "Stopped"}
}

# Persistent session
$s = New-PSSession -ComputerName "Server01"
Invoke-Command -Session $s -ScriptBlock { Get-Process }
Remove-PSSession -Session $s

# Copy files to/from remote computer
Copy-Item -Path "C:\script.ps1" -Destination "C:\Scripts\" `
    -ToSession (New-PSSession -ComputerName "Server01")
```

### WinRM Ports

| Protocol | Port | Notes |
|---|---|---|
| HTTP | 5985 | Default; acceptable on trusted internal networks |
| HTTPS | 5986 | Required for remoting over untrusted networks |

---

## 8. Execution Policy

| Policy | Behavior |
|---|---|
| Restricted | No scripts can run (default on client) |
| AllSigned | All scripts must be digitally signed |
| RemoteSigned | Local scripts run freely; downloaded scripts must be signed |
| Unrestricted | All scripts run; prompts for downloaded scripts |
| Bypass | No restrictions; no prompts |

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy RemoteSigned -Scope LocalMachine
```

---

## 9. Scheduled Tasks with PowerShell

```powershell
$action  = New-ScheduledTaskAction -Execute "PowerShell.exe" `
               -Argument "-File C:\Scripts\task.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "06:00AM"
$settings = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Hours 1)

Register-ScheduledTask -TaskName "DailyTask" -Action $action `
    -Trigger $trigger -Settings $settings -RunLevel Highest -User "SYSTEM"

Get-ScheduledTask -TaskName "DailyTask"
Start-ScheduledTask -TaskName "DailyTask"
Unregister-ScheduledTask -TaskName "DailyTask" -Confirm:$false
```

---

## 10. Exam Tips

**Exam Tip 1** — `Where-Object` uses `$_` to reference the current pipeline
object. `$_.Name`, `$_.Status`, `$_.CPU` access named properties. This syntax
is tested frequently in cmdlet completion scenarios.

**Exam Tip 2** — `Get-WinEvent -FilterHashtable` is more efficient than
`Get-EventLog | Where-Object` because filtering happens at the event log
subsystem, not in PowerShell memory. Use `-FilterHashtable` for production
scripts.

**Exam Tip 3** — `-ErrorAction Stop` is required for try/catch to intercept
non-terminating errors. Without it, cmdlet errors go to the error stream and
the catch block never executes.

**Exam Tip 4** — `Invoke-Command` fans out to multiple computers in parallel
and adds a `PSComputerName` property to each result. `Enter-PSSession` is for
interactive one-to-one remote work.

**Exam Tip 5** — `Export-Csv -NoTypeInformation` must be used to avoid the
`#TYPE` metadata header line. This header breaks CSV imports in Excel and
other applications.

**Exam Tip 6** — Functions should follow the Verb-Noun naming convention, just
like built-in cmdlets. Use `[Parameter(Mandatory=$true)]` for required
parameters.

**Exam Tip 7** — Execution Policy is not a security barrier — it is a safety
guard. It can be bypassed by running `powershell.exe -ExecutionPolicy Bypass
-File script.ps1`. The correct policy for most enterprise environments is
`RemoteSigned`.

**Exam Tip 8** — `[PSCustomObject]@{}` creates structured output objects that
pass cleanly through the pipeline, can be exported to CSV, and are sorted and
filtered like any other object. Use this instead of `Write-Host` when building
reporting functions.

---

## 11. Glossary

| Term | Definition |
|---|---|
| Cmdlet | A PowerShell command following Verb-Noun naming convention |
| Pipeline | The mechanism that passes objects from one cmdlet to the next using `\|` |
| Object | A .NET instance with named properties and methods; the fundamental unit in the PowerShell pipeline |
| `$_` | Current pipeline object; used inside `Where-Object`, `ForEach-Object`, and similar |
| `Where-Object` | Filters pipeline objects based on a boolean condition |
| `Select-Object` | Selects specific properties from pipeline objects |
| `ForEach-Object` | Executes a script block for each pipeline object |
| `PSCustomObject` | A lightweight .NET object with user-defined properties |
| `Try/Catch/Finally` | PowerShell structured error handling construct |
| `-ErrorAction Stop` | Converts non-terminating errors into terminating errors so they can be caught |
| `Invoke-Command` | Runs a script block on one or more remote computers via WinRM |
| `Enter-PSSession` | Opens an interactive 1-to-1 remote PowerShell session |
| WinRM | Windows Remote Management — the transport protocol for PowerShell Remoting |
| `Export-Csv` | Exports pipeline objects to a comma-separated values file |
| `-FilterHashtable` | `Get-WinEvent` parameter for efficient server-side event log filtering |
| Execution Policy | PowerShell safety setting controlling which scripts can run |
| Scheduled Task | A Windows task that runs a script or program on a schedule |

---

## 12. Study Checklist

- Watch Module 12 Part 1 video (object model, cmdlet syntax, pipeline, services, processes, event logs)
- Watch Module 12 Part 2 video (functions, error handling, Remoting, scheduled tasks, full scripts)
- Know the Verb-Noun cmdlet naming convention and common verbs
- Know `Where-Object`, `Select-Object`, `Sort-Object`, `ForEach-Object` pipeline usage
- Know `Get-Service`, `Set-Service`, `Start-Service`, `Stop-Service`
- Know `Get-Process`, `Stop-Process`
- Know `Get-EventLog` and `Get-WinEvent -FilterHashtable` differences
- Understand `-ErrorAction Stop` and try/catch structure
- Know `Invoke-Command` vs. `Enter-PSSession` for remoting
- Know execution policy options (Restricted, AllSigned, RemoteSigned, Unrestricted)
- Complete Lab 12 and submit required screenshots

---

## Additional Resources

- [PowerShell documentation overview](https://learn.microsoft.com/en-us/powershell/scripting/overview)
- [about_Pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines)
- [Get-WinEvent documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)
- [Invoke-Command documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command)

---

## 13. Supplemental Resources

The following free, open-access resources go deeper on Module 12 topics:

**1. Microsoft Learn — Automate Windows Server administration with PowerShell**
<https://learn.microsoft.com/en-us/training/modules/automate-windows-server-administration-with-powershell/>
Hands-on module covering pipeline usage, scripting fundamentals, error handling, remoting with `Invoke-Command`, and scheduled task creation with sandbox exercises aligned to AZ-800.

**2. Microsoft Docs — about_Functions_Advanced_Parameters**
<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters>
Full reference for PowerShell parameter attributes including `Mandatory`, `ValueFromPipeline`, `ValueFromPipelineByPropertyName`, `ValidateSet`, and parameter validation, with examples for building production-quality cmdlet-style functions.

**3. Microsoft Docs — Get-WinEvent**
<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent>
Complete documentation for `Get-WinEvent` including `-FilterHashtable` syntax, filtering by event ID, time range, level, and provider, plus comparison with the deprecated `Get-EventLog` cmdlet.

**4. Microsoft Docs — about_Try_Catch_Finally**
<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally>
Explains PowerShell's structured error handling model: terminating vs. non-terminating errors, the role of `-ErrorAction Stop`, catching specific exception types, and using `$_.Exception.Message` for detailed error reporting in production scripts.

---

*Review all sections before beginning Lab 12, Quiz 12, and Discussion 12.*

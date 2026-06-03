# Quiz: Module 12 — PowerShell for Server Administration

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
Review your Reading Guide and video notes before beginning.

---

## Question 1

An administrator needs to list all Windows services that are currently stopped,
sorted alphabetically by display name. Which PowerShell command is correct?

A) `Get-Service -Status Stopped | Sort-Object DisplayName`

B) `Get-Service | Where-Object {$_.Status -eq "Stopped"} | Sort-Object DisplayName`

C) `Get-Service | Filter {Status = "Stopped"} | Sort-Object DisplayName`

D) `Get-Service -Filter "Status='Stopped'" | Sort-Object DisplayName`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Get-Service` does not have a `-Status` parameter for
    filtering. You must use `Where-Object` to filter on the Status property.
  - Why C is incorrect: `Filter` is not a valid pipeline cmdlet in PowerShell.
    The correct filtering cmdlet is `Where-Object`.
  - Why D is incorrect: `Get-Service` does not support a `-Filter` parameter.
    `-Filter` is used with Active Directory cmdlets and some file system cmdlets,
    not with `Get-Service`.

---

## Question 2

An administrator writes the following script.

```powershell
$services = @("DNS", "W32Time", "Spooler")

foreach ($svc in $services) {
    $result = Get-Service -Name $svc
    Write-Host "$($result.Name) is $($result.Status)"
}
```

The script runs successfully for DNS and W32Time, but throws a red error for
Spooler (which is not installed). Which change ensures the error is handled
gracefully and the script continues to the next service?

A) Change `Get-Service -Name $svc` to `Get-Service -Name $svc -Confirm`

B) Wrap the `Get-Service` call in a `try` block and add `-ErrorAction Stop`;
   add a `catch` block to handle the error.

C) Add `$ErrorActionPreference = "SilentlyContinue"` before the loop to suppress
   all errors.

D) Change `Write-Host` to `Write-Error` to redirect the output to the error
   stream.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-Confirm` prompts the administrator to confirm the
    action — it does not handle errors. `Get-Service` does not use `-Confirm`.
  - Why C is incorrect: `$ErrorActionPreference = "SilentlyContinue"` silences
    all errors silently, which hides legitimate errors and makes debugging
    impossible. It is not the same as graceful error handling.
  - Why D is incorrect: Changing `Write-Host` to `Write-Error` does not prevent
    the error from `Get-Service` from stopping the loop. The issue is the
    cmdlet throwing an error, not the output method.

---

## Question 3

An administrator needs to check the last 24 hours of Security event log entries
for failed logon events (Event ID 4625) on a server. Which PowerShell command
is most efficient?

A) `Get-EventLog -LogName Security -Newest 1000 | Where-Object {$_.InstanceId -eq 4625}`

B) `Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddDays(-1)}`

C) `Get-EventLog -LogName Security | Select-Object -ExpandProperty Message | Where-Object {$_ -like "*4625*"}`

D) `Get-EventLog -LogName Security -Source 4625 -After (Get-Date).AddDays(-1)`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This retrieves 1000 events into memory and then filters.
    `Get-WinEvent -FilterHashtable` filters at the event log subsystem level,
    which is significantly more efficient for large logs.
  - Why C is incorrect: Expanding the Message property and doing a string match
    is extremely inefficient and would match event IDs within message text, not
    the actual EventID property.
  - Why D is incorrect: `Get-EventLog -Source` filters by source name (a string),
    not by Event ID (a number). 4625 is not a valid source name parameter value.

---

## Question 4

An administrator runs the following command.

```powershell
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 5 Name, Id, WorkingSet
```

What does this command return?

A) The five oldest running processes sorted by start time.

B) The five processes using the most memory, showing their name, process ID,
   and working set size.

C) The five processes with the highest CPU usage, showing name, ID, and CPU
   time.

D) The five largest executable files on the system, sorted by file size.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `WorkingSet` is the process's memory usage (physical
    memory), not the process age. Sorting by age would require the `StartTime`
    property.
  - Why C is incorrect: CPU usage would require sorting by the `CPU` property.
    `WorkingSet` is memory, not CPU.
  - Why D is incorrect: `Get-Process` returns running process objects, not file
    system objects. `WorkingSet` is an in-memory size property, not a file
    size on disk.

---

## Question 5

An administrator needs to run a script block on 20 servers simultaneously and
collect the results. Which approach is correct?

A) Use `Enter-PSSession` with each server name in a loop to connect and run
   the script one server at a time.

B) Use `Invoke-Command -ComputerName` with all 20 server names, which fans
   out the script block to all servers in parallel.

C) Use `New-PSSession` to create 20 sessions, then use `foreach` to run
   `Invoke-Command -Session` on each session sequentially.

D) Use `Connect-PSSession` with a list of all 20 server names, which runs
   the script block on each server.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Enter-PSSession` is interactive and one-to-one. Using
    it in a loop is sequential, not parallel. For bulk operations, `Invoke-Command`
    with multiple computer names is the correct approach.
  - Why C is incorrect: Running `Invoke-Command -Session` in a `foreach` loop
    sends commands sequentially, one session at a time. `Invoke-Command -ComputerName`
    with all names runs in parallel.
  - Why D is incorrect: `Connect-PSSession` reconnects to a disconnected
    session — it does not accept multiple computer names and does not run script
    blocks.

---

## Question 6

An administrator exports a service health report to CSV.

```powershell
$report | Export-Csv -Path "C:\Reports\Health.csv"
```

When the CSV is opened in Excel, the first row reads `#TYPE System.Management.Automation.PSCustomObject`. Which parameter corrects this?

A) `-SkipHeader`

B) `-NoTypeInformation`

C) `-ExcludeProperty TypeName`

D) `-Force`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `-SkipHeader` is not a valid parameter for
    `Export-Csv`. There is no parameter by this name.
  - Why C is incorrect: `-ExcludeProperty` is a parameter of `Select-Object`,
    not `Export-Csv`. It does not affect the type information header.
  - Why D is incorrect: `-Force` overwrites an existing file without prompting.
    It does not remove the type information header from the CSV.

---

## Question 7

Which PowerShell execution policy allows locally written scripts to run
without requiring a digital signature, while requiring that scripts downloaded
from the internet are signed?

A) Restricted — blocks all script execution

B) AllSigned — requires all scripts to be digitally signed

C) RemoteSigned — allows local scripts; requires signatures on downloaded
   scripts

D) Unrestricted — runs all scripts without any signature requirement

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: Restricted blocks all script execution — even local
    scripts. This is the most restrictive policy.
  - Why B is incorrect: AllSigned requires all scripts — both local and remote
    — to have a valid digital signature. Local scripts without a signature
    cannot run.
  - Why D is incorrect: Unrestricted runs all scripts and only prompts for
    confirmation for downloaded scripts — it does not require signatures. It is
    less restrictive than RemoteSigned and not recommended for servers.

---

## Question 8

An administrator needs to query Event ID 4740 (account lockout) from the
Security log for the past 6 hours. Which approach uses the most efficient
filtering method?

A)

```powershell
Get-EventLog -LogName Security | Where-Object {$_.InstanceId -eq 4740 -and $_.TimeGenerated -gt (Get-Date).AddHours(-6)}
```

B)

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4740; StartTime=(Get-Date).AddHours(-6)}
```

C)

```powershell
Get-EventLog -LogName Security -Newest 10000 | Where-Object {$_.EventID -eq 4740}
```

D)

```powershell
Get-WinEvent -LogName Security | Where-Object {$_.Id -eq 4740}
```

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: This retrieves all Security log events into memory and
    then filters in PowerShell. On an active domain controller, the Security
    log can contain millions of events. This approach is very inefficient.
  - Why C is incorrect: Retrieving 10,000 events into memory and filtering is
    inefficient compared to server-side filtering with `-FilterHashtable`.
  - Why D is incorrect: `Get-WinEvent -LogName Security` retrieves all events
    without server-side filtering, then filters in memory with `Where-Object`.
    This is the same inefficiency as options A and C.

---

## Question 9

An administrator creates the following function.

```powershell
function Get-DiskReport {
    param(
        [Parameter(Mandatory=$true)]
        [string]$ComputerName
    )

    $disk = Get-WmiObject Win32_LogicalDisk -ComputerName $ComputerName -Filter "DeviceID='C:'"

    [PSCustomObject]@{
        Computer = $ComputerName
        FreeGB   = [math]::Round($disk.FreeSpace / 1GB, 1)
        TotalGB  = [math]::Round($disk.Size / 1GB, 1)
    }
}
```

A colleague calls the function without the `-ComputerName` parameter.

```powershell
Get-DiskReport
```

What happens?

A) The function runs using "localhost" as the default computer name because
   `[string]` parameters default to empty strings.

B) PowerShell prompts the administrator to enter a value for ComputerName
   because it is marked `Mandatory=$true`.

C) The function throws a red terminating error because strings cannot be null.

D) The function silently skips execution and returns no output.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `[string]$ComputerName` with no default value defaults
    to `$null`, not "localhost." Since `Mandatory=$true` is set, PowerShell
    intercepts this before the function body runs.
  - Why C is incorrect: PowerShell does not throw an error for a missing
    mandatory parameter — it prompts interactively. A terminating error would
    only occur if an exception is raised inside the function body.
  - Why D is incorrect: PowerShell never silently skips execution of a function.
    The mandatory parameter mechanism actively prompts the user when the
    parameter is missing.

---

## Question 10

An administrator wants to create a scheduled task that runs a PowerShell
script (`C:\Scripts\Cleanup.ps1`) every day at 2:00 AM using the SYSTEM
account. Which set of PowerShell commands correctly creates this task?

A)

```powershell
Register-ScheduledTask -Name "Cleanup" -Execute "C:\Scripts\Cleanup.ps1" -At "02:00AM"
```

B)

```powershell
$action  = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File C:\Scripts\Cleanup.ps1"
$trigger = New-ScheduledTaskTrigger -Daily -At "02:00AM"
Register-ScheduledTask -TaskName "Cleanup" -Action $action -Trigger $trigger -User "SYSTEM" -RunLevel Highest
```

C)

```powershell
Set-ScheduledTask -Name "Cleanup" -Execute "PowerShell.exe" -Script "C:\Scripts\Cleanup.ps1" -Schedule Daily -Time "02:00"
```

D)

```powershell
New-ScheduledTaskAction -Execute "C:\Scripts\Cleanup.ps1" -Trigger "Daily" -At "2AM" -User "SYSTEM"
```

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Register-ScheduledTask` does not have `-Execute` or
    `-At` parameters directly. The action and trigger must be created as
    separate objects using `New-ScheduledTaskAction` and
    `New-ScheduledTaskTrigger`.
  - Why C is incorrect: `Set-ScheduledTask` modifies existing tasks and does
    not accept `-Execute`, `-Script`, or `-Schedule` parameters. Task creation
    requires `Register-ScheduledTask`.
  - Why D is incorrect: `New-ScheduledTaskAction` creates a task action object
    — it does not register a task. Additionally, the parameters `-Trigger`,
    `-At`, and `-User` do not belong to `New-ScheduledTaskAction`.

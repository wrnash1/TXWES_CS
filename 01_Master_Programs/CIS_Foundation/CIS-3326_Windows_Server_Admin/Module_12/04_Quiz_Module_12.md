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

---

### Question 11 (5 points)

An administrator needs to find all processes on a server whose name starts with
`"sql"` and display their process ID, name, and CPU time. Which command is
correct?

- A) `Get-Process | Where-Object {$_.Name -like "sql*"} | Select-Object Id, Name, CPU`
- B) `Get-Process -Name "sql" | Select-Object Id, Name, CPU`
- C) `Get-Process | Select-Object Id, Name, CPU | Where-Object {$_.Name -eq "sql*"}`
- D) `Get-Process | Filter {$_.Name -starts "sql"} | Select-Object Id, Name, CPU`

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. `Where-Object` with `-like "sql*"` uses a wildcard pattern to match any process whose name begins with "sql". `Select-Object` then picks the three required properties.
  - **B** — `Get-Process -Name "sql"` looks for a process named exactly "sql" (no wildcard). It would not match `sqlservr`, `sqlwriter`, etc. To use a wildcard with the `-Name` parameter: `Get-Process -Name "sql*"`.
  - **C** — `Select-Object` is placed before `Where-Object` here. While this still works, the `-eq "sql*"` operator does exact string comparison; it does not treat `*` as a wildcard. `-like` is required for wildcard pattern matching.
  - **D** — `Filter` is not a valid pipeline cmdlet. `-starts` is not a valid `-like` operator. The correct wildcard comparison operator is `-like`.

---

### Question 12 (5 points)

An administrator uses `Invoke-Command` to query disk space on 10 servers and
receives output objects. Each object has a `PSComputerName` property added
automatically. What is the purpose of the `PSComputerName` property?

- A) It specifies which computer should run the script block next time
- B) It identifies which remote computer the result object came from, since all results are returned to the local session
- C) It is the hostname of the local machine running the `Invoke-Command` call
- D) It is a required parameter for filtering results before export

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `PSComputerName` is a read-only property added to result objects. It has no role in directing future script execution.
  - **B** — Correct. When `Invoke-Command` fans out to multiple computers, all result objects are returned to the local session. PowerShell automatically adds a `PSComputerName` property to each object so the administrator can identify which remote computer produced each row of output.
  - **C** — `PSComputerName` identifies the remote source computer, not the local machine running the command. The local machine's name is available via `$env:COMPUTERNAME`.
  - **D** — `PSComputerName` is not a required filter parameter. It is an informational property added automatically and is useful but not required for export.

---

### Question 13 (5 points)

An administrator writes a script that reads a CSV file and creates AD user
accounts. When run, the script throws a terminating error on the third row
because the UPN already exists. The first two accounts were created successfully.
Which change ensures all rows are attempted even if some fail?

- A) Add `$ErrorActionPreference = "Ignore"` at the top of the script
- B) Wrap the `New-ADUser` call in a `try` block with `-ErrorAction Stop` and a `catch` block that logs the error and continues
- C) Add `-Confirm:$false` to the `New-ADUser` call to suppress the error dialog
- D) Use `Start-Job` to run each row as a background job so errors in one job do not affect others

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `$ErrorActionPreference = "Ignore"` silently discards all errors, including ones you need to know about. No logging occurs and the administrator has no record of which accounts failed.
  - **B** — Correct. Wrapping `New-ADUser` in `try { ... -ErrorAction Stop } catch { ... }` converts non-terminating errors to terminating ones that are intercepted by `catch`. The `catch` block logs the failure and the loop continues to the next row.
  - **C** — `-Confirm:$false` suppresses confirmation prompts, not errors. A duplicate UPN error is not a confirmation prompt; it is an exception thrown by AD.
  - **D** — `Start-Job` would work but adds significant complexity — jobs run asynchronously, results must be collected with `Receive-Job`, and job management overhead is unnecessary for a sequential CSV import that simply needs per-row error handling.

---

### Question 14 (5 points)

An administrator runs `Set-ExecutionPolicy Bypass -Scope Process`. What is the
scope of this change?

- A) The change applies to all users on the machine permanently
- B) The change applies only to the current PowerShell process and is lost when the session closes
- C) The change applies to the current user's profile and persists across sessions
- D) The change applies to the LocalMachine scope and overrides all other scopes

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `-Scope LocalMachine` applies to all users permanently. `-Scope Process` is restricted to the current session.
  - **B** — Correct. `-Scope Process` applies the execution policy only to the current running PowerShell process. When the process exits, the setting is gone. It does not modify the registry or any persistent configuration.
  - **C** — `-Scope CurrentUser` applies to the current user and persists across sessions by writing to the user's registry hive. `-Scope Process` is temporary.
  - **D** — `-Scope LocalMachine` sets the policy for all users on the machine. `-Scope Process` is the most restricted and temporary scope; it does not affect or override `LocalMachine` or `CurrentUser` policy in the registry.

---

### Question 15 (5 points)

An administrator wants to write a PowerShell function that accepts pipeline
input. The function should accept a list of server names piped from another
cmdlet. Which parameter declaration enables pipeline input by value?

- A) `[Parameter(Mandatory=$true)] [string]$ComputerName`
- B) `[Parameter(ValueFromPipeline=$true)] [string]$ComputerName`
- C) `[Parameter(ValueFromPipelineByPropertyName=$true)] [string]$ComputerName`
- D) `[Parameter(Pipeline=$true)] [string]$ComputerName`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Mandatory=$true` requires the parameter to be provided but does not enable pipeline binding. The parameter would need to be passed explicitly.
  - **B** — Correct. `ValueFromPipeline=$true` allows the parameter to accept input from the pipeline by value — meaning a string piped to the function populates `$ComputerName` directly.
  - **C** — `ValueFromPipelineByPropertyName=$true` binds pipeline input by matching a property name on the incoming object to the parameter name. This requires the piped object to have a property named `ComputerName`, not raw string values.
  - **D** — `Pipeline=$true` is not a valid `Parameter` attribute argument. The correct attribute is `ValueFromPipeline`.

---

### Question 16 (5 points)

An administrator exports a list of running services to a CSV using:

```powershell
Get-Service | Where-Object {$_.Status -eq "Running"} |
    Select-Object Name, DisplayName, Status |
    Export-Csv "C:\Services.csv" -NoTypeInformation
```

When the CSV is later imported with `Import-Csv`, what type is the `Status`
property of each imported object?

- A) `[System.ServiceProcess.ServiceControllerStatus]` — the original enum type
- B) `[string]` — CSV stores all values as text; Import-Csv creates string properties
- C) `[int]` — CSV stores numeric enum values
- D) `[bool]` — Status is either Running (true) or not Running (false)

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — CSV is a text format. When exported, the enum value is converted to its string representation (`"Running"`). When imported, `Import-Csv` creates `PSCustomObject` objects with all properties as strings.
  - **B** — Correct. `Export-Csv` serializes all property values as strings. `Import-Csv` reads them back as strings. The original .NET type information is not preserved. This means comparisons like `-eq "Running"` work, but `-eq [System.ServiceProcess.ServiceControllerStatus]::Running` would fail.
  - **C** — Enum values are exported as their string names (e.g., `"Running"`), not as integers. The integer representation is not written to the CSV.
  - **D** — `Status` is a multi-value enum (Stopped, Running, Paused, etc.), not a boolean.

---

### Question 17 (5 points)

An administrator needs to monitor a server's C: drive and send an email alert
when free space drops below 10 GB. They plan to use a scheduled task running a
PowerShell script every hour. Which script logic correctly checks the condition?

- A) `if ((Get-PSDrive C).Free -lt 10) { Send-MailMessage ... }`
- B) `if ((Get-Volume -DriveLetter C).SizeRemaining -lt 10GB) { Send-MailMessage ... }`
- C) `if ((Get-WmiObject Win32_LogicalDisk -Filter "DeviceID='C:'").FreeSpace -lt "10GB") { Send-MailMessage ... }`
- D) `if ((Get-Disk -Number 0).FreeSpace -lt 10GB) { Send-MailMessage ... }`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `(Get-PSDrive C).Free` returns free space in bytes. Comparing bytes to the integer `10` would be comparing bytes to a value of 10 bytes, not 10 GB. The comparison would almost never trigger correctly.
  - **B** — Correct. `Get-Volume -DriveLetter C` returns a volume object with `SizeRemaining` in bytes. Comparing to `10GB` (which PowerShell expands to 10,737,418,240 bytes) correctly identifies when free space is below 10 gigabytes.
  - **C** — `FreeSpace` from WMI is in bytes, which is correct for the comparison, but `"10GB"` is a string. Comparing a numeric property to a string would cause a type error or incorrect comparison. The literal should be `10GB` (no quotes).
  - **D** — `Get-Disk` returns physical disk objects, not volume objects. Physical disk objects do not have a `FreeSpace` property — that belongs to logical volume/partition objects.

---

### Question 18 (5 points)

An administrator runs `Get-Service -ComputerName DC2` and receives an error:
"Cannot open Service Control Manager on computer 'DC2'. This operation might
require other privileges." What is the most likely cause?

- A) The WinRM service is not running on DC2
- B) The administrator is not running PowerShell with elevated privileges or does not have administrative rights on DC2
- C) `Get-Service` does not support the `-ComputerName` parameter on Windows Server 2022
- D) DC2 is not reachable over the network

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Get-Service -ComputerName` uses the Windows Service Control Manager (SCM) API over RPC/DCOM, not WinRM. A WinRM failure would produce a different error.
  - **B** — Correct. The Service Control Manager error indicates the current user does not have permission to connect to the remote SCM on DC2. Running PowerShell as a domain administrator or providing credentials resolves this.
  - **C** — `Get-Service -ComputerName` is a supported parameter on all Windows Server versions. It uses legacy RPC/DCOM, not WinRM.
  - **D** — A network connectivity failure would produce a different error such as "The RPC server is unavailable" or a network timeout, not a "Cannot open Service Control Manager" message.

---

### Question 19 (5 points)

An administrator writes a script that generates a weekly server health report and
saves it as a CSV. They want to append new data to the existing CSV each week
without overwriting previous weeks' data. Which `Export-Csv` parameter enables
appending?

- A) `-Update`
- B) `-Append`
- C) `-Force`
- D) `-NoClobber`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `-Update` is not a valid `Export-Csv` parameter.
  - **B** — Correct. `-Append` adds new rows to an existing CSV file without overwriting existing content. The new rows are added after the last row. Note that `-NoTypeInformation` should also be specified to avoid adding a type header line to the appended rows.
  - **C** — `-Force` overwrites an existing file that has the read-only attribute set. It does not append to an existing file.
  - **D** — `-NoClobber` prevents `Export-Csv` from overwriting an existing file — the command fails instead. This is the opposite of append behavior.

---

### Question 20 (5 points)

An administrator creates a `[PSCustomObject]` inside a function and needs to
ensure the output displays cleanly in both the console and when exported to CSV.
Which approach produces the best structured output?

- A) Use `Write-Host` to output each property on its own line with a label
- B) Return a `[PSCustomObject]@{ Property1 = value1; Property2 = value2 }` from the function
- C) Use `Out-String` to convert the result to a formatted string before returning
- D) Use `Format-Table` to pre-format the output before returning from the function

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Write-Host` sends output directly to the console and cannot be captured in a variable, piped to `Export-Csv`, or processed further in the pipeline. It produces unstructured text, not objects.
  - **B** — Correct. `[PSCustomObject]@{}` creates a .NET object with named properties. This object passes cleanly through the PowerShell pipeline, can be sorted and filtered with `Where-Object`/`Sort-Object`, and serializes correctly with `Export-Csv -NoTypeInformation`.
  - **C** — `Out-String` converts objects to a formatted string. Once converted, the output is a single string and loses all property structure. It cannot be piped to `Export-Csv` or filtered by property.
  - **D** — `Format-Table` creates formatting objects for display purposes. Piping `Format-Table` output to `Export-Csv` produces malformed CSV with formatting metadata, not the original property values.

# Video Script: Module 12 — PowerShell for Server Administration (Part 1)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 13–15 minutes

**Part 1 focus:** Concepts — PowerShell pipeline, objects vs. text, cmdlet
syntax, common verbs, filtering and formatting, working with services,
processes, and event logs.

---

## Opening

Welcome to Module 12. This entire module is about PowerShell — the scripting
and automation backbone of Windows Server. By now you have been using
PowerShell for labs since Module 2. This module steps back and teaches you how
to use it systematically, understand the object model, write reusable scripts,
and manage servers remotely.

PowerShell is not optional for Windows Server administrators. It is how modern
server management works. Let's build a solid foundation.

---

## Section 1 — PowerShell Architecture: Objects, Not Text

The most important thing to understand about PowerShell is that it works with
.NET objects, not plain text. This is what separates PowerShell from traditional
Unix shells like bash.

When `Get-Process` returns a list of processes, each process is a .NET
`System.Diagnostics.Process` object. It has properties like `Name`, `Id`,
`CPU`, `WorkingSet`, and methods like `Kill()`. When you pipe the output to the
next command, you are passing those objects — not text characters.

[SHOW SCREEN: Comparison of text-based bash pipeline vs. PowerShell object pipeline]
[Alt-text: Two code windows side by side. Left (bash): ps | grep chrome | awk '{print $1}'. Right (PowerShell): Get-Process | Where-Object {$_.Name -eq "chrome"} | Select-Object Id, CPU.]

This is why PowerShell is so powerful for administration. You don't parse text
— you access properties directly.

---

## Section 2 — Cmdlet Anatomy

Every PowerShell cmdlet follows a Verb-Noun naming convention.

The verb describes the action: Get, Set, New, Remove, Enable, Disable, Start,
Stop, Invoke, Add, Export, Import.

The noun describes the object: Service, Process, EventLog, ADUser, VM, Item,
Content, NetFirewallRule.

```powershell
# Pattern: Verb-Noun [-Parameter Value]
Get-Service         # Get service objects
Set-Service         # Modify a service
Start-Service       # Start a service
Stop-Service        # Stop a service
New-Service         # Create a service
Remove-Item         # Delete a file or folder
Get-EventLog        # Get event log entries
Get-Process         # Get running processes
```

Parameters use `-ParameterName Value` syntax. Many parameters have aliases and
positional values. Use `Get-Help` to learn any cmdlet.

```powershell
Get-Help Get-Service -Full
Get-Help Get-Service -Examples
```

---

## Section 3 — The Pipeline

The pipeline `|` passes objects from one cmdlet to the next. This is how you
chain operations.

```powershell
# Get all services, filter to running ones, sort by name
Get-Service | Where-Object {$_.Status -eq "Running"} | Sort-Object Name

# Get processes using more than 100 MB of memory
Get-Process | Where-Object {$_.WorkingSet -gt 100MB} | Sort-Object WorkingSet -Descending

# Get the top 5 CPU-consuming processes
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Name, Id, CPU
```

`Where-Object` filters the pipeline using a condition. `$_` represents the
current object in the pipeline. `Select-Object` selects which properties to
display or pass forward.

---

## Section 4 — Formatting Output

By default, PowerShell formats output in a table or list depending on the
number of properties. You can override this.

```powershell
Get-Service | Format-Table Name, Status, StartType -AutoSize

Get-Service | Format-List Name, Status, DisplayName, StartType

Get-Process | Format-Wide Name -Column 4
```

For pipeline operations, use `Select-Object` to choose properties instead of
`Format-Table`. Format commands should be the last step in a pipeline because
they convert objects to formatted text — after formatting, the objects are gone.

---

## Section 5 — Working with Services

```powershell
# Get all services
Get-Service

# Get a specific service
Get-Service -Name "Spooler"

# Get services that are stopped
Get-Service | Where-Object {$_.Status -eq "Stopped"}

# Get services by display name pattern
Get-Service | Where-Object {$_.DisplayName -like "*Windows*"}

# Start, stop, restart a service
Start-Service   -Name "Spooler"
Stop-Service    -Name "Spooler"
Restart-Service -Name "Spooler"

# Change the startup type
Set-Service -Name "Spooler" -StartupType Automatic
Set-Service -Name "Spooler" -StartupType Disabled
Set-Service -Name "Spooler" -StartupType Manual
```

[SHOW SCREEN: Get-Service output showing multiple services with Status]
[Alt-text: PowerShell table showing columns Status, Name, DisplayName for several services including Spooler.]

On Windows Server, the Print Spooler service (Spooler) is a common example
because many systems should have it stopped and disabled if no printing is
needed — it is a frequent attack vector.

---

## Section 6 — Working with Processes

```powershell
# Get all running processes
Get-Process

# Get a specific process by name
Get-Process -Name "notepad"

# Get processes sorted by memory usage
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10 Name, Id, WorkingSet

# Stop a process by name (graceful)
Stop-Process -Name "notepad" -Confirm

# Stop a process by ID (forced)
Stop-Process -Id 1234 -Force

# Start a process
Start-Process -FilePath "notepad.exe"
Start-Process -FilePath "powershell.exe" -Verb RunAs    # run as admin
```

---

## Section 7 — Working with Event Logs

Event logs are how Windows Server records everything — service starts, errors,
security events, application crashes. Knowing how to query them with PowerShell
is essential.

Two cmdlets exist for event log work, and they behave differently.

`Get-EventLog` works with classic Windows event logs (Application, System,
Security). It is older but fast for simple queries.

`Get-WinEvent` works with both classic logs and the newer Windows Event
Tracing logs (ETW). It is the modern approach and handles more log types.

```powershell
# Get the 20 most recent System log events
Get-EventLog -LogName System -Newest 20

# Get all Error events in the Application log
Get-EventLog -LogName Application -EntryType Error -Newest 50

# Get all Error and Warning events in the last 24 hours
$since = (Get-Date).AddHours(-24)
Get-EventLog -LogName System -EntryType Error,Warning -After $since

# Get events by source
Get-EventLog -LogName System -Source "Service Control Manager" -Newest 10
```

[SHOW SCREEN: Get-EventLog output showing System log entries]
[Alt-text: PowerShell table showing Index, Time, EntryType, Source, InstanceID, and Message columns for recent System log entries.]

```powershell
# Get-WinEvent approach (modern)
Get-WinEvent -LogName "Application" -MaxEvents 20

# Filter with FilterHashtable (efficient)
Get-WinEvent -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4625          # Failed logon events
    StartTime = (Get-Date).AddDays(-1)
}
```

The `-FilterHashtable` approach is more efficient than piping to
`Where-Object` because it filters at the event log level rather than in
PowerShell memory.

---

## Section 8 — Variables, Arrays, and Loops

```powershell
# Variables
$serverName = "DC1"
$port = 443
$isEnabled = $true

# Arrays
$servers = @("DC1", "FS01", "APP01", "SQL01")
$ports = @(80, 443, 3389, 5985)

# foreach loop
foreach ($server in $servers) {
    Write-Host "Checking: $server" -ForegroundColor Cyan
}

# for loop
for ($i = 0; $i -lt $servers.Count; $i++) {
    Write-Host "Server $i : $($servers[$i])"
}

# while loop
$count = 0
while ($count -lt 5) {
    Write-Host "Count: $count"
    $count++
}

# ForEach-Object in pipeline (equivalent to foreach for pipeline)
$servers | ForEach-Object {
    Test-Connection -ComputerName $_ -Count 1 -Quiet
}
```

---

## Section 9 — Conditional Logic

```powershell
# if / elseif / else
$service = Get-Service -Name "Spooler"

if ($service.Status -eq "Running") {
    Write-Host "Spooler is running" -ForegroundColor Green
} elseif ($service.Status -eq "Stopped") {
    Write-Host "Spooler is stopped — starting it" -ForegroundColor Yellow
    Start-Service -Name "Spooler"
} else {
    Write-Host "Spooler is in an unexpected state: $($service.Status)" -ForegroundColor Red
}

# switch statement
switch ($service.StartType) {
    "Automatic" { Write-Host "Auto start" }
    "Manual"    { Write-Host "Manual start" }
    "Disabled"  { Write-Host "Disabled" }
    default     { Write-Host "Unknown start type" }
}
```

---

## Module Summary

PowerShell works with objects, not text. Cmdlets follow Verb-Noun naming.
The pipeline passes objects between cmdlets. `Where-Object` filters, `Select-Object`
chooses properties, `Sort-Object` sorts.

`Get-Service` / `Set-Service` / `Start-Service` / `Stop-Service` manage Windows
services. `Get-Process` / `Stop-Process` manage running processes.

`Get-EventLog` queries classic event logs. `Get-WinEvent` with
`-FilterHashtable` is the modern and efficient approach.

Variables, arrays, foreach loops, and if/else conditions are the building
blocks of any PowerShell script.

In Part 2 we will build complete scripts, use functions, write output to files,
and manage servers remotely. See you there.

---

Module 12 Part 1 — End of Script

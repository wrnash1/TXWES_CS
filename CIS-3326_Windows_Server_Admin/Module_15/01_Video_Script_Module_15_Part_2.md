# Video Script: Module 15 — Monitoring and Performance Tuning (Part 2)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 11–13 minutes

**Part 2 focus:** PowerShell and GUI demos — `Get-Counter`, `Get-Process`,
creating Data Collector Sets, filtering Event Viewer, PowerShell-based
performance monitoring, identifying bottlenecks from counter data. Exam tips
and lab preview.

---

## Opening

Welcome back to Module 15. In Part 1 we covered the monitoring tools and
performance counters conceptually. Now let's run them and interpret real data.

---

## Demo 1 — Get-Counter: Real-Time Counter Queries

The `Get-Counter` cmdlet reads performance counter values from the live
performance subsystem. This is the PowerShell equivalent of Performance Monitor.

[SHOW SCREEN: PowerShell window open as Administrator]
[Alt-text: Blue PowerShell console window with PS C:\> prompt.]

```powershell
# Get current CPU utilization
Get-Counter "\Processor(_Total)\% Processor Time"
```

[SHOW SCREEN: Get-Counter output]
[Alt-text: PowerShell output showing CounterSamples with Path and CookedValue showing a percentage number.]

```powershell
# Get CPU, memory, and disk counters simultaneously
Get-Counter @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length"
)
```

```powershell
# Sample counters every 5 seconds for 12 samples (1 minute)
Get-Counter "\Processor(_Total)\% Processor Time" `
    -SampleInterval 5 `
    -MaxSamples 12
```

```powershell
# Get all instances of a counter (per-core CPU)
Get-Counter "\Processor(*)\% Processor Time" |
    Select-Object -ExpandProperty CounterSamples |
    Select-Object InstanceName, CookedValue |
    Sort-Object CookedValue -Descending
```

[SHOW SCREEN: Per-core CPU counter output]
[Alt-text: PowerShell table showing InstanceName (0, 1, 2, 3, _total) and CookedValue percentages for each processor core.]

---

## Demo 2 — Collecting Counter Data to a File

```powershell
# Collect counters to a CSV file for 10 samples
$counters = @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
    "\System\Processor Queue Length"
)

Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path "C:\PerfData\Baseline_$(Get-Date -Format 'yyyyMMdd_HHmm').csv" `
    -FileFormat CSV
```

This collects 6 samples at 10-second intervals and saves to a timestamped CSV.

You can also use the BLG (binary log) format for use with Performance Monitor.

```powershell
Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path "C:\PerfData\Baseline.blg" -FileFormat BLG
```

Open the BLG file in Performance Monitor: open perfmon.exe, click the green
play button, then Change Graph Type to Report and open the saved log file.

---

## Demo 3 — Identifying Bottlenecks from Counter Data

Let's walk through a bottleneck identification scenario.

```powershell
# Collect a 60-second snapshot for analysis
$snapshot = Get-Counter @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
    "\System\Processor Queue Length"
) -SampleInterval 5 -MaxSamples 12

# Extract and display results
$snapshot.CounterSamples | Select-Object Path, CookedValue |
    Format-Table -AutoSize
```

Interpreting the results:

- If `% Processor Time` consistently above 85% AND `Processor Queue Length`
  above 2 per core: CPU bottleneck. Add CPU cores or move workloads.

- If `Available MBytes` below 100 MB OR `Pages/sec` consistently above 5:
  Memory bottleneck. Add RAM.

- If `Avg. Disk Queue Length` above 2: Storage bottleneck. Move to faster
  storage (SSD) or distribute I/O.

- If counters are normal but users report slowness: check the Network Interface
  counters for saturation.

---

## Demo 4 — Event Viewer: Filtering and Custom Views

Open Event Viewer from the command line.

```powershell
Start-Process eventvwr.msc
```

In the Event Viewer GUI, let's filter the System log for Error events in the
last 4 hours.

[SHOW SCREEN: Event Viewer System log with Filter Current Log dialog open]
[Alt-text: Filter Current Log dialog showing Logged dropdown set to Last 4 hours, Event level checkboxes with Error checked, all other sources and keywords empty.]

Click Action → Filter Current Log. Set Logged to Last 4 hours. Check Error
under Event level. Click OK. The log now shows only errors from the past 4
hours without permanently changing the log.

For PowerShell-based event filtering.

```powershell
# Filter System log errors from the last 4 hours
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    Level     = 2          # 2 = Error
    StartTime = (Get-Date).AddHours(-4)
} | Select-Object TimeCreated, Id, LevelDisplayName, Message -First 20
```

```powershell
# Find Service Control Manager events (service starts/stops)
Get-WinEvent -FilterHashtable @{
    LogName      = 'System'
    ProviderName = 'Service Control Manager'
    StartTime    = (Get-Date).AddDays(-1)
} | Select-Object TimeCreated, Id, Message -First 15
```

---

## Demo 5 — Creating a Data Collector Set with PowerShell

For automated, scheduled baseline collection, use the Performance Data Helper
(PLA) COM object through PowerShell.

```powershell
# Create a Data Collector Set for 24-hour baseline collection
$dcsName = "TXWES_Baseline_$(Get-Date -Format 'yyyyMMdd')"

$dataCollectorSet = New-Object -COM Pla.DataCollectorSet
$dataCollectorSet.DisplayName = $dcsName
$dataCollectorSet.Duration = 86400   # 24 hours in seconds
$dataCollectorSet.SubdirectoryFormat = 1

# Add a Performance Counter Data Collector
$perfCollector = $dataCollectorSet.DataCollectors.CreateDataCollector(0)
$perfCollector.Name = "PerfCounters"
$perfCollector.SampleInterval = 60   # every 60 seconds
$perfCollector.FileFormat = 3        # CSV

$perfCollector.PerformanceCounters.Add("\Processor(_Total)\% Processor Time")
$perfCollector.PerformanceCounters.Add("\Memory\Available MBytes")
$perfCollector.PerformanceCounters.Add("\PhysicalDisk(_Total)\Avg. Disk Queue Length")
$perfCollector.PerformanceCounters.Add("\System\Processor Queue Length")

$dataCollectorSet.DataCollectors.Add($perfCollector)
$dataCollectorSet.Commit($dcsName, $null, 3)  # 3 = create or modify
```

Alternatively, use the GUI as shown in Part 1 — right-click User Defined under
Data Collector Sets and select New, Data Collector Set.

---

## Demo 6 — Performance Monitoring from PowerShell: Health Check Script

```powershell
# ServerHealthSnapshot.ps1
# Collects a performance snapshot and writes a simple status report

param(
    [string]$ComputerName = "localhost",
    [int]$Samples = 3,
    [int]$Interval = 10
)

function Get-AvgCounter {
    param($CounterPath, $N, $I)
    $data = Get-Counter -Counter $CounterPath `
        -ComputerName $ComputerName `
        -SampleInterval $I `
        -MaxSamples $N `
        -ErrorAction SilentlyContinue

    if ($data) {
        [math]::Round(($data.CounterSamples | Measure-Object CookedValue -Average).Average, 1)
    } else { -1 }
}

$cpuPct   = Get-AvgCounter "\Processor(_Total)\% Processor Time" $Samples $Interval
$memMB    = Get-AvgCounter "\Memory\Available MBytes" $Samples $Interval
$diskQ    = Get-AvgCounter "\PhysicalDisk(_Total)\Avg. Disk Queue Length" $Samples $Interval
$procQ    = Get-AvgCounter "\System\Processor Queue Length" $Samples $Interval

$status = if ($cpuPct -gt 85 -or $memMB -lt 200 -or $diskQ -gt 2) {"WARNING"} else {"OK"}

[PSCustomObject]@{
    Computer    = $ComputerName
    CPU_Pct     = $cpuPct
    MemFree_MB  = $memMB
    DiskQueue   = $diskQ
    ProcQueue   = $procQ
    Status      = $status
    Timestamp   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
}
```

[SHOW SCREEN: Script output]
[Alt-text: PowerShell output showing a PSCustomObject table with Computer, CPU_Pct, MemFree_MB, DiskQueue, ProcQueue, Status:OK, and Timestamp columns.]

---

## Exam Tips

**Exam Tip 1** — Tool selection: Resource Monitor is the fastest tool when you
need to identify which specific process is causing a performance issue. Use
Performance Monitor when you need to trend counters over time or set up alerts.

**Exam Tip 2** — Data Collector Sets run as a background service — no active
user session required. A real-time PerfMon graph stops when you disconnect.
For baseline collection, always use a DCS.

**Exam Tip 3** — Counter thresholds to memorize: Processor Queue Length above
2 per core (CPU bottleneck), Available MBytes below 100 MB (memory pressure),
Pages/sec above 5 sustained (excessive paging), Avg. Disk Queue Length above 2
per spindle (disk bottleneck).

**Exam Tip 4** — `Get-WinEvent -FilterHashtable` is more efficient than piping
to `Where-Object` because filtering occurs at the event log service level, not
in PowerShell memory.

**Exam Tip 5** — Filter Current Log is temporary — it disappears when you close
Event Viewer. Custom Views are saved permanently and appear in the navigation
tree for reuse.

---

## Lab Preview

In Lab 15, you will use `Get-Counter` to collect performance counter data,
create a baseline CSV, query Event Viewer with both the GUI filter and
`Get-WinEvent -FilterHashtable`, write a PowerShell health check script with
threshold comparisons, and export the results to a report file. Complete all
parts and submit the required screenshots.

See you in the quiz.

---

Module 15 Part 2 — End of Script

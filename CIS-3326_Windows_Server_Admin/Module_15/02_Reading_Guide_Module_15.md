# Reading Guide: Module 15 — Monitoring and Performance Tuning

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Overview

Module 15 covers the monitoring and performance toolset built into Windows Server:
Task Manager, Resource Monitor, Performance Monitor, and Event Viewer. You will
learn which tool to use in each situation, how to read performance counters,
how to establish baselines, how to identify bottlenecks, and how to manage event
logs. These skills are tested on the Microsoft Windows Server Administration exam.

---

## 1. Monitoring Tool Comparison

| Tool | Executable | Primary Use | Scope | Persistence |
|---|---|---|---|---|
| Task Manager | taskmgr.exe | Quick resource overview | System-level totals | Real-time only |
| Resource Monitor | resmon.exe | Per-process resource detail | Per-process breakdown | Real-time only |
| Performance Monitor | perfmon.exe | Counter trending over time | Configurable counters | Saved to files |
| Event Viewer | eventvwr.msc | Log review and analysis | System, App, Security logs | Permanent (log files) |

**Tool selection rule:** Start with Task Manager. If aggregates show a problem,
switch to Resource Monitor to identify the specific process. For sustained
collection and trending, use Performance Monitor with a Data Collector Set. For
diagnosing past events (service failures, logon errors), use Event Viewer.

---

## 2. Task Manager — Performance Tab Reference

| Resource | Key Metrics Displayed |
|---|---|
| CPU | Overall utilization %, base speed, logical processor count, core graph |
| Memory | Total RAM, In Use, Available, Committed, Cached, Paged/Non-Paged pool |
| Disk | Active time %, read throughput MB/s, write throughput MB/s |
| Network | Adapter name, send rate, receive rate |

From the Processes tab, right-click any process to open it directly in Resource
Monitor for per-process detail.

---

## 3. Resource Monitor — Section Reference

| Section | Key Data Provided |
|---|---|
| CPU | Per-process CPU %, service host breakdown, DLLs loaded by each process |
| Memory | Per-process Commit, Working Set, Shareable, Private memory; Hard Faults/sec |
| Disk | Per-process read/write bytes/sec; file paths being read or written |
| Network | Per-process send/receive bytes/sec; remote addresses each process contacts |

**Hard Faults per second** — Hard faults occur when the OS reads a page from the
page file on disk because physical RAM is full. A sustained nonzero hard fault
rate is a strong signal that the server needs more RAM.

---

## 4. Performance Counter Anatomy

A performance counter is identified by three components.

| Component | Description | Example |
|---|---|---|
| Object | Category of the resource being measured | `Processor`, `Memory`, `PhysicalDisk` |
| Counter | The specific metric within that object | `% Processor Time`, `Available MBytes` |
| Instance | Which specific object (CPU core, disk, adapter) | `_Total`, `0`, `1`, `C:` |

Full counter path format: `\Object(Instance)\Counter`

Example: `\Processor(_Total)\% Processor Time`

---

## 5. Key Performance Counters and Thresholds

### CPU Counters

| Counter | Path | Threshold / Notes |
|---|---|---|
| CPU Utilization | `\Processor(_Total)\% Processor Time` | Sustained above 85% = CPU pressure |
| User Mode CPU | `\Processor(_Total)\% User Time` | CPU consumed by user-space applications |
| Kernel Mode CPU | `\Processor(_Total)\% Privileged Time` | CPU consumed by OS, drivers, I/O |
| Processor Queue | `\System\Processor Queue Length` | Above 2 per core = CPU bottleneck |

### Memory Counters

| Counter | Path | Threshold / Notes |
|---|---|---|
| Available RAM | `\Memory\Available MBytes` | Below 100 MB = critical memory pressure |
| Paging Rate | `\Memory\Pages/sec` | Sustained above 5 = excessive paging |
| Page Faults | `\Memory\Page Faults/sec` | Includes soft (cache) and hard (disk) faults |

### Disk Counters

| Counter | Path | Threshold / Notes |
|---|---|---|
| Queue Depth | `\PhysicalDisk(_Total)\Avg. Disk Queue Length` | Above 2 per spindle = disk bottleneck |
| Read Latency | `\PhysicalDisk(_Total)\Avg. Disk sec/Read` | Above 20 ms = concerning |
| Write Latency | `\PhysicalDisk(_Total)\Avg. Disk sec/Write` | Above 20 ms = concerning |
| Busy Time | `\PhysicalDisk(_Total)\% Disk Time` | Near 100% = disk saturation |

### Network Counters

| Counter | Path | Threshold / Notes |
|---|---|---|
| Throughput | `\Network Interface(*)\Bytes Total/sec` | Compare against link speed |
| Output Queue | `\Network Interface(*)\Output Queue Length` | Above 2 = network saturation |

---

## 6. Bottleneck Identification Logic

```text
Symptom                          → Check These Counters
─────────────────────────────────────────────────────────
Server feels slow overall        → % Processor Time AND Processor Queue Length
High CPU but not bottlenecked    → % Privileged Time (may indicate driver issue)
Server sluggish, low CPU         → Memory: Available MBytes, Pages/sec
Disk operations are slow         → Avg. Disk Queue Length, Avg. Disk sec/Read
Normal CPU/memory, still slow    → Network: Bytes Total/sec, Output Queue Length
```

**Decision table:**

| Condition | Bottleneck | Resolution |
|---|---|---|
| `% Processor Time` >85% AND `Processor Queue Length` >2/core | CPU | Add vCPUs or distribute workloads |
| `Available MBytes` <100 OR `Pages/sec` sustained >5 | Memory | Add RAM |
| `Avg. Disk Queue Length` >2 | Storage | Upgrade to SSD or distribute I/O |
| All normal, slowness reported | Network | Check `Bytes Total/sec` and `Output Queue Length` |

---

## 7. Data Collector Sets

A Data Collector Set (DCS) is a named collection of performance counters, traces,
and configuration items that runs on a schedule without requiring an active user
session.

| Feature | Description |
|---|---|
| Autonomous operation | Runs as a background Windows service; no logged-on user required |
| Scheduling | Start/stop on a schedule or duration |
| Output format | BLG (binary log) — opened in Performance Monitor; or CSV |
| Alert triggers | Can fire alerts when a counter exceeds a defined threshold |
| Templates | System templates: System Performance, System Diagnostics |

**DCS vs. real-time Performance Monitor:**

| Characteristic | Real-Time PerfMon Graph | Data Collector Set |
|---|---|---|
| Requires user session | Yes | No |
| Stops on disconnect | Yes | No |
| Saves data to file | No | Yes |
| Used for baseline capture | No | Yes |

### Creating a DCS in the GUI

1. Open `perfmon.exe`.
2. Expand Data Collector Sets in the left pane.
3. Right-click User Defined, select New, Data Collector Set.
4. Name it, select Create from a template, choose Server Performance.
5. Set the schedule and output path. Click Finish.

### Creating a DCS with PowerShell (PLA COM Object)

```powershell
$dcsName = "TXWES_Baseline_$(Get-Date -Format 'yyyyMMdd')"
$dcs = New-Object -COM Pla.DataCollectorSet
$dcs.DisplayName = $dcsName
$dcs.Duration = 86400           # 24 hours in seconds

$pc = $dcs.DataCollectors.CreateDataCollector(0)
$pc.Name = "PerfCounters"
$pc.SampleInterval = 60
$pc.FileFormat = 3              # 3 = CSV; 1 = BLG

$pc.PerformanceCounters.Add("\Processor(_Total)\% Processor Time")
$pc.PerformanceCounters.Add("\Memory\Available MBytes")
$pc.PerformanceCounters.Add("\PhysicalDisk(_Total)\Avg. Disk Queue Length")

$dcs.DataCollectors.Add($pc)
$dcs.Commit($dcsName, $null, 3)
```

---

## 8. Performance Baselines

A baseline is a measurement of the server's normal behavior captured when the
server is healthy.

**Why baselines matter:**

- Without a baseline, you cannot determine whether a metric is normal or abnormal.
- A 60% CPU reading may be expected for a workload-intensive server or alarming for
  a lightly loaded one. Only the baseline tells you which applies.

**Baseline best practice:**

- Capture a 72-hour baseline using a DCS before any major change.
- Include at minimum: CPU, memory, disk queue, and processor queue counters.
- Capture on a representative business day (not weekend or holiday).
- Store the BLG output and compare post-change data against it.

---

## 9. Get-Counter PowerShell Quick Reference

```powershell
# Single counter query
Get-Counter "\Processor(_Total)\% Processor Time"

# Multiple counters simultaneously
Get-Counter @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length"
)

# Sample at interval with max samples
Get-Counter "\Processor(_Total)\% Processor Time" `
    -SampleInterval 5 `
    -MaxSamples 12

# Per-core CPU
Get-Counter "\Processor(*)\% Processor Time" |
    Select-Object -ExpandProperty CounterSamples |
    Select-Object InstanceName, CookedValue |
    Sort-Object CookedValue -Descending

# Collect and export to CSV
$counters = @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length"
)
Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path "C:\PerfData\Baseline.csv" -FileFormat CSV

# Export to BLG (binary log for perfmon.exe)
Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path "C:\PerfData\Baseline.blg" -FileFormat BLG
```

**Key `Get-Counter` properties:**

| Property | Description |
|---|---|
| `CounterSamples` | Collection of individual counter sample objects |
| `Path` | Full counter path string |
| `CookedValue` | The numeric value of the counter sample |
| `InstanceName` | The specific instance (core number, disk letter, etc.) |

---

## 10. Event Viewer — Log Structure Reference

### Windows Logs

| Log | Contents |
|---|---|
| Application | Events from user-space applications and services |
| Security | Logon/logoff, privilege use, object access (requires audit policy) |
| System | Windows components, device drivers, service start/stop events |
| Setup | Role installation and Windows Update events |
| Forwarded Events | Events collected from remote computers via subscriptions |

### Applications and Services Logs

Vendor and role-specific logs. Examples:

- `Microsoft/Windows/DNS-Server/Operational` — DNS server events
- `Microsoft/Windows/GroupPolicy/Operational` — Group Policy processing
- `Microsoft/Windows/Security-Kerberos/Operational` — Kerberos authentication

### Event Levels

| Level | Meaning |
|---|---|
| Critical | Severe failure — system or application cannot recover |
| Error | Significant problem — function has failed |
| Warning | Potential problem — something may fail if not addressed |
| Information | Normal operational event |
| Audit Success | Security event completed successfully (Security log) |
| Audit Failure | Security event was attempted and denied (Security log) |

---

## 11. Event Viewer Filtering Reference

| Method | Persistence | Use Case |
|---|---|---|
| Filter Current Log | Temporary (resets on close) | One-time investigation |
| Custom View | Saved permanently in navigation tree | Recurring analysis |
| `Get-WinEvent -FilterHashtable` | Script / on-demand | Automated or scripted queries |

### Get-WinEvent PowerShell Reference

```powershell
# Errors from System log in last 4 hours
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    Level     = 2
    StartTime = (Get-Date).AddHours(-4)
} | Select-Object TimeCreated, Id, LevelDisplayName, Message -First 20

# Service Control Manager events (service starts/stops)
Get-WinEvent -FilterHashtable @{
    LogName      = 'System'
    ProviderName = 'Service Control Manager'
    StartTime    = (Get-Date).AddDays(-1)
} | Select-Object TimeCreated, Id, Message -First 15

# Security event 4625 (failed logons) in last hour
Get-WinEvent -FilterHashtable @{
    LogName = 'Security'
    Id      = 4625
    StartTime = (Get-Date).AddHours(-1)
} | Select-Object TimeCreated, Message

# Classic Get-EventLog (older cmdlet, still used for simple queries)
Get-EventLog -LogName System -EntryType Error -Newest 20 |
    Select-Object TimeGenerated, Source, EventID, Message
```

**Why `-FilterHashtable` is more efficient than `Where-Object`:**
Filtering with `-FilterHashtable` passes the filter criteria to the Windows Event
Log service, which does the filtering at the source. `Where-Object` retrieves all
events into memory first and then filters. For large logs, this is a significant
performance difference.

### Event Log Size and Retention

```powershell
# View log size and overflow settings
Get-EventLog -List | Select-Object Log, MaximumKilobytes, OverflowAction

# Set System log maximum to 64 MB
Limit-EventLog -LogName System -MaximumSize 65536KB

# OverflowAction values:
#   OverwriteAsNeeded  — default; overwrites oldest events
#   OverwriteOlder     — overwrites events older than specified days
#   DoNotOverwrite     — stops accepting new events when full (fills then stops)
```

---

## 12. Monitoring Architecture Overview

```text
Administrator Monitoring Workflow
══════════════════════════════════
Quick Check
  └── Task Manager (taskmgr.exe)
        └── Aggregate CPU/Memory/Disk/Network
              └── Problem found? → Identify process

Process Investigation
  └── Resource Monitor (resmon.exe)
        └── Per-process CPU, Memory, Disk, Network
              └── File paths, remote addresses, hard faults

Sustained Collection
  └── Performance Monitor (perfmon.exe)
        └── Data Collector Sets
              ├── Counters sampled every N seconds
              ├── Saved to BLG or CSV
              └── Compared against baseline

Historical Analysis
  └── Event Viewer (eventvwr.msc)
        ├── Filter Current Log (temporary)
        ├── Custom Views (saved)
        └── Get-WinEvent -FilterHashtable (scripted)
```

---

## 13. Exam Tips

**Exam Tip 1** — Tool selection: Resource Monitor is the correct answer when
the question asks how to identify which specific process is causing a performance
problem. Task Manager shows aggregates; it does not show per-process disk I/O or
network connections.

**Exam Tip 2** — Data Collector Sets run as a Windows service without requiring
an active user session. A real-time Performance Monitor graph stops when you
disconnect. For baseline collection, use a DCS.

**Exam Tip 3** — Counter thresholds to memorize: `Processor Queue Length` above
2 per core indicates CPU saturation. `Available MBytes` below 100 MB indicates
memory pressure. `Pages/sec` sustained above 5 indicates excessive paging. `Avg.
Disk Queue Length` above 2 per spindle indicates a storage bottleneck.

**Exam Tip 4** — `Get-WinEvent -FilterHashtable` is more efficient than
`Get-WinEvent | Where-Object` because filtering happens at the event log service
level, not after loading all events into memory.

**Exam Tip 5** — Filter Current Log is temporary. When Event Viewer is closed,
the filter is gone. Custom Views are saved permanently and appear in the
navigation tree for repeated use.

**Exam Tip 6** — Performance baselines should be captured before major changes
(new deployments, hardware changes, OS updates) so that post-change performance
can be compared against a known healthy state. 72 hours is the recommended
minimum baseline duration.

**Exam Tip 7** — `% Privileged Time` measures CPU in kernel mode. A high
`% Privileged Time` relative to `% Processor Time` suggests driver or I/O
overhead, not an application problem.

**Exam Tip 8** — `Avg. Disk Queue Length` above 2 per physical spindle indicates
a storage bottleneck. SSDs have much higher queue tolerance, but the threshold
remains the exam-standard answer for identifying a disk bottleneck.

---

## 14. Glossary

| Term | Definition |
|---|---|
| Performance counter | A named metric that measures a specific aspect of server behavior |
| Counter object | The category grouping related counters (Processor, Memory, PhysicalDisk) |
| Counter instance | The specific resource being measured (CPU core 0, disk C:) |
| CookedValue | The numeric value of a performance counter sample in PowerShell |
| Baseline | A snapshot of normal server performance used as a reference for comparison |
| Data Collector Set | A scheduled collection of performance counters that runs without a user session |
| BLG file | Binary Log — the native Performance Monitor output format |
| Performance Monitor | perfmon.exe — the GUI and framework for performance counter collection |
| Resource Monitor | resmon.exe — real-time per-process resource breakdown tool |
| Hard fault | A page fault resolved by reading from the page file on disk (not from memory cache) |
| Soft fault | A page fault resolved from memory cache (fast; not a performance concern) |
| Processor Queue Length | Count of threads waiting for CPU time; above 2 per core indicates saturation |
| Available MBytes | Free physical RAM; below 100 MB indicates memory pressure |
| Pages/sec | Rate of pages moved between RAM and disk; sustained high values indicate paging |
| Avg. Disk Queue Length | Average outstanding disk I/O requests; above 2 per spindle indicates bottleneck |
| Filter Current Log | Temporary Event Viewer filter; cleared when Event Viewer closes |
| Custom View | Saved Event Viewer filter that persists in the navigation tree |
| FilterHashtable | `Get-WinEvent` parameter that filters at the event log service level for efficiency |
| Event level | Severity classification: Critical, Error, Warning, Information, Audit |

---

## 15. Study Checklist

- Watch Module 15 Part 1 video (monitoring tools, performance counters, baselines,
  Data Collector Sets, Event Viewer)

- Watch Module 15 Part 2 video (Get-Counter demos, bottleneck identification,
  Event Viewer filtering, PowerShell health check script)

- Know which monitoring tool to use in each scenario (Task Manager, Resource
  Monitor, Performance Monitor, Event Viewer)

- Memorize all four bottleneck counter thresholds (CPU queue, memory, paging,
  disk queue)

- Know the difference between Filter Current Log (temporary) and Custom Views
  (saved)

- Know why `Get-WinEvent -FilterHashtable` is more efficient than piping to
  `Where-Object`

- Know the difference between a real-time PerfMon graph and a Data Collector Set

- Know the BLG file format and how to open it in Performance Monitor

- Review all PowerShell commands in Sections 9 and 11

- Complete Lab 15 and submit required screenshots

---

## Additional Resources

- [Performance Monitor overview](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon)
- [Get-Counter cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter)
- [Get-WinEvent cmdlet reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent)
- [Data Collector Sets overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749154(v=ws.11))

---

## 16. Supplemental Resources

The following free, open-access resources go deeper on Module 15 topics:

**1. Microsoft Learn — Monitor Windows Server performance**
<https://learn.microsoft.com/en-us/training/modules/monitor-windows-server-performance/>
Hands-on module covering Task Manager, Resource Monitor, Performance Monitor, Data Collector Sets, and event log analysis with sandbox exercises aligned to AZ-800.

**2. Microsoft Docs — Get-Counter cmdlet reference**
<https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter>
Full documentation for `Get-Counter` including counter path syntax, instance wildcards, `SampleInterval`, `MaxSamples`, `Continuous` mode, and exporting counter data with `Export-Counter`.

**3. Microsoft Learn — Implement Desired State Configuration (DSC)**
<https://learn.microsoft.com/en-us/training/modules/implement-desired-state-configuration/>
Covers DSC architecture, LCM configuration modes (ApplyOnly, ApplyAndMonitor, ApplyAndAutoCorrect), Push vs. Pull delivery, resource types, `DependsOn` ordering, and MOF compilation.

**4. Microsoft Docs — Windows PowerShell Desired State Configuration overview**
<https://learn.microsoft.com/en-us/powershell/scripting/dsc/overview>
Complete DSC reference including the DSC resource model, configuration data, partial configurations, troubleshooting with `Get-DscConfigurationStatus`, and `Test-DscConfiguration`.

---

*Review all sections before beginning Lab 15, Quiz 15, and Discussion 15.*

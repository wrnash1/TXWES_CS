# Reading Guide: Module 15 — Monitoring and Performance Tuning

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-3326 &BULL; WINDOWS SERVER ADMINISTRATION & ACTIVE DIRECTORY</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">Microsoft Learn &bull; CIS-3326 Module 15</strong>
    </div>
    <a href="https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/videoseries?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H" title="Windows Server Administration, Active Directory & Hybrid Cloud" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>Windows Server Administration, Active Directory & Hybrid Cloud</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->




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


---

## 3. Deep-Dive Conceptual Architecture & Theoretical Foundations

### 3.1 Foundational Invariants & Core Principles
At the center of **Module 15 — Monitoring and Performance Tuning** are specific mathematical, architectural, and operational invariants that govern how systems behave at enterprise scale. When designing or evaluating systems in this domain, engineers and technical leaders cannot treat the underlying mechanisms as a black box. 

Every operational trade-off boils down to three competing tensions:
1. **Consistency and Determinism:** The system must guarantee state transitions adhere strictly to formalized protocols, ACID/BASE guarantees, or regulatory frameworks.
2. **Computational Throughput and Scalability:** As data volume, transaction velocity, or organizational user counts scale horizontally, processing bottlenecks must be mitigated through asynchronous decoupling, caching, or hierarchical partitioning.
3. **Resilience and Adversarial Fault Tolerance:** The architecture must degrade gracefully under catastrophic failure, hardware degradation, or deliberate cyber-physical attacks.

### 3.2 Formal Mechanistic Walkthrough
To operationalize **Module 15 — Monitoring and Performance Tuning**, we decompose the execution lifecycle into sequential, verifiable stages:

```
[Phase 1: Ingestion & Validation] ──> [Phase 2: State Transformation] ──> [Phase 3: Verification & Persistence]
       │                                       │                                       │
       ▼                                       ▼                                       ▼
Input Sanitization, Schema              Algorithmic Execution,                  Cryptographic Hashing,
Validation & Boundary Checks             Concurrency Arbitration                 Write-Ahead Logging & Audit
```

1. **Ingestion & Boundary Verification:** Inputs entering the boundary of this architecture must undergo strict structural validation. In software systems, this prevents buffer overflows, injection vectors, and malformed state propagation. In enterprise and governance systems, this ensures data integrity before ledger entry.
2. **State Transformation & Concurrency Arbitration:** During execution, intermediate states must maintain transactional isolation. Whether managing distributed lock managers (DLM), thread synchronization, or multi-area routing convergence, race conditions must be mathematically eliminated using provable synchronization primitives.
3. **Commit, Persistence, and Telemetry:** Once state transitions execute successfully, atomic commits guarantee persistence across non-volatile memory or distributed journals. Comprehensive telemetry events are simultaneously emitted to structured observability pipelines.

---

## 4. Real-World Engineering Scenarios & Failure Mode Analysis

### Case Study: High-Impact Enterprise Failure Mode
Consider an enterprise production failure where an organization fails to adhere to the core principles of **Module 15 — Monitoring and Performance Tuning**:

* **Incident Context:** During peak quarterly processing, an enterprise infrastructure stack running critical financial or operational workflows experienced cascading timeouts and data corruption.
* **Root Cause Diagnostics:** Technicians misconfigured operational parameters, ignoring queue saturation thresholds and bypassing circuit-breaker protections. When transient latency occurred on upstream dependencies, worker threads blocked indefinitely, leading to resource starvation, memory exhaustion, and silent data drops.
* **Remediation Architecture:**
  * Implemented an exponential backoff retry policy coupled with full jitter to eliminate thundering herd phenomena.
  * Deployed strict isolation boundaries (bulkheads) to restrict cascading failures to isolated tenant pools.
  * Enforced continuous automated telemetry alarms monitoring p99 latency, queue depth, and error budget exhaustion.

```python
# Production Architectural Invariant: Resilient Execution with Circuit Breaking
import time
import random

class ResilientExecutionGovernor:
    def __init__(self, failure_threshold=5, recovery_timeout=30):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = 0
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def execute_with_guard(self, operation, *args, **kwargs):
        current_time = time.time()
        
        # Check Circuit State
        if self.state == "OPEN":
            if current_time - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF-OPEN"
            else:
                raise RuntimeError("CircuitBreakerOpen: Request rejected to preserve system invariants.")

        try:
            result = operation(*args, **kwargs)
            if self.state == "HALF-OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = current_time
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            raise e
```

---

## 5. Critical Misconceptions & Certification Exam Traps

In both certification examinations (such as CompTIA, Cisco, AWS, Scrum.org) and doctoral defense committees, specific high-yield traps consistently cause students to fail. Review these critical distinctions:

| Common Student Misconception | Architectural Reality & Truth | Consequence of Misunderstanding |
|---|---|---|
| *"More resources or threads linearly scale performance."* | Amdahl's Law proves speedup is strictly capped by the sequential fraction of the task; thread contention adds lock overhead. | Costly infrastructure overprovisioning with degraded throughput. |
| *"Redundancy alone guarantees high availability."* | Unmonitored redundancy creates hidden common-mode failure points and split-brain states without quorum arbitration. | Catastrophic double-outages and corrupted ledger state. |
| *"Default vendor configurations are production-ready."* | Vendor defaults prioritize ease of setup over least privilege, hardened encryption, and tuned memory limits. | Severe security vulnerability exposure and predictable resource exhaustion. |
| *"Fast recovery is a substitute for data integrity."* | Recovering quickly with inconsistent or unverified state compounds operational damage beyond the initial downtime. | Long-term ledger corruption and regulatory audit failure. |

---

## 6. Formative Knowledge Synthesis & Applied Defense Prompts

To confirm mastery before proceeding to this module's laboratory exercises and synthesis quizzes, synthesize responses to the following peer-review prompts:

### Mastery Check 1: Invariant Analysis
> **Question:** In the context of **Module 15 — Monitoring and Performance Tuning**, explain how an engineer or researcher mathematically proves that system invariants hold true across asynchronous boundaries. What specific telemetry metrics provide definitive empirical proof?

### Mastery Check 2: Architectural Trade-off Defense
> **Question:** Given an SLA requiring 99.999% availability with a maximum RTO of 60 seconds and RPO of 0 seconds, evaluate the specific trade-offs required in system throughput and capital expenditure. Why is zero-data-loss active-active replication significantly more complex than asynchronous warm-standby?

### Mastery Check 3: Adversarial Threat Modeling
> **Question:** Apply the STRIDE or NIST CSF threat modeling methodology to the core components of this module. Identify the single most dangerous privilege escalation or state desynchronization vector, and formulate a defense-in-depth mitigation strategy.

---

## 7. Faculty Synthesis & Academic Reflection
> *"True mastery in computing and technology leadership is not measured by the ability to recite definitions, but by the ability to diagnose anomalous system behavior, defend architectural trade-offs under rigorous peer review, and build systems that remain resilient in the face of uncertainty."*  
> — **Department of Computer Science & Information Systems, Texas Wesleyan University**


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

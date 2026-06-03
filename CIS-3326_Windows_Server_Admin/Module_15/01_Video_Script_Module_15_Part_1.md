# Video Script: Module 15 — Monitoring and Performance Tuning (Part 1)

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Production Notes

**Recorded by:** Professor Nash | Texas Wesleyan University

**Estimated runtime:** 13–15 minutes

**Part 1 focus:** Concepts — monitoring tools (Task Manager, Resource Monitor,
Performance Monitor, Event Viewer), key performance counters, performance
baselines, Data Collector Sets, and event log management.

---

## Opening

Welcome to Module 15 — Monitoring and Performance Tuning. Understanding how
to monitor a Windows Server and interpret what you see is one of the most
practical skills in server administration. You cannot fix what you cannot
measure.

This module covers the monitoring tools built into Windows Server, how to
identify performance bottlenecks, and how to tune the server to address them.

---

## Section 1 — The Monitoring Toolset

Windows Server provides four main monitoring tools that serve different
purposes. Knowing which tool to use in which situation is a key exam skill.

[SHOW SCREEN: Windows Server desktop showing Task Manager, Resource Monitor, Performance Monitor, and Event Viewer icons]
[Alt-text: Four application icons side by side: Task Manager, Resource Monitor (resmon.exe), Performance Monitor (perfmon.exe), and Event Viewer (eventvwr.msc).]

**Task Manager** (taskmgr.exe) provides a quick overview of CPU, memory,
disk, and network at the system level. On the Performance tab you see aggregate
resource usage. On the Processes tab you see which processes are running. It is
the fastest tool to open and gives you an immediate pulse check.

**Resource Monitor** (resmon.exe) goes deeper than Task Manager. It shows
per-process CPU, memory, disk, and network activity in a single unified view.
When you know something is slow but Task Manager only shows aggregate totals,
Resource Monitor tells you which specific process is responsible.

**Performance Monitor** (perfmon.exe) is the tool for sustained data
collection over time. You add specific performance counters, graph them over
hours or days, and compare against baselines. It is the right tool when you
need to capture trends and scheduled data collection.

**Event Viewer** (eventvwr.msc) is the log review tool. System events,
application errors, security audits, and diagnostic information are all
recorded here. It is not a real-time performance tool — it shows you what
happened, not what is happening right now.

---

## Section 2 — Task Manager Deep Dive

[SHOW SCREEN: Task Manager Performance tab]
[Alt-text: Task Manager Performance tab showing CPU, Memory, Disk, and Network graphs with a four-resource summary panel.]

The Performance tab shows:

- CPU: current percentage, base speed, logical processor count
- Memory: total, in use, available, cached, committed, paged pool
- Disk: active time percentage and read/write throughput
- Network: adapter name, send and receive throughput

The Processes tab sorts processes by CPU, Memory, Disk, or Network usage.
Right-click any process to open it in Resource Monitor for more detail.

For server administration without a GUI (Server Core), you can open Task
Manager from a remote desktop session or use PowerShell cmdlets like
`Get-Process` and `Get-Counter` instead.

---

## Section 3 — Resource Monitor

[SHOW SCREEN: Resource Monitor Overview tab]
[Alt-text: Resource Monitor showing four sections: CPU, Memory, Disk, and Network. Each section is expandable and shows per-process activity with utilization bars.]

Resource Monitor's Overview tab is the unified view. Click any section to
expand it and see per-process detail.

The CPU section shows which processes are consuming CPU and which DLLs they
have loaded — useful for diagnosing software conflicts.

The Memory section shows per-process Commit, Working Set, Shareable, and
Private memory. It also shows Hard Faults per second. Hard faults mean the
OS is reading data from the page file on disk because physical memory is full.
High hard faults indicate you need more RAM.

The Disk section shows each process's read and write activity in bytes per
second and the file paths being accessed. This is how you identify which
process is hammering the storage.

The Network section shows per-process send and receive rates and the remote
addresses each process is communicating with.

---

## Section 4 — Performance Monitor and Performance Counters

Performance Monitor is built around performance counters — individual metrics
that measure specific aspects of the server's behavior.

A counter is identified by three components:

- Object: the category (Processor, Memory, PhysicalDisk, Network Interface)
- Counter: the specific metric (% Processor Time, Available MBytes, Disk Read Bytes/sec)
- Instance: which specific object (which CPU core, which disk)

[SHOW SCREEN: Performance Monitor Add Counters dialog]
[Alt-text: Add Counters dialog showing Processor object selected with counter list including % Processor Time, % User Time, % Privileged Time. Instance list shows _Total and individual core numbers.]

Key counters to know for the exam:

CPU counters:

- `Processor\% Processor Time` — overall CPU utilization
- `Processor\% User Time` — CPU time in user mode (applications)
- `Processor\% Privileged Time` — CPU time in kernel mode (OS, drivers, I/O)
- `System\Processor Queue Length` — threads waiting to run; above 2 per core indicates saturation

Memory counters:

- `Memory\Available MBytes` — free physical RAM; below 100 MB is critical
- `Memory\Pages/sec` — pages moved to/from disk per second; sustained high values indicate excessive paging
- `Memory\Page Faults/sec` — includes both soft faults (from cache) and hard faults (from disk)

Disk counters:

- `PhysicalDisk\Avg. Disk Queue Length` — requests waiting; above 2 per spindle indicates a bottleneck
- `PhysicalDisk\Avg. Disk sec/Read` — latency for reads; above 20ms is concerning
- `PhysicalDisk\Avg. Disk sec/Write` — latency for writes
- `PhysicalDisk\% Disk Time` — percentage of time the disk is busy

Network counters:

- `Network Interface\Bytes Total/sec` — total throughput
- `Network Interface\Output Queue Length` — packets waiting to be sent; above 2 indicates saturation

---

## Section 5 — Data Collector Sets

A Data Collector Set (DCS) is a named collection of performance counters,
traces, and configuration data that runs on a schedule and saves results for
analysis.

[SHOW SCREEN: Performance Monitor with Data Collector Sets expanded in the left pane]
[Alt-text: Performance Monitor navigation tree showing Data Collector Sets expanded with User Defined and System subfolders. A custom DCS named Baseline_72hr appears under User Defined.]

Key features of Data Collector Sets:

- Run autonomously as a background service — no user session required
- Can be scheduled to run at specific times for specific durations
- Output is saved to a file (BLG format — Binary Log)
- Results can be analyzed in Performance Monitor by opening the saved log
- Can trigger alerts when a counter exceeds a threshold

To create a DCS in the GUI: Performance Monitor, expand Data Collector Sets,
right-click User Defined, New, Data Collector Set. Use the Server Performance
template as a starting point for baseline collection.

---

## Section 6 — Performance Baselines

A baseline is a measurement of the server's normal performance taken when the
server is healthy and operating normally. Baselines are the reference point
for all future comparisons.

Without a baseline, you cannot answer:

- Is 60% CPU normal for this server or is it abnormal?
- Was disk latency always this high or is this new?
- Did this application deployment change memory consumption?

Best practice: capture a 72-hour baseline using a Data Collector Set before
any major change (new application deployment, hardware change, OS update).
Compare post-change data to the pre-change baseline to isolate the impact.

---

## Section 7 — Event Viewer and Event Log Management

[SHOW SCREEN: Event Viewer navigation tree]
[Alt-text: Event Viewer showing Windows Logs folder expanded with Application, Security, Setup, System, and Forwarded Events logs visible.]

Event Viewer organizes logs into these categories:

Windows Logs include Application (user-space applications and services),
Security (authentication, logon/logoff, privilege use, object access), and
System (Windows components, device drivers, service starts/stops).

Applications and Services Logs contain vendor-specific and role-specific logs
such as Microsoft/Windows/DNS-Server/Operational for DNS events.

Event levels: Critical (severe failure), Error (significant problem), Warning
(potential problem), Information (normal event), Audit Success, and
Audit Failure for security log entries.

For focused analysis without changing the log permanently, use Filter Current
Log. Specify event level, time range, event source, event ID, and keywords.

For recurring analysis, create a Custom View which saves the filter criteria
and appears in the navigation tree for quick access.

Event log size and retention: when the log reaches capacity, the default
behavior is Overwrite events as needed. Archive the log when full preserves
all events by saving the full log to a file before starting a new one.

```powershell
# Check log size and retention settings
Get-EventLog -List | Select-Object Log, MaximumKilobytes, OverflowAction

# Set log maximum size (in KB)
Limit-EventLog -LogName System -MaximumSize 65536KB
```

---

## Module Summary

Windows Server monitoring tools: Task Manager for a quick pulse, Resource
Monitor for per-process real-time detail, Performance Monitor for sustained
counter collection and trending, Event Viewer for log review.

Key counter categories: Processor, Memory, PhysicalDisk, and Network Interface.
Threshold values to remember: Processor Queue Length above 2 per core,
Available MBytes below 100 MB, Avg. Disk Queue Length above 2 per spindle.

Data Collector Sets capture counter data on a schedule without requiring an
active user session. Used for baseline capture and long-term trending.

In Part 2 we demo all of this in PowerShell and GUI. See you there.

---

Module 15 Part 1 — End of Script

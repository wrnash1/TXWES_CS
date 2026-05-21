# Reading Guide: Module 15 - Monitoring and Performance Tuning

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Introduction

Welcome to **Module 15 – Monitoring and Performance Tuning**! This week's study material covers the tools and techniques used to monitor Windows Server health, diagnose performance bottlenecks, and tune the system for optimal throughput. Monitoring and performance topics appear on the AZ-800 exam in both identification and remediation scenarios.

As a student, you will learn how to use Performance Monitor, Resource Monitor, Task Manager, and Event Viewer to identify issues, how to set data collector sets and alerts, and how to baseline server performance to detect changes over time. Make sure to complete the checklist and review the glossary terms before beginning the lab activity.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Performance Monitor (PerfMon)**: A built-in Windows tool that tracks real-time and historical performance counters for CPU, memory, disk, and network. Data Collector Sets record counters over time to a log file for trend analysis and capacity planning. Accessed via `perfmon.exe`.
* **Key Performance Counters**: Critical counters for server health: `Processor\% Processor Time` (sustained >85% signals CPU saturation), `Memory\Available MBytes` (low values indicate memory pressure), `PhysicalDisk\Avg. Disk Queue Length` (>2 per spindle indicates disk bottleneck), `Network Interface\Bytes Total/sec` (compared against link capacity).
* **Resource Monitor**: A more granular real-time tool than Task Manager that shows per-process CPU, memory, disk I/O, and network activity. Useful for identifying which specific process is consuming resources. Accessed via `resmon.exe` or the Performance tab of Task Manager.
* **Event Viewer**: The central log management console for Windows Server. The most important logs are the System log (OS and driver events), Application log (application errors), and Security log (audit events — logon successes/failures, privilege use). Critical and Error events should be investigated first.
* **Windows Reliability Monitor**: A simplified view of system stability over time, scoring the system's reliability on a 1–10 scale and listing critical events, warnings, and informational entries. Useful for identifying when a performance or stability problem first appeared.
* **Data Collector Set**: A group of performance counters, event traces, and configuration data saved together in Performance Monitor. Data Collector Sets can be scheduled to run at specific times and export results to reports, enabling regular performance trending and SLA reporting.

---

### 2. Certification Exam Tips

* **Four bottleneck categories — CPU, memory, disk, network**: AZ-800 performance scenarios follow a standard pattern: identify the bottleneck category from symptoms, then identify the specific counter. High `% Processor Time` = CPU. Low `Available MBytes` + high paging = memory. High disk queue length = disk. High `Bytes Total/sec` near link capacity = network.
* **Baseline before optimization**: A performance "baseline" is a recorded snapshot of normal server performance under typical load. Without a baseline, you cannot distinguish a degraded state from normal behavior. Exam scenarios often establish that a baseline exists before asking about changes.
* **Event Viewer log filtering**: Know how to filter Event Viewer by Event ID, source, and date range using the "Filter Current Log" option. For AD DS-specific issues, the Directory Services log under Applications and Services Logs contains domain-related events not found in the System log.
* **Microsoft Learn Reference**: Review monitoring and performance documentation at [Microsoft Learn – Performance Tuning Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/) and [Microsoft Learn – Event Viewer](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-r2-and-2008/cc766042(v=ws.11)) for counter descriptions and tuning guidance.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Read the performance tuning documentation at [Microsoft Learn: Performance Tuning Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/). Focus on role-specific tuning guidelines, key performance counters, and Data Collector Set configuration.
* **Required Video:** Watch the video lecture on **Monitoring and Performance Tuning** in the official course playlist: [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).

---

### Lab & Command Integration

In this week's hands-on lab, you will create a Data Collector Set in Performance Monitor to record CPU, memory, and disk counters over a 10-minute period, generate a report from the collected data, and identify a simulated bottleneck. You will also use Event Viewer to filter the Security log for failed logon attempts (Event ID 4625).

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Read the performance tuning documentation at [Microsoft Learn: Performance Tuning Windows Server](https://learn.microsoft.com/en-us/windows-server/administration/performance-tuning/).
* [ ] Watch the video lecture on **Monitoring and Performance Tuning** in [Windows Server Administration Course](https://www.youtube.com/playlist?list=PLvG40H4sL3h0n72gQJ_m8N7xN61tL6d5H).
* [ ] Review the commands outlined in the lab instructions.
* [ ] Proceed to the weekly hands-on lab activity.

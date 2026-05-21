# Quiz: Module 15 - Monitoring and Performance Tuning

## Course: CIS-3326_Windows_Server_Admin (3326_Windows_Server_Admin - Microsoft Windows Server Administration (Active Directory))

---

### Question 1

A Windows Server administrator notices that the server responds slowly throughout the day. Before making any changes, the administrator wants to determine whether the bottleneck is CPU, memory, disk, or network. Which tool provides a real-time, unified view of all four resource categories simultaneously, including active processes sorted by resource consumption?

A) Performance Monitor (PerfMon), which graphs selected performance counters over time but requires the administrator to manually add each counter before viewing.
B) Resource Monitor (resmon.exe), which displays real-time CPU, memory, disk, and network activity broken down by individual process in a single consolidated view.
C) Task Manager on the Performance tab, which shows aggregate CPU and memory usage but does not display per-process disk and network statistics.
D) Event Viewer, which logs performance-related warning events with resource usage details when thresholds are exceeded.

* **Correct Answer:** B) Resource Monitor (resmon.exe), which displays real-time CPU, memory, disk, and network activity broken down by individual process in a single consolidated view.
* **Distractor Analysis:**
  * *Why A is incorrect:* Performance Monitor requires counters to be manually selected and added to a graph or Data Collector Set before data appears. It is the right tool for trending and baselining over time, but Resource Monitor is faster for an immediate real-time overview across all four resource categories without setup.
  * *Why C is incorrect:* Task Manager's Performance tab shows aggregate totals for CPU, memory, disk, and network but does not break down disk I/O or network activity by individual process. Resource Monitor provides that per-process breakdown needed to identify which specific application is causing the bottleneck.
  * *Why D is incorrect:* Event Viewer records discrete events and warnings after thresholds are breached — it is a log review tool, not a real-time resource monitoring tool. It would not show which process is currently consuming the most resources.

---

### Question 2

An administrator has been asked to establish a performance baseline for a Windows Server before a major application deployment. The baseline must capture CPU, memory, disk, and network counters continuously for 72 hours and save the data for future comparison. Which Performance Monitor feature is designed for this purpose?

A) A real-time Performance Monitor graph with all four counter categories added, run continuously on the administrator's workstation while connected to the server via Remote Desktop.
B) A Data Collector Set (DCS) configured with the required counters, a 72-hour schedule, and a defined output location — the DCS runs autonomously and saves the data without requiring an active user session.
C) Resource Monitor's Save function, which exports a 72-hour snapshot of all resource categories to a single report file.
D) Task Manager's history feature, which records CPU and memory usage for all processes over a rolling 72-hour window stored in the Windows event log.

* **Correct Answer:** B) A Data Collector Set (DCS) configured with the required counters, a 72-hour schedule, and a defined output location — the DCS runs autonomously and saves the data without requiring an active user session.
* **Distractor Analysis:**
  * *Why A is incorrect:* A real-time PerfMon graph requires an active Remote Desktop session to remain open for the full 72 hours. If the RDP session disconnects, the graph stops. Data Collector Sets run as a background service and continue collecting data independently of any user session.
  * *Why C is incorrect:* Resource Monitor does not have a "Save" or recording function that captures data over 72 hours. It is a real-time display tool only, with no built-in capability to record and export historical performance data.
  * *Why D is incorrect:* Task Manager does not maintain a 72-hour rolling performance history stored in the event log. The event log records discrete events, not continuous counter samples. CPU/memory history in Task Manager is a short-duration visual aid, not a persistent baselining mechanism.

---

### Question 3

An administrator reviewing Performance Monitor data on a Windows Server sees that the `Avg. Disk Queue Length` counter is consistently above 2 for the data volume, while CPU and memory counters are within normal ranges. What does this indicate, and what is the appropriate next step?

A) The disk controller driver is outdated; the administrator should update the storage driver and reboot the server to resolve the queue buildup.
B) The server has a disk I/O bottleneck — more I/O requests are arriving than the storage subsystem can service. The administrator should investigate moving workloads to faster storage (SSD) or distributing I/O across additional disks.
C) A value above 2 for Avg. Disk Queue Length is normal for production file servers and does not indicate a performance problem; no action is needed.
D) High Avg. Disk Queue Length always indicates low available memory causing excessive paging; the administrator should add RAM before examining disk hardware.

* **Correct Answer:** B) The server has a disk I/O bottleneck — more I/O requests are arriving than the storage subsystem can service. The administrator should investigate moving workloads to faster storage (SSD) or distributing I/O across additional disks.
* **Distractor Analysis:**
  * *Why A is incorrect:* While an outdated driver can sometimes cause issues, Avg. Disk Queue Length above 2 is a capacity and throughput metric, not a driver compatibility symptom. The primary indication is that the physical storage cannot process queued requests fast enough, which points to a storage capacity or speed issue.
  * *Why C is incorrect:* A sustained Avg. Disk Queue Length above 2 is the accepted threshold indicating a storage bottleneck. Values persistently above 2 per spindle mean that requests are waiting longer than the hardware can service, causing application delays.
  * *Why D is incorrect:* While high paging activity (caused by low memory) can increase disk queue length on the system/paging volume, the question specifies that memory counters are normal. High Avg. Disk Queue Length on a data volume with normal memory counters points directly to a disk I/O bottleneck, not a memory issue.

---

### Question 4

A Windows Server is generating thousands of application event log entries per day, making it difficult to identify critical errors. An administrator wants to see only Error and Critical events from the Application log that were generated by the service named `AppService` in the past 24 hours. Which Event Viewer feature accomplishes this without creating a permanent view change?

A) Sort the Event Viewer Application log by Level column and scroll to find Error entries — sorting is the fastest way to isolate error events in a large log.
B) Use the Filter Current Log feature in Event Viewer to specify Event Level (Error, Critical), the time period (Last 24 hours), and the event source (AppService), which applies a temporary filter to the current log view.
C) Create a Custom View in Event Viewer by specifying the same criteria — Custom Views are the only mechanism that supports multi-criteria filtering including source and time range.
D) Export the Application log to a CSV file and use Excel to filter rows by Level and Source columns.

* **Correct Answer:** B) Use the Filter Current Log feature in Event Viewer to specify Event Level (Error, Critical), the time period (Last 24 hours), and the event source (AppService), which applies a temporary filter to the current log view.
* **Distractor Analysis:**
  * *Why A is incorrect:* Sorting by Level shows all Error events but does not filter by time range or source. With thousands of entries per day, scrolling through sorted errors is inefficient compared to applying a multi-criteria filter that narrows the results immediately.
  * *Why C is incorrect:* Custom Views also support multi-criteria filtering including source and time range and are saved persistently for reuse. However, the question asks for a solution without creating a permanent view change, making Filter Current Log (which is temporary and discarded when the log is closed) the more precise answer.
  * *Why D is incorrect:* Exporting to CSV and filtering in Excel is a valid but unnecessarily complex approach when Event Viewer has built-in filtering. It also requires additional tools and is slower than the native filtering capability.

---

### Question 5

An administrator uses Performance Monitor to monitor the `% Processor Time` counter on a Windows Server and observes that it averages 92% over the past week. The server runs a single multi-threaded application. Which additional counter should the administrator examine to determine whether the CPU is the true bottleneck or whether the application is waiting on another resource such as disk?

A) `Memory\Available MBytes`, which indicates whether low memory is causing the CPU to spend time handling page faults rather than running application threads.
B) `Processor\% Privileged Time`, which measures the percentage of time the CPU spends on kernel-mode operations such as processing I/O requests, helping distinguish compute-bound from I/O-bound CPU utilization.
C) `Network Interface\Bytes Total/sec`, which shows whether network saturation is causing the application to stall, consuming CPU cycles waiting for data.
D) `System\Processor Queue Length`, which shows how many threads are waiting to run — if it is consistently above 2 per CPU core, the CPU is genuinely compute-saturated.

* **Correct Answer:** D) `System\Processor Queue Length`, which shows how many threads are waiting to run — if it is consistently above 2 per CPU core, the CPU is genuinely compute-saturated.
* **Distractor Analysis:**
  * *Why A is incorrect:* `Memory\Available MBytes` helps diagnose memory pressure and paging, which can indirectly affect CPU time. However, if CPU is running at 92% because of paging, the disk queue length would also be elevated. Available MBytes alone does not confirm whether the CPU itself is the bottleneck or whether it is spending time servicing I/O on behalf of a memory-starved application.
  * *Why B is incorrect:* `% Privileged Time` showing a high value does indicate that the CPU is spending significant time in kernel mode (often for I/O handling), which would suggest the CPU is not compute-saturated but rather I/O-bound. This is a useful companion counter, but the question asks for the counter that best determines whether CPU is the true bottleneck, which is Processor Queue Length.
  * *Why C is incorrect:* `Network Interface\Bytes Total/sec` reveals network throughput but does not directly explain high CPU utilization. Unless the application is specifically network-intensive and the CPU is processing network interrupts, network saturation would more likely manifest as network queue length rather than sustained high CPU time.

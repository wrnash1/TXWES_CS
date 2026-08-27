# Lab Activity: Module 15 — Monitoring and Performance Tuning

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Lab Overview

In this lab you will use `Get-Counter` to collect live performance counter data,
create a baseline CSV file, query Event Viewer with both the GUI filter and
`Get-WinEvent -FilterHashtable`, write a PowerShell server health check script
with threshold comparisons, export the results to a report file, and create a
Data Collector Set. Complete all parts and submit the required screenshots.

**Estimated Time:** 75–90 minutes

**Prerequisites:**

- DC1 is a domain controller for txwes.edu (Module 09 lab complete)
- DC1 IP address: 192.168.10.10
- PowerShell running as Administrator

**Learning Objectives:**

- Use `Get-Counter` to query live performance counters

- Collect counter data to CSV and BLG files

- Identify bottleneck conditions from counter output

- Filter Event Viewer logs using both the GUI and `Get-WinEvent -FilterHashtable`

- Write a health check script with `[PSCustomObject]` output and threshold logic

- Create a Data Collector Set using the PLA COM object

---

## Part 1 — Get-Counter: Live Performance Data

### Step 1.1 — Query Individual Counters

```powershell
# Query current CPU utilization
Get-Counter "\Processor(_Total)\% Processor Time"
```

```powershell
# Query multiple counters simultaneously
Get-Counter @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
    "\System\Processor Queue Length"
)
```

Take **Screenshot 1** — `Get-Counter` output showing CounterSamples with Path
and CookedValue columns for all five counters.

### Step 1.2 — Per-Core CPU Query

```powershell
# List CPU utilization per core, sorted descending
Get-Counter "\Processor(*)\% Processor Time" |
    Select-Object -ExpandProperty CounterSamples |
    Select-Object InstanceName, CookedValue |
    Sort-Object CookedValue -Descending
```

Take **Screenshot 2** — per-core CPU output showing InstanceName (0, 1, _total)
and CookedValue for each processor.

### Step 1.3 — Sample Counters Over Time

```powershell
# Sample CPU every 5 seconds for 12 samples (1 minute of data)
Get-Counter "\Processor(_Total)\% Processor Time" `
    -SampleInterval 5 `
    -MaxSamples 12 |
    Select-Object -ExpandProperty CounterSamples |
    Select-Object Path, CookedValue
```

Review the output. Note whether the CPU value is consistent or fluctuating.

---

## Part 2 — Collect Counter Data to File

### Step 2.1 — Create the Output Directory

```powershell
New-Item -Path "C:\PerfData" -ItemType Directory -Force | Out-Null
```

### Step 2.2 — Collect to CSV

```powershell
$counters = @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
    "\System\Processor Queue Length"
)

$csvPath = "C:\PerfData\Baseline_$(Get-Date -Format 'yyyyMMdd_HHmm').csv"

Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path $csvPath -FileFormat CSV

Write-Host "CSV saved to: $csvPath"
```

```powershell
# Verify the file was created
Get-ChildItem "C:\PerfData\" | Select-Object Name, Length, LastWriteTime
```

### Step 2.3 — Collect to BLG (Binary Log)

```powershell
Get-Counter -Counter $counters -SampleInterval 10 -MaxSamples 6 |
    Export-Counter -Path "C:\PerfData\Baseline.blg" -FileFormat BLG

# Verify
Get-ChildItem "C:\PerfData\" | Select-Object Name, Length, LastWriteTime
```

Take **Screenshot 3** — directory listing of `C:\PerfData\` showing both the
timestamped CSV file and the BLG file with file sizes.

### Step 2.4 — Open the BLG File in Performance Monitor

```powershell
Start-Process perfmon.exe
```

In Performance Monitor: click the green circle (Add Counters) arrow to stop
the live graph. Then click Action, Open Log File, and navigate to
`C:\PerfData\Baseline.blg`. The saved counter data will display as a graph.

---

## Part 3 — Bottleneck Identification

### Step 3.1 — Collect a 60-Second Snapshot

```powershell
$snapshot = Get-Counter @(
    "\Processor(_Total)\% Processor Time",
    "\Memory\Available MBytes",
    "\Memory\Pages/sec",
    "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
    "\System\Processor Queue Length"
) -SampleInterval 5 -MaxSamples 12

$snapshot.CounterSamples | Select-Object Path, CookedValue |
    Format-Table -AutoSize
```

### Step 3.2 — Evaluate the Results

Review each counter value against the thresholds:

```powershell
$cpu = ($snapshot.CounterSamples |
    Where-Object {$_.Path -like "*processor time*"} |
    Measure-Object CookedValue -Average).Average

$memMB = ($snapshot.CounterSamples |
    Where-Object {$_.Path -like "*available mbytes*"} |
    Measure-Object CookedValue -Average).Average

$diskQ = ($snapshot.CounterSamples |
    Where-Object {$_.Path -like "*disk queue*"} |
    Measure-Object CookedValue -Average).Average

$procQ = ($snapshot.CounterSamples |
    Where-Object {$_.Path -like "*processor queue*"} |
    Measure-Object CookedValue -Average).Average

Write-Host "Avg CPU %:        $([math]::Round($cpu,1))"
Write-Host "Avg Mem Free MB:  $([math]::Round($memMB,1))"
Write-Host "Avg Disk Queue:   $([math]::Round($diskQ,2))"
Write-Host "Avg Proc Queue:   $([math]::Round($procQ,2))"

if ($cpu -gt 85 -and $procQ -gt 2)  { Write-Warning "CPU bottleneck detected" }
if ($memMB -lt 100)                  { Write-Warning "Memory pressure detected" }
if ($diskQ -gt 2)                    { Write-Warning "Disk bottleneck detected" }
```

Take **Screenshot 4** — threshold evaluation output showing the four average
values and any warning messages generated.

---

## Part 4 — Event Viewer: GUI Filter and PowerShell Query

### Step 4.1 — Filter the System Log in Event Viewer GUI

```powershell
Start-Process eventvwr.msc
```

In Event Viewer:

1. Expand Windows Logs and click System.
2. Click Action in the menu bar, then Filter Current Log.
3. Set the Logged dropdown to Last 4 hours.
4. Under Event level, check Error.
5. Click OK.

The log now shows only Error events from the past 4 hours.

Take **Screenshot 5** — Event Viewer System log with the filter active, showing
filtered events with the Filter Current Log dialog or the orange filter bar
visible.

### Step 4.2 — Query Events with PowerShell

```powershell
# System log errors from the last 4 hours
Get-WinEvent -FilterHashtable @{
    LogName   = 'System'
    Level     = 2
    StartTime = (Get-Date).AddHours(-4)
} | Select-Object TimeCreated, Id, LevelDisplayName, Message -First 20 |
    Format-Table -AutoSize -Wrap
```

```powershell
# Service Control Manager events from the last 24 hours
Get-WinEvent -FilterHashtable @{
    LogName      = 'System'
    ProviderName = 'Service Control Manager'
    StartTime    = (Get-Date).AddDays(-1)
} | Select-Object TimeCreated, Id, Message -First 15 |
    Format-Table -AutoSize -Wrap
```

Take **Screenshot 6** — `Get-WinEvent -FilterHashtable` output showing
TimeCreated, Id, and Message columns for System log errors or service events.

### Step 4.3 — Check Event Log Size and Retention Settings

```powershell
Get-EventLog -List |
    Select-Object Log, MaximumKilobytes, OverflowAction |
    Format-Table -AutoSize
```

---

## Part 5 — Server Health Check Script

### Step 5.1 — Create the Script File

```powershell
New-Item -Path "C:\PerfData" -ItemType Directory -Force | Out-Null
```

Create the file `C:\PerfData\ServerHealthSnapshot.ps1` with the following
content:

```powershell
# ServerHealthSnapshot.ps1
# Collects a performance snapshot and writes a simple status report

param(
    [string]$ComputerName = "localhost",
    [int]$Samples         = 3,
    [int]$Interval        = 10
)

function Get-AvgCounter {
    param($CounterPath, $N, $I)
    $data = Get-Counter -Counter $CounterPath `
        -ComputerName $ComputerName `
        -SampleInterval $I `
        -MaxSamples $N `
        -ErrorAction SilentlyContinue

    if ($data) {
        [math]::Round(
            ($data.CounterSamples |
             Measure-Object CookedValue -Average).Average, 1)
    } else { -1 }
}

$cpuPct = Get-AvgCounter "\Processor(_Total)\% Processor Time" $Samples $Interval
$memMB  = Get-AvgCounter "\Memory\Available MBytes"            $Samples $Interval
$diskQ  = Get-AvgCounter "\PhysicalDisk(_Total)\Avg. Disk Queue Length" $Samples $Interval
$procQ  = Get-AvgCounter "\System\Processor Queue Length"      $Samples $Interval

$status = if ($cpuPct -gt 85 -or $memMB -lt 200 -or $diskQ -gt 2) {
    "WARNING"
} else {
    "OK"
}

[PSCustomObject]@{
    Computer   = $ComputerName
    CPU_Pct    = $cpuPct
    MemFree_MB = $memMB
    DiskQueue  = $diskQ
    ProcQueue  = $procQ
    Status     = $status
    Timestamp  = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
}
```

### Step 5.2 — Run the Script

```powershell
# Run with default 3 samples at 10-second intervals
$result = & "C:\PerfData\ServerHealthSnapshot.ps1" -ComputerName "localhost"
$result | Format-List
```

### Step 5.3 — Export the Result

```powershell
$result | Export-Csv `
    -Path "C:\PerfData\HealthSnapshot_$(Get-Date -Format 'yyyyMMdd_HHmm').csv" `
    -NoTypeInformation

# Verify
Get-ChildItem "C:\PerfData\" | Select-Object Name, Length, LastWriteTime
```

Take **Screenshot 7** — health check script output showing Computer, CPU_Pct,
MemFree_MB, DiskQueue, ProcQueue, Status, and Timestamp fields.

---

## Part 6 — Create a Data Collector Set

### Step 6.1 — Create the DCS with the PLA COM Object

```powershell
$dcsName = "TXWES_Baseline_$(Get-Date -Format 'yyyyMMdd')"

$dcs = New-Object -COM Pla.DataCollectorSet
$dcs.DisplayName = $dcsName
$dcs.Duration    = 3600          # 1 hour in seconds
$dcs.SubdirectoryFormat = 1

$pc = $dcs.DataCollectors.CreateDataCollector(0)
$pc.Name           = "PerfCounters"
$pc.SampleInterval = 30          # every 30 seconds
$pc.FileFormat     = 3           # 3 = CSV

$pc.PerformanceCounters.Add("\Processor(_Total)\% Processor Time")
$pc.PerformanceCounters.Add("\Memory\Available MBytes")
$pc.PerformanceCounters.Add("\Memory\Pages/sec")
$pc.PerformanceCounters.Add("\PhysicalDisk(_Total)\Avg. Disk Queue Length")
$pc.PerformanceCounters.Add("\System\Processor Queue Length")

$dcs.DataCollectors.Add($pc)
$dcs.Commit($dcsName, $null, 3)   # 3 = create or modify

Write-Host "Data Collector Set '$dcsName' created."
```

### Step 6.2 — Verify in Performance Monitor GUI

```powershell
Start-Process perfmon.exe
```

In Performance Monitor: expand Data Collector Sets, then User Defined. The
newly created DCS should appear in the list.

### Step 6.3 — Start the DCS

```powershell
# Start the collector set (it will run for 1 hour then stop automatically)
$dcs.Start($false)
Write-Host "DCS status: $($dcs.Status)"
```

### Step 6.4 — Check Status and Stop

```powershell
Write-Host "DCS status: $($dcs.Status)"

# Stop the DCS manually
$dcs.Stop($false)
Write-Host "DCS stopped."
```

Take **Screenshot 8** — Performance Monitor showing the TXWES_Baseline DCS
under User Defined in the navigation tree.

---

## Part 7 — Verification Summary

```powershell
Write-Host "=== PerfData Directory Contents ===" -ForegroundColor Cyan
Get-ChildItem "C:\PerfData\" -Recurse |
    Select-Object Name, Length, LastWriteTime |
    Format-Table -AutoSize

Write-Host "=== Health Snapshot CSV ===" -ForegroundColor Cyan
Get-ChildItem "C:\PerfData\HealthSnapshot_*.csv" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1 |
    ForEach-Object { Import-Csv $_.FullName | Format-List }

Write-Host "=== Event Log Sizes ===" -ForegroundColor Cyan
Get-EventLog -List |
    Select-Object Log, MaximumKilobytes, OverflowAction |
    Format-Table -AutoSize
```

Take **Screenshot 9** — full verification summary showing PerfData directory
contents, health snapshot values, and event log size settings.

---

## Deliverables

Submit the following screenshots to Canvas before the due date.

**Screenshot 1** — `Get-Counter` output for all five counters showing
CounterSamples with Path and CookedValue.

**Screenshot 2** — Per-core CPU output showing InstanceName and CookedValue
for each processor.

**Screenshot 3** — `C:\PerfData\` directory listing showing both the CSV and
BLG baseline files with sizes.

**Screenshot 4** — Threshold evaluation output showing average CPU, memory,
disk queue, and processor queue values.

**Screenshot 5** — Event Viewer System log with Filter Current Log active
(Last 4 hours, Error level).

**Screenshot 6** — `Get-WinEvent -FilterHashtable` output showing system log
error events.

**Screenshot 7** — ServerHealthSnapshot.ps1 output showing all fields including
Status.

**Screenshot 8** — Performance Monitor showing the TXWES_Baseline DCS under
User Defined.

**Screenshot 9** — Full verification summary.

---

## Lab Rubric (100 Points)

| Item | Points | Criteria |
|---|---|---|
| Get-Counter multi-counter query | 10 | Screenshot 1 shows all five counters with CookedValue |
| Per-core CPU query | 10 | Screenshot 2 shows per-instance CPU data |
| Baseline files created | 15 | Screenshot 3 shows both CSV and BLG files |
| Bottleneck evaluation | 15 | Screenshot 4 shows threshold comparison output |
| Event Viewer GUI filter | 10 | Screenshot 5 shows filtered System log |
| Get-WinEvent PowerShell query | 10 | Screenshot 6 shows FilterHashtable output |
| Health check script | 20 | Screenshot 7 shows all PSCustomObject fields |
| Data Collector Set | 10 | Screenshot 8 shows DCS in Performance Monitor |

---

## Troubleshooting Notes

If `Get-Counter` returns no data for `\PhysicalDisk(_Total)\Avg. Disk Queue
Length`, ensure the Performance Counter DLL host service is running:

```powershell
Get-Service -Name PerfHost | Select-Object Name, Status
Start-Service -Name PerfHost
```

If `Export-Counter` fails with "the path cannot be null," ensure the target
directory exists:

```powershell
New-Item -Path "C:\PerfData" -ItemType Directory -Force
```

If `Get-WinEvent` returns no results, the time range may contain no matching
events. Try extending the time window:

```powershell
Get-WinEvent -FilterHashtable @{
    LogName = 'System'
    Level   = 2
    StartTime = (Get-Date).AddDays(-7)
} -MaxEvents 10
```

If the PLA COM object fails with "class not registered," ensure the server is
running Windows Server (not a client edition) and that Performance Monitor is
installed:

```powershell
Get-WindowsFeature -Name RSAT-Performance-Tools
```

---

## Part 9 — Challenge Exercise

### Challenge 1: Build an Automated Multi-Server Performance Baseline Report

Collect performance counter data from multiple servers simultaneously and generate
a comparative baseline CSV that can be used for trend analysis.

1. Create a function that collects a 60-second average of key performance counters
   from a remote server:

   ```powershell
   function Get-PerformanceBaseline {
       param(
           [Parameter(Mandatory=$true, ValueFromPipeline=$true)]
           [string]$ComputerName
       )
       process {
           try {
               $counters = @(
                   "\Processor(_Total)\% Processor Time",
                   "\Memory\Available MBytes",
                   "\Memory\Pages/sec",
                   "\PhysicalDisk(_Total)\Avg. Disk Queue Length",
                   "\System\Processor Queue Length"
               )

               $samples = Get-Counter -Counter $counters `
                   -ComputerName $ComputerName `
                   -SampleInterval 5 -MaxSamples 12 `
                   -ErrorAction Stop

               $data = $samples.CounterSamples | Group-Object Path |
                   ForEach-Object {
                       [PSCustomObject]@{
                           Counter   = ($_.Name -split "\\")[-1]
                           AvgValue  = [math]::Round(($_.Group.CookedValue | Measure-Object -Average).Average, 2)
                       }
                   }

               $result = [ordered]@{ Computer = $ComputerName }
               foreach ($item in $data) { $result[$item.Counter] = $item.AvgValue }
               [PSCustomObject]$result | Add-Member -NotePropertyName "Timestamp" `
                   -NotePropertyValue (Get-Date).ToString("yyyy-MM-dd HH:mm") -PassThru

           } catch {
               [PSCustomObject]@{
                   Computer  = $ComputerName
                   Error     = $_.Exception.Message
                   Timestamp = (Get-Date).ToString("yyyy-MM-dd HH:mm")
               }
           }
       }
   }
   ```

2. Run the function against a list of servers and collect baselines:

   ```powershell
   $servers  = @("DC1", "localhost")
   $baseline = $servers | Get-PerformanceBaseline
   $baseline | Format-Table -AutoSize
   ```

3. Export the baseline and compare against thresholds:

   ```powershell
   $baseline | Export-Csv "C:\PerfData\MultiServer_Baseline_$(Get-Date -Format yyyyMMdd).csv" `
       -NoTypeInformation

   # Flag servers exceeding thresholds
   foreach ($server in $baseline) {
       if ($server.'% Processor Time' -gt 80) {
           Write-Warning "$($server.Computer): CPU $($server.'% Processor Time')% — HIGH"
       }
       if ($server.'Available MBytes' -lt 200) {
           Write-Warning "$($server.Computer): Available RAM $($server.'Available MBytes') MB — LOW"
       }
       if ($server.'Pages/sec' -gt 5) {
           Write-Warning "$($server.Computer): Paging $($server.'Pages/sec') pages/sec — EXCESSIVE"
       }
   }
   ```

4. Load a previously saved baseline CSV and compare current values against it:

   ```powershell
   $previous = Import-Csv "C:\PerfData\MultiServer_Baseline_$(Get-Date -Format yyyyMMdd).csv"
   $current  = $servers | Get-PerformanceBaseline

   foreach ($cur in $current) {
       $prev = $previous | Where-Object { $_.Computer -eq $cur.Computer }
       if ($prev) {
           $cpuDelta = [double]$cur.'% Processor Time' - [double]$prev.'% Processor Time'
           Write-Host "$($cur.Computer) CPU delta vs baseline: $([math]::Round($cpuDelta,1))%"
       }
   }
   ```

   In your lab notes, explain why a 60-second sample (12 × 5-second intervals) is
   the minimum recommended duration for a meaningful baseline, and what time of
   day you should capture a baseline to represent typical production load.

### Challenge 2: Write and Apply a Multi-Resource DSC Configuration

Build a DSC configuration that configures three resources with dependency
ordering, compile it to a MOF, and verify compliance.

1. Write a DSC configuration that ensures IIS is installed, a web root directory
   exists, and the W3SVC service is running — in that order:

   ```powershell
   Configuration LabWebServer {
       Import-DscResource -ModuleName PSDesiredStateConfiguration

       Node "localhost" {
           WindowsFeature InstallIIS {
               Name   = "Web-Server"
               Ensure = "Present"
           }

           File WebRoot {
               DestinationPath = "C:\WebRoot"
               Type            = "Directory"
               Ensure          = "Present"
               DependsOn       = "[WindowsFeature]InstallIIS"
           }

           Service StartW3SVC {
               Name        = "W3SVC"
               State       = "Running"
               StartupType = "Automatic"
               DependsOn   = "[File]WebRoot"
           }
       }
   }

   # Compile to MOF
   LabWebServer -OutputPath "C:\DSC\LabWeb"
   Get-ChildItem "C:\DSC\LabWeb"
   ```

2. Configure the LCM for `ApplyAndMonitor` mode before applying:

   ```powershell
   [DSCLocalConfigurationManager()]
   Configuration LCMConfig {
       Node "localhost" {
           Settings {
               ConfigurationMode             = "ApplyAndMonitor"
               RefreshFrequencyMins          = 30
               ConfigurationModeFrequencyMins = 15
           }
       }
   }

   LCMConfig -OutputPath "C:\DSC\LCM"
   Set-DscLocalConfigurationManager -Path "C:\DSC\LCM" -Verbose
   Get-DscLocalConfigurationManager | Select-Object ConfigurationMode, RefreshFrequencyMins
   ```

3. Apply the configuration and verify:

   ```powershell
   Start-DscConfiguration -Path "C:\DSC\LabWeb" -Wait -Verbose -Force

   Test-DscConfiguration -Verbose
   Get-DscConfigurationStatus | Select-Object Status, StartDate, DurationInSeconds, ResourcesInDesiredState
   ```

4. Simulate drift by stopping the W3SVC service, then run `Test-DscConfiguration`
   to confirm the LCM detects the change:

   ```powershell
   Stop-Service -Name W3SVC -Force

   Test-DscConfiguration
   # Expected output: False (drift detected)

   Get-DscConfigurationStatus | Select-Object Status, ResourcesNotInDesiredState
   ```

   In your lab notes, record the `ResourcesNotInDesiredState` output. Then switch
   the LCM to `ApplyAndAutoCorrect` and observe whether the W3SVC service restarts
   automatically at the next consistency check.

### Reflection Questions

1. A performance baseline collected on Monday morning shows `Available MBytes: 1,800`
   and `Pages/sec: 0.2`. A baseline collected the following Friday afternoon shows
   `Available MBytes: 380` and `Pages/sec: 18.4`. Both baselines were collected
   from the same server with no hardware changes. Interpret these values, identify
   the resource bottleneck, and describe three investigation steps you would take
   to identify the root cause before recommending a hardware upgrade.

2. DSC `ApplyAndAutoCorrect` mode automatically corrects configuration drift, which
   sounds ideal. However, a change management board questions whether auto-correction
   could interfere with emergency manual changes made directly on a server during an
   incident. Describe a scenario where `ApplyAndAutoCorrect` would revert a valid
   emergency change, explain how you would prevent this in production while still
   maintaining configuration integrity, and identify which DSC configuration mode
   would be most appropriate for a regulated environment with strict change control.

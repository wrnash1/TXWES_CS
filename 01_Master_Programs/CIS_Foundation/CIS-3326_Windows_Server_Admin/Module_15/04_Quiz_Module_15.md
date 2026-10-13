# Quiz: Module 15 — PowerShell Automation and DSC

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Windows Server Administration

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
Review your Reading Guide and video notes before beginning.

---

### Question 1

An administrator wants to apply a server configuration that continuously enforces
the desired state and automatically corrects any drift without administrator
intervention. Which DSC Local Configuration Manager setting achieves this?

A) `ConfigurationMode = "ApplyOnly"`

B) `ConfigurationMode = "ApplyAndMonitor"`

C) `ConfigurationMode = "ApplyAndAutoCorrect"`

D) `RefreshMode = "Push"`

- **Correct Answer:** C
- **Distractor Analysis:**
  - Why A is incorrect: `ApplyOnly` applies the configuration once and never
    monitors or corrects drift afterward. Once the configuration is applied,
    any subsequent changes to the server are not detected or corrected.
  - Why B is incorrect: `ApplyAndMonitor` detects drift and logs it, but does
    not automatically correct it. An administrator must manually re-apply the
    configuration to restore the desired state.
  - Why D is incorrect: `RefreshMode = "Push"` describes how configurations
    are delivered to nodes — it does not control whether the LCM monitors for
    or corrects drift.

---

### Question 2

An administrator writes a DSC configuration that installs IIS and then starts
the W3SVC service. The service must not start until IIS is fully installed.
Which DSC property enforces this ordering?

A) `Requires`

B) `DependsOn`

C) `StartAfter`

D) `RunOrder`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Requires` is not a DSC property. There is no such
    keyword in DSC resource declarations.
  - Why C is incorrect: `StartAfter` is not a DSC property. DSC does not use
    this syntax for resource ordering.
  - Why D is incorrect: `RunOrder` is not a DSC property. Resource ordering in
    DSC is controlled exclusively through `DependsOn`.

---

### Question 3

An administrator runs `Test-DscConfiguration` on a server and receives the
output `False`. What does this mean?

A) The DSC configuration has not been applied to the server yet.

B) At least one DSC resource is out of compliance with the desired state.

C) The MOF file is corrupt and must be recompiled.

D) The LCM is in Push mode and must be switched to Pull mode.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `Test-DscConfiguration` tests the current state against
    the applied configuration. A return value of `False` means the configuration
    was previously applied but a resource has since drifted. If no configuration
    had been applied, a different error would occur.
  - Why C is incorrect: `Test-DscConfiguration` does not validate MOF file
    integrity. MOF corruption would produce an error, not a `False` return.
  - Why D is incorrect: `Test-DscConfiguration` is unrelated to the LCM
    `RefreshMode` setting. Push and Pull mode affect how configurations are
    delivered, not whether resources are in compliance.

---

### Question 4

An administrator wants to pass a collection of parameters to a cmdlet using a
hashtable to improve script readability. Which PowerShell technique does this?

A) Piping

B) Splatting

C) Dot-sourcing

D) Banding

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: Piping (`|`) passes objects from one cmdlet to another
    through the pipeline. It does not group named parameters into a hashtable
    for a single cmdlet call.
  - Why C is incorrect: Dot-sourcing (`. "script.ps1"`) loads a script file
    into the current scope, making its functions and variables available. It has
    nothing to do with parameter passing.
  - Why D is incorrect: Banding is not a PowerShell concept. There is no such
    technique in PowerShell parameter handling.

---

### Question 5

An administrator adds `[Parameter(ValueFromPipeline)]` to a function parameter.
What does this enable?

A) The parameter becomes optional and can be omitted when calling the function.

B) The parameter value can be supplied by objects flowing through the pipeline
   instead of being typed explicitly.

C) The parameter is validated against a list of allowed values at runtime.

D) The parameter is automatically populated from environment variables.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: `ValueFromPipeline` makes the parameter accept pipeline
    input — it does not affect whether the parameter is mandatory or optional.
    A `Mandatory=$true` attribute controls optionality.
  - Why C is incorrect: Validation against a list of allowed values uses the
    `[ValidateSet()]` attribute, not `ValueFromPipeline`.
  - Why D is incorrect: Environment variable population is not controlled by
    parameter attributes. It would require explicit code inside the function
    body using `$env:`.

---

### Question 6

An administrator compiles the following DSC configuration.

```powershell
Configuration WebSetup {
    Node "WebServer01" {
        WindowsFeature IIS {
            Name   = "Web-Server"
            Ensure = "Present"
        }
    }
}
WebSetup -OutputPath "C:\DSC\Web"
```

What file is produced in `C:\DSC\Web`?

A) `WebSetup.mof`

B) `WebServer01.mof`

C) `IIS.mof`

D) `localhost.mof`

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The output MOF file is named after the `Node` value,
    not the `Configuration` name. The configuration name `WebSetup` identifies
    the function, not the output file.
  - Why C is incorrect: `IIS` is the resource instance name within the
    configuration. DSC generates one MOF per node, not per resource.
  - Why D is incorrect: `localhost.mof` would be generated only if the `Node`
    value were `"localhost"`. Since the node is `"WebServer01"`, the file is
    `WebServer01.mof`.

---

### Question 7

An administrator needs a function that accepts input from the pipeline and
processes each object individually. Which function structure is correct?

A) Declare the parameter in the `begin {}` block and process objects in the
   `end {}` block.

B) Declare the parameter with `[Parameter(ValueFromPipeline)]` and place
   processing logic in the `process {}` block.

C) Use the `$input` automatic variable in the function body without a
   `process {}` block.

D) Declare the parameter as `[string[]]` and iterate with `foreach` in the
   function body without pipeline support.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: The `begin {}` block runs once before any pipeline
    objects arrive. Processing objects inside `end {}` would buffer all objects
    and process them only after the pipeline completes, breaking streaming
    behavior.
  - Why C is incorrect: The `$input` automatic variable is available in simple
    functions but also buffers all input rather than streaming. Functions with
    `[CmdletBinding()]` should use the `process {}` block for correct pipeline
    behavior.
  - Why D is incorrect: Declaring a parameter as `[string[]]` allows passing
    an array by value, but it does not accept pipeline input. `ValueFromPipeline`
    on a scalar parameter with a `process {}` block is the correct pattern.

---

### Question 8

What is the primary advantage of DSC over traditional imperative PowerShell
scripts for configuration management?

A) DSC scripts run faster than PowerShell scripts because they are compiled
   to machine code.

B) DSC configurations are declarative — they describe the desired end state,
   and the LCM detects and corrects drift automatically.

C) DSC requires fewer administrator privileges than running PowerShell scripts
   manually.

D) DSC configurations can only be applied to virtual machines, not physical
   servers.

- **Correct Answer:** B
- **Distractor Analysis:**
  - Why A is incorrect: DSC configurations are compiled to MOF files and applied
    by the LCM using PowerShell cmdlets. They are not compiled to machine code
    and do not have a performance advantage over scripts.
  - Why C is incorrect: DSC configurations typically require Administrator
    privileges to apply because they can install features, modify services, and
    change system settings. The privilege requirement is not lower than
    traditional scripts.
  - Why D is incorrect: DSC applies to any Windows Server node — physical or
    virtual. The node type does not restrict DSC applicability.

---

## Question 9

An administrator runs the following command.

```powershell
Get-Counter "\Processor(*)\% Processor Time" |
    Select-Object -ExpandProperty CounterSamples |
    Select-Object InstanceName, CookedValue |
    Sort-Object CookedValue -Descending
```

What does the asterisk `(*)` in the counter path accomplish?

A. It collects the counter for all computers on the network simultaneously

B. It returns the _Total instance only, averaging across all processor cores

C. It returns a separate counter sample for each processor core instance plus
   the _Total aggregate

D. It applies a wildcard filter to return only the top 10 processor instances

Correct Answer: C

Distractor Analysis:

- **A** — The `(*)` is an instance wildcard, not a computer selector. To collect
  from multiple computers, use `-ComputerName` parameter on `Get-Counter`.

- **B** — `(_Total)` is the instance name for the aggregate. Using `(*)` expands
  to all instances including individual cores (0, 1, 2, 3, ...) and `_Total`.

- **C** — Correct. In a performance counter path, `(*)` is an instance wildcard
  that returns all available instances. For `\Processor(*)`, this includes each
  individual core by number and the `_Total` summary instance.

- **D** — `(*)` returns all instances without a numeric limit. There is no
  "top 10" behavior built into the counter path wildcard.

---

## Question 10

An administrator reviews a server health report and sees the following values:

- CPU %: 42
- Available MBytes: 312
- Avg. Disk Queue Length: 0.3
- Processor Queue Length: 0.8
- Pages/sec (average over 10 minutes): 14.2

Which resource is experiencing a bottleneck condition?

A. CPU — processor queue length exceeds the threshold

B. Disk — disk queue length exceeds the threshold

C. Memory — Pages/sec is sustained above 5, indicating excessive paging

D. No bottleneck — all values are within normal operating ranges

Correct Answer: C

Distractor Analysis:

- **A** — Processor Queue Length of 0.8 is well below the threshold of 2 per
  core. CPU at 42% is not a bottleneck condition.

- **B** — Avg. Disk Queue Length of 0.3 is well below the threshold of 2 per
  spindle. The disk is not bottlenecked.

- **C** — Correct. `Pages/sec` sustained above 5 indicates excessive paging —
  the OS is actively moving data between RAM and the page file on disk because
  physical memory is insufficient for the workload. Even though `Available MBytes`
  is 312 (above the 100 MB critical threshold), sustained paging at 14.2 pages
  per second indicates the working set exceeds what fits comfortably in RAM.

- **D** — One value is outside acceptable range: Pages/sec at 14.2 sustained
  over 10 minutes indicates a memory bottleneck via excessive paging. The server
  would benefit from additional RAM.

---

*Submit answers to Canvas by the due date shown in the course schedule.*

---

### Question 11 (5 points)

An administrator needs to monitor `\Processor(_Total)\% Processor Time` once
every 5 seconds for 60 seconds and export the results to a CSV file. Which
PowerShell command accomplishes this?

- A) `Get-Counter "\Processor(_Total)\% Processor Time" -SampleInterval 5 -MaxSamples 12 | Export-Csv "C:\cpu.csv" -NoTypeInformation`
- B) `Get-Counter "\Processor(_Total)\% Processor Time" -SampleInterval 5 -MaxSamples 12 | Select-Object -ExpandProperty CounterSamples | Export-Csv "C:\cpu.csv" -NoTypeInformation`
- C) `Get-Counter "\Processor(_Total)\% Processor Time" -Duration 60 | Export-Counter -Path "C:\cpu.csv"`
- D) `Measure-Command { Get-Counter "\Processor(_Total)\% Processor Time" -SampleInterval 5 } | Export-Csv "C:\cpu.csv"`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Exporting the raw `PerformanceCounterSampleSet` objects (what `Get-Counter` returns) to CSV produces metadata objects, not the individual counter path and value rows. The `CounterSamples` property must be expanded first for useful CSV output.
  - **B** — Correct. `-SampleInterval 5 -MaxSamples 12` collects 12 samples at 5-second intervals (60 seconds total). Expanding `CounterSamples` gives flat objects with `Path`, `CookedValue`, and `Timestamp` properties suitable for CSV export.
  - **C** — `Export-Counter` exports to BLG or CSV format using the Performance Logging service, but `-Duration 60` is not a valid `Get-Counter` parameter. The correct parameter is `-MaxSamples`.
  - **D** — `Measure-Command` measures how long a script block takes to run. It does not capture performance counter values.

---

### Question 12 (5 points)

An administrator is reviewing a performance baseline and notices that
`% Privileged Time` is consistently 35% while `% Processor Time` is 40% on a
server running a database application. What does this ratio indicate?

- A) The database application is using 35% CPU for user-mode processing
- B) The system is spending a disproportionate amount of CPU time in kernel mode, suggesting driver or I/O overhead rather than application processing
- C) 35% of CPU capacity is reserved for the operating system and unavailable to applications
- D) The server has 35% of its cores disabled to save power

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `% Privileged Time` measures CPU in kernel mode (driver calls, system calls, I/O processing), not user-mode application processing. User-mode CPU time is measured by `% User Time`.
  - **B** — Correct. When `% Privileged Time` is close to `% Processor Time`, it means most CPU work is happening in kernel mode — typically due to high disk I/O, network processing, or driver activity. A well-optimized application should have the majority of CPU time in user mode. The 35/40 ratio indicates a kernel-heavy workload, pointing to I/O or driver overhead.
  - **C** — Windows does not statically reserve a percentage of CPU for OS use. Kernel mode CPU is driven by actual system calls and I/O operations.
  - **D** — CPU core disablement is managed in BIOS/power settings and does not appear in `% Privileged Time` metrics.

---

### Question 13 (5 points)

A DSC configuration uses the `File` resource to ensure a configuration file
exists at `C:\App\config.ini`. The LCM `ConfigurationMode` is set to
`ApplyAndAutoCorrect`. An application deletes `config.ini` during an error
condition. What does the LCM do?

- A) Nothing — the LCM only monitors during the initial application
- B) Logs the drift in the event log but takes no action until the next manual push
- C) At the next consistency check interval, detects the missing file and restores it
- D) Terminates the application that deleted the file

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — `ApplyOnly` would take no action after initial application. `ApplyAndAutoCorrect` continuously monitors and corrects drift.
  - **B** — `ApplyAndMonitor` logs drift without correcting it. `ApplyAndAutoCorrect` goes further and automatically re-applies the configuration to correct the drift.
  - **C** — Correct. `ApplyAndAutoCorrect` causes the LCM to run consistency checks at the `RefreshFrequencyMins` interval (default 30 minutes). When it detects that `config.ini` is missing, it uses the `File` resource to restore the file to its desired state.
  - **D** — DSC does not monitor or terminate processes. It manages resource states (file presence, service status, registry values) but has no visibility into which process caused a state change.

---

### Question 14 (5 points)

An administrator splatted parameters to `New-ADUser` as follows:

```powershell
$params = @{
    Name              = "Alice Johnson"
    SamAccountName    = "ajohnson"
    UserPrincipalName = "ajohnson@txwes.edu"
    Enabled           = $true
}
New-ADUser @params
```

What does the `@params` syntax do when calling `New-ADUser`?

- A) Passes `$params` as a single hashtable argument to a `-Parameters` parameter
- B) Expands the hashtable keys as parameter names and values as parameter values, equivalent to typing each `-Key Value` pair explicitly
- C) Converts the hashtable to a JSON string and passes it as a single string argument
- D) Passes `$params` by reference so `New-ADUser` can modify the hashtable

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — There is no `-Parameters` parameter on `New-ADUser`. Splatting is not passing a hashtable argument; it is expanding the hashtable into individual named parameters.
  - **B** — Correct. Splatting with `@params` expands the hashtable so PowerShell treats it as if the administrator had typed `-Name "Alice Johnson" -SamAccountName "ajohnson" -UserPrincipalName "ajohnson@txwes.edu" -Enabled $true`. This improves readability for cmdlets with many parameters.
  - **C** — Splatting does not serialize to JSON. The values are passed as their original .NET types.
  - **D** — PowerShell does not have pass-by-reference semantics for hashtables in the way C does. Splatting is purely a parameter expansion mechanism.

---

### Question 15 (5 points)

An administrator writes a DSC configuration that must install IIS, then create
a website directory, then start the W3SVC service. Which DSC property chain
enforces this order?

- A) The `DependsOn` property on the directory resource references the IIS feature; the `DependsOn` property on the service resource references the directory resource
- B) The resources are listed in order in the configuration block and DSC executes them sequentially
- C) The `RunOrder` property is set to 1, 2, 3 on each resource respectively
- D) The `Requires` property on each resource specifies the previous resource name

- **Correct Answer: A**
- **Distractor Analysis:**
  - **A** — Correct. `DependsOn` chains resources. The directory resource includes `DependsOn = "[WindowsFeature]IIS"` ensuring IIS installs first. The service resource includes `DependsOn = "[File]WebDir"` ensuring the directory exists before the service starts. DSC resolves the dependency graph before applying resources.
  - **B** — DSC is declarative, not sequential. The order of resource blocks in a configuration does not guarantee execution order. `DependsOn` is required to enforce dependencies.
  - **C** — `RunOrder` is not a DSC resource property. DSC uses `DependsOn` for dependency management.
  - **D** — `Requires` is not a valid DSC resource property. The correct property is `DependsOn`.

---

### Question 16 (5 points)

An administrator uses `Get-Counter` to collect memory performance data and wants
to check if available memory is below 200 MB in the sample results. Which
PowerShell expression evaluates the collected sample correctly?

- A) `(Get-Counter "\Memory\Available MBytes").CookedValue -lt 200`
- B) `(Get-Counter "\Memory\Available MBytes").CounterSamples[0].CookedValue -lt 200`
- C) `(Get-Counter "\Memory\Available MBytes").Value -lt 200`
- D) `Get-Counter "\Memory\Available MBytes" | Where-Object {$_ -lt 200}`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Get-Counter` returns a `PerformanceCounterSampleSet` object. The `CookedValue` property does not exist directly on the sample set; it exists on each individual `CounterSample` within the `CounterSamples` collection.
  - **B** — Correct. `CounterSamples[0].CookedValue` accesses the first (and in this single-counter case, only) counter sample and its numeric value. This can then be compared to the threshold of 200.
  - **C** — `Value` is not a property of the `PerformanceCounterSampleSet` object. The numeric metric is accessed via `CounterSamples[0].CookedValue`.
  - **D** — `Get-Counter` returns a sample set object, not a numeric value. Piping to `Where-Object {$_ -lt 200}` compares a complex object to 200, which produces a false result since objects are never less than integers.

---

### Question 17 (5 points)

An administrator wants to create a Custom View in Event Viewer that shows only
Critical and Error events from the System and Application logs in the last 24
hours. How does a Custom View differ from using Filter Current Log?

- A) Custom Views apply permanently to all event logs; Filter Current Log applies only to the current view
- B) Custom Views are saved in the Event Viewer navigation tree and persist between sessions; Filter Current Log is temporary and lost when Event Viewer closes
- C) Custom Views can filter on Event IDs but Filter Current Log can only filter on severity
- D) Filter Current Log is faster because it queries the log locally; Custom Views query the domain controller

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — Both Custom Views and Filter Current Log can span multiple logs. The distinction is persistence, not scope.
  - **B** — Correct. The key difference is persistence. A Custom View is saved in Event Viewer's navigation tree under Custom Views and remains available across Event Viewer sessions. Filter Current Log applies a temporary filter that disappears when the view is changed or Event Viewer is closed.
  - **C** — Both Filter Current Log and Custom Views support filtering by Event ID, source, level, and time range. There is no functional difference in filtering capabilities.
  - **D** — Both tools query the local event log. Neither queries a domain controller for event data.

---

### Question 18 (5 points)

A DSC configuration is compiled with `Node "localhost"`. The resulting MOF file
is pushed to the local server using `Start-DscConfiguration`. The LCM is set to
`RefreshMode = "Push"`. When does the LCM next apply the configuration?

- A) Only when an administrator manually runs `Start-DscConfiguration` again
- B) Every 15 minutes automatically, as that is the Push mode default interval
- C) At the `RefreshFrequencyMins` interval for consistency checks, but Push mode only delivers new configurations on manual push
- D) Never — Push mode applies configurations only once

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — In Push mode, new configurations are delivered manually. However, the LCM in `ApplyAndMonitor` or `ApplyAndAutoCorrect` mode still runs consistency checks at the `RefreshFrequencyMins` interval (default 30 minutes) to detect and optionally correct drift.
  - **B** — Push mode does not automatically pull or reapply configurations on an interval. The 15-minute interval is not accurate; the LCM default consistency check is 30 minutes.
  - **C** — Correct. Push mode means configurations are delivered by an administrator running `Start-DscConfiguration`. The LCM's consistency check (`RefreshFrequencyMins`) still runs on schedule to check for and correct drift if `ApplyAndAutoCorrect` is set. New configurations, however, are only applied when pushed manually.
  - **D** — DSC LCM in `ApplyAndAutoCorrect` mode continues to run consistency checks and apply corrections indefinitely. It is not a one-time application.

---

### Question 19 (5 points)

An administrator wants to identify which process on a server is causing high disk
I/O, specifically which files are being written to most frequently. Which Windows
monitoring tool provides per-process disk write activity at the file level?

- A) Task Manager — Processes tab
- B) Performance Monitor — `\PhysicalDisk(_Total)\Disk Writes/sec`
- C) Resource Monitor — Disk tab, showing per-process disk write activity
- D) Event Viewer — System log filtered for disk write events

- **Correct Answer: C**
- **Distractor Analysis:**
  - **A** — Task Manager's Processes tab shows aggregate disk I/O per process (read + write combined in bytes per second) but does not show file-level detail or separate read/write activity.
  - **B** — Performance Monitor's `\PhysicalDisk\Disk Writes/sec` shows total disk write rate but does not identify which process or files are responsible.
  - **C** — Correct. Resource Monitor's Disk tab shows per-process disk activity including which specific files are being read and written, the read/write rate in bytes per second, and the total I/O for each process. This is the correct tool for diagnosing per-process disk I/O at the file level.
  - **D** — Event Viewer's System log does not record individual file write operations. Disk-related events in the System log are typically errors or warnings from storage drivers, not performance-level write activity tracking.

---

### Question 20 (5 points)

An administrator runs the following command to verify that a DSC-managed server
is in compliance:

```powershell
Get-DscConfigurationStatus
```

The output shows `Status: Failure` and `ResourcesNotInDesiredState` with one
entry. What is the correct next step to force a re-application of the
configuration?

- A) `Push-DscConfiguration -Wait`
- B) `Start-DscConfiguration -UseExisting -Wait -Verbose`
- C) `Restore-DscConfiguration -ComputerName localhost`
- D) `Set-DscLocalConfigurationManager -ConfigurationMode ApplyAndAutoCorrect`

- **Correct Answer: B**
- **Distractor Analysis:**
  - **A** — `Push-DscConfiguration` is not a valid DSC cmdlet. Configurations are pushed using `Start-DscConfiguration` with the MOF path or `-UseExisting`.
  - **B** — Correct. `Start-DscConfiguration -UseExisting -Wait -Verbose` re-applies the currently stored MOF configuration on the node without requiring the MOF file to be re-pushed. `-UseExisting` uses the MOF already in `C:\Windows\System32\Configuration`. `-Wait` blocks until complete; `-Verbose` shows resource-level detail.
  - **C** — `Restore-DscConfiguration` is not a valid built-in DSC cmdlet. There is no standard restore command; re-application is done with `Start-DscConfiguration`.
  - **D** — `Set-DscLocalConfigurationManager` changes the LCM settings (mode, refresh interval, etc.) but does not immediately re-apply the current configuration. It would take effect on the next consistency check cycle.

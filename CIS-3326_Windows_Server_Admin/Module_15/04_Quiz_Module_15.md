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

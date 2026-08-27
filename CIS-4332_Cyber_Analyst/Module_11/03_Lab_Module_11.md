# Lab Activity: Module 11 — Incident Response for Analysts

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

In this lab you will simulate the analyst's role during the Detection and Analysis phase of a security incident. You will receive a set of SIEM alerts and supporting log data, perform triage to classify severity, scope the incident across multiple evidence sources, extract Indicators of Compromise, and produce an incident documentation record.

This lab mirrors real-world Tier 1 and Tier 2 analyst workflows and maps directly to CySA+ exam objective 4.2 (apply the appropriate incident response procedure given a scenario).

**Estimated Time:** 90–120 minutes

**Tools Required:** Text editor or word processor, provided log data files (in Canvas), MITRE ATT&CK Navigator (free at attack.mitre.org)

---

## Learning Objectives

Upon completing this lab you will be able to:

- Perform structured triage on a security alert using the NIST severity framework
- Scope an incident across host, network, and identity evidence
- Extract and document Indicators of Compromise in standard format
- Produce an incident timeline and documentation record
- Map observed behaviors to MITRE ATT&CK techniques

---

## Scenario Background

Your organization is a regional financial services firm. You are the on-call Tier 2 analyst. At 22:14 UTC your SIEM generates three correlated alerts:

- **Alert 1** — Endpoint Detection: Suspicious PowerShell execution on workstation WS-FINANCE-047, user account `jsmith@corp.local`, at 22:09 UTC
- **Alert 2** — Network: Outbound connection from WS-FINANCE-047 to 185.220.101.47 port 443, sustained for 14 minutes, at 22:10 UTC
- **Alert 3** — Authentication: Failed RDP login attempts against four internal servers (DC-PROD-01, FS-PROD-02, APP-PROD-03, HR-PROD-04) from WS-FINANCE-047, at 22:11 UTC

The SIEM correlation rule that fired is titled "Possible C2 Beaconing + Lateral Movement Probe."

---

## Part 1 — Initial Triage

### Step 1.1 — Classify the Alert

Using the NIST SP 800-61 severity framework, classify this potential incident.

Answer the following in your lab report:

1. What is the **functional impact**? Choose: None / Minimal / Significant / Severe. Justify your choice.
2. What is the **information impact**? Choose: None / Privacy Breach / Proprietary Breach / Integrity Loss. Justify your choice.
3. What is the **recoverability**? Choose: Regular / Supplemented / Extended / Not Recoverable. Justify your choice based on what you currently know.
4. Is this a true positive, false positive, or benign true positive? State your initial assessment and the evidence that supports it.

### Step 1.2 — Establish a Triage Timeline

Document the following timestamps in your lab report in a timeline table:

- Time the first alert fired
- Time you (the analyst) began triage (use the current time of your lab session)
- Estimated triage completion time

Calculate the gap between alert fire time and analyst triage start. This is your contribution to MTTD/MTTR metrics.

---

## Part 2 — Evidence Collection and Scoping

Review the following evidence snippets (provided in your Canvas lab data file). For this printed lab guide the data is represented as structured descriptions.

### Step 2.1 — Endpoint Evidence

The EDR console shows the following process execution chain on WS-FINANCE-047 at 22:09 UTC:

```text
explorer.exe (PID 1284)
  └── powershell.exe -enc JABjAGwAaQBlAG4AdAA... (PID 4412)
        └── cmd.exe /c whoami /all (PID 4413)
        └── cmd.exe /c net user /domain (PID 4414)
        └── cmd.exe /c net group "Domain Admins" /domain (PID 4415)
```

Answer in your lab report:

1. What technique does the base64-encoded PowerShell parameter suggest? (Reference MITRE ATT&CK T1059.001)
2. What do the three child cmd.exe commands suggest the attacker is attempting to do? Name the ATT&CK tactic.
3. Is the user account `jsmith@corp.local` likely the attacker, or is the account likely compromised? State your reasoning.

### Step 2.2 — Network Evidence

Firewall logs show the following outbound connection:

```text
Source IP:        10.0.4.47 (WS-FINANCE-047)
Destination IP:   185.220.101.47
Destination Port: 443
Protocol:         TCP
Bytes Out:        2,841
Bytes In:         847,492
Duration:         14m 22s
Start:            22:10:07 UTC
End:              22:24:29 UTC
```

Threat intelligence lookup of 185.220.101.47 returns: "Known Tor exit node. Previously observed in C2 communications for multiple commodity RAT families."

Answer in your lab report:

1. Does the bytes-in to bytes-out ratio suggest a download, an upload, or command-and-control traffic? Explain.
2. What does the connection to a known Tor exit node indicate about the nature of this traffic?
3. Map this network behavior to the appropriate MITRE ATT&CK technique (hint: look at Command and Control, T1071 or T1090).

### Step 2.3 — Identity and Authentication Evidence

Active Directory logs from DC-PROD-01 show:

```text
22:11:03 UTC — Failed RDP login: jsmith@corp.local from 10.0.4.47 to DC-PROD-01  (10.0.1.10)
22:11:05 UTC — Failed RDP login: jsmith@corp.local from 10.0.4.47 to FS-PROD-02  (10.0.1.11)
22:11:07 UTC — Failed RDP login: jsmith@corp.local from 10.0.4.47 to APP-PROD-03 (10.0.1.12)
22:11:09 UTC — Failed RDP login: jsmith@corp.local from 10.0.4.47 to HR-PROD-04  (10.0.1.13)
22:11:12 UTC — Successful RDP login: jsmith@corp.local from 10.0.4.47 to HR-PROD-04 (10.0.1.13)
```

Answer in your lab report:

1. What attack technique do the rapid failed logins followed by a success suggest? (Reference T1110)
2. Which system is now confirmed compromised in addition to WS-FINANCE-047?
3. What data may be at risk given the system that was successfully accessed?

---

## Part 3 — IoC Extraction and Documentation

### Step 3.1 — Extract and Document IoCs

Create an IoC table in your lab report with the following columns: IoC Type, Value, Confidence (High/Med/Low), Source Evidence.

You must document at minimum:

- The attacker-controlled external IP address
- The suspicious process name and command-line argument indicator
- The compromised user account
- The two confirmed compromised internal hostnames
- The ATT&CK technique IDs associated with this incident (minimum three)

### Step 3.2 — Produce the Incident Timeline

Create a chronological timeline table with columns: Timestamp (UTC), Event Description, Source/Evidence.

Your timeline must cover all events from 22:09 UTC through the point where you completed triage.

---

## Part 4 — Containment Recommendation

Based on your triage findings, write a containment recommendation memo (150–200 words) addressed to the on-call IR Team Lead. Your memo must include:

- A one-sentence incident summary
- The confirmed scope (systems and accounts)
- Your recommended immediate containment actions (be specific — name the systems and accounts)
- Any evidence preservation considerations that should guide the containment approach
- Your recommended escalation priority level (P1 Critical / P2 High / P3 Medium / P4 Low) with justification

---

## Part 5 — Reflection Questions

Answer the following in your lab report (3–5 sentences each):

1. If you had performed only basic triage on Alert 1 without investigating Alerts 2 and 3, what would you have missed about the incident scope?
2. The successful RDP login to HR-PROD-04 occurred only 2 minutes after the initial PowerShell execution. What does this timing suggest about the attacker's capability and preparation?
3. This incident involved both endpoint and network indicators. Which evidence source would you preserve first if you could only choose one before containment? Justify your answer.

---

## Deliverables

Submit the following to Canvas as a single PDF document:

1. Part 1 — Triage classification answers and timeline
2. Part 2 — All evidence analysis answers (2.1, 2.2, 2.3)
3. Part 3 — IoC table and incident timeline
4. Part 4 — Containment recommendation memo
5. Part 5 — Reflection question answers

**Grading:** 100 points total. Each part is worth 20 points. Accuracy, completeness, and use of correct IR terminology are evaluated.

---

## Submission

Upload your completed lab report PDF to the Module 11 Lab assignment in Canvas by the due date shown in the course schedule. Late submissions are subject to the course late policy.

---

## Part 9 — Challenge Exercise

### Challenge 1: Incident Severity Escalation Triage

At 08:14 AM on a Monday, a Tier 1 analyst receives three alerts simultaneously: (A) successful login to Office 365 admin portal from an IP in Eastern Europe for an account whose last login was from Texas 3 hours ago; (B) 47 failed SSH attempts followed by a successful login to a DMZ web server from the same Eastern European IP; (C) EDR alert on `PAYROLL-SRV-01` for `mimikatz.exe` execution at 07:58 AM.

1. Classify each alert as Low, Medium, High, or Critical and justify your severity rating for each using at least two contributing factors.
2. Determine whether all three alerts are likely part of the same incident chain or separate incidents. Support your conclusion with specific indicators.
3. Write a 90-second verbal handoff script for the Tier 1-to-Tier-2 escalation covering all three alerts, in the format: what happened, what evidence exists, what immediate containment you recommend, and what the Tier 2 analyst should investigate first.

### Challenge 2: Post-Incident Action Items

The same incident from Challenge 1 concluded with the following confirmed findings: the attacker used compromised O365 credentials (acquired via phishing 6 days prior) to access email, used an email rule to forward all messages to an external address, pivoted to the DMZ server via exposed SSH, used that access to reach PAYROLL-SRV-01 via a trust relationship, and ran Mimikatz to dump credentials — but did not exfiltrate payroll data. The incident was detected 6 days after initial access (dwell time: 6 days).

1. Write three specific, actionable lessons-learned items. For each, specify: the detection or process gap it addresses, the recommended control or improvement, and which NIST IR phase it improves.
2. Calculate the blast radius: if Mimikatz successfully dumped all domain credentials from PAYROLL-SRV-01's memory, list every remediation action required in the correct priority order.
3. Identify which regulatory notification requirement (if any) is triggered by the email forwarding rule alone — even if payroll data was not exfiltrated.

### Reflection Questions

1. The six-day dwell time was only discovered because an EDR alert fired on Day 6. What proactive activity would most likely have reduced the dwell time, and which IR phase governs that capability?
2. Explain why the NIST IR phases are described as iterative rather than strictly sequential, using a specific example from this incident where returning to a previous phase was necessary.

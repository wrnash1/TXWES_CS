# Video Script: Module 15 — Advanced Threat Hunting

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Slide 1 — Introduction

Welcome to Module 15: Advanced Threat Hunting. I am Professor Nash.

We have covered reactive security — triage, incident response, and forensics. We have covered proactive defense — vulnerability management and compliance. In this module we cover proactive offense: going out to find attackers who are already in your environment before they trigger an alert.

Threat hunting is the practice of proactively searching through an organization's environment for signs of malicious activity that has evaded automated detection. It is hypothesis-driven, analyst-led, and built on the premise that determined adversaries will eventually bypass your automated defenses.

---

## Slide 2 — Why Threat Hunting Exists

Automated detection is reactive. SIEM rules fire when an event matches a known pattern. EDR alerts fire when behavior matches a known signature or heuristic. Both approaches have a fundamental weakness: they only catch what they know to look for.

Advanced adversaries deliberately craft their techniques to stay below detection thresholds, use legitimate tools, and blend into normal network traffic. They can maintain persistent access for weeks or months before automated detection fires.

The average time between initial compromise and detection — called dwell time — has historically been measured in months. Threat hunting directly attacks dwell time by putting human analysts actively searching for hidden threats in the environment.

---

## Slide 3 — The Hunting Loop

Threat hunting follows an iterative cycle called the hunting loop:

Step one: form a hypothesis. Based on threat intelligence, recent CVEs, known adversary TTPs, or analytical intuition, the hunter asks "what if an attacker is doing X in our environment right now?"

Step two: investigate. Use available telemetry — endpoint logs, network logs, authentication logs — to search for evidence that would confirm or refute the hypothesis.

Step three: uncover new patterns and TTPs. Whether or not the hunt confirms the hypothesis, the analysis reveals something new about the environment.

Step four: inform and improve. Findings inform detection engineering. New SIEM rules, EDR policies, and playbooks are created based on what the hunt discovered.

Then the loop begins again with a new hypothesis.

---

## Slide 4 — Hypothesis Development

A threat hunting hypothesis is a specific, testable statement about attacker activity. A vague hypothesis leads to unfocused hunting. A specific hypothesis leads to targeted investigation.

Weak hypothesis: "Let us look for malware."

Strong hypothesis: "Based on recent threat intelligence indicating that TA505 is targeting financial sector organizations with macro-enabled Excel files that spawn PowerShell to download Cobalt Strike beacons, we hypothesize that if this group has targeted our organization, we will see Excel spawning PowerShell with encoded command-line arguments in endpoint telemetry from our finance department workstations in the past 30 days."

Strong hypotheses are time-bounded, specific about the expected indicator, and tied to a credible threat source.

---

## Slide 5 — Sources for Hypothesis Generation

Effective hunters develop hypotheses from multiple sources.

Threat intelligence reports from ISACs, commercial feeds, and government advisories describe active threat actor campaigns, targeted industries, and specific TTPs.

MITRE ATT&CK provides a structured catalog of adversary techniques organized by tactic. Hunters can select specific techniques relevant to their environment and threat landscape and build hypotheses around detecting them.

Recent CVE publications and active exploitation reports identify techniques attackers are currently using against unpatched systems.

Peer organization sharing — conversations with other security teams about what they are seeing — often provides the most timely and relevant hypothesis seeds.

Internal anomaly data from SIEM, UEBA, and EDR platforms can surface unusual patterns that do not rise to alert thresholds but are worth investigating.

---

## Slide 6 — MITRE ATT&CK for Hunting

MITRE ATT&CK is the most important structured knowledge base for threat hunters. It catalogs adversary behaviors across the full attack lifecycle, organized into tactics (the why) and techniques (the how).

The ATT&CK Enterprise matrix covers 14 tactics:

- Reconnaissance, Resource Development, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact

Each tactic contains multiple techniques. For example, Execution contains techniques like PowerShell (T1059.001), Windows Management Instrumentation (T1047), and Scheduled Task/Job (T1053).

For each technique, ATT&CK provides: a description of how the technique works, procedure examples from real threat actors, data sources that would capture the activity, and detection guidance.

Hunters use ATT&CK to pick a technique, understand what evidence it leaves, and then search for that evidence in their telemetry.

---

## Slide 7 — Endpoint Telemetry

Endpoint telemetry is the primary data source for most threat hunts. Endpoint Detection and Response (EDR) platforms collect rich, high-fidelity data from every managed endpoint.

Key endpoint telemetry types:

Process creation events — every process that starts, including its parent, command-line arguments, and file hash.

Network connection events — every outbound and inbound connection a process makes, with process name and PID.

File creation and modification events — every file written to disk, including executable drops.

Registry modification events — every registry key created or modified, including persistence-relevant keys.

Module load events — every DLL loaded by every process, enabling detection of DLL hijacking and side-loading.

User account and authentication events — logons, privilege escalations, and new account creation.

---

## Slide 8 — EDR and XDR Platforms

EDR platforms provide endpoint telemetry collection and local detection capability. Leading EDR platforms include CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, and Carbon Black.

XDR (Extended Detection and Response) expands EDR by integrating telemetry from endpoints, networks, email, cloud environments, and identity systems into a unified detection and hunting platform.

For threat hunting, EDR and XDR platforms offer:

- Query interfaces for hunting across endpoint telemetry (CrowdStrike's RTR, Microsoft's Advanced Hunting, SentinelOne's Deep Visibility)
- Process tree visualization showing parent-child relationships
- Timeline views showing all activity on a host over a time period
- File and hash analysis with threat intelligence correlation
- Lateral movement tracking across multiple endpoints

---

## Slide 9 — Structured Query Languages for Hunting

Modern EDR and XDR platforms use SQL-like query languages for threat hunting.

Microsoft Defender Advanced Hunting uses Kusto Query Language (KQL):

```kql
DeviceProcessEvents
| where FileName == "powershell.exe"
| where ProcessCommandLine contains "-EncodedCommand"
| where InitiatingProcessFileName in ("WINWORD.EXE", "EXCEL.EXE")
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessFileName
```

This query finds PowerShell processes launched by Office applications with encoded command lines — a classic macro malware execution pattern.

CrowdStrike uses its own query language in Event Search. Splunk hunters use SPL. Understanding the concepts is transferable across platforms even if the exact syntax differs.

---

## Slide 10 — Hunting Workflow Example

Let us walk through a complete hunting workflow.

Hypothesis: Based on CISA advisory AA24-038A warning of LockBit ransomware operators using AnyDesk for remote access persistence after initial compromise, we hypothesize that if LockBit has accessed our environment, AnyDesk may be installed and running on systems where it was not previously present.

Investigation: Query EDR telemetry for AnyDesk process creation events in the past 60 days. Cross-reference against the IT-approved software list. Filter for instances where AnyDesk was running on endpoints not in the approved remote access exception list.

Finding: Three endpoints in the warehouse management network show AnyDesk installations from 23 days ago that are not in the approved software list and were not installed through the standard software deployment mechanism.

Outcome: Escalate to IR team. Three hunts confirmed legitimate installs after investigation, one confirmed unauthorized — turned out to be IT shadow IT, not LockBit. New detection rule created for unauthorized remote access software installation.

---

## Slide 11 — Network-Based Hunting

While endpoint telemetry is the richest data source for hunting, network data provides visibility for devices without EDR agents — IoT, OT systems, network appliances, and unmanaged devices.

Network hunting techniques include:

Hunting for beaconing behavior — regular, clock-like outbound connections to external hosts indicating C2 check-in.

Hunting for DNS anomalies — high-volume queries to rare domains, long subdomain strings, or DNS queries that resolve to recently registered domains.

Hunting for protocol misuse — HTTP traffic with non-standard User-Agent strings, HTTPS to IP addresses without domain names, or protocols on non-standard ports.

Hunting for data staging — unusually large internal file share access prior to an exfiltration event.

---

## Slide 12 — Documenting Hunt Results

Every hunt produces a documented record regardless of outcome. A hunt that finds nothing is not a wasted hunt — it establishes a baseline and confirms the hypothesis was tested.

A hunt documentation record includes:

- Hunt title and date
- Hypothesis and threat intelligence source
- Data sources queried and time range covered
- Query or search methodology used
- Findings — positive or negative
- New detection rules or logic created from the hunt
- Recommendations for future hunts or control improvements

Hunt documentation feeds the detection engineering backlog. Over time, a library of hunt documentation records becomes the organization's threat knowledge base.

---

## Slide 13 — Hunting Maturity

Hunting programs mature through recognizable stages.

Initial maturity: ad-hoc hunting by senior analysts following major incidents or threat intelligence reports.

Developing maturity: scheduled hunt cycles, basic documentation, initial MITRE ATT&CK coverage mapping.

Mature: hypothesis library, regular hunt cadence, detection engineering integration, coverage metrics tracked against ATT&CK.

Advanced maturity: automated hunt triggers based on new threat intelligence, hunting integrated into SOAR, coverage measured and reported to leadership.

---

## Slide 14 — CySA+ Exam Connection

For the CySA+ CS0-003 exam, threat hunting concepts appear in Domain 1 (Security Operations). Focus on:

- The hunting loop as an iterative process
- MITRE ATT&CK as the primary structured resource for hunting hypotheses
- Endpoint telemetry types and their sources
- EDR and XDR as the primary hunting platforms
- The difference between reactive detection and proactive hunting
- Hunt documentation as a required professional output

Exam questions will present hunting scenarios and ask which hypothesis, data source, or technique is most appropriate for a given threat or environment.

---

## Slide 15 — Summary

Module 15 covered advanced threat hunting from hypothesis development through investigation, findings, and documentation. We examined MITRE ATT&CK as the structured framework that enables systematic coverage of adversary techniques. We explored endpoint telemetry and EDR/XDR platforms as the primary hunting infrastructure. We walked through a complete hunting workflow and discussed how hunts improve detection engineering over time.

---

## Slide 16 — Looking Ahead

Module 16 is our final module: CySA+ CS0-003 Exam Preparation and Capstone. We will review all exam domains, practice with 20 exam-style questions, and discuss exam strategy. Everything you have learned in Modules 1 through 15 will come together here.

Complete all Module 15 activities before our final session.

---

End of Module 15 Video Script — 225 lines

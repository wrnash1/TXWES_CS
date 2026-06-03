# Lab Activity: Module 15 — Advanced Threat Hunting

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Lab Overview

This lab develops structured threat hunting skills through two exercises: a guided hunt using provided endpoint telemetry, and an independent hunt plan development exercise. You will form hypotheses, execute targeted searches, analyze findings, and produce professional hunt documentation.

**Estimated Time:** 2–3 hours

**Tools Required:** ATT&CK Navigator (free at mitre-attack.github.io/attack-navigator), spreadsheet application, text editor or word processor, provided lab data files from Canvas Module 15 Lab folder.

**Lab Files (download from Canvas):**

- `lab15_process_events.csv` — 72-hour endpoint telemetry export (process creation events)
- `lab15_network_events.csv` — 72-hour network connection log (process-correlated)
- `lab15_dns_queries.csv` — 72-hour DNS query log

---

## Scenario Context

Your organization is a mid-size logistics company. A threat intelligence report published two days ago indicates that a financially motivated threat actor group designated TA-FREIGHT has been targeting logistics companies in North America using the following attack chain:

1. Initial access via phishing emails with macro-enabled Excel attachments
2. Excel spawns PowerShell with a base64-encoded download cradle to retrieve a Cobalt Strike beacon
3. Cobalt Strike establishes HTTPS C2 to actor-controlled infrastructure
4. Discovery commands run within 30 minutes of execution
5. Lateral movement using stolen credentials via RDP within 4 hours
6. Data staged to a local folder before exfiltration

---

## Part 1 — Hypothesis Development

### Step 1.1 — Primary Hunt Hypothesis

Using the threat intelligence report and the strong hypothesis structure from the reading guide, write a complete hunt hypothesis for this threat. Your hypothesis must:

- Reference the specific threat actor (TA-FREIGHT)
- Identify the specific ATT&CK technique(s) you will hunt for
- Specify the expected telemetry indicator
- Specify the data source you will use
- Include a time boundary

Write your hypothesis in your lab report before proceeding.

### Step 1.2 — ATT&CK Technique Mapping

In your lab report, create a table mapping each stage of the TA-FREIGHT attack chain to the corresponding MITRE ATT&CK technique ID and name. Your table must have columns: Attack Stage, ATT&CK Technique ID, Technique Name, Expected Observable Evidence.

You must map all six stages of the attack chain described above.

---

## Part 2 — Guided Hunt: Endpoint Telemetry

Open `lab15_process_events.csv`. The file contains the following columns: Timestamp, Hostname, ParentProcess, ParentPID, ChildProcess, ChildPID, CommandLine, FileHash.

### Step 2.1 — Hunt for Excel Spawning PowerShell

Filter the process events for rows where ParentProcess contains `EXCEL.EXE` and ChildProcess contains `powershell.exe`.

In your lab report:

1. How many such events exist in the 72-hour window?
2. For each event found, record the Timestamp, Hostname, and the first 100 characters of the CommandLine column.
3. Does the CommandLine contain base64-encoded content? How do you recognize base64 encoding in a PowerShell argument?

### Step 2.2 — Analyze Discovery Commands

For each Hostname identified in Step 2.1, filter for any child processes of `powershell.exe` or `cmd.exe` in the 60 minutes following the initial PowerShell execution.

In your lab report:

1. What discovery commands (whoami, net user, ipconfig, nltest, net group, etc.) appear in the CommandLine column within this window?
2. Map each discovery command to the relevant MITRE ATT&CK Discovery sub-technique.
3. Does the timing and sequence of these commands suggest manual attacker interaction or automated scripted execution? Justify your assessment.

### Step 2.3 — Hunt for Lateral Movement

Filter `lab15_process_events.csv` for RDP-related process activity (look for `mstsc.exe` in the ChildProcess column) on the same hostnames, in the 4-hour window following the discovery phase.

Also filter for authentication-related processes that might indicate pass-the-hash or credential use: `lsass.exe` access, `sekurlsa` in CommandLine strings, or `mimikatz` in FileHash lookups.

In your lab report:

1. Were any lateral movement indicators found?
2. If yes, which hostnames are new targets beyond the initially compromised system?
3. Assess the confidence level of your lateral movement finding: High / Medium / Low. Justify.

---

## Part 3 — Network Corroboration

Open `lab15_network_events.csv`. Columns: Timestamp, Hostname, ProcessName, DestinationIP, DestinationPort, Protocol, BytesOut, BytesIn, Duration.

### Step 3.1 — Identify C2 Connections

Filter for network events where ProcessName contains `powershell.exe` and DestinationPort is 443.

In your lab report:

1. List all external destination IPs connected to by PowerShell processes on the affected hostnames.
2. For each connection, record the BytesIn, BytesOut, and Duration values.
3. What does the BytesIn-to-BytesOut ratio suggest about the nature of these connections?

### Step 3.2 — Beaconing Analysis

For the top destination IP from Step 3.1, extract all connections to that IP regardless of process name over the 72-hour window.

Calculate the interval between consecutive connections (time of connection N+1 minus time of connection N).

In your lab report:

1. What is the mean and standard deviation of the connection intervals?
2. Does this pattern meet the criteria for beaconing? (Consistent intervals, low standard deviation)
3. Map this behavior to the appropriate MITRE ATT&CK technique ID.

### Step 3.3 — DNS Anomaly Hunt

Open `lab15_dns_queries.csv`. Columns: Timestamp, Hostname, QueryName, QueryType, ResponseCode, ResponseIP.

Filter for queries from the affected hostnames that resulted in successful resolution (ResponseCode = NOERROR) to domains not ending in `.com`, `.net`, `.org`, or `.gov`.

Also flag any QueryName where the subdomain portion (the text before the first dot-separated TLD) is longer than 30 characters.

In your lab report:

1. List any suspicious DNS queries found.
2. For each suspicious query, assess whether it indicates DGA activity or DNS tunneling. Justify.

---

## Part 4 — Hunt Documentation

Using your findings from Parts 1–3, produce a complete hunt documentation record in your lab report. Your record must include all required sections from the reading guide:

1. Hunt title and unique identifier (use format: HUNT-2024-L15-001)
2. Hunt date, analyst name, and estimated time spent
3. Hypothesis (from Step 1.1)
4. ATT&CK technique mapping (from Step 1.2)
5. Data sources queried, tools used, and time range covered
6. Exact queries or filters used (be specific — list the column filters you applied)
7. Findings with supporting evidence for each finding
8. IoCs identified (IPs, domains, file hashes, hostnames)
9. New detection rules recommended based on findings (at minimum two specific rule descriptions)
10. Recommendations for follow-up hunts or IR escalation

---

## Part 5 — Independent Hunt Plan

Based on your findings in this lab, develop a hunt plan for a follow-on hunt that a colleague could execute next week.

Your hunt plan must include:

1. A new hypothesis addressing a stage of the TA-FREIGHT attack chain that your initial hunt did not fully cover
2. The data sources required for the hunt
3. The specific queries or filters that would be applied
4. The success criteria — what would confirm the hypothesis
5. The failure criteria — what would refute the hypothesis and what that would mean

---

## Deliverables

Submit a single PDF to Canvas containing:

1. Part 1 — Hypothesis and ATT&CK mapping table
2. Part 2 — Endpoint telemetry hunt findings (Steps 2.1–2.3)
3. Part 3 — Network corroboration findings (Steps 3.1–3.3)
4. Part 4 — Complete hunt documentation record
5. Part 5 — Independent hunt plan

**Grading:** 100 points total. Parts 1 and 4 are worth 25 points each. Parts 2, 3, and 5 are worth 17 points each (rounding to 101 — Part 5 is worth 16 points to sum to 100).

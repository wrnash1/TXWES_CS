# Reading Guide: Module 15 — Advanced Threat Hunting

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4332 &BULL; CYBERSECURITY ANALYST & THREAT HUNTING</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Introduction

Module 15 covers one of the highest-skill disciplines in security operations: threat hunting. Where reactive detection waits for attackers to trigger alerts, threat hunting proactively searches for adversary activity that has evaded automated systems — and gets there before the attacker completes their mission.

Threat hunting is increasingly a required skill for senior analysts and is explicitly tested in the CySA+ CS0-003 exam under Domain 1 (Security Operations). This module builds your understanding of hypothesis-driven hunting methodology, MITRE ATT&CK as a hunting framework, endpoint telemetry analysis, and hunt documentation standards.

---

## Section 1 — High-Yield Glossary

**Threat Hunting** — The proactive, analyst-led search through an organization's environment for signs of adversary activity that has evaded automated detection. Distinguished from reactive detection by its hypothesis-driven, human-led nature.

**Dwell Time** — The period between an attacker's initial compromise of an environment and the organization's detection of that compromise. Threat hunting directly reduces dwell time.

**Hypothesis** — A specific, testable statement about adversary activity that a threat hunt is designed to confirm or refute. Effective hypotheses are time-bounded, technique-specific, and tied to a credible threat source.

**Hunting Loop** — The iterative cycle of threat hunting: form hypothesis → investigate → uncover patterns → inform detection → repeat.

**MITRE ATT&CK** — A knowledge base of adversary tactics and techniques derived from real-world observations, organized into a matrix framework. The primary structured resource for hunting hypothesis development.

**Tactic** — The "why" of adversary behavior in MITRE ATT&CK — the high-level goal the adversary is trying to achieve. Examples: Persistence, Lateral Movement, Exfiltration.

**Technique** — The "how" of adversary behavior in MITRE ATT&CK — a specific method used to accomplish a tactic. Examples: T1059.001 (PowerShell), T1078 (Valid Accounts).

**Sub-technique** — A more specific variant of a technique. T1059 (Command and Scripting Interpreter) has sub-techniques for PowerShell (T1059.001), Bash (T1059.004), etc.

**EDR (Endpoint Detection and Response)** — A security platform that continuously monitors endpoint activity, collects telemetry (process, network, file, registry events), and provides detection and response capability. The primary data source for most threat hunts.

**XDR (Extended Detection and Response)** — An evolution of EDR that integrates telemetry from endpoints, networks, email, cloud, and identity systems into a unified detection and hunting platform.

**KQL (Kusto Query Language)** — The query language used in Microsoft Defender Advanced Hunting, Azure Sentinel (Microsoft Sentinel), and Azure Log Analytics. Widely used for threat hunting in Microsoft environments.

**Beaconing** — Periodic, clock-like outbound network connections from a compromised host to a C2 server, indicating the malware is checking in for commands. A key network hunting indicator.

**Detection Engineering** — The practice of translating threat hunting findings and threat intelligence into new automated detection rules, SIEM content, and EDR policies.

**ATT&CK Navigator** — A web-based tool (attack.mitre.org/navigator) that visualizes ATT&CK technique coverage, allowing teams to map which techniques they can detect and identify gaps.

---

## Section 2 — The Hunting Loop in Depth

### Forming a Strong Hypothesis

A hunt hypothesis must be specific enough to direct investigation but broad enough that confirmable evidence could exist. The Sqrrl threat hunting maturity model provides a useful framing:

Level 0 (Reactive): No proactive hunting; relies entirely on automated alerts.

Level 1 (Minimal): Ad-hoc hunting based on IoCs (known-bad IPs, hashes). Low detection lift.

Level 2 (Procedural): Follows documented procedures and hunt playbooks. Moderate lift.

Level 3 (Innovative): Creates new hunting hypotheses using ATT&CK and threat intelligence. High lift.

Level 4 (Leading): Automates successful hunts into detection content; hunting directly drives detection engineering.

CySA+ analysts should aspire to Level 3. The exam tests Level 3 concepts.

A good hypothesis structure:

"Based on [threat intelligence or TTPs], we hypothesize that [specific adversary activity] is or has occurred in [specific environment or time range], which we would detect by observing [specific telemetry indicator] in [specific data source]."

### Investigating the Hypothesis

Investigation follows the hypothesis's implied data sources and indicators. If the hypothesis targets PowerShell execution from Office processes, the investigation queries endpoint telemetry for exactly that process relationship. If the hypothesis targets DNS beaconing, it analyzes DNS query patterns in network logs.

Investigation is structured, not exploratory browsing. Time-boxing hunts prevents infinite scope expansion. A focused 8-hour hunt is more productive than an open-ended 3-day investigation.

### Uncovering Patterns and Informing Detection

Whether the hunt confirms the hypothesis or not, it surfaces knowledge about the environment:

- Confirmation: the hunt finds the adversary activity → IR escalation + detection rule creation
- Refutation with clean result: hypothesis was wrong or attacker is absent → document negative finding + refine hypothesis for future
- Refutation with anomaly: hypothesis was wrong but something else was found → pivot to new hypothesis

Every hunt output must produce detection value: either a new SIEM rule, EDR policy, or hunt playbook that other analysts can reuse.

---

## Section 3 — MITRE ATT&CK as a Hunting Framework

### Using ATT&CK for Hunt Planning

The ATT&CK Navigator allows hunters to mark which techniques they can currently detect (green), which they are hunting for (yellow), and which they have no coverage for (red/blank). This creates a visual gap analysis of detection coverage.

A systematic hunt program works through the ATT&CK matrix technique by technique, prioritizing:

1. Techniques used by threat actors known to target your industry
2. Techniques for which your current automated detection has gaps
3. Techniques associated with active campaigns in current threat intelligence

### Key Techniques to Know for CySA+

The exam expects familiarity with common ATT&CK techniques:

**T1059 — Command and Scripting Interpreter** — Use of PowerShell, Bash, Python, and other scripting environments. Sub-technique T1059.001 (PowerShell) is the most commonly detected.

**T1078 — Valid Accounts** — Attackers use legitimate stolen credentials to blend in with normal traffic. Extremely difficult to detect with signature-based methods.

**T1055 — Process Injection** — Injecting malicious code into legitimate processes (svchost.exe, explorer.exe) to evade detection.

**T1547 — Boot or Logon Autostart Execution** — Persistence through registry run keys, startup folders, or scheduled tasks.

**T1021 — Remote Services** — Lateral movement using RDP, SMB, SSH, WinRM.

**T1041 — Exfiltration Over C2 Channel** — Data exfiltrated using the same channel as C2 communications, blending exfiltration with normal C2 traffic.

**T1071 — Application Layer Protocol** — Using HTTP, HTTPS, DNS for C2 communications to blend into normal web traffic.

**T1136 — Create Account** — Attacker creates a new user account for persistence or backdoor access.

---

## Section 4 — Endpoint Telemetry Analysis

### Process Trees and Parent-Child Relationships

The process tree is the most powerful single data structure for detecting malicious activity. Every process has a parent — the process that created it. Normal parent-child relationships follow predictable patterns. Malicious activity creates abnormal patterns.

Normal patterns:

- `explorer.exe` → `chrome.exe` (user launching a browser)
- `services.exe` → `svchost.exe` (Windows service management)
- `svchost.exe` → `msiexec.exe` (software installation via Windows Update)

Malicious patterns:

- `winword.exe` → `powershell.exe` (macro executing PowerShell — T1059.001)
- `powershell.exe` → `cmd.exe` → `whoami.exe` (discovery chain — T1087)
- `svchost.exe` → `powershell.exe` (process hollowing or injection — T1055)
- `explorer.exe` → `regsvr32.exe` loading a DLL from `C:\Users\Public\` (LOLBin abuse — T1218.010)

### Command-Line Argument Analysis

Malicious processes often reveal themselves through their command-line arguments:

- Base64-encoded arguments: `powershell.exe -enc JABjAGwAaQBlAG4Ad...` (T1059.001 obfuscation)
- Download cradles: `powershell.exe -c "IEX(New-Object Net.WebClient).DownloadString('http://...')"` (T1105)
- WMI execution: `wmic.exe process call create "cmd.exe /c..."` (T1047)

### Network Connection Analysis from Endpoints

EDR platforms correlate network connections with the process that made them. This enables hunting for:

- Processes making unexpected outbound connections (e.g., `word.exe` connecting to an external IP)
- Connections to newly registered domains or Tor exit nodes
- Processes making connections at regular intervals (beaconing)

---

## Section 5 — Network-Based Hunting

### Beaconing Detection

Beaconing is one of the most reliable C2 indicators. Most C2 frameworks beacon at configurable intervals with optional jitter.

Detection approach: calculate the standard deviation of connection intervals from each internal IP to each external IP. Low standard deviation (consistent timing) + regular intervals = beaconing candidate.

Additional indicators: small consistent payload sizes, connections surviving weekends and off-hours (automated, not human-driven), connections to IPs hosting no legitimate services.

### DNS Hunting

DNS provides visibility into every domain resolution attempt, including those using encrypted connections that hide the payload.

High-value DNS hunt queries:

- Domains registered within the past 30 days with connections from internal hosts
- Subdomains with entropy scores above threshold (DGA detection)
- NXDOMAIN rates above baseline (DGA pre-registration queries)
- DNS query volume per host above baseline (DNS tunneling)
- Queries for domains with no HTTPS content or no legitimate business purpose

---

## Section 6 — Hunt Documentation Standards

Every hunt, regardless of outcome, produces a documented record. The hunt record serves four purposes: institutional memory, detection engineering input, audit evidence of proactive security activity, and repeatable playbook for future hunts.

Required sections in a hunt documentation record:

- Hunt title and unique identifier
- Hunt date, analyst name, time spent
- Hypothesis and supporting threat intelligence source
- Data sources queried, tools used, time range covered
- Queries or search methodology (exact queries should be recorded)
- Findings — positive (with evidence) or negative (confirmed absence or inconclusive)
- IoCs or TTPs identified
- New detection rules created or recommended
- Recommendations for future hunts or control improvements

---

## Section 7 — CySA+ Exam Focus Areas

For the exam, know these threat hunting topics:

- The hunting loop — four stages and the purpose of each
- Hypothesis development — what makes a strong vs. weak hypothesis
- MITRE ATT&CK — tactics vs. techniques, how to use ATT&CK for hunt planning
- Endpoint telemetry — process trees, command-line arguments, network connections
- EDR vs. XDR — what each collects and provides
- Beaconing as a network hunting indicator
- Hunt documentation as a required output

---

## Study Checklist

- [ ] Define all glossary terms without referencing notes
- [ ] Write one strong hunting hypothesis using the required structure
- [ ] List the 14 MITRE ATT&CK Enterprise tactics in order
- [ ] Name five ATT&CK techniques relevant to endpoint hunting and describe each
- [ ] Describe three abnormal process parent-child relationships and explain what each suggests
- [ ] Explain what beaconing is and how to detect it in network telemetry
- [ ] List the required sections in a hunt documentation record
- [ ] Complete the Module 15 Lab
- [ ] Complete the Module 15 Quiz
- [ ] Post your Module 15 Discussion initial post by Wednesday

---

## 9. Supplemental Resources

**1. MITRE ATT&CK Navigator**
<https://mitre-attack.github.io/attack-navigator/>
The free, browser-based tool for visualizing MITRE ATT&CK coverage. Analysts use the Navigator to create heat maps showing which techniques are covered by existing detections, which techniques a known threat group uses, and where coverage gaps exist. For threat hunting, the Navigator is the primary planning tool: load a threat actor group layer, overlay your detection coverage layer, and the uncovered techniques become your hunt priority list. The Navigator documentation and the pre-built group layers (available for APT groups and financially motivated actors) are directly applicable to the lab scenario and exam questions.

**2. SANS Threat Hunting Survey and Hunt Methodology Papers**
<https://www.sans.org/blog/category/threat-hunting/>
SANS's collection of threat hunting research, methodology papers, and practitioner guides. Key resources include the annual SANS Threat Hunting Survey (which documents how real SOC teams structure hunts, what tools they use, and their maturity levels) and technique-specific hunting guides. The SANS hunting posts consistently demonstrate the hypothesis-driven hunt loop in action with real examples using Splunk SPL, KQL, and Elastic EQL — directly reinforcing the querying approach practiced in this module's lab.

**3. Florian Roth's Sigma Rule Repository**
<https://github.com/SigmaHQ/sigma>
Sigma is an open, vendor-neutral format for SIEM detection rules, similar to how Snort rules describe network threats for IDS platforms. The SigmaHQ repository contains thousands of community-contributed detection rules mapped to MITRE ATT&CK techniques, covering Windows process execution, PowerShell abuse, credential dumping, lateral movement, and dozens of other hunt categories. Reviewing Sigma rules for ATT&CK techniques you are hunting teaches you what telemetry fields to query, what field values indicate malicious activity, and how experienced practitioners express detection logic — directly supporting both hunt query development and the detection engineering deliverables required in the lab.

---

## Required Resources

- MITRE ATT&CK Enterprise Matrix — attack.mitre.org (free)
- ATT&CK Navigator — mitre-attack.github.io/attack-navigator (free)
- Sqrrl Threat Hunting Reference Guide (archived, available via Google)
- CrowdStrike Threat Hunting Guide — crowdstrike.com (free registration)
- CompTIA CySA+ CS0-003 Exam Objectives — Domain 1
- Module 15 Video Lecture (Professor Nash)

# Reading Guide: Module 08 — Incident Response: Detection and Triage

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


## Course: CIS-4332 Cyber Analyst

## Texas Wesleyan University | Professor Nash

## Certification Alignment: CompTIA CySA+ (CS0-003)

---

## Introduction

Detection and triage are where the security operations center earns its value. Every alert that arrives in the SIEM represents a decision point: is this a genuine attack, a misconfigured system, or a false positive? An analyst who makes that determination accurately — and documents the reasoning clearly — protects the organization. An analyst who closes alerts based on assumptions lets attackers operate undetected. This module covers the NIST SP 800-61 incident response lifecycle, the five-step triage workflow, alert classification, severity assignment, IR playbooks, and escalation documentation. These topics appear throughout Domain 1 of the CySA+ CS0-003 exam.

---

## Section 1 — NIST SP 800-61 Incident Response Lifecycle

### 1.1 Four-Phase IR Lifecycle

| Phase | Name | Primary Activities |
|---|---|---|
| Phase 1 | Preparation | Build IR capability: policies, playbooks, tools, training, communication plans |
| Phase 2 | Detection and Analysis | Monitor for events, triage alerts, classify incidents, determine scope and severity |
| Phase 3 | Containment, Eradication, and Recovery | Stop spread, remove threat, restore operations |
| Phase 4 | Post-Incident Activity | Lessons-learned review, playbook updates, metrics reporting |

### 1.2 Event vs. Incident Distinction

| Term | Definition | Example |
|---|---|---|
| Event | Any observable occurrence in a system or network | User login, file access, firewall rule match |
| Adverse Event | Event with negative security implications | Failed login, blocked connection, antivirus detection |
| Incident | Adverse event that violates security policy or threatens CIA | Confirmed malware infection, unauthorized data access, active breach |
| Precursor | Indicator that an incident may occur in the future | Port scan preceding exploitation attempt |
| Indicator | Sign that an incident may have occurred or is occurring now | Malicious IP in firewall logs, alert from EDR, suspicious process creation |

---

## Section 2 — Alert Triage Workflow

### 2.1 Five-Step Triage Process

```text
Step 1: RECEIVE AND ACKNOWLEDGE
- Log receipt of alert with timestamp
- Note alert source (SIEM rule name, EDR alert ID, ticket number)
- Do not close without investigation

Step 2: CLASSIFY — TRUE POSITIVE OR FALSE POSITIVE
- Review raw evidence behind the alert
- Apply alert classification matrix
- Never classify as FP based on account identity alone
- Document classification decision with supporting evidence

Step 3: IDENTIFY INCIDENT TYPE
- If TP: categorize the incident type
  (malware, unauthorized access, data exfiltration, DoS, insider, policy violation)
- Identify the relevant playbook

Step 4: DETERMINE SCOPE VIA IOC PIVOTING
- Extract all IOCs from the alert (IP, hash, domain, user account)
- Search SIEM and EDR for the same IOCs across all systems
- Build preliminary scope: confirmed compromised vs. potentially compromised

Step 5: DOCUMENT AND ESCALATE
- Record all findings in the incident ticket
- Apply severity rating
- Escalate to Tier 2 with structured escalation note
- Never close an uncertain case without supervisor acknowledgment
```

### 2.2 Alert Classification Matrix

| Classification | Description | Correct Action |
|---|---|---|
| True Positive (TP) | Alert fired correctly — the activity it detected is real and malicious | Open incident, triage, escalate |
| False Positive (FP) | Alert fired incorrectly — the activity is legitimate, not malicious | Document evidence for FP determination, tune the rule, close with notes |
| True Negative (TN) | No alert fired and no malicious activity occurred | Normal state — no action required |
| False Negative (FN) | No alert fired but malicious activity occurred | Discovered post-compromise — triggers detection gap review |

The most consequential error in the SOC is a **False Negative caused by premature FP classification** — closing a genuine incident because the analyst assumed the activity was authorized.

---

## Section 3 — Severity Classification

### 3.1 Severity Scale

| Severity | Name | Response SLA | Description |
|---|---|---|---|
| Severity 1 | Critical | 15 minutes | Active breach with ongoing attacker access; data exfiltration in progress; infrastructure-wide impact |
| Severity 2 | High | 1 hour | Confirmed malware on critical asset; compromised privileged account; multiple affected systems |
| Severity 3 | Medium | 4 hours | Malware on standard endpoint; suspicious activity requiring investigation; single non-critical system |
| Severity 4 | Low | 24 hours | Policy violation; anomalous activity with low confidence; informational event requiring documentation |

### 3.2 Severity Assignment Factors

| Factor | Description | Why It Matters |
|---|---|---|
| Asset criticality | How important is the affected system to business operations? | Domain controller compromise is Severity 1; personal workstation may be Severity 3 |
| Data sensitivity | What data does the system process or store? | PII, financial, PHI, source code require higher severity |
| Threat type | Active vs. historical? Spreading vs. contained? | Active C2 connection is more urgent than a historical detection |
| Scope | Number of affected systems | Widespread infection increases severity |
| Privilege level | What access does the compromised account have? | Domain admin compromise is always high severity |
| Exploitability | Can the attacker escalate or pivot from this position? | Internet-facing exploited service escalates severity |

---

## Section 4 — IR Playbooks

### 4.1 Playbook Structure Components

| Component | Purpose |
|---|---|
| Trigger conditions | What alert or event activates this playbook |
| Triage checklist | Step-by-step actions for Tier 1 — ordered, non-ambiguous |
| Evidence preservation steps | What to collect and how before containment |
| Containment actions by tier | What Tier 1 can do independently vs. what requires Tier 2 approval |
| Escalation criteria | When to escalate and who to notify |
| Communication templates | Pre-written notification language for stakeholders |
| Recovery steps | Ordered actions to restore normal operations after eradication |
| Post-incident actions | Documentation, lessons learned, playbook update trigger |

### 4.2 Common Playbook Types

| Playbook Type | Trigger | Key Distinguishing Actions |
|---|---|---|
| Malware infection | EDR alert, AV detection, suspicious process tree | EDR isolation, memory acquisition, IOC pivoting |
| Phishing / credential theft | Email gateway alert, user report, MFA anomaly | Account suspension, password reset, email header analysis |
| Ransomware | File extension change, shadow copy deletion, ransom note | Emergency isolation, backup integrity check, no ransom without alternatives |
| Unauthorized access | Impossible travel, off-hours auth, new admin account | Account lockout, access log review, privilege audit |
| Data exfiltration | Large outbound transfer, DLP alert, cloud storage anomaly | Block destination, preserve netflow, legal/compliance notification |
| Insider threat | Policy violation, abnormal data access, terminated user activity | HR/legal coordination, evidence preservation, access revocation |

---

## Section 5 — IOC Pivoting and Scope Determination

### 5.1 IOC Pivot Table

| IOC Type | What to Search | Tool | Scope Question |
|---|---|---|---|
| IP address (C2) | All hosts that connected to this IP in past 30 days | SIEM firewall/proxy logs | How many endpoints beaconed to the same C2? |
| File hash | All endpoints where this hash was observed | EDR file hash search | How many systems have the malware installed? |
| Domain name | All DNS queries matching this domain | SIEM DNS logs | Which endpoints looked up the C2 domain? |
| Registry key | All endpoints with this persistence key | EDR registry hunt | How many systems have attacker persistence? |
| User account | All systems this account authenticated to | SIEM auth logs | How far has lateral movement spread? |
| Scheduled task name | All endpoints with this task name | EDR or SIEM process logs | How many systems have this persistence mechanism? |

### 5.2 Scope Classification

| Classification | Criteria | Response Priority |
|---|---|---|
| Confirmed compromised | Malware hash confirmed present, or attacker command execution observed directly | Immediate containment |
| Potentially compromised | C2 domain queried, or suspicious IOC match without full confirmation | Isolation pending investigation |
| Exposed but not compromised | Shares network segment with confirmed infected host; no direct IOC match | Monitor, restrict access |
| Not in scope | No IOC match across any pivot; no network path to infected host | Document negative result |

---

## Section 6 — Escalation Documentation

### 6.1 Structured Escalation Note Template

```text
ESCALATION NOTE — INCIDENT TICKET: [TICKET-ID]

Alert Source: [SIEM rule / EDR alert ID]
Alert Time: [timestamp UTC]
Analyst: [Tier 1 name]
Escalation Time: [timestamp UTC]

Affected Systems:
  - Primary: [hostname, IP, function]
  - Additional (from IOC pivot): [list]

IOCs Identified:
  - File hash: [value]
  - C2 IP: [value] Port: [value]
  - C2 Domain: [value]
  - Registry key: [value]

Investigation Steps Completed:
  1. [Action taken — result]
  2. [Action taken — result]
  3. [Action taken — result]

Classification: [True Positive / Uncertain — requires Tier 2 review]
Preliminary Scope: [Confirmed compromised / Potentially compromised systems]
Recommended Containment: [EDR isolation / Account lockout / IP block]

Reason for Escalation: [Specific reason — severity, scope, uncertainty, time constraint]
```

### 6.2 Critical Triage Mistakes

| Mistake | Why It Is Wrong | Correct Action |
|---|---|---|
| Closing alert because the account belongs to a known user | Legitimate credentials are the attacker's most effective tool | Separate account legitimacy from activity legitimacy |
| Rebooting the affected system immediately | Destroys volatile memory (RAM), running processes, and network connections | Perform EDR network isolation; collect memory before any reboot |
| Deleting malware files before evidence collection | Eliminates forensic evidence needed for root cause analysis | Hash and image before removing |
| Scoping to a single system without IOC pivoting | Misses lateral movement and additional compromised hosts | Always pivot on every IOC before finalizing scope |
| Documenting FP closure without evidence | Creates audit trail gap; no basis to challenge if incident is later confirmed | Document all evidence supporting FP determination |
| Tier 1 taking containment action without authorization | Violates IR policy; may disrupt business-critical systems | Follow playbook; Tier 1 containment requires pre-approved playbook authority or Tier 2 approval |

---

## CySA+ Exam Tips

Exam Tip 1: NIST SP 800-61 defines four phases. Phase 2 (Detection and Analysis) is where the triage workflow lives. Phase 3 (Containment, Eradication, and Recovery) is Module 09. Know which phase each activity belongs to.

Exam Tip 2: The alert classification matrix has four quadrants. The exam most frequently tests the distinction between True Positive and False Positive in scenario questions. The critical concept: a known-good account performing suspicious activity is NOT automatically a FP.

Exam Tip 3: Severity assignment is based on asset criticality, data sensitivity, and scope — not solely on the type of malware. A Severity 3 malware infection on a domain controller is still Severity 1 because of the asset.

Exam Tip 4: IOC pivoting is the mechanism for determining incident scope. The exam expects analysts to use every confirmed IOC as a search term across all available data sources — not just the affected host.

Exam Tip 5: EDR network isolation is the correct containment action for a running compromised system. Shutdown destroys volatile evidence. Isolation preserves the system state while cutting attacker access.

Exam Tip 6: Escalation notes must contain specific technical information. Exam scenario questions may ask what is missing from an escalation. The answer almost always involves IOC details, investigation steps completed, or specific scope findings.

Exam Tip 7: False Negative incidents — where no alert fired but an attack was occurring — are the most damaging outcome. The exam tests awareness that FN incidents result from detection gaps, not just analyst error.

Exam Tip 8: IR playbooks reduce response time by pre-authorizing Tier 1 actions. Pre-approved isolation authority is the mechanism that allows Tier 1 to contain without waiting for Tier 2 approval — this directly reduces dwell time.

---

## Glossary

- Alert: A notification generated by a security tool indicating that a monitored condition has been met
- Containment: Actions taken to stop an incident from spreading before eradication begins
- Dwell Time: The duration between initial compromise and detection; lower is better
- EDR (Endpoint Detection and Response): Agent-based endpoint security platform providing real-time behavioral monitoring, alerting, and response capabilities
- False Negative: Security tool fails to detect a real malicious event
- False Positive: Security tool fires an alert on a legitimate, non-malicious event
- IOC (Indicator of Compromise): Technical artifact — hash, IP, domain, registry key — that indicates a system has been compromised
- IOC Pivoting: Using a known IOC to search all data sources for additional affected systems
- IR Playbook: Documented, ordered procedure for responding to a specific incident type
- NIST SP 800-61: NIST guide for computer security incident handling — the foundational IR framework
- Scope: The total set of systems confirmed or potentially affected by an incident
- Severity: A classification of incident urgency and impact used to assign response SLAs
- SIEM (Security Information and Event Management): Centralized log aggregation and correlation platform
- True Positive: Security tool correctly identifies a real malicious event

---

## Study Checklist

- [ ] Explain the four phases of NIST SP 800-61 and what activities occur in each phase
- [ ] Describe the five-step triage workflow without notes
- [ ] Explain the four alert classification types and give an example of each
- [ ] Describe the four severity levels and the factors that affect severity assignment
- [ ] Name at least four components of an IR playbook
- [ ] Explain what IOC pivoting is and describe the pivot process for three IOC types
- [ ] Describe the scope classification framework (confirmed / potentially / exposed / not in scope)
- [ ] Write a complete escalation note template from memory
- [ ] List six critical triage mistakes and the correct action for each
- [ ] Review all eight exam tips
- [ ] Complete the Module 08 Lab
- [ ] Complete the Module 08 Quiz
- [ ] Post initial response to the Module 08 Discussion by Wednesday at 11:59 PM

---

## 9. Supplemental Resources

**1. FIRST — EPSS (Exploit Prediction Scoring System)**
<https://www.first.org/epss/>
The official EPSS specification and data download page. EPSS provides a daily-updated exploitation probability score for every CVE, complementing CVSS severity with real-world threat intelligence. The FIRST site includes research papers explaining the model and an API for programmatic access — essential reading for understanding modern risk-based vulnerability prioritization covered in Section 4 of this guide.

**2. CISA — Stakeholder-Specific Vulnerability Categorization (SSVC) Guide**
<https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc>
CISA's decision-tree framework for vulnerability prioritization that combines exploitation status, technical impact, and deployment context to produce actionable remediation decisions without relying solely on CVSS. The guide includes worked examples and a scoring calculator. SSVC is increasingly adopted by federal agencies and represents the current state of practice for risk-based vulnerability management.

**3. NIST — NVD (National Vulnerability Database)**
<https://nvd.nist.gov/>
The primary source for CVSS vector strings, CWE classifications, CPE applicability, and vendor advisory links for every CVE. Practice reading the full NVD entry for any recent high-profile CVE to build fluency in interpreting CVSS Base metrics, temporal metrics, and the relationships between CVE, CWE, and CPE that are tested throughout the CySA+ exam.

# Reading Guide: Module 11 — Incident Response for Analysts

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

Welcome to Module 11: Incident Response for Analysts. This module bridges the gap between detection and action. You have spent previous modules building skills in threat detection, log analysis, vulnerability management, and threat intelligence. Now you will learn what happens after detection fires — and specifically, what the analyst's role is within a formal incident response program.

This module is anchored in NIST Special Publication 800-61 Revision 2, "Computer Security Incident Handling Guide." This document is explicitly cited in the CySA+ CS0-003 exam objectives and should be on your reading list. We will walk through each of its four phases, analyze the analyst's specific contributions at each stage, and examine the critical skills of triage, scoping, playbook execution, and documentation.

Incident response knowledge spans multiple CySA+ exam domains. Domain 4 (Incident Response and Digital Forensics) carries the most direct weight, but IR concepts appear in Domain 1 (Security Operations) and Domain 3 (Reporting and Communication) as well. Invest time here — it pays dividends on the exam and in the field.

---

## Section 1 — High-Yield Glossary

Review these definitions carefully. The CySA+ exam will use these terms in scenario questions and expect precise understanding.

**Incident** — A violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices. Not every security event is an incident. An event becomes an incident when it is confirmed to have a negative security impact.

**Event** — Any observable occurrence in a system or network. Events include logins, file accesses, network connections, and configuration changes. Events are the raw material that analysts evaluate to identify incidents.

**CSIRT (Computer Security Incident Response Team)** — The formal team responsible for coordinating the organization's response to security incidents. Analysts typically support and feed intelligence to the CSIRT rather than lead it, except in smaller organizations where analysts may fill both roles.

**Playbook** — A documented, step-by-step procedure for handling a specific incident type. Playbooks standardize response, reduce decision fatigue under pressure, and ensure consistency across analyst shifts.

**Triage** — The initial assessment of an alert or event to determine whether it is a true positive, what its severity is, and what immediate actions are required. Triage is time-boxed and focused on classification, not full investigation.

**Scope** — The full extent of systems, accounts, data, and time periods affected by an incident. Accurate scoping is required before effective containment can be planned.

**Containment** — Actions taken to stop the spread or continued damage of an incident without necessarily removing the threat. Divided into short-term (immediate isolation) and long-term (sustained limitation pending eradication).

**Eradication** — Removal of the root cause of the incident, including malware, compromised accounts, unauthorized changes, and all persistence mechanisms.

**Recovery** — Restoration of systems and services to normal, verified operation following eradication.

**Chain of Custody** — The documented, unbroken record of who collected, handled, and transferred evidence. Required for evidence to be admissible in legal proceedings.

**IoC (Indicator of Compromise)** — Observable evidence of a compromise or malicious activity. Examples include malicious file hashes, attacker IP addresses, suspicious registry keys, and anomalous network connections.

**MTTD / MTTR / MTTC** — Mean Time to Detect, Mean Time to Respond, and Mean Time to Contain. These metrics measure IR program effectiveness and drive investment decisions.

---

## Section 2 — NIST SP 800-61 Phase-by-Phase Analysis

### Phase 1: Preparation

Preparation is the foundation of effective incident response. Organizations that invest in preparation respond faster, with more accuracy, and with less collateral damage when incidents occur.

Key preparation activities include establishing the CSIRT, defining IR policies and procedures, building and maintaining playbooks, deploying detection and logging infrastructure, establishing communication trees and escalation protocols, and conducting regular training exercises including tabletop simulations and live-fire drills.

The analyst's preparation responsibilities include tuning SIEM correlation rules to reduce false positives, maintaining threat intelligence feeds, familiarizing themselves with current playbooks, and understanding the network and asset topology they are defending.

Preparation quality directly determines the effectiveness of every subsequent phase. An organization that has never exercised their ransomware playbook will perform poorly when ransomware actually lands.

### Phase 2: Detection and Analysis

This is the phase where analysts spend the majority of their incident-related time. Detection involves recognizing anomalous activity through automated alerts, manual log review, user reports, or threat hunting. Analysis involves confirming whether the detected activity represents a genuine incident.

Detection sources analysts rely on include:

- SIEM correlation rules and alerts
- IDS/IPS events
- Endpoint detection and response (EDR) telemetry
- DNS query anomalies
- NetFlow analysis
- User and Entity Behavior Analytics (UEBA) alerts
- Threat intelligence platform matches
- Help desk and user reports

Analysis quality depends on log coverage, alert fidelity, and analyst experience. A well-tuned environment with comprehensive log coverage enables analysts to quickly confirm incidents and establish accurate scope. A poorly instrumented environment forces analysts to work with incomplete data and increases investigation time.

### Phase 2 Deep Dive: Triage

Triage is a structured, time-bounded process. Most organizations define triage SLAs — for example, all high-severity alerts must be triaged within 15 minutes.

The NIST 800-61 severity classification framework uses three dimensions:

- **Functional impact** — None, Minimal, Significant, Severe. Measures business function disruption.
- **Information impact** — None, Privacy Breach, Proprietary Breach, Integrity Loss. Measures data exposure.
- **Recoverability** — Regular, Supplemented, Extended, Not Recoverable. Measures recovery effort.

Combining these dimensions produces the overall incident severity that drives escalation and resource allocation decisions.

### Phase 2 Deep Dive: Scoping

Scoping follows confirmation. An analyst confirming a true positive immediately pivots to answering: how far has this spread?

Lateral movement is the most common scoping failure point. An analyst who identifies a compromised workstation but fails to check whether that workstation made internal SMB connections to file servers has scoped the incident too narrowly. IR teams have repeatedly found that what appeared to be a single-host incident had actually propagated to dozens of systems.

Scoping tools include SIEM event correlation across source and destination IPs, EDR process trees showing parent-child relationships, Active Directory authentication logs showing which accounts authenticated from the affected host, and network flow data showing internal connection attempts.

### Phase 3: Containment, Eradication, and Recovery

Containment requires a tradeoff decision: speed versus evidence preservation. Aggressive immediate isolation may destroy volatile memory evidence (running processes, network connections, RAM contents) that forensic analysis would require. Your playbook should define this tradeoff based on incident type.

For ransomware: isolate immediately. Ransomware spreads to network shares and backup systems in minutes. Evidence preservation is secondary to preventing mass encryption.

For APT (Advanced Persistent Threat) incidents: consider delayed or covert containment. Immediately isolating an APT actor may cause them to activate destructive payloads or destroy evidence. Sometimes it is better to observe and document before acting.

Eradication must address every persistence mechanism. Common persistence mechanisms include scheduled tasks, registry run keys, WMI subscriptions, startup folders, service installations, cron jobs, and web shells. Missing any one of these results in re-compromise, often within hours.

Recovery monitoring should continue for at least 30 days for significant incidents. Re-compromise is most common in the first week following recovery.

### Phase 4: Post-Incident Activity

The lessons learned meeting should occur within two weeks while memories are fresh. NIST recommends including all participants: analysts, IR team members, IT operations, and management.

The output of lessons learned is a formal incident report and a set of concrete action items — not just narrative reflection. Action items should have owners, deadlines, and follow-up verification.

---

## Section 3 — Playbook Development

Playbooks are living documents. They require regular review, especially after incident exercises reveal gaps.

A mature playbook library covers:

- Malware / ransomware
- Phishing and business email compromise
- Unauthorized access
- Data exfiltration
- DDoS
- Insider threat
- Cloud account compromise
- Third-party / supply chain compromise

Each playbook follows a consistent structure: trigger conditions, initial triage steps, escalation criteria, containment procedures, evidence checklist, eradication steps, recovery milestones, and communication templates.

When writing or reviewing playbooks, test them. Walk a colleague through a scenario using the playbook as the only guide. Gaps become immediately apparent.

---

## Section 4 — Incident Documentation Best Practices

Documentation is the analyst's permanent record of thought and action. It must be:

- **Accurate** — Record what actually happened, not what you expected
- **Timestamped** — Every entry includes date and time, preferably UTC
- **Complete** — Do not summarize away important detail
- **Objective** — Stick to observable facts; mark inferences clearly as inferences

Incident documentation serves multiple purposes beyond the immediate response. It feeds the lessons learned process, supports legal and regulatory proceedings, enables forensic reconstruction, and provides reference for future similar incidents.

Modern IR platforms (ServiceNow Security Operations, IBM Resilient, Palo Alto XSOAR) provide structured case management with automated evidence linking and timeline building. Even without these tools, a rigorous ticketing discipline in a standard ITSM system produces defensible documentation.

---

## Section 5 — Communication in Incident Response

Communication failures during incidents are as damaging as technical failures. Key communication practices include:

Establish a single incident bridge or communication channel at the start of significant incidents. All updates flow through one channel, avoiding information fragmentation across email, Slack, phone, and Teams.

Define a status cadence. For significant incidents, brief stakeholders on a defined schedule (every 30 minutes, every hour) rather than only when something changes. Silence during an incident is interpreted as incompetence or lost control.

Separate technical and executive communication. Technical channel contains full detail. Executive updates are brief: what happened, what we are doing, what the business impact is, when we expect resolution.

Preserve all communication records as part of the incident documentation.

---

## Section 6 — CySA+ Exam Focus Areas

The CySA+ CS0-003 exam tests incident response across several objective areas:

- **4.1** — Explain the importance of incident response processes
- **4.2** — Given a scenario, apply the appropriate incident response procedure
- **4.3** — Given an incident, analyze potential indicators of compromise
- **4.4** — Utilize basic digital forensics techniques

For the exam, know the NIST phases in order and be able to identify which phase a described action belongs to. Understand that the phases are iterative, not strictly sequential. Know the difference between containment and eradication. Be able to classify incidents using the NIST severity framework.

Scenario questions will present an incident in progress and ask what the analyst should do next. The answer usually requires identifying the correct phase and the appropriate action within that phase.

---

## Study Checklist

- [ ] Read NIST SP 800-61 Rev. 2 Sections 1–4 (free at nvlpubs.nist.gov)
- [ ] Define all glossary terms from memory without referencing notes
- [ ] Map analyst actions to each of the four NIST phases
- [ ] Describe the difference between triage and scoping
- [ ] Explain the tradeoff between evidence preservation and containment speed
- [ ] List five common malware persistence mechanisms
- [ ] Describe what a complete incident timeline record must contain
- [ ] Complete the Module 11 Lab activity
- [ ] Complete the Module 11 Quiz
- [ ] Post your Module 11 Discussion initial post by Wednesday

---

## 9. Supplemental Resources

**1. NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide**
<https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf>
This is the primary reference document for this entire module. Sections 3.1 through 3.4 define the four IR phases, escalation criteria, evidence handling principles, and post-incident activity requirements that form the core of the CySA+ exam's IR content. If you have time to read only one document for this module, this is it.

**2. CISA — Incident Response Playbooks (Federal Civilian Executive Branch)**
<https://www.cisa.gov/sites/default/files/2024-08/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf>
CISA's federal IR playbook templates covering phishing, malware, and vulnerability response. Reading through a playbook (especially the Malware Response playbook, Section 3) illustrates how abstract NIST phase descriptions translate into concrete analyst actions, decision branches, and escalation criteria — directly applicable to the scenario-based questions on the CySA+ exam.

**3. MITRE ATT&CK — Incident Response Techniques Reference**
<https://attack.mitre.org/tactics/TA0040/>
The ATT&CK Impact tactic page documents adversary actions that cause harm to systems and data — including data encryption (ransomware), inhibit system recovery (VSS deletion), and data destruction. Understanding the technique IDs and descriptions at the Impact tactic level gives analysts a structured vocabulary for documenting what an attacker accomplished during an incident, directly feeding the incident timeline and lessons-learned deliverables covered in Section 5.

---

## Required Resources

- NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide (free: nvlpubs.nist.gov)
- CompTIA CySA+ CS0-003 Exam Objectives — Domain 4: Incident Response
- CertifyBreakfast CySA+ CS0-003 Complete Playlist — Incident Response sections
- Module 11 Video Lecture (Professor Nash)

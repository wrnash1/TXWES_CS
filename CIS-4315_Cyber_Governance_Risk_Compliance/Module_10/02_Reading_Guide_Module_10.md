# Reading Guide: Module 10 — Incident Management Planning

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4315 &BULL; CYBERSECURITY GOVERNANCE, RISK & COMPLIANCE (GRC)</text>
    
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


## Course: CIS-4315 Cyber Governance, Risk, and Compliance

## Texas Wesleyan University | Professor Nash

## CISM Domain Alignment: Domain 4 — Incident Management

---

## Overview

This reading guide provides comprehensive reference material for Module 10. Incident response planning is the foundational preparation activity that determines how effectively an organization responds when a security incident occurs. The quality of preparation — the plan, the team, the communication protocols, and the exercises — determines the speed and effectiveness of response. CISM Domain 4 tests this material extensively.

Work through each section in order. Complete the study checklist before attempting the quiz.

---

## Section 1 — Foundations of Incident Response Planning

### 1.1 Incident vs. Event vs. Breach

Before examining the Incident Response Plan, it is essential to establish clear definitions for terms that are frequently confused:

| Term | Definition | Example |
|---|---|---|
| Security event | Any observable occurrence in a system or network | A user logs in at 3 AM |
| Security incident | An event that threatens or violates security policy, integrity, or availability | A user logs in at 3 AM from a foreign country and accesses PII records |
| Data breach | A confirmed incident in which sensitive data was accessed, exfiltrated, or exposed without authorization | The PII records are confirmed to have been copied and sent externally |

Not every event is an incident. Not every incident is a breach. The severity classification framework in the IRP defines these distinctions operationally.

### 1.2 Why Incident Response Planning Matters

The IBM Cost of a Data Breach Report consistently identifies incident response preparedness as among the highest-impact factors in breach cost reduction. Key findings:

- Organizations with a formally tested IR plan and team spend on average 1.5–2.5 million dollars less per incident than unprepared organizations.

- Mean time to identify and contain a breach averages 277 days for organizations without a formal IR capability.

- The cost differential between fast and slow response exceeds 1 million dollars annually for mid-large organizations.

The CISM framework positions incident response planning as a governance responsibility, not just an operational one. The CISM must ensure that the organization has and maintains a functional IRP.

### 1.3 NIST SP 800-61 — The Authoritative Framework

NIST Special Publication 800-61 Revision 2, Computer Security Incident Handling Guide, is the primary authoritative reference for incident response planning in the United States. Key points about the framework:

- Defines a four-phase incident response lifecycle applicable to all organization types.

- Provides guidance on establishing an incident response capability, handling incidents, and coordinating with external parties.

- Is framework-agnostic — compatible with ISO 27001, NIST CSF, and CISM.

- Is referenced directly in many regulatory compliance standards.

| Phase | Name | Key Activities |
|---|---|---|
| 1 | Preparation | Build team, write plan, deploy tools, train staff, run exercises |
| 2 | Detection and Analysis | Identify, triage, scope, and characterize incidents |
| 3 | Containment, Eradication, Recovery | Stop spread, remove threat, restore operations |
| 4 | Post-Incident Activity | Lessons learned, root cause, plan updates |

---

## Section 2 — Incident Response Plan Components

### 2.1 Required IRP Sections

A complete Incident Response Plan must contain the following sections:

**1. Purpose and Scope**: Defines why the plan exists, which incident types it covers, which organizational units and systems are in scope, and what is explicitly excluded.

**2. Policy and Management Authorization**: Documents executive authorization for the IRP. The incident response team requires organizational authority to take disruptive actions such as isolating systems or disconnecting business-critical services.

**3. Incident Classification Framework**: Defines severity levels (typically Severity 1 through Severity 4 or Critical/High/Medium/Low) with specific criteria for each level. This framework governs escalation and response procedures.

**4. Incident Response Team Roles and Responsibilities**: Defines each IRT role, the person assigned to that role, their backup contact, and their authorized actions.

**5. Response Procedures**: Step-by-step procedures for priority incident types. Must be specific and actionable, not general guidance.

**6. Communication Plan**: Internal notification chain and external notification obligations, including regulatory reporting, customer notification, law enforcement, and cyber insurance.

**7. Evidence Preservation Guidelines**: Defines how evidence is collected, documented, and protected for potential legal proceedings or regulatory audits.

**8. Plan Testing and Maintenance Schedule**: Defines exercise cadence, plan review schedule, and triggers for out-of-cycle review.

### 2.2 Incident Severity Classification Framework

| Severity Level | Characteristics | Response Time | Escalation |
|---|---|---|---|
| Critical (S1) | Data breach confirmed; critical systems offline; regulated data exposed | Immediate | CISO, Executive team, Legal, Board if applicable |
| High (S2) | Active intrusion; significant system disruption; threat of data breach | Within 1 hour | CISO, Legal, relevant BUs |
| Medium (S3) | Malware on endpoint; policy violation; contained scope | Within 4 hours | Security manager, system owners |
| Low (S4) | Suspicious activity; attempted but failed attack; minor policy violation | Within 24 hours | Security operations team |

### 2.3 IRP Policy Authorization

The IRP must be authorized at the executive level — typically signed by the CEO or CIO/CISO with explicit board-level acknowledgment. This authorization is necessary because:

- Incident response may require isolating production systems, causing business disruption.

- Incident response may involve engaging law enforcement or regulatory authorities.

- Incident response may require emergency expenditures beyond normal budget authority.

- Incident response activities may create legal obligations affecting the entire organization.

Without executive authorization, the IR team may face resistance from business unit owners who resist system isolation decisions, even during an active incident.

---

## Section 3 — Incident Response Team Roles

### 3.1 Core IRT Roles

| Role | Primary Responsibilities | Typical Title |
|---|---|---|
| Incident Response Manager | Overall incident command, escalation decisions, leadership interface | CISO or designated IR Manager |
| Technical Lead | Forensic investigation, containment execution, system recovery | Senior security engineer |
| Communications Lead | Internal and external communications, media management | Security manager or PR liaison |
| Legal Counsel | Regulatory obligations, litigation hold, law enforcement coordination | General Counsel or outside counsel |
| HR Representative | Insider threat investigations, employee-related actions | HR Manager |
| Business System Owner | Recovery authorization for specific business systems | Line-of-business IT manager |

### 3.2 RACI Matrix Application

The RACI framework is the standard tool for defining accountability in incident response:

| Activity | IR Manager | Technical Lead | Comms Lead | Legal | HR |
|---|---|---|---|---|---|
| Incident declaration | A | C | I | I | I |
| System isolation decision | A | R | I | C | I |
| Evidence collection | C | R | I | A | I |
| Regulatory notification | A | C | R | C | I |
| Employee investigation | A | C | I | C | R |
| Media statement | A | I | R | C | I |

Key: R = Responsible, A = Accountable, C = Consulted, I = Informed

### 3.3 Retaining External Support

Many organizations retain third-party incident response support. Models include:

**Break-glass retainer**: Contract with an IR firm that can be activated on short notice. Typically 40–80 hours of pre-paid capacity. Activated when internal team is overwhelmed.

**Embedded support**: IR firm staff work alongside the internal team regularly, including during exercises, providing surge capacity and specialized expertise.

**Full outsourcing**: Organizations without internal IR capability contract a managed security service provider (MSSP) for all IR activities.

---

## Section 4 — Communication Plans

### 4.1 Internal Communication Structure

The internal communication plan defines the notification chain triggered at each severity level:

| Severity | Immediately Notify | Notify Within 1 Hour | Notify Within 4 Hours |
|---|---|---|---|
| Critical (S1) | CISO, IR Manager, Legal | CEO, COO, Board Chair | All department heads, Cyber insurance |
| High (S2) | CISO, IR Manager | Legal, affected BU heads | IT leadership |
| Medium (S3) | IR Manager | Security manager, system owner | |
| Low (S4) | On-call security analyst | IR Manager (next business day) | |

### 4.2 Need-to-Know Principle in Incident Communication

During an active incident, information disclosure must be carefully controlled:

- **Insider threat risk**: Premature broad communication may alert an internal threat actor to the investigation.

- **Legal privilege**: Incident information shared with legal counsel may be protected. Sharing it too broadly may waive that protection.

- **Regulatory exposure**: Pre-mature public statements before legal review can create additional regulatory liability.

- **Market sensitivity**: For publicly traded organizations, breach information may be material non-public information subject to securities law.

### 4.3 Out-of-Band Communication

If the incident has compromised normal communication infrastructure:

- Designate personal cell phones as primary during response.

- Pre-establish a secure messaging channel (Signal, encrypted email) as backup.

- Maintain a printed contact list for key IRT members — not accessible only through potentially compromised systems.

- Consider a secondary email domain maintained specifically for incident response.

### 4.4 External Notification Obligations

| Obligation | Trigger | Deadline | Authority |
|---|---|---|---|
| HIPAA Breach Notification | PHI breach affecting 500+ individuals | 60 days from discovery | HHS Office for Civil Rights |
| GDPR Breach Notification | Personal data breach likely to result in risk | 72 hours from discovery | Supervisory Authority |
| State breach notification (US) | PII breach affecting state residents | Varies: 30–90 days | State AG office |
| SEC Form 8-K (material breach) | Publicly traded company, material incident | 4 business days from materiality determination | SEC |
| PCI-DSS notification | Cardholder data breach | Immediately | Card brands and acquiring bank |
| Cyber insurance notification | Covered incident | Per policy terms (typically 24–72 hours) | Carrier |

### 4.5 Pre-Drafted Notification Templates

Every IRP should include pre-drafted notification templates for likely scenarios:

- Customer breach notification letter

- Regulatory notification form (HIPAA, GDPR)

- Internal all-employee communication

- Media holding statement ("We are aware of a security incident and are conducting a thorough investigation")

- Vendor and partner notification

Pre-drafting these templates saves critical time during an incident when legal review and rapid communication are both essential.

---

## Section 5 — Escalation Procedures

### 5.1 Criteria-Based Escalation

Effective escalation procedures use explicit criteria, not subjective judgment. Each criterion triggers a specific notification action:

**Data-based triggers**:

- Confirmed access to regulated data (PHI, PCI cardholder data, PII): escalate to CISO and Legal immediately.

- Estimated records affected exceeds 500: escalate to executive team and prepare regulatory notification.

- Estimated records affected exceeds 5,000: escalate to board chair.

**Time-based triggers**:

- Incident active for 4 hours without confirmed containment: escalate to CISO.

- Incident active for 24 hours without confirmed containment: escalate to COO and CEO.

**Threat-based triggers**:

- Evidence of nation-state actor or APT: escalate to board and engage law enforcement.

- Critical infrastructure systems (power, water, healthcare delivery) affected: engage CISA and law enforcement.

- Evidence of ongoing exfiltration: escalate to CISO and Legal immediately.

### 5.2 Escalation Documentation

Every escalation event must be documented in the incident log:

- Who made the escalation decision.

- What criteria triggered the escalation.

- Who was notified and by what method.

- Timestamp of notification.

- Response received (if any).

This documentation is essential for regulatory compliance and post-incident legal proceedings.

---

## Section 6 — IRP, BCP, and DRP Alignment

### 6.1 The Three-Plan Framework

| Plan | Scope | Primary Question | Owner |
|---|---|---|---|
| IRP | Security response | How do we detect and stop the threat? | CISO / IR Manager |
| DRP | Technical recovery | How do we restore systems and data? | IT / Infrastructure |
| BCP | Business continuity | How do we keep operating while recovery occurs? | COO / Business Units |

### 6.2 Key Alignment Requirements

The three plans must be aligned in the following areas:

**Recovery Time Objectives (RTOs)**: The IRP may require systems to remain offline for forensic investigation; the DRP defines how quickly they must be restored. These objectives must be negotiated in advance.

**Evidence vs. Speed trade-off**: Forensics requires system preservation; DRP may require system reinstallation. The IRP must pre-authorize specific recovery approaches for specific incident types.

**Command authority**: During a major incident, who is in command — the IR Manager, the CIO, or the COO? The answer depends on the incident phase. This must be pre-defined.

**Communication integration**: IRP, BCP, and DRP must use compatible communication structures and contact lists.

### 6.3 Plan Testing Schedule

| Exercise Type | Frequency | Participants | Scope |
|---|---|---|---|
| Tabletop exercise | Annually minimum | IRT, executive team, legal | Decision-making and communication |
| Functional exercise | Annually | IRT, IT, communications | Specific response functions |
| Full-scale simulation | Every 2–3 years | All relevant teams | Complete IRP, DRP, BCP integration |
| Post-incident review | After every real incident | IRT, management | Lessons learned, plan update |

---

## Section 7 — CISM Exam Alignment

### 7.1 Domain 4 Objectives Covered

This module addresses CISM Domain 4 — Incident Management objectives:

- Establish an incident response capability aligned to organizational risk.

- Develop incident response plans, playbooks, and procedures.

- Define escalation criteria and communication protocols.

- Align IRP with business continuity and disaster recovery plans.

### 7.2 High-Probability Exam Topics

- **NIST SP 800-61 phases**: Know all four phases and their key activities.

- **IRP components**: Know what a complete IRP must include.

- **RACI matrix**: Understand how to assign accountability in IR scenarios.

- **Escalation criteria**: Know that effective escalation is criteria-based, not judgment-based.

- **External notification deadlines**: HIPAA 60 days, GDPR 72 hours, SEC 4 business days.

- **IRP vs. DRP vs. BCP**: Know the scope and relationship of each.

### 7.3 Sample CISM Exam Question

**Question**: An organization has just experienced a confirmed ransomware incident affecting 15 servers. The incident response team has successfully isolated the infected systems. Which of the following actions should occur NEXT?

A. Restore systems from backup immediately to meet recovery time objectives.
B. Notify all employees about the incident via company-wide email.
C. Conduct a forensic investigation to determine scope, origin, and persistence before restoration.
D. Engage law enforcement before taking any further action.

**Correct Answer: C** — Forensic investigation must occur before restoration to preserve evidence and understand the full scope of the attack. Restoring from backup prematurely may destroy evidence needed to understand how the attacker entered, whether they persist elsewhere, and whether the backup itself is clean. Option A sacrifices forensic integrity. Option B violates need-to-know principles. Option D is not universally required as a next step.

---

## Study Checklist

Before attempting the Module 10 quiz, verify:

- [ ] I can define security event, security incident, and data breach with examples of each.

- [ ] I can name and describe all four phases of the NIST SP 800-61 lifecycle.

- [ ] I can list eight required components of an Incident Response Plan.

- [ ] I can define a severity classification framework with at least four levels.

- [ ] I can explain the purpose and application of a RACI matrix in incident response.

- [ ] I can describe the internal communication structure at each severity level.

- [ ] I can explain the need-to-know principle and why it applies during an incident.

- [ ] I can state the external notification deadline for HIPAA, GDPR, and SEC incidents.

- [ ] I can explain the role of pre-drafted notification templates.

- [ ] I can describe criteria-based escalation and give three examples of escalation triggers.

- [ ] I can explain the relationship between IRP, DRP, and BCP and their key alignment requirements.

- [ ] I can describe three types of IRP exercises and when each is appropriate.

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| IRP | Incident Response Plan — documented procedures for preparing, detecting, containing, and recovering from security incidents |
| NIST SP 800-61 | NIST Computer Security Incident Handling Guide — four-phase IR lifecycle framework |
| IRT | Incident Response Team — organizational unit responsible for executing the IRP |
| RACI matrix | Responsible, Accountable, Consulted, Informed — tool for defining accountability in team activities |
| Severity classification | Tiered system defining incident severity levels and corresponding response requirements |
| Escalation criteria | Pre-defined conditions that automatically require incident notification to higher organizational levels |
| BCP | Business Continuity Plan — procedures for maintaining essential operations during a disruption |
| DRP | Disaster Recovery Plan — procedures for restoring IT systems and data after a disruption |
| RTO | Recovery Time Objective — maximum acceptable time to restore a system or function |
| Tabletop exercise | Verbal walkthrough of a simulated scenario to test decision-making without activating real systems |
| Out-of-band communication | Communication channel independent of potentially compromised infrastructure |

---

## Recommended References

- NIST SP 800-61 Rev. 2, Computer Security Incident Handling Guide

- ISACA CISM Review Manual, Domain 4 — Incident Management

- SANS Incident Handler's Handbook

- CISA Federal Incident Notification Guidelines

- IBM Cost of a Data Breach Report (current year edition)

## 9. Supplemental Resources

**1. NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide**
https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final
The authoritative NIST framework for incident response. Defines the four-phase lifecycle (Preparation, Detection and Analysis, Containment/Eradication/Recovery, Post-Incident Activity) that underpins all IRP development covered in this module. Free download from NIST.

**2. CISA Incident Notification Guidelines for Federal Agencies**
https://www.cisa.gov/sites/default/files/publications/Federal_Incident_Notification_Guidelines.pdf
CISA's operational guidance for categorizing and reporting cybersecurity incidents, including severity taxonomy and notification timelines. Applicable to understanding structured escalation design for any organization type.

**3. SANS Institute — Incident Handler's Handbook**
https://www.sans.org/white-papers/33901/
A practitioner-level reference describing IRP components, communication planning, and evidence handling procedures. Complements the NIST framework with hands-on field guidance from experienced incident responders.

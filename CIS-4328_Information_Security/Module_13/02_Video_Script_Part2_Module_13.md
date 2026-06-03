# Video Script: Module 13 — Risk Management for Security+ (Part 2 of 2)

## Course: CIS-4328 Information Security

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: CompTIA Security+ (SY0-701)

---

## Segment 1 — The Risk Register (3 minutes)

Welcome back to Module 13. In Part 1 we established risk concepts, response strategies, and analysis methods. Now let us put those into practice with the tools that operationalize risk management.

The **risk register** is the central operational document of a risk management program. It is a living inventory of all identified risks, their assessments, and their treatment status. Every significant risk to the organization should be documented in the risk register.

A risk register entry typically contains:

- **Risk ID** — a unique identifier for tracking
- **Risk Description** — what is the risk? ("Ransomware encrypts primary file server due to unpatched vulnerability CVE-XXXX-YYYY")
- **Risk Category** — what domain does this affect? (Technology, Operational, Regulatory, Physical)
- **Threat** — what is the threat agent or threat event?
- **Vulnerability** — what weakness does the threat exploit?
- **Likelihood** — how likely is the risk to materialize? (Qualitative: L/M/H or quantitative: ARO)
- **Impact** — what is the consequence if the risk occurs? (Qualitative: L/M/H or quantitative: SLE)
- **Risk Rating** — the combined assessment (from the risk matrix or ALE calculation)
- **Risk Owner** — who is responsible for managing this risk? Not the security team — the owner of the affected asset or process
- **Current Controls** — what controls are already in place?
- **Risk Response** — Avoid / Transfer / Mitigate / Accept
- **Planned Actions** — specific mitigation steps, with deadlines
- **Residual Risk** — the remaining risk level after planned actions
- **Status** — Open / In Progress / Closed / Accepted
- **Review Date** — when will this risk be re-evaluated?

### Risk Register as a Management Tool

The risk register is not a static document — it must be reviewed and updated regularly. New risks emerge (new vulnerabilities, new threat actors, organizational changes). Existing risks change status as controls are implemented or threat landscape evolves.

Risk owners — the people responsible for managing specific risks — should review their risks at a minimum quarterly. Annual enterprise risk reviews should examine the entire register.

**Exam tip:** Security+ may ask about the purpose of a risk register. The answer is to document, track, and manage identified risks across the organization in a centralized, auditable format.

---

## Segment 2 — Business Impact Analysis (4 minutes)

The **Business Impact Analysis (BIA)** is a systematic process for identifying which business functions and systems are most critical to organizational survival and determining the impact of disruptions to those functions. The BIA informs both risk management (what to protect) and business continuity/disaster recovery planning (what to recover first and how fast).

### Why the BIA Matters for Security

The BIA tells you which assets are most valuable and where security investment should be prioritized. It also establishes the targets that recovery efforts must meet — targets that your incident response, backup, and disaster recovery plans must satisfy.

### BIA Key Metrics

**Maximum Tolerable Downtime (MTD)** — also called Maximum Acceptable Outage (MAO) — the longest period of time the organization can survive without a particular business function before the impact becomes catastrophic. If the payroll system is unavailable for more than three days, employees cannot be paid on time — this might be the MTD for payroll.

**RTO (Recovery Time Objective)** — the target time to restore a business function or system after a disruption. RTO must be less than the MTD. If the MTD for the e-commerce platform is 4 hours, the RTO must be less than 4 hours — otherwise the backup/recovery plan will fail to meet business requirements.

**RPO (Recovery Point Objective)** — the maximum acceptable amount of data loss measured in time. An RPO of 1 hour means the organization can accept losing up to 1 hour of transactions in a recovery scenario. The RPO drives your backup frequency: if RPO = 1 hour, backups must occur at least hourly.

**MTBF (Mean Time Between Failures)** — the average time between system failures. A server with MTBF of 50,000 hours fails approximately once every 5.7 years. Used to predict reliability and justify redundancy investments.

**MTTR (Mean Time to Repair/Recover)** — the average time to repair or recover a system after a failure. In the IR context (Module 11), MTTR measures incident recovery time. In BIA, it measures technical repair time.

### Performing a BIA

The BIA process:

1. **Identify critical business functions** — what does the organization do that, if stopped, would severely harm the business? Payment processing, patient care delivery, manufacturing line, customer order fulfillment.

2. **Identify supporting systems and assets** — what IT systems, applications, and data underpin each critical function?

3. **Determine MTD for each function** — interview business stakeholders. They know how long they can operate manually, with workarounds, or not at all.

4. **Assess the impact of disruption** — financial loss per hour of downtime, regulatory consequences, reputational damage, customer impact.

5. **Set RTO and RPO** — derive from MTD and business stakeholder requirements.

6. **Prioritize** — rank critical functions by their MTD (shorter MTD = higher priority for recovery).

The BIA output feeds directly into:

- Disaster Recovery Planning (which systems to recover first)
- Backup strategy (backup frequency, retention, offsite storage)
- High availability architecture decisions (which systems need redundancy)
- Security investment prioritization (what to protect most)

---

## Segment 3 — Security Controls Classification (4 minutes)

Security controls are the safeguards implemented to reduce risk. Security+ organizes controls in two dimensions: by **function** and by **type**.

### Controls by Function

**Preventive controls** — designed to stop a threat from being realized before it occurs. They reduce vulnerability or likelihood.

Examples:

- Firewalls (prevent unauthorized network access)
- Encryption (prevents unauthorized data reading)
- Input validation (prevents injection attacks)
- MFA (prevents unauthorized account access)
- Security awareness training (prevents successful phishing)

**Detective controls** — designed to identify that a threat has occurred or is occurring.

Examples:

- IDS/IPS (detects attack traffic patterns)
- SIEM (detects anomalous behavior patterns across logs)
- Security cameras (detects unauthorized physical access)
- Audit logs (detects unauthorized data access)
- Vulnerability scanners (detects misconfigured or unpatched systems)

**Corrective controls** — designed to limit the damage after a threat is realized and restore normal operations.

Examples:

- Backup and restore systems (corrects data loss)
- Incident response procedures (corrects the effects of an incident)
- Patch management (corrects the vulnerability after it has been exploited)
- Disaster recovery plans (corrects business disruption)

**Deterrent controls** — designed to discourage a threat from attempting an attack. They do not prevent or detect — they reduce the motivation of the threat.

Examples:

- Visible security cameras (deters physical intrusion attempts)
- Warning banners on systems ("Unauthorized access is prohibited and monitored")
- Prosecution and publicized examples of enforcement (deters malicious actors)

**Compensating controls** — controls implemented to satisfy a requirement when the primary control is not feasible. They provide alternative coverage.

Example: A legacy system cannot support MFA. The compensating controls are network isolation (limiting access to the system), enhanced monitoring, and privileged access management requiring a separate jump server.

**Directive controls** — policies, procedures, and standards that direct people to behave in certain ways.

Examples:

- Acceptable use policies
- Security policies and standards
- Data classification policy
- Procedures for handling sensitive data

### Controls by Type

**Technical controls (Logical controls)** — implemented through technology.

Examples: firewalls, encryption, access control systems, IDS, antivirus, MFA

**Administrative controls (Managerial controls)** — implemented through policies, procedures, and management processes.

Examples: security awareness training, background checks, separation of duties, risk assessments, change management procedures

**Physical controls** — implemented through physical security measures.

Examples: locks, badge readers, security guards, fences, cable locks, environmental controls (temperature, fire suppression)

### Combining the Dimensions

The two classification dimensions can be combined. A security camera is a physical, detective control. An acceptable use policy is an administrative, directive control. Network segmentation is a technical, preventive control. This combined classification is how Security+ scenario questions are structured: "What type of control is a firewall? A physical detective control / A technical preventive control / An administrative corrective control / A physical deterrent control?"

**The answer: a technical preventive control.**

### Defense in Depth Using Control Types

Defense in depth means layering controls from different categories so that the failure of one does not result in full compromise:

- Physical layer: biometric door locks (physical, preventive)
- Network layer: firewall and IDS (technical, preventive + detective)
- Endpoint layer: EDR and patching (technical, detective + corrective)
- Application layer: input validation and SAST (technical, preventive)
- Identity layer: MFA and PAM (technical, preventive)
- Data layer: encryption and DLP (technical, preventive)
- Administrative layer: training and policy (administrative, directive + preventive)

Each layer independently reduces risk. An attacker who defeats the physical controls still faces the network controls. An attacker who bypasses the network controls still faces the endpoint controls.

---

## Segment 4 — Risk Management Frameworks (4 minutes)

Risk management does not happen in a vacuum — it is guided by frameworks that provide structure, vocabulary, and methodology. Security+ tests your awareness of the major frameworks.

### NIST Risk Management Framework (RMF)

The NIST RMF (NIST SP 800-37) is the comprehensive risk management process required for US federal information systems and widely adopted in private sector. It has six steps:

1. **Categorize** — categorize the information system and the data it processes based on impact (FIPS 199)
2. **Select** — select security controls appropriate to the system's impact level (NIST SP 800-53)
3. **Implement** — implement the selected security controls
4. **Assess** — assess whether controls are implemented correctly, operating as intended, and producing desired results
5. **Authorize** — a senior official makes a risk-based authorization decision (Authority to Operate)
6. **Monitor** — continuously monitor controls and the threat environment

The RMF is not a one-time exercise — it is an ongoing process. Security controls are continuously monitored, and the authorization is periodically reviewed.

### ISO 31000 — Risk Management Guidelines

ISO 31000 is an international standard providing principles and guidelines for risk management across all types of organizations. It is not prescriptive about specific controls — it provides a framework for establishing a risk management program. Key components:

- Risk management principles (integrated, structured, inclusive, dynamic)
- Risk management framework (leadership commitment, integration, design, implementation, evaluation, improvement)
- Risk management process (communication, establishing context, risk assessment, risk treatment, monitoring, recording)

### NIST Cybersecurity Framework (CSF)

The NIST CSF organizes cybersecurity activities into five core functions that can be used to assess and improve risk posture:

1. **Identify** — understand assets, risks, and governance
2. **Protect** — implement controls to limit impact of potential events
3. **Detect** — develop capabilities to identify cybersecurity events
4. **Respond** — take action when a cybersecurity event is detected
5. **Recover** — restore capabilities and services after a cybersecurity event

The CSF is not prescriptive — organizations self-assess against it to identify gaps and prioritize improvements.

### COSO ERM Framework

COSO (Committee of Sponsoring Organizations) ERM (Enterprise Risk Management) framework is widely used in corporate governance contexts, particularly for financial services and publicly traded companies. It integrates cybersecurity risk into enterprise-wide risk management rather than treating it as a separate discipline.

---

## Module 13 Full Summary

Risk management is the overarching discipline that gives security work its direction and business alignment:

- Core formula: Risk = Threat × Vulnerability × Impact. Reducing any factor reduces overall risk.
- Risk vocabulary: appetite, tolerance, threshold, inherent risk, residual risk
- Four risk response strategies: Avoidance, Transference, Mitigation, Acceptance — and the importance of documented acceptance
- Quantitative analysis: AV → EF → SLE → ARO → ALE → cost-benefit evaluation
- Qualitative analysis: risk matrix mapping likelihood vs. impact
- Risk register: the living inventory of risks with ownership, status, and treatment tracking
- BIA: identifies critical functions, establishes MTD, RTO, RPO, and MTBF/MTTR metrics
- Security controls by function: Preventive, Detective, Corrective, Deterrent, Compensating, Directive
- Security controls by type: Technical, Administrative, Physical
- Frameworks: NIST RMF, NIST CSF, ISO 31000

This module completes the foundational content arc of this course. You now have the vocabulary and framework to think about security not as a series of technical tasks but as a risk management discipline. That perspective will serve you well on the Security+ exam and throughout your career. Complete the reading, lab, and quiz. I will see you in Module 14.

---

*End of Part 2 Script*

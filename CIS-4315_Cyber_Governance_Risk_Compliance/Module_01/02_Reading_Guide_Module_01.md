# Reading Guide: Module 01 — Information Security Governance Foundations

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

## CISM Domain Alignment: Domain 1 — Information Security Governance (17% of exam)

---

## Introduction

Welcome to Module 01. This reading guide supports the video lecture and prepares you for the lab, quiz, and discussion activities. Information security governance is the strategic foundation of the entire CISM certification, and mastering it now pays dividends across all subsequent modules.

As you work through this guide, read every definition carefully and ask yourself: how does this concept connect to a business decision? The CISM exam consistently tests your ability to think like a security manager advising executive leadership, not like a technician configuring systems.

---

## Section 1: Core Definitions and Concepts

### 1.1 Information Security Governance

Information security governance is the system of policies, accountability structures, and decision-making processes through which an organization directs and controls its information security program. It answers three fundamental governance questions:

- Who is accountable for information security outcomes?
- What direction has the organization set for its security program?
- How does the organization know whether its security program is effective?

Governance is not the same as management. Governance sets direction and holds management accountable. Management executes the direction that governance has established.

### 1.2 The CIA Triad

The CIA triad is the foundational model for evaluating security requirements. Every security control, policy, and governance decision ultimately serves one or more of its three components.

**Confidentiality** is the property that information is not made available or disclosed to unauthorized individuals, entities, or processes. Confidentiality failures include unauthorized data access, data breaches, and accidental disclosure.

**Integrity** is the property that information has not been altered or destroyed in an unauthorized manner. Integrity failures include unauthorized modification of records, tampering with audit logs, and corruption of configuration files.

**Availability** is the property that information and information systems are accessible and usable upon demand by an authorized entity. Availability failures include denial-of-service attacks, ransomware, and unplanned system outages.

### 1.3 Risk Appetite

Risk appetite is the amount and type of risk an organization is willing to accept in pursuit of its objectives. It is set by the board of directors and expressed as a policy-level statement. The security program must operate within the boundaries of the stated risk appetite.

Risk appetite is distinct from risk tolerance, which is the acceptable variation around a specific risk objective. An organization may have a low risk appetite for regulatory compliance failures but a moderate risk tolerance for minor operational disruptions.

### 1.4 Security Strategy Alignment

Security strategy alignment is the process of ensuring that the information security program supports and enables the organization's overall business strategy and mission. Aligned security programs justify investments in terms of business objectives, not just threat mitigation.

### 1.5 Information Security Policy

An information security policy is a high-level, board-approved document that states the organization's commitment to protecting information assets and establishes the overall framework for the security program. It is the top of the policy hierarchy and must be reviewed and reapproved at least annually.

### 1.6 Policy Hierarchy

The policy hierarchy provides a structured framework for documenting security requirements at different levels of specificity.

| Level | Document Type | Purpose | Approval Authority |
|---|---|---|---|
| 1 | Information Security Policy | States commitment and overall framework | Board / Executive |
| 2 | Standards | Mandatory specific requirements | CISO / Steering Committee |
| 3 | Procedures | Step-by-step implementation instructions | Security Management |
| 4 | Guidelines | Recommended practices (not mandatory) | Security Management |
| 5 | Baselines | Minimum security configurations | Security Architecture |

### 1.7 Security Steering Committee

A security steering committee is an interdisciplinary governance body that provides oversight and direction for the information security program. It typically includes the CISO, CIO, CFO, Chief Risk Officer, legal counsel, and senior business unit leaders. The committee approves security policies, prioritizes investments, and reviews the organization's overall risk posture.

### 1.8 Data Owner

A data owner is a business manager who has been assigned responsibility for a specific set of data. The data owner is accountable for classifying the data, ensuring appropriate controls are in place, and making decisions about risk acceptance. Data ownership is a business function, not an IT function.

### 1.9 Data Custodian

A data custodian is typically an IT role responsible for the technical storage, maintenance, and protection of data on behalf of the data owner. The custodian implements the controls that the data owner requires but does not have authority to change classification or accept risk.

---

## Section 2: Governance Frameworks

### 2.1 COBIT 2019

COBIT (Control Objectives for Information and Related Technologies) is ISACA's governance framework for enterprise IT. It provides a comprehensive set of governance and management objectives organized into five domains.

COBIT distinguishes clearly between governance objectives (overseen by the board and executive level) and management objectives (executed by IT management). This distinction mirrors the CISM exam's core governance-versus-management theme.

Key COBIT 2019 governance objectives include:

- EDM01: Ensure Governance Framework Setting and Maintenance
- EDM02: Ensure Benefits Delivery
- EDM03: Ensure Risk Optimization
- EDM04: Ensure Resource Optimization
- EDM05: Ensure Stakeholder Engagement

### 2.2 ISO/IEC 27001

ISO/IEC 27001 is the international standard for Information Security Management Systems (ISMS). An ISMS is a systematic, risk-based approach to managing information security across an organization.

The standard is structured around the Plan-Do-Check-Act (PDCA) cycle:

| PDCA Phase | ISO 27001 Activity |
|---|---|
| Plan | Define scope, risk assessment, select controls |
| Do | Implement controls and security program |
| Check | Monitor, measure, audit, review |
| Act | Correct deficiencies, continually improve |

ISO 27001 certification requires an accredited third-party audit. Annex A of the standard contains 93 control categories (as of the 2022 version) organized into four themes: Organizational, People, Physical, and Technological.

### 2.3 NIST Cybersecurity Framework (CSF)

The NIST CSF organizes security activities into five core functions that can be used to communicate security posture at a governance level.

| NIST CSF Function | Description | Governance Relevance |
|---|---|---|
| Identify | Asset management, risk assessment, governance | Directly relevant to Module 01 |
| Protect | Access control, training, data security | Security program scope |
| Detect | Continuous monitoring, anomaly detection | Security operations |
| Respond | Incident response planning and execution | Modules 09-10 |
| Recover | Recovery planning, communications | Modules 10-11 |

The NIST CSF is voluntary but widely adopted in critical infrastructure and federal agencies. It is referenced in CISM study materials as an example of a risk-based governance communication tool.

### 2.4 Framework Comparison Summary

| Attribute | COBIT 2019 | ISO/IEC 27001 | NIST CSF |
|---|---|---|---|
| Produced by | ISACA | ISO/IEC | NIST |
| Primary focus | IT governance | ISMS certification | Risk-based security |
| Certification available | No | Yes | No |
| Mandatory | Rarely | Contractually sometimes | Rarely |
| CISM exam relevance | High | High | Moderate |

---

## Section 3: Governance Roles and Accountability

### 3.1 Board of Directors

The board is the highest governance authority. Its security responsibilities include:

- Setting the organization's risk appetite
- Ensuring adequate security oversight structures exist
- Holding executive management accountable for security outcomes
- Reviewing significant security incidents and risk reports

### 3.2 Executive Leadership (CEO, CFO, CRO)

Executive leadership translates board-level risk appetite into organizational strategy and resource allocation. The CEO is ultimately accountable to the board for all enterprise risk, including information security risk.

### 3.3 Chief Information Security Officer (CISO)

The CISO leads the information security program. Key CISO responsibilities include:

- Developing and maintaining the information security strategy
- Reporting security posture to the board and executive team
- Managing the security team and security program budget
- Ensuring the security program operates within the risk appetite
- Communicating security in business terms to non-technical stakeholders

### 3.4 Security Steering Committee

The steering committee provides the governance layer between the board and the CISO. It approves policies, resolves cross-departmental security conflicts, and ensures that security investments align with business priorities.

### 3.5 Data Owner vs. Data Custodian

| Role | Responsibility | Business or IT? |
|---|---|---|
| Data Owner | Classifies data, accepts risk | Business |
| Data Custodian | Implements and maintains controls | IT |
| Data User | Accesses data per authorization | End User |

---

## Section 4: The Five Outcomes of Information Security Governance

ISACA defines five essential outcomes of effective security governance. These outcomes are tested directly in CISM Domain 1 scenario questions.

| Outcome | Definition | Example Indicator |
|---|---|---|
| Strategic Alignment | Security supports business objectives | Security roadmap tied to business goals |
| Risk Management | Risks managed within risk appetite | Risk register reviewed quarterly |
| Resource Management | Security resources allocated efficiently | Budget justified by risk reduction |
| Performance Management | Measurable security objectives tracked | KPIs reported to steering committee |
| Value Delivery | Security enables business value | New products enabled by compliant controls |

---

## Section 5: NIST SP 800-39 — Enterprise Risk Governance

NIST Special Publication 800-39, "Managing Information Security Risk," provides a three-tier governance model for enterprise risk management.

- Tier 1 (Organization): Strategy, risk framing, risk appetite, governance structure
- Tier 2 (Mission/Business Process): Security requirements for business processes
- Tier 3 (Information System): System-level risk assessment and controls

This three-tier model illustrates why governance cannot be confined to IT. Risk decisions at Tier 1 flow down through business processes at Tier 2 to influence system-level controls at Tier 3. Security managers must understand and engage all three tiers.

---

## Section 6: Common Governance Failures

Understanding what governance failure looks like helps you recognize correct governance in exam scenarios.

| Failure Mode | Description | Governance Gap |
|---|---|---|
| Security operates in IT silo | No executive sponsorship or business alignment | Lack of strategic alignment |
| No risk appetite statement | Security team cannot make risk decisions | Missing governance direction |
| Policies never reviewed | Controls become stale relative to threat environment | Performance management failure |
| No steering committee | Security investments lack business input | Accountability gap |
| CISO reports to CIO only | Security interests subordinated to IT priorities | Independence issue |

---

## Section 7: CISM Exam Tips

The following eight tips reflect the most common governance pitfalls in Domain 1 exam questions.

**Exam Tip 1 — Management perspective.** CISM tests you as a manager, not a technician. When choosing between answers, always favor the option that addresses organizational risk, business alignment, or governance accountability over technical controls.

**Exam Tip 2 — Governance vs. management.** The board governs; the CISO manages. Governance sets direction and holds management accountable. Management executes. This distinction appears in dozens of exam scenarios.

**Exam Tip 3 — Who approves what.** Policies are approved by the board or executive leadership, not by IT. Risk decisions are made by business owners, not the security team.

**Exam Tip 4 — Risk appetite belongs to the board.** The board sets risk appetite. The CISO implements controls to operate within it. The CISO does not independently decide how much risk to accept.

**Exam Tip 5 — CIA triad mapping.** Practice matching real-world scenarios to CIA components. Ransomware is primarily an availability threat. Phishing leading to credential theft is primarily a confidentiality threat. Unauthorized record modification is an integrity threat.

**Exam Tip 6 — Five governance outcomes.** Memorize the five ISACA governance outcomes: strategic alignment, risk management, resource management, performance management, and value delivery. Questions may present a governance failure and ask which outcome is missing.

**Exam Tip 7 — Data owner is business, not IT.** The data owner classifies data and accepts risk. The data custodian (IT) implements controls. Misidentifying this responsibility is a common wrong-answer trap.

**Exam Tip 8 — First action in governance scenarios.** When an exam scenario describes a governance problem (e.g., security is not aligned with business, executives do not support security), the correct first action is almost always to establish executive sponsorship or align with business strategy — not to implement a technical control.

---

## Section 8: Required Reading

The following sources are available at no cost and directly support module learning objectives.

NIST Special Publication 800-39, "Managing Information Security Risk: Organization, Mission, and Information System View," is available at no cost from the NIST Computer Security Resource Center. Focus on Section 2 (Framing Risk) and Section 3 (Risk Response). This document directly supports CISM Domain 1 study.

ISACA publishes governance resources, white papers, and CISM exam preparation materials at isaca.org. The CISM Review Manual is the authoritative exam preparation resource.

---

## Section 9: Study Checklist

Work through each item before moving to the quiz.

- [ ] Define information security governance in your own words without looking at the guide
- [ ] Explain the difference between governance and management using one original analogy
- [ ] List the three CIA triad components and give one example of a failure for each
- [ ] Describe the five ISACA governance outcomes from memory
- [ ] Name the three major governance frameworks and one distinguishing characteristic of each
- [ ] Identify the four levels of the policy hierarchy and explain who approves each
- [ ] Distinguish between a data owner and a data custodian
- [ ] Explain what a risk appetite statement is and who is responsible for setting it
- [ ] Identify at least three common governance failure modes
- [ ] Review all eight CISM exam tips and note which concepts feel least familiar
- [ ] Complete the Module 01 lab before attempting the quiz
- [ ] Post your initial discussion response by Wednesday at 11:59 PM

---

Reading Guide — Module 01 | CIS-4315 | Texas Wesleyan University

---

## 9. Supplemental Resources

The following resources extend the Module 01 content and are recommended for CISM exam preparation and professional practice.

**NIST Cybersecurity Framework 2.0**
URL: https://www.nist.gov/cyberframework
Description: The authoritative NIST CSF 2.0 document, freely available. Includes the new Govern function, implementation tiers, and profiles. Essential reading for understanding how governance drives the entire framework. Read the Executive Summary and the Govern function overview.

**ISACA COBIT 2019 Framework: Introduction and Methodology**
URL: https://www.isaca.org/resources/cobit
Description: ISACA's official COBIT 2019 documentation, available free to ISACA members. The Introduction and Methodology volume explains the governance/management distinction, the goals cascade, and the design factors. Directly aligned with CISM Domain 1.

**ISO/IEC 27001:2022 Overview — ISO.org**
URL: https://www.iso.org/standard/27001
Description: The official ISO page for the ISO/IEC 27001:2022 standard. Explains the ISMS structure and the relationship between ISO 27001 requirements and ISO 27002 controls. Useful for understanding how the standard translates governance requirements into an auditable management system.

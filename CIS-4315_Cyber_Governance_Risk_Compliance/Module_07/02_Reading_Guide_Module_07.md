# Reading Guide: Module 07 — Security Architecture and Controls

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Introduction

Module 07 focuses on how security programs translate policy and strategy into operational reality: the security architecture that organizes controls, and the controls themselves that reduce risk. Understanding security architecture is essential for CISM candidates because Domain 3 tests not just what controls exist, but how they are organized, selected, and justified.

This reading guide provides structured reference material covering defense-in-depth, the major control frameworks, the NIST Cybersecurity Framework in depth, and the primary control domains. Use it alongside the video lecture and as a reference when completing the lab.

---

## 1. Defense-in-Depth

### 1.1 Core Concept

Defense-in-depth is the principle of layering multiple independent security controls so that the failure of any single control does not result in a successful attack or breach. The concept draws from military strategy: an adversary who penetrates one defensive layer immediately faces another, imposing cumulative cost and detection risk.

In information security, layers are defined both by their physical or logical position (perimeter, network, host, application, data) and by their control type (preventive, detective, corrective).

### 1.2 Control Types

| Control Type | Purpose | Examples |
|---|---|---|
| Preventive | Stop attacks before they succeed | Firewall, access control, encryption, MFA |
| Detective | Identify attacks in progress or after the fact | IDS/IPS, SIEM, audit logs, DLP alerts |
| Corrective | Restore normal operations after an attack | Backup restoration, patch deployment, incident response |
| Deterrent | Discourage attackers from attempting | Warning banners, visible cameras, audit clauses |
| Compensating | Substitute for a primary control that cannot be implemented | Enhanced monitoring when a patch cannot be applied |

### 1.3 Control Categories

| Control Category | Definition | Examples |
|---|---|---|
| Technical | Implemented in hardware, software, or firmware | Firewalls, EDR, encryption, MFA systems |
| Administrative | Policies, procedures, and management processes | Security policy, background checks, training requirements |
| Physical | Tangible safeguards for facilities and hardware | Locks, badge readers, security cameras, shredding |

### 1.4 Defense-in-Depth Architecture Layers

| Layer | Description | Representative Controls |
|---|---|---|
| Perimeter | Boundary between internal network and external networks | Next-gen firewall, DDoS mitigation, WAF |
| Network | Internal network traffic controls and segmentation | VLANs, IPS, network segmentation, NAC |
| Host | Individual device protection | EDR, host firewall, disk encryption, patch management |
| Application | Controls within software applications | Authentication, session management, input validation |
| Data | Protection of information assets directly | Encryption at rest, DLP, IRM, access control |

---

## 2. Security Control Frameworks

### 2.1 Framework Comparison Overview

| Framework | Publisher | Primary Use | Mandatory? |
|---|---|---|---|
| NIST SP 800-53 Rev 5 | NIST (US Government) | Comprehensive control catalog | Required for US federal agencies |
| ISO/IEC 27001:2022 | ISO/IEC | ISMS certification standard | Voluntary; certifiable |
| CIS Controls v8 | Center for Internet Security | Prioritized implementation guide | Voluntary |
| NIST CSF 2.0 | NIST (US Government) | Program structure and communication | Voluntary |
| PCI DSS v4.0 | PCI SSC | Payment card security | Required for card processors |

### 2.2 NIST SP 800-53 — Control Families

NIST SP 800-53 Rev 5 organizes controls into 20 families. Key families for CISM candidates:

| Family Code | Family Name | Relevance |
|---|---|---|
| AC | Access Control | Identity and access management requirements |
| AT | Awareness and Training | Security training program requirements |
| AU | Audit and Accountability | Logging and monitoring requirements |
| CA | Assessment, Authorization, Monitoring | Security assessments and continuous monitoring |
| CM | Configuration Management | Baseline configurations and change control |
| CP | Contingency Planning | BCP/DR requirements |
| IA | Identification and Authentication | Identity verification requirements |
| IR | Incident Response | Incident handling requirements |
| PM | Program Management | Security program governance requirements |
| RA | Risk Assessment | Risk assessment process requirements |
| SC | System and Communications Protection | Network and cryptographic controls |
| SI | System and Information Integrity | Malware protection and patch management |

### 2.3 ISO/IEC 27001:2022 — Annex A Control Themes

ISO 27001:2022 reorganized its controls into four themes, replacing the 14-category structure of the 2013 version:

| Theme | Control Count | Focus Areas |
|---|---|---|
| Organizational | 37 | Policies, roles, supplier relationships, incident management, business continuity |
| People | 8 | Screening, terms of employment, training, disciplinary process |
| Physical | 14 | Physical security perimeters, equipment security, media handling |
| Technological | 34 | Access control, cryptography, network security, system acquisition |

The management system clauses (4–10) are equally important for certification: Context, Leadership, Planning, Support, Operations, Performance Evaluation, and Improvement.

### 2.4 CIS Controls v8 — Implementation Groups

CIS Controls v8 defines 18 controls and three Implementation Groups (IGs) that prioritize controls based on organizational size and risk profile.

| Implementation Group | Target Organization | Controls Included |
|---|---|---|
| IG1 — Essential Cyber Hygiene | Small organizations, limited resources | Subset of all 18 controls (56 safeguards) |
| IG2 — Foundational | Mid-size organizations with security staff | IG1 + additional controls (74 safeguards) |
| IG3 — Organizational | Large organizations with mature programs | All 18 controls (153 safeguards) |

The first six CIS Controls are considered foundational for every organization:

1. Inventory and Control of Enterprise Assets
2. Inventory and Control of Software Assets
3. Data Protection
4. Secure Configuration of Enterprise Assets and Software
5. Account Management
6. Access Control Management

---

## 3. NIST Cybersecurity Framework 2.0

### 3.1 CSF Functions Overview

The NIST CSF organizes security activities into six functions. CSF 2.0 (released February 2024) added the Govern function to the original five.

| Function | Core Question Answered | Key Categories |
|---|---|---|
| Govern | How do we manage cybersecurity risk organizationally? | Organizational context, risk strategy, roles, policies, oversight |
| Identify | What assets and risks do we have? | Asset management, risk assessment, improvement |
| Protect | How do we prevent and limit impact? | Identity management, awareness/training, data security, platform security |
| Detect | How do we find cybersecurity events? | Continuous monitoring, adverse event analysis |
| Respond | How do we act on detected incidents? | Incident management, analysis, mitigation, reporting |
| Recover | How do we restore capabilities after incidents? | Incident recovery plan, communication, improvements |

### 3.2 CSF Tiers

Tiers describe the sophistication of an organization's cybersecurity risk management practices. They are descriptive, not prescriptive — higher is not always better if the cost exceeds the benefit.

| Tier | Name | Characteristics |
|---|---|---|
| 1 | Partial | Ad hoc, reactive, limited awareness of risk |
| 2 | Risk Informed | Risk management practices exist but are not enterprise-wide |
| 3 | Repeatable | Formal, documented, consistently applied practices |
| 4 | Adaptive | Actively adapts based on threat intelligence and lessons learned |

### 3.3 CSF Profiles

A CSF Profile expresses an organization's security posture in terms of CSF outcomes.

- **Current Profile**: Documents the cybersecurity outcomes the organization is currently achieving
- **Target Profile**: Documents the outcomes the organization aims to achieve
- **Gap Analysis**: Comparison between Current and Target Profiles that drives the security roadmap

Profiles can be used to communicate with business leadership, compare against peers, or satisfy regulatory requirements that reference the CSF.

### 3.4 CSF Use Cases by Stakeholder

| Stakeholder | Primary CSF Use |
|---|---|
| Board of Directors | Tier assessment, Target Profile approval |
| CISO | Strategy development, gap analysis, roadmap |
| Security Architects | Control selection mapped to CSF categories |
| Auditors | Assess Current Profile against Target Profile |
| Regulators | Reference framework for sector-specific profiles |

---

## 4. Network Controls

### 4.1 Perimeter Controls

| Control | Function | Key Considerations |
|---|---|---|
| Next-Generation Firewall (NGFW) | Application-layer traffic filtering | Application ID, user ID, intrusion prevention integrated |
| Web Application Firewall (WAF) | Protect web applications from OWASP Top 10 | SQL injection, XSS, CSRF protection |
| Intrusion Prevention System (IPS) | Block known attack signatures and anomalies | Signature updates, false positive tuning |
| DDoS Mitigation | Absorb or deflect volumetric attacks | Cloud-based scrubbing centers for large attacks |

### 4.2 Network Segmentation

Segmentation divides the network into security zones, limiting lateral movement and containing breaches.

Key segmentation zones:

- **DMZ (Demilitarized Zone)**: Internet-facing servers accessible from outside and inside, isolated from the internal network
- **Trusted Zone**: Internal corporate systems, highest trust
- **OT/ICS Zone**: Operational technology systems, often air-gapped or strictly segmented
- **Guest Zone**: Visitor and BYOD devices, no access to corporate resources
- **Management Zone**: Out-of-band network management, highly restricted access

### 4.3 Zero Trust Architecture

Zero Trust replaces the "trust but verify" model of perimeter-based security with "never trust, always verify."

Core Zero Trust principles:

- Verify every user and device explicitly at every access request
- Apply least-privilege access — minimum access needed for the task
- Assume breach — design as though the network is already compromised
- Microsegment workloads to limit blast radius

---

## 5. Endpoint Controls

### 5.1 Endpoint Protection Evolution

| Generation | Technology | Capability |
|---|---|---|
| 1st Gen | Signature-based antivirus | Known malware identification |
| 2nd Gen | Heuristic/behavioral AV | Unknown malware detection |
| 3rd Gen | EDR (Endpoint Detection and Response) | Behavioral detection, telemetry, threat hunting |
| 4th Gen | XDR (Extended Detection and Response) | Cross-domain telemetry (endpoint + network + cloud) |

### 5.2 Key Endpoint Controls

| Control | Purpose | Best Practice |
|---|---|---|
| EDR | Detect and respond to endpoint threats | Deploy with managed detection or SOC integration |
| Patch Management | Eliminate known vulnerabilities | Critical patches within 14 days; routine within 30 days |
| Disk Encryption | Protect data on lost/stolen devices | Full-disk encryption with centrally escrowed keys |
| Application Control | Prevent unauthorized software execution | Allowlisting for high-risk systems; denylisting baseline |
| Host Firewall | Filter traffic at the device level | Default-deny inbound; restrict outbound by application |
| Privileged Access Management | Control and monitor admin credentials | Just-in-time access, session recording, no shared accounts |

---

## 6. Data Controls

### 6.1 Data Classification Scheme

| Classification Level | Description | Example Controls |
|---|---|---|
| Public | Approved for public release | No special controls required |
| Internal | For internal use; not for public release | Access control, clean desk policy |
| Confidential | Sensitive business or customer data | Encryption, DLP, access logging |
| Restricted | Highest sensitivity; regulatory or legal protection required | Encryption, IRM, strict need-to-know access, audit |

### 6.2 Encryption Reference

| Use Case | Recommended Standard | Notes |
|---|---|---|
| Data at rest (disks) | AES-256 | Full-disk or file-level depending on risk |
| Data in transit (web) | TLS 1.3 preferred, TLS 1.2 minimum | Disable SSL, TLS 1.0, TLS 1.1 |
| Database encryption | AES-256 with column-level for sensitive fields | Transparent data encryption (TDE) for baseline |
| Email encryption | S/MIME or PGP for sensitive communications | Gateway encryption for bulk email |
| Key management | HSM for critical keys; centralized KMS | Key rotation policy; escrow for business continuity |

### 6.3 Data Loss Prevention (DLP)

DLP identifies and prevents unauthorized transmission of sensitive data.

| DLP Deployment Mode | Coverage | Example Use Case |
|---|---|---|
| Network DLP | Email, web, and FTP traffic | Block outbound emails containing SSNs |
| Endpoint DLP | USB, print, clipboard, local apps | Prevent copying classified files to USB drives |
| Cloud DLP | Cloud storage and SaaS applications | Alert on credit card data uploaded to personal cloud |
| Discovery DLP | Scans repositories for misplaced sensitive data | Find PII stored in unprotected file shares |

---

## 7. CISM Exam Tips — Module 07

**Defense-in-depth:**

- When an exam scenario describes a breach that succeeded despite having a firewall, the answer almost always involves a missing control at a different layer — a detective control (no monitoring) or a host control (no EDR)
- Compensating controls are explicitly recognized by most frameworks as acceptable alternatives when primary controls cannot be implemented

**Framework selection:**

- NIST 800-53: Use when you need a comprehensive control catalog, especially for government or highly regulated industries
- NIST CSF: Use when you need to communicate security program maturity to business leadership or assess gaps
- CIS Controls: Use when you need to prioritize limited resources on the highest-impact controls
- ISO 27001: Use when you need external certification of your security management system

**Control classification:**

- The exam frequently presents a control and asks you to classify it — know all five types (preventive, detective, corrective, deterrent, compensating) and all three categories (technical, administrative, physical)
- A single control can belong to multiple types: an audit log is both detective and corrective (it supports both detection and post-incident investigation)

**Zero Trust:**

- Zero Trust is an architecture philosophy, not a product — questions testing this concept focus on principles (verify explicitly, least privilege, assume breach) rather than specific tools

---

## 8. Key Terms Glossary

| Term | Definition |
|---|---|
| Defense-in-depth | Layered security approach using multiple independent controls across architecture layers |
| Preventive control | Control that stops attacks before they succeed |
| Detective control | Control that identifies attacks in progress or after the fact |
| Corrective control | Control that restores normal operations after an attack |
| NIST SP 800-53 | Comprehensive security control catalog for federal and other organizations |
| ISO/IEC 27001 | International standard for information security management systems |
| CIS Controls | 18 prioritized security safeguards organized by implementation group |
| NIST CSF | Cybersecurity Framework with six functions: Govern, Identify, Protect, Detect, Respond, Recover |
| CSF Tier | Maturity descriptor for cybersecurity risk management practices (1–4) |
| CSF Profile | Expression of current or target security posture in CSF terms |
| Zero Trust | Architecture model requiring explicit verification of every access request |
| Network segmentation | Dividing a network into security zones to limit lateral movement |
| EDR | Endpoint Detection and Response — behavioral threat detection and response tool |
| DLP | Data Loss Prevention — technology preventing unauthorized data transmission |
| Data classification | Labeling data by sensitivity to guide proportional control application |

---

## 9. Required and Recommended Readings

**Required (Zero-Textbook-Cost resources):**

- NIST CSF 2.0 Core — [nist.gov/cyberframework](https://www.nist.gov/cyberframework) — Review the six functions and their categories
- CIS Controls v8 Overview — [cisecurity.org/controls](https://www.cisecurity.org/controls/cis-controls-list) — Review the 18 controls and three Implementation Groups
- NIST SP 800-53 Rev 5 Control Families Overview — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) — Review the 20 family descriptions

**Recommended:**

- OWASP Top 10 (2021) — [owasp.org/Top10](https://owasp.org/www-project-top-ten/) — Application security control context
- Zero Trust Architecture (NIST SP 800-207) — [csrc.nist.gov](https://csrc.nist.gov/publications/detail/sp/800-207/final) — Conceptual overview of ZTA principles

---

## 10. Study Checklist

- [ ] Explain defense-in-depth using the layered architecture model
- [ ] Classify any given control as preventive, detective, or corrective AND as technical, administrative, or physical
- [ ] Identify the correct framework for a given organizational scenario (800-53 vs. CSF vs. CIS vs. ISO 27001)
- [ ] Name all six NIST CSF 2.0 functions and the core question each answers
- [ ] Distinguish CSF Tiers from CSF Profiles and explain how each is used
- [ ] Describe the purpose and deployment modes of DLP
- [ ] Explain the core principles of Zero Trust architecture
- [ ] Complete the Module 07 lab (CSF mapping and gap analysis)
- [ ] Take the Module 07 quiz
- [ ] Post to the Module 07 discussion forum by Wednesday 11:59 PM

---

## 11. Supplemental Resources

**NIST SP 800-207 — Zero Trust Architecture**
URL: https://csrc.nist.gov/publications/detail/sp/800-207/final
Description: Free NIST publication providing the authoritative definition and conceptual framework for Zero Trust Architecture. Covers the seven tenets of ZTA, the logical components of a Zero Trust deployment (Policy Decision Point, Policy Enforcement Point), and deployment models for organizations migrating from perimeter-based architectures. Essential reading for understanding the Zero Trust principles covered in Section 6 of this module.

**CIS Controls v8 — Full Document with Implementation Groups**
URL: https://www.cisecurity.org/controls/v8
Description: The Center for Internet Security's free Controls v8 publication provides the complete list of 18 control families and 153 safeguards with Implementation Group assignments. The document includes detailed guidance on why each safeguard matters, how it maps to common attack patterns from the CIS Community Attack Model, and which IG level applies. Directly supports the control framework comparison content in Section 3 of this module.

**NIST CSF 2.0 — Quick Start Guides**
URL: https://www.nist.gov/cyberframework/getting-started
Description: NIST's free collection of Quick Start Guides for CSF 2.0, including guides for small businesses, enterprise risk management integration, and supply chain risk management. These practical guides demonstrate how the six CSF functions are applied in real organizational contexts and include worked examples of CSF Current and Target Profiles — directly supporting the CSF Profiles and Tiers content in Section 4 of this module.

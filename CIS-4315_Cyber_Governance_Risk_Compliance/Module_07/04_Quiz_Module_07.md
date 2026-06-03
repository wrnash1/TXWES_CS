# Quiz: Module 07 — Security Architecture and Controls

## Course: CIS-4315 Cyber Governance, Risk, and Compliance

**Certification Alignment:** ISACA CISM — Domain 3: Information Security Program

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points (100 points total). Questions reflect CISM Domain 3 exam-style scenarios.

---

## Question 1

An attacker successfully bypasses a company's perimeter firewall using a phishing email. Despite this, they are detected and contained before reaching any sensitive data. Which security principle does this outcome best illustrate?

- A) Least privilege — the attacker did not have sufficient permissions to access sensitive data
- B) Defense-in-depth — multiple independent controls at different layers prevented a successful breach
- C) Separation of duties — different teams managed the perimeter and the internal network
- D) Security through obscurity — the internal network structure was unknown to the attacker

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Least privilege describes minimizing access rights. While it may have been a contributing factor, the scenario specifically illustrates how layered controls at multiple architecture levels stopped an attacker who already penetrated the perimeter — that is defense-in-depth.
- B — Correct. The attacker bypassed one layer (perimeter firewall) but was stopped by controls at deeper layers (detection and containment). This is the defining characteristic of defense-in-depth: failure of one control does not result in a successful breach.
- C — Incorrect. Separation of duties is a fraud prevention control ensuring no single individual can complete a sensitive transaction alone. Different teams managing different systems is an organizational design choice, not the principle illustrated here.
- D — Incorrect. Security through obscurity relies on hiding system details as a defense, which is widely considered an inadequate primary control. The scenario describes multiple active controls working in sequence, not information concealment.

---

## Question 2

A security architect needs to select controls that will identify attacks that have already bypassed preventive measures. Which control type should the architect prioritize?

- A) Preventive controls such as firewalls and multi-factor authentication
- B) Corrective controls such as backup restoration and patch deployment
- C) Detective controls such as SIEM, IDS, and audit log analysis
- D) Deterrent controls such as legal warning banners and visible security cameras

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. Preventive controls stop attacks before they succeed but by definition cannot identify attacks that have already bypassed them. The scenario explicitly requires detection capability after prevention has failed.
- B — Incorrect. Corrective controls restore normal operations after an incident. They respond to a known incident but do not provide the detection capability the scenario requires.
- C — Correct. Detective controls identify attacks in progress or after the fact. SIEM, IDS, and audit log analysis are the core detective tools that compensate for preventive control failures.
- D — Incorrect. Deterrent controls discourage attacks but do not detect them. A warning banner does not alert the security team that an attack is underway.

---

## Question 3

An organization must comply with U.S. federal information security requirements and needs a comprehensive catalog of controls to implement across all security domains. Which framework is most appropriate?

- A) CIS Controls v8, because it provides the 18 most critical security actions prioritized for impact
- B) NIST SP 800-53 Rev 5, because it is the mandatory comprehensive control catalog for federal systems
- C) ISO/IEC 27001, because it provides an externally certifiable management system standard
- D) NIST CSF 2.0, because it organizes security activities into six functions for executive communication

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. CIS Controls are a prioritized subset of security actions, valuable for organizations with limited resources. They are not a comprehensive catalog and are not the designated standard for federal compliance.
- B — Correct. NIST SP 800-53 is the mandatory security control catalog for U.S. federal information systems under FISMA. It provides over 1,000 controls across 20 families and is specifically designed for the federal compliance context described.
- C — Incorrect. ISO 27001 is an international standard for information security management systems and supports voluntary certification. It is not the designated framework for U.S. federal compliance requirements.
- D — Incorrect. NIST CSF is a voluntary framework for program structure and risk management communication. It references other frameworks (including 800-53) for control selection but is not itself a comprehensive control catalog.

---

## Question 4

A CISO uses the NIST Cybersecurity Framework to document what the organization's security program currently achieves, then creates a second document describing where it should be in three years. What are these two documents called?

- A) Current Tier and Target Tier
- B) Baseline Assessment and Gap Analysis
- C) Current Profile and Target Profile
- D) Current State Report and Security Roadmap

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. CSF Tiers describe the rigor and sophistication of risk management practices on a four-point scale. They are not used to document current and desired security outcomes in the way described.
- B — Incorrect. While gap analysis is a related concept, these are not the official CSF terms. The NIST CSF uses specific terminology: Profile for the expression of current or desired outcomes.
- C — Correct. A Current Profile documents the cybersecurity outcomes an organization is currently achieving. A Target Profile documents the outcomes it aims to achieve. This is the standard CSF usage described in the scenario.
- D — Incorrect. While these terms are used in practice, they are not the formal NIST CSF terminology. Using unofficial terms on the exam will lead to selecting this distractor over the correct CSF-specific answer.

---

## Question 5

A security manager reviews an organization's network architecture and finds that corporate workstations, servers hosting customer data, and industrial control systems all reside on the same flat network with no access restrictions between them. Which control is most urgently needed?

- A) Next-generation firewall at the internet perimeter to block external threats
- B) Endpoint detection and response deployed to all workstations and servers
- C) Network segmentation to establish security zones and restrict lateral movement
- D) Data loss prevention to monitor outbound transfers of customer data

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. A perimeter firewall controls traffic between the internal network and the internet but does nothing to restrict lateral movement within a flat internal network. An attacker already inside the network would face no internal barriers.
- B — Incorrect. EDR is valuable for endpoint detection but does not address the architectural problem. An attacker who compromises one endpoint in a flat network can freely reach industrial control systems — EDR detects but cannot substitute for architectural separation.
- C — Correct. A flat network with no segmentation between corporate IT and industrial control systems represents a critical architectural vulnerability. Network segmentation creates security zones that contain breaches and prevent lateral movement between high-risk and high-value systems.
- D — Incorrect. DLP protects against data exfiltration but does not address the lateral movement risk described. The most urgent need is containment of movement within the network, not monitoring of data leaving it.

---

## Question 6

An organization cannot apply a critical security patch to a legacy system because the vendor no longer supports the software. The system must remain operational for 18 more months until a replacement is deployed. Which control type best describes the additional monitoring and access restrictions implemented in the interim?

- A) Preventive control — the restrictions prevent the vulnerability from being exploited
- B) Corrective control — the monitoring restores the system if the vulnerability is exploited
- C) Compensating control — the measures substitute for the primary control that cannot be applied
- D) Deterrent control — the monitoring discourages attackers from targeting the system

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. Preventive controls stop attacks; the additional monitoring and restrictions reduce risk but do not prevent exploitation of the unpatched vulnerability. More importantly, the control type that specifically addresses substituting for an unimplementable primary control has a dedicated name.
- B — Incorrect. Corrective controls restore normal operations after an attack. Monitoring and access restrictions are not restorative in nature.
- C — Correct. A compensating control is explicitly defined as a control that substitutes for a primary control that cannot be implemented. The CISM exam and most compliance frameworks (including PCI DSS) recognize compensating controls as the appropriate response when primary controls are not feasible.
- D — Incorrect. Deterrent controls discourage attacks. While monitoring may have a mild deterrent effect, this is not the defining characteristic of the control type described, and it does not address the underlying vulnerability management problem.

---

## Question 7

Which NIST CSF 2.0 function was added in the 2024 revision and addresses organizational context, risk management strategy, roles, and oversight?

- A) Identify
- B) Protect
- C) Govern
- D) Manage

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. Identify is one of the original five CSF functions and covers asset management, risk assessment, and business environment understanding. It was present in CSF 1.1.
- B — Incorrect. Protect is one of the original five functions and covers preventive controls including identity management, data security, and awareness training.
- C — Correct. Govern is the new function added in CSF 2.0 (February 2024). It addresses organizational context, risk management strategy, roles and responsibilities, policies, and oversight — essentially the governance layer that enables all other functions to operate effectively.
- D — Incorrect. "Manage" is not a CSF function. This is a distractor designed to catch candidates who confuse the CSF with other frameworks that use management-oriented terminology.

---

## Question 8

A company discovers that an employee emailed a spreadsheet containing 10,000 customer Social Security numbers to a personal Gmail account. Which control, if it had been implemented, would MOST directly have prevented this specific incident?

- A) Network segmentation between corporate systems and the internet
- B) Multi-factor authentication on the corporate email system
- C) Data loss prevention configured to block outbound emails containing SSN patterns
- D) Endpoint detection and response on the employee's workstation

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. Network segmentation controls which systems can communicate with which other systems. It would not prevent an authorized user from emailing data from a permitted email client to an external address.
- B — Incorrect. MFA verifies user identity and prevents unauthorized access. This incident involved an authorized employee taking a deliberate action — MFA would not stop an authenticated user from exfiltrating data.
- C — Correct. Network DLP configured with SSN detection patterns would inspect outbound email content and block transmission of messages containing Social Security number patterns. This directly addresses the specific exfiltration vector described.
- D — Incorrect. EDR detects malicious software behavior and threat actor activity. It is not designed to detect or prevent authorized users from sending sensitive data through legitimate applications.

---

## Question 9

An organization wants to implement Zero Trust Architecture. Which of the following principles is MOST central to the Zero Trust model?

- A) All traffic originating from within the corporate network perimeter is trusted by default
- B) Users must verify identity once per session; subsequent requests within the session are trusted
- C) Every access request is verified explicitly regardless of network location or previous authentication
- D) Network segmentation replaces the need for identity verification on internal systems

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. This describes the traditional perimeter-based trust model that Zero Trust explicitly replaces. Trusting traffic based on network location is the exact assumption that Zero Trust rejects.
- B — Incorrect. Session-based trust after initial authentication is a legacy model. Zero Trust requires continuous verification and may re-challenge users based on risk signals even within an established session.
- C — Correct. "Never trust, always verify" is the core Zero Trust principle. Every access request — regardless of whether it comes from inside or outside the network — must be explicitly authenticated and authorized.
- D — Incorrect. Segmentation is a supporting control in Zero Trust but does not replace identity verification. Zero Trust combines both: segment the network AND verify identity at every access boundary.

---

## Question 10

A security manager is building a security program for a small nonprofit with limited budget and a two-person IT team. The manager needs to prioritize the highest-impact security controls given severe resource constraints. Which framework is best suited to guide this prioritization?

- A) NIST SP 800-53 Rev 5, because it provides the most comprehensive control coverage
- B) ISO/IEC 27001, because it supports external certification that builds stakeholder trust
- C) CIS Controls v8 Implementation Group 1, because it identifies essential cyber hygiene for resource-constrained organizations
- D) NIST CSF 2.0, because its six functions provide a complete program structure

**Correct Answer:** C

**Distractor Analysis:**

- A — Incorrect. NIST 800-53 with over 1,000 controls is designed for organizations with mature security programs and significant resources. Applying it to a two-person IT team at a small nonprofit would be overwhelming and counterproductive.
- B — Incorrect. ISO 27001 certification requires significant organizational investment in documentation, internal audits, and external assessment. It is not appropriate for a small organization prioritizing essential controls with minimal budget.
- C — Correct. CIS Controls v8 Implementation Group 1 was specifically designed for small organizations with limited resources and cybersecurity expertise. Its 56 safeguards represent the minimum essential cyber hygiene that every organization should implement regardless of size or budget.
- D — Incorrect. NIST CSF is excellent for program structure and communication but does not provide the specific prioritization guidance that resource-constrained organizations need. It references other frameworks for control selection rather than prescribing a priority order.

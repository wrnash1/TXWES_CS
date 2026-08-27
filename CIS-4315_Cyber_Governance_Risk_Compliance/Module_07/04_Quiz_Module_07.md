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

---

## Question 11

An organization implements network segmentation by placing its payment card processing systems in an isolated VLAN with strict firewall rules controlling all inbound and outbound traffic. Which security benefit does this architecture most directly provide?

- A) It eliminates the possibility of a SQL injection attack against the payment systems
- B) It limits an attacker's ability to move laterally from a compromised non-payment system to the payment systems
- C) It ensures that payment card data is encrypted during transmission
- D) It prevents insider threats by restricting physical access to payment servers

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Network segmentation does not prevent application-layer attacks like SQL injection, which exploit vulnerabilities in application code rather than network topology. SQL injection prevention requires input validation, parameterized queries, and web application firewalls at the application layer.
- B — Correct. Network segmentation is specifically designed to limit lateral movement — an attacker who compromises a workstation on a general business network cannot traverse directly to the payment card VLAN because the firewall rules block that path. Segmentation is a core containment strategy in defense-in-depth architectures and a PCI DSS requirement for cardholder data environments.
- C — Incorrect. Encryption in transit is provided by protocols like TLS, not by network segmentation. Segmentation controls which systems can communicate with each other; encryption controls whether that communication can be intercepted and read.
- D — Incorrect. Physical access controls (badge readers, locked server rooms) prevent unauthorized physical access to servers. Network segmentation is a logical network control; it has no effect on physical access to hardware.

---

## Question 12

Under the Zero Trust Architecture model, which of the following best describes the treatment of traffic from a device on the corporate internal network?

- A) Internal traffic is implicitly trusted because it has already passed the perimeter firewall
- B) Internal traffic is subject to the same continuous verification requirements as external traffic
- C) Internal traffic is trusted for read operations but requires explicit verification for write operations
- D) Internal traffic from managed devices is trusted; traffic from unmanaged devices is not

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. The foundational principle of Zero Trust is "never trust, always verify." Zero Trust explicitly rejects the concept of an implied trusted internal network. Every access request — whether originating inside or outside the network perimeter — must be authenticated, authorized, and continuously validated based on identity, device health, and context. The source network location is not a trust indicator.
- A — Incorrect. This describes the traditional perimeter-based security model that Zero Trust was designed to replace. The perimeter model assumes that anything inside the firewall is trustworthy — an assumption that fails when attackers gain internal access through phishing, insider threats, or compromised systems.
- C — Incorrect. Zero Trust does not make distinctions based on operation type (read vs. write). All access requests are subject to continuous verification regardless of the type of operation requested. Risk-based access policies may consider the sensitivity of data being accessed, but this is not a read/write distinction.
- D — Incorrect. While device health is one factor in Zero Trust access decisions, managed-device status alone does not grant implicit trust. A managed device may be compromised, misconfigured, or used by an unauthorized user. Zero Trust requires verification of identity, device posture, and context for every request.

---

## Question 13

A Data Loss Prevention (DLP) solution is deployed in network monitoring mode. A security analyst notices that large volumes of sensitive customer data are being transferred to a personal cloud storage account via HTTPS. The DLP system generated an alert but did not block the transfer. What does this outcome reveal about the DLP deployment?

- A) The DLP is functioning correctly — network monitoring mode generates alerts but does not block traffic
- B) The DLP solution is misconfigured because it should always block HTTPS traffic
- C) The DLP solution failed because it cannot inspect HTTPS traffic
- D) The DLP solution is inadequate for protecting against insider threats

**Correct Answer:** A

**Distractor Analysis:**

- A — Correct. DLP solutions are typically deployed in one of three modes: monitoring (alert only), active blocking (intercept and block), or a hybrid. Network monitoring mode generates alerts for policy violations but does not interrupt the data flow. The analyst's observation is consistent with a correctly functioning monitoring-mode deployment. To block transfers, the organization would need to reconfigure the DLP to active blocking mode or deploy an inline proxy that can inspect and terminate HTTPS sessions.
- B — Incorrect. Blocking all HTTPS traffic would be operationally catastrophic — HTTPS is the primary protocol for all secure web communications. DLP policies target specific data patterns, destinations, and users, not entire protocols. Blocking all HTTPS would break virtually all web-based business functions.
- C — Incorrect. Modern DLP solutions can inspect HTTPS traffic when deployed with SSL/TLS inspection capabilities (often via a transparent proxy). The fact that an alert was generated indicates the DLP did inspect the traffic content — it simply did not block it because it is in monitoring mode.
- D — Incorrect. The DLP performed its configured function correctly. The scenario reveals a deployment configuration decision (monitoring vs. blocking), not an inadequacy of DLP for insider threat scenarios. Whether monitoring mode is sufficient is a policy and risk decision, not a technology deficiency.

---

## Question 14

An organization is mapping its controls to the NIST Cybersecurity Framework 2.0. The security team has documented a process for reviewing firewall rules quarterly to remove stale access permissions. Under which CSF 2.0 function does this activity most appropriately belong?

- A) Identify
- B) Protect
- C) Detect
- D) Recover

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. The Protect function encompasses activities that implement safeguards to limit or contain the impact of cybersecurity events. Access control management — including periodic review and removal of unnecessary access permissions — is a protective activity. NIST CSF 2.0 maps access control management to the Protect function, specifically under the Identity Management, Authentication, and Access Control (PR.AA) category.
- A — Incorrect. The Identify function covers asset management, risk assessment, and understanding the organization's cybersecurity risk. Reviewing firewall rules to remove stale permissions is an access control maintenance activity (protective), not an asset identification or risk assessment activity.
- C — Incorrect. The Detect function encompasses activities that enable timely discovery of cybersecurity events. Firewall rule review is a preventive/protective maintenance activity, not an event detection activity. Detection would include monitoring firewall logs for anomalous traffic patterns.
- D — Incorrect. The Recover function covers activities to restore capabilities after a cybersecurity incident. Quarterly firewall rule review is a routine maintenance activity conducted before any incident occurs.

---

## Question 15

An organization is evaluating whether to implement a Privileged Access Management (PAM) solution. The primary driver is that three recent security incidents involved attackers using compromised administrator credentials to access critical systems. Which security principle does a PAM solution most directly address?

- A) Defense-in-depth, by adding a detection layer around privileged accounts
- B) Least privilege and access control, by managing and constraining what privileged accounts can do and when
- C) Non-repudiation, by creating audit logs of privileged account activity
- D) Separation of duties, by requiring two administrators to approve all privileged actions

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. PAM solutions are specifically designed to implement least privilege and access control principles for privileged accounts. They typically enforce just-in-time access (credentials are issued only when needed and expire automatically), vault and rotate credentials (preventing attackers from reusing stolen credentials), and enforce approval workflows for sensitive privileged operations. These capabilities directly address the scenario where attackers used compromised admin credentials — PAM would have limited the usability and lifespan of those credentials.
- A — Incorrect. While PAM solutions do include monitoring and alerting capabilities, their primary value is access control and credential management, not detection. The detection aspect is secondary to the access restriction function. Defense-in-depth describes the layered architecture strategy, not the specific function of PAM.
- C — Incorrect. Audit logging and non-repudiation are important secondary features of PAM solutions, but they are not the primary security value. The scenario describes attackers using valid credentials — audit logs would document what they did but would not prevent the access. The primary need is credential protection and access control, not logging.
- D — Incorrect. While some PAM solutions do include approval workflow features, separation of duties (requiring two people to complete a sensitive action) is not the defining characteristic of PAM. The core PAM functions are credential vaulting, rotation, just-in-time access, and session monitoring — which collectively address least privilege, not separation of duties.

---

## Question 16

A security architect is designing the network zone structure for a new hospital system. The environment includes medical devices connected to patient monitors, a clinical application server housing patient records, administrative workstations, and a guest Wi-Fi network. Which network segmentation design is MOST aligned with a defense-in-depth architecture?

- A) Place all clinical systems on a dedicated VLAN separate from the internet perimeter, with no further segmentation needed between clinical subsystems
- B) Create four separate zones — medical devices, clinical servers, administrative systems, and guest Wi-Fi — with strict inter-zone firewall policies controlling traffic between each zone
- C) Connect all internal systems to a trusted internal network and isolate only the guest Wi-Fi from the trusted zone
- D) Place all HIPAA-covered systems in a single flat zone and segment only internet-facing systems from the trusted network

**Correct Answer:** B

**Distractor Analysis:**

- A — Incorrect. Placing all clinical systems in one zone without internal segmentation leaves the medical devices directly reachable from clinical servers, and vice versa. A compromised clinical server could then directly reach life-critical medical devices. Internal segmentation between subsystems is essential in healthcare environments.
- B — Correct. Defense-in-depth network architecture requires that systems with different sensitivity levels, operational functions, and risk profiles be isolated into separate security zones. Four distinct zones with firewall policy control between each zone ensures that a compromise of any single zone (e.g., a ransomware infection on an administrative workstation) cannot directly reach medical devices or clinical servers without traversing controlled access points.
- C — Incorrect. Isolating only guest Wi-Fi while treating all internal systems as a flat trusted network is the traditional perimeter model. Medical devices, patient records, and employee workstations have vastly different sensitivity and attack surface profiles. Treating them as equally trusted creates significant lateral movement risk.
- D — Incorrect. Grouping all HIPAA-covered systems into a single flat zone and segmenting only internet-facing systems provides minimal containment benefit. A breach of any one HIPAA-covered system would give an attacker full access to all others in the flat zone. This design provides only perimeter defense, not internal containment.

---

## Question 17

An organization deploys a web application firewall (WAF) in front of its customer-facing e-commerce platform. During a security review, the team discovers that database queries from the application to the backend database server are not validated or parameterized. Which statement BEST describes the security posture gap this finding represents?

- A) The WAF is sufficient to address SQL injection risk because it inspects all inbound web traffic
- B) The WAF provides perimeter protection, but the lack of parameterized queries is an application-layer vulnerability that the WAF does not fully mitigate
- C) The database server must be moved inside the WAF protection boundary to resolve this issue
- D) The finding is low priority because the WAF's SQL injection rules are regularly updated by the vendor

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. A WAF provides a valuable external control layer that can block many common SQL injection patterns, but WAF rules can be bypassed through encoding variations, novel attack vectors, or WAF misconfigurations. Parameterized queries (prepared statements) are an input validation control at the application code layer — they prevent SQL injection by construction, regardless of what reaches the database. Defense-in-depth requires both controls: the WAF reduces the attack surface visible from the network; parameterized queries eliminate the vulnerability at the source.
- A — Incorrect. WAFs are not foolproof against SQL injection. Attackers routinely bypass WAF rules using encoding techniques, fragmented requests, or by exploiting WAF signature gaps. Relying solely on a WAF for SQL injection prevention is a single-point-of-failure defense that OWASP and security frameworks explicitly caution against.
- C — Incorrect. The database server's network location relative to the WAF is a network architecture concern. Moving the database inside the WAF zone does not address the underlying application vulnerability of unparameterized queries. Network position and application code quality are separate defense layers.
- D — Incorrect. WAF vendor updates address known signature-based attacks but cannot address all obfuscated or novel SQL injection techniques. Classifying an application-layer coding vulnerability as low priority because a network-layer control has current signatures misunderstands the defense-in-depth principle and creates unjustified risk acceptance.

---

## Question 18

A security team is conducting a control gap analysis against the NIST Cybersecurity Framework 2.0. They find that the organization has strong Identify and Protect capabilities but no defined processes in the Detect, Respond, or Recover functions. Which risk does this imbalance most directly create?

- A) The organization cannot achieve ISO 27001 certification without addressing all six CSF functions equally
- B) The organization has no ability to discover security events in progress or limit damage after a breach, meaning incidents may go undetected and uncontained indefinitely
- C) The organization's Identify function is unnecessary because detection and response are more important
- D) The imbalance means the organization's CSF Tier rating will be reduced to Tier 1 across all functions

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. The Detect function provides the capability to discover that a security event is occurring. The Respond function enables containment, eradication, and communication. The Recover function restores operations. Without these three functions, the organization may identify assets and implement preventive controls — but when those controls fail (which they eventually will), the organization has no mechanism to discover the breach, limit damage, or restore operations. This gap is operationally severe: breaches can persist for months without detection capability.
- A — Incorrect. ISO 27001 certification and the NIST CSF are independent frameworks. CSF function coverage is not a prerequisite for ISO 27001 certification. This distractor incorrectly creates a dependency between two separate frameworks.
- C — Incorrect. The Identify function is foundational — without knowing your assets, risk profile, and dependencies, you cannot make informed decisions about what to detect or protect. Suggesting that Identify is unnecessary because other functions exist inverts the CSF's intended sequence and misrepresents the framework.
- D — Incorrect. CSF Tiers describe the maturity and rigor of risk management practices. Tiers are assessed by function and can vary across functions — they are not averaged or reduced by gaps in other functions. This distractor misrepresents how CSF Tiers work.

---

## Question 19

An organization is implementing a data classification program. The security architect proposes four tiers: Public, Internal, Confidential, and Restricted. A business unit manager argues that creating four tiers will be "too confusing" and proposes reducing to two tiers: Public and Private. Which response from the security architect is most appropriate?

- A) Accept the two-tier proposal — simplicity improves adoption and two tiers are sufficient for most organizations
- B) Explain that four tiers are required by ISO 27001 and cannot be reduced without losing compliance
- C) Explain that four tiers allow proportionate controls to be applied based on data sensitivity, while a two-tier system would apply the same high-cost controls to all non-public data, including low-sensitivity internal documents
- D) Defer the decision to the CISO and proceed with no classification system until a decision is made

**Correct Answer:** C

**Distractor Analysis:**

- C — Correct. Data classification tiers exist to enable proportionate control application. If all non-public data is classified as "Private," the organization must either apply expensive high-sensitivity controls to low-risk internal data (costly and impractical) or apply weak controls to genuinely sensitive data (a risk acceptance problem). Four tiers allow the organization to apply encryption and strict access controls to Restricted data while using lighter-touch controls for Internal documents like meeting agendas. Proportionality is the core justification for multi-tier classification.
- A — Incorrect. While simplicity aids adoption, accepting two tiers without addressing the proportionality concern accepts a false choice. The goal is a classification system that is both usable and effective. Well-designed four-tier systems with clear examples and decision guides can achieve both goals; collapsing to two tiers solves the adoption problem by creating a risk management problem.
- B — Incorrect. ISO 27001 does not mandate a specific number of classification tiers. Annex A control A.5.12 requires information classification, but the number of categories is an organizational design decision. Citing a non-existent ISO requirement undermines the architect's credibility.
- D — Incorrect. Deferring without a plan creates an operational gap — data is being handled without defined controls in the interim. The security architect should make the business case for the appropriate number of tiers and resolve the disagreement through governance, not defer indefinitely.

---

## Question 20

A security engineer recommends deploying micro-segmentation within the organization's data center, where each workload communicates only with explicitly permitted peers using identity-based policies rather than IP-based firewall rules. Which architecture principle does this recommendation most directly implement?

- A) Defense-in-depth, by adding a detection layer inside the data center network
- B) Zero Trust, by enforcing continuous, identity-based authorization for every workload-to-workload communication
- C) Least functionality, by reducing the number of services running on each server
- D) Separation of duties, by ensuring no single administrator can configure both the workloads and the network policies

**Correct Answer:** B

**Distractor Analysis:**

- B — Correct. Micro-segmentation with identity-based policies is a direct implementation of the Zero Trust principle of "never trust, always verify." Rather than assuming that workloads within the same data center VLAN can freely communicate, micro-segmentation enforces that every communication request — even east-west traffic between servers in the same data center — must be explicitly authorized based on workload identity. This eliminates the implicit trust of traditional network zones and is a foundational Zero Trust data center architecture pattern.
- A — Incorrect. Defense-in-depth is the broader principle of layered controls. While micro-segmentation contributes to a defense-in-depth architecture, the specific mechanism described — identity-based authorization for workload communication — is more precisely characterized as Zero Trust implementation. The engineer is not adding a detection layer; they are adding an access control enforcement point.
- C — Incorrect. Least functionality (or least functionality/minimal footprint) refers to disabling unused services, ports, and protocols on individual systems. It is a hardening principle applied to system configuration, not a network communication authorization principle.
- D — Incorrect. Separation of duties is a fraud prevention and error reduction control that prevents a single individual from completing a sensitive process end-to-end. Micro-segmentation is a network access control architecture, not an administrative role separation mechanism.

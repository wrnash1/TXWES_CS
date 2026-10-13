# Quiz: Module 13 — Compliance and Security Controls Validation

## Course: CIS-4332 Cyber Security Analysis

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA CySA+ (CS0-003)

---

## Instructions

Select the best answer for each question. Distractor analysis is provided after each question to support exam preparation.

---

## Question 1

A security analyst is asked to map the organization's log management and SIEM alerting program to the NIST Cybersecurity Framework v2.0. Which CSF function most directly encompasses continuous monitoring and anomaly detection activities?

- A) Identify
- B) Protect
- C) Detect
- D) Respond

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: The Identify function covers asset management, risk assessment, and governance — establishing the foundational understanding of the organization's environment. Monitoring and alerting are not Identify activities. Why B is incorrect: The Protect function covers access control, awareness training, data security, and protective technologies. Protective controls are implemented under Protect; monitoring those controls' effectiveness is under Detect. Why C is correct: The Detect function specifically encompasses anomalies and events detection, security continuous monitoring, and detection processes — exactly what a SIEM and log management program delivers. This is the function that represents analyst SOC work most directly. Why D is incorrect: The Respond function covers what happens after an event is detected — response planning, communications, analysis, and mitigation. Detection must precede response; they are separate functions.

---

## Question 2

An organization implements security awareness training for all employees, delivered annually through an online platform. Which control classification correctly describes this control?

- A) Technical and preventive
- B) Administrative and detective
- C) Administrative and preventive
- D) Physical and deterrent

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Security awareness training is not implemented through technology in hardware or software — it is a policy and process activity, making it administrative, not technical. Why B is incorrect: Training is administrative (correct), but it is not a detective control. It does not identify when security events occur; it reduces the likelihood of events by improving employee behavior. Why C is correct: Security awareness training is administrative — implemented through a program and policy, not technology or physical measures. It is preventive — its purpose is to reduce the likelihood that employees will fall for phishing, mishandle data, or make security mistakes. This is the standard two-dimensional classification. Why D is incorrect: Physical controls operate in the physical environment (locks, badges, cameras). Training is not a physical control, and while it has some deterrent effect, its primary function is prevention.

---

## Question 3

A security analyst performing a gap analysis against CIS Controls v8 finds that the organization has a hardware asset inventory but it was last updated 18 months ago and is estimated to be only 60% complete. How should this finding be classified in the gap report?

- A) Implemented — a hardware inventory exists and satisfies CIS Safeguard 1.1
- B) Not Implemented — the inventory does not exist
- C) Partial — an inventory process exists but is not current, complete, or maintained to the CIS standard
- D) Compensating Control — the 60% coverage is sufficient given the organization's small size

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: CIS Safeguard 1.1 requires a "detailed" and "maintained" inventory. An inventory that is 18 months stale and 60% complete does not meet the standard. Classifying it as Implemented would misrepresent the organization's compliance posture. Why B is incorrect: The inventory does exist — it simply is not maintained to the required standard. Not Implemented would be reserved for organizations with no inventory process at all. Why C is correct: Partial correctly captures the situation: the control is partially in place (an inventory process exists with some documented assets) but does not meet the requirement for completeness and currency. This classification drives the gap description that explains what improvement is needed. Why D is incorrect: Organization size is not a compensating control for an incomplete asset inventory. Small organizations have the same risk from unmanaged assets as large ones — unmanaged assets cannot be patched, secured, or monitored.

---

## Question 4

Which of the following types of audit evidence is strongest for demonstrating that multifactor authentication (MFA) is actively being enforced on all externally exposed VPN connections?

- A) A written policy stating that MFA is required for all VPN connections
- B) A screenshot of the MFA configuration settings in the identity provider taken on the day of the audit
- C) An extract from authentication logs showing MFA challenges and completions for VPN connections across the full audit period
- D) A vendor support document showing that the identity provider product supports MFA enforcement

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: A policy stating that MFA is required proves the requirement exists but does not demonstrate that the control is actually implemented and operating. Policy is the weakest form of audit evidence for control effectiveness. Why B is incorrect: A configuration screenshot proves the setting is configured at a point in time but does not prove the control has been consistently operating throughout the audit period. An auditor may question whether it was configured just before the audit. Why C is correct: Authentication logs showing actual MFA challenges and completions across the full audit period provide operational evidence that the control has been functioning consistently over time. This is the gold standard for compliance evidence — it shows the control operating, not just configured. Why D is incorrect: Vendor documentation proves the product can support MFA enforcement, not that the customer has configured and is actively using it. This is product capability evidence, not control operation evidence.

---

## Question 5

An organization subject to HIPAA discovers that an unencrypted backup drive containing ePHI was stolen from an employee's car. Under HIPAA, which description of the breach notification obligation is most accurate?

- A) HIPAA does not require breach notification for physical media theft — only electronic intrusions trigger notification requirements
- B) The organization must notify affected individuals without unreasonable delay and no later than 60 days after discovery; HHS must also be notified
- C) Notification is only required if the stolen data is confirmed to have been accessed by an unauthorized person, which cannot be proven for a stolen drive
- D) The organization must notify the FBI within 24 hours because HIPAA is a federal criminal statute

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: HIPAA's breach notification rule applies to all unauthorized acquisition, access, use, or disclosure of unsecured ePHI — regardless of whether the incident involves physical media or electronic intrusion. Why B is correct: The HIPAA Breach Notification Rule (45 CFR Part 164, Subpart D) requires covered entities to notify affected individuals without unreasonable delay and within 60 calendar days of discovering a breach. HHS must also be notified. For breaches affecting 500 or more individuals in a state, media notification is also required. An unencrypted drive containing ePHI is "unsecured ePHI" and triggers these requirements. Why C is incorrect: HIPAA uses a presumption standard — if unsecured ePHI is acquired by an unauthorized person, it is presumed to be a breach unless the covered entity can demonstrate a low probability that the PHI has been compromised. The burden is on the organization to show it is NOT a breach, not on regulators to prove access occurred. Why D is incorrect: HIPAA is primarily a civil regulatory statute enforced by HHS Office for Civil Rights, not the FBI. Criminal charges are possible under HIPAA for willful violations, but the FBI notification timeline described here is fictional.

---

## Question 6

A security analyst is testing whether the organization's email gateway correctly blocks phishing emails containing malicious attachments. The analyst sends a test phishing email with an inert malicious-looking attachment to a test inbox and verifies it is quarantined. Which control testing method does this represent?

- A) Examination
- B) Interview
- C) Testing
- D) Observation

**Correct Answer:** C

**Distractor Analysis:** Why A is incorrect: Examination involves reviewing documentation, configurations, and records. The analyst is not reviewing the email gateway configuration — they are actively exercising it by sending a test message. Why B is incorrect: Interview involves questioning personnel to verify that procedures are followed. No personnel are being questioned in this scenario. Why C is correct: Testing involves actively exercising a control and observing whether it functions as intended. Sending a test phishing email and verifying the quarantine outcome is direct operational testing of the email filtering control. This is the most rigorous method — it confirms the control works, not just that it is configured. Why D is incorrect: Observation is not a standard NIST control assessment method. The three NIST methods are Examine, Interview, and Test. "Observation" is sometimes used colloquially but is not a distinct method in the framework.

---

## Question 7

Which NIST Cybersecurity Framework function includes the activities of recovery planning, communications during recovery, and improvements based on lessons learned from past incidents?

- A) Detect
- B) Respond
- C) Protect
- D) Recover

**Correct Answer:** D

**Distractor Analysis:** Why A is incorrect: Detect covers anomaly and event identification and continuous monitoring. Recovery activities occur after an incident has already been detected and responded to. Why B is incorrect: Respond covers response planning, communications during the active incident, analysis of the incident, and mitigation actions. Respond addresses the active phase; Recover addresses restoration and learning. Why C is incorrect: Protect covers controls that prevent incidents — access controls, training, data security. Recovery planning is not a preventive activity. Why D is correct: The Recover function encompasses exactly these activities: recovery planning (developing and implementing plans to restore capabilities), improvements (incorporating lessons learned), and communications (coordinating restoration activities with stakeholders). This function closes the loop on the incident lifecycle.

---

## Question 8

An organization's security team deploys a Data Loss Prevention (DLP) system that monitors outbound email and blocks messages containing credit card numbers. A few months later, an analyst discovers that employees have been using a personal cloud storage service to share files containing cardholder data, bypassing the email DLP entirely. What type of security gap does this represent?

- A) A false positive problem — the DLP is blocking too many legitimate emails
- B) A control coverage gap — the DLP control only covers one data exfiltration channel, leaving others unmonitored
- C) A compensating control failure — the DLP was intended to compensate for weak access controls
- D) A detective control failure — the DLP should have detected the cloud storage uploads

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: A false positive problem means the control is triggering on legitimate activity that should be allowed. The scenario describes the opposite — malicious data egress is not being blocked at all. Why B is correct: This is a classic control coverage gap. The DLP is functioning correctly for email but the control scope does not cover all exfiltration channels. Employees found an uncontrolled path (personal cloud storage) and used it. A comprehensive DLP program must cover all data egress points — email, web uploads, USB, printing, and cloud sync clients — or the control has coverage gaps that attackers and negligent insiders will exploit. Why C is incorrect: A compensating control is a control that replaces a primary control that cannot be implemented. There is no indication the DLP was intended to compensate for another failed control. Why D is incorrect: The DLP is preventive (blocking email transmission), not detective. A detective control would log or alert on the cloud storage activity. The gap here is coverage (the wrong channel), not a failure of the detection function.

---

## Question 9

A security analyst discovers that a critical Windows server in the organization has not received operating system patches in nine months because the patch management tool excludes systems with the "production-critical" tag. The server runs a legacy application that cannot tolerate maintenance windows. Which description best characterizes this situation from a controls validation perspective?

- A) This is an acceptable residual risk because the application requires continuous availability
- B) This is a control scope exception that should be documented, risk-rated, and formally accepted by an appropriate risk owner, with compensating controls implemented where possible
- C) This is evidence that the patch management tool is misconfigured and should be fixed immediately by removing the exclusion
- D) This is not a security issue because legacy applications are not targeted by modern threat actors

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Declaring residual risk "acceptable" without documentation, formal risk acceptance by an authorized decision-maker, and compensating controls is not a legitimate risk management approach. It is an undocumented exception that exposes the organization without accountability. Why B is correct: Security programs must balance security requirements against business requirements. When a legitimate business need prevents full control implementation, the correct approach is to document the exception formally, have it risk-accepted by a person with appropriate authority (typically a system owner or risk officer), rate the residual risk, implement compensating controls where feasible (network segmentation, enhanced monitoring, application-layer controls), and review the exception on a defined schedule. This is how mature organizations handle unavoidable control exceptions. Why C is incorrect: Removing the exclusion and patching a legacy application that cannot tolerate maintenance windows could cause system failures that disrupt business operations more severely than the unpatched vulnerability. The correct action is not to force patching but to manage the exception properly. Why D is incorrect: Legacy systems running unpatched, well-known vulnerabilities are among the most targeted systems in enterprise networks. Nation-state actors and ransomware operators specifically enumerate unpatched legacy systems. This premise is false.

---

## Question 10

An analyst is preparing a security compliance dashboard for a board-level briefing. Which metric most accurately represents the organization's current vulnerability management posture?

- A) The total number of vulnerability scan findings from the most recent scan, regardless of age or remediation status
- B) The percentage of critical and high vulnerabilities that have exceeded the organization's defined SLA for remediation, broken down by business unit
- C) The names of all vulnerabilities discovered in the past year, sorted alphabetically
- D) The date of the most recent penetration test and its overall risk rating

**Correct Answer:** B

**Distractor Analysis:** Why A is incorrect: Total scan findings without context about age or remediation status is a raw count metric with no actionable meaning. A finding that was remediated yesterday has the same weight as one that has been open for six months. This metric does not measure program performance. Why B is correct: SLA breach rate for critical and high vulnerabilities is the most meaningful board-level metric for vulnerability management. It measures whether the organization is meeting its own defined risk tolerance for exposure time on the highest-risk vulnerabilities. Breaking it down by business unit enables accountability. This metric directly answers the board's question: "Are we managing our most critical vulnerabilities within acceptable timeframes?" Why C is incorrect: An alphabetical list of vulnerability names has no analytical value for a board audience. It provides no severity context, remediation status, or trend information. Why D is incorrect: The date and overall risk rating of the most recent penetration test is a useful program activity metric, but it measures a point-in-time assessment from months or years ago, not the current operational vulnerability posture. It says nothing about the day-to-day vulnerability management program.

---

## Question 11 (5 points)

The NIST Cybersecurity Framework (CSF) Identify function includes the Asset Management category. Which control outcome is most directly aligned with this category?

- A) Deploying multi-factor authentication on all privileged accounts
- B) Maintaining a comprehensive inventory of all hardware, software, and data assets, with data classifications assigned
- C) Encrypting all data at rest on storage systems
- D) Implementing network segmentation between IT and OT environments

Correct Answer: B

Distractor Analysis:

- A is incorrect. MFA deployment is a Protect function activity — it implements access control to reduce risk of unauthorized access. It presupposes knowing what to protect, which is the Identify function's output.
- B is correct. NIST CSF Identify > Asset Management (ID.AM) specifically requires organizations to identify and manage all physical devices, software, and data assets in the context of organizational objectives. Maintaining a comprehensive inventory with data classifications is the direct embodiment of this control outcome.
- C is incorrect. Data at rest encryption is a Protect function activity (PR.DS — Data Security). Protection controls are applied after assets are identified.
- D is incorrect. Network segmentation between IT and OT is a Protect function activity (PR.AC — Identity Management, Access Control, and Authentication) and potentially a Risk Assessment activity — not an asset identification outcome.

---

## Question 12 (5 points)

An organization undergoes a SOC 2 Type II audit. The auditor examines controls over a 12-month observation period and reviews evidence including automated system logs, access reviews, and change management tickets. How does this differ from a SOC 2 Type I audit?

- A) Type II audits are performed by internal auditors; Type I audits are performed by external auditors
- B) Type I audits assess whether controls are suitably designed at a point in time; Type II audits assess whether controls operated effectively over an extended observation period
- C) Type I provides a higher assurance level than Type II because it uses more rigorous testing procedures
- D) Type II audits only apply to cloud service providers; Type I applies to all organization types

Correct Answer: B

Distractor Analysis:

- A is incorrect. Both SOC 2 Type I and Type II are performed by external certified public accounting firms. Neither is an internal audit type.
- B is correct. SOC 2 Type I reports on whether controls are suitably designed as of a specific date — a point-in-time snapshot. SOC 2 Type II reports on whether the suitably designed controls actually operated effectively over a defined observation period (typically 6–12 months). Type II provides significantly higher assurance because it demonstrates sustained control operation, not just design intent.
- C is incorrect. Type II provides higher assurance than Type I because it covers operational effectiveness over time, not just design at a single moment. The assurance hierarchy runs Type I < Type II.
- D is incorrect. Both SOC 2 types apply to any service organization that handles user data — including cloud providers, SaaS vendors, and other third-party service organizations. The distinction is not based on organization type.

---

## Question 13 (5 points)

CIS Control 4 (Secure Configuration of Enterprise Assets and Software) requires organizations to establish and maintain secure baseline configurations. Which analyst action most directly validates that this control is operating effectively?

- A) Running a vulnerability scan to identify missing OS patches
- B) Using a compliance scanning tool (such as CIS-CAT or SCCM Compliance Baseline) to compare running system configurations against the approved CIS Benchmark baseline and reporting deviation percentages
- C) Reviewing firewall rule changes in the change management ticketing system
- D) Checking whether all users have completed annual security awareness training

Correct Answer: B

Distractor Analysis:

- A is incorrect. Vulnerability scanning identifies missing patches (relevant to CIS Control 7 — Continuous Vulnerability Management) not configuration drift from a defined secure baseline. Configuration and patch management are related but distinct controls.
- B is correct. CIS Control 4 requires maintaining and enforcing secure configurations against a documented baseline. Validating this control requires comparing current running configurations against the approved baseline using automated compliance scanning tools. The deviation percentage directly measures control effectiveness — a high deviation means the control is not operating as designed.
- C is incorrect. Firewall rule change review validates change management processes and potentially network security policy controls, not the secure baseline configuration control for endpoints and servers.
- D is incorrect. Security awareness training is an administrative control related to CIS Control 14 (Security Awareness and Skills Training), not CIS Control 4's technical configuration requirements.

---

## Question 14 (5 points)

An organization's gap analysis identifies that MFA is not enforced on its VPN gateway for non-privileged users. The organization's IT security policy requires MFA for all remote access. How should this gap be classified and what is the correct remediation path?

- A) Technical gap — compensating control only (cannot be fully remediated without replacing the VPN hardware)
- B) Policy compliance gap — the control is required by policy but not implemented; the gap should be risk-rated, assigned to a responsible owner, given a remediation target date, and tracked until MFA is enabled
- C) Acceptable risk — non-privileged users do not need MFA because they have limited access permissions
- D) Administrative gap — the policy should be updated to remove the MFA requirement for non-privileged users to eliminate the gap

Correct Answer: B

Distractor Analysis:

- A is incorrect. Modern VPN solutions uniformly support MFA through RADIUS, SAML, or built-in integrations. Hardware replacement is not required and is not the correct classification.
- B is correct. A policy compliance gap exists when a defined security requirement is not implemented. The correct response is to: (1) document the gap with specifics, (2) assign risk severity, (3) identify a responsible owner, (4) set a target completion date, and (5) track to closure. This is the standard gap analysis remediation workflow.
- C is incorrect. Non-privileged users represent the majority of accounts and are the primary target of credential phishing attacks. Their lower permissions do not eliminate the authentication security requirement — compromised non-privileged accounts are frequently used for lateral movement and privilege escalation.
- D is incorrect. Weakening a policy to eliminate a gap rather than remediating the underlying control deficiency is backwards security governance. Policy controls exist to protect the organization; they should not be relaxed to make compliance easier.

---

## Question 15 (5 points)

Which of the following best describes the difference between a preventive control and a detective control?

- A) Preventive controls are technical; detective controls are administrative
- B) Preventive controls attempt to stop an adverse event from occurring; detective controls identify that an adverse event has occurred or is occurring
- C) Preventive controls are more expensive than detective controls and should only be implemented for Critical assets
- D) Preventive controls protect data at rest; detective controls protect data in transit

Correct Answer: B

Distractor Analysis:

- A is incorrect. Both preventive and detective controls can be technical, administrative, or physical. Firewalls (technical preventive), security awareness training (administrative preventive), security cameras (physical detective), and SIEM alerts (technical detective) demonstrate that the control type and function are independent dimensions.
- B is correct. The preventive/detective/corrective taxonomy describes control function. Preventive controls stop security events from happening (firewalls, MFA, encryption, access controls). Detective controls identify that a security event has occurred or is in progress (SIEM alerts, IDS, audit logs, anomaly detection). These are complementary — preventive controls reduce frequency; detective controls enable response when prevention fails.
- C is incorrect. Control selection should be based on risk analysis, not cost tier alone. Both preventive and detective controls span a wide cost range from free configuration settings to expensive hardware platforms.
- D is incorrect. Data at rest and data in transit are data states that encryption controls protect. They have no direct relationship to the preventive/detective control function distinction.

---

## Question 16 (5 points)

An analyst is conducting a continuous monitoring review and finds that an administrative account that was flagged for deprovisioning 45 days ago is still active and was used to log on yesterday. Which compliance framework requirement does this most likely violate?

- A) NIST CSF Protect > Data Security (PR.DS) — encryption requirements
- B) CIS Control 5 — Account Management, specifically the requirement to disable accounts of departing users promptly
- C) PCI DSS Requirement 6 — Develop and maintain secure systems and applications
- D) HIPAA Security Rule Physical Safeguards — facility access controls

Correct Answer: B

Distractor Analysis:

- A is incorrect. PR.DS addresses data encryption and protection at rest and in transit. An undeprovisioned account is an access control issue, not a data encryption issue.
- B is correct. CIS Control 5 (Account Management) includes the requirement to disable or remove accounts when personnel leave or change roles. An account that should have been disabled 45 days ago but remains active and in use directly violates this control. The account represents an unauthorized access risk and may be a compliance finding in any audit that reviews CIS Control 5 implementation.
- C is incorrect. PCI DSS Requirement 6 addresses software security and patch management. Account lifecycle management is covered by PCI DSS Requirement 8 (Identify Users and Authenticate Access to System Components).
- D is incorrect. HIPAA Physical Safeguards cover physical facility access controls — not logical access account management. Logical access management falls under HIPAA Technical Safeguards.

---

## Question 17 (5 points)

During a compliance audit, an auditor asks the security team to provide evidence that access reviews are performed quarterly for privileged accounts. Which evidence package most completely satisfies this audit request?

- A) A policy document stating that quarterly access reviews are required
- B) Completed access review reports with review dates, reviewer names, action items, and sign-off for the past four quarters, along with access provisioning tickets documenting any changes made as a result
- C) A screenshot showing that all privileged accounts currently have appropriate access
- D) The most recent annual penetration test report demonstrating no privilege escalation findings

Correct Answer: B

Distractor Analysis:

- A is incorrect. A policy document proves a requirement exists but provides zero evidence of implementation. Auditors require evidence of control operation, not just documented intent.
- B is correct. This evidence package demonstrates the control is operating as designed: the completed review reports prove reviews occurred, the dates confirm quarterly frequency, reviewer names establish accountability, and the provisioning tickets prove that identified issues were remediated — completing the evidence chain for a fully operating control.
- C is incorrect. A current screenshot shows present state but does not demonstrate that reviews occurred historically. An auditor examining four quarters of reviews cannot rely on a single current-state snapshot.
- D is incorrect. A penetration test report evaluates whether privilege escalation is achievable through technical means. It does not demonstrate that access review processes were executed on schedule. These are different controls.

---

## Question 18 (5 points)

An organization subject to HIPAA undergoes a risk analysis as required by the HIPAA Security Rule. The risk analysis identifies that electronic protected health information (ePHI) is transmitted via unencrypted email between clinical staff and external consultants. Which HIPAA requirement applies most directly?

- A) HIPAA Privacy Rule — Minimum Necessary Standard
- B) HIPAA Security Rule — Technical Safeguards, specifically the requirement to implement technical security measures to guard against unauthorized access to ePHI transmitted over an electronic communications network
- C) HIPAA Breach Notification Rule — requires notification within 60 days of discovering unsecured ePHI
- D) HIPAA Enforcement Rule — specifies civil monetary penalties for non-compliance

Correct Answer: B

Distractor Analysis:

- A is incorrect. The Minimum Necessary Standard (Privacy Rule) addresses limiting disclosure of PHI to what is necessary for a specific purpose. It does not govern the technical security of transmission mechanisms.
- B is correct. The HIPAA Security Rule Technical Safeguards (45 CFR § 164.312(e)) require covered entities to implement technical security measures to guard against unauthorized access to ePHI transmitted over electronic communications networks. Unencrypted email transmission of ePHI directly violates this standard.
- C is incorrect. The Breach Notification Rule applies after a breach of unsecured ePHI has been discovered. The scenario describes an identified risk, not a confirmed breach. The notification obligation would arise if a breach occurred; the immediate applicable requirement is the Security Rule's encryption standard.
- D is incorrect. The Enforcement Rule defines penalties for violations of the Privacy, Security, and Breach Notification Rules — it is the consequence structure, not the technical requirement that applies.

---

## Question 19 (5 points)

A security analyst performs a controls assessment and finds that network segmentation between the payment card environment (CDE) and general corporate network is implemented via a single VLAN tag with no firewall between the segments. PCI DSS Requirement 1 mandates network security controls protecting the CDE boundary. How should this finding be classified?

- A) Compensating control — VLAN segmentation satisfies the spirit of the requirement even without a firewall
- B) Control deficiency / compliance gap — VLAN tagging alone is not recognized by PCI DSS as sufficient network segmentation; a properly configured firewall or equivalent network security control is required at the CDE boundary
- C) Acceptable risk — VLAN segmentation eliminates all unauthorized CDE access vectors
- D) Not applicable — PCI DSS only requires physical network separation, not logical segmentation

Correct Answer: B

Distractor Analysis:

- A is incorrect. PCI DSS compensating controls have specific criteria — they must be documented, submitted to the Qualified Security Assessor, and approved. VLAN tagging alone does not meet the compensating control criteria because it is not equivalent to a firewall's capability to inspect and control traffic.
- B is correct. PCI DSS Requirement 1 requires network security controls including firewalls at the CDE boundary that enforce traffic rules. VLAN tagging performs layer-2 segmentation but does not inspect or filter traffic at the network layer. PCI DSS specifically addresses this scenario and does not accept VLANs without proper firewalling as compliant network segmentation.
- C is incorrect. VLAN segmentation can be bypassed through VLAN hopping attacks, misconfigured trunk ports, or by any device that has access to the trunk link. It does not eliminate unauthorized access vectors.
- D is incorrect. PCI DSS accepts logical segmentation in addition to physical separation, but logical segmentation must be properly implemented with network security controls (firewalls). The requirement specifies controls, not specifically physical cabling.

---

## Question 20 (5 points)

A security controls assessment uses the NIST SP 800-53 framework to evaluate an organization's controls. The assessment finds that a required control from a HIGH baseline is implemented but only partially effective — the technical control is deployed but the associated procedures and training are missing. How should this control be rated?

- A) Fully Implemented — the technical control is in place
- B) Planned — the control is not yet implemented
- C) Partially Implemented — the technical implementation exists but the procedural and training components required for the control to be fully effective are absent
- D) Not Applicable — controls with missing procedures are excluded from NIST assessments

Correct Answer: C

Distractor Analysis:

- A is incorrect. "Fully Implemented" requires all components of the control — technical, administrative (procedures), and training — to be in place and operating effectively. A control missing its procedural and training components is not fully implemented even if the technical mechanism is deployed.
- B is incorrect. "Planned" means the control does not yet exist but is scheduled for implementation. The technical component exists, so "Planned" is not accurate.
- C is correct. NIST SP 800-53A assessment methodology uses implementation status ratings including Fully Implemented, Partially Implemented, Planned, and Alternative Implementation. A control with the technical component in place but missing required procedures and training is Partially Implemented — the control provides some protection but is not providing the full intended protection.
- D is incorrect. Controls with incomplete implementation are not excluded from NIST assessments — they are assessed as Partially Implemented and generate findings that drive remediation actions to achieve full implementation.

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

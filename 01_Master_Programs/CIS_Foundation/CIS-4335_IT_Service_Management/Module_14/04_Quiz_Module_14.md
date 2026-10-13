# Quiz: Module 14 — Risk and Compliance in ITSM

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

### Question 1

ITIL 4 defines risk as a possible event that could cause harm or loss, or affect the ability to achieve objectives. Which two dimensions are used to characterize a risk and determine its relative priority?

- A) Cost and duration — how expensive the risk event would be and how long the impact would last.
- B) Likelihood and impact — how probable the risk event is and how severe the consequences would be.
- C) Owner and category — who is responsible for the risk and which domain it falls under.
- D) Visibility and age — how long the risk has been known and whether leadership has been informed.

**Correct Answer:** B) Risk is characterized by likelihood (probability of occurrence) and impact (severity of consequences).

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines the two fundamental dimensions of risk as likelihood and impact. Risk exposure is typically expressed as the product of these two dimensions — a high-likelihood, low-impact risk may have the same score as a low-likelihood, high-impact risk, but the nature of management may differ significantly. Understanding both dimensions is essential for prioritizing risk responses.
- *Why A is incorrect:* Cost and duration are consequences of a risk event, not defining characteristics used to assess and prioritize risks. They may inform impact scoring, but they are not the two fundamental dimensions.
- *Why C is incorrect:* Owner and category are important risk register attributes for governance and organization, but they do not characterize the severity or urgency of the risk itself.
- *Why D is incorrect:* Visibility and age are not ITIL 4 risk characterization dimensions. A risk that has been known for a long time is not inherently lower priority than a newly identified risk.

---

### Question 2

An organization identifies a risk that a key cloud provider could experience a multi-hour outage, affecting a customer-facing payment service. The organization decides to sign a contractual agreement with a cyber-insurance provider to cover financial losses in the event of an outage. Which risk response strategy does this represent?

- A) Avoid — eliminating the activity that creates the risk.
- B) Mitigate — implementing controls to reduce the likelihood or impact of the risk.
- C) Transfer — shifting the financial consequences of the risk to another party.
- D) Accept — acknowledging the risk without taking any action.

**Correct Answer:** C) Transfer — the organization is shifting the financial consequences to the insurance provider.

**Distractor Analysis:**

- *Why C is correct:* Risk transfer moves the financial impact of a risk event to another party — typically through insurance, contracts, or indemnification clauses. Purchasing cyber-insurance for cloud outage financial losses is a textbook example of risk transfer. Note that transfer does not eliminate the operational impact — the outage would still occur — but the financial consequences are shifted.
- *Why A is incorrect:* Avoidance would require the organization to stop using the cloud provider entirely, eliminating the risk by eliminating the activity. Simply purchasing insurance while continuing to use the provider is not avoidance.
- *Why B is incorrect:* Mitigation would involve implementing controls that reduce the likelihood of outage (redundant providers, geographic distribution) or reduce the impact (failover systems, offline capabilities). Insurance does not change the likelihood or operational impact — it only covers financial losses.
- *Why D is incorrect:* Acceptance involves acknowledging the risk and taking no action. Purchasing insurance is an action taken in response to the risk — that is transfer, not acceptance.

---

### Question 3

An IT organization is preparing for ISO 27001 certification. The compliance team has completed its risk assessment and selected controls from Annex A to address identified risks. They have also identified three Annex A controls that do not apply to their organization. What document must the organization produce to record which controls are selected, implemented, and excluded?

- A) Risk register — the risk register documents all selected controls and their implementation status.
- B) Statement of Applicability — this document lists all Annex A controls and indicates which are selected, which are implemented, and which are excluded with justification.
- C) Gap analysis report — the gap analysis is the authoritative record of control selection for ISO 27001.
- D) Audit evidence package — all control decisions must be recorded in the audit evidence package submitted to the certification body.

**Correct Answer:** B) The Statement of Applicability (SoA) is the required ISO 27001 document that records control selection, implementation status, and exclusion justifications.

**Distractor Analysis:**

- *Why B is correct:* ISO 27001 explicitly requires a Statement of Applicability as a mandatory output of the risk treatment process. The SoA lists every Annex A control and states whether it is applicable (and if so, whether it is implemented) or excluded (and if so, why). It is a required document that certification auditors review to verify that the organization has made conscious, documented decisions about its control landscape.
- *Why A is incorrect:* The risk register tracks identified risks, their assessments, and responses — it is not the document that records Annex A control selection decisions. The risk register and the SoA are complementary but distinct documents.
- *Why C is incorrect:* The gap analysis identifies where controls are missing or inadequate — it is an input to the implementation roadmap. It is not the formal ISO 27001 document that records control selection decisions.
- *Why D is incorrect:* An audit evidence package is assembled to support a specific audit engagement. It is not the ongoing management document that records control applicability decisions. The SoA exists independently of audit cycles.

---

### Question 4

A company's SOC 2 Type I report from last year showed that all required controls were suitably designed. A new enterprise customer is requesting a SOC 2 Type II report before signing a contract. Why does the customer specifically require Type II rather than accepting the existing Type I report?

- A) SOC 2 Type II covers more Trust Services Criteria than Type I — it evaluates all five criteria, while Type I only evaluates Security.
- B) SOC 2 Type II evaluates whether controls operated effectively over a period of time, demonstrating sustained performance rather than just adequate design at a single point.
- C) SOC 2 Type I is issued by the company itself; SOC 2 Type II is issued by an independent auditor, making it more credible.
- D) SOC 2 Type II is required by law for all companies handling personal data; Type I has no legal standing.

**Correct Answer:** B) SOC 2 Type II evaluates operating effectiveness over time — it demonstrates that controls consistently worked, not just that they were designed to work.

**Distractor Analysis:**

- *Why B is correct:* This is the defining distinction between SOC 2 Type I and Type II. Type I is a point-in-time snapshot of control design — it says the controls look right as of a specific date. Type II evaluates actual operation over a period (typically six to twelve months) — it says the controls were consistently applied throughout that period. Enterprise customers require Type II because design adequacy without operational evidence does not prove that data was actually protected day-to-day.
- *Why A is incorrect:* Both Type I and Type II reports can cover the same set of Trust Services Criteria. The distinction between the two report types is not about which criteria are covered but about point-in-time design versus sustained operating effectiveness.
- *Why C is incorrect:* Both SOC 2 Type I and Type II are issued by independent Certified Public Accountants. The self-assessment versus independent audit distinction does not differentiate Type I from Type II.
- *Why D is incorrect:* SOC 2 is not legally mandated — it is a voluntary framework used by service organizations to demonstrate control quality to customers. Some regulations reference SOC reports as evidence of controls, but SOC 2 itself is not a legal requirement for handling personal data.

---

### Question 5

An auditor conducting a SOC 2 Type II audit for a SaaS company requests evidence that changes to production systems are authorized before deployment. Which ITSM artifact most directly satisfies this request?

- A) The company's change management policy document — a written policy stating that all changes require approval.
- B) Change records from the ITSM ticketing system showing approved change requests, approval timestamps, and the names of approvers for each change deployed during the audit period.
- C) A verbal confirmation from the IT Director that all changes are reviewed before deployment.
- D) The deployment pipeline configuration showing that an approval gate exists in the CI/CD workflow.

**Correct Answer:** B) Change records with approval history from the ticketing system provide direct, system-generated evidence that authorization controls operated consistently during the audit period.

**Distractor Analysis:**

- *Why B is correct:* SOC 2 Type II requires evidence that controls operated effectively over the entire audit period. System-generated change records showing approval history for every production change are the strongest form of evidence because they are automatic, continuous, and difficult to fabricate. They demonstrate that the authorization control was applied to actual changes, not just documented as a policy.
- *Why A is incorrect:* A policy document demonstrates that authorization is required — but it does not demonstrate that authorization was actually obtained for specific changes. Policy documents satisfy the "is it documented" question, not the "did it operate" question that Type II requires.
- *Why C is incorrect:* Verbal confirmation is the weakest form of audit evidence. SOC 2 auditors require documentary evidence, particularly for Type II's operational effectiveness standard. A verbal confirmation cannot demonstrate consistent operation over twelve months.
- *Why D is incorrect:* A pipeline configuration showing an approval gate exists is closer to Type I evidence — it demonstrates that the control is designed. It does not prove that the gate was actually used and that approvals were obtained for each change. Combined with change records, it is useful — but alone it does not satisfy the Type II standard.

---

### Question 6

A gap analysis conducted against ISO 27001 reveals that the organization has no documented process for removing access rights when employees leave the company. In the last six months, four former employees were discovered to have had active credentials for an average of three weeks after their termination. Which gap status best describes this finding?

- A) Compliant — the organization detected and remediated the access rights issue, demonstrating a functioning process.
- B) Partial Gap — a process exists but has deficiencies that allowed some access rights to persist beyond termination.
- C) Full Gap — no documented process exists for removing access rights upon employee termination, and the evidence demonstrates the control is not operating.
- D) Acceptable Risk — the access rights were revoked within the audit period, so no compliance action is required.

**Correct Answer:** C) Full Gap — the absence of a documented process combined with demonstrated operational failures indicates the control is not present.

**Distractor Analysis:**

- *Why C is correct:* ISO 27001 control A.9.2.6 requires a process for removing access rights upon termination or role change. If no documented process exists and four former employees had active credentials for an average of three weeks post-termination, the control is not in place. Detection and eventual remediation of specific incidents does not constitute a functioning control — it represents ad hoc discovery without systematic prevention.
- *Why A is incorrect:* Detecting access rights issues after the fact without a systematic process is not evidence of a functioning control — it is evidence of the absence of one. Compliance requires a proactive process that prevents the issue, not reactive discovery.
- *Why B is incorrect:* A partial gap applies when a process exists but has deficiencies. The scenario states no documented process exists — this is not a deficient process but an absent one.
- *Why D is incorrect:* "Acceptable risk" is a risk response strategy applied to known, assessed risks that the organization consciously chooses not to address. It cannot be applied post-hoc to justify a compliance failure. Former employees with active credentials represent a real, unacceptable security risk regardless of eventual remediation.

---

### Question 7

An organization's compliance dashboard shows the following: 78% of required controls are fully implemented; 15% are partially implemented; 7% have no implementation. There are 23 open audit findings from the last external audit, 14 of which are overdue. The next ISO 27001 surveillance audit is in 11 weeks. What does this dashboard data most indicate about the organization's compliance readiness?

- A) The organization is in excellent shape — 78% implementation is above average for most industries.
- B) The 11-week window presents a concern — 14 overdue findings and 22% of controls not fully implemented requires triage and a remediation sprint to close the most critical gaps before the surveillance audit.
- C) The dashboard data is incomplete — compliance readiness cannot be assessed without knowing the specific controls that are not implemented.
- D) The organization should delay the surveillance audit until all controls reach 100% implementation.

**Correct Answer:** B) The combination of overdue findings and partially implemented controls requires triage and prioritized remediation before the audit window.

**Distractor Analysis:**

- *Why B is correct:* A compliance dashboard is designed to surface exactly this kind of actionable urgency. Fourteen overdue audit findings mean that the auditor's previous concerns have not been addressed — which will be the first thing reviewed at the next surveillance audit. Twenty-two percent of controls not fully implemented is a substantial gap 11 weeks before a scheduled audit. The appropriate response is immediate triage: identify which open findings and gaps are most critical to the audit scope, assign owners, and execute a focused remediation sprint.
- *Why A is incorrect:* 78% is not "excellent shape" when an audit is 11 weeks away and 14 prior findings are overdue. Industry benchmarks for compliance percentage do not change what the auditor will find. Complacency at this stage is the wrong response.
- *Why C is incorrect:* While the specific controls matter for detailed remediation planning, the macro picture is clear enough to identify urgency. Waiting for more detail before acknowledging a readiness concern would waste the limited time available.
- *Why D is incorrect:* Delaying a surveillance audit is generally not available as an option under certification agreements — surveillance audits are part of the ongoing certification maintenance schedule. The appropriate response is focused remediation, not postponement.

---

### Question 8

Which of the following correctly describes the purpose of residual risk in IT risk management?

- A) Residual risk is the total risk before any controls are applied — the baseline from which risk management begins.
- B) Residual risk is the risk that remains after controls are implemented — the exposure the organization consciously accepts after applying its chosen response strategies.
- C) Residual risk is the risk that has been fully transferred to an insurance provider and is no longer the organization's responsibility.
- D) Residual risk is risk that has been deferred — it will be addressed in a future risk treatment cycle.

**Correct Answer:** B) Residual risk is the risk remaining after controls are applied — the accepted exposure after risk treatment.

**Distractor Analysis:**

- *Why B is correct:* No set of controls eliminates all risk. After implementing mitigating controls, transferring financial exposure, or accepting certain risks, the organization is left with residual risk — the exposure that remains. Risk management does not aim to achieve zero residual risk (which is generally impossible) but to reduce residual risk to within the organization's defined risk tolerance. Residual risk must be explicitly acknowledged and accepted by the risk owner.
- *Why A is incorrect:* The risk before controls are applied is called inherent risk. Residual risk is calculated after controls are considered, not before.
- *Why C is incorrect:* Transferred risk is risk whose financial consequences have been shifted to another party — such as an insurer. But transferred risk is still a form of risk management response, and the operational impact of the risk event typically still falls on the organization. It does not disappear from consideration entirely.
- *Why D is incorrect:* Deferred risk is not a standard ITIL 4 or risk management term. Risk treatment decisions include avoid, mitigate, transfer, or accept — not defer. An untreated risk that is acknowledged but not acted upon would fall under the "accept" category.

---

### Question 9

A healthcare organization subject to HIPAA is implementing ISO 27001. The compliance team notes that HIPAA's Security Rule requires a documented risk analysis and risk management program. How does implementing ISO 27001's risk assessment requirements relate to HIPAA's Security Rule obligations?

- A) They are entirely separate — ISO 27001 and HIPAA have no overlapping requirements.
- B) ISO 27001's risk assessment process, when applied to systems that process electronic protected health information (ePHI), can satisfy a significant portion of HIPAA's Security Rule risk analysis requirement.
- C) Implementing ISO 27001 automatically grants HIPAA compliance certification.
- D) HIPAA supersedes ISO 27001 in all healthcare organizations — ISO 27001 is irrelevant for HIPAA-covered entities.

**Correct Answer:** B) ISO 27001's risk assessment methodology, applied to ePHI systems, substantially overlaps with HIPAA's Security Rule risk analysis requirement.

**Distractor Analysis:**

- *Why B is correct:* HIPAA's Security Rule requires covered entities to conduct an accurate and thorough assessment of potential risks and vulnerabilities to ePHI. ISO 27001's risk assessment process — identifying assets, threats, vulnerabilities, likelihood, and impact — is a recognized methodology for conducting exactly this type of analysis. Organizations that implement ISO 27001 for their ePHI systems can leverage their ISO risk assessment documentation as evidence toward HIPAA's risk analysis requirement, reducing duplication of effort.
- *Why A is incorrect:* ISO 27001 and HIPAA have significant overlap in the areas of access control, incident response, encryption, asset management, and risk management. Organizations that pursue both compliance objectives routinely find that controls implemented for one framework support the other.
- *Why C is incorrect:* ISO 27001 certification does not grant HIPAA compliance. HIPAA compliance requires meeting all HIPAA-specific requirements — many of which are not addressed by ISO 27001 — and is regulated by HHS, not ISO certification bodies.
- *Why D is incorrect:* HIPAA and ISO 27001 can coexist. HIPAA is a U.S. law that sets minimum requirements for ePHI protection; ISO 27001 is an international standard that provides a systematic management framework. Healthcare organizations commonly use ISO 27001 as the management framework that helps them meet HIPAA's technical and administrative safeguard requirements.

---

### Question 10

An IT organization collects audit evidence continuously as a byproduct of normal ITSM operations rather than assembling evidence only when an audit is announced. Which of the following best describes the primary advantage of this approach?

- A) Continuous evidence collection eliminates the need for external audits — organizations can self-certify their compliance.
- B) When audits are announced, evidence is already organized and accessible, enabling rapid response and also allowing proactive identification and remediation of control failures before they become audit findings.
- C) Continuous evidence collection reduces the cost of operating ITSM tools because less storage is needed.
- D) Auditors require continuous evidence collection by law — organizations that do not collect continuously are automatically non-compliant.

**Correct Answer:** B) Pre-existing, organized evidence enables fast audit response and also surfaces control failures proactively — before they appear in an audit finding.

**Distractor Analysis:**

- *Why B is correct:* The two benefits of continuous evidence readiness are response speed and proactive control monitoring. When an audit is announced, a mature organization can provide evidence promptly — rather than spending weeks scrambling to find, assemble, and verify records under pressure. More importantly, continuously reviewing evidence (change records, access logs, incident records) surfaces gaps between policy and practice before an external auditor does, giving the organization the opportunity to remediate on its own timeline.
- *Why A is incorrect:* Continuous evidence collection does not replace the independent external audit. Self-certification has no standing with regulators, customers, or certification bodies that require independent assessment.
- *Why C is incorrect:* Continuous evidence collection typically increases storage requirements because more records are retained over longer periods. The benefit is compliance quality and readiness, not storage reduction.
- *Why D is incorrect:* While specific regulatory frameworks have data retention requirements, there is no universal law that mandates continuous evidence collection as a compliance methodology. This is a best practice, not a legal mandate that automatically triggers non-compliance for those who do not follow it.

---

### Question 11

A risk owner reviews a risk and determines that the cost of fully mitigating it would exceed the financial impact if the risk event actually occurred. The risk owner formally documents this assessment and accepts the residual risk. Which principle does this decision reflect?

- A) Risk avoidance — by accepting the risk, the organization is avoiding the cost of mitigation.
- B) Rational risk acceptance — accepting a risk when the cost of treatment exceeds the expected loss is a legitimate risk management strategy.
- C) Risk negligence — failing to mitigate a known risk is always a compliance violation.
- D) Risk transfer — accepting documentation of the risk transfers responsibility to the risk owner.

**Correct Answer:** B) Rational risk acceptance is a legitimate strategy when the cost of treatment exceeds the potential loss.

**Distractor Analysis:**

- *Why B is correct:* Risk acceptance is one of the four standard risk response strategies in ITIL 4. When the cost of a control exceeds the expected cost of the risk event (probability × impact), a rational risk management decision may be to accept the risk, document the decision, assign a risk owner, and monitor for changes in likelihood or impact. This is not negligence — it is a conscious, documented, and governed decision.
- *Why A is incorrect:* Avoidance involves eliminating the activity that creates the risk. Accepting a risk while continuing the activity is not avoidance — it is acceptance.
- *Why C is incorrect:* Accepting a risk is not automatically a compliance violation. Many compliance frameworks explicitly require risk acceptance as a documented option within a risk management program. The key is that the acceptance must be formal, documented, and reviewed periodically — not simply ignored.
- *Why D is incorrect:* Documenting a risk and assigning an owner does not constitute risk transfer. Risk transfer moves the financial consequences to another party (such as an insurer). Assigning an internal risk owner keeps accountability within the organization and is a governance step within acceptance, not transfer.

---

### Question 12

An organization stores the following types of data: customer credit card numbers, employee health records, company financial forecasts, and publicly available marketing materials. Which regulatory framework would most directly apply to the storage of customer credit card numbers?

- A) HIPAA — the Health Insurance Portability and Accountability Act.
- B) PCI-DSS — the Payment Card Industry Data Security Standard.
- C) GDPR — the General Data Protection Regulation.
- D) SOC 2 — the AICPA Service Organization Control framework.

**Correct Answer:** B) PCI-DSS specifically governs the security of cardholder data, including credit card numbers.

**Distractor Analysis:**

- *Why B is correct:* PCI-DSS is the industry standard developed by the major card networks (Visa, Mastercard, American Express, Discover) to protect cardholder data. Any organization that stores, processes, or transmits credit card numbers is subject to PCI-DSS requirements. Its 12 requirements address network security, access control, encryption, monitoring, and vulnerability management specifically in the context of payment card data.
- *Why A is incorrect:* HIPAA governs the protection of electronic protected health information (ePHI) in healthcare settings. Credit card numbers are not ePHI. HIPAA would apply to the employee health records in this scenario, not the payment data.
- *Why C is incorrect:* GDPR governs the processing of personal data of EU residents broadly, and credit card numbers of EU residents could fall within its scope as personal data. However, PCI-DSS is the primary, most directly applicable framework for payment card data security, regardless of geography.
- *Why D is incorrect:* SOC 2 is an auditing framework for service organizations, not a regulatory requirement. An organization may obtain SOC 2 certification to demonstrate its controls to customers, but SOC 2 does not create a compliance obligation for handling credit card numbers — PCI-DSS does.

---

### Question 13

An IT risk register lists a risk as: "Critical ERP system hosted on a single server with no redundancy." The risk has been in the register for 14 months and is listed as "accepted." No acceptance documentation exists, no risk owner is assigned, and no review date is recorded. What does this situation represent?

- A) Proper risk acceptance — if the risk is accepted, no further action is needed.
- B) A governance failure — risk acceptance without documentation, ownership, or review schedule is not risk management; it is untracked exposure.
- C) Risk avoidance — removing the risk from active consideration is equivalent to avoiding it.
- D) Appropriate risk deferral — some risks cannot be addressed and must be left for future cycles.

**Correct Answer:** B) Undocumented, unowned risk acceptance with no review schedule is a governance failure, not a managed risk response.

**Distractor Analysis:**

- *Why B is correct:* Legitimate risk acceptance requires: a documented rationale for why acceptance is appropriate, a named risk owner who monitors the risk, and a review schedule to reassess the acceptance decision if conditions change. A risk that sits in a register for 14 months with "accepted" status but no documentation, no owner, and no review is a risk that has simply been ignored. The absence of these governance attributes transforms accepted risk into unmanaged exposure.
- *Why A is incorrect:* Risk acceptance is not a one-time decision that requires no follow-up. Accepted risks must be owned, documented, and periodically reviewed because their likelihood and impact change over time. A 14-month-old undocumented acceptance is not properly managed risk.
- *Why C is incorrect:* Risk avoidance requires eliminating the activity that creates the risk. Listing a risk as accepted while the single-server ERP continues to operate unchanged is not avoidance — the risk-creating condition (no redundancy) is still present.
- *Why D is incorrect:* Risk deferral is not a standard ITIL 4 or ISO 31000 risk response category. If a risk is genuinely not addressable currently, it should be formally accepted with documentation of why treatment is not feasible and when the decision will be revisited — not left unowned in a register.

---

### Question 14

A company's compliance team discovers that its change management policy requires change records to be retained for five years, but the ITSM tool is configured to purge records after 18 months. An ISO 27001 internal audit is scheduled in six weeks. What is the most appropriate immediate action?

- A) Update the ITSM tool retention settings to five years going forward, and document the discrepancy as an internal audit finding requiring remediation.
- B) Delete the compliance team's discovery notes to prevent the finding from appearing in the audit.
- C) Inform the external auditor in advance that the retention gap exists and request an audit postponement.
- D) Migrate all ITSM data to a new platform with proper retention settings before the audit.

**Correct Answer:** A) Fix the configuration going forward, document the gap as an internal finding, and prepare remediation evidence for the audit.

**Distractor Analysis:**

- *Why A is correct:* When a compliance gap is discovered before an audit, the appropriate response is to fix the issue where possible and document it honestly as an internal finding. Updating the retention setting immediately stops the gap from growing. Documenting it as an internal finding demonstrates that the organization has a functioning internal audit process — which ISO 27001 requires. Auditors view proactively identified and remediated findings more favorably than gaps they discover themselves.
- *Why B is incorrect:* Destroying evidence of a known compliance issue is a serious integrity violation that could result in audit disqualification, certification revocation, and legal exposure. It directly contradicts ISO 27001's continual improvement and honest management review requirements.
- *Why C is incorrect:* Informing the auditor in advance is part of transparent audit management, but requesting postponement is generally not available for scheduled surveillance audits and is not the primary response. The gap should be fixed and documented, not deferred.
- *Why D is incorrect:* Migrating to a new platform in six weeks to obscure a compliance gap is both impractical and inadvisable. Platform migrations are major changes that introduce their own risks and could create additional audit findings. The gap in historical records cannot be retroactively restored by a platform change anyway.

---

### Question 15

In the context of ITSM and compliance, which description best explains what a control is?

- A) A control is a documented policy statement that describes what the organization intends to do about a risk.
- B) A control is a measure that modifies risk by reducing its likelihood, limiting its impact, or both — it may be technical, procedural, or physical in nature.
- C) A control is the action taken after a risk event occurs to restore normal operations.
- D) A control is a metric used to measure how often a risk event occurs.

**Correct Answer:** B) A control modifies risk by reducing likelihood or impact through technical, procedural, or physical means.

**Distractor Analysis:**

- *Why B is correct:* Controls are the primary mechanism for risk treatment in ISO 27001 and broader risk management frameworks. A control may be technical (firewall rule, encryption, access restriction), procedural (change approval process, incident response procedure), or physical (locked server room, security camera). All controls function by either reducing the probability that a risk event will occur or limiting the damage if it does. ITIL 4's service management practices generate many controls as byproducts of normal operations.
- *Why A is incorrect:* A policy statement describes intent but is not itself a control. A policy that states "all production changes must be authorized" becomes a control only when it is operationalized through a working process that actually enforces authorization. Policy without operation is not a functioning control.
- *Why C is incorrect:* Actions taken after a risk event occurs are incident response or recovery actions — not controls in the risk management sense. Controls act before or during an event, not after. Post-event remediation may reduce impact, but it is distinct from preventive or detective control operation.
- *Why D is incorrect:* A metric measures frequency, severity, or status but does not by itself modify risk. Monitoring the frequency of risk events is part of risk tracking and reporting, not a control. A metric combined with an alert threshold that triggers a human response is closer to a detective control, but the metric alone is measurement, not modification.

---

### Question 16

An organization's risk register shows that a critical manufacturing system has a residual risk of "High" after all available controls are applied. The risk cannot be further reduced without replacing the entire system, which is budgeted for two years from now. What is the most appropriate action for the risk owner to take today?

- A) Remove the risk from the register until the system replacement is approved.
- B) Escalate the residual high risk to executive leadership for formal acceptance, document the decision, and establish enhanced monitoring with a defined review schedule until the system replacement is completed.
- C) Classify the risk as transferred because the replacement project has been funded.
- D) Accept the risk informally and continue normal operations until the replacement is complete.

**Correct Answer:** B) High residual risk requires executive escalation, formal acceptance documentation, enhanced monitoring, and a defined review schedule.

**Distractor Analysis:**

- *Why B is correct:* When residual risk is high and treatment options are exhausted or deferred, the risk cannot simply be left unmanaged — it requires formal escalation to the appropriate authority level. Executive leadership must formally accept a high residual risk because the potential consequences exceed the authority of operational management. Enhanced monitoring compensates partially for the absence of complete risk treatment by enabling faster detection and response if the risk materializes.
- *Why A is incorrect:* Removing a risk from the register because it cannot be remediated immediately is risk concealment, not risk management. The risk continues to exist regardless of whether it is tracked. Removing it prevents proper governance of an acknowledged exposure.
- *Why C is incorrect:* A funded replacement project in two years is not risk transfer. Transfer moves financial consequences to another party. Budgeting for future system replacement is a planned risk treatment, not a transfer. The risk exposure remains entirely within the organization until the replacement is complete.
- *Why D is incorrect:* Informal acceptance without documentation or monitoring is the governance failure described in Question 13. High residual risk requires formal acceptance at an appropriate authority level, not informal continuation of normal operations without governance.

---

### Question 17

An organization implements multi-factor authentication (MFA) across all remote access connections. Before MFA, the probability of an unauthorized remote access event was assessed as "Likely." After MFA implementation, the probability is reassessed as "Unlikely." Which risk characterization dimension did MFA primarily affect?

- A) Impact — MFA reduced the severity of harm that would result from an unauthorized access event.
- B) Likelihood — MFA reduced the probability of an unauthorized access event occurring.
- C) Residual risk — MFA eliminated all remaining risk from remote access.
- D) Risk appetite — implementing MFA changed the organization's tolerance for remote access risk.

**Correct Answer:** B) MFA primarily reduced the likelihood (probability) of an unauthorized remote access event occurring.

**Distractor Analysis:**

- *Why B is correct:* MFA is a preventive control — it makes unauthorized access harder to achieve by requiring a second authentication factor that an attacker typically does not possess. Its primary effect is on likelihood: the probability of a successful unauthorized access event is lower because most attack scenarios (password theft, credential stuffing) are defeated by the second factor. The impact of a successful breach event remains the same — MFA does not reduce the damage done if an attacker does somehow get in.
- *Why A is incorrect:* MFA does not reduce the impact of a successful unauthorized access event. If an attacker bypasses MFA and accesses the system, the data they can access and the harm they can cause is unchanged. Impact reduction would require controls like data segmentation, least-privilege access, or encryption of sensitive data at rest.
- *Why C is incorrect:* MFA reduces residual risk by lowering likelihood, but it does not eliminate all remaining risk. Residual risk from remote access still exists after MFA — social engineering, SIM swapping, and authenticator app compromise are all potential vectors. Residual risk is reduced, not eliminated.
- *Why D is incorrect:* Risk appetite is an organizational governance decision about how much risk is acceptable. Implementing a control does not change the organization's risk appetite — it changes the actual risk level to bring it within or closer to the defined appetite. Risk appetite informs the decision to implement controls; controls do not change the appetite.

---

### Question 18

A company completes a SOC 2 Type II audit and receives a report with a qualified opinion. The auditor found that one control — the requirement to disable access within 24 hours of employee termination — operated effectively for 9 of 12 months but had three documented exceptions in the remaining months. What does a qualified opinion mean, and how should the company respond?

- A) A qualified opinion means the company passed the audit with distinction — "qualified" indicates superior performance.
- B) A qualified opinion indicates that controls were generally effective but had specific documented exceptions — the company should investigate the root cause of the three exceptions, implement corrective controls, and address the finding in the next audit period.
- C) A qualified opinion voids the SOC 2 report — the company must restart the audit from the beginning.
- D) A qualified opinion means the audit is still in progress — the auditor needs more evidence before issuing a final opinion.

**Correct Answer:** B) A qualified opinion identifies specific exceptions to otherwise effective controls; the company should investigate, remediate, and address the findings in the next audit period.

**Distractor Analysis:**

- *Why B is correct:* In auditing, a "qualified opinion" indicates that controls were generally effective but with specific, documented exceptions. It is not a failure — the report is still issued and is generally accepted by customers. However, the exceptions are documented in the report and are visible to any organization reviewing it. The company should treat each exception as a corrective action item, investigate the root cause, and demonstrate remediation in the next audit cycle.
- *Why A is incorrect:* In auditing terminology, "qualified" does not mean superior. A qualified opinion indicates that while the auditor can generally issue an opinion, something specific prevented a completely clean assessment. It is often confused with the informal English usage of "qualified" as meaning skilled or accomplished.
- *Why C is incorrect:* A qualified opinion does not void the report. The report is issued with the qualified opinion documented, and it can still be shared with customers. Many enterprise customers will accept a qualified SOC 2 report alongside a remediation plan for the noted exceptions.
- *Why D is incorrect:* A qualified opinion is a final audit opinion, not an interim status. If the audit were still in progress, no opinion would have been issued. The auditor has completed the assessment and issued a final opinion that identifies specific exceptions.

---

### Question 19

Which of the following most accurately describes the relationship between risk management and ITSM practices in ITIL 4?

- A) Risk management is a separate discipline that operates independently of ITSM — the two do not interact.
- B) ITSM practices generate risk data, implement controls, and provide evidence of control operation, while risk management uses this information to maintain the organization's risk posture.
- C) Risk management replaces ITSM practices in high-risk environments — organizations subject to strict regulatory requirements do not need formal ITSM frameworks.
- D) ITSM practices create risk and risk management is responsible for eliminating those risks entirely.

**Correct Answer:** B) ITSM practices and risk management are mutually reinforcing — ITSM generates risk-relevant data and implements controls while risk management governs overall posture.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 explicitly integrates risk management with service management. Change Enablement assesses risk before authorizing changes. Incident Management detects risk events in progress. Problem Management identifies systemic risks. IT Asset Management tracks asset-related risks. Each of these practices generates data that feeds risk registers and implements controls that appear in the Statement of Applicability. Risk management, in turn, sets the risk appetite and priorities that inform how ITSM practices are configured and resourced.
- *Why A is incorrect:* ITIL 4 describes risk as a shared responsibility across all practices and explicitly includes risk management considerations in the service value chain. The two disciplines are deeply integrated in ITIL 4's design.
- *Why C is incorrect:* High-risk and regulated environments typically require both robust risk management and formal ITSM frameworks. Regulatory requirements such as HIPAA, PCI-DSS, and ISO 27001 frequently require ITSM-like controls (change management, access control procedures, incident response) as specific safeguards. The two frameworks reinforce each other in regulated contexts.
- *Why D is incorrect:* ITSM practices do not inherently create net risk — they manage risk by providing structured processes for operating IT services. The claim that risk management should "eliminate all risks" also contradicts ITIL 4's risk management philosophy, which accepts that residual risk is normal and that the goal is to bring risk within acceptable tolerance, not to eliminate it.

---

### Question 20

A security team is prioritizing remediation of three vulnerabilities. Vulnerability A has a high impact but a very low likelihood of exploitation because it requires physical access to a restricted data center. Vulnerability B has a medium impact and medium likelihood — exploitable remotely via a known public exploit. Vulnerability C has a low impact and very high likelihood — it is being actively exploited in the wild but only allows read access to non-sensitive cached data. In what order should these vulnerabilities be prioritized for remediation, and why?

- A) A first, B second, C third — highest impact should always be addressed first.
- B) B first, C second, A last — risk score (likelihood × impact) combined with exploitability in the current threat environment suggests B poses the highest combined exposure, C poses active but limited exposure, and A's physical access requirement significantly reduces its effective likelihood.
- C) C first, B second, A last — active exploitation in the wild always takes priority over theoretical risk.
- D) All three are equal — likelihood and impact cannot be compared across different vulnerability types.

**Correct Answer:** B) Risk-informed prioritization considers both likelihood and impact together — B's combined exposure and active public exploit makes it highest priority, C's active but limited exploitation is next, and A's physical access requirement significantly reduces its effective likelihood.

**Distractor Analysis:**

- *Why B is correct:* Risk prioritization requires evaluating both dimensions together. Vulnerability B has a known public exploit (elevated effective likelihood) and medium impact — its risk score is moderate to high and it is actionable. Vulnerability C is being actively exploited (very high likelihood) but its impact is limited to non-sensitive cached data (low impact) — the risk score is moderate and the business consequence is contained. Vulnerability A has high impact but very low effective likelihood due to the physical access requirement — a meaningful control is already in place. The risk register score for A may appear high on paper but its effective likelihood is suppressed by the existing physical control.
- *Why A is incorrect:* Prioritizing solely by impact ignores likelihood. Vulnerability A's high impact is effectively reduced by the physical access control already in place. Addressing it ahead of an actively exploitable remote vulnerability (B) would misallocate remediation resources toward a lower effective risk.
- *Why C is incorrect:* Active exploitation is a significant urgency factor but is not the only factor. If Vulnerability C is being actively exploited but the impact is trivially low (non-sensitive cached read access), and Vulnerability B is imminently exploitable with medium impact, prioritizing C over B would leave a higher-consequence exploitable vulnerability open longer. Risk score and business impact must both inform the decision.
- *Why D is incorrect:* Risk management exists precisely to compare and prioritize risks across different categories using the common dimensions of likelihood and impact. Claiming they cannot be compared is a practical abdication of the risk management function. All risk management frameworks — ISO 31000, NIST, ISO 27001 — provide methods for cross-domain risk comparison and prioritization.

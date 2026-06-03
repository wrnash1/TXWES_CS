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

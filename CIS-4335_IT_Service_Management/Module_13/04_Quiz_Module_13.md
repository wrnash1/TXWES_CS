# Quiz: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

### Question 1

What is the defined purpose of IT Asset Management in ITIL 4?

- A) To track and manage the configuration of all IT components in order to support other ITSM practices.
- B) To plan and manage the full lifecycle of all IT assets to maximize value, control costs, manage risks, support decision-making, and meet regulatory requirements.
- C) To ensure that software development teams follow approved change processes before deploying new features.
- D) To monitor all IT assets in real time for security events and alert the information security team.

**Correct Answer:** B) The purpose of IT Asset Management is to plan and manage the full lifecycle of all IT assets to maximize value, control costs, manage risks, support decision-making, and meet regulatory requirements.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 explicitly defines this as the purpose of IT Asset Management. The four objectives — maximize value, control costs, manage risks, meet regulatory requirements — reflect the practice's focus on the full financial, operational, and legal dimensions of asset ownership throughout the asset lifecycle.
- *Why A is incorrect:* Tracking and managing the configuration of IT components is the purpose of Service Configuration Management, not IT Asset Management. Configuration Management focuses on CIs and their relationships to support service delivery; Asset Management focuses on the financial and lifecycle value of assets.
- *Why C is incorrect:* Ensuring software development follows approved change processes is the purpose of Change Enablement. This has no connection to asset lifecycle management.
- *Why D is incorrect:* Real-time monitoring for security events is the purpose of Monitoring and Event Management and Information Security Management. IT Asset Management focuses on lifecycle and inventory management, not event-based alerting.

---

### Question 2

An organization's CMDB shows that a server hosts three critical applications. The change manager proposes a hardware upgrade to that server. Which CMDB capability makes this information most directly useful for evaluating the proposed change?

- A) The CMDB's historical record of when the server was purchased and how much it cost.
- B) The CMDB's relationship mapping, which shows which services and applications depend on that server and will be affected by the change.
- C) The CMDB's list of software licenses installed on the server and their expiration dates.
- D) The CMDB's record of past incidents associated with that server model.

**Correct Answer:** B) The CMDB's relationship mapping enables impact analysis by showing which services and applications depend on the server being changed.

**Distractor Analysis:**

- *Why B is correct:* The most distinctive value of a CMDB over a simple asset spreadsheet is relationship mapping. By recording that Server A hosts Application B, which supports Service C, which is covered by SLA D, the CMDB enables impact analysis — the process of determining what will be affected by a proposed change. This is how Change Management uses the CMDB, and it is only possible because relationships are tracked.
- *Why A is incorrect:* Purchase date and cost are financial asset management data. They are relevant to budgeting and depreciation but do not help assess the operational impact of a proposed hardware change.
- *Why C is incorrect:* License expiration dates are Software Asset Management data. While relevant to compliance, they do not address the question of which services will be affected by the hardware upgrade.
- *Why D is incorrect:* Past incident history is useful for problem management analysis but does not tell the change manager which services will be impacted by the proposed hardware change.

---

### Question 3

A software vendor notifies a company that it will be conducting an audit of its Adobe Creative Cloud usage. The company's IT Asset Manager discovers that 180 users are actively using the software but only 140 named-user licenses were purchased. What term describes this situation, and what is the primary risk?

- A) Over-licensing — the primary risk is financial waste from purchasing more licenses than needed.
- B) Under-licensing — the primary risk is legal and compliance exposure because the company is using software beyond the terms of its license agreement.
- C) License drift — the primary risk is that the CMDB is out of date and discovery data is inaccurate.
- D) Concurrent violation — the primary risk is that too many users are logged in simultaneously for the concurrent license count.

**Correct Answer:** B) Under-licensing — 40 users are using the software without a license, creating legal and compliance exposure during the vendor audit.

**Distractor Analysis:**

- *Why B is correct:* Under-licensing occurs when actual usage exceeds licensed entitlements. Named-user licensing requires one license per authorized user — 180 users with 140 licenses means 40 users are unlicensed. This is a breach of the license agreement. The vendor audit will identify this gap, and the company faces retroactive license fees, penalties, and potentially other contractual consequences.
- *Why A is incorrect:* Over-licensing is the opposite problem — purchasing more licenses than needed. In this scenario, usage exceeds entitlements, so this is under-licensing, not over-licensing.
- *Why C is incorrect:* License drift is not a standard ITIL 4 term, and the scenario does not describe a CMDB accuracy problem — it describes a specific compliance gap between entitlements and actual usage.
- *Why D is incorrect:* The license model is named-user, not concurrent. Named-user licensing counts total authorized users, not simultaneous logins. A concurrent violation would apply to a concurrent (floating) license model.

---

### Question 4

An organization purchases 500 Microsoft 365 Business licenses in January for a workforce of 480 employees. By October, the company downsizes and has 390 active employees, all of whom use Microsoft 365. The remaining 110 licenses expire in January. What term describes this situation, and what action should the IT Asset Manager take?

- A) Under-licensing — the IT Asset Manager should immediately purchase additional licenses to avoid compliance risk.
- B) Over-licensing — the IT Asset Manager should plan to renew only 390 licenses (or the current headcount) when the subscription expires in January, avoiding unnecessary spend.
- C) License expiration — the IT Asset Manager should renew all 500 licenses immediately to prevent a lapse in compliance.
- D) License drift — the IT Asset Manager should run a discovery scan to determine the actual installation count.

**Correct Answer:** B) Over-licensing — the organization is paying for 110 licenses it does not need; the appropriate action is to right-size the renewal to match actual usage.

**Distractor Analysis:**

- *Why B is correct:* Over-licensing occurs when an organization has purchased more licenses than it uses. Paying for 500 licenses when only 390 are needed wastes the cost of 110 seats. The appropriate SAM action is to right-size at renewal — purchasing only the licenses needed for the current user count. Subscription licensing with annual renewal creates a natural opportunity to adjust license counts.
- *Why A is incorrect:* The organization is compliant — 390 users are covered by 500 licenses. There is no under-licensing. Purchasing additional licenses would worsen the over-licensing problem.
- *Why C is incorrect:* Renewing all 500 licenses would perpetuate the financial waste of 110 unused seats. The audit trigger is not present here — the appropriate action is reduction, not continuation.
- *Why D is incorrect:* A discovery scan is already informing the analysis — the scenario states 390 active employees use the software. License drift (a non-standard term) is not the applicable concept here; the issue is excess entitlement relative to confirmed usage.

---

### Question 5

A hospital IT department is preparing to donate 60 desktop computers to a local school district. The computers previously processed patient medical records. Which data sanitization approach is most appropriate before the hardware is transferred?

- A) No sanitization is required because the computers are being donated, not sold — the school district is a trusted recipient.
- B) Physical destruction — shred the storage media before transferring the computer cases to the school district.
- C) Software-based overwriting using a NIST SP 800-88 approved method, followed by verification and documentation with a sanitization certificate.
- D) Simply uninstall the hospital's applications and delete user accounts — this is sufficient to protect patient data.

**Correct Answer:** C) Software-based overwriting per NIST SP 800-88, with verification and a sanitization certificate, is the appropriate method for hardware being reused.

**Distractor Analysis:**

- *Why C is correct:* The hospital is subject to HIPAA, which requires that electronic protected health information be rendered unreadable and indecipherable before hardware is disposed of or transferred. Software-based overwriting per NIST SP 800-88 accomplishes this while preserving the hardware for reuse by the school district. The sanitization certificate documents compliance for HIPAA audit purposes. This is the appropriate balance between data security and hardware utility.
- *Why A is incorrect:* HIPAA imposes data sanitization requirements regardless of who receives the hardware. Being a trusted recipient does not waive the legal obligation to sanitize ePHI before transfer.
- *Why B is incorrect:* Physical destruction would make the computers unusable, defeating the purpose of donation. While physical destruction is the most certain sanitization method, it is appropriate when hardware will not be reused — not when the intent is donation.
- *Why D is incorrect:* Uninstalling applications and deleting user accounts does not remove data from storage media. Data deleted at the operating system level is typically recoverable using standard forensic tools. This approach would leave patient records accessible to anyone with basic data recovery skills.

---

### Question 6

An asset discovery tool scans NCC's network and identifies 47 devices that are not in the CMDB. Separately, the CMDB contains records for 12 devices that the discovery scan did not find. What do these two findings most likely indicate?

- A) The discovery tool is malfunctioning — only CMDB records should be trusted.
- B) The 47 unrecorded devices are unauthorized; all 12 missing devices have been stolen.
- C) The 47 devices may be unauthorized or undocumented assets; the 12 missing devices may be decommissioned, offline, or in need of record retirement from the CMDB.
- D) The CMDB has too many records — all 12 missing devices should be deleted immediately.

**Correct Answer:** C) Both discrepancy types trigger investigation: unrecorded devices may be unauthorized assets; CMDB records for devices no longer found may need to be retired.

**Distractor Analysis:**

- *Why C is correct:* CMDB discrepancies in both directions require investigation, not immediate deletion or assumption of theft. The 47 undiscovered devices could be new assets that were never recorded, authorized assets on network segments the scan did not cover, or unauthorized devices. The 12 devices in CMDB but not discovered could be decommissioned, powered off, moved to an unscanned location, or stolen. Each case requires verification before action.
- *Why A is incorrect:* Discovery tool findings are a primary mechanism for maintaining CMDB accuracy. Dismissing discovery data in favor of potentially stale CMDB records defeats the purpose of running discovery scans.
- *Why B is incorrect:* Assuming all unrecorded devices are unauthorized and all missing devices are stolen is not a justified conclusion from discovery scan data alone. Both scenarios require investigation, not automatic assumption.
- *Why D is incorrect:* Deleting CMDB records for unconfirmed retired assets before investigation could result in losing records for assets that are still active but temporarily unreachable. Investigation must precede deletion.

---

### Question 7

Which of the following best describes the relationship between IT Asset Management and Service Configuration Management in ITIL 4?

- A) They are the same practice — ITIL 4 uses both names interchangeably.
- B) IT Asset Management focuses on the financial and lifecycle value of assets; Service Configuration Management focuses on the attributes and relationships of configuration items that support service delivery.
- C) Service Configuration Management manages hardware assets; IT Asset Management manages software assets only.
- D) IT Asset Management is a subset of Service Configuration Management — every configuration item is also an IT asset.

**Correct Answer:** B) The two practices have complementary but distinct focus areas — Asset Management on value and lifecycle, Configuration Management on CI attributes and relationships.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 defines these as distinct practices with different purposes. IT Asset Management's purpose centers on value maximization, cost control, lifecycle management, and regulatory compliance. Service Configuration Management's purpose centers on ensuring accurate information about configuration items and their relationships to support service management. The two practices share data — every asset that is a CI has both an asset record and a CI record — but their management objectives differ.
- *Why A is incorrect:* ITIL 4 explicitly defines these as two separate practices with distinct purposes. They are complementary but not interchangeable.
- *Why C is incorrect:* Both practices apply to all categories of assets and configuration items. The distinction is not by asset type but by management purpose — financial/lifecycle versus attribute/relationship.
- *Why D is incorrect:* The relationship works in both directions — some assets are not managed as CIs (minor peripherals below a tracking threshold), and some CIs are not financial assets (documentation, processes). The overlap is significant but neither practice is a complete subset of the other.

---

### Question 8

An organization discovers that its CMDB has not been updated in eight months. During that time, 45 servers were provisioned in the cloud, 12 physical servers were decommissioned, and 200 software licenses were purchased. What is the primary risk created by this eight-month CMDB gap?

- A) The organization will be charged extra by cloud providers for unregistered assets.
- B) Change impact analysis, incident diagnosis, and compliance reporting will be based on inaccurate data — increasing the risk of unintended service disruption and regulatory exposure.
- C) The CMDB license will be revoked by the software vendor if records are not current.
- D) Discovery scans will fail if the CMDB baseline is too old.

**Correct Answer:** B) An outdated CMDB undermines every practice that depends on accurate asset and relationship data — change impact analysis, incident diagnosis, and compliance.

**Distractor Analysis:**

- *Why B is correct:* The CMDB serves as the authoritative foundation for multiple ITSM practices. When it is eight months out of date, every decision made using its data is potentially wrong. A change manager assessing impact does not know about the 45 new cloud servers. An incident responder does not know that 12 physical servers are decommissioned. A compliance officer's asset inventory is incomplete. Each of these gaps creates specific, concrete risks to service quality and regulatory standing.
- *Why A is incorrect:* Cloud providers charge based on resources consumed, not CMDB registration status. CMDB records have no effect on cloud billing.
- *Why C is incorrect:* CMDB software vendors do not revoke licenses based on data currency. CMDB license compliance is governed by the number of users or managed nodes, not record freshness.
- *Why D is incorrect:* Discovery scans operate independently of CMDB baselines — they scan the network regardless of CMDB state. The output of a discovery scan is then compared to CMDB records, which is how discrepancies are identified.

---

### Question 9

A company completes its annual software license audit and finds that it is compliant with all license agreements. However, the IT Asset Manager notes that four software products represent 62% of the total software licensing budget, but usage data shows that two of those products have an average utilization rate of 11% over the past six months. Which SAM action is most appropriate?

- A) Immediately terminate all licenses for the two underutilized products to recover budget.
- B) Analyze whether the low utilization reflects genuine low demand or barriers to adoption, then right-size license counts at renewal if genuine low demand is confirmed.
- C) Do nothing — the company is compliant, which is the only objective of SAM.
- D) Purchase additional licenses for the underutilized products to encourage more adoption.

**Correct Answer:** B) Low utilization warrants investigation before action — barriers to adoption must be ruled out before right-sizing at renewal.

**Distractor Analysis:**

- *Why B is correct:* SAM addresses both compliance risk (under-licensing) and financial efficiency (over-licensing). 11% utilization across six months strongly suggests over-licensing, but the correct response is investigation before action. Low utilization could reflect genuine low demand (supporting license reduction at renewal) or barriers to adoption such as inadequate training, poor integration, or user preference for alternative tools. The distinction matters — right-sizing a product users cannot access is different from right-sizing one users have chosen not to use.
- *Why A is incorrect:* Immediately terminating licenses could disrupt the 11% of users who are actively using the products. Contract terms may also impose penalties for early termination. Investigation and right-sizing at renewal is the appropriate approach.
- *Why C is incorrect:* SAM's objectives include both compliance and cost efficiency. Compliance without efficiency leaves significant budget waste unaddressed — one of the explicit risks SAM is designed to control.
- *Why D is incorrect:* Purchasing additional licenses for an underutilized product would increase cost without evidence that demand exists. If utilization is low due to poor fit or user resistance, more licenses will not increase adoption.

---

### Question 10

Which of the following correctly describes the purpose of retaining a certificate of destruction or sanitization for each disposed IT asset?

- A) The certificate proves that the asset was not stolen — it establishes a chain of custody showing the asset was intentionally disposed of.
- B) The certificate serves as evidence that data protection obligations were met during disposal, supporting compliance audits and demonstrating due diligence to regulators.
- C) The certificate is required by ITIL 4 and must be submitted to Axelos as part of annual compliance reporting.
- D) The certificate entitles the organization to a tax deduction for the disposed hardware.

**Correct Answer:** B) The certificate documents that sanitization was performed, supporting compliance audits and demonstrating that the organization met its data protection obligations.

**Distractor Analysis:**

- *Why B is correct:* Regulators under HIPAA, GDPR, PCI-DSS, and other frameworks may ask an organization to demonstrate that hardware containing regulated data was properly sanitized before disposal. The certificate of destruction — documenting the asset, the date, the method, and the party that performed the sanitization — is the evidence that answers this question. It also protects the organization if a data breach claim is later made related to a disposed device.
- *Why A is incorrect:* While a certificate does establish a disposal record, its primary purpose is data protection compliance documentation, not theft prevention. A chain of custody for theft prevention purposes would typically involve different documentation.
- *Why C is incorrect:* Axelos does not collect or require disposal certificates. ITIL 4 establishes best practices for asset disposal documentation, but this is an organizational process requirement, not a certification-body submission requirement.
- *Why D is incorrect:* While charitable donations of hardware may have tax implications in some jurisdictions, the certificate of destruction or sanitization is a data protection document, not a tax document. Tax treatment of donated hardware is governed by accounting and tax regulations, not ITAM documentation practices.

---

### Question 11

An IT Asset Manager discovers that 30 laptops last seen in the CMDB as "in use" have not checked in to the endpoint management system in 90 days. The associated employees are still shown as active in HR records. What is the most appropriate first action?

- A) Mark all 30 laptops as "lost" in the CMDB and initiate insurance claims immediately.
- B) Investigate the discrepancy by cross-referencing with HR, the employees' managers, and physical location records before changing the CMDB status.
- C) Delete the 30 records from the CMDB to prevent inaccurate data from affecting impact analysis.
- D) Assume the laptops are decommissioned and generate certificates of destruction.

**Correct Answer:** B) Investigate the discrepancy before taking action — discovery data alone is insufficient to determine the asset's actual status.

**Distractor Analysis:**

- *Why B is correct:* A 90-day check-in gap has multiple plausible explanations — the employee may be on extended leave, the laptop may be in a location without corporate network access, the endpoint agent may have been uninstalled, or the device may genuinely be lost. The CMDB update should reflect confirmed facts, not assumptions. Cross-referencing HR status, manager records, and physical location data is the appropriate investigation step before any status change or escalation.
- *Why A is incorrect:* Filing insurance claims requires confirmed loss determination. Initiating claims without investigation could result in false claims if the laptops are located — a legal and financial risk. Discovery gap alone is not proof of loss.
- *Why C is incorrect:* Deleting CMDB records before confirming asset status destroys the audit trail needed to investigate and resolve the discrepancy. If the laptops are later found, the records will need to be recreated. Investigation precedes record deletion.
- *Why D is incorrect:* Generating certificates of destruction without performing actual data sanitization is fraudulent documentation. A certificate of destruction must reflect actual sanitization — it cannot be generated proactively based on an assumption that hardware no longer exists.

---

### Question 12

A university IT department tracks all devices with a replacement value above $500 in its CMDB as formal configuration items. Devices below $500 — primarily keyboards, mice, and USB hubs — are recorded in a separate inventory spreadsheet but are not in the CMDB. Which IT Asset Management principle does this policy reflect?

- A) This is a compliance violation — ITIL 4 requires all physical assets to be in the CMDB.
- B) This reflects the principle of establishing a tracking threshold — not all assets justify the overhead of full CMDB management, and organizations set minimum value or criticality levels for formal CI registration.
- C) This is over-management — keyboards and mice should not be tracked at all because they have no business impact.
- D) This reflects under-management — the CMDB should contain every physical object in the building.

**Correct Answer:** B) Establishing a tracking threshold is standard ITAM practice — not all assets justify full CMDB management overhead.

**Distractor Analysis:**

- *Why B is correct:* ITIL 4 does not require every physical object to be managed as a formal configuration item. IT Asset Management practice recognizes that maintaining full lifecycle records for low-value, easily replaceable items creates administrative overhead that exceeds the value of the information produced. Organizations establish thresholds — by value, criticality, or both — to focus CMDB resources on assets where accurate tracking produces material value for impact analysis, financial management, and compliance.
- *Why A is incorrect:* ITIL 4 does not mandate CMDB registration for all physical assets. The practice guides organizations to define appropriate tracking levels based on the value and risk of each asset category. A separate inventory for minor peripherals is a legitimate and common approach.
- *Why C is incorrect:* Tracking keyboards and mice in a lightweight inventory (even a spreadsheet) is reasonable for basic accountability, particularly for assets that can be purchased with petty cash and go missing frequently. Complete non-tracking of physical assets creates accountability gaps. The question is what level of tracking is appropriate, not whether to track at all.
- *Why D is incorrect:* Managing every physical object as a CMDB CI would create unsustainable administrative burden. The CMDB would be flooded with records for $15 mice and $8 USB cables, obscuring the records for the servers, network devices, and licensed software where CMDB accuracy has material operational and financial value.

---

### Question 13

An organization's IT Asset Manager is preparing for a vendor software license audit covering the past three years. The organization has complete SAM records — purchase records, deployment data, and utilization reports — for the current year but has incomplete records for the prior two years. What risk does this create, and what is the appropriate response?

- A) No risk — software audits only cover the current year's usage.
- B) The incomplete historical records create exposure for the audit period they do not cover; the organization should attempt to reconstruct historical data from purchase orders, emails, and system logs while engaging legal counsel about the audit scope.
- C) The organization should deny access to the auditor because incomplete records would result in automatic non-compliance findings.
- D) The organization should immediately terminate all software contracts to prevent the audit from proceeding.

**Correct Answer:** B) Incomplete records create audit exposure for uncovered periods; the appropriate response is reconstruction efforts and legal counsel engagement.

**Distractor Analysis:**

- *Why B is correct:* Software license audits typically cover a defined period, often 1–3 years. Incomplete records for prior years leave the organization unable to demonstrate compliance for those periods, which may result in adverse findings even if actual usage was compliant. The appropriate response is to reconstruct historical data from available sources — purchase orders, contract records, IT ticketing history — while engaging legal counsel to understand audit scope, negotiate terms if possible, and prepare for potential findings.
- *Why A is incorrect:* Most vendor audit rights cover multi-year periods defined in the license agreement — commonly 1–3 years of audit lookback. A current-year-only assumption would be incorrect and potentially costly if the auditor identifies historical gaps.
- *Why C is incorrect:* Denying auditor access when contractual audit rights exist exposes the organization to immediate contract termination and legal action. Cooperation — even with incomplete records — is generally the legally appropriate response, with counsel advising on scope and disclosure.
- *Why D is incorrect:* Terminating software contracts does not eliminate audit rights that have already accrued under prior agreements. Vendors retain the right to audit usage during the contract period regardless of subsequent termination, and terminating active contracts would disrupt operations unnecessarily.

---

### Question 14

A company is evaluating whether to renew a three-year enterprise agreement for a productivity suite at $2.1 million or switch to a competing product. The IT Asset Manager is asked to contribute to the decision. Which ITAM data would be most relevant to this evaluation?

- A) The purchase date and depreciation schedule for the servers that run the productivity suite.
- B) Current license utilization rates, active user counts, feature adoption data, and the total cost of ownership including licensing, support, integration, and training costs.
- C) The names and job titles of all employees who have been assigned licenses.
- D) The version numbers of all software installed on workstations across the organization.

**Correct Answer:** B) Utilization rates, user counts, feature adoption, and total cost of ownership are the ITAM data points directly relevant to a renewal vs. replacement decision.

**Distractor Analysis:**

- *Why B is correct:* The renewal decision requires understanding actual value delivered versus cost. License utilization tells the decision maker whether all purchased seats are being used. Feature adoption data reveals whether users are using the advanced features that justify the enterprise tier. Total cost of ownership — licensing plus support costs, integration dependencies, and training investment — provides the true cost comparison against the competing product. This is ITAM's contribution to strategic procurement decisions.
- *Why A is incorrect:* Server depreciation schedules are hardware asset financial data. They are relevant to infrastructure planning but do not address the value or cost of a software licensing decision for a productivity suite.
- *Why C is incorrect:* A list of names and job titles assigned to licenses is operational directory data, not the financial and utilization analysis needed for a renewal decision. The relevant question is how many and how actively licenses are used, not who specifically holds them.
- *Why D is incorrect:* Version numbers across workstations are relevant to patch management and compliance baseline tracking, not to the business case for a software renewal decision at the enterprise agreement level.

---

### Question 15

During a CMDB reconciliation, an IT team discovers that a critical financial application has no documented dependencies in the CMDB — no relationships to the servers, databases, network segments, or authentication services it uses. An incident involving one of those servers is now in progress. What is the immediate consequence of the missing relationship data?

- A) The incident cannot be resolved until the CMDB is updated with the missing relationships.
- B) The incident management team cannot use the CMDB to determine which other services may be affected by the server incident, increasing the risk of missing related impact or notifying the wrong stakeholders.
- C) The CMDB must be frozen until all missing relationships are documented before any further changes are made.
- D) The financial application's SLA is automatically suspended because the CMDB is inaccurate.

**Correct Answer:** B) Missing relationship data prevents the incident team from using the CMDB for impact analysis, increasing risk of undetected collateral effects.

**Distractor Analysis:**

- *Why B is correct:* The primary value of CMDB relationship mapping is enabling impact analysis — understanding what depends on what. When a server hosting a financial application has no documented relationships, the incident team cannot use the CMDB to determine which other services may be affected, which stakeholders to notify, or which SLAs may be at risk. They must work from memory, direct inquiry, or trial and error — all slower and more error-prone than accurate CMDB-driven impact analysis.
- *Why A is incorrect:* Incidents are resolved by fixing the technical problem, not by updating the CMDB. CMDB updates are important for future accuracy but do not block incident resolution. The incident response team works the technical problem in parallel with (or prior to) any CMDB correction.
- *Why C is incorrect:* Freezing all changes until CMDB relationships are fully documented is impractical and potentially more harmful than the documentation gap itself — it could prevent necessary emergency fixes. CMDB improvement is an ongoing process, not a gate for all other operations.
- *Why D is incorrect:* SLA enforcement is governed by actual service performance against defined targets, not CMDB completeness. An SLA is not suspended because of internal documentation gaps. SLA management continues independently of CMDB accuracy issues.

---

### Question 16

A company purchases 300 device licenses for a security monitoring tool under a license model that allows installation on any device owned by the company. The IT Asset Manager discovers that 340 devices currently have the agent installed. What action best reflects mature SAM practice?

- A) Immediately remove the agent from 40 devices to return to compliance, selecting devices at random.
- B) Generate a report identifying which 40 over-licensed devices have the lowest security risk profile, then evaluate whether to purchase 40 additional licenses or remove the agent from the lowest-priority devices based on business risk.
- C) Do nothing — 40 devices over-licensed on a security tool creates no risk because security software is beneficial.
- D) Report the discrepancy to the vendor immediately to avoid audit penalties.

**Correct Answer:** B) Mature SAM practice combines compliance restoration with business risk evaluation — the most risk-informed remediation approach.

**Distractor Analysis:**

- *Why B is correct:* SAM is not purely a compliance function — it is a business value function. When over-licensing is discovered on a security tool, the remediation decision should be informed by business risk: which devices most need the monitoring agent, what is the cost of 40 additional licenses versus the security risk of removing coverage from 40 devices? A mature SAM function produces this analysis and presents options, rather than blindly removing installations or ignoring the gap.
- *Why A is incorrect:* Random removal of the agent from 40 devices may remove coverage from high-risk devices while retaining it on low-risk ones. Remediation decisions should be informed by risk analysis, not randomness.
- *Why C is incorrect:* Being over-licensed still constitutes a license agreement violation even for beneficial software. It also signals a breakdown in SAM controls — if over-licensing of a security tool goes unaddressed, the same gap exists for all software. Compliance is a minimum floor, not an optional goal.
- *Why D is incorrect:* Proactively reporting over-licensing to a vendor before an audit is not standard practice and may trigger an accelerated audit or invoice for back-license fees. The appropriate action is to assess and remediate internally. Self-disclosure of compliance gaps is a legal decision that requires counsel, not a standard SAM procedure.

---

### Question 17

A healthcare organization disposes of 100 retired servers that previously stored encrypted patient records. The encryption keys were held in a hardware security module (HSM) that has also been decommissioned and securely destroyed. The IT Asset Manager argues that because the data is encrypted and the keys are destroyed, additional data sanitization of the server storage media is unnecessary before physical disposal. Is this argument correct?

- A) Yes — destroying the encryption keys renders the encrypted data permanently unrecoverable, satisfying data sanitization requirements through cryptographic erasure.
- B) No — HIPAA requires physical destruction of all storage media regardless of encryption status.
- C) Yes — encryption satisfies all regulatory data protection requirements without any additional sanitization steps.
- D) No — encryption keys are never truly destroyed and the data remains at risk.

**Correct Answer:** A) Cryptographic erasure — destroying the encryption keys — renders encrypted data permanently unrecoverable and satisfies NIST SP 800-88 sanitization requirements for encrypted media.

**Distractor Analysis:**

- *Why A is correct:* NIST SP 800-88 explicitly recognizes cryptographic erasure as a valid sanitization method for encrypted media when the encryption was applied using a strong algorithm and the keys are demonstrably destroyed. If the data was encrypted at rest with a strong algorithm and the only copies of the keys have been destroyed (including backups), the ciphertext on the media is computationally unrecoverable. This satisfies the sanitization requirement without requiring physical destruction of 100 servers.
- *Why B is incorrect:* HIPAA does not mandate physical destruction for all media — it requires that ePHI be rendered unreadable, indecipherable, and unable to be reconstructed. NIST SP 800-88 cryptographic erasure satisfies this requirement. Physical destruction is one option, not the only option.
- *Why C is incorrect:* The argument is correct in this specific case, but the statement "encryption satisfies all regulatory requirements without additional sanitization" is too broad. Encryption alone — without key destruction — does not satisfy sanitization requirements. The key step is destroying the keys, not merely having encrypted the data.
- *Why D is incorrect:* Cryptographic keys can be destroyed — this is the explicit purpose of HSMs with secure key deletion functionality. When a properly designed HSM is decommissioned with secure key deletion, the keys it held are gone. Claiming keys are "never truly destroyed" is technically incorrect for modern cryptographic key management systems.

---

### Question 18

An organization's IT Asset Manager is asked to define the scope of assets that should be included in the CMDB versus those tracked only in a separate asset register. Which factor is most relevant to this scoping decision?

- A) The physical size of the asset — larger assets are harder to lose and do not need CMDB tracking.
- B) Whether the asset is relevant to service delivery impact analysis — assets whose failure or change would affect services should be in the CMDB; others may be tracked in simpler registers.
- C) The age of the asset — assets more than three years old should always be in the CMDB regardless of function.
- D) The manufacturer of the asset — branded equipment requires CMDB tracking while generic equipment does not.

**Correct Answer:** B) Service delivery relevance — whether the asset's failure or change affects services — is the primary criterion for CMDB inclusion.

**Distractor Analysis:**

- *Why B is correct:* The CMDB's core value is enabling service management decisions — impact analysis, incident diagnosis, change planning. Assets belong in the CMDB when their attributes and relationships are needed to support these decisions. A server that hosts a critical application, a network switch that connects a data center, a load balancer that directs customer traffic — these are CMDB-worthy because their relationships to services matter. A keyboard, a desk lamp, or a surge protector has no service delivery relationship and adds noise without value to the CMDB.
- *Why A is incorrect:* Physical size has no relevance to service delivery impact. A thumb drive containing encryption keys may be small but is critically important. A large industrial printer may be physically large but have no relationship to IT service delivery.
- *Why C is incorrect:* Asset age is a financial management consideration relevant to depreciation and replacement planning, not to service delivery relevance. A 5-year-old server that hosts a critical service is more CMDB-worthy than a brand-new keyboard.
- *Why D is incorrect:* Manufacturer branding is irrelevant to CMDB scoping. Generic network switches can be as service-critical as branded ones. The scoping decision is based on function and service relationship, not manufacturer.

---

### Question 19

Which of the following scenarios represents the most significant financial risk that Software Asset Management is designed to prevent?

- A) A company purchases 50 extra licenses for a product it already owns to have spares available.
- B) A company deploys software on 800 devices under a 500-device license, is audited by the vendor, and is required to pay back-license fees plus penalties for three years of unauthorized usage.
- C) A company renews a software subscription two weeks early, slightly overlapping with the previous contract period.
- D) A company's SAM database records a product version number incorrectly.

**Correct Answer:** B) Multi-year unauthorized deployment discovered during a vendor audit represents the most significant financial risk — back-license fees plus penalties can reach multiples of the original license cost.

**Distractor Analysis:**

- *Why B is correct:* Under-licensing at scale over multiple years represents the most significant financial risk in the SAM domain. Vendor audit rights typically cover 1–3 years. If 300 unauthorized deployments are identified across three years, the vendor can demand retroactive license fees for the entire unauthorized period plus contractual penalties. Total exposure can reach several times the cost of simply purchasing the licenses upfront. This is the primary risk SAM is designed to prevent through continuous entitlement-to-deployment reconciliation.
- *Why A is incorrect:* Purchasing extra licenses creates financial waste (over-licensing) but not legal risk. The organization is compliant — it owns more than it uses. While wasteful, this is a financial efficiency issue, not a compliance crisis.
- *Why C is incorrect:* A brief subscription overlap at renewal is a minor administrative inefficiency with negligible financial impact. It does not represent a compliance risk and is easily corrected at next renewal.
- *Why D is incorrect:* An incorrect version number in the SAM database is a data quality issue that may affect patch tracking and vulnerability management but does not create direct financial risk from license compliance perspective.

---

### Question 20

An organization is implementing a Hardware Asset Management program for the first time. The IT Director proposes assigning each physical asset a unique asset tag number and recording it in a spreadsheet. The IT Asset Manager recommends implementing a dedicated ITAM tool with CMDB integration instead. Which argument best supports the IT Asset Manager's recommendation?

- A) Spreadsheets are prohibited by ITIL 4 — all asset records must be in a dedicated tool.
- B) A dedicated ITAM tool with CMDB integration enables automated discovery reconciliation, relationship mapping to services, lifecycle tracking across the full asset lifecycle, and reporting capabilities that a manual spreadsheet cannot provide at scale.
- C) Asset tag numbers are only valid when generated by a dedicated ITAM tool — spreadsheet-assigned numbers are not recognized by auditors.
- D) A spreadsheet is appropriate for fewer than 100 assets, but the organization has 101 assets, so a dedicated tool is required.

**Correct Answer:** B) A dedicated ITAM tool with CMDB integration provides discovery reconciliation, relationship mapping, lifecycle tracking, and reporting that spreadsheets cannot replicate at scale.

**Distractor Analysis:**

- *Why B is correct:* Spreadsheets can track basic asset attributes but cannot reconcile data against automated discovery scans, cannot map asset relationships to services for impact analysis, and become unmanageable at scale. A dedicated ITAM tool integrates with discovery tools to automatically flag discrepancies, links assets to CI records for Change and Incident Management use, tracks lifecycle stages and depreciation, and generates compliance and financial reports. These capabilities collectively represent the practical difference between basic inventory management and mature ITAM.
- *Why A is incorrect:* ITIL 4 does not prohibit spreadsheets. For very small organizations with few assets and simple needs, a well-maintained spreadsheet can be sufficient. The argument against spreadsheets is practical capability, not ITIL 4 rule.
- *Why C is incorrect:* Asset tag numbers are organizational identifiers — the format and generation method are determined by the organization's own ITAM standards. Auditors review asset records and compliance evidence, not the system used to generate tag numbers.
- *Why D is incorrect:* There is no threshold number in ITIL 4 or standard ITAM practice that triggers a mandatory tool requirement. The decision is based on the capabilities needed, the scale of the asset base, and the complexity of relationships — not an arbitrary count threshold.

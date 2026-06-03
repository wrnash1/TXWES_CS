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

# Quiz: Module 15 - ERP Post-Implementation

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Why is post-implementation auditing critical for ERP deployments?

* A) To write code comments for all custom programs developed during the project
* B) To evaluate whether the system met the business objectives defined in the project charter and to address operational defects before they compound
* C) To configure DNS records for the new application server domain names
* D) To purge hard drive logs from the decommissioned legacy system

* **Correct Answer:** B) Post-implementation audits verify that the system delivered projected ROI, resolved the target business bottlenecks, and is being used correctly — catching problems before they become entrenched.
* **Distractor Analysis:**
  * *Why B is correct:* A formal post-implementation review (PIR) — typically conducted 3–6 months after go-live — compares actual system performance and user adoption against the objectives stated in the original business case, and documents lessons learned.
  * *Why A is incorrect:* Code commenting is a development quality practice performed during development, not a post-go-live audit activity.
  * *Why C is incorrect:* DNS configuration is an infrastructure task completed before go-live; it is not related to evaluating business value after deployment.
  * *Why D is incorrect:* Legacy system decommissioning is a data management task; purging old server logs does not constitute an ERP post-implementation audit.

---

### Question 2

Which of the following best describes **upgrading modules** in the context of on-premise SAP ERP post-implementation management?

* A) Importing new Salesforce Flow versions from a sandbox to production using a change set
* B) Applying vendor-delivered enhancement packages, support packages, and kernel patches to the on-premise SAP system, which requires a project-managed testing and cutover cycle
* C) Updating user training documentation to reflect interface changes from the most recent Salesforce seasonal release
* D) Re-running the initial data migration load to add records missed during the original go-live cutover

* **Correct Answer:** B) On-premise SAP module upgrades are significant projects — applying SAP Enhancement Packages or moving to S/4HANA requires regression testing, configuration adjustments, and a formal cutover, unlike the automatic SaaS release model.
* **Distractor Analysis:**
  * *Why B is correct:* An on-premise SAP upgrade (e.g., from ECC 6.0 EHP7 to EHP8, or a migration to S/4HANA) involves months of planning, transport management, regression testing in development and QA systems, and a production cutover weekend. It is a major project, not a routine maintenance task.
  * *Why A is incorrect:* Deploying Salesforce Flow changes via change sets is a configuration deployment activity for the SaaS platform, not an on-premise SAP module upgrade.
  * *Why C is incorrect:* Updating training documentation is a change management activity; it is not the same as a technical module upgrade to the ERP software version.
  * *Why D is incorrect:* Re-running data loads is a data quality remediation activity; it is not a software module upgrade.

---

### Question 3

Three months after an ERP go-live, the finance director reports that 40% of the accounts payable team is still manually entering invoice data into spreadsheets instead of using the new ERP system. What does this pattern most directly indicate?

* A) The ERP system has a technical defect in the accounts payable module that prevents invoice entry
* B) Low user adoption, most likely caused by insufficient training, change management, or usability issues that were not resolved before go-live
* C) The implementation team selected the wrong ERP vendor for the organization's needs
* D) The data migration was incomplete and the AP team cannot find vendor records in the new system

* **Correct Answer:** B) Manual workarounds three months after go-live are a classic indicator of low user adoption — employees defaulting to familiar tools because they were not adequately trained or motivated to use the new system.
* **Distractor Analysis:**
  * *Why B is correct:* User adoption tracking should detect this pattern early. The corrective actions include targeted re-training, floor support from super-users, management reinforcement, and possible usability improvements based on user feedback.
  * *Why A is incorrect:* If the AP module had a technical defect preventing invoice entry, the entire AP team would be unable to use it; 60% partial adoption suggests the system works but users are choosing not to use it.
  * *Why C is incorrect:* Vendor selection is a pre-implementation decision; by go-live, the question is about adoption and usage, not whether the right vendor was chosen.
  * *Why D is incorrect:* If vendor records were missing, users would encounter errors when trying to use the system — the symptom would be error messages, not voluntary bypass of the system entirely.

---

### Question 4

A Salesforce administrator receives a notification from Salesforce that the upcoming Winter release will deprecate a feature currently used in three active Flows. What is the correct post-implementation response?

* A) Ignore the notification because Salesforce handles all upgrade impacts automatically without administrator involvement
* B) Review the release notes, test the affected Flows in a sandbox against the new release, update the Flows to use the replacement feature, and deploy to production before the release date
* C) Submit a support ticket to Salesforce asking them to skip the Winter release for this org
* D) Delete the three affected Flows and rebuild them from scratch after the release is deployed

* **Correct Answer:** B) Proactive release management — reading release notes, testing in sandbox, remediating affected customizations, and deploying fixes before the production release — is the standard Salesforce administrator post-implementation practice.
* **Distractor Analysis:**
  * *Why B is correct:* This is the exact workflow Salesforce recommends: review release notes (published weeks before the release), test in sandbox (Salesforce updates sandboxes before production), fix issues, then deploy. Sandboxes exist precisely to enable this pre-release testing cycle.
  * *Why A is incorrect:* Salesforce does not automatically update customer Flows or custom configurations; deprecated features may simply stop working, and it is the administrator's responsibility to proactively remediate affected customizations.
  * *Why C is incorrect:* In Salesforce's SaaS multi-tenant model, individual customers cannot opt out of or defer platform releases; all customers receive the same update on the same schedule.
  * *Why D is incorrect:* Deleting and rebuilding Flows post-release is a reactive approach that causes downtime and user disruption; proactive testing and remediation before the release date is the correct practice.

---

### Question 5

Six months after go-live, a company's ERP system is running significantly slower than at launch. The Basis team reports that the primary FI document table has grown from 2 million to 18 million rows and nightly batch jobs are now taking 4 hours instead of 45 minutes. Which post-implementation action best addresses this?

* A) Purchase additional user licenses to distribute the transaction load across more users
* B) Implement data archiving to move closed historical FI documents to an archive store, rebuild table statistics, and review index health to restore query and batch performance
* C) Reinstall the ERP system from scratch and re-migrate all data to restore original performance levels
* D) Reduce the number of financial posting periods from 12 to 4 per year to limit document growth

* **Correct Answer:** B) Data archiving removes historical records from active tables (reducing scan time), refreshing database statistics and index health restores the query optimizer's accuracy, and together these actions address the performance degradation caused by table growth.
* **Distractor Analysis:**
  * *Why B is correct:* ERP database tables grow continuously with business transactions. SAP's data archiving objects (via transaction SARA) move completed documents to archive storage, keeping the active table small. Index maintenance and statistics updates are standard DBA tasks that restore performance after significant data growth.
  * *Why A is incorrect:* Adding user licenses increases the number of people who can log in; it does not reduce table size or improve query performance for batch jobs running in the background.
  * *Why C is incorrect:* Reinstalling and re-migrating is an extreme, high-risk, and time-consuming approach that would cause major business disruption; performance issues caused by data growth have targeted technical remedies.
  * *Why D is incorrect:* Reducing posting periods from 12 to 4 would fundamentally break the accounting model (companies need monthly financial statements) and would not reduce the number of existing rows in the table.

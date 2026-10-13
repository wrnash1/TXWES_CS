# Lab: Module 16 — ERP Certification Exam Preparation and Capstone

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Lab Overview

**Title:** 20 Practice Questions and Implementation Capstone Scenario

**Estimated Time:** 3–4 hours (this is the final, comprehensive lab)

**Format:** Individual work — multiple choice practice questions, written capstone analysis

**Submission:** Upload completed lab report (PDF or DOCX) to the LMS by the module due date.

**Weight:** This lab is worth 25% of the final course grade.

---

## Part 1: 20 Practice Certification Questions (40 points, 2 points each)

Answer each question. For questions you miss, write a one-sentence explanation of why the correct answer is right. This correction process is more valuable than the score itself.

---

**Question P1:** A Salesforce Administrator needs to ensure that sales reps can only see Opportunity records they own, while all sales managers can see all Opportunities in their region. What is the minimum set of configurations required?

A. Set Opportunity OWD to Public Read/Write; no other configuration needed.

B. Set Opportunity OWD to Private; configure the role hierarchy so managers are above reps.

C. Create a sharing rule granting managers access to all reps' Opportunities; OWD setting does not matter.

D. Set every rep's profile to "View All" for Opportunity.

**Correct Answer: B**

---

**Question P2:** Which Salesforce report format cannot be used as the source for a dashboard bar chart?

A. Summary

B. Matrix

C. Tabular

D. Joined

**Correct Answer: C**

---

**Question P3:** A company uses Salesforce for CRM and SAP for finance. When an Opportunity reaches "Closed Won," a financial record must be created in SAP within 10 minutes. The middleware platform is MuleSoft. What Salesforce mechanism triggers the process?

A. A scheduled Apex batch job that runs every 10 minutes

B. A Platform Event published by a record-triggered Flow when Stage = Closed Won

C. An IDoc sent from Salesforce directly to SAP

D. A Bulk API job that runs every 10 minutes

**Correct Answer: B**

---

**Question P4:** In SAP, a procurement analyst needs to receive goods into inventory against a purchase order. Which movement type is used?

A. 261

B. 311

C. 101

D. 501

**Correct Answer: C**

---

**Question P5:** A Salesforce user is getting an error when trying to view a Case record. The user has the Standard User profile. The Case object OWD is set to "Public Read Only." What is the most likely cause?

A. The user's profile does not have Read access to the Case object.

B. Public Read Only prevents standard users from viewing cases.

C. The Case OWD should be set to Private for users to see records.

D. The user is not in the correct role hierarchy.

**Correct Answer: A**

---

**Question P6:** What does SAP transaction PFCG do?

A. Displays the last failed authorization check for a user

B. Creates and maintains SAP roles and generates authorization profiles

C. Assigns roles to users in the user master record

D. Configures the Security Audit Log settings

**Correct Answer: B**

---

**Question P7:** A Salesforce Administrator wants to allow customer service reps to see all Account records (for context) but not edit them, while only allowing reps to edit Cases they own. What OWD settings achieve this?

A. Account OWD: Public Read Only; Case OWD: Private

B. Account OWD: Private; Case OWD: Public Read/Write

C. Account OWD: Public Read/Write; Case OWD: Private

D. Account OWD: Public Read Only; Case OWD: Public Read/Write

**Correct Answer: A**

---

**Question P8:** In SAP's ASAP methodology, the Go/No-Go decision occurs in which phase?

A. Phase 2 — Business Blueprint

B. Phase 3 — Realization

C. Phase 4 — Final Preparation

D. Phase 5 — Go-Live and Support

**Correct Answer: C**

---

**Question P9:** A Salesforce report includes a "Deal Size" column showing Small, Mid-Market, and Enterprise categories based on the Opportunity Amount. This column was created without adding a new custom field to the Opportunity object. What report feature was used?

A. Summary Formula

B. Cross-Object Filter

C. Bucket Field

D. Custom Report Type

**Correct Answer: C**

---

**Question P10:** What is the primary purpose of SAP BW/4HANA in the SAP landscape?

A. To process real-time financial transactions for SAP S/4HANA

B. To provide a data warehouse for analytical reporting separate from the transaction system

C. To manage SAP user authorizations and roles

D. To serve as the integration middleware between SAP and external systems

**Correct Answer: B**

---

**Question P11:** Salesforce Change Data Capture automatically publishes events for configured object types. A developer subscribed to the Contact CDC channel receives an event. Which field in the event payload would indicate whether the event was triggered by a record creation, update, delete, or undelete?

A. RecordId

B. ChangeType

C. EntityName

D. CreatedById

**Correct Answer: B**

---

**Question P12:** A company has 200 Salesforce users. 150 are standard sales reps and 50 are account managers who need two additional permissions beyond the standard rep capabilities. What is the most scalable approach?

A. Create 50 separate custom profiles — one for each account manager

B. Create one "Account Manager" permission set and assign it to the 50 account managers

C. Clone the Standard User profile 50 times with custom permissions

D. Assign the System Administrator profile to all 50 account managers

**Correct Answer: B**

---

**Question P13:** In SAP Financial Accounting, what is the "document principle"?

A. All financial documents must be stored as PDF attachments in the SAP system

B. Every financial transaction creates a balanced accounting document that cannot be changed after posting — only reversed

C. SAP requires paper documentation for all financial transactions above a threshold

D. Financial documents are numbered sequentially within a fiscal year and cannot have gaps

**Correct Answer: B**

---

**Question P14:** A Salesforce Administrator receives a request to give three specific users the ability to run a report that exports sensitive financial data. Most users should not have this capability. What is the best solution?

A. Change the OWD for the financial object to Private

B. Create a permission set with the appropriate reporting permission and assign it to the three users

C. Create a new profile for the three users

D. Enable Field History Tracking on the financial fields

**Correct Answer: B**

---

**Question P15:** An SAP implementation is six weeks from go-live. The business process owner for Finance has just requested that the chart of accounts be completely redesigned. The current chart of accounts was approved and signed off in the Business Blueprint four months ago. How should the project manager respond?

A. Immediately implement the redesign; Finance owns the process.

B. Route the request through formal change control; assess the schedule and budget impact; escalate to the steering committee.

C. Defer the request to a post-go-live Phase 2 project.

D. Implement the change in a development sandbox and keep it secret from the steering committee until after go-live.

**Correct Answer: B**

---

**Question P16:** What is the retention period for data in the Salesforce Setup Audit Trail without any additional products?

A. 30 days

B. 90 days

C. 180 days

D. 18 months

**Correct Answer: C**

---

**Question P17:** In SAP, a user attempts to post a vendor invoice and receives an authorization error. The SAP Basis administrator runs SU53 for that user. The SU53 output shows that authorization object F_BKPF_BUK is missing for activity 01 and company code 2000. What is the correct remediation?

A. Add the user to the accounting user group in SU01

B. Add authorization for F_BKPF_BUK with activity 01 and company code 2000 to the user's role in PFCG

C. Grant the user System Administrator access

D. Change the OWD setting for the financial document object

**Correct Answer: B**

---

**Question P18:** A Salesforce implementation project is using the ADKAR change management model. Post-go-live surveys show that users have high Awareness and high Desire but are still not using the system correctly. Which two remaining ADKAR stages should the project team focus on?

A. Desire and Reinforcement

B. Knowledge and Ability

C. Awareness and Reinforcement

D. Ability and Reinforcement

**Correct Answer: B**

---

**Question P19:** An enterprise wants to run a Salesforce CRM Analytics dashboard that combines Salesforce Opportunity data with SAP financial data. What does this require that native Salesforce reports cannot provide?

A. A Joined Report with five blocks

B. CRM Analytics with an external data connector ingesting SAP data into a dataset

C. A Custom Report Type joining Salesforce and SAP objects

D. A Platform Event published from SAP to Salesforce

**Correct Answer: B**

---

**Question P20:** A company processes 500,000 Account records to be loaded from a legacy system into Salesforce. The data was extracted as a CSV file. Which operation and API combination is most appropriate?

A. REST API with 500,000 individual PATCH requests

B. SOAP API with the update() method in a loop

C. Bulk API 2.0 with an Upsert job using an external ID field

D. Data Import Wizard with a 50,000-record CSV file uploaded ten times

**Correct Answer: C**

---

## Part 2: Capstone Implementation Scenario (60 points)

### Scenario Background

**Company:** Horizon Logistics Group

**Industry:** Third-party logistics (3PL) — warehousing, freight, and supply chain management

**Size:** 1,200 employees; $800M annual revenue; 14 distribution centers across the United States

**Systems:**

- SAP S/4HANA (on-premises, 3 years old) for: Finance (FI), Materials Management (MM), and Transportation Management
- Salesforce Sales Cloud (2 years old) for: account management, opportunity tracking, and customer contracts
- A legacy customer portal (15 years old) that customers use to track shipments and raise service requests
- A separate Business Intelligence tool (MicroStrategy) that pulls data from both SAP and a Salesforce export

**Business Challenges:**

1. Sales reps close contracts in Salesforce, but the contract terms (rate cards, service levels) must be manually re-entered into SAP — causing a 3-to-5-day delay before operational teams can begin onboarding new customers.

2. Customer service requests are being tracked in email — the legacy portal does not write structured ticket data anywhere. Customer satisfaction is declining.

3. The MicroStrategy dashboards are always two days behind because data extracts run nightly. Senior leadership wants real-time visibility into operational metrics.

4. A recent SOX audit identified two Salesforce users with the System Administrator profile who have been using it to approve their own purchase requisitions — entered manually in Salesforce and exported to SAP. This is a clear SoD violation.

5. Three new distribution centers are coming online in 18 months. The company wants to use the expansion to retire the legacy portal and launch a modern customer experience.

---

### Capstone Deliverables

Your submission must address all five sections. Each section should be 200–350 words. Use headings for each section. Support all recommendations with specific terminology from the course.

---

#### Section A: Integration Architecture (12 points)

Design the integration architecture to solve Challenge 1 (contract terms from Salesforce to SAP) and define how the legacy portal will be replaced for Challenge 5.

Your response must address:

- What Salesforce mechanism should trigger the integration when a contract is finalized (be specific about the technology)
- What SAP API or mechanism should receive the data (IDoc, BAPI, OData — choose and justify)
- Whether middleware (MuleSoft or equivalent) is needed and what role it plays
- How the legacy portal replacement should be architected — specifically, will Salesforce Service Cloud replace it? What integration will expose real-time shipment status from SAP to the customer portal?
- What the data mapping challenge is between Salesforce contract fields and SAP contract/customer master fields

---

#### Section B: Security and SoD Remediation (12 points)

Address Challenge 4 (the SAP and Salesforce SoD violations) and design the ongoing security model for both systems.

Your response must address:

- What immediate actions are required for the two users with System Administrator profiles who violated SoD
- What Salesforce access control mechanism should be used to prevent the recurrence (be specific about which profile or permission set configuration resolves the SoD conflict)
- What SAP tool should be implemented to continuously monitor for SoD conflicts across all 1,200 users
- What the principle of least privilege means for a 1,200-person logistics company, and how the access review process should be structured
- What audit trail evidence is available in both Salesforce and SAP to support the SOX audit response

---

#### Section C: Reporting and Business Intelligence (12 points)

Design the BI architecture to address Challenge 3 (real-time executive visibility) and identify what KPIs are most important for a 3PL company.

Your response must address:

- Whether the legacy MicroStrategy tool should be retained, replaced, or supplemented — and why
- What SAP BI tool should deliver real-time operational metrics from S/4HANA
- What Salesforce reporting tool should deliver sales and customer service metrics
- How senior leadership gets a unified view combining SAP and Salesforce data without logging into two systems
- Five specific KPIs that are critical for a 3PL company — at least one from Sales, one from Finance, and one from Operations — with target values and data sources defined

---

#### Section D: Implementation Methodology for the Three New Distribution Centers (12 points)

Design the implementation approach for Challenge 5 — the new portal, Salesforce Service Cloud for customer service, and the SAP expansion to the three new distribution centers.

Your response must address:

- Which implementation methodology — SAP Activate, Salesforce Agile lifecycle, or a hybrid — you recommend and why
- What the phasing strategy should be (can all three distribution centers go live simultaneously, or should they be phased?)
- What the key change management challenges are for the customer-facing portal replacement, and which ADKAR stages need the most focus
- What the cutover plan must address to ensure existing customers experience no disruption during the portal transition
- What hypercare staffing should look like for a customer-facing system go-live

---

#### Section E: Five-Year TCO Analysis (12 points)

Build a simplified TCO analysis for the customer portal replacement project, which includes: implementing Salesforce Service Cloud, retiring the legacy portal, and building the integration with SAP.

**Given assumptions:**

- Salesforce Service Cloud: $150/user/month for 60 customer service agents
- Implementation consulting (Service Cloud + Integration): $420,000 Year 1
- Internal IT staff for implementation: 30% of two IT staff at $90,000/year each
- Legacy portal decommission and migration: $65,000 one-time
- Annual Salesforce Service Cloud license escalation: 3% per year after Year 1
- Annual enhancement consulting: $50,000/year from Year 2 onward
- Current legacy portal maintenance cost: $85,000/year (this is the cost avoided)

**Build a five-year TCO table using these inputs.** Then answer:

1. What is the five-year total cost of the new solution?

2. What is the five-year cost avoided by decommissioning the legacy portal?

3. What is the net five-year investment?

4. What is one cost not included in this model that could significantly affect the ROI calculation?

5. If senior leadership requires ROI in under three years, does this project meet that threshold? Show your calculation.

---

## Submission Checklist

Before submitting, verify:

- Part 1: All 20 practice questions answered; incorrect answers include the one-sentence correction
- Part 2 Section A: Integration architecture recommendation — 200–350 words, all required points addressed
- Part 2 Section B: Security and SoD remediation — 200–350 words, all required points addressed
- Part 2 Section C: BI architecture recommendation — 200–350 words, all required points addressed
- Part 2 Section D: Implementation methodology — 200–350 words, all required points addressed
- Part 2 Section E: TCO table with all cells calculated; five analysis questions answered
- Document has your name, student ID, and date on the cover page
- Total submission is well-organized with clear headings

---

## Grading Rubric — Capstone

| Section | Points | Primary Criteria |
|---------|--------|------------------|
| Part 1 — 20 practice questions (2 pts each) | 40 | Correct answers; corrections for missed questions demonstrate understanding |
| Section A — Integration architecture | 12 | Correct technology choices (Platform Event, OData/BAPI, MuleSoft role); data mapping challenge addressed |
| Section B — Security and SoD | 12 | Immediate remediation steps; correct Salesforce access control mechanism; SAP GRC identified; audit trail evidence accurate |
| Section C — BI architecture | 12 | Appropriate tool for each data source; unified view strategy; five KPIs fully defined with targets and data sources |
| Section D — Implementation methodology | 12 | Justified methodology choice; phasing strategy logical; ADKAR application correct; cutover and hypercare addressed |
| Section E — TCO analysis | 12 | All calculations correct; net investment figure accurate; ROI threshold analysis shows work |
| **Total** | **100** | |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

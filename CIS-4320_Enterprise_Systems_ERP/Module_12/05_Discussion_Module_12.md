# Discussion Forum: Module 12 — Data Migration

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

---

## Overview

This forum applies Module 12 data migration concepts to realistic scenarios involving data quality failures, migration tool decisions, and the human cost of underestimating the Transform phase. Choose one scenario, write an original analytical post, and respond substantively to two classmates who chose different scenarios.

---

## Instructions

### Initial Post (Due Wednesday at 11:59 PM)

Choose **one** of the three scenarios below (A, B, or C). Write a response of **175–225 words** directly addressing the scenario questions. Begin your post by identifying your scenario choice.

Your post must:

- Reference at least one specific migration concept or tool from Module 12 (ETL, Extract, Transform, Load, data profiling, deduplication, External ID, upsert, Data Loader, Data Import Wizard, LSMW, Migration Cockpit, mock cutover, cutback plan) by name
- Name a specific data quality dimension from Module 12 (completeness, accuracy, consistency, uniqueness, timeliness, validity)
- Make a concrete recommendation or analysis grounded in the scenario details

### Peer Responses (Due Sunday at 11:59 PM)

Reply to at least **two classmates** who chose **different scenarios** from yours. Each reply must be at least 60 words and must do one of the following:

- Identify a downstream business process failure your classmate did not mention that would result from the data quality problem described
- Connect the migration failure to a specific ERP module impact (SAP FI, MM, SD, or Salesforce CRM) your classmate overlooked
- Describe how the migration approach your classmate recommended would perform differently if the dataset were 10 times larger

---

## Scenarios

### Scenario A: The Transform Phase Nobody Scheduled

A healthcare network is implementing Salesforce Sales Cloud. The project manager builds a 20-week implementation timeline. She allocates 2 weeks to Extract (pull data from the legacy CRM), 1 week to Transform (clean and format the data), and 1 week to Load (import into Salesforce). The remaining 16 weeks cover configuration, training, and testing.

When the migration team actually extracts the data, they discover the legacy CRM has been in use for 9 years with no data governance. The profiling analysis reveals: 22% of Account records missing Billing Address, 31% of Contact records with phone numbers in inconsistent formats, 14% of Accounts without an industry classification, and over 8,000 duplicate Account records. The data team estimates the cleansing work alone will take 6 weeks — four times the time allocated.

**Your task:** What data quality dimensions are violated by each finding in the profiling analysis? Why was the Transform phase so severely underestimated? What should the project team have done before building the timeline to produce a more accurate estimate of Transform duration? Reference the specific analysis technique that produces this information and explain what it produces.

### Scenario B: The External ID Oversight

A wholesale distribution company migrates their customer data from a legacy Oracle system into Salesforce. The migration team correctly loads 32,000 Account records and 98,000 Contact records — all successfully. No External ID field was added to the Account or Contact objects because the team decided they would not need to run incremental migrations.

Three weeks after go-live, the legacy Oracle system is not yet decommissioned because several AR reports still depend on it. The business decides they need to run a weekly sync of any Account records that were updated in Oracle during the parallel run period — approximately 4,000 records per week with address changes, phone updates, and status changes.

**Your task:** Explain why the absence of an External ID field creates a problem for this incremental update requirement. What is the risk if the team runs a new insert of the 4,000 changed records rather than an update? What is the correct process for adding External ID support after a migration has already been completed? What tool would you use for the weekly upsert, and why?

### Scenario C: The Saturday Night That Never Ended

A manufacturing company plans a 48-hour production cutover for their SAP S/4HANA go-live. The cutover begins Saturday at 8 PM and must be complete by Monday at 8 AM. The migration team has run two mock cutovers, each completing in 44 hours. The production cutover begins on schedule.

At hour 36 — Sunday at 8 AM — the automated reconciliation step reveals that 1,200 of the 24,000 vendor master records failed to load due to a missing mandatory field that was present in the test system but absent in 5% of production records. The migration team estimates it will take 3 hours to fix the records and 4 more hours to re-run the vendor master load and re-validate. That would put go-live at approximately hour 43 — 5 hours before the deadline.

However, the financial close team raises an objection: the 1,200 failed vendors include 3 of the company's top-10 suppliers by spend volume. If the system goes live with those vendors missing, the AP team cannot process their invoices.

**Your task:** Should the team proceed to go-live at hour 43, or fix the 1,200 records and delay go-live to hour 43? Apply the go/no-go decision framework from Module 12. What role does the cutback plan play in this decision? What should the team have done during mock cutovers to prevent this specific failure from reaching the production cutover?

---

## Discussion Rubric

| Criterion | Points | Description |
|---|---|---|
| Initial post submitted by Wednesday 11:59 PM | 1 | On-time submission |
| Scenario identified at start of post | 1 | Clearly states scenario letter at top of post |
| Specific migration concept or tool named and applied | 2 | Tool or concept name used accurately in context of scenario |
| Data quality dimension named correctly | 1 | Dimension name used and applied correctly to the scenario |
| Concrete recommendation or analysis | 1 | Specific and grounded — not generic migration advice |
| **Initial Post Subtotal** | **6** | |
| Peer response 1: 60+ words, substantive extension | 2 | Adds downstream impact, module consequence, or scale consideration classmate missed |
| Peer response 2: 60+ words, substantive extension | 2 | Same criteria |
| **Peer Response Subtotal** | **4** | |
| **Total** | **10** | |

---

## Professor Nash's Note

Scenario A happens on almost every ERP implementation I have ever observed. The project manager builds a timeline. The timeline has a box called "Data Migration." The box is too small. The reason it is too small is that no one ran a data profiling analysis before building the timeline. The team does not know how bad the source data is until they look at it — and they do not look at it until the migration sprint starts. Then they find 8,000 duplicates and a 22% address completion rate, and the 1-week Transform box becomes a 6-week emergency. Data profiling is not an optional step that you do if you have time. It is the step that tells you how much time everything else will take. Run it first. Budget the project from its results. That sequence — profile, then plan — is the difference between a migration that finishes on time and one that delays the go-live by six weeks.

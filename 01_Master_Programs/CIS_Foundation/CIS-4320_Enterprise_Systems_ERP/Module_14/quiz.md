# Quiz: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

This quiz contains 10 multiple-choice questions worth 10 points each. Select the single best answer. Distractor analysis is provided for instructor and student review.

---

## Question 1

A Salesforce Administrator needs to build a report showing total opportunity revenue grouped by sales rep and further sub-grouped by quarter. Which report format is most appropriate?

A. Tabular Report

B. Summary Report with one grouping level

C. Matrix Report with row grouping by rep and column grouping by quarter

D. Joined Report with two report blocks

**Correct Answer: C**

**Distractor Analysis:**

- **A — Tabular Report:** Tabular reports produce a flat list with no grouping or subtotals. They cannot group by two dimensions simultaneously, which is the requirement here.
- **B — Summary Report with one grouping level:** A summary report with a single grouping could show revenue by rep or by quarter, but not both simultaneously in a cross-tab format. You can add a second grouping in a summary report, but the result is nested rows — rep, then within each rep, quarters listed vertically. This is functional but less readable than a matrix for this use case.
- **C — Matrix Report (Correct):** A matrix report places one grouping on rows (reps) and another on columns (quarters), producing a cross-tab with cells showing the sum for each rep-quarter combination. This is the ideal format for comparing performance across two dimensions simultaneously.
- **D — Joined Report:** A joined report combines multiple report blocks from different report types. It is not designed for cross-tabulating two groupings within a single report type. Using a joined report here would be unnecessarily complex.

---

## Question 2

A Salesforce Administrator creates a dashboard with a "running user" set to a specific sales manager. What data will a sales rep see when they open this dashboard?

A. The sales rep sees only their own data, filtered to their record access.

B. The sales rep sees the data that the sales manager would see — based on the manager's record access.

C. The sales rep sees all data in the organization regardless of sharing settings.

D. The dashboard is not visible to the sales rep because only the running user can view it.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** A dynamic dashboard — where the running user is the "logged-in user" — shows each viewer their own data. But this dashboard has a specific static running user (the sales manager), not a dynamic setting. Static running user means all viewers see the same data.
- **B — Manager's data (Correct):** When a static running user is configured, every person who opens the dashboard — regardless of their own access level — sees the data that the running user would see. If the sales manager's role hierarchy gives them visibility into all team records, the sales rep viewing the dashboard also sees all team records. This is a security consideration: data governance policies must account for what the running user can see.
- **C:** Seeing all organization data would require the running user to have a profile with "View All" on every object, or System Administrator access. This is not implied by the scenario.
- **D:** Dashboard visibility is controlled by folder sharing, not by the running user setting. If the sales rep has access to the dashboard folder, they can view the dashboard.

---

## Question 3

Which Salesforce reporting feature allows an administrator to group opportunity amounts into "Small," "Mid-Market," and "Enterprise" categories in a report without creating a new custom field on the Opportunity object?

A. Summary Formula

B. Bucket Field

C. Cross-Object Filter

D. Custom Report Type

**Correct Answer: B**

**Distractor Analysis:**

- **A — Summary Formula:** A summary formula creates a calculated column based on other numeric fields in the report. It is used for calculations like margin percentage or year-over-year growth, not for categorizing text or numeric values into named groups.
- **B — Bucket Field (Correct):** Bucket fields allow report creators to define named categories and assign field values to those categories without modifying the data model. For Amount, you define rules such as "$0–$9,999 = Small." The bucket appears as a virtual column in the report. No custom field is needed on the object.
- **C — Cross-Object Filter:** Cross-object filters filter report records based on the presence or absence of related records (for example, "Accounts with no Opportunities"). They filter the report's row set — they do not create new categorization columns.
- **D — Custom Report Type:** A custom report type defines which objects and fields are available as data sources for building a report. It is an administrator-level configuration for report accessibility, not a tool for categorizing values within a report.

---

## Question 4

SAP BW/4HANA is described as a data warehouse separate from SAP S/4HANA. What is the primary architectural reason for this separation?

A. S/4HANA does not support OData APIs, so a separate system is needed for reporting.

B. BW/4HANA uses a different programming language (ABAP) than S/4HANA.

C. Running analytical queries against the live transaction database would degrade transaction performance; the warehouse provides an isolated, optimized environment for analysis.

D. BW/4HANA is required because S/4HANA stores data in a format that cannot be read by SQL.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** S/4HANA exposes extensive OData APIs and supports direct analytical reporting via Fiori tiles and CDS views. The separation from BW is not about API limitations.
- **B:** Both S/4HANA and BW/4HANA use ABAP as a development language. This is not the reason for the architectural separation.
- **C — Performance isolation (Correct):** Analytical queries — especially those scanning millions of records to produce trend reports and aggregations — consume significant database resources. Running them against the same database that handles real-time financial postings, order creation, and goods movements would cause transaction timeouts and performance degradation. A data warehouse provides an isolated, optimized environment where analytical workloads do not compete with operational workloads.
- **D:** S/4HANA uses the HANA in-memory database, which is fully SQL-accessible. Data format is not a barrier. The separation is about workload management and optimization, not data format incompatibility.

---

## Question 5

A marketing analyst in Salesforce wants to run a report showing Accounts that have no associated Opportunities created in the last 90 days — to identify dormant accounts for a re-engagement campaign. Which report filter type achieves this?

A. Standard filter with a date range on Close Date

B. Row-limit filter restricting results to 100 rows

C. Cross-object filter: Accounts WITHOUT Opportunities where Created Date >= 90 days ago

D. Bucket field categorizing accounts by last activity date

**Correct Answer: C**

**Distractor Analysis:**

- **A:** A date range filter on Close Date filters which Opportunity records are included — it does not remove from results the Accounts that have no Opportunities at all. It would also require an Opportunity to exist to have a Close Date to filter on.
- **B:** Row-limit filters restrict how many rows appear in the report — they do not filter records based on the presence or absence of related records.
- **C — Cross-object filter (Correct):** Cross-object filters allow filtering based on the existence (or absence) of related records and conditions on those related records. Setting a filter for "Accounts WITHOUT Opportunities (Created Date >= Last 90 Days)" returns exactly the dormant accounts the analyst needs. This is the purpose cross-object filters were designed for.
- **D:** A bucket field creates a categorized column in the report. It does not filter which records are included in the result set. Buckets are for grouping values within the results, not for including or excluding records.

---

## Question 6

SAP Analytics Cloud (SAC) differentiates itself from SAP Crystal Reports primarily because:

A. Crystal Reports requires a BW/4HANA data warehouse; SAC connects directly to S/4HANA.

B. SAC provides interactive, AI-assisted analytics and planning; Crystal Reports specializes in formatted, pixel-perfect document output.

C. SAC is an on-premises tool; Crystal Reports is cloud-native.

D. Crystal Reports supports live connections to S/4HANA; SAC requires data extraction to a flat file.

**Correct Answer: B**

**Distractor Analysis:**

- **A:** Both SAC and Crystal Reports can connect to BW/4HANA or S/4HANA data. The connection type is not the primary differentiator.
- **B — Interactive analytics vs. formatted output (Correct):** This is the core distinction. SAP Analytics Cloud is an interactive, exploratory, AI-powered platform for analytics, prediction, and planning — users slice data, apply filters, run what-if scenarios, and receive AI-generated insights. Crystal Reports specializes in high-fidelity document output — the exact fonts, margins, logos, and page breaks needed for invoices, financial statements, and regulatory reports. They serve fundamentally different use cases.
- **C:** This is backwards. SAP Analytics Cloud is cloud-native (SaaS). Crystal Reports is traditionally an on-premises or server-deployed product, though cloud versions exist.
- **D:** SAC supports live connections to SAP S/4HANA and BW/4HANA — it does not require flat file extraction for live reporting scenarios.

---

## Question 7

A company wants each individual sales rep to see their own performance metrics on a shared Salesforce dashboard, without creating separate dashboards for each rep. What type of dashboard and configuration achieves this?

A. A static dashboard with a running user set to the VP of Sales

B. A dynamic dashboard with "Run as logged-in user" selected

C. Separate summary reports emailed to each rep via scheduled report subscriptions

D. A matrix report shared in the Salesforce1 mobile app

**Correct Answer: B**

**Distractor Analysis:**

- **A — Static dashboard with VP running user:** All viewers would see the VP's data — the entire team's pipeline. Sales reps would see each other's records, which is the opposite of what is needed.
- **B — Dynamic dashboard (Correct):** A dynamic dashboard uses "Run as logged-in user," which means Salesforce renders the dashboard using the viewing user's own access permissions. Each sales rep sees their own pipeline, their own metrics. One dashboard configuration serves all reps without creating individual dashboards.
- **C — Scheduled report emails:** This would work functionally but requires separate scheduled reports per rep, is email-based rather than real-time, and does not provide an interactive dashboard experience. It is not the correct answer for the scenario described.
- **D — Matrix report in Salesforce1:** A matrix report is a report format, not a dashboard. Sharing a report does not give each viewer a personalized view of their data unless the report is filtered to show only records they own — but that would require the report itself to have a filter, not a report sharing setting.

---

## Question 8

A company's CFO reviews the executive dashboard and notices the "Days Sales Outstanding" (DSO) metric has increased from 32 days six months ago to 47 days today. What does this trend indicate?

A. The company is collecting payments faster than before.

B. The company's cost of goods sold has increased.

C. Customers are taking longer to pay invoices, which could indicate cash flow stress.

D. Sales volume has decreased, causing fewer invoices to be outstanding.

**Correct Answer: C**

**Distractor Analysis:**

- **A:** A decreasing DSO means faster collection. An increasing DSO — from 32 to 47 days — is the opposite: it means collection is taking longer, not faster.
- **B:** DSO measures accounts receivable collection time, not cost of goods sold. An increase in COGS would appear in gross margin metrics, not DSO.
- **C — Slower collection / cash flow concern (Correct):** DSO formula is (Accounts Receivable / Total Credit Sales) × days in period. An increasing DSO means the receivable balance is growing relative to sales — customers are taking longer to pay. This creates cash flow risk: the company has delivered goods and services but has not received payment, requiring it to fund operations out of its own cash reserves. Finance teams investigate increasing DSO to identify slow-paying customers, billing disputes, and collections process breakdowns.
- **D:** Lower sales volume would generally reduce both the numerator (receivables) and the denominator (sales) in the DSO formula. The net effect depends on the specific figures, but a simple volume decrease alone does not explain a systematic DSO increase. Slower collection is the standard interpretation.

---

## Question 9

In Salesforce, which permission is required to create a new dashboard in a public shared folder (not your private folder)?

A. "Create and Customize Reports"

B. "View Reports in Public Folders"

C. "Manage Dashboards in Public Folders"

D. "Modify All Data"

**Correct Answer: C**

**Distractor Analysis:**

- **A — Create and Customize Reports:** This permission allows users to build and modify reports in their private folder and in public folders they have access to. It is about reports, not dashboards. Having this permission does not grant dashboard creation rights.
- **B — View Reports in Public Folders:** This is a read-only permission for reports. It grants no creation or editing capability.
- **C — Manage Dashboards in Public Folders (Correct):** This permission allows users to create, edit, and delete dashboards in public shared folders. Without it, a user can only manage dashboards in their own private folder. For team-shared or company-wide dashboards, this permission is required.
- **D — Modify All Data:** This is a broad data permission that bypasses record-level sharing. It is not related to dashboard administration and would represent significant over-provisioning if granted just for dashboard creation purposes.

---

## Question 10

A Salesforce Administrator is asked to build a report that shows which Accounts have both open support Cases and active Opportunities simultaneously. Which Salesforce report format supports this requirement?

A. Summary Report with row groupings on Account

B. Matrix Report with Cases on rows and Opportunities on columns

C. Joined Report with two blocks — one for Accounts with Cases and one for Accounts with Opportunities

D. Tabular Report with a filter combining Cases and Opportunities

**Correct Answer: C**

**Distractor Analysis:**

- **A — Summary Report:** A summary report uses a single report type. "Accounts with Cases" is a different report type than "Accounts with Opportunities." A single summary report cannot source data from two different report types simultaneously.
- **B — Matrix Report:** Matrix reports use a single report type with two grouping dimensions. They cannot combine two different report types, so they cannot combine Case data with Opportunity data in the way described.
- **C — Joined Report (Correct):** A joined report is specifically designed to combine data from multiple report types in a single view. Creating one block with the "Accounts with Cases" report type and a second block with the "Accounts with Opportunities" report type, joined on the Account, provides exactly the side-by-side view requested.
- **D — Tabular Report:** Tabular reports, like summary and matrix reports, use a single report type. You cannot filter a tabular report to show combined Case and Opportunity data from two different object hierarchies. A filter combining Cases and Opportunities within a single report type is not possible in standard Salesforce reporting without a custom report type that joins those objects.

---

## Quiz Summary

| Question | Topic | Correct Answer |
|----------|-------|----------------|
| 1 | Matrix report for two-dimensional grouping | C |
| 2 | Static running user shows manager's data to all viewers | B |
| 3 | Bucket field for in-report categorization | B |
| 4 | BW/4HANA separation for performance isolation | C |
| 5 | Cross-object filter for absent related records | C |
| 6 | SAC interactive analytics vs. Crystal Reports formatted output | B |
| 7 | Dynamic dashboard for per-user data | B |
| 8 | Rising DSO indicates slower collections | C |
| 9 | "Manage Dashboards in Public Folders" permission | C |
| 10 | Joined report for combining two report types | C |

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

# Quiz: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. Questions are drawn from the video lecture, reading guide, and lab activity for Module 14.

---

## Questions

### Question 1

A sales manager needs a report that shows total opportunity revenue grouped by sales rep, with each rep's totals broken out by product family across the columns. Which Salesforce report type should be used?

A) Tabular

B) Summary

C) Matrix

D) Joined

**Correct Answer:** C

### Distractor Analysis

- **A — Tabular** is incorrect. Tabular reports display flat lists with no grouping. They cannot produce row-and-column group summaries.
- **B — Summary** is incorrect. Summary reports support row groupings and subtotals but only one axis of grouping — they cannot simultaneously group rows by sales rep and columns by product family.
- **C — Matrix** is correct. Matrix reports support two-dimensional groupings: one dimension in rows (sales rep) and one in columns (product family), with summarized values in each cell. This is the defining use case for the matrix format.
- **D — Joined** is incorrect. Joined reports combine multiple report blocks for side-by-side comparison, not two-dimensional grouping of a single dataset.

---

### Question 2

A Salesforce dashboard was refreshed at 8:00 AM. A deal worth $250,000 closed at 10:00 AM and the opportunity was updated in Salesforce. A VP views the dashboard at 11:00 AM and the pipeline total has not changed. What is the most likely explanation?

A) The VP does not have permission to view the closed opportunity.

B) The dashboard shows data as of its last refresh and has not been refreshed since 8:00 AM.

C) The Opportunity record is missing a required field and was not saved correctly.

D) Salesforce dashboards only update once per day at midnight.

**Correct Answer:** B

### Distractor Analysis

- **A — Permission** is incorrect. If the VP lacked permission, the dashboard would show an error or blank component, not a stale number.
- **B — Refresh timing** is correct. Salesforce dashboards display data as of the last refresh. A deal that closed after the last refresh will not appear until the dashboard is refreshed again.
- **C — Missing required field** is incorrect. A record missing a required field cannot be saved in the first place; it would not produce a stale total.
- **D — Midnight refresh** is incorrect. Dashboard refresh schedules are configurable; there is no system-imposed midnight-only rule.

---

### Question 3

Which statement about Salesforce dynamic dashboards is correct?

A) Dynamic dashboards can have unlimited components because they use Einstein Analytics.

B) Dynamic dashboards display data based on the permissions of the dashboard creator.

C) Dynamic dashboards show each viewer data based on their own access level rather than a single running user.

D) Dynamic dashboards require a custom report type and cannot use standard report types.

**Correct Answer:** C

### Distractor Analysis

- **A — Unlimited components** is incorrect. Component limits apply to all dashboard types regardless of Einstein Analytics.
- **B — Creator's permissions** is incorrect. That describes a standard (non-dynamic) dashboard. Dynamic dashboards show data from each viewer's own perspective.
- **C — Viewer's own access** is correct. The defining characteristic of a dynamic dashboard is that it runs as "the logged-in user," so each viewer sees data scoped to their own access rights.
- **D — Custom report type required** is incorrect. Dynamic dashboards work with any report type, standard or custom.

---

### Question 4

Einstein Analytics datasets differ from Salesforce native report data in which of the following ways?

A) Datasets are stored inside standard Salesforce objects alongside CRM records.

B) Datasets are extracted from Salesforce objects and external sources into a separate analytical engine, enabling higher row volumes and richer visualizations.

C) Datasets are only available to System Administrators and cannot be shared with standard users.

D) Datasets automatically refresh every minute and always reflect live data.

**Correct Answer:** B

### Distractor Analysis

- **A — Inside standard objects** is incorrect. Datasets are stored in Einstein Analytics's own data store, separate from the Salesforce object model.
- **B — Separate analytical engine** is correct. Einstein Analytics extracts data via dataflows into its own engine, enabling much larger datasets and more sophisticated analytics than native reports allow.
- **C — Admins only** is incorrect. Einstein Analytics dashboards and lenses can be shared with any licensed user.
- **D — Minute-by-minute refresh** is incorrect. Dataset refreshes are scheduled (typically daily or hourly); they do not provide real-time live data by default.

---

### Question 5

In SAP BW, what is the role of an InfoCube?

A) A real-time connection between S/4HANA and SAP Analytics Cloud

B) A star-schema fact table optimized for multidimensional analytical reporting

C) A configuration object that defines user authorizations for BW queries

D) A staging table that holds granular transactional data before aggregation

**Correct Answer:** B

### Distractor Analysis

- **A — Real-time connection** is incorrect. Real-time connectivity is handled by live data connections in SAP Analytics Cloud, not InfoCubes.
- **B — Star-schema fact table** is correct. An InfoCube is structured as a star schema with a fact table surrounded by dimension tables, optimized for multidimensional OLAP queries.
- **C — Authorization object** is incorrect. SAP BW authorizations are defined via analysis authorizations, not InfoCubes.
- **D — Staging table** is incorrect. That describes a DataStore Object (DSO). InfoCubes store aggregated data for reporting, not granular staging data.

---

### Question 6

A finance team has been using a report showing "Total Invoices Processed This Month" as a key metric. According to the KPI design criteria in the reading, what is this metric most likely missing that prevents it from qualifying as a true KPI?

A) A measurable formula

B) A defined target or threshold and strategic alignment to a business objective

C) An assigned report type in Salesforce

D) An Einstein Analytics dataset

**Correct Answer:** B

### Distractor Analysis

- **A — Measurable formula** is incorrect. "Total Invoices Processed" has a clear formula (count of invoices with posting date in current month). Measurability is not the missing element.
- **B — Target/threshold and strategic alignment** is correct. Without a defined target (e.g., 500 invoices/month) and a connection to a business goal (e.g., operational efficiency), the number has no actionable meaning. A metric becomes a KPI only when targets, ownership, and strategic alignment are defined.
- **C — Report type** is incorrect. Whether the metric is surfaced in a tabular or summary report is irrelevant to its KPI status.
- **D — Einstein Analytics dataset** is incorrect. KPI design is a business concept, not a tool requirement.

---

### Question 7

SAP Analytics Cloud (SAC) differs from BEx Analyzer in which of the following ways?

A) BEx Analyzer is a cloud-native platform; SAC is a legacy Excel-based tool.

B) SAC is a cloud SaaS platform combining BI, planning, and predictive analytics; BEx Analyzer is an Excel-based query tool for SAP BW.

C) SAC can only connect to external databases and cannot access S/4HANA directly.

D) BEx Analyzer includes built-in machine learning models; SAC does not.

**Correct Answer:** B

### Distractor Analysis

- **A — Reversed descriptions** is incorrect. This inverts the two tools. BEx Analyzer is the legacy Excel add-in; SAC is the modern cloud platform.
- **B — Correct distinction** is correct. SAC is SAP's cloud-native SaaS BI platform that unifies reporting, planning, and predictive analytics. BEx Analyzer is the established Excel-based query tool for SAP BW, a legacy on-premises tool.
- **C — SAC cannot connect to S/4HANA** is incorrect. SAC supports live connections directly to S/4HANA and BW.
- **D — BEx Analyzer has ML** is incorrect. Machine learning and predictive analytics are features of SAC and Einstein Analytics, not BEx Analyzer.

---

### Question 8

Which executive dashboard design principle is violated when a dashboard shows 35 individual numeric values with no charts, no color thresholds, and no trend indicators?

A) The drill-down principle

B) The data freshness principle

C) The cognitive load and at-a-glance status principles

D) The running user principle

**Correct Answer:** C

### Distractor Analysis

- **A — Drill-down** is incorrect. A dashboard with 35 numbers may or may not support drill-down; drill-down is a separate principle about navigation depth.
- **B — Data freshness** is incorrect. The freshness principle concerns timestamp disclosure, not the number of metrics or visual design.
- **C — Cognitive load and at-a-glance status** is correct. Showing 35 numbers with no visual encoding violates the "minimize cognitive load" principle (limit to 5–7 top-level KPIs) and the "show status at a glance" principle (use color coding and visual indicators so status is understood in seconds).
- **D — Running user** is incorrect. Running user is a Salesforce-specific dashboard setting, not an executive dashboard design principle.

---

### Question 9

A Salesforce report shows 0 records for "Accounts with no open Opportunities," but the sales team says they know of at least 20 accounts with no activity. What Salesforce report feature should be used to correctly build this report?

A) A matrix report with a column grouping on Opportunity Stage

B) A joined report with two blocks: one for accounts and one for opportunities

C) A summary report with conditional highlighting

D) A tabular report with a cross-filter excluding accounts that have active opportunities

**Correct Answer:** D

### Distractor Analysis

- **A — Matrix report** is incorrect. A matrix report groups existing data; it cannot filter for the absence of related records.
- **B — Joined report** is incorrect. A joined report shows two datasets side by side but does not inherently filter for records with no related objects.
- **C — Conditional highlighting** is incorrect. Conditional highlighting formats cell colors based on values; it cannot filter for missing relationships.
- **D — Cross-filter** is correct. A cross-filter specifically filters parent records based on the presence or absence of child records. "Accounts without Opportunities" is the classic cross-filter use case.

---

### Question 10

Which of the following best describes the relationship between data quality and ERP reporting?

A) Data quality only affects reports built on custom objects; standard object reports are always accurate.

B) Poor data quality in source records produces inaccurate report totals and KPIs, which can lead to flawed business decisions regardless of how well the reports are designed.

C) ERP systems automatically correct data quality issues before reports are generated.

D) Data quality is the responsibility of the IT department only and does not affect how analysts build reports.

**Correct Answer:** B

### Distractor Analysis

- **A — Standard objects are always accurate** is incorrect. Data quality problems affect all object types equally. Standard object records are entered by users and are just as susceptible to errors and omissions.
- **B — Poor data produces inaccurate reports** is correct. This captures the core principle: no matter how well-designed a report or dashboard is, it will produce misleading outputs if the underlying data is incomplete, inaccurate, or stale.
- **C — ERP corrects data automatically** is incorrect. ERP systems can enforce validation rules and required fields, but they cannot infer correct values for missing or wrong entries.
- **D — IT responsibility only** is incorrect. Data quality is a shared responsibility involving data entry users, business process owners, data stewards, and administrators.

---

*End of Quiz — Module 14*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

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

---

### Question 11

(5 points)

A Salesforce administrator builds a report showing Opportunity win rate (Won Opportunities / Total Closed Opportunities) and wants to display it as a gauge chart on a dashboard. The VP asks why the gauge is not moving despite new deals closing. What is the most likely cause?

- A) Gauge charts cannot display calculated percentages — only raw record counts
- B) The dashboard has not been refreshed since the new deals were closed — the gauge still shows data from the last refresh
- C) The Opportunity OWD is set to Private, blocking the dashboard from reading the VP's deals
- D) Gauge charts require Einstein Analytics datasets and cannot use native Salesforce reports

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Salesforce dashboards display data as of their last refresh. A deal that closed after the most recent dashboard refresh will not appear in any dashboard component — including gauge charts — until the dashboard is refreshed again. This is one of the most frequently misunderstood behaviors in Salesforce dashboards.
  - *Why A is incorrect:* Gauge charts can display both counts and percentages, including metrics derived from formula fields in summary reports. The chart type is not the limitation.
  - *Why C is incorrect:* OWD settings affect record-level visibility for users. The dashboard runs as a specific running user (or the logged-in user for dynamic dashboards). If the running user can see the deals, they appear in the report and dashboard regardless of OWD. The symptom described is stale data, not missing records.
  - *Why D is incorrect:* Gauge charts work with native Salesforce reports. Einstein Analytics is required only for more complex analytics scenarios — not for a simple win rate gauge.

---

### Question 12

(5 points)

A Salesforce report builder creates a summary report grouped by Account Industry, with a formula field calculating average deal size (Total Amount / Record Count). The report shows 0.00 for all industry groups. What is the most likely cause?

- A) Summary reports cannot display formula fields — a matrix report is required for calculated metrics
- B) The Amount field has no values — most Opportunity records have a blank or zero Amount, making the average calculate to zero
- C) The formula field was added to the report header rather than the grouping summary row
- D) Salesforce does not allow division operations in report formula fields

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* If most or all Opportunity records have a blank or zero Amount field, the sum is zero and the average calculates to zero. This is a data quality problem — required fields left empty or defaulted to zero — not a report configuration error. The first diagnostic step should always be to inspect the underlying records for the data quality issue.
  - *Why A is incorrect:* Summary reports fully support formula fields. Formula fields can be added to summary report grouping rows and perform calculations including division. Matrix reports are not required.
  - *Why C is incorrect:* Formula fields in summary reports are added to the field list and display at the record level or at summary rows depending on configuration. Placement at the header vs. grouping row would affect where the value appears, not whether it calculates to zero.
  - *Why D is incorrect:* Salesforce report formula fields support all standard arithmetic operations including division. There is no restriction on division in report formulas (though division by zero returns null, not zero).

---

### Question 13

(5 points)

In SAP S/4HANA, CDS (Core Data Services) Views enable embedded analytics directly within the operational system. What is the key advantage of using a CDS View for reporting compared to extracting data to SAP BW?

- A) CDS Views require no user authorization configuration while BW queries require complex analysis authorizations
- B) CDS Views provide access to live, real-time operational data from S/4HANA without the latency of ETL extraction and BW data loading — reports show current transactional data rather than a snapshot loaded at a scheduled time
- C) CDS Views can display historical data going back 10 years while BW has a 3-year data retention limit
- D) CDS Views automatically apply machine learning predictions to each data row while BW only shows historical data

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The defining advantage of CDS-based embedded analytics in S/4HANA is real-time data access. Because CDS Views query directly against the S/4HANA database (on HANA's in-memory engine), reports show the current state of operational data. BW requires data to be extracted, transformed, and loaded — introducing latency that can range from hours to one day depending on the extraction schedule.
  - *Why A is incorrect:* CDS Views absolutely require authorization configuration — they use the standard SAP authorization framework. Simplifying authorization is not a CDS advantage over BW.
  - *Why C is incorrect:* Data retention limits in BW are configurable by the customer. There is no standard 3-year BW retention limit. BW is specifically designed for long-term historical data storage — often many years.
  - *Why D is incorrect:* Machine learning and predictive analytics in SAP are delivered through SAP Analytics Cloud (SAC) with Smart Predict, not through the CDS layer itself. CDS Views are data access objects, not ML execution engines.

---

### Question 14

(5 points)

A controller wants to design a financial dashboard with the following KPIs: Current Ratio, Days Sales Outstanding (DSO), Gross Margin %, and EBITDA. The controller's analyst says two of these are lagging indicators and two are leading indicators. Which classification is correct?

- A) Current Ratio and DSO are leading indicators; Gross Margin % and EBITDA are lagging indicators
- B) All four are lagging indicators because they are all calculated from historical financial data
- C) EBITDA and Gross Margin % are lagging indicators (measuring past profitability outcomes); Current Ratio and DSO are more operational and forward-looking, making them closer to leading indicators
- D) EBITDA is the only lagging indicator; all others are leading indicators

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* EBITDA (earnings before interest, taxes, depreciation, amortization) and Gross Margin % measure the outcome of past revenue and cost decisions — classic lagging indicators. Current Ratio (current assets / current liabilities) reflects liquidity available for near-term obligations and DSO (how quickly customers are paying) predicts future cash flow timing — they are more operational and forward-looking, classifying them as closer to leading indicators in the financial context.
  - *Why A is incorrect:* This reverses the correct classification. EBITDA and Gross Margin % are classic income statement outcome metrics — they summarize what already happened, making them lagging. Current Ratio and DSO are balance sheet and operational metrics that signal what is likely to happen to cash flow.
  - *Why B is incorrect:* While all four metrics use historical data in their calculation, the distinction between leading and lagging is about whether the metric predicts future outcomes (leading) or summarizes past ones (lagging). DSO specifically predicts when cash will arrive — it is directionally forward-looking even though it uses past invoice dates.
  - *Why D is incorrect:* Classifying only EBITDA as lagging while calling all others leading is too narrow. Gross Margin % is equally a lagging profitability metric — it measures the outcome of pricing and cost of goods decisions that have already occurred.

---

### Question 15

(5 points)

A Salesforce administrator needs to create a report that shows Accounts alongside their most recent Case subject line and the total number of open Cases. Which Salesforce report feature or type enables combining data from two different report types (Accounts and Cases) in a single report view?

- A) Summary report with a cross-filter on Cases
- B) Matrix report with Account as the row grouping and Case Status as the column grouping
- C) Joined report with one block for Accounts and a second block for Cases, linked on the Account ID
- D) Einstein Analytics lens with a SAQL query joining the Account and Case datasets

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Joined reports are specifically designed to display data from multiple report types side-by-side in a single report. The administrator creates one block from the Accounts report type and a second block from the Cases report type, both filtered and linked by Account. This enables displaying account-level information alongside case-level information in one view.
  - *Why A is incorrect:* A cross-filter can identify Accounts with or without Cases (filtering based on presence/absence of related records), but it cannot display the Case subject line or case count alongside the Account — it is a filter mechanism, not a display mechanism.
  - *Why B is incorrect:* A matrix report groups data from a single report type on two axes. It cannot combine data from the Accounts report type and the Cases report type — matrix reports work within one report type.
  - *Why D is incorrect:* While SAQL in Einstein Analytics can join datasets, this is a technically advanced solution requiring a separate tool. The question describes a standard Salesforce reporting scenario that can be addressed with native report features without requiring Einstein Analytics.

---

### Question 16

(5 points)

A company's SAP BW data warehouse is refreshed nightly from S/4HANA. An operations manager reviews a BW query each morning and makes production scheduling decisions based on inventory levels shown. What is the critical limitation the manager must understand, and what would be the alternative if real-time inventory data were required?

- A) The limitation is that BW queries can only show financial data — inventory levels require a separate ERP module; the alternative is to use SAP PP transaction MD04
- B) The limitation is that the BW data reflects inventory as of the prior night's load — any goods movements after that time are not visible; the alternative is to use a CDS View or direct S/4HANA transaction (e.g., MMBE) for real-time inventory
- C) The limitation is that BW queries require an SAP Analytics Cloud license to view — the free alternative is transaction SE16N
- D) There is no limitation — BW refreshes in real time as each goods movement posts in S/4HANA

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Because BW is loaded via nightly ETL extraction from S/4HANA, BW data is always at least several hours stale. For production scheduling decisions that depend on current inventory (e.g., whether material received this morning is available), the manager must use a real-time S/4HANA transaction like MMBE (Stock Overview) or a CDS-based embedded analytics app rather than the BW query.
  - *Why A is incorrect:* BW absolutely can store and report inventory levels — MM (Materials Management) data including stock quantities and movements is a standard BW extraction subject area. The limitation is not object coverage but data latency.
  - *Why C is incorrect:* BW queries are accessed via BEx Analyzer or SAP Analytics Cloud, but the limitation is data latency, not licensing. SE16N is a table browser for database-level data inspection — it is not an analytics alternative.
  - *Why D is incorrect:* Standard SAP BW uses extraction-based (ETL) loading with scheduled refresh windows. It does not continuously replicate transactions in real time. SAP HANA-based real-time replication (using SLT or similar) is a separate configuration that must be explicitly implemented.

---

### Question 17

(5 points)

A Salesforce dashboard component is configured to run as the "dashboard viewer" (dynamic). A junior sales rep opens the dashboard and sees only their own 12 opportunities. Their manager opens the same dashboard and sees 89 opportunities across their entire team. Which Salesforce capability produces this behavior?

- A) Conditional highlighting — values above a threshold are hidden from junior users
- B) Dynamic dashboard running-user configuration combined with the Role Hierarchy — each user sees data within their own access scope, which is determined by their role's record visibility
- C) Permission Sets — the junior rep's Permission Set restricts their dashboard view to 12 records maximum
- D) Einstein Analytics row-level security applied to the dashboard dataset

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Dynamic dashboards run as the "logged-in user" rather than a fixed running user. When the junior rep opens the dashboard, the underlying reports run with the rep's access credentials — they can only see records within their access scope (their own records under Private OWD). When the manager opens the same dashboard, it runs with the manager's credentials, and the Role Hierarchy grants the manager visibility into all subordinate records — producing 89 opportunities.
  - *Why A is incorrect:* Conditional highlighting applies color formatting to numeric values based on thresholds. It has no ability to hide records or filter which records appear in the report. It is a visual formatting feature, not a security or access control.
  - *Why C is incorrect:* Permission Sets control which objects and fields a user can access — they do not set record count limits. There is no Salesforce feature that restricts a user to seeing a maximum number of records.
  - *Why D is incorrect:* Einstein Analytics row-level security is a feature of the Einstein Analytics platform. This scenario describes behavior in a standard Salesforce native dashboard, not an Einstein Analytics dashboard. The behavior results from dynamic dashboard configuration and the standard Salesforce security model.

---

### Question 18

(5 points)

A financial analyst exports a Salesforce report to Excel to create a management presentation. The analyst's manager points out that the Excel file shows revenue data that is three days old. What is the structural problem with this reporting workflow, and how should it be redesigned?

- A) Excel cannot open Salesforce CSV exports — the analyst should use Data Loader instead
- B) Exporting to Excel creates a static snapshot that goes stale immediately — the analyst should use a live Salesforce dashboard or embedded report in Salesforce that automatically reflects current data, or schedule the report to refresh and email on a defined cadence
- C) The three-day lag is caused by BW replication latency — the analyst should connect Excel to SAP directly
- D) Salesforce reports only update on the first of each month — the export must be timed accordingly

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Exporting to Excel is one of the most common anti-patterns in ERP reporting. The moment the file is saved, it is a static snapshot — it never updates. If the management presentation is delivered three days after export, all the numbers are three days stale. The correct redesign is to use a live Salesforce dashboard or schedule automated report delivery, ensuring the data is current at the time of review.
  - *Why A is incorrect:* Excel can open Salesforce CSV exports. Data Loader is a bulk data operation tool, not a reporting export tool. The problem is not file format incompatibility.
  - *Why C is incorrect:* This scenario is entirely within Salesforce — there is no BW or SAP component. The lag is from static Excel export, not from a data warehouse replication schedule.
  - *Why D is incorrect:* Salesforce reports reflect current object data (subject to dashboard refresh timing for dashboard components). There is no system rule that Salesforce reports only update on the first of the month.

---

### Question 19

(5 points)

A company wants to implement a sales performance scorecard that includes both Salesforce CRM data (pipeline, win rate) and SAP FI data (actual invoiced revenue, days outstanding). Which integration architecture enables combining these two data sources into a single reporting view?

- A) Export both datasets to separate Excel files and compare them side by side
- B) Use Salesforce native reports, which automatically connect to SAP FI without any configuration
- C) Use SAP Analytics Cloud (SAC) with live connections or data imports from both Salesforce (via an API connector) and SAP S/4HANA — SAC serves as the unified reporting layer across both systems
- D) Copy all SAP FI data into Salesforce custom objects, then report on the custom objects using Salesforce reports

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* SAP Analytics Cloud supports connections to both SAP S/4HANA (live connection or data import) and external systems including Salesforce via API connectors. It is specifically designed to be the unified enterprise analytics layer that combines data from multiple source systems into a single reporting environment — exactly the scenario described.
  - *Why A is incorrect:* Exporting to separate Excel files requires manual work for every reporting cycle, creates static snapshots, and produces a fragmented view requiring manual reconciliation. This is the anti-pattern that enterprise BI platforms are designed to replace.
  - *Why B is incorrect:* Salesforce native reports query only Salesforce objects. They have no native connectivity to SAP FI. Cross-system reporting requires an integration layer or a common analytical platform.
  - *Why D is incorrect:* Copying SAP FI data into Salesforce custom objects creates a data duplication problem: two authoritative sources, synchronization latency, data governance challenges, and additional storage costs. It is a technically possible but architecturally poor approach.

---

### Question 20

(5 points)

A Salesforce administrator creates a report using a custom report type. The manager complains that the report is not showing accounts that have no cases at all. The report only shows accounts that have at least one case. How should the custom report type be reconfigured to include accounts with no related cases?

- A) Change the report type from Summary to Tabular — tabular reports show all records
- B) In the custom report type definition, change the Accounts-to-Cases relationship from "Each 'A' record must have at least one related 'B' record" to "Each 'A' record may or may not have related 'B' records"
- C) Add a cross-filter to the report: "Accounts without Cases"
- D) Set the Opportunity OWD to Public Read Only to expose all account records

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Custom Report Types define the primary object and related objects. When the relationship is set to "must have at least one related record," only parent records with matching child records appear in reports using that type — accounts with no cases are excluded. Changing the relationship to "may or may not have related records" creates a left-outer-join behavior that includes all accounts regardless of whether they have cases. This is a configuration setting in the custom report type definition itself.
  - *Why A is incorrect:* Changing the report format (Summary to Tabular) does not change what records are included in the report. The inclusion logic is determined by the report type's relationship definition, not the display format.
  - *Why C is incorrect:* A cross-filter is applied to a report to filter based on the presence or absence of child records — but it requires the report type to already include accounts with no cases. If the report type excludes them at the definition level, a cross-filter applied to the report cannot add them back.
  - *Why D is incorrect:* OWD settings control which records a user can see from a security perspective. They have no bearing on the join logic of a custom report type. Setting Opportunity OWD to Public Read Only is unrelated to whether accounts without cases appear in a report.

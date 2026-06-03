# Reading Guide: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

Module 14 addresses the reporting and analytics capabilities of both Salesforce and SAP S/4HANA. Reporting is among the most heavily tested topics on the Salesforce Administrator exam. This guide also develops the analytical vocabulary you will need when designing dashboards and recommending BI tools in professional settings. Allocate approximately 90 minutes for this guide.

---

## Section 1: The Business Case for ERP Reporting

### From Transactions to Intelligence

Every time a business transaction occurs in an ERP system — a sale is made, an invoice is paid, a shipment is delivered — that transaction leaves a digital record. Over months and years, those records accumulate into one of the most comprehensive data assets a company possesses.

The transformation from raw transaction data to actionable business intelligence occurs through reporting. Well-designed reporting answers questions at every level of the organization. An operations manager asks: are all orders on track for delivery this week? A regional sales director asks: which of my reps are on track for quota this quarter, and which need coaching? A CFO asks: how does this quarter's margin compare to our projection, and what is driving the variance?

ERP systems without effective reporting are accounting for the past but not illuminating the future. BI turns historical data into decisions.

### The Reporting Maturity Model

Organizations typically evolve through reporting maturity levels. Understanding where a client is on this scale helps you recommend the right next step.

**Level 1 — Reactive Reporting:** reports are run on demand when a problem is discovered or a question is asked. No dashboards; no scheduled reports. Analysts pull data manually.

**Level 2 — Scheduled Reporting:** standardized reports run on a schedule (daily, weekly, monthly) and are distributed by email. Consistent but not real-time; not interactive.

**Level 3 — Self-Service Reporting:** business users can build their own reports using a tool like Salesforce Report Builder without IT involvement. Empowers the business but introduces governance challenges (inconsistent metric definitions, report sprawl).

**Level 4 — Predictive and Prescriptive Analytics:** AI and machine learning identify patterns, predict outcomes, and recommend actions. Einstein Discovery, SAP Analytics Cloud's predictive models, and similar tools operate at this level.

Most organizations are between Level 2 and Level 3. The goal of a well-implemented Salesforce or SAP environment is to enable Level 3 for business users while providing Level 4 capabilities for strategic decisions.

---

## Section 2: Salesforce Native Reporting

### Report Formats in Depth

The four Salesforce report formats serve distinct analytical purposes. Selecting the wrong format produces a technically valid report that does not answer the intended question.

**Tabular Reports** produce a row-by-row listing with column headers. They support sorting and basic filtering but no grouping or subtotals. The primary use case is creating a flat list for export or for use as a dashboard component showing a record count or a list. Tabular reports cannot be used as the source for a bar chart component on a dashboard because there is no grouping structure to chart.

**Summary Reports** add one or more row groupings. Each grouping level can show a subtotal. Summary reports can be charted directly — a bar chart showing opportunity value grouped by stage is a classic example. Summary reports support up to three grouping levels.

**Matrix Reports** add column groupings in addition to row groupings, producing a cross-tabulation. For example, opportunity count by sales rep (rows) and by quarter (columns) creates a matrix that shows performance patterns across two dimensions simultaneously. Matrix reports are more complex to build but provide more analytical insight.

**Joined Reports** are unique in that they can contain up to five report blocks, each drawing from a different report type. The blocks are joined on a common value — typically a related account or opportunity. Joined reports can answer complex questions such as "Show me accounts with open cases alongside their open opportunities." They require the "Create and Customize Reports" permission and are rarely built by end users — they are typically maintained by administrators or power users.

### Custom Report Types

A Custom Report Type (CRT) defines the object relationships and fields available when building a report. CRTs are created by administrators and define:

- The primary object (for example, Account)
- Related objects to include (for example, Contacts and Opportunities)
- Whether records are included only if related records exist (inner join) or regardless of related records (outer join)
- Which fields from each object are exposed in the report builder

CRTs allow administrators to expose exactly the data users need while hiding irrelevant fields. They are the correct solution when users need report data from multiple related objects that standard report types do not cover.

### Bucket Fields, Formulas, and Filters

**Bucket fields** categorize existing field values into named buckets without changing the underlying data. They work on numeric fields (grouping amounts into Small/Medium/Large), text fields (grouping industry values into custom categories), and picklist fields. Buckets appear in the report as new virtual columns.

**Summary formula fields** calculate custom values using other fields in the report. For example, a summary formula could calculate gross margin as (Amount - Cost) / Amount and display it as a percentage column.

**Report Filters** narrow the dataset. Three types of filters exist:

- Standard filters (date ranges, field conditions)
- Cross-object filters (include or exclude records based on related object criteria, such as "Accounts without Cases in the last 30 days")
- Row-limit filters on tabular reports that limit the number of rows displayed

### Dashboard Architecture

Dashboards in Salesforce are containers for up to 20 visual components (in Enterprise Edition), each sourced from a report. Dashboard components are refreshed either on demand, on a schedule, or when the dashboard is opened.

Dashboard folders control who can view and edit dashboards. The administrator manages folder sharing to ensure that sensitive dashboards (such as executive compensation reports) are visible only to authorized viewers.

The **Running User** is the most important security concept in Salesforce dashboards. A static running user means the dashboard shows data as if that specific person were running the reports — regardless of who is actually viewing the dashboard. This is appropriate for a shared "company snapshot" dashboard where all viewers should see the same overall numbers.

A **Dynamic Dashboard** uses the viewer's identity as the running user. Each person who opens the dashboard sees their own data. This is appropriate for rep-level performance dashboards — each sales rep sees their own pipeline, and the same dashboard configuration serves all reps.

**Dashboard subscriptions** deliver an email with a screenshot of the dashboard on a configured schedule (daily, weekly, monthly). Useful for executives who want a morning briefing without logging in.

---

## Section 3: CRM Analytics and Einstein Analytics

### Architecture of CRM Analytics

CRM Analytics (CRMA) operates on a separate analytical data store called the **Analytics Data Store**, sometimes referred to as the Analytics platform. Data is ingested from Salesforce objects via dataflows or recipes and stored in optimized datasets. External data from CSV files or connected sources can also be ingested.

The separation of the analytical store from the transactional database is the key architectural advantage. Analytical queries run against the separate store without impacting Salesforce transaction performance.

**Dataflows** are JSON-based configurations that define how data is extracted from Salesforce objects, transformed, and loaded into datasets. **Recipes** are a newer, more user-friendly alternative with a visual interface for data preparation.

### CRMA Lenses and Stories

A **Lens** is an interactive exploration of a single dataset. In a lens, business analysts slice and dice data in real time — applying filters, changing chart types, grouping by different dimensions — to explore patterns without modifying any underlying data.

An **Einstein Discovery Story** takes a dataset and automatically analyzes it to identify key drivers of a selected metric. The system presents natural-language explanations such as "Deals with more than two stakeholders involved are 22% more likely to close" — surfacing insights that a human analyst might take days to find.

---

## Section 4: SAP Business Intelligence Architecture

### The SAP BI Stack

SAP's BI architecture has three tiers that correspond to the data flow from operational systems to analytical presentation.

**Tier 1 — Source Systems:** SAP S/4HANA and other SAP and non-SAP systems generate transactional data. CDS views in S/4HANA can directly expose data for real-time operational analytics via SAP Fiori tiles, bypassing the warehouse entirely for simple use cases.

**Tier 2 — Data Warehouse:** SAP BW/4HANA stores and harmonizes data from multiple source systems. Data is modeled into subject-area DataStore Objects (Advanced DSOs in BW/4HANA). The HANA in-memory database enables complex analytical queries in seconds.

**Tier 3 — Presentation Layer:** SAP Analytics Cloud (SAC) or Crystal Reports consumes data from BW/4HANA and presents it to end users as interactive stories, dashboards, or formatted reports.

### BW/4HANA Data Modeling

BW/4HANA's primary data modeling object is the **Advanced DataStore Object (aDSO)**. An aDSO holds three internal tables:

- The **Inbound Table** stores data as it arrives from extractors, before processing.
- The **Activation Queue** holds data after validation, before it is committed to the main table.
- The **Active Data Table** holds the current state of the data, ready for reporting.

aDSOs can be configured for different scenarios: standard (delta updates), direct update (used for write-optimized staging), and planning (used as a target for planning data).

**Composite Providers** (CompositeProviders) join multiple aDSOs into a unified reporting view, enabling queries that span multiple subject areas without pre-joining the data in a single large object.

### SAP Analytics Cloud Capabilities

SAP Analytics Cloud delivers three integrated capabilities in one platform.

**Business Intelligence:** interactive dashboards called "Stories" with drag-and-drop design, live connections to SAP S/4HANA and BW/4HANA, and drill-down capabilities.

**Augmented Analytics:** built-in Smart Insights explains what is driving a KPI change. Smart Predict builds predictive models using machine learning without requiring a data science background.

**Planning:** SAC supports integrated business planning — financial planning, workforce planning, and supply chain planning — with write-back capability to the underlying data sources.

### Crystal Reports Use Cases

Crystal Reports remains the standard for high-fidelity formatted output — documents that must look exactly right for printing, emailing to customers, or submitting to regulators. Typical use cases include:

- Customer invoices and statements
- Purchase order confirmation documents
- Financial statements with precise layout requirements
- Regulatory compliance reports with mandatory format specifications

Crystal Reports is increasingly maintained rather than expanded — new BI development uses SAC or third-party tools. However, in any established SAP environment, you will find dozens of Crystal Reports still in active use.

---

## Section 5: KPI Design and Executive Dashboard Principles

### The Anatomy of a Well-Defined KPI

A metric becomes a KPI when it has all of the following components:

**A clear definition:** What exactly is being measured? Is "revenue" net or gross? Is it recognized or booked?

**A measurable numerator and denominator:** Revenue this quarter / quota this quarter = pipeline attainment percentage.

**A target:** What is the desired value? Below what value is performance concerning?

**A time horizon:** Daily, weekly, monthly, quarterly, annual?

**An owner:** Who is responsible for moving this metric?

**A data source:** Where does the underlying data come from, and how fresh is it?

Without all six components, a "KPI" is just a number on a screen.

### KPI Categories by Business Function

**Sales KPIs:**

- Quota Attainment: closed revenue / assigned quota × 100%
- Pipeline Coverage Ratio: total pipeline value / remaining quota (target: 3x–5x)
- Average Deal Size: closed revenue / number of deals closed
- Win Rate: closed won deals / total deals closed (won + lost)
- Sales Cycle Length: average days from opportunity created to closed won

**Financial KPIs:**

- Days Sales Outstanding (DSO): (accounts receivable / total credit sales) × days in period
- Current Ratio: current assets / current liabilities (target: above 2.0)
- Gross Margin %: (revenue - cost of goods sold) / revenue × 100%
- Operating Cash Flow: net income + non-cash charges + changes in working capital

**Operations KPIs:**

- On-Time Delivery Rate: deliveries on time / total deliveries × 100%
- Inventory Turnover: cost of goods sold / average inventory value
- Order Fulfillment Cycle Time: average days from order receipt to delivery

### Principles of Effective Executive Dashboards

**Limit the number of metrics.** Research on cognitive load suggests that humans can comfortably process five to nine chunks of information simultaneously. An executive dashboard with twenty metrics is unlikely to drive focused action. Choose the five to seven metrics that most directly indicate whether the business is on track against its most important objectives.

**Design for the decision, not the data.** Every metric on an executive dashboard should have a clear answer to the question: if this metric is red, what decision does the executive need to make? Metrics that do not trigger decisions are interesting but not executive-grade.

**Always show trend.** A single data point is less informative than a trend. DSO of 45 days — is that good or bad? 45 days and declining for three months is good news. 45 days and increasing from 32 days two months ago is a warning signal. Always provide trend context.

**Align on definitions.** The most trust-destroying dashboard problem is when the dashboard number does not match what the operations team says. This almost always means two different sources are using different definitions. Before launching a dashboard, require written agreement on metric definitions from all stakeholders.

**Provide drill-down, not drill-to.** Executives want to click on a number and see the contributing details — not be redirected to a separate report that takes 30 seconds to load. Fast, contextual drill-down keeps executives engaged.

---

## Section 6: Certification Focus Areas

### Salesforce Administrator Exam

Report and dashboard topics represent 13–14% of the Salesforce Admin exam. Key areas:

- Differences between the four report formats and when to use each
- What custom report types are and why they are created
- What bucket fields do and how they differ from formula fields
- Running user behavior in static vs. dynamic dashboards
- Dashboard folder permissions
- Report schedule and subscription functionality

### SAP S/4HANA Essentials Exam

SAP BI topics to review:

- The role of BW/4HANA as a data warehouse separate from the transaction system
- What SAP Analytics Cloud is and its three capability pillars (BI, Analytics, Planning)
- The purpose of Crystal Reports and when it is used
- The concept of extractors for moving data from S/4HANA to BW
- Understanding that S/4HANA Fiori tiles can display live analytics without BW for operational use cases

---

## Key Terms for Module 14

**Tabular Report:** flat list report format in Salesforce with no grouping or subtotals.

**Summary Report:** Salesforce report format with row groupings and subtotals.

**Matrix Report:** Salesforce cross-tab report with row and column groupings.

**Joined Report:** Salesforce report combining up to five report blocks from different report types.

**Custom Report Type (CRT):** administrator-defined data source for reports, controlling which objects and fields are available.

**Bucket Field:** a virtual field grouping raw values into named categories for report analysis.

**Running User:** the user whose data access determines what a Salesforce dashboard displays.

**Dynamic Dashboard:** a Salesforce dashboard where the running user is the viewer, showing each person their own data.

**CRM Analytics:** Salesforce's advanced analytics platform with its own data store.

**Einstein Discovery:** AI-powered analysis and prediction within CRM Analytics.

**SAP BW/4HANA:** SAP's enterprise data warehouse platform built on HANA in-memory technology.

**SAP Analytics Cloud (SAC):** SAP's cloud-native platform unifying BI, planning, and predictive analytics.

**Crystal Reports:** SAP's pixel-perfect formatted report tool.

**DataStore Object (aDSO):** primary data modeling object in BW/4HANA.

**Extractor:** SAP program that reads data from S/4HANA and delivers it to BW.

**KPI (Key Performance Indicator):** a measurable value with a target, time horizon, and owner that indicates progress toward a business objective.

**DSO (Days Sales Outstanding):** average days to collect payment after invoicing.

---

## Study Questions

1. A sales manager wants a report showing the total opportunity value for each sales rep broken down by quarter. Which Salesforce report format is most appropriate, and why?

2. Explain the difference between a Custom Report Type and a standard report type. Give an example of a scenario where a Custom Report Type is necessary.

3. What is the "running user" on a Salesforce dashboard, and how does it behave differently between a static and a dynamic dashboard?

4. Describe the use case where CRM Analytics (Einstein Analytics) would be a better tool than native Salesforce reports.

5. In the SAP BI stack, what is the role of BW/4HANA and how is data moved from SAP S/4HANA into it?

6. What distinguishes SAP Analytics Cloud from SAP Crystal Reports? When would you use each?

7. Define Days Sales Outstanding (DSO) and explain why it is considered a critical financial KPI. What does a rising DSO indicate?

8. Describe the six components that must be present for a metric to qualify as a well-defined KPI.

9. An executive asks why the revenue number on the Salesforce dashboard does not match the revenue figure the finance team reports. What are three possible causes of this discrepancy?

10. Explain the principle "design for the decision, not the data" as applied to executive dashboard design. Give a concrete example.

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

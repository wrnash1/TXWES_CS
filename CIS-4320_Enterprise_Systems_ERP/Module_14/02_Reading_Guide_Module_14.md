# Reading Guide: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Overview

This reading guide supports Module 14, which covers the reporting and analytics capabilities of enterprise ERP systems. You will explore Salesforce's native reporting tools, Einstein Analytics, SAP Business Warehouse and SAP Analytics Cloud, KPI framework design, executive dashboard principles, and the critical role of data quality in producing reliable business intelligence.

**Estimated Reading Time:** 90–110 minutes

---

## Learning Objectives

By the end of this module, you will be able to:

1. Distinguish between OLTP and OLAP processing and explain why each approach suits different use cases.
2. Identify the four Salesforce report types and select the appropriate type for a given business scenario.
3. Describe the architecture of Salesforce dashboards, including components, refresh behavior, and dynamic dashboards.
4. Explain the role of Einstein Analytics (Tableau CRM) in the Salesforce analytics ecosystem.
5. Describe the SAP BW architecture including InfoProviders, BEx tools, and SAP Analytics Cloud.
6. Define KPI criteria and apply them to evaluate ERP metric designs.
7. Apply executive dashboard design principles to critique and improve a sample dashboard.
8. Articulate the relationship between data quality and reporting accuracy.

---

## Section 1 — OLTP vs. OLAP: Why Architecture Matters

### 1.1 Transaction Processing vs. Analytical Processing

ERP systems are built primarily as OLTP — Online Transaction Processing — systems. OLTP databases are optimized for:

- High concurrency (thousands of simultaneous users)
- Fast individual record inserts and updates
- Normalized data structures that reduce redundancy and maintain referential integrity
- Short, predictable transactions with ACID guarantees (Atomicity, Consistency, Isolation, Durability)

Reporting and analytics require OLAP — Online Analytical Processing — which is optimized for:

- Large-volume sequential reads across millions of rows
- Aggregations (sums, counts, averages, percentages) across multiple dimensions
- Denormalized or star-schema data structures that allow efficient joins
- Longer-running queries that may take seconds or minutes

Running heavy analytical queries against an OLTP database can degrade transaction performance for all users. This is why organizations developed dedicated data warehouse architectures.

### 1.2 SAP HANA's In-Memory Column Store

SAP HANA addresses the OLTP/OLAP tension through a columnar in-memory database design. Traditional row-store databases store all fields of a single record together. Columnar databases store each field across all records together. For aggregations — sum all revenues, count all open orders — the columnar layout reads only the relevant column, ignoring fields not needed in the query. This makes analytical queries dramatically faster without a separate data warehouse extraction.

S/4HANA's Universal Journal (table ACDOCA) stores all financial line items in a single column-store table. A query for total revenue by profit center that would have required joining dozens of tables in R/3 runs in seconds in S/4HANA.

### 1.3 Salesforce Cloud Reporting Architecture

Salesforce native reports run directly against the Salesforce operational database. Salesforce manages its infrastructure at scale so that reporting queries do not visibly degrade transaction performance for most customers. Row limits exist — standard reports return up to 2,000 rows; report exports can return up to 100,000 rows — to prevent unbounded queries from affecting shared infrastructure.

Einstein Analytics (Tableau CRM) operates differently. Data is extracted from Salesforce objects and external sources into datasets stored in Einstein's separate analytical engine. Queries run against these datasets, not the live Salesforce database. This removes the row limit constraint and enables more complex analytical computations.

---

## Section 2 — Salesforce Reports

### 2.1 Report Types

Salesforce report types define the data model available to a report — which objects and fields you can include. Standard report types come pre-configured (Accounts, Opportunities, Cases). Custom report types extend these by adding related objects up to four levels deep.

The four report formats are distinct from the report type:

**Tabular:** Rows and columns, no grouping. Fastest to build. Cannot be used as a dashboard source unless configured with a row limit (for a metric count) or converted to a summary.

**Summary:** Rows grouped by one or more field values, with subtotals and grand totals. The standard format for operational dashboards. Supports charts.

**Matrix:** Both row-level and column-level groupings, creating a grid of summarized data. Analogous to a spreadsheet pivot table. Powerful for time-series and multi-dimensional analysis.

**Joined:** Multiple report blocks displayed together. Each block can use a different report type. Blocks can share filters. Useful for side-by-side comparisons that cannot be expressed in a single-block report.

### 2.2 Filters and Conditional Highlighting

All report types support filters. Standard filters include: Show Me (My Records vs. All Records), Date field and range, and custom field filters. Cross-filters are a powerful advanced feature — they filter based on the presence or absence of related records. "Accounts without open Opportunities" requires a cross-filter: include Accounts where Opportunities do not exist.

Conditional highlighting (also called color coding or heatmaps in some contexts) applies color formatting to summary or matrix report cells based on numeric thresholds. A revenue-by-region matrix can show cells green above target, yellow within 10% of target, and red below. This is configured in the report's Display options.

### 2.3 Report Charts

Summary and matrix reports can include an embedded chart. Chart types available: bar, column, line, pie, donut, funnel, scatter, combination. Charts display in the report view and can be added to dashboards as components.

### 2.4 Subscriptions

Users can subscribe to a report and receive email delivery of the results on a defined schedule. The subscription delivers up to 2,000 rows. Subscription conditions can be set — only deliver if a threshold is met (e.g., only email me if pipeline dropped below $1M).

---

## Section 3 — Salesforce Dashboards

### 3.1 Dashboard Components

A Salesforce dashboard consists of up to 20 components arranged on a grid canvas. Each component is powered by one source report. Component types:

- **Chart** — bar, column, line, pie, donut, funnel, scatter
- **Gauge** — shows a value against a min/max range with color zones
- **Metric** — displays a single number prominently (e.g., total open pipeline)
- **Table** — shows grouped data from a summary report in tabular form
- **Visualforce** — embeds custom Visualforce page content (advanced)
- **Lightning Web Component** — embeds custom LWC content (advanced)

### 3.2 Refresh Behavior

Dashboards do not display live data. They display data as of the last refresh. Refresh occurs when:

- A user manually clicks the Refresh button
- A scheduled refresh fires (daily or hourly based on edition)
- The dashboard is viewed and the data is stale beyond a configured threshold

This is a common exam topic. If a dashboard shows incorrect data, the first troubleshooting step is to check when it was last refreshed and whether the source report data has changed since then.

### 3.3 Dynamic Dashboards

Standard dashboards run as a single "running user" — the data reflects that user's access. A Sales Director's pipeline dashboard that runs as the director shows the director's team's data to all viewers.

Dynamic dashboards run as "the logged-in user." Every viewer sees the data they themselves have access to. One dashboard serves all roles — reps see their own pipeline, managers see their team, VP sees all. Dynamic dashboards require a feature license and have limits on the number per org.

### 3.4 Dashboard Folders and Sharing

Dashboards live in folders, and folder visibility controls access. Folder types:

- My Personal Custom Dashboards — visible only to you
- Private folders — visible to specific users, roles, or groups
- Public folders — visible to all users or subsets by role

The folder a dashboard lives in determines who can see it. The running user setting determines whose data is shown.

---

## Section 4 — Einstein Analytics

### 4.1 Architecture Overview

Einstein Analytics (also marketed as Tableau CRM) is a separate analytical platform layered on top of Salesforce. Its core components are:

- **Datasets** — curated data tables extracted from Salesforce objects and/or uploaded from external sources
- **Dataflows** — scheduled processes that extract, transform, and load data into datasets
- **Lenses** — single exploratory visualizations built against a dataset
- **Dashboards** — collections of visualizations and interactive controls assembled from lenses
- **Stories (Einstein Discovery)** — automated statistical analyses that explain outcomes and surface predictions

### 4.2 Lenses and Exploration

A lens is the building block of Einstein Analytics exploration. You select a dataset, choose a measure (a numeric field to aggregate), and a dimension (a field to group by). Visualizations are interactive — click a segment to drill down, drag to filter, toggle measure calculations between sum/count/average.

### 4.3 Einstein Discovery

Einstein Discovery scans your datasets and builds statistical models that answer three questions:

1. What happened? (descriptive statistics)
2. Why did it happen? (factor analysis — which variables correlate with the outcome)
3. What will happen? (predictive scoring on new records)

Discovery stories can be embedded directly in Salesforce record pages, surfacing predictions (e.g., likelihood to close, churn risk score) on individual Account or Opportunity records.

### 4.4 Licensing and Exam Considerations

Einstein Analytics is a paid add-on license, not included in standard Salesforce editions. For the Salesforce Administrator exam, key points include: datasets are separate from reports and require dataflow configuration; Einstein Analytics dashboards cannot be used as components in standard Salesforce dashboards (and vice versa); and dataset row limits are significantly higher than native report limits.

---

## Section 5 — SAP Business Intelligence

### 5.1 SAP BW Architecture

SAP Business Warehouse is a dedicated data warehouse application built on top of the SAP HANA or AnyDB database. The data model in BW organizes data into InfoProviders:

- **InfoObjects** — metadata elements: characteristics (dimensions like product, customer, time) and key figures (numeric measures like revenue, quantity)
- **DataStore Objects (DSOs)** — staging tables that hold granular transactional data at the detail level before aggregation
- **InfoCubes** — star-schema fact tables optimized for multidimensional analysis; used as the primary reporting layer
- **CompositeProviders** — virtual objects that combine data from multiple InfoProviders without physical storage

Data flows from S/4HANA (source) → Extraction → DataStore Object → InfoCube → Query (via BEx Query Designer).

### 5.2 BEx Query Designer

BEx Query Designer is the tool used to define analytical queries against BW InfoProviders. A query consists of:

- **Rows** — characteristics placed in rows define the row headers of the output
- **Columns** — key figures or characteristics placed in columns define the column headers
- **Free Characteristics** — available for interactive filtering but not displayed by default
- **Filters** — fixed values that restrict the query's scope
- **Calculated Key Figures** — formulas built from existing key figures (e.g., profit margin = revenue minus cost, divided by revenue)

Queries are executed via BEx Analyzer (Excel add-in) or BEx Web Analyzer (browser-based).

### 5.3 SAP Lumira

SAP Lumira is a self-service data visualization tool that can connect to BW queries, SAP HANA views, and external data sources. Lumira provides chart types and storytelling features similar to Tableau or Power BI. There are two versions: Lumira Discovery (desktop self-service) and Lumira Designer (developer tool for building guided analytical applications).

### 5.4 SAP Analytics Cloud

SAP Analytics Cloud (SAC) is the strategic SaaS BI platform for SAP. It unifies three capabilities:

- **Business Intelligence** — reports and dashboards built against live S/4HANA or BW data connections or imported datasets
- **Planning** — collaborative financial and operational planning with direct writeback to S/4HANA
- **Predictive Analytics** — machine learning models trained on SAP data, similar to Einstein Discovery for Salesforce

SAC uses live data connections (real-time query to S/4HANA or BW) or import connections (data extracted into SAC's own in-memory store). For S/4HANA customers, live connections to CDS views deliver real-time operational analytics without BW extraction.

### 5.5 Embedded Analytics in S/4HANA Fiori

S/4HANA ships with hundreds of Fiori analytical apps. These apps are built on SAP HANA CDS (Core Data Services) views and run analytical queries directly against the S/4HANA database. Examples:

- Accounts Receivable: Overdue Receivables, DSO Trend
- Inventory: Inventory Turnover, Slow-Moving Stock
- Procurement: Purchase Order Fulfillment, Supplier Performance
- Sales: Open Sales Orders, Revenue by Product

Each Fiori analytical app includes drill-down to the underlying SAP documents. These replace many of the BW-dependent reports that R/3 customers had to build separately.

---

## Section 6 — KPIs and Metrics Design

### 6.1 KPI Definition Criteria

A metric becomes a KPI when it meets all of the following criteria:

- **Strategic alignment** — it measures something tied to an organizational goal
- **Measurability** — it can be calculated from available data with a defined formula
- **Thresholds** — it has defined targets (what good looks like) and alert levels (what requires action)
- **Ownership** — a specific person or team is responsible for the KPI's value
- **Actionability** — when the KPI moves outside target, there is a defined response

Metrics that do not meet these criteria are "vanity metrics" — they look impressive but do not drive decisions.

### 6.2 ERP KPI Categories

ERP KPIs cluster by functional area:

**Finance:** Days Sales Outstanding (DSO), Days Payable Outstanding (DPO), Days Inventory Outstanding (DIO), Cash Conversion Cycle, Budget Variance

**Supply Chain:** Inventory Turnover, Order Fill Rate, On-Time Delivery, Perfect Order Rate, Supplier Lead Time

**Sales (Salesforce CRM):** Pipeline Coverage Ratio, Win Rate, Average Sales Cycle Length, Customer Acquisition Cost, Quota Attainment

**Service:** First-Call Resolution Rate, Average Handle Time, Case Backlog, Customer Satisfaction (CSAT), Net Promoter Score (NPS)

### 6.3 Leading vs. Lagging Indicators

KPIs can be lagging (measuring outcomes that have already occurred — revenue closed, defects found) or leading (measuring activities that predict future outcomes — pipeline created, demos scheduled, training completed).

A balanced scorecard uses both types. Lagging indicators tell you how you did. Leading indicators tell you how you are likely to do.

---

## Section 7 — Executive Dashboard Design

### 7.1 Audience-First Design

An executive dashboard serves a specific audience with a specific decision-making context. Before designing, answer:

- What decisions does this audience make?
- What information do they need to make those decisions confidently?
- How frequently do those decisions occur?
- What is the consequence of a wrong decision?

An executive reviewing weekly business performance needs different information than a supply chain manager reviewing daily inventory levels. Same ERP system, completely different dashboards.

### 7.2 The 1-3-10 Rule

A useful heuristic for executive dashboards: the viewer should be able to understand overall status in 1 second (at-a-glance color and health indicators), understand the key numbers in 3 seconds (the KPI values), and drill into any detail in 10 seconds (one or two clicks to the underlying data).

### 7.3 Common Dashboard Mistakes

**Too many metrics.** A dashboard showing 40 numbers is a report, not a dashboard. Limit top-level KPIs to five to seven.

**Missing context.** A number without a comparison is meaningless. Always show trend (vs. last period), target (vs. goal), and benchmark (vs. industry or peer group) when available.

**Stale data without disclosure.** Always show the last-refresh timestamp. Users lose trust in dashboards that show wrong numbers without explanation.

**Poor chart selection.** Bar charts compare categories. Line charts show trends over time. Pie charts are appropriate only when parts sum to a meaningful whole and there are fewer than five slices. Gauge charts show performance against a single target. Use the chart type that matches the analytical question.

---

## Section 8 — Data Quality and Reporting Integrity

### 8.1 The Data Quality Hierarchy

Data quality problems occur at four levels:

1. **Completeness** — required fields left blank, optional fields skipped
2. **Accuracy** — incorrect values entered (wrong dates, wrong amounts, typos)
3. **Consistency** — same entity represented in different ways (IBM vs. I.B.M., phone formats 555-1234 vs. (555) 1234)
4. **Timeliness** — records not updated when real-world events occur (deal closed but opportunity still marked Open)

### 8.2 Data Quality Controls in Salesforce

- **Required fields** — system prevents save without a value
- **Validation rules** — formula-based rules that enforce data integrity (e.g., Close Date cannot be in the past for Open opportunities)
- **Duplicate Management** — matching rules detect potential duplicates; duplicate rules block or warn on save
- **Field Dependencies** — controlling fields that restrict which values are available in dependent fields
- **Data Quality Dashboards** — reports that measure completeness rates, track duplicate records, and highlight stale records

### 8.3 Data Quality Controls in SAP

- **Field selection** — in Customizing, each field in a transaction can be marked required, optional, display-only, or hidden per activity type
- **Master Data Governance (MDG)** — workflow-based approval process for creating and changing master data (customer, vendor, material)
- **Data Quality Management (DQM)** — module that scores data quality, identifies duplicates in master data, and runs cleansing workflows
- **Validation at posting** — S/4HANA performs business rule validation at the time of document posting, blocking incorrect entries

### 8.4 Building Reporting Trust

Data quality and reporting are inseparable. High-quality dashboards built on poor data destroy organizational trust in ERP systems. The recommended practice is to audit data quality before launching any new reporting initiative, establish data stewardship roles responsible for ongoing quality, and build data quality metrics into the reporting layer itself (e.g., a "data completeness" tile on every operational dashboard).

---

## Key Terms

- **OLTP** — Online Transaction Processing; optimized for individual record writes
- **OLAP** — Online Analytical Processing; optimized for aggregate reads across large datasets
- **Tabular Report** — simple list format; rows are records, columns are fields
- **Summary Report** — grouped report with subtotals; workhorse of Salesforce reporting
- **Matrix Report** — two-dimensional grouped report; equivalent to a pivot table
- **Joined Report** — multi-block report combining different report types
- **Dashboard Component** — a single visualization on a Salesforce dashboard, backed by a report
- **Dynamic Dashboard** — dashboard that shows data from the perspective of the logged-in user
- **Einstein Analytics** — Salesforce's advanced analytics platform (also called Tableau CRM)
- **Dataset** — data table in Einstein Analytics extracted from Salesforce objects
- **Dataflow** — scheduled process that builds and refreshes Einstein Analytics datasets
- **SAP BW** — SAP Business Warehouse; dedicated analytical data warehouse platform
- **InfoCube** — star-schema fact table in SAP BW used as primary reporting layer
- **BEx Analyzer** — Excel-based query and analysis tool for SAP BW
- **SAP Analytics Cloud (SAC)** — SAP's cloud-native BI, planning, and predictive analytics platform
- **CDS View** — Core Data Services view in S/4HANA; enables embedded real-time analytics
- **KPI** — Key Performance Indicator; a metric tied to a strategic objective with defined targets
- **Lagging Indicator** — measures past outcomes
- **Leading Indicator** — measures activities that predict future outcomes
- **Data Quality** — completeness, accuracy, consistency, and timeliness of ERP data

---

## Review Questions

1. What is the primary difference between OLTP and OLAP processing, and why does this distinction matter for ERP reporting?

2. A sales manager needs a report that shows total opportunity value grouped by sales rep, with a breakdown by product category in columns. Which Salesforce report type should be used?

3. Describe the difference between a standard dashboard and a dynamic dashboard in Salesforce. When would you choose each?

4. What is a Salesforce dataflow, and what role does it play in Einstein Analytics?

5. Explain the SAP BW data flow from source system to InfoCube. What are the intermediate storage objects?

6. What is SAP Analytics Cloud, and how does it differ from BEx Analyzer?

7. List five criteria that a metric must meet to qualify as a KPI.

8. A dashboard shows total revenue as $4.2M, but the actual revenue that closed this week was $5.1M. What is the most likely cause, and how would you investigate?

9. What is the difference between a lagging indicator and a leading indicator? Give one example of each for a sales organization.

10. Name three data quality controls available in Salesforce and explain what each one enforces.

---

## Pre-Lab Preparation

Before attending Lab 14, complete the following:

- Log in to your Salesforce Developer Org and verify you have at least 10 Opportunity records with varied Stage, Close Date, and Amount values
- Navigate to the Reports tab and review the standard "Opportunities" report type
- Review the Salesforce Help article on Dashboard Component Types
- Review the SAP Analytics Cloud free trial overview at sap.com/products/technology-platform/cloud-analytics.html

---

*End of Reading Guide — Module 14*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

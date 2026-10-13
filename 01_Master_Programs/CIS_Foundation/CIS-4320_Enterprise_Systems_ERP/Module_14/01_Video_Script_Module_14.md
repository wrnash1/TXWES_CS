# Video Script: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP | Texas Wesleyan University

## Instructor: Professor Nash

## Estimated Duration: 22–26 minutes

---

## Pre-Production Notes

- Slide deck: 30 slides
- Diagrams: Salesforce report types matrix, dashboard layout with components, Einstein Analytics flow, SAP BW architecture, KPI hierarchy pyramid, data quality impact chain
- Key terms on screen: Report, Dashboard, KPI, Einstein Analytics, SAP BW, BEx Analyzer, OLTP vs. OLAP, Data Quality, Executive Dashboard, Drill-Down, Tabular Report, Summary Report, Matrix Report, Joined Report
- End card: Lab 14, Quiz 14, Discussion Forum 14

---

## [00:00 – 02:00] Opening Hook

[PROFESSOR ON CAMERA]

I want to start with a question. You have an ERP system. It contains every transaction your company has ever processed — every sale, every purchase order, every paycheck, every inventory movement. Millions of records, updated in real time. Congratulations. You have data.

Now the CEO walks in on Monday morning and asks: how did we perform last quarter? Which sales regions missed their targets? Which products have inventory at risk? Are our service tickets trending up or down?

What do you say?

If you cannot answer those questions quickly, confidently, and accurately — your ERP system has failed at its most important job. Because an ERP system is not just a transaction engine. It is a decision-support system. The reporting and analytics layer is where data becomes information, and information becomes action.

Today we cover that layer. Salesforce reports, dashboards, and Einstein Analytics. SAP Business Intelligence and BEx Analyzer. What makes a good KPI. What makes a great executive dashboard. And the thing nobody talks about enough — how bad data quietly destroys good reporting.

[SHOW TITLE SLIDE: Module 14 — ERP Reporting and Business Intelligence]

---

## [02:00 – 06:30] The Reporting Landscape

[SHOW SLIDE: OLTP vs. OLAP]

Before we look at specific tools, we need to understand why ERP reporting requires a different mindset than ERP transaction processing.

Your ERP system is an OLTP system — Online Transaction Processing. It is optimized for writing. Insert a record, update a record, retrieve a single row by primary key. Fast, concurrent, high-volume. Salesforce processes millions of individual actions per day. SAP S/4HANA handles thousands of simultaneous users entering data. OLTP is the engine room.

Reporting is OLAP — Online Analytical Processing. It is optimized for reading. Aggregate millions of rows. Summarize across dimensions. Compare this month to last month to last year. Slice the data by region, by product, by sales rep. OLAP puts enormous read pressure on the database and can slow down the transaction system if you are not careful.

[SHOW SLIDE: Three Reporting Strategies]

Organizations handle this tension in three ways.

Strategy one: run reports directly against the operational database. This is what Salesforce native reports do. It works well for moderate data volumes because Salesforce is a cloud SaaS that manages its own infrastructure scaling.

Strategy two: extract data into a separate data warehouse. SAP Business Warehouse does this. You run the heavy analytical processing on BW, leaving the S/4HANA operational system free for transactions.

Strategy three: use an in-memory column store. SAP HANA's native architecture stores data in columns rather than rows, which makes analytical aggregations dramatically faster. This is why SAP S/4HANA reporting can run directly against the live database in ways that older SAP R/3 could not.

Understanding which architecture you are working in tells you where to build reports and what constraints you are working under.

---

## [06:30 – 12:00] Salesforce Reporting Deep Dive

[SHOW SLIDE: Four Salesforce Report Types]

Salesforce gives you four native report types. Understanding when to use each one is an exam topic and a practical skill.

Tabular reports are the simplest. They look like a spreadsheet. Each row is a record, each column is a field. Use tabular reports when you need a list — all open cases, all accounts in Texas, all opportunities closing this month. Tabular reports are fast to build but cannot be used as dashboard sources without adding a row count or summary.

Summary reports add groupings and subtotals. You can group by field values — by stage, by owner, by region — and see counts, sums, and averages at each group level. Summary reports are the most common report type and the workhorse of Salesforce analytics. A typical Sales VP dashboard runs on summary reports grouped by sales rep.

Matrix reports are two-dimensional. You group both horizontally and vertically. Think of a pivot table. Opportunities by month across the top, by region down the side, dollar amounts in the cells. Matrix reports are powerful but require more planning to set up correctly.

Joined reports are the most advanced. They combine multiple report blocks in one view, each block potentially using a different report type. A joined report could show accounts with no opportunities next to accounts with active opportunities, side by side. Joined reports are used for complex comparisons that would require multiple separate reports otherwise.

[SHOW SLIDE: Building a Report — Key Steps]

When you build a Salesforce report, you start by selecting the Report Type. Report Type is not the format — it is the object relationship that defines what data you can access. Accounts with Contacts is a different report type than Accounts with Opportunities. You cannot add fields from objects not included in the report type.

Then you select columns, apply filters, add groupings for summary or matrix reports, and choose the chart type if you want a visual.

[SHOW SLIDE: Dashboard Architecture]

Dashboards in Salesforce are collections of components. Each component is backed by a report. One dashboard can have up to 20 components. Components can be bar charts, line charts, pie charts, donut charts, funnel charts, gauges, metrics, tables, or Visualforce components.

The critical concept: dashboards in Salesforce show data as of the last refresh. A dashboard does not query live data when someone views it. It queries when it is refreshed — either manually, on a schedule, or automatically when the running user's data changes. For time-sensitive information, schedule dashboard refreshes appropriately.

Dynamic dashboards are a special case. They show data from the perspective of the viewing user rather than a single running user. A sales rep sees their own pipeline. A manager sees their team's pipeline. Same dashboard, different data.

[SHOW SLIDE: Report Subscriptions and Sharing]

Reports and dashboards can be subscribed to by email. Users set up a subscription and receive report results on a schedule — daily, weekly, monthly. This is how you deliver Monday morning metrics to leaders who are not going to log into Salesforce to find a report.

Sharing: reports and dashboards live in folders. Folder sharing controls who can view and who can edit. My Personal Custom Reports folder is private. Public folders are shared across roles, groups, or the entire organization.

---

## [12:00 – 16:00] Einstein Analytics and AI-Driven Insights

[SHOW SLIDE: Einstein Analytics — What It Is]

Einstein Analytics — now called Tableau CRM in some documentation — is Salesforce's advanced analytics platform. It goes beyond native reports in three significant ways.

First, it handles larger data volumes. Native Salesforce reports have row limits. Einstein Analytics can process millions of records from multiple sources, including external data loaded into datasets.

Second, it offers richer visualizations. Lenses and dashboards in Einstein Analytics are more interactive and visually sophisticated than native dashboard components.

Third, it incorporates AI. Einstein Discovery analyzes your data and surfaces statistical insights — not just what happened, but why it happened, and what is predicted to happen. It can identify which factors most strongly correlate with deal wins, or which service account attributes predict churn.

[SHOW SLIDE: Einstein Analytics Data Flow]

The Einstein Analytics data flow has three stages.

Stage one: data intake. Data from Salesforce objects is extracted and loaded into datasets via a dataflow. External data — from spreadsheets, databases, or other cloud services — can be loaded via connectors or the dataset uploader.

Stage two: exploration. Users build lenses — single visualizations against a dataset — by selecting measures and dimensions and applying filters. Lenses are interactive; you can click a bar in a chart to drill into the underlying records.

Stage three: dashboards. Lenses are assembled into Einstein Analytics dashboards, which are more interactive than native dashboards. Steps and widgets in an Einstein dashboard can be linked so that filtering one chart automatically filters all related charts.

[SHOW SLIDE: Einstein AI Features]

Einstein features for reporting include: Prediction Builder (build custom predictive models on any Salesforce field), Next Best Action (surface recommended actions to users based on Einstein scores), and Einstein Discovery (automated statistical analysis and story generation from data).

For the Salesforce Administrator exam, you need to know that Einstein Analytics is an additional licensed product, that datasets must be configured and refreshed, and that dataflows define how Salesforce data is transformed into datasets.

---

## [16:00 – 20:00] SAP Business Intelligence

[SHOW SLIDE: SAP BI Architecture]

SAP's business intelligence ecosystem is more complex than Salesforce's, reflecting its enterprise data warehouse heritage.

SAP Business Warehouse — SAP BW — is the dedicated data warehouse platform. It extracts data from S/4HANA (and legacy R/3) and stores it in InfoProviders optimized for reporting. The extraction mechanism is called a data transfer process. The InfoProviders include InfoObjects (the metadata — master data and characteristics), InfoCubes (star-schema fact tables), and DataStore Objects (DSOs, which hold detailed transactional data before it is aggregated into InfoCubes).

[SHOW SLIDE: SAP BW Query Tools]

BEx Analyzer is the Excel-based query and analysis tool for SAP BW. Finance and supply chain analysts who grew up on SAP live in BEx Analyzer. You build queries using BEx Query Designer — dragging characteristics and key figures into rows, columns, and free dimensions — and execute them in Excel. The output is a live-connected pivot-table-style analysis that can be filtered, drilled, and saved as a workbook.

BEx Web Application Designer creates web-based analytical applications — dashboards and reports that run in a browser without Excel. These are used for read-only displays on executive portals.

SAP Lumira is the modern self-service visualization tool. Think of it as SAP's answer to Tableau — drag-and-drop data visualization with richer chart types than BEx.

SAP Analytics Cloud — SAC — is the cloud-native BI platform. It combines BI, planning, and predictive analytics in one SaaS tool. SAC connects directly to S/4HANA and BW, and it is the strategic direction for SAP analytics going forward.

[SHOW SLIDE: Embedded Analytics in S/4HANA]

S/4HANA Fiori includes embedded analytical apps built on CDS views — Core Data Services. These are real-time reports that run directly against the S/4HANA database without an extraction to BW. Inventory management, accounts receivable aging, open purchase orders — all available as Fiori analytical tiles with drill-down to individual documents.

This is a significant architectural shift from older SAP. In R/3, you had to extract to BW to get good reports. In S/4HANA, many operational reports run live.

---

## [20:00 – 23:00] KPIs and Executive Dashboards

[SHOW SLIDE: What Makes a Good KPI]

KPI stands for Key Performance Indicator. Every organization tracks dozens of metrics. A KPI is a metric that matters — one tied directly to a strategic objective, measurable with available data, and actionable when it moves in the wrong direction.

A good KPI has five properties: it is aligned to a business objective, it is measurable with current data, it has a defined target or threshold, it is owned by a person or team who can act on it, and it is reviewed on a regular cadence.

Common ERP KPIs include: Days Sales Outstanding in Finance, Inventory Turnover in Supply Chain, First-Call Resolution Rate in Service, Pipeline Coverage Ratio in Sales, and On-Time Delivery in Operations.

[SHOW SLIDE: Executive Dashboard Principles]

An executive dashboard is not a report. It is a decision cockpit. Design principles for executive dashboards:

One — show status at a glance. Use color coding and simple visual indicators. Green is good, yellow is watch, red is act. Executives should not have to read a number to know if something is wrong.

Two — minimize cognitive load. No more than seven metrics on a single view. Group related KPIs. Use consistent scales.

Three — provide drill-down paths. The dashboard shows the summary. One click should reveal the detail. Two clicks should show the source records.

Four — be honest about data freshness. Label every metric with its last-refresh timestamp. Executives making decisions on stale data is worse than no dashboard at all.

---

## [23:00 – 26:00] Data Quality and Its Impact on Reporting

[SHOW SLIDE: The Garbage In Problem]

I want to close with the topic that reporting textbooks often skip: data quality.

Every reporting principle we discussed today assumes that the data in your ERP system is accurate, complete, and timely. In practice, it often is not. Users skip required fields. They enter dummy values to get past validation. They use inconsistent names — IBM vs. I.B.M. vs. International Business Machines. They close records without updating status fields.

The result: your carefully designed KPI dashboard reports wrong numbers. Leadership makes decisions based on fiction. And because it looks like a professional dashboard, nobody questions it.

[SHOW SLIDE: Data Quality Impact Chain]

The chain of impact runs like this. Bad data entry creates inaccurate records. Inaccurate records produce wrong report totals. Wrong totals produce misleading KPIs. Misleading KPIs produce bad decisions. Bad decisions produce business outcomes that nobody can explain — because the dashboard looked fine.

[SHOW SLIDE: Data Quality Controls in ERP]

ERP systems have data quality controls you can configure. In Salesforce: required fields, validation rules, field-level duplicate management, data cleanup tools, and Salesforce Data Quality dashboards that show completeness rates per field. In SAP: field selection (required vs. optional), master data governance workflows, and the Data Quality Management module.

Reporting design must account for data quality. Before you build a dashboard for an executive, run a data quality audit on the fields that will feed it. Know your completeness rates. Know your common error patterns. Fix what you can before the first review meeting.

[SHOW SLIDE: Module 14 Summary]

Let me summarize. Reporting and BI are the layer where ERP data becomes organizational intelligence. Salesforce provides four report types, native dashboards, and Einstein Analytics for advanced AI-driven insights. SAP provides BEx Analyzer for BW-based analysis and SAP Analytics Cloud for modern cloud BI. KPIs require strategic alignment, clear ownership, and defined thresholds. Executive dashboards must show status at a glance with drill-down paths. And none of it works if the underlying data is dirty.

Your lab this week walks you through building a Salesforce dashboard from scratch and analyzing a KPI design scenario. Your quiz covers report types, dashboard components, Einstein Analytics basics, and SAP BI tools.

See you in the discussion forum.

[END CARD: Lab 14 | Quiz 14 | Discussion Forum 14]

---

*End of Video Script — Module 14*

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

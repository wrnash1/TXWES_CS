# Video Script: Module 14 — ERP Reporting and Business Intelligence

## Course: CIS-4320 Enterprise Systems and ERP

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Salesforce Administrator / SAP S/4HANA Essentials

---

## Production Notes

**Duration:** Approximately 25–30 minutes
**Format:** Lecture with slide transitions and live demonstration walkthroughs
**Segments:** 6 segments with natural pause points

---

## Segment 1: Introduction — From Data to Decisions (Lines 1–40)

[SLIDE: Title card — "Module 14: ERP Reporting and Business Intelligence"]

Welcome to Module 14. I am Professor Nash. Today we focus on one of the most business-visible aspects of any ERP system: reporting and business intelligence. ERP systems are valuable not just because they process transactions, but because they accumulate enormous amounts of structured, authoritative data that can drive better decisions. The question we answer today is: how do you turn that data into insight?

[SLIDE: The reporting pyramid]

Imagine a pyramid. At the base is raw operational data — sales orders, purchase orders, financial postings, inventory movements. In the middle are standard reports and dashboards — aggregated views consumed by managers on a daily or weekly basis. At the top is strategic intelligence — executive dashboards, trend analysis, forecasting models, and AI-generated insights.

ERP systems touch every layer. The challenge is building the reporting architecture that serves each layer efficiently.

[SLIDE: Why reporting breaks down]

Reporting in enterprise systems commonly fails for three reasons. First, the data quality problem — if your ERP data is dirty (missing fields, duplicate records, inconsistent coding), your reports will be wrong. Executives learn not to trust them, and the whole reporting apparatus loses value. Second, the performance problem — running heavy analytical queries against the same database that handles live transactions slows down operations. Third, the usability problem — reports that only a trained analyst can run and interpret do not scale.

[SLIDE: Learning objectives]

Today we cover four areas: Salesforce reports, dashboards, and Einstein Analytics; SAP Business Intelligence including BW/4HANA and Crystal Reports; KPI design principles; and executive dashboard best practices.

[PAUSE]

---

## Segment 2: Salesforce Reporting (Lines 41–85)

[SLIDE: Salesforce report types]

Salesforce has four native report formats.

A **Tabular Report** is the simplest — it is a flat list of records, like a spreadsheet. Great for exports, not great for analysis. Use tabular reports when you want a list of open opportunities or a contact directory.

A **Summary Report** groups records by a field and shows subtotals. For example, opportunities grouped by Sales Stage, with total value per stage. This is the most commonly used format for operational reporting.

A **Matrix Report** is a two-dimensional cross-tab. Rows represent one grouping (such as sales rep), columns represent another (such as quarter), and cells show the aggregate value. This is the right format for comparing performance across two dimensions.

A **Joined Report** combines multiple report blocks — each with its own report type — in a single view. Useful for comparing, for example, open cases versus closed cases side-by-side in one report. Joined reports are the most complex and are tested on the Admin exam.

[SLIDE: Report types — not the same as report formats]

Do not confuse "report formats" with "report types." Report types define which objects and their related objects are available as data sources for a report. For example, the "Opportunities with Products" report type includes both Opportunity and Opportunity Line Item data. The "Opportunities without Products" type includes only Opportunity data.

Standard report types ship with Salesforce. Custom report types let administrators define precisely which objects and fields are available in a report, including controlling which related record fields are joined in.

[SLIDE: Report filters and buckets]

Reports can be filtered to show only relevant records. Standard filter conditions include field equals, contains, greater than, and many others. Cross-object filters allow filtering by the presence or absence of related records — for example, "Accounts with no open Opportunities in the past 90 days."

Bucket fields allow grouping numeric or text values into named categories directly in the report, without modifying the underlying data. For example, a bucket on Opportunity Amount might group values under $10,000 as "Small," $10,000–$100,000 as "Mid," and over $100,000 as "Large." This is powerful for ad-hoc segmentation.

[SLIDE: Salesforce Dashboards]

Salesforce Dashboards are visual displays built from report data. Each dashboard contains up to 20 components (in Enterprise Edition and above). Component types include bar charts, line charts, pie charts, donut charts, funnel charts, scatter plots, gauges, tables, and metrics (single number KPIs).

Each dashboard has a "running user" — the user whose access permissions determine what data the dashboard shows. If the running user is a specific person, all dashboard viewers see the same data. If the running user is "logged-in user," each viewer sees only the data they have permission to access.

[SLIDE: Dashboard subscriptions and dynamic dashboards]

Dashboard subscriptions allow users to receive scheduled email snapshots. Dynamic dashboards use the viewing user as the running user, which means each viewer sees data filtered to their access level — ideal for performance dashboards shown to individual sales reps.

For the Admin exam: know the maximum number of dashboard components (20 in Enterprise), the difference between static and dynamic dashboards, and what the running user controls.

[PAUSE — transition to Einstein Analytics]

---

## Segment 3: Einstein Analytics and CRM Analytics (Lines 86–125)

[SLIDE: Beyond standard reports — CRM Analytics]

Salesforce CRM Analytics (formerly Einstein Analytics, formerly Wave Analytics) is Salesforce's advanced analytics platform. It operates separately from native reports and dashboards — it ingests data into its own analytical data store, which enables much faster query performance on large datasets.

CRM Analytics supports data from Salesforce objects, external CSV files, and connected data sources. Its main components are:

Datasets: structured analytical data tables.

Lenses: explorations of a single dataset — interactive charts that you slice and dice in real time.

Dashboards: collections of visualizations built from lenses and datasets.

Stories: AI-generated narrative explanations of trends in your data.

[SLIDE: Einstein Discovery]

Einstein Discovery is the AI-powered prediction and explanation engine within CRM Analytics. It can automatically identify correlations, predict outcomes (such as whether an opportunity will close), and explain what factors most influence a metric.

For example, Einstein Discovery might analyze your Closed Lost opportunities and tell you: "Opportunities that went through more than three proposal revisions have a 67% higher chance of closing lost." That kind of pattern recognition, surfaced automatically, is the promise of AI-assisted analytics.

[SLIDE: When to use CRM Analytics vs. native reports]

Use native reports and dashboards when: the data volume is moderate, the analysis is operational rather than exploratory, and non-technical users need to build their own reports.

Use CRM Analytics when: data volumes are very large (millions of records), you need multi-dimensional slicing and filtering in real time, you want AI-powered predictions, or you are combining Salesforce data with external data sources.

[SLIDE: Salesforce reporting permissions]

Reporting-related permissions relevant to the Admin exam:

"Create and Customize Dashboards" — needed to create dashboards.

"Manage Dashboards in Public Folders" — needed to create or edit dashboards in public folders.

"Create and Customize Reports" — needed to build reports.

"Manage Reports in Public Folders" — needed to create or edit reports in public folders (different from your private folder).

[PAUSE — transition to SAP BI]

---

## Segment 4: SAP Business Intelligence (Lines 126–170)

[SLIDE: SAP's BI landscape]

SAP has a rich and somewhat complex business intelligence landscape that has evolved over decades through organic development and acquisitions. Let me map out the main components you need to know.

[SLIDE: SAP BW/4HANA — the data warehouse]

SAP BW/4HANA (Business Warehouse on HANA) is SAP's enterprise data warehouse platform. It extracts data from SAP S/4HANA and other sources, applies business transformations, and stores the data in an optimized structure for analytical queries.

BW/4HANA uses a layered modeling approach. The Persistent Staging Area (PSA) stores raw extracted data. DataStore Objects (DSOs) hold transformed, reconciled data. Composite Providers join multiple data sources for reporting. The HANA in-memory database accelerates queries dramatically — reports that took hours in older BW systems now run in seconds.

[SLIDE: Extractors — connecting SAP S/4HANA to BW]

Data flows from SAP S/4HANA to BW through extractors — predefined data extraction programs. Standard extractors exist for most functional areas: financial statements, sales analytics, purchasing analytics, inventory analytics, and many others. Custom extractors can be built using ABAP for non-standard data needs.

[SLIDE: SAP Analytics Cloud — SAP AC]

SAP Analytics Cloud (SAC) is SAP's modern, cloud-based analytics platform. It unifies planning, predictive analytics, and business intelligence in a single tool. SAC can connect directly to SAP BW/4HANA, SAP S/4HANA (via live connections), and many external data sources.

SAC's main capabilities: story-based dashboards (called "Stories"), planning models for financial forecasting and budgeting, and built-in machine learning for predictive analytics. SAC is SAP's strategic direction for BI — if you are starting a new SAP analytics project today, SAC is the answer.

[SLIDE: SAP Crystal Reports and SAP Lumira]

**Crystal Reports** is a pixel-perfect report designer traditionally used for operational reports — invoices, shipping labels, financial statements. Crystal Reports produce formatted output for printing or PDF export. They are driven by SQL queries or OLAP connections and are still widely used for compliance and operational reporting.

**SAP Lumira** was SAP's self-service data visualization tool, allowing business users to create interactive charts and stories without IT involvement. Lumira's capabilities have largely been absorbed into SAP Analytics Cloud.

[SLIDE: Operational vs. Analytical reporting in SAP]

SAP distinguishes between operational reporting — real-time queries against the live S/4HANA database — and analytical reporting — queries against a data warehouse or analytical store.

For operational reporting, SAP Fiori apps and embedded CDS (Core Data Services) views in S/4HANA provide real-time list views and analytical tiles. For strategic analytical reporting, BW/4HANA and SAP Analytics Cloud are used. Understanding this distinction helps you recommend the right tool for a given reporting need.

[PAUSE]

---

## Segment 5: KPIs and Executive Dashboard Design (Lines 171–210)

[SLIDE: What makes a KPI?]

A Key Performance Indicator is a measurable value that demonstrates how effectively an organization is achieving a key business objective. Not every metric is a KPI. Good KPIs share five characteristics — they are often described using the SMART framework: Specific, Measurable, Achievable, Relevant, and Time-bound.

Poor example of a KPI: "track sales." Good KPI: "Closed Won Opportunity revenue in the current fiscal quarter compared to quota."

The difference is that a real KPI has a target, a time horizon, and a clear owner.

[SLIDE: Common ERP KPIs by function]

Financial KPIs:

- Days Sales Outstanding (DSO): average days to collect payment after invoicing
- Budget vs. Actual Variance: planned spend versus actual spend by cost center
- Cash Conversion Cycle: time from cash outflow (purchasing) to cash inflow (collections)

Sales and CRM KPIs:

- Pipeline Coverage: total pipeline value divided by quota
- Win Rate: Closed Won opportunities divided by total closed opportunities
- Average Sales Cycle Length: average days from opportunity creation to close

Operations KPIs:

- On-Time Delivery Rate: percentage of deliveries reaching the customer by the committed date
- Perfect Order Rate: orders delivered on time, in full, with no damage and no invoice errors
- Inventory Turnover: cost of goods sold divided by average inventory value

[SLIDE: Dashboard design principles]

Designing an executive dashboard that actually gets used requires discipline. These are the principles that separate a dashboard people look at daily from one that is abandoned after two weeks.

**Principle 1: Less is more.** An executive dashboard should show five to seven key metrics, not twenty. Every metric takes cognitive load to process. If everything is important, nothing is.

**Principle 2: Context before drill-down.** Show the high-level number with a trend indicator (up/down arrow versus prior period) before offering drill-down details. Executives need to know quickly whether things are on track.

**Principle 3: Consistent time periods.** If one metric shows this quarter and another shows this month, the dashboard is confusing. Align all time periods, and make the current date visible on the dashboard.

**Principle 4: Actionable alerts.** Color-coded indicators (green/yellow/red) should map to defined thresholds. "Red" should mean "something requires executive attention now," not just "below last quarter."

**Principle 5: Mobile-friendly.** Executives check dashboards on phones and tablets. Design for a small screen first.

[SLIDE: Data quality and reporting trust]

No reporting architecture survives if users do not trust the data. The most common reasons executives stop using dashboards are: numbers that do not match what the ops team says, inconsistent definitions (does "revenue" mean booked or recognized?), and reports that are always slightly out of date.

Building trust requires: agreed definitions in a data dictionary, a known refresh cadence, and a visible "last updated" timestamp on every dashboard.

[PAUSE]

---

## Segment 6: Summary and Certification Prep (Lines 211–240)

[SLIDE: Comparing Salesforce and SAP reporting]

Let me put the two platforms side by side for comparison.

Salesforce native reports and dashboards are built for business users — administrators and non-technical users can build them without coding. They are strong for CRM operational data but limited for very large volumes and complex analytics.

CRM Analytics (Einstein Analytics) extends Salesforce's analytical capability with a separate data store and AI features, at the cost of additional licensing and configuration complexity.

SAP BW/4HANA is an enterprise data warehouse built for very high-volume, multi-source analytical reporting. It requires technical expertise to configure but provides exceptional query performance.

SAP Analytics Cloud is SAP's modern cloud BI platform, unifying analytics, planning, and prediction. It is the strategic choice for new SAP implementations.

[SLIDE: Certification exam tips]

Salesforce Admin exam reporting topics:

- Know the four report formats (tabular, summary, matrix, joined) and when to use each
- Know that the running user on a dashboard controls data visibility
- Know the difference between standard report types and custom report types
- Know what bucket fields do
- Know that "Manage Dashboards in Public Folders" is needed to create dashboards in shared folders

SAP essentials reporting topics:

- Know what BW/4HANA is and how data flows from S/4HANA via extractors
- Know what SAP Analytics Cloud is and how it differs from Crystal Reports
- Know the difference between operational reporting (live S/4HANA) and analytical reporting (BW)
- Understand the concept of a KPI and be able to give examples

[SLIDE: Key terms]

Summary Report: Salesforce report format that groups records and shows subtotals.

Matrix Report: two-dimensional cross-tab report in Salesforce.

Joined Report: Salesforce report combining multiple report blocks.

Bucket Field: a report feature that groups field values into named categories.

Dashboard Running User: the user whose access determines what data appears in a shared dashboard.

CRM Analytics: Salesforce's advanced analytics platform with its own data store.

Einstein Discovery: AI-powered prediction engine within CRM Analytics.

SAP BW/4HANA: SAP's enterprise data warehouse platform running on HANA in-memory database.

SAP Analytics Cloud (SAC): SAP's cloud-native BI and planning platform.

Crystal Reports: SAP's pixel-perfect formatted report tool for operational and compliance reports.

KPI: a metric tied to a specific business objective with a target and time horizon.

[SLIDE: Coming up in Module 15]

In Module 15 we tackle ERP implementation methodology — the ASAP methodology for SAP, the Salesforce implementation lifecycle, change management, cutover planning, and total cost of ownership. This is the "how do we go live" module, and it covers a topic that every enterprise systems professional will face in their career.

Complete the Reading Guide, Lab, and Discussion. The quiz opens Monday.

See you in Module 15.

[END OF VIDEO SCRIPT]

---

*Document prepared for CIS-4320 instructional use. Texas Wesleyan University. Proprietary and Confidential.*

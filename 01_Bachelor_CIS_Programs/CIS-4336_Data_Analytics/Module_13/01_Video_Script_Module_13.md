# Video Script: Module 13 — Reporting and Dashboard Design

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Estimated Duration:** 18–22 minutes

---

### [00:00 – 02:00] Introduction

**Visual:** Instructor on camera with title card: **Reporting and Dashboard Design**.

**Audio:** "Welcome to Module 13. This week we step back from writing code and focus on communicating data. Even the most sophisticated analysis has no value if the person making decisions cannot understand or trust what you are showing them. This module covers the business intelligence tools professionals use most — Tableau, Power BI, and Looker — along with dashboard design principles, KPI selection, data storytelling, and stakeholder communication. These topics appear directly on the CompTIA Data+ exam in Domain 4, Data Visualization. Let's get into it."

**Study Link:** [Tableau Public Training Resources](https://public.tableau.com/en-us/s/resources)

---

### [02:00 – 06:00] Business Intelligence Tools Overview

**Visual:** Side-by-side screenshots of Tableau Desktop, Power BI Desktop, and a Looker dashboard.

**Alt-text:** Three BI tool interfaces shown side by side. Tableau shows a geographic sales map. Power BI shows a bar and line combo chart with a filter panel. Looker shows a web-based explore interface with a data table and a line chart.

**Audio:** "There are three BI tools you are most likely to encounter in the workplace and on the Data+ exam: Tableau, Power BI, and Looker.

**Tableau** is a drag-and-drop desktop tool known for fast visual analytics. You connect to a data source, drag dimensions and measures onto a canvas, and Tableau suggests chart types. It is particularly strong for ad-hoc exploration and for publishing polished dashboards to Tableau Server or Tableau Public.

**Power BI** is Microsoft's BI platform, deeply integrated with Excel, Azure, and Microsoft 365. It uses a drag-and-drop interface like Tableau but adds Power Query for data transformation and DAX — Data Analysis Expressions — for calculated measures. If your organization runs on Microsoft, you will encounter Power BI.

**Looker** is a cloud-based BI platform owned by Google. Its unique feature is LookML — a modeling language that defines metrics and dimensions once in a central repository so every analyst in the organization calculates revenue the same way. Looker is common in data-mature technology companies.

For the Data+ exam you do not need deep tool expertise. You need to understand what category of problem each tool solves and how they differ architecturally."

---

### [06:00 – 10:00] Dashboard Design Principles

**Visual:** Split screen comparing a cluttered dashboard with 14 charts versus a clean dashboard with 4 focused KPI tiles and charts. Red annotations highlight problems in the cluttered version.

**Alt-text:** Left: a dashboard so densely packed that individual charts are unreadable. Right: four large charts with generous whitespace, consistent color, and clear titles.

**Audio:** "A dashboard is not a data dump. It is a communication tool designed to help a specific audience answer specific questions quickly. The five most important design principles are:

One — Single audience, single purpose. Every dashboard should serve one role — executive, operations manager, sales rep — and answer the questions that role asks most often.

Two — Five or fewer KPIs at the top. The human eye cannot process more than five numbers simultaneously without losing focus. Lead with the most critical metrics, large and clearly labeled.

Three — Consistent color encoding. Pick one color to mean good and one to mean bad and use them consistently across every chart. Never use red for both a warning state and a product category label.

Four — Remove chart junk. Gridlines, 3D effects, legends when labels will do, and decorative borders all compete with the data for attention.

Five — Proximity and grouping. Related metrics belong next to each other. Whitespace between groups signals a topic boundary."

---

### [10:00 – 13:30] KPI Selection

**Visual:** A two-column table: left shows vanity metrics; right shows actionable KPIs.

**Alt-text:** Table with columns Vanity Metric and Actionable KPI. Rows include: Total website visits vs. Conversion rate; Total social media followers vs. Lead generation from social; Total emails sent vs. Email click-through rate.

**Audio:** "Choosing the right KPIs is where business understanding meets data analysis. A KPI — Key Performance Indicator — must be tied to a business outcome, measurable with available data, and actionable. If no one can take a specific action in response to a KPI moving, it is not a useful KPI.

A common trap is reporting **vanity metrics** — numbers that look impressive but do not drive decisions. Total website visitors is a vanity metric. Conversion rate — the percentage of visitors who complete a purchase — is a KPI. Total support tickets closed is a vanity metric. Average resolution time is a KPI.

For the Data+ exam, know the difference between a metric, a KPI, and a benchmark. A metric is any quantitative measurement. A KPI is a metric tied to a strategic objective with a target and a direction. A benchmark is a reference value used to evaluate performance in context."

---

### [13:30 – 17:00] Storytelling with Data

**Visual:** A four-panel sequence: raw data table → single chart → annotated chart → one-sentence insight statement.

**Alt-text:** Four-panel progression. Panel 1: a raw spreadsheet. Panel 2: a line chart of monthly revenue. Panel 3: the same chart with an annotation circle and callout "March drop caused by warehouse outage." Panel 4: text reading "Revenue recovered in April after a temporary March disruption; Q2 on track to exceed target."

**Audio:** "Data storytelling is the practice of combining data, visualization, and narrative to communicate a finding in a way that drives action. The classic structure is:

First — **Context.** What was the situation before you ran the analysis?

Second — **Finding.** What did the data show? State the most important result in one sentence.

Third — **Evidence.** Show the chart or table that supports the finding. Annotate the most important point directly on the chart so the viewer's eye goes there first.

Fourth — **Implication.** What should happen next? What decision does this data support?

This four-part structure works for a one-page executive summary, a five-minute presentation, or a single email. Lead with the insight, not the methodology."

---

### [17:00 – 20:30] Stakeholder Communication

**Visual:** A two-by-two persona matrix with four stakeholder types and their communication preferences.

**Alt-text:** Grid with rows labeled Technical and Non-Technical, columns labeled Operational and Strategic. Each quadrant contains a role and preferred format: data engineer prefers schema docs, operations manager prefers daily drill-down report, executive prefers one-page summary, board member prefers single-chart quarterly slide.

**Audio:** "Different stakeholders need the same data presented differently. An executive needs a one-page summary with three numbers and a trend arrow. A data engineer needs schema documentation and query logic. An operations manager needs a daily report with drill-down capability. A board member needs a quarterly slide with a single chart and a one-sentence takeaway.

The common mistake analysts make is presenting data in the format that makes sense to them — detailed, technically precise, hedged with caveats — to an audience that makes decisions at a strategic level.

Key communication rules for the Data+ exam: match detail to role; always label axes, units, and time periods; provide data definitions for any metric that might be calculated differently across teams; and always state the data's recency — 'as of last Monday' or 'refreshed daily at 6 AM.'"

---

### [20:30 – 22:00] Exam Connection and Wrap-Up

**Visual:** Data+ domain map with Domain 4 — Data Visualization — highlighted.

**Audio:** "Domain 4 covers approximately 20 to 24 percent of Data+ exam questions, making it one of the highest-value domains to study. Expect questions about chart type selection for a given scenario, dashboard design principles, the difference between KPI and metric and benchmark, and how to match communication format to audience. The reading guide this week covers every chart type on the exam. The lab has you producing a dashboard design document. See you there."

---

### Instructor Notes

* Dashboard critique exercise works well before the lab — find three public Tableau dashboards and evaluate them against the five design principles
* Data+ exam Domain 4 is approximately 20–24% of exam weight — emphasize this module
* Lab requires no BI software — students produce a design specification document

# Quiz: Module 13 — Reporting and Dashboard Design

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

A sales director wants a dashboard that shows the total number of leads generated this month, total sales calls made, and total emails sent. An analyst reviewing the requirements argues that these are vanity metrics and should be replaced. Which replacement set best reflects actionable KPIs?

A) Total leads, total calls, total emails — these are already KPIs because they are quantitative measurements.

B) Lead-to-opportunity conversion rate, call-to-meeting booking rate, and email click-through rate — these tie activity to outcomes and reveal where the sales funnel is leaking.

C) Average lead age in days, average call duration, and average email length — these add detail but still do not connect to revenue outcomes.

D) Monthly active users, net promoter score, and churn rate — these are KPIs but for customer success, not sales activity.

#### Q1 Correct Answer: B

#### Q1 Distractor Analysis

A is incorrect because raw counts without targets or outcome connections are vanity metrics. C adds granularity without strategic relevance. D are valid KPIs for a different function entirely.

---

### Question 2

An analyst is designing a dashboard for a Chief Financial Officer who reviews business performance quarterly. Which combination of design decisions is most appropriate?

A) Real-time data refresh; 15 KPI tiles; detailed drill-down tables with raw transaction data.

B) Weekly refresh; 5 KPI tiles; one trend chart; one comparison chart; no raw data tables.

C) Daily refresh; 10 KPI tiles; six charts; a data export button and a filter panel for every metric.

D) Monthly refresh; 3 summary KPIs; one year-over-year chart; a two-sentence narrative summary.

#### Q2 Correct Answer: D

#### Q2 Distractor Analysis

A gives a CFO real-time granularity they do not need and cognitive overload from 15 KPIs. B is reasonable but the weekly refresh and 5 KPI count are less optimal for a quarterly review context. C provides too much detail and too many KPIs for a strategic executive. D matches the CFO's quarterly cadence, limits KPIs, and adds a narrative — the most executive-appropriate format.

---

### Question 3

Which of the following is the best example of a leading indicator?

A) Total revenue closed this quarter — reflects outcomes already achieved.

B) Average deal size for closed contracts — a lagging measure of past performance.

C) Number of qualified leads added to the pipeline this week — predicts future revenue and can be acted on now.

D) Customer satisfaction score for last month's support interactions — reflects past service quality.

#### Q3 Correct Answer: C

#### Q3 Distractor Analysis

A, B, and D are all lagging indicators — they report on events that have already occurred. C measures new pipeline activity that has not yet converted, making it predictive of future sales performance.

---

### Question 4

A data analyst is building a chart to show how monthly revenue has trended over the past three years (36 data points). Which chart type is most appropriate?

A) Pie chart — shows part-to-whole relationships; inappropriate for continuous time-series data.

B) Scatter plot — shows the relationship between two numeric variables; not suited for time-series trend display.

C) Line chart — connects data points across a continuous time axis and is the standard choice for showing trends over time.

D) Histogram — shows the distribution of a numeric variable; does not show change over time.

#### Q4 Correct Answer: C

#### Q4 Distractor Analysis

A is for part-to-whole composition, not trends. B requires two numeric variables with no inherent time order. D shows frequency distribution, not chronological trend.

---

### Question 5

A Looker administrator defines all revenue calculations in a central LookML model. What problem does this architecture solve that Tableau and Power BI do not solve by default?

A) It prevents analysts from building charts without SQL knowledge.

B) It eliminates the need for a data warehouse by storing data inside Looker.

C) It ensures every team calculates revenue using the same definition, preventing metric inconsistency across departments.

D) It automatically generates dashboards without any analyst input.

#### Q5 Correct Answer: C

#### Q5 Distractor Analysis

A is incorrect — Looker still requires technical setup; it does not prevent SQL use. B is wrong; Looker queries external databases and does not store data itself. D is incorrect; LookML defines data models, not finished dashboards.

---

### Question 6

Which dashboard design principle is violated when a dashboard uses red to indicate both "below sales target" and "the product category Electronics" in separate charts?

A) Single audience, single purpose — the dashboard is trying to serve multiple users.

B) Limit the KPI count — too many metrics are being tracked.

C) Consistent color encoding — the same color carries two different meanings in the same dashboard.

D) Remove chart junk — decorative elements are distracting from the data.

#### Q6 Correct Answer: C

#### Q6 Distractor Analysis

A is about scope, not color. B is about KPI count, not color usage. D is about unnecessary visual elements, not color meaning conflicts.

---

### Question 7

An analyst presents a finding to an executive by showing 22 pages of methodology documentation, confidence intervals for every estimate, and a full data dictionary. The executive seems confused and disengaged. What is the most likely cause?

A) The data is incorrect and the executive detected the error.

B) The analyst communicated at the wrong level of detail for a strategic decision-maker who needs a clear finding and implication, not methodology.

C) The executive does not understand data and needs a training course before reviewing the analysis.

D) Confidence intervals should always be removed from executive presentations because they are mathematically incorrect.

#### Q7 Correct Answer: B

#### Q7 Distractor Analysis

A is possible but not the most likely cause given the described scenario. C blames the audience rather than the communication format. D is incorrect — confidence intervals are valid but inappropriate at the level of detail for a strategic executive presentation.

---

### Question 8

A product manager wants to compare how five product lines contribute to total annual revenue, where no single product line has an overwhelming share. Which chart type is most appropriate?

A) Line chart — best for continuous time trends, not for comparing proportional shares.

B) Stacked bar chart — shows the absolute value of each component over time or across categories while also displaying total magnitude.

C) Pie chart with five slices — acceptable for five clear proportions; communicates part-to-whole cleanly when slices are distinct.

D) Scatter plot — requires two numeric variables and no part-to-whole relationship.

#### Q8 Correct Answer: C

#### Q8 Distractor Analysis

A does not show composition. B is better when time or sequence is involved — for a single period comparison, it adds unnecessary complexity. D requires two numeric variables and does not display proportional composition. C is the standard choice for five-category part-to-whole comparison with distinct proportions.

---

### Question 9

Which of the following correctly defines a benchmark in the context of business intelligence reporting?

A) A benchmark is a KPI whose target has been exceeded for three consecutive reporting periods.

B) A benchmark is a reference value — internal, external, or aspirational — used to evaluate whether a metric's current value is acceptable.

C) A benchmark is a chart annotation that marks the median value of a distribution.

D) A benchmark is a Power BI DAX formula used to calculate a running total.

#### Q9 Correct Answer: B

#### Q9 Distractor Analysis

A conflates benchmark with a performance milestone. C describes a chart annotation, not a data concept. D confuses benchmark with a specific tool formula unrelated to the definition.

---

### Question 10

Which Data+ exam domain is most directly covered by the dashboard design, KPI selection, and data storytelling content in Module 13?

A) Domain 1 — Data Concepts and Environments.

B) Domain 2 — Data Mining.

C) Domain 3 — Data Analysis and Statistics.

D) Domain 4 — Data Visualization, which covers report types, chart selection, dashboard design, and communicating findings to stakeholders.

#### Q10 Correct Answer: D

#### Q10 Distractor Analysis

A covers foundational data concepts and infrastructure. B covers data collection and transformation. C covers statistical analysis methods. D explicitly includes visualization types, design principles, and stakeholder communication — the exact content of Module 13.

---

---

### Question 11 (5 points)

A financial analyst builds a dashboard showing only one metric: net revenue for the current month with a green/red indicator versus last month. A colleague argues the dashboard should include 12 more KPIs. What dashboard design principle does the colleague's suggestion violate?

A) Consistent color encoding — using too many KPIs creates color palette conflicts.

B) Limit the KPI count — a focused dashboard with fewer, well-chosen metrics communicates more clearly than a crowded one.

C) Single audience, single purpose — the dashboard is serving too many departments.

D) Remove chart junk — additional KPI tiles add unnecessary decorative elements.

#### Q11 Correct Answer: B

#### Q11 Distractor Analysis

The principle being violated is KPI limitation — adding 12 more metrics creates cognitive overload and dilutes attention from the most important signal. A is about color meaning consistency, not KPI count. C is about audience scope, not number of metrics. D is about removing non-data visual elements, not reducing metric count.

---

### Question 12 (5 points)

A sales team dashboard auto-refreshes every 5 seconds. The sales data is only updated in the data warehouse once per day. What problem does this create?

A) The dashboard will display incorrect data because real-time refresh requires a streaming data source.

B) The refresh rate wastes server resources and creates unnecessary query load without providing any new information, since the underlying data is not changing.

C) A 5-second refresh violates data governance policies by exposing PII in real time.

D) Dashboard refresh rates must match the update cadence exactly — a 5-second refresh on daily data is technically impossible.

#### Q12 Correct Answer: B

#### Q12 Distractor Analysis

When the data source only updates once per day, refreshing every 5 seconds queries the same static data repeatedly, consuming database compute resources without benefit. A is incorrect — the dashboard will show the same data every time, not incorrect data. C is unrelated to refresh rate; PII governance is a separate concern. D is incorrect; technically the dashboard can refresh at any rate, but it is pointless if the data does not change.

---

### Question 13 (5 points)

Which data storytelling element answers the question "so what should we do about it?"

A) Context — establishes why the finding matters relative to goals or benchmarks.

B) Insight — explains what the data means in plain language.

C) Call to action — specifies the recommended next step or decision that the audience should take.

D) Finding — states the specific data-supported observation.

#### Q13 Correct Answer: C

#### Q13 Distractor Analysis

A call to action moves the audience from understanding to decision by naming a concrete recommended action. Context frames the problem but does not prescribe action (A). An insight explains meaning but stops short of directing action (B). A finding states what the data shows but leaves interpretation open (D).

---

### Question 14 (5 points)

A bubble chart is used to show the relationship between three variables: ad spend (x-axis), sales revenue (y-axis), and campaign reach (bubble size). If a fourth variable — profit margin — needs to be added, which encoding technique is most appropriate?

A) Add profit margin as a second bubble size using a dashed border.

B) Color the bubbles by profit margin using a sequential color scale.

C) Replace the y-axis with profit margin and move sales revenue to bubble size.

D) Add a fourth axis perpendicular to the chart plane.

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

Color encoding with a sequential scale (e.g., light = low margin, dark = high margin) is the standard method for adding a fourth continuous variable to a bubble chart without distorting the spatial or size dimensions. Using two bubble sizes (A) is visually ambiguous and confusing. Replacing the y-axis (C) removes sales revenue, losing information. A fourth axis (D) is not a supported chart encoding in standard 2D visualization.

---

### Question 15 (5 points)

An analyst builds a Power BI dashboard with 8 charts, each using a different color scheme. A design consultant recommends reducing this to a single 3-color palette. Which design principle does the current dashboard violate?

A) Removing chart junk — the extra colors are unnecessary decorations.

B) Consistent color encoding — inconsistent palettes prevent viewers from building a mental model of what each color means.

C) Single audience, single purpose — different color schemes suggest the dashboard serves multiple users.

D) Limiting KPI count — color variety correlates with too many metrics.

#### Q15 Correct Answer: B

#### Q15 Distractor Analysis

Using a different color scheme for each chart prevents viewers from using color as a consistent signal across the dashboard. A consistent palette allows colors to carry meaning (e.g., blue = actual, orange = target) throughout. A is about removing visual clutter, not color inconsistency. C is about audience scope. D is about metric quantity, not color encoding.

---

### Question 16 (5 points)

A report shows customer satisfaction scores as a bar chart. A colleague adds 3D effects, a gradient background, and drop shadows to make the bars "pop." Which design principle is violated?

A) Limiting KPI count — decorative effects inflate the number of visible metrics.

B) Consistent color encoding — gradients create multiple color meanings within a single bar.

C) Remove chart junk — decorative elements that do not represent data should be removed because they increase cognitive load without adding information.

D) Single audience — 3D effects are appropriate only for technical audiences.

#### Q16 Correct Answer: C

#### Q16 Distractor Analysis

3D effects, gradient fills, and drop shadows are classic "chart junk" — visual elements that add visual complexity without encoding any data. They distort perception of bar heights and slow comprehension. A is about KPI quantity. B is about color meaning consistency, not gradient fills. D is incorrect; chart junk is inappropriate for all audiences.

---

### Question 17 (5 points)

A BI tool uses "row-level security" (RLS). What does this feature control?

A) It limits which charts a user can view based on their job title.

B) It restricts which rows of data a user can see based on their identity, ensuring that a regional manager sees only their region's data.

C) It prevents users from exporting data to Excel or CSV.

D) It controls how frequently each user's dashboard refreshes.

#### Q17 Correct Answer: B

#### Q17 Distractor Analysis

Row-level security filters which database rows a user can access based on their identity (e.g., a manager in the West region only sees West region data). It is a data access control mechanism, not a UI or refresh control. A describes feature-level access, not row-level data filtering. C describes export restrictions, which is a separate permission setting. D describes refresh scheduling, unrelated to RLS.

---

### Question 18 (5 points)

Which of the following best describes a lagging indicator?

A) A metric that predicts future outcomes and can be acted on before the outcome occurs.

B) A metric that measures outcomes or events that have already happened, such as last quarter's revenue or last month's customer churn rate.

C) A metric whose data is delayed by 30 or more days due to reporting system latency.

D) A metric used exclusively in financial reporting and not applicable to operational dashboards.

#### Q18 Correct Answer: B

#### Q18 Distractor Analysis

A lagging indicator measures results that have already occurred — it confirms whether goals were achieved after the fact. A describes a leading indicator (predictive and actionable). C confuses reporting latency (a technical delay) with the strategic concept of lagging vs. leading. D is incorrect; lagging indicators appear in all domains, including operations, HR, and marketing.

---

### Question 19 (5 points)

A dashboard filter allows users to select a date range and all charts update accordingly. This capability is an example of which dashboard feature?

A) Drill-through — navigating from a summary view to a detailed sub-report.

B) Bookmarks — saving a specific combination of filter states for quick navigation.

C) Interactivity (cross-filtering / slicers) — user-controlled filters that dynamically update all connected visualizations.

D) Scheduled refresh — automatic background data updates on a defined cadence.

#### Q19 Correct Answer: C

#### Q19 Distractor Analysis

A date range selector that updates all charts simultaneously is a slicer or cross-filter — the core interactive element of modern BI dashboards. Drill-through navigates to a new report page or view with more detail (A). Bookmarks save pre-configured view states (B). Scheduled refresh controls when new data is pulled from the source, not user-driven visual filtering (D).

---

### Question 20 (5 points)

An organization's sales dashboard shows revenue is 15% below target. The executive audience immediately asks "why?" The dashboard cannot answer this question. What type of analytics capability is missing?

A) Descriptive analytics — the ability to report what happened.

B) Diagnostic analytics — the ability to explain why something happened by supporting drill-down and root-cause investigation.

C) Predictive analytics — the ability to forecast whether the shortfall will continue next quarter.

D) Prescriptive analytics — the ability to recommend corrective actions the sales team should take.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

When a dashboard shows a performance gap but cannot explain the cause, it provides descriptive (what happened) output but lacks diagnostic capability (why it happened). Diagnostic analytics enables investigation through drill-downs, segmentation, and root-cause views. A is what the dashboard already provides (the metric). C is about forecasting, not explaining the current gap. D is about recommending actions, which requires the diagnosis first.

---

### Answer Key

| Question | Correct Answer |
|---|---|
| 1 | B |
| 2 | D |
| 3 | C |
| 4 | C |
| 5 | C |
| 6 | C |
| 7 | B |
| 8 | C |
| 9 | B |
| 10 | D |
| 11 | B |
| 12 | B |
| 13 | C |
| 14 | B |
| 15 | B |
| 16 | C |
| 17 | B |
| 18 | B |
| 19 | C |
| 20 | B |

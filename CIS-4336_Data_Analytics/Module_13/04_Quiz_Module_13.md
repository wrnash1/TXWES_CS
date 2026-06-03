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

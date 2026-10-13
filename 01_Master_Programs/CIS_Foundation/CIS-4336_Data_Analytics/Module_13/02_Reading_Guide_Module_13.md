# Reading Guide: Module 13 — Reporting and Dashboard Design

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4336 &BULL; DATA ANALYTICS & BUSINESS INTELLIGENCE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

---

### Introduction

Welcome to **Module 13 — Reporting and Dashboard Design**. Data analysis produces value only when findings reach decision-makers in a form they can understand and act on. This module bridges the technical work of Modules 11 and 12 with the communication skills that define a professional analyst. You will learn how business intelligence platforms work, how to design dashboards that serve their audience, how to select meaningful KPIs, and how to structure data-driven narratives for different stakeholder types.

The CompTIA Data+ exam allocates approximately 20–24% of its questions to Domain 4, Data Visualization. This is the largest single domain. Understanding dashboard design principles, chart selection, and KPI definitions is not optional preparation — it is the core of the exam.

---

### Learning Objectives

By the end of this module you will be able to:

* Compare Tableau, Power BI, and Looker on architecture, use case, and deployment model
* Apply five dashboard design principles to evaluate and improve a dashboard
* Distinguish between a metric, a KPI, and a benchmark
* Select the appropriate chart type for a given data relationship and audience
* Structure a data finding as a four-part narrative: context, finding, evidence, implication
* Match communication format and detail level to stakeholder role

---

### Section 1: Business Intelligence Platforms

#### What Is a BI Platform?

A business intelligence platform is a software environment that connects to data sources, transforms and models that data, and enables users to create visualizations, reports, and dashboards without writing SQL or code for every request. Modern BI platforms sit between the raw data store (database, data warehouse, or data lake) and the business user.

The core components of a BI platform are:

* A data connector layer that queries databases, APIs, flat files, and cloud services
* A semantic model that maps raw tables and columns to business-friendly names and calculated measures
* A visualization layer where users build charts and dashboards
* A distribution layer for publishing and sharing content with controlled access

#### Tableau

Tableau was founded in 2003 and acquired by Salesforce in 2019. Its core product is Tableau Desktop, a Windows and macOS application that uses a drag-and-drop canvas called a workbook. Users connect to data sources, build visualizations on sheets, and combine sheets into dashboards.

Key Tableau concepts for the Data+ exam:

* **Dimension** — a categorical field used for grouping (Region, Product, Date)
* **Measure** — a numeric field used for aggregation (Revenue, Units, Profit)
* **Calculated field** — a custom formula added to a data source
* **Tableau Public** — free hosting for public dashboards; no account required to view
* **Tableau Server / Tableau Cloud** — enterprise publishing with access controls

Tableau's strength is speed of visual exploration. Its limitation for organizations is that individual analysts can define the same metric differently, producing inconsistent numbers across teams.

#### Power BI

Power BI is Microsoft's BI platform, available as a free desktop application (Power BI Desktop) and a cloud service (Power BI Service). Its tight integration with Excel means most Excel users can transition to Power BI without learning an entirely new interface.

Key Power BI components:

* **Power Query** — an ETL editor inside Power BI for transforming and shaping data before it reaches the visualization layer
* **Data Model** — a relational model where tables are connected by relationships, similar to a star schema
* **DAX (Data Analysis Expressions)** — a formula language for calculated columns and measures; more powerful than Excel formulas, less flexible than SQL
* **Report** — a collection of visuals on one or more pages
* **Dashboard** — a single-page collection of pinned tiles from one or more reports

Power BI's strength is deep Microsoft ecosystem integration. Its limitation is that DAX has a steep learning curve.

#### Looker

Looker, acquired by Google in 2020, takes a fundamentally different architecture. Instead of each analyst connecting directly to data and building their own calculations, Looker uses **LookML** — a YAML-like modeling language — to define all metrics, dimensions, and relationships in a central Git repository.

Key Looker concepts:

* **LookML model** — defines which database tables exist and how they join
* **Explore** — a self-service query interface where business users build queries from the model
* **Look** — a saved query with a visualization
* **Dashboard** — a collection of Looks or inline tiles
* **Derived table** — a custom SQL query defined in LookML and treated as a virtual table

Looker's strength is metric governance — every team uses the same revenue definition because it is defined once in LookML. Its limitation is that setting up LookML requires technical data modeling expertise.

#### Choosing a BI Tool — Exam Context

For the Data+ exam you will not be tested on tool-specific syntax. You will be asked to identify which type of tool or feature matches a described scenario.

| Scenario | Tool feature |
|---|---|
| Self-service drag-and-drop exploration without writing code | Tableau or Power BI canvas |
| Central metric definitions to prevent inconsistency across teams | Looker LookML |
| Transforming raw data before visualization without a separate ETL tool | Power BI Power Query |
| Publishing a dashboard publicly with no login required | Tableau Public |
| Building reports in an organization standardized on Microsoft Azure | Power BI |

---

### Section 2: Dashboard Design Principles

#### Principle 1 — Single Audience, Single Purpose

A dashboard designed for multiple audiences typically fails all of them. Before designing any dashboard, answer two questions: Who is the primary user? What single question does this dashboard answer? All design decisions flow from those answers.

Executive dashboards answer: "How is the business performing against targets this period?" They use large KPI tiles, trend sparklines, and one or two supporting charts. They do not contain drill-down tables or raw data exports.

Operational dashboards answer: "What needs my attention right now?" They update frequently (hourly or daily), show current-state metrics, and include thresholds that color-code status. They often contain filters for region, team, or product.

Analytical dashboards answer: "Why is this happening?" They are more exploratory, include more charts, and are used by analysts rather than executives.

#### Principle 2 — Limit the KPI Count

Research on working memory (Miller's Law) supports limiting dashboards to five to seven primary KPIs. More than that creates cognitive overload where the viewer cannot identify what is most important. Place the three to five most critical KPIs at the top of the dashboard in large, clearly labeled tiles before any charts appear.

#### Principle 3 — Consistent Color Encoding

Color carries meaning. Establish a color legend and apply it consistently:

* Use green for on-target or positive trend
* Use red for below-target or negative trend
* Use gray or neutral for in-progress or informational
* Use one accent color for the primary data series in charts; use a second only when two series must be compared

Never use the same color to mean two different things in the same dashboard.

#### Principle 4 — Remove Chart Junk

Chart junk is any visual element that does not encode data. Common examples are:

* 3D effects on bar or pie charts (distort proportions)
* Decorative gridlines (replace with subtle gray or remove entirely)
* Redundant legends when direct labels on bars or lines are clearer
* Drop shadows, borders, and gradients on chart backgrounds
* Pie charts with more than five slices (use a bar chart instead)

Every pixel not encoding data is competing with the data for the viewer's attention.

#### Principle 5 — Proximity and Grouping

The Gestalt principle of proximity states that elements placed near each other are perceived as related. Group revenue metrics together, cost metrics together, and customer metrics together. Separate groups with whitespace rather than dividing lines. The eye reads whitespace as a boundary without adding visual clutter.

---

### Section 3: KPIs, Metrics, and Benchmarks

#### Definitions

* **Metric** — any quantitative measurement derived from data. Metrics have no inherent strategic meaning.
* **KPI (Key Performance Indicator)** — a metric that is tied to a specific strategic objective, has a defined target, and has a direction (higher is better or lower is better).
* **Benchmark** — a reference value against which a metric is evaluated. Benchmarks may be internal (last year's value), external (industry average), or aspirational (target).
* **Leading indicator** — a metric that predicts future performance (e.g., new leads added this week predicts sales next month).
* **Lagging indicator** — a metric that reflects outcomes already achieved (e.g., revenue closed this month).

#### Vanity Metrics vs. Actionable KPIs

A vanity metric looks impressive but does not tell you what to do. An actionable KPI reveals a gap between current state and target that prompts a specific response.

| Vanity metric | Actionable KPI |
|---|---|
| Total page views | Bounce rate by landing page |
| Total registered users | Monthly active users / total registered (activation rate) |
| Total support tickets closed | Average first-response time |
| Total sales calls made | Lead-to-opportunity conversion rate |

#### KPI Properties

A well-defined KPI has:

* A clear name and definition (including which data source and calculation)
* A unit of measurement (dollars, percentage, count, days)
* A target value or range
* A direction (increase is good, decrease is good, maintain range)
* A reporting frequency (daily, weekly, monthly, quarterly)
* An owner (the role responsible for moving this metric)

---

### Section 4: Chart Type Selection

Selecting the right chart type is a core Data+ exam skill. The rule is simple: match the chart to the relationship in the data.

| Relationship | Recommended chart | Avoid |
|---|---|---|
| Trend over time (continuous) | Line chart | Bar chart for many time points |
| Comparison across categories | Bar or column chart | Pie chart for more than 5 categories |
| Part-to-whole (few parts) | Pie or donut chart | Pie chart for more than 5 slices |
| Distribution of one variable | Histogram or box plot | Line chart |
| Relationship between two numeric variables | Scatter plot | Bar chart |
| Geographic distribution | Choropleth map or bubble map | Bar chart (loses geographic context) |
| Correlation matrix | Heatmap | Table of numbers |
| Composition change over time | Stacked area chart | Pie chart |
| Ranking with magnitude | Horizontal bar chart | Vertical bar with many labels |
| Performance vs. target | Bullet chart or gauge | Speedometer (distorts perception) |

---

### Section 5: Data Storytelling

#### The Four-Part Narrative Structure

Professional data communication follows a consistent four-part structure regardless of the format:

1. **Context** — establish what was known before the analysis and what decision depends on the finding
2. **Finding** — state the most important result in one sentence using plain language
3. **Evidence** — present the supporting visualization with annotation pointing to the key data point
4. **Implication** — state what the finding means for the decision at hand

#### Annotation on Charts

A chart without annotation forces the viewer to find the insight themselves. An annotated chart guides them directly to it. Effective annotations:

* Use a callout arrow or circle to point to the key data point
* Include one sentence of plain-language explanation at the annotation location
* Never annotate more than two points per chart — more than two annotations signal that the wrong chart or the wrong data is being shown

#### Avoiding Common Storytelling Errors

* Truncated y-axes that exaggerate small differences
* Dual y-axes that imply a relationship between two unrelated variables
* Cherry-picking the time range to make a trend look better than it is
* Using color to imply causation (red for one series, green for another, when both are neutral)

---

### Section 6: Stakeholder Communication

#### Audience Analysis

Before preparing any report or dashboard, identify:

* The stakeholder's role (executive, manager, analyst, board)
* Their primary question (performance, diagnosis, compliance)
* Their data literacy level (technical, intermediate, non-technical)
* Their preferred format (slide deck, email, live dashboard, printed report)

#### Communication Format by Role

| Role | Format | Detail level | Update frequency |
|---|---|---|---|
| Board / C-suite | Single slide or one-pager | 3–5 KPIs, no raw data | Monthly or quarterly |
| VP / Director | Dashboard with filters | 10–15 KPIs, summary tables | Weekly or daily |
| Manager | Operational dashboard | Full detail with drill-down | Daily or real-time |
| Analyst | Report with data export | All columns, full history | On demand |

#### Data Definitions and Transparency

Always include a footnote or tooltip that defines how each metric is calculated. Ambiguous metric names — "revenue," "active users," "cost" — mean different things in different departments. A data definition prevents the meeting where two people argue about whose number is right and neither is wrong; they are just measuring different things.

---

### Key Terms

* **business intelligence (BI)** — the technologies, processes, and practices for collecting, integrating, analyzing, and presenting business data to support decision-making.
* **KPI (Key Performance Indicator)** — a metric tied to a strategic objective with a defined target and direction.
* **metric** — any quantitative measurement; not all metrics are KPIs.
* **benchmark** — a reference value against which a metric is evaluated; may be internal or external.
* **vanity metric** — a measurement that looks impressive but does not drive actionable decisions.
* **leading indicator** — a metric that predicts future performance.
* **lagging indicator** — a metric that reflects outcomes already achieved.
* **chart junk** — visual elements on a chart that do not encode data and reduce clarity.
* **LookML** — Looker's YAML-based modeling language for defining metrics centrally.
* **DAX (Data Analysis Expressions)** — Power BI's formula language for calculated measures.
* **data storytelling** — combining data, visualization, and narrative to communicate findings that drive action.
* **annotation** — text or a graphic element added to a chart to highlight a key data point.
* **choropleth map** — a map in which geographic regions are shaded in proportion to a data value.

---

### Review Questions

1. What is the difference between a metric, a KPI, and a benchmark? Give one example of each.

2. A colleague wants to show quarterly revenue for 12 product categories over four years. They propose a pie chart. What would you recommend instead and why?

3. Explain Looker's LookML approach and why it addresses a limitation of tools like Tableau.

4. You are building a dashboard for a Chief Operating Officer. What are the three design decisions you would make first?

5. What is the four-part narrative structure for data storytelling? Give a brief example applying it to a real business scenario.

---

### OER Resources

* **Storytelling with Data (free blog and examples)** — [storytellingwithdata.com](https://www.storytellingwithdata.com/)
* **Tableau Public Gallery** — [public.tableau.com/gallery](https://public.tableau.com/en-us/gallery/)
* **Microsoft Power BI documentation** — [learn.microsoft.com/power-bi](https://learn.microsoft.com/en-us/power-bi/)
* **Google Looker documentation** — [cloud.google.com/looker/docs](https://cloud.google.com/looker/docs)
* **DataViz Project — chart type reference** — [datavizproject.com](https://datavizproject.com/)

---

## 9. Supplemental Resources

**1. Storytelling with Data — Chart Guide**
<https://www.storytellingwithdata.com/chart-guide>
Cole Nussbaumer Knaflic's free chart selection guide covering when to use each chart type, how to eliminate chart junk, and how to direct audience attention. Directly reinforces the visualization selection and dashboard design principles in Module 13 and the Data+ Domain 4 exam content.

**2. Google Data Studio (Looker Studio) — Quick Start Guide**
<https://support.google.com/datastudio/answer/6283323>
Google's official quickstart for Looker Studio (formerly Data Studio), a free BI and dashboard tool. Useful for hands-on practice with dashboard layout, KPI tiles, chart types, and filter controls — closely matching the concepts in Module 13 without requiring a paid tool license.

**3. Harvard Business Review — The Art of Data Storytelling**
<https://hbr.org/2013/04/how-to-tell-a-story-with-data>
A practitioner-focused HBR article on structuring data narratives for executive audiences — covering context, insight, and call-to-action framing. Supports the data storytelling and audience communication skills tested in Module 13 and essential for real-world BI analyst roles.

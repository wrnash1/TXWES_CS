# Video Script — Module 07: Data Visualization Principles and Chart Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 4: Visualization

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 07: Data Visualization Principles and Chart Types.

Data visualization is where analysis becomes communication. A technically correct analysis that cannot be understood by its audience has failed. Visualization translates numbers into visual forms that human perception can process rapidly — patterns, comparisons, trends, and outliers become visible in seconds.

By the end of this module, you will be able to:

- Apply the core principles of effective data visualization
- Select the appropriate chart type for a given data scenario
- Identify common visualization mistakes and their consequences
- Distinguish between charts that show comparison, composition, distribution, and relationship
- Apply these concepts to Data+ DA0-001 Domain 4 exam questions

Domain 4 — Visualization — comprises approximately 21 percent of the Data+ exam. It is the largest single domain by weight.

---

## Segment 2 — Core Visualization Principles (3 minutes)

Before choosing a chart type, you need to understand the principles that separate effective visualizations from misleading or confusing ones.

**Principle 1: Match the chart to the analytical question.** The chart type should serve the question being asked. Is the question about trend over time? Comparison between categories? Distribution of values? Relationship between two variables? Each question has a preferred chart family.

**Principle 2: Maximize the data-to-ink ratio.** Edward Tufte's foundational principle states that every drop of ink on a chart should represent data. Remove gridlines that add no value, remove 3D effects that distort perception, remove decorative elements that compete with data.

**Principle 3: Avoid misleading scales.** A y-axis that does not start at zero exaggerates differences between bars. A truncated axis can make a small change look dramatic. Always examine axes before interpreting a chart — and always build your own charts with honest scales.

**Principle 4: Use color purposefully.** Color should encode information, not decorate. Use distinct hues to distinguish categories. Use sequential color scales (light to dark) for numeric magnitude. Use diverging color scales (two-hue gradient through a neutral midpoint) for data that has a meaningful center (like positive vs. negative values).

**Principle 5: Reduce cognitive load.** The reader should not have to work hard to understand your chart. Eliminate legends when you can label data directly. Write a descriptive title that states the main finding, not just the variables. Annotate significant data points.

[SHOW CHART: Side-by-side comparison — a cluttered chart with 3D bars, decorative background, redundant legend, and unlabeled axes on the left; a clean redesigned version of the same data on the right with direct labels, minimal gridlines, and a descriptive title]

---

## Segment 3 — Comparison Charts (3 minutes)

Comparison charts answer the question: how do these values rank relative to each other?

**Bar chart (vertical or horizontal)** is the default choice for comparing values across discrete categories. Vertical bars (column chart) work best when category labels are short. Horizontal bars work best when labels are long.

Key rules for bar charts: always start the y-axis at zero. The length of a bar encodes value — truncating the axis makes small differences appear large.

**Grouped bar chart** compares multiple series across categories side by side. Use when you need to compare two or three metrics across the same categories.

**Stacked bar chart** shows both the total and the composition of each category simultaneously. Use when both part-to-whole and total-to-total comparisons matter.

[SHOW CHART: Three side-by-side examples — simple bar chart for regional revenue, grouped bar chart for revenue by region by year, and stacked bar chart for revenue composition by product category within each region]

---

## Segment 4 — Trend and Time Series Charts (2 minutes)

Time series charts answer the question: how does this value change over time?

**Line chart** is the standard for continuous time series data. Connect measurements chronologically and the slope of the line communicates direction and rate of change. Multiple lines on the same chart compare trends across different groups or metrics.

**Area chart** fills the region beneath the line. Use for emphasizing volume or cumulative magnitude over time. Stacked area charts show composition changing over time.

**Avoid bar charts for time series.** While technically possible, bar charts force the reader to compare bar heights rather than following a continuous line — the line chart is perceptually more efficient for temporal data.

[SHOW CHART: Line chart showing monthly revenue trend over 24 months with annotations marking key business events — product launch, price change, seasonal dip]

---

## Segment 5 — Distribution Charts (2 minutes)

Distribution charts answer the question: how are these values spread across the range?

**Histogram** groups continuous data into equal-width bins and shows frequency per bin. Reveals distribution shape, modality, center, and spread. The bin width choice significantly affects interpretation — too few bins hide detail; too many bins add noise.

**Box plot** displays the five-number summary (minimum, Q1, median, Q3, maximum) and marks outliers beyond 1.5 times IQR. Excellent for comparing distributions across multiple groups on the same chart.

**Violin plot** combines the box plot with a kernel density estimate — showing the full shape of the distribution. More informative than a box plot when distribution shape matters.

[SHOW CHART: Three charts side by side showing the same salary data as a histogram, a box plot, and a violin plot — comparing what each reveals and hides about the distribution]

---

## Segment 6 — Relationship Charts (2 minutes)

Relationship charts answer the question: how do two or more variables co-vary?

**Scatter plot** plots one numeric variable on each axis and one point per observation. Reveals linear or non-linear relationships, clusters, and outliers. The relationship between two variables and the direction and strength of correlation are visually apparent.

**Bubble chart** extends the scatter plot by encoding a third numeric variable as the size (area) of each point. Use sparingly — more than three numeric dimensions create visual complexity that most readers cannot parse.

**Heatmap** displays a matrix of values using color intensity. Useful for correlation matrices, confusion matrices, and geographic grids.

[SHOW CHART: Scatter plot showing training hours vs. sales revenue with a fitted trend line, correlation coefficient annotated, and two labeled outlier points]

---

## Segment 7 — Composition Charts (2 minutes)

Composition charts answer the question: what is the part-to-whole breakdown?

**Pie chart** shows the proportion of each category within a whole. Use only when you have five or fewer categories and the comparison is between individual slices rather than across multiple charts. Humans are poor at estimating angles — avoid pie charts when precise comparison matters.

**Donut chart** is a variation of the pie chart with a hollow center. The center space can display a key metric.

**Treemap** displays hierarchical composition using nested rectangles sized by value. Effective for large numbers of categories.

**Waterfall chart** shows how an initial value is built up or broken down by successive positive and negative contributions. Used for financial analysis (revenue bridge, budget variance).

[SHOW CHART: Side-by-side comparison of the same five-category composition data shown as a pie chart vs. a horizontal bar chart — demonstrating why the bar chart is easier to read for precise comparison]

---

## Segment 8 — Chart Selection Decision Guide (2 minutes)

[SHOW CHART: Chart selection tree — top-level branches: Comparison, Trend over Time, Distribution, Relationship, Composition — each branch leads to two to three recommended chart types with one-line descriptions]

The exam will present a data scenario and ask you to select the most appropriate chart. Apply this decision process:

First, identify what question the chart needs to answer. Then match the question type to the chart family. Then select the specific chart based on the number of variables and the number of categories.

Common exam traps:

- Using a pie chart with many categories — bar chart is better
- Using a bar chart for time series — line chart is better
- Using a line chart for unrelated categories — bar chart is better
- Using a 3D chart of any type — flat versions are always more accurate

---

## Segment 9 — Exam Alignment and Closing (2 minutes)

Module 07 maps to Data+ exam Domain 4 — Visualization — the largest domain at approximately 21 percent of the exam. Expect scenario-based questions that ask you to:

- Select the most appropriate chart type for a described dataset and question
- Identify visualization errors that mislead the audience
- Interpret a described visualization and identify what it communicates
- Recognize when a chart's design choices introduce bias or distortion

For exam preparation, review the official objectives at comptia.org and Professor Messer's study materials at professormesser.com.

Your Module 07 assignments:

- Complete the Reading Guide — focus on the chart selection guide and the visualization mistakes reference
- Complete Lab 07 — you will match five data scenarios to chart types and justify each selection
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

See you in Module 08, where we cover business intelligence tools including Power BI and Tableau.

---

End of Module 07 Video Script — Estimated runtime: 22 minutes

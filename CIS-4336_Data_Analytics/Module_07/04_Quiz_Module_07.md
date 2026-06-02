# Quiz — Module 07: Data Visualization Principles and Chart Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 4: Visualization

---

## Question 1

An analyst needs to show how total monthly website traffic has changed over the past 18 months. Which chart type is most appropriate?

- A) Pie chart
- B) Bar chart with one bar per month
- C) Line chart with months on the x-axis
- D) Scatter plot with months on the x-axis

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A line chart is the standard visualization for continuous time series data. The connected line makes trend direction and rate of change immediately apparent. The x-axis represents ordered time, and the line visually connects each month's value to show the trajectory.
- **Why A is incorrect:** A pie chart shows part-to-whole composition at a single point in time. It cannot represent change over time.
- **Why B is incorrect:** A bar chart for monthly time series forces the reader to compare bar heights rather than following a continuous line. While it technically works, a line chart is perceptually more efficient for trend data and is the professional standard for time series.
- **Why D is incorrect:** A scatter plot shows the relationship between two continuous numeric variables. Months are not a second numeric variable — they are an ordered time sequence. Using a scatter plot would not connect the dots and would not convey the trend.

---

## Question 2

A manager creates a bar chart comparing four departments' annual budgets. The y-axis runs from $900,000 to $1,100,000. The tallest bar appears to be twice the height of the shortest, suggesting one department has twice the budget. The actual values are: Dept A $1,080,000; Dept B $980,000; Dept C $1,040,000; Dept D $995,000. What is wrong with this chart?

- A) The bar chart is the wrong chart type for this data
- B) The truncated y-axis that does not start at zero exaggerates the differences between departments
- C) There are too many departments for a bar chart
- D) The bars should be horizontal for this type of comparison

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The y-axis starting at $900,000 instead of zero makes the visual height differences between bars appear proportionally much larger than the actual numerical differences. A $100,000 difference on a truncated axis looks like a 100% difference, when it is actually less than 10%.
- **Why A is incorrect:** Bar chart is the correct chart type for comparing values across discrete categories. The problem is the scale, not the chart type.
- **Why C is incorrect:** Four departments is a reasonable number for a bar chart. The chart type is appropriate; the axis is the problem.
- **Why D is incorrect:** Horizontal bars are preferred when category labels are long. For short department names, vertical bars are fine. The orientation does not fix the truncated axis problem.

---

## Question 3

An analyst wants to show how annual revenue is split among five business units. Which chart type is most appropriate for this part-to-whole comparison?

- A) Line chart
- B) Scatter plot
- C) Histogram
- D) Pie chart or stacked bar chart

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** Both pie charts and stacked bar charts are designed for part-to-whole composition. With five categories, either works. A stacked bar chart is generally preferred when precise comparison between parts matters; a pie chart is acceptable when approximate proportions are sufficient.
- **Why A is incorrect:** A line chart shows trends over time. It does not represent part-to-whole composition at a single point in time.
- **Why B is incorrect:** A scatter plot shows the relationship between two numeric variables. It does not represent proportional composition.
- **Why C is incorrect:** A histogram shows the frequency distribution of a continuous numeric variable. It does not show composition across named categories.

---

## Question 4

An analyst wants to compare the salary distributions of four departments simultaneously, specifically to show median, spread, and outliers for each group. Which chart type is most appropriate?

- A) Line chart with one line per department
- B) Pie chart with one slice per department
- C) Box plot with one box per department
- D) Bar chart with one bar per department showing mean salary

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A box plot directly encodes the five-number summary (minimum, Q1, median, Q3, maximum) and marks outliers beyond 1.5 times IQR. When the requirement is specifically to show distribution shape, spread, and outliers across multiple groups, box plot is the correct tool.
- **Why A is incorrect:** A line chart implies ordered sequence or trend over time. Salary values for four departments are not an ordered sequence — they are independent distributions.
- **Why B is incorrect:** A pie chart shows proportional composition of a whole. It cannot represent the distribution shape, median, or spread within each department.
- **Why D is incorrect:** A bar chart showing mean salary communicates only one summary statistic per department. It hides the spread, the presence of outliers, and the shape of the distribution — exactly the information the requirement specifies.

---

## Question 5

Which of the following is the BEST example of applying the data-to-ink ratio principle?

- A) Adding a colorful gradient background to make the chart more visually appealing
- B) Adding a 3D effect to bars to give the chart depth
- C) Removing gridlines that do not help the reader interpret values
- D) Adding a legend in addition to direct labels already placed on each data point

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The data-to-ink ratio principle (Tufte) states that every mark on a chart should represent data. Gridlines that do not aid interpretation are non-data ink and should be removed or minimized.
- **Why A is incorrect:** A gradient background is decorative — it adds ink without adding data. This directly violates the data-to-ink ratio principle.
- **Why B is incorrect:** 3D effects add visual complexity and can distort bar heights through perspective. They reduce accuracy and add non-data visual elements — the opposite of the data-to-ink principle.
- **Why D is incorrect:** If data points already have direct labels, adding a separate legend creates redundant ink encoding the same information twice. The data-to-ink principle recommends direct labeling instead of legends when possible, not both simultaneously.

---

## Question 6

An analyst creates a scatter plot to show the relationship between customer age and annual purchase amount. The chart shows a moderate positive trend. A colleague argues this proves that older customers spend more money. What is wrong with this reasoning?

- A) Scatter plots cannot show the relationship between age and purchase amount
- B) A moderate correlation suggests no relationship exists
- C) Correlation in a scatter plot does not establish causation — a confounding variable may explain the pattern
- D) Scatter plots require both axes to start at zero

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A scatter plot shows that two variables co-vary, not that one causes the other. Older customers may have higher income (a confounding variable), which drives higher spending. The correlation is real but the causal mechanism requires further investigation.
- **Why A is incorrect:** Scatter plots are specifically designed to show the relationship between two numeric variables. Age and purchase amount are both numeric — a scatter plot is the correct tool.
- **Why B is incorrect:** A moderate correlation does indicate a relationship. The issue is not the presence of a relationship but the interpretation of that relationship as causal.
- **Why D is incorrect:** Scatter plots do not require axes to start at zero. The zero-start rule applies primarily to bar charts where bar length encodes value. Scatter plot axes are typically set to show the range of the data clearly.

---

## Question 7

A pie chart has 11 slices for 11 different website traffic sources. What is the primary problem with this visualization?

- A) Pie charts should never be used for website traffic data
- B) Humans cannot accurately compare angles or areas for 11 slices, making the chart difficult to interpret
- C) The correct chart for 11 categories is always a line chart
- D) Pie charts require a minimum of 15 slices to be meaningful

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Human visual perception is poor at comparing angles and arc lengths, especially among many similarly-sized slices. With 11 slices, many will be small and nearly indistinguishable. A horizontal bar chart sorted by value would convey the same information far more clearly.
- **Why A is incorrect:** Pie charts can be used appropriately for website traffic data when there are few categories (5 or fewer) with meaningfully different proportions.
- **Why C is incorrect:** A line chart is for trends over time or ordered sequences. It is not appropriate for showing the distribution of traffic sources — a bar chart is the correct alternative to an overcrowded pie chart.
- **Why D is incorrect:** There is no minimum slice requirement for pie charts. The recommendation is a maximum of roughly five to six slices for readability.

---

## Question 8

When encoding numeric magnitude on a heatmap or choropleth map (geographic heatmap), which color scale is most appropriate?

- A) Qualitative color scale with 10 distinct unrelated hues
- B) Sequential color scale from light to dark using a single hue
- C) Diverging color scale with equal brightness on both ends
- D) Random colors with no systematic relationship to value

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A sequential color scale (single hue, light to dark) encodes numeric magnitude clearly — lighter shades represent smaller values and darker shades represent larger values. This creates an intuitive visual ordering that matches how humans perceive luminance.
- **Why A is incorrect:** A qualitative color scale uses distinct unrelated hues to distinguish categories with no order. It is appropriate for nominal categorical data, not numeric magnitude.
- **Why C is incorrect:** A diverging color scale is appropriate when data has a meaningful center point (like zero, or a target value) and values diverge in two directions from it. It is not appropriate for monotonically increasing magnitude with no meaningful midpoint.
- **Why D is incorrect:** Random colors with no relationship to value create visual noise and prevent any meaningful interpretation of the heatmap. Color encoding must be systematic.

---

## Question 9

Which chart type is specifically designed to show how a starting value changes through a series of positive and negative contributions to reach a final value?

- A) Stacked area chart
- B) Bubble chart
- C) Waterfall chart
- D) Grouped bar chart

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A waterfall chart shows an initial value (e.g., starting revenue), then a series of bars extending up (positive contributions) or down (negative contributions), ending at a final value. It is specifically designed for financial bridge analysis, budget variance, and sequential change decomposition.
- **Why A is incorrect:** A stacked area chart shows how composition changes over time across multiple continuous series. It does not show a sequential build-up or break-down of a single starting value.
- **Why B is incorrect:** A bubble chart extends a scatter plot by encoding a third variable as point size. It shows the relationship between three variables, not sequential contributions to a total.
- **Why D is incorrect:** A grouped bar chart compares multiple series across categories side by side. It does not show how one value builds up or breaks down through sequential contributions.

---

## Question 10

An analyst is choosing between a histogram and a box plot to show the distribution of response times for a customer support system. The analyst needs to show both the distribution shape AND compare it across three different support tiers simultaneously. Which chart type is most appropriate?

- A) Three separate histograms, one per tier, on separate pages
- B) A pie chart with one slice per tier
- C) Three box plots displayed side by side on the same chart
- D) A single line chart with three lines showing response time trends

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Side-by-side box plots are the standard tool for comparing distributions across multiple groups simultaneously. They efficiently show median, spread (IQR), range, and outliers for all three tiers on the same scale, enabling direct visual comparison.
- **Why A is incorrect:** Three separate histograms on separate pages make direct visual comparison very difficult — the reader must mentally hold each chart to compare them. Placing them side-by-side on the same chart would improve this, but box plots remain the more compact and efficient solution for distribution comparison.
- **Why B is incorrect:** A pie chart shows part-to-whole composition. It cannot represent the distribution shape or spread of a continuous variable like response time.
- **Why D is incorrect:** A line chart with three lines shows trends over time or ordered sequences. Response time distribution across three support tiers is not a time series — it requires a distribution chart.

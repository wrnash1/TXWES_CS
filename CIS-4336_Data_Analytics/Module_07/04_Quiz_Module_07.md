# Quiz: Module 07 - Data Visualization Principles and Chart Types
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
An analyst wants to show how a company's monthly revenue has changed over the past two years. Which chart type is most appropriate?
*   A) Pie chart, because revenue slices add up to the annual total.
*   B) Scatter plot, because revenue and time are two numeric variables.
*   C) Line chart, because it is designed to show trends and change over a continuous time axis.
*   D) Box plot, because it summarizes the distribution of monthly revenue values.
*   **Correct Answer:** C) Line chart, because it is designed to show trends and change over a continuous time axis.
*   **Distractor Analysis:**
    *   *Why correct:* Line charts connect data points in time order, making upward and downward trends immediately visible. They are the standard chart for any "over time" analytical question.
    *   A pie chart shows proportions of a whole at a single point in time, not change over time. B) A scatter plot is used to reveal correlation between two independent numeric variables, not sequential time-series data. D) A box plot shows the distribution (spread, median, outliers) of a set of values but does not convey temporal sequence.

---

**Question 2**
In data visualization, which of the following most accurately defines a **scatter plot**?
*   A) A chart that uses rectangular bars of varying height or length to compare discrete categorical values, where the length of each bar encodes its quantity.
*   B) A chart that plots individual observations as points on two numeric axes to reveal the direction and strength of the relationship between two continuous variables.
*   C) A circular chart divided into proportional slices where each slice represents a category's share of a total, useful when parts sum to 100%.
*   D) A chart that connects sequential data points with a line to display how a numeric value changes over a continuous axis such as time.
*   **Correct Answer:** B) A chart that plots individual observations as points on two numeric axes to reveal the direction and strength of the relationship between two continuous variables.
*   **Distractor Analysis:**
    *   *Why B is correct:* A scatter plot's defining purpose is correlation analysis — each point represents one observation plotted by two numeric dimensions, making patterns (positive, negative, or no correlation) visible.
    *   *Why A is incorrect:* Rectangular bars comparing categories describes a bar chart, not a scatter plot.
    *   *Why C is incorrect:* Proportional slices summing to 100% describes a pie chart, not a scatter plot.
    *   *Why D is incorrect:* Connecting sequential points to show change over time describes a line chart, not a scatter plot.

---

**Question 3**
A data analyst creates a bar chart showing customer satisfaction scores by support tier. The y-axis starts at 92 instead of 0. A manager reviewing the chart believes Tier 3 is performing dramatically worse than Tier 1. What is the visualization problem?
*   A) The wrong chart type was selected — a pie chart would show the differences more clearly.
*   B) The y-axis is truncated, which exaggerates small differences and makes them appear far larger than they are.
*   C) The chart has too many categories; satisfaction scores should only be visualized using a line chart.
*   D) The bar chart colors are inconsistent, which is causing the manager to misread the data.
*   **Correct Answer:** B) The y-axis is truncated, which exaggerates small differences and makes them appear far larger than they are.
*   **Distractor Analysis:**
    *   *Why B is correct:* When a bar chart's y-axis starts above zero, even a 1-point difference can look like a massive gap. The visual height of the bars no longer represents true proportion, misleading the viewer about the magnitude of the difference.
    *   *Why A is incorrect:* A pie chart is for part-to-whole proportions, not for comparing values across categories. Switching to a pie chart would not fix the misleading axis.
    *   *Why C is incorrect:* There is no rule limiting bar charts to a specific number of categories for satisfaction scores. The problem is the axis, not the chart type.
    *   *Why D is incorrect:* Color inconsistency can reduce clarity, but it is not what causes a viewer to believe large differences exist where small ones do — that is caused by the truncated axis.

---

**Question 4**
An analyst needs to compare the distribution of delivery times across three shipping carriers — including median, spread, and any outliers — in a single chart. Which chart type is most appropriate?
*   A) A grouped bar chart showing average delivery time per carrier.
*   B) A pie chart showing each carrier's share of total deliveries.
*   C) A line chart with one line per carrier showing delivery times over the year.
*   D) A box-and-whisker plot with one box per carrier, showing median, IQR, and outliers.
*   **Correct Answer:** D) A box-and-whisker plot with one box per carrier, showing median, IQR, and outliers.
*   **Distractor Analysis:**
    *   *Why D is correct:* A box plot displays the five-number summary (min, Q1, median, Q3, max) and marks individual outliers, making it ideal for comparing distributions across multiple groups simultaneously.
    *   *Why A is incorrect:* A grouped bar chart showing only the average hides the spread and outliers — two carriers could have the same mean delivery time but very different variability.
    *   *Why B is incorrect:* A pie chart shows proportions of a whole, not distributions of a numeric variable. It cannot convey median or spread.
    *   *Why C is incorrect:* A line chart shows a value changing over time. It does not summarize the distribution of delivery times or highlight outliers across carriers.

---

**Question 5**
A dashboard pie chart has 14 slices representing different product subcategories, with 9 of the slices each accounting for less than 3% of total sales. A stakeholder says the chart is hard to read. What is the best remediation?
*   A) Add a legend with a color key to help the viewer match each slice to its label.
*   B) Replace the pie chart with a horizontal bar chart sorted by sales value, grouping small categories into an "Other" segment.
*   C) Increase the chart size so all 14 slices are visually distinct and easier to compare.
*   D) Switch to a scatter plot to show the correlation between subcategory count and sales volume.
*   **Correct Answer:** B) Replace the pie chart with a horizontal bar chart sorted by sales value, grouping small categories into an "Other" segment.
*   **Distractor Analysis:**
    *   *Why B is correct:* Pie charts with many small, similarly-sized slices are fundamentally difficult to read because humans cannot accurately judge angles. A sorted bar chart makes magnitude comparisons straightforward, and grouping tiny slices into "Other" reduces noise without losing meaningful information.
    *   *Why A is incorrect:* A legend does not fix the core problem — with 14 slices, even a color key requires the viewer to repeatedly look back and forth between the legend and the chart. The issue is the chart type itself.
    *   *Why C is incorrect:* Making the chart larger does not resolve the difficulty of comparing 14 angular slices. The perceptual limitation is inherent to pie charts with many similar-sized segments.
    *   *Why D is incorrect:* A scatter plot is designed to show correlation between two numeric variables. Subcategory proportions of total sales is a part-to-whole problem, not a correlation problem, and a scatter plot would not communicate it effectively.

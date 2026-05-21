# Reading Guide: Module 07 - Data Visualization Principles and Chart Types
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 07 - Data Visualization Principles and Chart Types**! Data visualization transforms raw numbers and tables into visual forms that reveal patterns, trends, and outliers that would be invisible in a spreadsheet. This module covers the chart types and design principles that appear throughout the **CompTIA Data+** exam — knowing when to use a bar chart vs. a line chart vs. a scatter plot, and how to avoid misleading your audience through poor visual choices.

These concepts bridge statistics and communication. An analyst who can compute accurate statistics but cannot present them clearly fails the last step of the analytics workflow. Visualization is also a significant component of the Data+ exam, appearing in both the Analytics and Reporting domain and in scenario questions about interpreting existing charts.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Bar chart**: A chart that uses rectangular bars to compare categorical values, where bar length or height encodes quantity. Bar charts are ideal for comparing discrete categories (e.g., sales by region, headcount by department). Horizontal bar charts are preferred when category labels are long. The y-axis must start at zero to avoid distorting comparisons.
*   **Line chart**: A chart that connects data points with lines to show change over a continuous variable, most commonly time. Line charts are the standard choice for trends — sales over months, temperature over hours. Multiple lines on the same chart allow comparison of trends across groups, but using more than four lines risks visual clutter.
*   **Scatter plot**: A chart that plots individual observations as points using two numeric axes to show the relationship (correlation) between two variables. Scatter plots reveal whether variables are positively correlated, negatively correlated, or uncorrelated. A third variable can be encoded using point size (bubble chart) or color.
*   **Pie chart and its limitations**: A circular chart divided into slices where each slice's angle represents a category's proportion of the whole. Pie charts are only appropriate when the parts sum to a meaningful 100% and there are five or fewer categories. They are difficult to read when slices are similar in size — bar charts almost always communicate proportions more clearly.
*   **Box-and-whisker plot (box plot)**: A chart that displays a five-number summary (minimum, Q1, median, Q3, maximum) and marks outliers as individual points beyond the whiskers. Box plots are ideal for comparing distributions across groups, revealing skewness, and identifying outliers at a glance — information that a bar chart showing only the mean cannot convey.
*   **Color, labeling, and chart design best practices**: Effective charts use color purposefully — to encode a data dimension or draw attention, not for decoration. Axis labels and titles must be present and descriptive. Gridlines should be subtle. Direct labels on data points reduce the need for a legend. Truncating the y-axis (not starting at zero on a bar chart) is a common misleading practice that exaggerates differences.

---

### 2. Certification Exam Tips
*   **Domain weight:** Data visualization and reporting questions appear in Domain 4 (Analytics and Reporting, ~23%) of the Data+ DA0-001 exam. Chart selection and chart interpretation scenarios are high-frequency question types.
*   **Exam trap — choosing the wrong chart type:** The exam will describe an analytical goal and ask which chart type is most appropriate. Key rules: use a line chart for trends over time; use a bar chart to compare categories; use a scatter plot to show correlation between two numeric variables; use a pie chart only for part-to-whole proportions with few categories. If you see "over time," the answer is almost always a line chart.
*   **Exam trap — pie chart misuse:** A pie chart with 10+ slices or where categories do not sum to a meaningful whole is a poor visualization choice. The exam tests whether you recognize this. A stacked bar chart is usually the better alternative for multi-category proportions.
*   **Exam trap — truncated y-axis:** A bar chart whose y-axis starts at a value other than zero makes small differences look large. The exam may show a chart and ask what makes it misleading — truncated axis is a top answer.
*   **Exam trap — scatter plot interpretation:** A scatter plot showing points trending upward from left to right indicates a positive correlation. Points trending downward indicate negative correlation. Widely dispersed points with no direction indicate no correlation. Do not confuse correlation with causation — the exam tests this distinction explicitly.
*   **Study Resource:** The visualization chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) demonstrate constructing and interpreting bar charts, histograms, box plots, and scatter plots using ggplot2 with extensive visual examples. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) covers building these same chart types using Matplotlib and Seaborn with real datasets.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the data visualization chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on the sections covering principles of good visualization, chart type selection, and distribution plots including histograms and box plots.
*   **Required Video:** Watch the data visualization sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates creating and customizing charts using Matplotlib and Seaborn in Python.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Build a bar chart comparing sales by product category**: Label axes, add a title, and verify the y-axis starts at zero. Identify which category has the highest and lowest values.
*   **Create a line chart of monthly revenue over a 12-month period**: Annotate the peak and trough months and explain what trend the chart reveals.
*   **Produce a scatter plot of advertising spend vs. revenue**: Describe the direction and strength of the correlation visible in the plot and note any apparent outliers.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data visualization chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.

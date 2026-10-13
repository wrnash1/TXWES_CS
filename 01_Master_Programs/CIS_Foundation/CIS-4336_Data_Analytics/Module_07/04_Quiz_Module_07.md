# Quiz: Module 07 — Statistical Analysis and Visualization

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 20 (2 points each)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Instructions

Select the single best answer for each question. Each question is worth 2 points. No partial credit.

---

## Question 1

A dataset of annual salaries contains values ranging from $35,000 to $2,400,000. A few executives earn far more than the rest of the workforce. Which measure of central tendency best represents the typical salary?

A. Mean

B. Median

C. Mode

D. Range

**Correct Answer:** B — The median is resistant to outliers and reflects the center of the actual distribution. The mean is pulled upward by extreme executive salaries (A). Mode identifies the most frequent value, not the center (C). Range is a measure of spread, not central tendency (D).

---

## Question 2

For a normally distributed dataset with a mean of 100 and a standard deviation of 15, approximately what percentage of values fall between 70 and 130?

A. 68%

B. 90%

C. 95%

D. 99.7%

**Correct Answer:** C — 70 to 130 spans mean ± 2 standard deviations (100 ± 30), covering approximately 95% by the empirical rule. 68% covers ± 1 SD (A). 90% is not a standard empirical rule threshold (B). 99.7% covers ± 3 SD (D).

---

## Question 3

A data analyst calculates the Pearson correlation coefficient between hours studied and exam score and obtains `r = 0.84`. How should this be interpreted?

A. Hours studied causes higher exam scores

B. There is a strong positive linear relationship between hours studied and exam scores

C. There is a weak positive linear relationship between the two variables

D. The two variables are perfectly correlated

**Correct Answer:** B — `r = 0.84` falls in the 0.7–0.9 range, indicating a strong positive linear relationship. Correlation does not establish causation (A). A value of 0.84 is strong, not weak (C). Perfect correlation requires `r = 1.0` (D).

---

## Question 4

Which formula correctly calculates sample variance for a dataset?

A. `variance = sum((x - mean)^2) / n`

B. `variance = sum((x - mean)^2) / (n - 1)`

C. `variance = sum(x - mean) / n`

D. `variance = sqrt(sum((x - mean)^2) / n)`

**Correct Answer:** B — Sample variance divides by `n - 1` (Bessel's correction) to produce an unbiased estimate. Dividing by `n` gives biased population variance (A). Without squaring, positive and negative deviations cancel to zero (C). Taking the square root produces standard deviation, not variance (D).

---

## Question 5

A dataset has Q1 = 40 and Q3 = 70. What is the upper outlier fence using the standard IQR rule?

A. 75

B. 85

C. 105

D. 115

**Correct Answer:** D — `IQR = 70 - 40 = 30`. `Upper fence = Q3 + (1.5 × IQR) = 70 + 45 = 115`. Options A and B do not apply the correct IQR multiplier. Option C incorrectly adds 1.5 × IQR to Q1 rather than Q3.

---

## Question 6

An analyst wants to show how the proportion of sales contributed by each product category changes across four regions. Which chart type is most appropriate?

A. Scatter plot

B. Line chart

C. Stacked bar chart

D. Histogram

**Correct Answer:** C — A stacked bar chart shows each category's proportional contribution within each group. Scatter plots show relationships between two continuous variables (A). Line charts are best for trends over time (B). Histograms show the frequency distribution of a single continuous variable (D).

---

## Question 7

Which of the following best describes skewness in a dataset?

A. The distance between the minimum and maximum values

B. The degree to which a distribution deviates from symmetry

C. The percentage of values within two standard deviations of the mean

D. The strength of the linear relationship between two variables

**Correct Answer:** B — Skewness measures asymmetry, indicating whether one tail is longer than the other. The min-to-max distance is the range (A). The percentage within ± 2 SD describes the empirical rule (C). The strength of a linear relationship is described by the Pearson correlation coefficient (D).

---

## Question 8

A data analyst creates a chart where each point represents one customer, plotted by age (x-axis) and annual spending (y-axis). What type of chart is this?

A. Bar chart

B. Histogram

C. Scatter plot

D. Line chart

**Correct Answer:** C — A scatter plot places each observation as a point defined by two continuous variable values. Bar charts compare discrete categories (A). Histograms show the frequency distribution of one variable (B). Line charts connect ordered time-series points (D).

---

## Question 9

A dataset has a mean of 200 and a standard deviation of 25. According to the empirical rule, approximately what percentage of values fall above 250?

A. 2.5%

B. 5%

C. 16%

D. 32%

**Correct Answer:** A — 250 equals mean + 2 SD. The empirical rule places 5% total outside ± 2 SD; the upper tail alone holds approximately 2.5%. The 5% figure covers both tails combined (B). 16% is the upper tail beyond ± 1 SD (C). 32% is the total outside ± 1 SD in both tails (D).

---

## Question 10

Which correlation coefficient indicates the weakest linear relationship between two variables?

A. `r = -0.91`

B. `r = 0.65`

C. `r = -0.18`

D. `r = 0.77`

**Correct Answer:** C — `|r| = 0.18` is the smallest absolute value, indicating a negligible linear relationship. `r = -0.91` is very strong negative (A). `r = 0.65` is moderate positive (B). `r = 0.77` is strong positive (D).

---

---

## Question 11 (5 points)

A dataset has a mean of 80 and a standard deviation of 10. According to the empirical rule, approximately what percentage of values fall between 60 and 100?

A. 68%

B. 80%

C. 95%

D. 99.7%

**Correct Answer:** C — 60 to 100 is mean ± 2 standard deviations (80 ± 20), which covers approximately 95% of values by the empirical rule. 68% covers ± 1 SD (A). 80% is not a standard empirical rule threshold (B). 99.7% covers ± 3 SD (D).

---

## Question 12 (5 points)

An analyst computes the Spearman rank correlation instead of Pearson correlation for a dataset. What is the most likely reason for this choice?

A. The dataset has more than 1,000 rows

B. The two variables have a non-linear but monotonic relationship or significant outliers

C. The Pearson coefficient returned a negative value

D. Spearman is always more accurate than Pearson

**Correct Answer:** B — Spearman correlation is appropriate when the relationship is monotonic but not strictly linear, when data is ordinal, or when outliers would distort Pearson's calculation. Row count does not determine the choice (A). A negative Pearson r is a valid result that does not require switching methods (C). Neither method is universally more accurate; each is appropriate for different data conditions (D).

---

## Question 13 (5 points)

Which chart type is most appropriate for showing how a company's five product lines each contribute to total revenue, expressed as percentages?

A. Line chart

B. Scatter plot

C. Histogram

D. Stacked bar chart or pie chart

**Correct Answer:** D — Both stacked bar charts and pie charts show part-to-whole composition. With five categories, either is appropriate. Line charts show trends over time (A). Scatter plots display relationships between two continuous variables (B). Histograms show the frequency distribution of a single continuous variable (C).

---

## Question 14 (5 points)

A sales dataset has Q1 = $25,000 and Q3 = $55,000. What is the lower outlier fence?

A. $10,000

B. −$20,000

C. $0

D. $20,000

**Correct Answer:** B — IQR = Q3 − Q1 = $55,000 − $25,000 = $30,000. Lower fence = Q1 − (1.5 × IQR) = $25,000 − $45,000 = −$20,000. Since negative sales are impossible in this context, no values fall below the lower fence. Options A, C, and D apply incorrect multipliers or arithmetic.

---

## Question 15 (5 points)

A dataset of 500 customer response times is right-skewed. Which pair of statistics should be reported to best represent both the typical value and the spread?

A. Mean and standard deviation

B. Mean and range

C. Median and IQR

D. Mode and variance

**Correct Answer:** C — For right-skewed distributions, median is the appropriate central tendency measure (resistant to outlier distortion) and IQR is the appropriate spread measure (based on percentiles, also resistant to outliers). Mean and standard deviation are both sensitive to the extreme values that cause skew (A, B). Mode and variance are not informative together for this context (D).

---

## Question 16 (5 points)

Two scatter plot datasets both show `r = 0.70`. In the first dataset, all points cluster tightly around the trend line. In the second, points are more dispersed with a few extreme values. What accounts for this difference while both have the same `r`?

A. The two datasets must have different sample sizes

B. Pearson r only measures linear trend direction and strength, not whether points are uniformly distributed around the line; scatter around the trend varies independently of r

C. The second dataset's r value is incorrect and should be recalculated

D. The first dataset has a higher correlation because its points are tighter

**Correct Answer:** B — Pearson r captures the overall linear trend strength and direction, but it does not capture heteroscedasticity (uneven spread around the trend line). Two datasets can have identical r values while displaying very different scatter patterns. Sample size does not determine scatter tightness (A). An r = 0.70 from dispersed data is not incorrect (C). Both datasets have r = 0.70 by definition — neither has a "higher" correlation (D).

---

## Question 17 (5 points)

A box plot for a dataset has the following values: minimum whisker end = 10, Q1 = 30, median = 40, Q3 = 60, maximum whisker end = 80, and two points plotted at 95 and 102. What are the two points at 95 and 102?

A. The maximum and second maximum values of the dataset

B. Outlier values that fall beyond the upper whisker boundary

C. The mean and one standard deviation above the mean

D. Errors in the chart that should be removed

**Correct Answer:** B — In a box plot, individual points plotted beyond the whisker boundaries are outliers — values that exceed Q3 + 1.5 × IQR (the upper fence). The whisker itself extends to the largest non-outlier value (80). Points at 95 and 102 are above the upper fence and are plotted individually. They are not necessarily errors (D), and they are not related to mean or standard deviation (C).

---

## Question 18 (5 points)

Which of the following best describes kurtosis?

A. The degree to which a distribution is asymmetric

B. The measure of tail heaviness relative to a normal distribution

C. The distance between the 25th and 75th percentiles

D. The percentage of values within one standard deviation of the mean

**Correct Answer:** B — Kurtosis measures how heavy or light the tails of a distribution are compared to a normal distribution. High kurtosis (leptokurtic) means heavier tails and more extreme outliers. Asymmetry is measured by skewness (A). The distance between Q1 and Q3 is IQR (C). The percentage within one SD is a property of the empirical rule for normal distributions (D).

---

## Question 19 (5 points)

An analyst wants to visualize the relationship between three variables: ad spend (x), sales revenue (y), and campaign reach (size of the bubble). Which chart type is most appropriate?

A. Stacked bar chart

B. Bubble chart

C. Histogram

D. Waterfall chart

**Correct Answer:** B — A bubble chart is specifically designed to represent three variables simultaneously: two on the axes (x, y) and one encoded in the size of each bubble. Stacked bar charts show categorical part-to-whole composition (A). Histograms show the distribution of a single variable (C). Waterfall charts show incremental cumulative changes (D).

---

## Question 20 (5 points)

An analyst uses SQL to compute `AVG(sales_amount)` grouped by region. The result for the South region is $52,000. What does this value represent?

A. The total revenue for all stores in the South region

B. The most frequent sales amount recorded in the South region

C. The arithmetic mean of all `sales_amount` values for rows where region = 'South'

D. The median sales amount for the South region

**Correct Answer:** C — `AVG()` in SQL computes the arithmetic mean: the sum of all non-null values in the group divided by the count of non-null values. It is not a total (A), mode (B), or median (D). The SQL median requires `PERCENTILE_CONT(0.5)`, not `AVG()`.

---

End of Module 07 Quiz

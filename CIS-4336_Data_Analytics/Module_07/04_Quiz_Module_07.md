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

End of Module 07 Quiz

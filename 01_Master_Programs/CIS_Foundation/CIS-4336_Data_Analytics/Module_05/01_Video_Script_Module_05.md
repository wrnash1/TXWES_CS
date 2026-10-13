# Video Script — Module 05: Statistical Foundations — Descriptive Statistics

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 05: Statistical Foundations — Descriptive Statistics.

Statistics is the mathematical language of data analysis. You cannot interpret data correctly, choose the right analytical method, or communicate findings accurately without a working knowledge of statistics. This module covers descriptive statistics — the branch that summarizes and describes what is in a dataset, before any inference or prediction.

By the end of this module, you will be able to:

- Calculate and interpret measures of central tendency: mean, median, and mode
- Calculate and interpret measures of spread: range, variance, standard deviation, and IQR
- Describe the shape of a distribution and explain what skewness means for analysis
- Read and interpret box plots, histograms, and frequency tables
- Identify which descriptive measure is appropriate for a given data type and situation
- Apply these concepts to Data+ DA0-001 Domain 3 exam questions

Let us get into it.

---

## Segment 2 — Measures of Central Tendency (5 minutes)

Central tendency describes the "center" of a dataset — a single value that represents the typical observation.

**The Mean** is the arithmetic average. Sum all values and divide by the count.

For a dataset of daily sales: 120, 145, 130, 112, 98, 500, 115 — the mean is 120 + 145 + 130 + 112 + 98 + 500 + 115 divided by 7, which equals 1220 divided by 7, approximately 174.3.

Notice something: most values cluster between 98 and 145, but the single value of 500 pulls the mean up to 174.3 — higher than six of the seven data points. This is the fundamental weakness of the mean: it is sensitive to outliers.

**The Median** is the middle value when data is sorted in order. For an odd number of values, it is the center value. For an even number, it is the average of the two center values.

Sorting our dataset: 98, 112, 115, 120, 130, 145, 500. The median is the fourth value: 120.

The median is 120, compared to a mean of 174.3. The median better represents the typical day because it is not distorted by the 500 outlier. For skewed distributions or data with outliers, median is the more informative measure.

**The Mode** is the most frequently occurring value. In our seven-value dataset, every value is unique — there is no mode. Mode is most useful with categorical data (the most common product category) or with discrete numeric data where values repeat frequently.

A dataset can be unimodal (one mode), bimodal (two modes), or multimodal (multiple modes).

[SHOW CHART: Three side-by-side histograms — symmetric distribution where mean equals median, right-skewed distribution where mean exceeds median, and left-skewed distribution where mean is below median — with mean and median marked on each]

---

## Segment 3 — When to Use Each Measure (2 minutes)

The appropriate measure depends on the data type and distribution shape.

| Situation | Recommended Measure | Why |
|---|---|---|
| Ratio data, symmetric distribution, no outliers | Mean | Most mathematically efficient; uses all data |
| Ratio data with outliers or skewed distribution | Median | Not distorted by extreme values |
| Ordinal data | Median | Preserves rank order; mean is not valid on ordinal scale |
| Nominal data | Mode | Only measure valid on unordered categories |
| Reporting income or home prices | Median | These distributions are right-skewed; mean overstates typical |

This table is exam-relevant. The Data+ exam presents scenarios and asks which central tendency measure is most appropriate.

---

## Segment 4 — Measures of Spread (5 minutes)

Central tendency alone is incomplete. Two datasets can have the same mean but very different spreads.

Dataset A: 50, 50, 50, 50, 50 — mean 50
Dataset B: 10, 30, 50, 70, 90 — mean 50

The mean is identical, but the datasets are fundamentally different. Measures of spread quantify how dispersed data is around the center.

**Range** is the simplest spread measure: maximum minus minimum. For Dataset B: 90 minus 10 equals 80. For Dataset A: 50 minus 50 equals 0.

Range is easy to compute but sensitive to outliers — a single extreme value can produce a misleadingly large range.

**Variance** is the average squared deviation from the mean. For each data point, compute the difference from the mean, square it, sum the squared differences, and divide by N (for a population) or N minus 1 (for a sample). Squaring ensures negative and positive deviations do not cancel each other out.

The sample variance formula:

s squared equals the sum of (xi minus x-bar) squared, divided by (n minus 1).

[SHOW CHART: Step-by-step variance calculation table for Dataset B — column for xi, xi minus mean, and squared deviation — with sum and division shown at the bottom]

**Standard Deviation** is the square root of variance. It returns the spread measure to the original units of the data, making it interpretable.

For Dataset B: variance equals 1000, standard deviation equals approximately 31.6.

Standard deviation is the most commonly reported spread measure because it is in the same units as the data. A standard deviation of 31.6 on a mean-50 dataset means a typical value is about 32 units from the mean.

**Interquartile Range (IQR)** measures the spread of the middle 50 percent of data, from the 25th percentile (Q1) to the 75th percentile (Q3).

IQR equals Q3 minus Q1.

IQR is resistant to outliers, unlike range and standard deviation. This is why IQR is used in the box plot outlier detection method we covered in Module 03.

---

## Segment 5 — Percentiles and Quartiles (2 minutes)

Percentiles divide a sorted dataset into 100 equal parts. The 90th percentile is the value below which 90 percent of observations fall.

Quartiles are specific percentiles:

- Q1 is the 25th percentile
- Q2 is the 50th percentile — equivalent to the median
- Q3 is the 75th percentile

[SHOW CHART: Box plot diagram with the five-number summary labeled — minimum, Q1, median (Q2), Q3, maximum — and whiskers extending to 1.5 times IQR beyond Q1 and Q3, with individual dots representing outliers beyond the whiskers]

The five-number summary (minimum, Q1, median, Q3, maximum) provides a compact description of a distribution and is the foundation of the box plot visualization.

---

## Segment 6 — Distribution Shape: Skewness and Kurtosis (3 minutes)

Understanding the shape of a distribution informs both your choice of descriptive statistics and the validity of subsequent analytical methods.

**Symmetric distribution** — The left and right sides are mirror images. Mean, median, and mode are approximately equal. The normal distribution (bell curve) is the canonical example.

**Right-skewed distribution (positive skew)** — A long tail extends to the right. Most values cluster at the low end, with a few extreme high values. The mean is pulled rightward above the median. Income distributions, home prices, and response times are typically right-skewed.

**Left-skewed distribution (negative skew)** — A long tail extends to the left. The mean is pulled leftward below the median. Test scores in an easy exam (most students score high, a few score very low) are often left-skewed.

[SHOW CHART: Three distribution curves — symmetric (normal), right-skewed with the tail extending right and mean to the right of median, left-skewed with the tail extending left and mean to the left of median — with the relationship between mean and median annotated on each]

**Kurtosis** describes the "tailedness" of a distribution. High kurtosis means heavy tails and more extreme outliers. Low kurtosis means light tails and fewer extremes. For the Data+ exam, you need to know that skewness affects which central tendency measure to use, and that kurtosis describes tail behavior.

---

## Segment 7 — Visualizations for Descriptive Statistics (2 minutes)

Three visualizations directly represent descriptive statistics.

**Histogram** — Groups continuous data into equal-width bins and shows the count or frequency for each bin. Reveals distribution shape, modality, and approximate location of the center.

**Box plot** — Displays the five-number summary visually. The box spans from Q1 to Q3 (the IQR). The line inside the box is the median. Whiskers extend to 1.5 times IQR beyond the box edges. Points outside the whiskers are potential outliers.

**Frequency table** — For categorical or discrete data, tabulates the count and percentage for each unique value. The simplest and most direct way to show distribution of a qualitative variable.

These are tools you will use constantly in professional analytics. Interpreting them correctly on the exam requires understanding the descriptive statistics that underlie each one.

---

## Segment 8 — Exam Alignment and Closing (2 minutes)

Module 05 content aligns with Data+ exam Domain 3 — Data Analysis. The exam tests:

- Computing and interpreting mean, median, mode for given datasets
- Identifying which measure is appropriate for a given scenario
- Interpreting box plot components (Q1, Q3, IQR, outlier thresholds)
- Identifying the direction and implication of skewness
- Selecting the appropriate measure of spread for a given analytical goal

For exam preparation, review the official objectives at comptia.org and Professor Messer's study materials at professormesser.com.

Your Module 05 assignments:

- Complete the Reading Guide — focus on the formula reference and the measure selection guide
- Complete Lab 05 — you will calculate all measures manually and with Python for a provided dataset
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

See you in Module 06, where we move from descriptive to inferential statistics and hypothesis testing.

---

End of Module 05 Video Script — Estimated runtime: 23 minutes

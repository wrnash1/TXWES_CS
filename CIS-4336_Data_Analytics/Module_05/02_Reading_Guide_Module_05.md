# Reading Guide — Module 05: Statistical Foundations — Descriptive Statistics

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


**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Overview

Descriptive statistics summarize and characterize datasets before any inference or modeling. This guide provides formulas, worked examples, decision tables, and Python code for every measure covered in Module 05.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Descriptive statistics | Methods for summarizing and characterizing a dataset without generalizing beyond it |
| Population | The complete set of all observations of interest |
| Sample | A subset of the population used to make inferences |
| Parameter | A numerical characteristic of a population (e.g., population mean, denoted mu) |
| Statistic | A numerical characteristic computed from a sample (e.g., sample mean, denoted x-bar) |
| Mean | The arithmetic average of all values |
| Median | The middle value when data is sorted in ascending order |
| Mode | The most frequently occurring value |
| Range | Maximum minus minimum |
| Variance | The average squared deviation from the mean |
| Standard deviation | The square root of variance; spread in original units |
| IQR | Interquartile Range — Q3 minus Q1; measures spread of the middle 50% |
| Percentile | The value below which a given percentage of observations fall |
| Quartile | Specific percentiles: Q1 (25th), Q2 (50th/median), Q3 (75th) |
| Skewness | A measure of asymmetry in a distribution |
| Kurtosis | A measure of the "tailedness" — how much weight is in the distribution's tails |
| Normal distribution | A symmetric bell-shaped distribution where mean equals median equals mode |
| Right skew | Positive skew — long tail to the right; mean exceeds median |
| Left skew | Negative skew — long tail to the left; mean is below median |
| Five-number summary | Minimum, Q1, Median, Q3, Maximum |
| Box plot | A visualization of the five-number summary with outlier indicators |
| Histogram | A bar chart showing frequency distribution of a continuous variable |

---

## Section 2 — Formula Reference

### Mean

Population mean: mu = (sum of all xi) / N

Sample mean: x-bar = (sum of all xi) / n

### Median

1. Sort all values in ascending order
2. If n is odd: median = value at position (n + 1) / 2
3. If n is even: median = average of values at positions n/2 and (n/2) + 1

### Variance

Population variance: sigma-squared = sum of (xi minus mu) squared, divided by N

Sample variance: s-squared = sum of (xi minus x-bar) squared, divided by (n minus 1)

The denominator is n minus 1 for samples (Bessel's correction) to produce an unbiased estimate of population variance.

### Standard Deviation

Population: sigma = square root of sigma-squared

Sample: s = square root of s-squared

### IQR

IQR = Q3 minus Q1

Outlier lower bound = Q1 minus (1.5 times IQR)

Outlier upper bound = Q3 plus (1.5 times IQR)

---

## Section 3 — Worked Example

Dataset: Monthly sales figures (in thousands): 42, 55, 38, 61, 70, 44, 52, 48, 39, 120

Step 1 — Sort the data: 38, 39, 42, 44, 48, 52, 55, 61, 70, 120

Step 2 — Mean: Sum = 569; n = 10; Mean = 56.9

Step 3 — Median: n = 10 (even); positions 5 and 6 = 48 and 52; Median = (48 + 52) / 2 = 50

Step 4 — Mode: No value repeats; no mode

Step 5 — Range: 120 minus 38 = 82

Step 6 — Quartiles:

- Q1: median of lower half (38, 39, 42, 44, 48) = 42
- Q3: median of upper half (52, 55, 61, 70, 120) = 61

Step 7 — IQR: 61 minus 42 = 19

Step 8 — Outlier bounds: Lower = 42 minus (1.5 × 19) = 42 minus 28.5 = 13.5; Upper = 61 plus 28.5 = 89.5

The value 120 exceeds 89.5 and is flagged as a potential outlier.

Step 9 — Variance (sample):

Deviations from mean 56.9: (38-56.9)=-18.9, (39-56.9)=-17.9, (42-56.9)=-14.9, (44-56.9)=-12.9, (48-56.9)=-8.9, (52-56.9)=-4.9, (55-56.9)=-1.9, (61-56.9)=4.1, (70-56.9)=13.1, (120-56.9)=63.1

Squared deviations: 357.21, 320.41, 222.01, 166.41, 79.21, 24.01, 3.61, 16.81, 171.61, 3981.61

Sum of squared deviations = 5342.9

Sample variance = 5342.9 / 9 = 593.66

Standard deviation = sqrt(593.66) = approximately 24.37

---

## Section 4 — Measure Selection Guide

| Scenario | Central Tendency | Spread Measure | Why |
|---|---|---|---|
| Ratio/interval data, symmetric, no outliers | Mean | Standard deviation | Mathematically optimal for symmetric distributions |
| Ratio/interval data with outliers | Median | IQR | Both are resistant to outlier distortion |
| Ordinal data | Median | IQR or range | Mean is not valid; median preserves order |
| Nominal data | Mode | Frequency table | Only valid operations on unordered categories |
| Income, home prices, response times | Median | IQR | Right-skewed distributions; mean overstates typical |
| Test scores | Mean or median | Standard deviation | Depends on whether outliers are present |
| Comparing two groups | Mean (if symmetric) or Median (if skewed) | Standard deviation or IQR | Match the measure to the distribution shape |

---

## Section 5 — Distribution Shape Reference

| Shape | Mean vs. Median | Skewness Value | Tail Direction | Example Data |
|---|---|---|---|---|
| Symmetric (normal) | Mean ≈ Median ≈ Mode | Near 0 | Equal on both sides | Height, weight of a large population |
| Right-skewed (positive) | Mean > Median > Mode | Positive | Long tail to the right | Income, home prices, response times |
| Left-skewed (negative) | Mean < Median < Mode | Negative | Long tail to the left | Easy exam scores, age at death |

Key rule for the exam: In a right-skewed distribution, the mean is pulled toward the tail and exceeds the median. Report the median to avoid overstating the typical value.

---

## Section 6 — Python Descriptive Statistics Cheat Sheet

```python
import pandas as pd
import numpy as np

data = [42, 55, 38, 61, 70, 44, 52, 48, 39, 120]
s = pd.Series(data)

# Central tendency
mean   = s.mean()
median = s.median()
mode   = s.mode()[0]  # returns a Series; [0] gets the first mode
print(f"Mean: {mean:.2f}, Median: {median:.2f}, Mode: {mode}")

# Spread
rng    = s.max() - s.min()
var    = s.var()          # sample variance (ddof=1 by default)
std    = s.std()          # sample standard deviation
q1     = s.quantile(0.25)
q3     = s.quantile(0.75)
iqr    = q3 - q1
print(f"Range: {rng}, Variance: {var:.2f}, Std Dev: {std:.2f}")
print(f"Q1: {q1}, Q3: {q3}, IQR: {iqr}")

# Outlier bounds
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr
print(f"Outlier bounds: [{lower:.2f}, {upper:.2f}]")
outliers = s[(s < lower) | (s > upper)]
print(f"Outliers: {outliers.values}")

# Full summary
print(s.describe())

# Skewness and kurtosis
print(f"Skewness: {s.skew():.4f}")
print(f"Kurtosis: {s.kurt():.4f}")
```

---

## Section 7 — Box Plot Interpretation Guide

A box plot encodes the five-number summary visually.

- The left edge of the box = Q1
- The right edge of the box (or top for vertical plots) = Q3
- The line inside the box = Median (Q2)
- The box width = IQR (middle 50% of data)
- Whiskers extend to: the furthest data point within 1.5 times IQR of the box edges
- Points beyond the whiskers = potential outliers (plotted individually)

When reading a box plot for an exam question:

1. A box shifted far to one side indicates skew in that direction
2. A long whisker on one side indicates a long tail in that direction
3. Many outlier points on one side indicate a heavily skewed distribution
4. A median line close to Q1 (bottom of box) rather than centered indicates right skew

---

## Section 8 — Data+ Exam Tips

1. **Mean vs. median for skewed data.** When exam text describes income, housing prices, or response times — all right-skewed — the answer involving "most representative" or "typical" value is median, not mean.

2. **Ordinal data and mean.** The exam may present a Likert-scale column with numeric values (1–5) and ask for the best central tendency measure. The answer is median, because ordinal intervals are not equal.

3. **IQR outlier boundary formula.** Memorize: Lower = Q1 minus 1.5 times IQR; Upper = Q3 plus 1.5 times IQR. This formula appears in questions about outlier detection and box plot interpretation.

4. **Sample vs. population standard deviation.** When computing standard deviation from a sample (which is almost always the case in analytics), divide by n minus 1, not n. This distinction appears in exam questions.

5. **Right skew means mean exceeds median.** In a right-skewed distribution: mean > median > mode. In a left-skewed distribution: mean < median < mode.

6. **The five-number summary.** The box plot displays minimum, Q1, median, Q3, and maximum. Exam questions may ask you to identify which statistic corresponds to which part of a box plot.

7. **Mode for categorical data.** When an exam question asks for descriptive statistics on a categorical (nominal) variable, mode is the only valid central tendency measure.

8. **Standard deviation in original units.** Standard deviation is always expressed in the same units as the original data. If revenue is in dollars, standard deviation is in dollars. This makes it more interpretable than variance, which is in squared units.

---

## Section 9 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Reproduce the formula reference in Section 2 from memory
- [ ] Complete the worked example in Section 3 independently (without looking)
- [ ] Reproduce the measure selection guide table from memory
- [ ] Run all Python code in Section 6 and confirm output matches expected values
- [ ] Practice interpreting a box plot using the Section 7 guide
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 05
- [ ] Complete Quiz 05

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. Khan Academy — Descriptive Statistics**
<https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data>
Free video lessons and exercises on mean, median, mode, standard deviation, IQR, and box plots. Each concept includes practice problems with immediate feedback, mapped directly to the content of this module.

**2. StatQuest with Josh Starmer — Standard Deviation vs. Standard Error**
<https://www.youtube.com/watch?v=SzZ6GpcfoQY>
A clear visual explanation of variance, standard deviation, and the practical difference between population and sample calculations. Directly addresses the Bessel's correction concept tested in this module.

**3. Towards Data Science — Understanding Box Plots**
<https://towardsdatascience.com/understanding-boxplots-5e2df7bcbd51>
A detailed visual guide to reading and interpreting box plots, including skewness identification, whisker length, and outlier detection. Includes Python code to generate and annotate box plots for real datasets.

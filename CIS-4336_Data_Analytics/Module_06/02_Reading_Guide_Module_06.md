# Reading Guide — Module 06: Statistical Analysis — Inferential Statistics and Hypothesis Testing

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

Inferential statistics allows analysts to draw conclusions about populations from sample data. This guide covers hypothesis testing, error types, correlation, and common statistical tests — all tested in Data+ Domain 3.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Inferential statistics | Methods for drawing conclusions about a population based on sample data |
| Population | The complete set of all observations of interest |
| Sample | A subset selected from the population |
| Parameter | A measurable characteristic of a population (e.g., population mean) |
| Statistic | A measurable characteristic of a sample (e.g., sample mean) |
| Null hypothesis (H0) | The default assumption of no effect, no difference, or no relationship |
| Alternative hypothesis (H1) | The claim being tested — that an effect, difference, or relationship exists |
| p-value | The probability of observing results at least as extreme as those found, assuming H0 is true |
| Significance level (alpha) | The pre-set threshold below which p-value leads to rejection of H0; typically 0.05 |
| Type I error | Rejecting H0 when it is actually true (false positive); probability equals alpha |
| Type II error | Failing to reject H0 when it is actually false (false negative); probability equals beta |
| Statistical power | Probability of correctly detecting a real effect; 1 minus beta |
| Correlation | A measure of the strength and direction of the linear relationship between two numeric variables |
| Pearson r | The correlation coefficient; ranges from -1 (perfect negative) to +1 (perfect positive) |
| Causation | A relationship where changes in one variable directly cause changes in another |
| Confounding variable | A third variable that causes both of two correlated variables, creating a spurious correlation |
| t-test | Statistical test comparing means between one or two groups |
| Chi-square test | Statistical test for association between two categorical variables |
| ANOVA | Analysis of Variance — compares means across three or more groups |
| Effect size | A measure of practical significance; quantifies how large the observed effect is |
| Cohen's d | A standardized effect size for comparing two means: (mean1 minus mean2) / pooled SD |
| Confidence interval | A range of values that likely contains the true population parameter with a stated confidence level |

---

## Section 2 — Hypothesis Testing Framework

### Step-by-Step Process

1. State the null hypothesis (H0) and alternative hypothesis (H1)
2. Set the significance level (alpha) — typically 0.05
3. Collect sample data
4. Compute the test statistic appropriate for the test type
5. Compute or look up the p-value
6. Decision: if p-value <= alpha, reject H0; if p-value > alpha, fail to reject H0
7. State the conclusion in plain language

### p-Value Interpretation

| p-Value | Interpretation |
|---|---|
| p < 0.01 | Very strong evidence against H0; reject |
| 0.01 <= p < 0.05 | Strong evidence against H0; reject at alpha = 0.05 |
| 0.05 <= p < 0.10 | Marginal evidence; fail to reject at alpha = 0.05 |
| p >= 0.10 | Insufficient evidence to reject H0 |

Important: "Fail to reject H0" is NOT the same as "prove H0 is true." It simply means the sample evidence was not strong enough to conclude otherwise.

---

## Section 3 — Type I and Type II Error Reference

| | H0 is True (No Real Effect) | H0 is False (Real Effect Exists) |
|---|---|---|
| Reject H0 | Type I Error (False Positive) — probability = alpha | Correct Decision — probability = power (1 - beta) |
| Fail to Reject H0 | Correct Decision — probability = 1 - alpha | Type II Error (False Negative) — probability = beta |

### Practical Examples

- **Type I error example:** A cancer screening test incorrectly flags a healthy patient as having cancer. The patient undergoes unnecessary treatment.
- **Type II error example:** A cancer screening test fails to detect cancer in a patient who has it. The disease goes untreated.
- **Which is worse?** Depends entirely on context and the consequences of each error type.

### Reducing Errors

- Increase sample size: reduces both Type I and Type II error risk
- Lower alpha: reduces Type I error but increases Type II error risk
- Increase statistical power: reduces Type II error (achieved through larger samples, better measurement)

---

## Section 4 — Correlation Reference

### Pearson r Strength Guidelines

| r Value (absolute) | Interpretation |
|---|---|
| 0.00 to 0.19 | Negligible / no practical relationship |
| 0.20 to 0.39 | Weak positive or negative relationship |
| 0.40 to 0.59 | Moderate relationship |
| 0.60 to 0.79 | Strong relationship |
| 0.80 to 1.00 | Very strong relationship |

### Correlation vs. Causation

Correlation measures co-movement between two variables. Causation requires evidence that changes in one variable directly produce changes in the other.

A correlation alone never proves causation. Establishing causation requires:

- Temporal precedence (cause must precede effect)
- Correlation (the variables must co-vary)
- Elimination of confounding variables (alternative explanations must be ruled out)
- Ideally, a randomized controlled experiment

### Python Correlation Code

```python
import pandas as pd

df = pd.read_csv("data.csv")

# Pearson correlation between two columns
r = df["variable_a"].corr(df["variable_b"])
print(f"Pearson r: {r:.4f}")

# Full correlation matrix
print(df[["col1", "col2", "col3"]].corr())
```

---

## Section 5 — Statistical Test Selection Guide

| Scenario | Test | Notes |
|---|---|---|
| Compare sample mean to known value | One-sample t-test | Data should be approximately normal |
| Compare means of two independent groups | Independent samples t-test | Data should be approximately normal in each group |
| Compare means before and after (same subjects) | Paired t-test | Each observation is matched to a partner |
| Compare means of three or more groups | ANOVA (F-test) | Post-hoc tests needed to identify which groups differ |
| Test association between two categorical variables | Chi-square test of independence | Requires adequate expected cell counts (typically >= 5) |
| Model linear relationship between numeric variables | Linear regression | Produces prediction equation; r-squared measures fit |
| Non-normal data, two groups | Mann-Whitney U test | Non-parametric alternative to independent t-test |

---

## Section 6 — Python Hypothesis Testing Code

```python
from scipy import stats
import numpy as np

# Independent samples t-test
group_a = [23, 25, 28, 21, 26, 24, 27, 22]
group_b = [18, 20, 22, 19, 21, 17, 23, 20]

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

alpha = 0.05
if p_value <= alpha:
    print("Reject H0: The group means are significantly different.")
else:
    print("Fail to reject H0: No significant difference detected.")

# Chi-square test for categorical association
from scipy.stats import chi2_contingency

observed = [[45, 30], [20, 55]]  # 2x2 contingency table
chi2, p, dof, expected = chi2_contingency(observed)
print(f"\nChi-square: {chi2:.4f}, p-value: {p:.4f}, df: {dof}")

# Pearson correlation with significance
import pandas as pd
df = pd.DataFrame({"x": [1,2,3,4,5,6,7,8], "y": [2,4,5,4,5,7,8,9]})
r, p_corr = stats.pearsonr(df["x"], df["y"])
print(f"\nPearson r: {r:.4f}, p-value: {p_corr:.4f}")
```

---

## Section 7 — Confidence Intervals

A confidence interval gives a range of plausible values for a population parameter.

A 95% confidence interval for a mean means: if we repeated this sampling process many times, 95% of the resulting intervals would contain the true population mean.

The interval does NOT mean there is a 95% probability the true mean is in this specific interval — either it is in the interval or it is not.

Wider intervals indicate more uncertainty (smaller samples, higher variability). Narrower intervals indicate more precision (larger samples, lower variability).

```python
import scipy.stats as stats
import numpy as np

data = [42, 55, 38, 61, 70, 44, 52, 48, 39, 50]
n = len(data)
mean = np.mean(data)
se = stats.sem(data)  # standard error of the mean

# 95% confidence interval
ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=se)
print(f"Sample mean: {mean:.2f}")
print(f"95% CI: ({ci[0]:.2f}, {ci[1]:.2f})")
```

---

## Section 8 — Data+ Exam Tips

1. **p-value decision rule.** If p-value <= alpha, reject H0. If p-value > alpha, fail to reject H0. This rule appears on the exam in multiple formats — always apply it precisely.

2. **Failing to reject is not proof.** "Fail to reject H0" never means H0 is proven true. It means the sample evidence was insufficient to reject it. The exam distinguishes these carefully.

3. **Type I vs. Type II identification.** Type I = false positive (reject when H0 is true). Type II = false negative (keep H0 when it is false). Match the error type to the scenario: treating a healthy person for a disease they do not have is Type I.

4. **Correlation does not imply causation.** This statement appears on the Data+ exam. Always identify the confounding variable when a spurious correlation is described.

5. **r = 0 means no linear relationship.** Two variables can be related non-linearly and still have r near zero. The exam tests understanding of what r does and does not measure.

6. **Chi-square is for categorical variables.** When two variables are both categorical and you want to know if they are associated, the test is chi-square. For numeric means, use t-test or ANOVA.

7. **Sample size and power.** Increasing sample size increases statistical power and reduces both Type I and Type II error probability. The exam may present a scenario where the analyst can improve results by collecting more data.

8. **Effect size and practical significance.** A statistically significant result with very large sample size may have a negligible effect size. The exam distinguishes between statistical significance (p-value) and practical significance (effect size).

---

## Section 9 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Reproduce the hypothesis testing seven-step process from memory
- [ ] Correctly apply the p-value decision rule to five practice examples
- [ ] Reproduce the Type I / Type II error matrix from memory
- [ ] Classify four correlation examples by strength using the r scale
- [ ] Explain why correlation does not imply causation using an original example
- [ ] Select the correct test type for five different scenarios
- [ ] Run all Python code in Sections 6 and 7 and confirm expected output
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 06
- [ ] Complete Quiz 06

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. StatQuest with Josh Starmer — Hypothesis Testing (YouTube Playlist)**
<https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9>
A highly rated playlist covering p-values, t-tests, ANOVA, chi-square, and Type I/II errors with visual intuition. Widely used by students preparing for statistics exams and certifications.

**2. Seeing Theory — Interactive Probability and Statistics**
<https://seeing-theory.brown.edu/frequentist-inference/index.html>
An interactive, browser-based visualization of confidence intervals, hypothesis testing, and the central limit theorem. Allows students to manipulate sample sizes and significance levels to observe effects in real time.

**3. SciPy Stats Documentation — Statistical Tests Reference**
<https://docs.scipy.org/doc/scipy/reference/stats.html>
The official reference for all statistical tests available in Python's scipy.stats module, including t-tests, ANOVA, chi-square, Mann-Whitney, and Pearson correlation. Includes function signatures, parameters, and worked examples.

# Lab 06 — Inferential Statistics and Hypothesis Testing

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Objectives

By completing this lab, you will be able to:

- Formulate null and alternative hypotheses for business scenarios
- Conduct independent samples t-tests and interpret p-values
- Perform chi-square tests for categorical association
- Compute Pearson correlation coefficients and assess significance
- Identify Type I and Type II errors in context
- Distinguish statistical significance from practical significance

---

## Prerequisites

- Module 06 Reading Guide completed
- Python 3.8 or later (or Google Colab)
- Libraries: `pip install pandas numpy scipy matplotlib`

---

## Dataset Setup

Run this block first to create all datasets used in the lab.

```python
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

np.random.seed(42)

# Dataset 1: Website A/B test conversion data
group_a_conversions = np.random.normal(loc=8.5, scale=2.1, size=150).round(2)
group_b_conversions = np.random.normal(loc=9.2, scale=2.3, size=150).round(2)

# Dataset 2: Customer satisfaction by region (categorical)
satisfaction_data = pd.DataFrame({
    "region": (["North"]*120 + ["South"]*110 + ["East"]*95 + ["West"]*105),
    "satisfied": (
        [1]*78 + [0]*42 +  # North: 65% satisfied
        [1]*66 + [0]*44 +  # South: 60% satisfied
        [1]*52 + [0]*43 +  # East:  55% satisfied
        [1]*71 + [0]*34    # West:  68% satisfied
    )
})

# Dataset 3: Sales rep performance
sales_data = pd.DataFrame({
    "rep_id": range(1, 41),
    "training_hours": np.random.normal(loc=20, scale=8, size=40).clip(5, 40).round(1),
    "quarterly_sales": np.random.normal(loc=85000, scale=18000, size=40).clip(30000, 150000).round(0)
})
sales_data["quarterly_sales"] = (
    sales_data["training_hours"] * 1500 +
    np.random.normal(0, 8000, 40) + 50000
).round(0)

print("Datasets created.")
print(f"A/B test: Group A n={len(group_a_conversions)}, Group B n={len(group_b_conversions)}")
print(f"Satisfaction data: {len(satisfaction_data)} rows")
print(f"Sales data: {len(sales_data)} rows")
```

---

## Part A — Hypothesis Formulation (15 points)

### Part A Instructions

For each of the four scenarios below, write out:

1. The null hypothesis (H0) in a complete sentence
2. The alternative hypothesis (H1) in a complete sentence
3. The appropriate statistical test to use
4. The significance level you would use and why

**Scenario A1:** A marketing team ran an A/B test on their website landing page. Version A is the current page; Version B has a new headline. The team wants to know if the conversion rate for Version B is different from Version A.

**Scenario A2:** A retailer wants to know whether customer satisfaction ratings (Satisfied / Not Satisfied) differ between the four geographic regions (North, South, East, West).

**Scenario A3:** A sales manager believes that the number of training hours a sales representative completes is related to their quarterly sales revenue.

**Scenario A4:** A hospital wants to determine whether a new patient intake process (implemented in Q3) changed the average patient wait time compared to Q2. The same patients are not compared — these are different patient populations in the two quarters.

### Part A Deliverable

Four sets of H0, H1, test name, and significance level rationale. No code required.

**Grading:** 3.75 points per scenario. 15 points total.

---

## Part B — Independent Samples t-Test (25 points)

### Part B Instructions

Use Dataset 1 (A/B test conversion rates) to conduct an independent samples t-test.

```python
# Step 1: Compute basic statistics for each group
print("Group A: mean={:.2f}, std={:.2f}, n={}".format(
    group_a_conversions.mean(),
    group_a_conversions.std(),
    len(group_a_conversions)
))
print("Group B: mean={:.2f}, std={:.2f}, n={}".format(
    group_b_conversions.mean(),
    group_b_conversions.std(),
    len(group_b_conversions)
))

# Step 2: Conduct the t-test
t_stat, p_value = stats.ttest_ind(group_a_conversions, group_b_conversions)
print(f"\nt-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

# Step 3: Make a decision
alpha = 0.05
if p_value <= alpha:
    print(f"\nDecision: Reject H0 (p={p_value:.4f} <= alpha={alpha})")
    print("Conclusion: The conversion rates differ significantly between groups.")
else:
    print(f"\nDecision: Fail to reject H0 (p={p_value:.4f} > alpha={alpha})")
    print("Conclusion: No statistically significant difference detected.")

# Step 4: Visualize
fig, ax = plt.subplots(figsize=(8, 5))
ax.hist(group_a_conversions, bins=20, alpha=0.6, label="Group A", color="steelblue")
ax.hist(group_b_conversions, bins=20, alpha=0.6, label="Group B", color="coral")
ax.axvline(group_a_conversions.mean(), color="blue", linestyle="--",
           label=f"Mean A: {group_a_conversions.mean():.2f}")
ax.axvline(group_b_conversions.mean(), color="red", linestyle="--",
           label=f"Mean B: {group_b_conversions.mean():.2f}")
ax.set_title("A/B Test: Conversion Rate Distribution")
ax.set_xlabel("Conversion Rate (%)")
ax.set_ylabel("Frequency")
ax.legend()
plt.tight_layout()
plt.savefig("ab_test_histogram.png", dpi=100)
plt.show()
```

### Part B Questions

**Question B1 (8 points):** State your H0 and H1 from Part A, Scenario A1. Report the t-statistic and p-value. State your decision (reject or fail to reject H0) at alpha = 0.05, and write a one-paragraph conclusion in plain business language explaining what the result means for the marketing team.

**Question B2 (9 points):** Explain the difference between statistical significance and practical significance in the context of this A/B test. The difference in means between Group A and Group B is approximately 0.7 percentage points. In a business context, is this difference practically significant? What additional information would you need to decide whether to roll out Version B to all users?

**Question B3 (8 points):** If the p-value had been 0.08 instead of what you calculated: (a) would you reject or fail to reject H0 at alpha = 0.05? (b) Would your decision change at alpha = 0.10? (c) Explain why the choice of alpha before running the test matters — what is the risk of choosing alpha after seeing the data?

### Part B Deliverable

Code output, histogram PNG, and written answers to B1 through B3.

---

## Part C — Chi-Square Test (25 points)

### Part C Instructions

Use Dataset 2 (satisfaction by region) to test whether satisfaction differs across regions.

```python
# Build contingency table
ct = pd.crosstab(
    satisfaction_data["region"],
    satisfaction_data["satisfied"],
    rownames=["Region"],
    colnames=["Satisfied (1=Yes, 0=No)"]
)
print("Contingency Table:")
print(ct)
print("\nRow Percentages:")
print(ct.div(ct.sum(axis=1), axis=0).round(3) * 100)

# Run chi-square test
from scipy.stats import chi2_contingency
chi2, p, dof, expected = chi2_contingency(ct)
print(f"\nChi-square statistic: {chi2:.4f}")
print(f"p-value: {p:.4f}")
print(f"Degrees of freedom: {dof}")
print("\nExpected frequencies:")
print(pd.DataFrame(expected, index=ct.index, columns=ct.columns).round(2))
```

### Part C Questions

**Question C1 (8 points):** State H0 and H1 for this chi-square test. Report the chi-square statistic, degrees of freedom, and p-value. Make a decision at alpha = 0.05 and write a conclusion in plain language for a regional sales manager.

**Question C2 (9 points):** Review the row percentages in the output. Which region has the highest satisfaction rate? Which has the lowest? If the chi-square test returns a significant result, does that mean every region is different from every other region? Explain what additional analysis would be needed to identify which specific regions differ.

**Question C3 (8 points):** The chi-square test requires that expected cell counts be at least 5. Look at the expected frequencies table in your output. Does this assumption appear to be met? Explain why violating this assumption matters and what you would do if any expected cell count fell below 5.

### Part C Deliverable

Code output and written answers to C1 through C3.

---

## Part D — Correlation Analysis (20 points)

### Part D Instructions

Use Dataset 3 (sales rep performance) to analyze the relationship between training hours and sales revenue.

```python
# Step 1: Compute correlation
r, p_corr = stats.pearsonr(
    sales_data["training_hours"],
    sales_data["quarterly_sales"]
)
print(f"Pearson r: {r:.4f}")
print(f"p-value for correlation: {p_corr:.4f}")

strength = (
    "negligible" if abs(r) < 0.20 else
    "weak" if abs(r) < 0.40 else
    "moderate" if abs(r) < 0.60 else
    "strong" if abs(r) < 0.80 else
    "very strong"
)
direction = "positive" if r > 0 else "negative"
print(f"Relationship: {strength} {direction}")

# Step 2: Scatter plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(sales_data["training_hours"], sales_data["quarterly_sales"],
           alpha=0.7, color="steelblue")
m, b = np.polyfit(sales_data["training_hours"], sales_data["quarterly_sales"], 1)
x_line = np.linspace(sales_data["training_hours"].min(),
                     sales_data["training_hours"].max(), 100)
ax.plot(x_line, m * x_line + b, color="red", linewidth=2, label=f"Trend line")
ax.set_title(f"Training Hours vs. Quarterly Sales (r = {r:.3f})")
ax.set_xlabel("Training Hours")
ax.set_ylabel("Quarterly Sales ($)")
ax.legend()
plt.tight_layout()
plt.savefig("correlation_scatter.png", dpi=100)
plt.show()
```

### Part D Questions

**Question D1 (7 points):** Report the Pearson r value and its classification by strength and direction. Is the correlation statistically significant at alpha = 0.05? Write a three to four sentence interpretation of what this correlation means for the sales manager — being careful to use appropriate causal language.

**Question D2 (7 points):** A sales director reviews your scatter plot and says: "This proves that more training causes higher sales — we should double everyone's training hours." Evaluate this claim. Identify at least two alternative explanations (confounding variables) that could explain the correlation without training directly causing higher sales.

**Question D3 (6 points):** If the correlation between training hours and sales revenue is r = 0.78, what percentage of the variance in sales revenue is explained by training hours? Show your calculation. What does the remaining unexplained variance suggest about other factors influencing sales performance?

### Part D Deliverable

Code output, scatter plot PNG, and written answers to D1 through D3.

---

## Submission Instructions

Compile all deliverables into a single PDF. Include all code, outputs, chart images, and written answers. Name your file: `Lab06_LastName_FirstName.pdf`. Submit to Canvas before the stated deadline.

---

## Grading Rubric Summary

| Part | Description | Points |
|---|---|---|
| A | Hypothesis Formulation | 15 |
| B | Independent Samples t-Test | 25 |
| C | Chi-Square Test | 25 |
| D | Correlation Analysis | 20 |
| E | Submission completeness and formatting | 15 |
| **Total** | | **100** |

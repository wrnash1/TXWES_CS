# Reading Guide: Module 06 - Statistical Analysis – Inferential Statistics and Hypothesis Testing
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 06 - Statistical Analysis: Inferential Statistics and Hypothesis Testing**! While descriptive statistics summarize the data you have, inferential statistics use that sample to draw conclusions about a larger population. This module covers the core inferential concepts tested on the **CompTIA Data+** exam: hypothesis testing, p-values, confidence intervals, and data quality dimensions.

These concepts directly support analytics decisions — whether a new feature improves conversion rates, whether two groups differ significantly, or whether a dataset meets quality thresholds for production use.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Population vs. sample**: A population is the complete set of all entities of interest (e.g., all customers). A sample is a subset drawn from the population for analysis. Inferential statistics use sample statistics (mean, proportion) to estimate population parameters. The quality of inference depends on whether the sample is representative and large enough.
*   **Hypothesis testing**: A formal statistical procedure for deciding whether observed data provides enough evidence to reject a null hypothesis (H₀). The null hypothesis typically states "no effect" or "no difference." The alternative hypothesis (H₁) states the effect or difference you expect to find. The test produces a p-value that is compared against a significance level (alpha, typically 0.05).
*   **p-value**: The probability of observing results at least as extreme as the data, assuming the null hypothesis is true. A p-value below alpha (commonly 0.05) leads to rejecting H₀. A common exam trap is confusing a low p-value with "the probability that H₀ is true" — it is not. It is the probability of the data, given H₀.
*   **Data quality dimensions (accuracy, completeness, consistency, validity, uniqueness)**: The five dimensions used to assess whether data is fit for its intended analytical purpose. Accuracy means values reflect reality; completeness means no required fields are missing; consistency means values agree across systems; validity means values conform to defined formats and rules; uniqueness means no duplicate records exist for the same entity.
*   **Profiling statistics**: Summary statistics generated during data profiling — null counts, distinct value counts, min/max values, frequency distributions — used to audit a dataset's quality before analysis.

---

### 2. Certification Exam Tips
*   **Domain weight:** Statistical analysis and data quality concepts span Domain 3 (Data Mining, ~23%) and Domain 4 (Analytics and Reporting, ~23%) of the Data+ DA0-001 exam.
*   **Exam trap — p-value misinterpretation**: The exam may offer an answer stating "p = 0.03 means there is a 3% probability the null hypothesis is true." This is wrong. p = 0.03 means: given H₀ is true, there is only a 3% chance of observing data this extreme. The correct conclusion is to reject H₀ at alpha = 0.05.
*   **Exam trap — data quality dimension identification**: Scenario questions describe a data problem and ask which quality dimension is violated. If records exist in one system but not another, that is a consistency issue. If email fields contain phone numbers, that is a validity issue. If required fields are blank, that is a completeness issue.
*   **Exam trap — completeness vs. accuracy**: Completeness asks "is the data present?" Accuracy asks "is the data correct?" A field can be complete (not null) but inaccurate (wrong value). The exam tests this distinction.
*   **Study Resource:** The inference and statistical testing chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/) cover hypothesis testing with simulated examples. The [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) covers statistical testing with SciPy.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the inference and probability chapters in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). Focus on the sections covering hypothesis tests, p-values, and confidence intervals with worked examples.
*   **Required Video:** Watch the statistics and data quality sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238), which demonstrates profiling datasets for quality issues using Pandas.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Profile a database table to count null percentages per column**: Compute the null rate for each column and flag any column with more than 5% nulls as a completeness concern.
*   **Validate formats of zip codes and email entries**: Use regex to check that zip codes match a 5-digit pattern and emails contain "@" and a domain, flagging non-conforming values as validity violations.
*   **Identify duplicate rows**: Count distinct rows vs. total rows; document the uniqueness violation rate and propose a deduplication strategy.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the inference and probability chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.

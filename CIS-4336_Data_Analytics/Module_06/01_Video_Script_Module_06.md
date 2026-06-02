# Video Script — Module 06: Statistical Analysis — Inferential Statistics and Hypothesis Testing

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 06: Statistical Analysis — Inferential Statistics and Hypothesis Testing.

In Module 05 we described data. In this module we draw conclusions from it. Inferential statistics is the branch of statistics that uses sample data to make inferences about a larger population, and to evaluate whether observed patterns are real or likely due to chance.

By the end of this module, you will be able to:

- Explain the difference between descriptive and inferential statistics
- Define the null hypothesis and alternative hypothesis
- Interpret p-values and significance levels
- Describe Type I and Type II errors
- Distinguish correlation from causation
- Identify basic statistical tests and when each is appropriate
- Apply these concepts to Data+ DA0-001 Domain 3 exam questions

---

## Segment 2 — Populations, Samples, and Inference (3 minutes)

The fundamental challenge in statistics is that we rarely have access to the entire population of interest. We work with samples.

A **population** is the complete set of all observations we care about. Every customer who has ever bought a product. Every patient with a given diagnosis. Every transaction processed in a year.

A **sample** is a subset selected from the population. We measure the sample, compute statistics, and use those statistics to make inferences about population parameters.

This process works reliably only when the sample is representative — drawn from the population in a way that avoids systematic bias.

A **random sample** gives every member of the population an equal chance of selection. This is the gold standard.

A **stratified sample** divides the population into subgroups (strata) and samples proportionally from each. This is used when the population has known structure (regions, age groups) and you need the sample to represent that structure.

A **convenience sample** uses whoever is easily available. It is fast and cheap but frequently biased. Online survey respondents who voluntarily self-select are a convenience sample.

[SHOW CHART: Diagram showing Population on the left, an arrow labeled "sampling" pointing to Sample on the right, and an arrow labeled "inference" pointing back from Sample to Population]

The Data+ exam tests your ability to identify sampling strategies and assess their validity for a given research question.

---

## Segment 3 — Hypothesis Testing Framework (4 minutes)

Hypothesis testing provides a formal procedure for deciding whether sample evidence is strong enough to support a claim about the population.

Every hypothesis test begins with two hypotheses.

**The null hypothesis (H0)** is the default assumption — the position of "no effect" or "no difference." In a drug trial, the null hypothesis might be: this drug has no effect on blood pressure compared to placebo.

**The alternative hypothesis (H1 or Ha)** is the claim we are trying to establish — the position that something is different or that an effect exists. In the drug trial: this drug reduces blood pressure compared to placebo.

The logic of hypothesis testing is indirect. We assume the null hypothesis is true and ask: if the null is true, how likely is it that we would observe sample data this extreme or more extreme purely by chance?

That likelihood is the **p-value**.

If the p-value is very small — meaning the observed data would be very unlikely under the null hypothesis — we reject the null hypothesis and conclude that the evidence supports the alternative.

The **significance level (alpha)** is the threshold we set in advance for "small enough." The conventional threshold is alpha = 0.05, meaning we accept a 5% chance of wrongly rejecting a true null hypothesis.

Decision rule:

- If p-value is less than or equal to alpha: reject the null hypothesis
- If p-value is greater than alpha: fail to reject the null hypothesis (this is not the same as proving the null is true)

[SHOW CHART: p-value distribution diagram — a normal curve with a shaded rejection region in the tail, the critical value (alpha = 0.05) marked, and labels showing "Fail to Reject H0" in the main region and "Reject H0" in the tail]

---

## Segment 4 — Type I and Type II Errors (3 minutes)

Hypothesis testing can produce two types of errors.

**Type I error (false positive)** — We reject the null hypothesis when it is actually true. We conclude an effect exists when it does not. The probability of a Type I error equals alpha (the significance level). At alpha = 0.05, we accept a 5% chance of Type I error.

**Type II error (false negative)** — We fail to reject the null hypothesis when it is actually false. We miss a real effect. The probability of a Type II error is called beta.

**Statistical power** is the probability of correctly detecting a real effect (1 minus beta). High power is desirable.

[SHOW CHART: Two-by-two matrix showing reality (H0 true / H0 false) on the rows and our decision (reject H0 / fail to reject H0) on the columns — with "Correct" and "Type I Error" on the first row, and "Type II Error" and "Correct" on the second row]

The tradeoff: lowering alpha (e.g., from 0.05 to 0.01) reduces Type I error risk but increases Type II error risk. Increasing sample size reduces both error types simultaneously.

On the Data+ exam, you will be asked to identify which error type a given scenario represents.

---

## Segment 5 — Correlation (3 minutes)

Correlation measures the strength and direction of the linear relationship between two numeric variables.

The **Pearson correlation coefficient (r)** ranges from -1 to +1.

- r = +1: perfect positive linear relationship — as one variable increases, the other increases proportionally
- r = -1: perfect negative linear relationship — as one increases, the other decreases proportionally
- r = 0: no linear relationship

The strength guidelines commonly used in practice:

- 0.00 to 0.19: negligible
- 0.20 to 0.39: weak
- 0.40 to 0.59: moderate
- 0.60 to 0.79: strong
- 0.80 to 1.00: very strong

**Critical rule: Correlation does not imply causation.**

Two variables can be strongly correlated without either one causing the other. The classic example: ice cream sales and drowning deaths are positively correlated. Does eating ice cream cause drowning? Of course not. Both are caused by a third variable — hot weather. This is called a **confounding variable** or **lurking variable**.

[SHOW CHART: Four scatter plots side by side showing r = 0.9 (strong positive), r = 0.4 (weak positive), r = 0 (no relationship), and r = -0.8 (strong negative) — with a data point cloud illustrating each correlation strength]

---

## Segment 6 — Common Statistical Tests (3 minutes)

Different research questions require different statistical tests. The choice of test depends on the data types, the number of groups, and whether the data meets parametric assumptions.

**t-test** — Compares means between two groups. Used when data is approximately normally distributed and the variable is ratio or interval.

- One-sample t-test: Is this sample's mean different from a known value?
- Independent samples t-test: Are the means of two independent groups different?
- Paired t-test: Are the means of paired measurements different?

**Chi-square test** — Tests for association between two categorical variables. Asks: are these two categories distributed independently of each other?

**ANOVA (Analysis of Variance)** — Compares means across three or more groups. Extends the two-group t-test.

**Linear regression** — Models the relationship between a numeric outcome variable and one or more predictor variables. Produces a prediction equation.

[SHOW CHART: Decision tree — "How many groups?" branches to 1 group (one-sample t-test), 2 groups (independent t-test), 3+ groups (ANOVA). Side branch — "Both variables categorical?" leads to Chi-square]

---

## Segment 7 — Practical Significance vs. Statistical Significance (2 minutes)

A result can be statistically significant without being practically meaningful.

Statistical significance means: the observed effect is unlikely to be due to chance (p-value below threshold).

Practical significance means: the observed effect is large enough to matter in the real world.

With a very large sample, even a tiny difference becomes statistically significant. A website A/B test with 1 million users might find that one button color produces a conversion rate of 2.01% while another produces 2.02% — statistically significant, but practically meaningless.

**Effect size** quantifies practical significance. Cohen's d measures the standardized difference between two group means. A d of 0.2 is small, 0.5 is medium, and 0.8 is large.

Always report both statistical and practical significance in professional analytics work.

---

## Segment 8 — Exam Alignment and Closing (2 minutes)

Module 06 aligns with Data+ Domain 3 — Data Analysis. The exam tests:

- Identifying null and alternative hypotheses in a described scenario
- Interpreting a p-value and making a reject/fail-to-reject decision
- Identifying Type I and Type II errors from a scenario description
- Distinguishing correlation from causation with an example
- Selecting the appropriate test type for a described scenario

For exam preparation, review the official objectives at comptia.org and Professor Messer's study materials at professormesser.com.

Your Module 06 assignments:

- Complete the Reading Guide — focus on the hypothesis testing framework and error types table
- Complete Lab 06 — you will perform hypothesis tests and interpret correlation using Python
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

See you in Module 07, where we cover data visualization principles and chart types.

---

End of Module 06 Video Script — Estimated runtime: 22 minutes

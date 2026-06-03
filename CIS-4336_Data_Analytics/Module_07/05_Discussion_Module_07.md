# Discussion: Module 07 — Statistical Analysis and Visualization

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

## Points: 10 (6 initial post + 4 peer responses)

## Certification Alignment: CompTIA Data+ (DA0-001) — Domain 2: Data Analysis

---

## Instructions

Choose ONE of the three scenarios below and write an initial post of 175–225 words. Then respond to at least TWO classmates who chose different scenarios. Peer responses must be at least 75 words and go beyond "I agree" — add a new insight, ask a probing question, or respectfully challenge an assumption.

Initial posts are due by Thursday at 11:59 PM. Peer responses are due by Sunday at 11:59 PM.

---

## Scenario A: The Hospital Readmission Report

A regional hospital network wants to reduce 30-day patient readmission rates. The analytics team has collected data on 4,200 discharge cases including patient age, diagnosis category, length of stay, number of prior admissions in the past year, insurance type, and whether the patient was readmitted within 30 days.

The chief medical officer asks the analytics team to present findings to hospital administrators — a group with no statistical background. The team must choose which statistical measures to highlight and which visualizations to use.

In your initial post, address the following:

- Which measures of central tendency and spread would you compute for the numeric variables (age, length of stay, prior admissions)? Justify your choices based on the likely shape of the distributions.
- One variable — number of prior admissions — has a strong right skew (most patients have 0–1 prior admissions, but a small group has 10 or more). How does this affect your choice of mean vs. median? What does the difference between mean and median tell you about this population?
- What two chart types would you use in the executive presentation, and what specific insight would each one communicate to non-technical administrators?

---

## Scenario B: The E-Commerce Conversion Rate Mystery

An e-commerce company tracks website visitors, time spent on product pages, number of items viewed, cart abandonment rate, and final purchase amount. A marketing analyst notices that ad spend and weekly revenue appear to move together — when ad spend goes up, revenue goes up too. The VP of Marketing concludes: "We just need to keep increasing the ad budget and revenue will keep growing."

The analytics manager asks you to evaluate this conclusion before it becomes company strategy.

In your initial post, address the following:

- How would you use the Pearson correlation coefficient to evaluate the relationship between ad spend and weekly revenue? What value of `r` would you consider strong enough to justify further investigation?
- The VP's statement implies causation. Identify at least two alternative explanations (confounding variables or coincidental factors) that could explain a strong positive correlation between ad spend and revenue without ad spend being the cause.
- What visualization would best help the VP understand both the correlation and its limitations? Describe what the chart would show and why that specific chart type is the right choice for this audience.

---

## Scenario C: The Manufacturing Quality Dashboard

A manufacturing plant produces electronic components. Quality control engineers collect data on component dimensions, defect counts per batch, machine temperature during production, and whether each batch passed or failed final inspection. Leadership wants a real-time quality dashboard that shows both current performance and historical trends.

The data science team must decide what statistics and visualizations to include in the dashboard.

In your initial post, address the following:

- For component dimension measurements, which measure of spread — standard deviation or IQR — would you display on the dashboard, and why? Consider how outliers from machine malfunctions would affect each measure differently.
- Using the empirical rule, explain how you would set automated alert thresholds for dimension measurements on a normally distributed production run. What statistical values define the alert boundaries?
- The dashboard needs to show both the distribution of defect counts per batch and the trend of defect counts over time. Which two chart types would you use for these two purposes, and what would each reveal that the other could not?

---

## Peer Response Guidelines

When responding to classmates, consider:

- Did they correctly identify the appropriate measure of central tendency for the data distribution described?
- Did they accurately apply the empirical rule or IQR outlier fences?
- Did they match the chart type to the right analytical purpose?
- Is there a chart type, statistical measure, or business consideration they may have overlooked?

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| Statistical accuracy | 3 | Correct formulas, appropriate measure selection, accurate interpretation |
| Visualization justification | 2 | Chart type matches the data type and analytical goal |
| Depth of analysis | 2 | Goes beyond surface answers; considers business context |
| Peer response quality | 2 | Substantive engagement; adds new insight or asks probing questions |
| Writing clarity | 1 | Clear, organized, professional tone; within word count |

---

## Professor Nash Note

These scenarios are drawn from real analytics work in healthcare, e-commerce, and manufacturing — three of the largest employers of data analysts. As you write, think past the textbook definitions and consider the audience: how do you explain a standard deviation or a correlation coefficient to someone who has never taken a statistics course? That translation skill — from numbers to narrative — is what separates good analysts from great ones.

---

End of Module 07 Discussion

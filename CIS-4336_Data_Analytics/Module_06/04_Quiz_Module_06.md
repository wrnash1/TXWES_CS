# Quiz — Module 06: Statistical Analysis — Inferential Statistics and Hypothesis Testing

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 3: Data Analysis

---

## Question 1

A pharmaceutical company tests a new drug. The null hypothesis states that the drug has no effect on blood pressure. The study finds p = 0.03 with alpha = 0.05. What is the correct decision?

- A) Fail to reject H0, because 0.03 is close to 0.05
- B) Reject H0, because p = 0.03 is less than alpha = 0.05
- C) Accept H0, because the p-value is below 0.05
- D) Accept H1, because the result is statistically significant

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The decision rule is: if p-value <= alpha, reject H0. Since 0.03 <= 0.05, we reject the null hypothesis. This means there is statistically significant evidence that the drug affects blood pressure.
- **Why A is incorrect:** "Close to 0.05" is not a valid statistical criterion. The rule is strict: if p < 0.05, reject. 0.03 is below 0.05, so we reject H0.
- **Why C is incorrect:** In formal hypothesis testing, we never "accept" H0. We either reject it or fail to reject it. Saying "accept H0" implies it has been proven true, which is not what hypothesis testing establishes.
- **Why D is incorrect:** We also do not "accept H1" — we reject H0 and conclude the data provides evidence consistent with H1. This is a linguistic precision point that appears on the exam.

---

## Question 2

A medical screening test incorrectly identifies a healthy patient as having a disease, leading to unnecessary treatment. What type of error is this?

- A) Type II error (false negative)
- B) Type I error (false positive)
- C) Sampling error
- D) Measurement error

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A Type I error occurs when the null hypothesis is true (patient is healthy) but we reject it (test says they are sick). This produces a false positive — incorrectly flagging something that is not there.
- **Why A is incorrect:** A Type II error is a false negative — failing to detect something that is real. Here, the test detected something that is not real — that is a false positive (Type I).
- **Why C is incorrect:** Sampling error refers to variation between a sample statistic and the true population parameter due to random chance in sample selection. It is not the same as a wrong test decision.
- **Why D is incorrect:** Measurement error refers to inaccuracy in how a value is measured or recorded. A screening test making an incorrect classification is an error in the decision process, not in the measurement of a continuous variable.

---

## Question 3

A researcher sets alpha = 0.05 and conducts a hypothesis test. The result is p = 0.07. A colleague suggests lowering alpha to 0.10 to obtain a significant result. What is wrong with this approach?

- A) Nothing; changing alpha is a standard statistical practice
- B) Alpha must always equal 0.05 — it cannot be changed
- C) Adjusting alpha after seeing the data inflates the Type I error rate and represents p-hacking
- D) A p-value of 0.07 automatically means the null hypothesis is true

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The significance level must be set before collecting data. Changing alpha after seeing the p-value to make a result "significant" is called p-hacking or data dredging. It inflates the actual Type I error rate beyond the stated alpha and violates the integrity of hypothesis testing.
- **Why A is incorrect:** While alpha can legitimately be set at different levels for different research contexts, changing it after observing the data specifically to achieve significance is a methodological violation.
- **Why B is incorrect:** Alpha can legitimately be 0.01, 0.05, 0.10, or another value depending on the context and the consequences of errors. The issue is not what value is chosen, but when it is chosen.
- **Why D is incorrect:** A p-value of 0.07 means insufficient evidence to reject H0 at alpha = 0.05. It does not mean H0 is true — the data simply did not provide enough evidence to reject it.

---

## Question 4

Two variables have a Pearson correlation coefficient of r = 0.82. What is the most accurate interpretation?

- A) Variable A causes Variable B to change
- B) There is a very strong positive linear relationship between the two variables
- C) 82% of the data points lie on the regression line
- D) The variables are weakly correlated

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** r = 0.82 falls in the "very strong" range (0.80–1.00). The positive sign indicates both variables tend to increase together. A correlation coefficient describes the strength and direction of the linear relationship only.
- **Why A is incorrect:** Correlation does not imply causation. r = 0.82 tells us the variables co-vary strongly, not that one causes the other. A confounding variable or reverse causation might explain the relationship.
- **Why C is incorrect:** The percentage of variance explained by the linear relationship is r-squared (0.82 squared = 0.67), meaning about 67% of variance in one variable is explained by the other. 82% is not the percentage of data points on the line.
- **Why D is incorrect:** r = 0.82 is a very strong correlation by any standard interpretation. "Weakly correlated" would describe r values below 0.40.

---

## Question 5

A researcher finds a strong positive correlation between the number of fire trucks dispatched to a fire and the amount of property damage caused by the fire. Does this mean more fire trucks cause more damage?

- A) Yes, because the correlation is strong and positive
- B) No, because correlation does not imply causation — fire size is a confounding variable that causes both
- C) Yes, because statistical significance confirms a causal relationship
- D) No, because the Pearson r only applies to negative relationships

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** This is a classic confounding variable example. Larger fires cause both more damage and require more fire trucks. The number of trucks and the damage are both caused by fire size — neither causes the other. Correlation between them is spurious (appears causal but is not).
- **Why A is incorrect:** A strong positive correlation tells us the variables co-vary, not that one causes the other. Correlation strength is not evidence of causation.
- **Why C is incorrect:** Statistical significance means the correlation is unlikely to be zero in the population. It says nothing about the direction or existence of a causal mechanism.
- **Why D is incorrect:** Pearson r applies to both positive and negative linear relationships. The sign indicates direction; the magnitude indicates strength.

---

## Question 6

An analyst wants to test whether customer satisfaction scores (Satisfied / Not Satisfied) differ across three age groups (Under 30, 30–50, Over 50). Which statistical test is most appropriate?

- A) Independent samples t-test
- B) ANOVA
- C) Chi-square test of independence
- D) Paired t-test

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Both variables are categorical — satisfaction is binary (Satisfied/Not Satisfied) and age group is nominal with three categories. The chi-square test of independence tests whether two categorical variables are associated.
- **Why A is incorrect:** The independent samples t-test compares the means of two numeric groups. Satisfaction here is categorical (not a numeric score), and there are three groups, not two.
- **Why B is incorrect:** ANOVA compares the means of three or more groups when the outcome variable is numeric. Satisfaction here is categorical, not numeric.
- **Why D is incorrect:** A paired t-test compares two matched numeric measurements from the same subjects. The data here is categorical and from independent groups, not paired measurements.

---

## Question 7

A study with n = 10,000 participants finds that a new app feature increases daily session time by an average of 4 seconds (p < 0.001). What concern should an analyst raise about this finding?

- A) The sample size is too small to detect real effects
- B) The p-value should be higher for large samples
- C) The result is statistically significant but may not be practically significant
- D) A p-value below 0.001 automatically confirms causation

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** With very large samples, even tiny differences become statistically significant because the test has enormous statistical power. A 4-second increase in daily session time may be real (not due to chance) but is practically irrelevant from a product standpoint. Analysts must evaluate both statistical and practical significance.
- **Why A is incorrect:** n = 10,000 is a large sample. Large samples detect smaller effects more reliably — the concern is the opposite (over-detection of trivial effects).
- **Why B is incorrect:** p-values do not have a requirement to be above a certain level for large samples. Large samples tend to produce smaller p-values for the same effect size — which is exactly the concern.
- **Why D is incorrect:** No p-value confirms causation. Statistical significance (p < 0.001) means the effect is unlikely due to chance, not that the app feature caused the change through a confirmed mechanism.

---

## Question 8

What is statistical power?

- A) The probability of making a Type I error
- B) The probability of rejecting H0 when H0 is true
- C) The probability of correctly detecting a real effect when one exists (1 minus beta)
- D) The significance level alpha

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Statistical power = 1 minus beta, where beta is the probability of a Type II error. High power means the test is likely to detect a real effect when one exists. Power increases with larger sample sizes, larger effect sizes, and higher significance levels.
- **Why A is incorrect:** The probability of making a Type I error equals alpha (the significance level). Power is a different quantity.
- **Why B is incorrect:** Rejecting H0 when H0 is true is a Type I error, with probability alpha. Power is about correctly rejecting H0 when H0 is false.
- **Why D is incorrect:** Alpha is the significance level — the threshold for rejecting H0. Power is a different calculation related to Type II error.

---

## Question 9

A 95% confidence interval for the average delivery time is (4.2 days, 5.8 days). Which interpretation is correct?

- A) There is a 95% probability that the true mean is between 4.2 and 5.8 days
- B) 95% of all deliveries take between 4.2 and 5.8 days
- C) If this sampling process were repeated many times, 95% of the resulting confidence intervals would contain the true population mean
- D) The true mean is definitely between 4.2 and 5.8 days

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The correct interpretation of confidence intervals refers to the long-run frequency of the procedure. For any single interval, either the true mean is in it or it is not. Saying "95% of intervals constructed this way would contain the true mean" correctly describes the frequentist interpretation.
- **Why A is incorrect:** This is the most common misinterpretation. Once the interval is computed, the true mean is a fixed (unknown) value — not random. We cannot assign a probability to whether it falls in the interval.
- **Why B is incorrect:** A confidence interval for the mean describes uncertainty about the population mean, not the distribution of individual observations. A prediction interval would describe where individual values are likely to fall.
- **Why D is incorrect:** "Definitely" implies certainty. There is a 5% chance this specific interval does not contain the true mean.

---

## Question 10

An analyst is studying whether a new employee onboarding program reduces the time to full productivity. Before the program, 30 employees were measured. After the program, a different group of 30 new employees was measured. Which test should be used?

- A) Paired t-test, because two groups are being compared
- B) Independent samples t-test, because the two groups are different (unrelated) people
- C) Chi-square test, because productivity is a categorical outcome
- D) ANOVA, because there are more than two measurements per group

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The two groups consist of entirely different people — the "before" group and the "after" group are independent. An independent samples t-test compares means from two unrelated groups, which is the correct choice here.
- **Why A is incorrect:** A paired t-test requires each person in one group to be matched to a specific person in the other group (e.g., the same employee measured before and after the program). Since these are entirely different employees, the data is unpaired.
- **Why C is incorrect:** Time to full productivity is a numeric (ratio) variable, not categorical. The chi-square test is for categorical variable association, not numeric group comparisons.
- **Why D is incorrect:** ANOVA is used when comparing means across three or more groups. This scenario has exactly two groups. A t-test is the appropriate two-group comparison.

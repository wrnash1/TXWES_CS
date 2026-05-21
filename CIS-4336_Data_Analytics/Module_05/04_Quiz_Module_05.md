# Quiz: Module 05 - Statistical Foundations – Descriptive Statistics
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
Which method involves replacing missing dataset values with statistical estimates like mean or median?
*   A) Deletion
*   B) Imputation
*   C) Normalization
*   D) Deduplication
*   **Correct Answer:** B) Imputation replaces missing values with calculated substitutes rather than omitting records entirely, preserving sample size.
*   **Distractor Analysis:**
    *   *Why correct:* Imputation substitutes missing values with estimates derived from the existing data distribution.
    *   Deletion drops rows with missing values. Normalization reduces database redundancy. Deduplication removes duplicate records.

---

**Question 2**
In descriptive statistics, which of the following most accurately defines **deletion methods for handling missing data**?
*   A) Replacing missing values in a column with the column mean, median, or mode to retain all rows for analysis.
*   B) Removing rows (listwise deletion) or excluding specific variables from calculations (pairwise deletion) when data is missing, accepting the reduced sample size.
*   C) Converting missing value placeholders from one data type to another so the database engine can process them.
*   D) Applying a regex pattern to identify and remove whitespace characters that appear as blank but are not technically NULL.
*   **Correct Answer:** B) Removing rows (listwise deletion) or excluding specific variables from calculations (pairwise deletion) when data is missing, accepting the reduced sample size.
*   **Distractor Analysis:**
    *   *Why B is correct:* Deletion methods explicitly remove data points or rows containing missing values, which reduces the available sample.
    *   *Why A is incorrect:* This describes imputation, which retains rows by substituting estimates for missing values.
    *   *Why C is incorrect:* This describes type casting, a data transformation operation unrelated to handling missingness.
    *   *Why D is incorrect:* Whitespace removal is a text cleaning technique, not a missing-data strategy.

---

**Question 3**
A sorted dataset of 7 test scores is: 55, 62, 70, 74, 81, 88, 95. A student with a score of 200 (data entry error) is added, making 8 values. Which measure of central tendency is LEAST affected by this error?
*   A) Mean, because it uses all data values in its calculation.
*   B) Median, because it depends only on the middle values after sorting, not on extreme values.
*   C) Range, because it measures the spread from minimum to maximum.
*   D) Variance, because it squares each deviation from the mean.
*   **Correct Answer:** B) Median, because it depends only on the middle values after sorting, not on extreme values.
*   **Distractor Analysis:**
    *   *Why B is correct:* With 8 sorted values, the median is the average of the 4th and 5th values. The extreme value 200 only shifts sorting position; the middle values change minimally. Mean, range, and variance are all pulled heavily by the outlier.
    *   *Why A is incorrect:* The mean is calculated using all values, so the erroneous 200 inflates it significantly.
    *   *Why C is incorrect:* Range is maximally sensitive to outliers — it is defined as max minus min, so adding 200 dramatically increases it.
    *   *Why D is incorrect:* Variance squares deviations from the mean. When the mean is inflated by an outlier, variance is severely distorted.

---

**Question 4**
A dataset has Q1 = 40, Q3 = 70, and IQR = 30. Using the standard 1.5×IQR rule, which value would be flagged as an outlier?
*   A) 25, because it is below Q1.
*   B) 85, because it is above Q3.
*   C) 103, because it exceeds the upper fence of Q3 + 1.5×IQR = 70 + 45 = 115. Actually 103 < 115, so it is NOT an outlier.
*   D) 118, because it exceeds the upper fence of Q3 + 1.5×IQR = 70 + 45 = 115.
*   **Correct Answer:** D) 118, because it exceeds the upper fence of Q3 + 1.5×IQR = 70 + 45 = 115.
*   **Distractor Analysis:**
    *   *Why D is correct:* Upper fence = Q3 + 1.5×IQR = 70 + 1.5(30) = 70 + 45 = 115. Lower fence = Q1 − 1.5×IQR = 40 − 45 = −5. Any value above 115 or below −5 is an outlier. Only 118 exceeds 115.
    *   *Why A is incorrect:* 25 is above the lower fence of −5 (25 > −5), so it is not flagged as an outlier by the 1.5×IQR rule.
    *   *Why B is incorrect:* 85 is above Q3 but below the upper fence of 115 (85 < 115), so it is not an outlier.
    *   *Why C is incorrect:* This answer contains a self-correction — 103 is below the upper fence of 115 and is not an outlier.

---

**Question 5**
Two datasets each have a mean of 50. Dataset A has a standard deviation of 2; Dataset B has a standard deviation of 20. What does this difference tell an analyst?
*   A) Dataset A has more data points than Dataset B.
*   B) Dataset A's values are tightly clustered near 50, while Dataset B's values are widely spread around 50.
*   C) Dataset B has more missing values than Dataset A.
*   D) Both datasets are identical because they share the same mean.
*   **Correct Answer:** B) Dataset A's values are tightly clustered near 50, while Dataset B's values are widely spread around 50.
*   **Distractor Analysis:**
    *   *Why B is correct:* Standard deviation measures dispersion around the mean. SD=2 means most values are within 2 units of 50; SD=20 means values can be 20+ units away from 50. Same mean does not imply same distribution shape.
    *   *Why A is incorrect:* Standard deviation measures spread, not sample size. A dataset with 1,000 values can have a smaller standard deviation than one with 10 values.
    *   *Why C is incorrect:* Standard deviation does not indicate the rate of missing values; those are separate data quality metrics.
    *   *Why D is incorrect:* Two datasets can share the same mean while having completely different shapes and spreads — mean alone does not fully describe a distribution.

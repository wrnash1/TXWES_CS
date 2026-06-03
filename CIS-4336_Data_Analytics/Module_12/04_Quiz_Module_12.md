# Quiz: Module 12 — Python for Data Analysis

## Course: CIS-4336 Data Analytics

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** CompTIA Data+ (DA0-001)

**Instructions:** Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

An analyst has a pandas DataFrame with 50,000 rows. The `revenue` column has 2,300 null values. The analyst wants to preserve all rows and replace missing values with a central value that is resistant to outliers. Which approach is most appropriate?

A) `df['revenue'].fillna(df['revenue'].mean())` — fills nulls with the arithmetic mean, which is sensitive to outliers.

B) `df['revenue'].fillna(df['revenue'].median())` — fills nulls with the median, which is resistant to outliers and represents the middle of the distribution.

C) `df.dropna(subset=['revenue'])` — removes all rows with null revenue, discarding valid data in other columns.

D) `df['revenue'].fillna(0)` — fills nulls with zero, implying no revenue occurred, which may distort totals and averages.

#### Q1 Correct Answer: B

#### Q1 Distractor Analysis

A is incorrect because the mean is pulled by extreme values. C violates the requirement to preserve all rows. D is only appropriate when null genuinely means zero revenue, which is not stated here.

---

### Question 2

A data analyst wants to calculate the total units sold for each combination of region and product category from a single DataFrame. Which pandas operation accomplishes this most directly?

A) `pd.merge()` — combines two separate DataFrames on a shared key; does not aggregate within one table.

B) `df.pivot_table(values='units', index='region', columns='product', aggfunc='sum')` — reshapes and aggregates simultaneously, producing a totals matrix.

C) `df.describe()` — returns descriptive statistics for all numeric columns; does not group by region or product.

D) `df.sort_values(['region', 'product'])` — sorts rows but performs no aggregation.

#### Q2 Correct Answer: B

#### Q2 Distractor Analysis

A joins two tables rather than aggregating within one. C gives summary statistics for entire columns, not by group. D only reorders rows without computing totals.

---

### Question 3

Which of the following best describes the difference between `pd.merge()` with `how='inner'` versus `how='left'`?

A) `inner` keeps all rows from both tables; `left` keeps only rows present in the left table.

B) `inner` keeps only rows with matching keys in both tables; `left` keeps all rows from the left table and fills unmatched right columns with NaN.

C) `inner` adds new columns from the right table; `left` adds new columns from the left table.

D) `inner` and `left` produce identical results when the key column has no duplicates.

#### Q3 Correct Answer: B

#### Q3 Distractor Analysis

A reverses the definitions — `outer` keeps all rows from both tables. C describes column concatenation, not join behavior. D is incorrect because a left join retains left-table rows with no right match (filling with NaN), whereas inner drops them regardless.

---

### Question 4

An analyst calls `np.percentile(arr, [25, 75])` and gets `[18.5, 64.2]`. Using the standard 1.5×IQR rule, what are the outlier boundaries?

A) IQR = 45.7; lower = −50.05; upper = 132.75

B) IQR = 45.7; lower = 18.5; upper = 64.2

C) IQR = 82.7; lower = 18.5; upper = 64.2

D) IQR = 45.7; lower = −49.85; upper = 132.55

#### Q4 Correct Answer: A

#### Q4 Distractor Analysis

IQR = 64.2 − 18.5 = 45.7. Lower = 18.5 − (1.5 × 45.7) = −50.05. Upper = 64.2 + (1.5 × 45.7) = 132.75. B confuses quartile values with boundary values. C adds rather than subtracts quartiles. D has an arithmetic error in the lower bound.

---

### Question 5

Which seaborn function is most appropriate for visualizing the distribution of a single numeric variable and identifying whether it is skewed?

A) `sns.heatmap()` — displays a matrix of values; best for correlation matrices, not single-variable distributions.

B) `sns.scatterplot()` — shows the relationship between two numeric variables; requires two axes.

C) `sns.histplot()` — shows the frequency distribution of one numeric variable and reveals skewness, modality, and spread.

D) `sns.barplot()` — compares means across categories; requires a categorical grouping variable.

#### Q5 Correct Answer: C

#### Q5 Distractor Analysis

A requires a 2D matrix input. B requires two numeric variables. D requires a categorical grouping variable and shows means rather than distributions.

---

### Question 6

A dataset has a correlation coefficient of −0.87 between `support_tickets` and `customer_satisfaction_score`. What is the most accurate interpretation?

A) Increasing support tickets causes lower satisfaction scores — a strong negative causal relationship.

B) There is a strong negative linear association; as support tickets increase, satisfaction scores tend to decrease, but causation cannot be confirmed from correlation alone.

C) The two variables are unrelated because the coefficient is negative.

D) Approximately 87% of customers are dissatisfied when they submit a support ticket.

#### Q6 Correct Answer: B

#### Q6 Distractor Analysis

A incorrectly asserts causation; correlation never establishes cause. C is wrong — a coefficient of −0.87 indicates a strong inverse relationship. D misinterprets the coefficient as a percentage of customers.

---

### Question 7

An analyst calls `df.groupby('department')['salary'].mean().reset_index()`. What does `reset_index()` do in this context?

A) Removes all rows where the index is null.

B) Resets the DataFrame index to the default integer sequence, converting the grouped column back into a regular column rather than an index label.

C) Sorts the result by the department column in ascending order.

D) Recalculates the mean to exclude null salary values.

#### Q7 Correct Answer: B

#### Q7 Distractor Analysis

A is a null-handling operation unrelated to reset_index. C describes sort_values. D is incorrect because mean() already excludes nulls by default and reset_index does not affect calculations.

---

### Question 8

Which statement about NumPy vectorized operations is true?

A) Vectorized operations require a for-loop to iterate over each element of the array.

B) Vectorized operations apply a computation to all array elements simultaneously using compiled C code, which is significantly faster than a Python for-loop.

C) Vectorized operations only work on integer arrays; float arrays require explicit loops.

D) Vectorized operations produce a Python list, not an array, as output.

#### Q8 Correct Answer: B

#### Q8 Distractor Analysis

A contradicts the definition — eliminating explicit loops is the purpose of vectorization. C is false; NumPy supports float64, float32, and all numeric dtypes. D is false; operations on an ndarray return an ndarray.

---

### Question 9

A data analyst needs to combine a `transactions` table and a `products` table on `product_id`, keeping every transaction even when the product record is missing. Which call is correct?

A) `pd.merge(transactions, products, on='product_id', how='inner')` — drops transactions with no matching product.

B) `pd.merge(products, transactions, on='product_id', how='left')` — reverses table order; product table drives the join and may drop transactions.

C) `pd.merge(transactions, products, on='product_id', how='left')` — keeps every transaction; fills missing product columns with NaN.

D) `pd.merge(transactions, products, on='product_id', how='outer')` — retains all rows from both tables and fills both sides with NaN where unmatched.

#### Q9 Correct Answer: C

#### Q9 Distractor Analysis

A uses inner join and drops unmatched transactions. B reverses table positions so products drive the join. D is broader than necessary and produces extra rows from products that have no matching transaction.

---

### Question 10

Which Data+ exam domain is most directly tested by the Python for Data Analysis skills in Module 12?

A) Domain 1 — Data Concepts and Environments, covering data types and storage formats.

B) Domain 2 — Data Mining, covering data collection, transformation, and preparation.

C) Domain 3 — Data Analysis, covering statistical methods, Python tools, and analytical techniques.

D) Domain 5 — Data Governance, covering compliance, policies, and data quality standards.

#### Q10 Correct Answer: C

#### Q10 Distractor Analysis

A covers data fundamentals and infrastructure. B addresses some cleaning concepts but is broader than Python analysis techniques. D focuses on policy and compliance rather than programming and statistics.

---

### Answer Key

| Question | Correct Answer |
|---|---|
| 1 | B |
| 2 | B |
| 3 | B |
| 4 | A |
| 5 | C |
| 6 | B |
| 7 | B |
| 8 | B |
| 9 | C |
| 10 | C |

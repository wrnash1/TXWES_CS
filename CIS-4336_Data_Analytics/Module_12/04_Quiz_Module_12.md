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

---

### Question 11 (5 points)

An analyst has a DataFrame with a `date` column stored as object (string) dtype. After calling `pd.to_datetime(df['date'])`, what new capability becomes available?

A) `df['date'].str.contains('2024')` — string accessor methods work on datetime columns for pattern matching.

B) `df['date'].dt.month` — the `.dt` accessor exposes date/time components such as year, month, day, and day of week.

C) `df['date'].apply(len)` — calculates the character length of each date string.

D) `df['date'].value_counts()` — counting unique values requires datetime dtype.

#### Q11 Correct Answer: B

#### Q11 Distractor Analysis

After `pd.to_datetime()` conversion, the column becomes datetime64 dtype, enabling the `.dt` accessor for extracting year, month, day, hour, etc. A is a string accessor and does not work on datetime dtype. C measures string length and is unrelated to datetime conversion. D — `value_counts()` works on any dtype including object; it does not require datetime conversion.

---

### Question 12 (5 points)

Which pandas method produces a new column by applying a custom Python function to each row of a DataFrame?

A) `df.apply(func, axis=1)` — applies `func` to each row and returns a new Series or DataFrame.

B) `df.map(func)` — applies `func` element-wise to a single Series column but cannot access multiple columns simultaneously.

C) `df.transform(func)` — returns a DataFrame of the same shape but does not accept row-level custom functions with cross-column logic.

D) `df.agg(func)` — aggregates values within each column using `func`; does not compute row-level results.

#### Q12 Correct Answer: A

#### Q12 Distractor Analysis

`df.apply(func, axis=1)` passes each row as a Series to `func`, enabling logic that references multiple columns in the same row. B (`map`) operates element-wise on a single Series and cannot reference other columns. C (`transform`) returns same-shape output but is designed for group-wise transformations, not arbitrary row logic. D (`agg`) collapses each column to a scalar.

---

### Question 13 (5 points)

A pandas DataFrame column `region` contains the values: `['North', 'north', 'NORTH', 'South', 'south']`. After calling `df['region'].str.lower()`, how many unique values remain?

A) 5 — `str.lower()` does not merge case variants; all original strings remain distinct.

B) 3 — only the three 'North' variants are merged; 'South' variants remain separate.

C) 2 — all 'North' variants become 'north' and all 'South' variants become 'south'.

D) 1 — `str.lower()` converts all values to a single canonical representation.

#### Q13 Correct Answer: C

#### Q13 Distractor Analysis

`str.lower()` converts every string to lowercase, so 'North', 'north', and 'NORTH' all become 'north', and 'South' and 'south' both become 'south' — yielding 2 unique values. A is wrong because case normalization does merge variants. B undercounts; 'South' and 'south' are also merged. D is wrong because two distinct root words remain.

---

### Question 14 (5 points)

Which seaborn function is the best choice to visualize the pairwise relationships and distributions between four numeric columns in a single figure?

A) `sns.heatmap(df.corr())` — shows correlation coefficients but not the scatter distribution of raw values.

B) `sns.pairplot(df)` — creates a grid of scatter plots for every variable pair and histograms/KDE plots on the diagonal.

C) `sns.violinplot(data=df)` — shows the distribution of each variable independently, not pairwise relationships.

D) `sns.lineplot(data=df)` — connects data points with lines; appropriate for time-series, not pairwise relationship exploration.

#### Q14 Correct Answer: B

#### Q14 Distractor Analysis

`sns.pairplot()` produces an n×n grid showing scatter plots between every pair of variables and distribution plots on the diagonal — ideal for initial multivariate exploration. A shows correlation magnitudes, not raw distributions. C shows individual distributions without cross-variable comparison. D is designed for trend lines over an ordered axis.

---

### Question 15 (5 points)

An analyst creates a new column using: `df['price_tier'] = pd.cut(df['price'], bins=[0, 25, 75, 150], labels=['Low', 'Mid', 'High'])`. What happens to a row where `price = 0`?

A) It is assigned to the 'Low' tier because 0 is the minimum boundary.

B) It is assigned NaN because `pd.cut` intervals are open on the left by default, so 0 does not fall inside the (0, 25] interval.

C) It raises a ValueError because 0 cannot be a bin boundary and a data value simultaneously.

D) It is assigned to the 'Mid' tier because `pd.cut` rounds up to the nearest bin center.

#### Q15 Correct Answer: B

#### Q15 Distractor Analysis

By default, `pd.cut` uses left-open, right-closed intervals: (0, 25], (25, 75], (75, 150]. A value of exactly 0 is not inside any interval and receives NaN. To include the left boundary, use `include_lowest=True`. A is incorrect because the default left boundary is exclusive. C is incorrect; no error is raised. D is incorrect; `pd.cut` does not round to bin centers.

---

### Question 16 (5 points)

A DataFrame has 100,000 rows. An analyst wants to remove exact duplicate rows (all column values identical). Which call correctly removes duplicates and retains the first occurrence of each group?

A) `df.drop_duplicates(keep='first')` — removes all rows that are exact duplicates, keeping the first occurrence.

B) `df.dropna(how='all', keep='first')` — drops rows where all values are NaN; does not address duplicate rows.

C) `df.reset_index(drop=True)` — resets the integer index; does not remove any rows.

D) `df.unique()` — returns unique values from a single Series; does not operate on a full DataFrame.

#### Q16 Correct Answer: A

#### Q16 Distractor Analysis

`df.drop_duplicates(keep='first')` compares every column in each row and removes subsequent occurrences of identical rows, retaining the first. B handles missing values, not duplicates. C renumbers the index without changing row content. D is a Series method, not a DataFrame method, and returns values rather than filtering rows.

---

### Question 17 (5 points)

A matplotlib figure is saved with `plt.savefig('chart.png')` but all text and labels appear blurry when printed. What is the most likely cause and fix?

A) The figure was saved with the default DPI of 72; increasing to `dpi=150` or `dpi=300` produces a sharper image for print.

B) The `plt.show()` call must come before `plt.savefig()` or the image is blank.

C) Matplotlib does not support PNG format; use `plt.savefig('chart.pdf')` instead.

D) The `figsize` parameter controls DPI; increasing `figsize=(20, 12)` produces a higher-resolution image.

#### Q17 Correct Answer: A

#### Q17 Distractor Analysis

Matplotlib's default DPI is 100 (or 72 in some configurations), which is too low for crisp printing. Setting `dpi=150` or `dpi=300` increases pixel density. B is incorrect and reverses the correct order — `plt.savefig()` must come before `plt.show()` or the figure may already be cleared. C is false; Matplotlib fully supports PNG. D confuses figure size in inches with pixel density; `figsize` controls physical dimensions, not DPI.

---

### Question 18 (5 points)

An analyst runs `df.groupby('store_id')['revenue'].agg(['sum', 'mean', 'count'])` and gets back a DataFrame. What does the `count` column represent?

A) The number of non-null `revenue` values for each `store_id`.

B) The total number of rows in the original DataFrame.

C) The number of distinct `store_id` values in the group.

D) The number of stores in the dataset.

#### Q18 Correct Answer: A

#### Q18 Distractor Analysis

Within a `groupby`, `count` returns the number of non-null values in the aggregated column for each group — meaning the number of non-null `revenue` entries per `store_id`. B describes the total row count of the full DataFrame, not per group. C would require `nunique()`, not `count`. D is the number of unique groups, which is the number of rows in the resulting DataFrame, not a column value.

---

### Question 19 (5 points)

What is the primary advantage of using `df.query("sales > 5000 and region == 'North'")` over standard boolean indexing?

A) `query()` is the only method that supports AND conditions; boolean indexing can only apply one condition at a time.

B) `query()` uses a string expression that is often more readable and concise than chained boolean masks, and can reference column names directly without brackets.

C) `query()` executes faster than boolean indexing for all DataFrame sizes.

D) `query()` returns a copy of the filtered DataFrame; boolean indexing returns a view that causes SettingWithCopyWarning.

#### Q19 Correct Answer: B

#### Q19 Distractor Analysis

`df.query()` allows natural language-like filtering strings, improving readability when multiple conditions are combined. A is false — boolean indexing supports AND (`&`) and OR (`|`) with multiple conditions. C is false — for small DataFrames, query may be slightly slower; the speed advantage appears mainly at scale. D is an oversimplification; both methods can return views or copies depending on context.

---

### Question 20 (5 points)

A NumPy array `arr` contains test scores. Which expression correctly identifies all scores that are more than 1.5 standard deviations above the mean?

A) `arr[arr > np.mean(arr) + 1.5]` — compares to the mean plus 1.5, not 1.5 standard deviations above the mean.

B) `arr[arr > np.mean(arr) + 1.5 * np.std(arr)]` — correctly calculates the threshold as mean plus 1.5 times standard deviation.

C) `arr[np.percentile(arr, 85)]` — returns the 85th percentile value, not a boolean mask for filtering.

D) `arr[arr.std() > 1.5]` — compares the scalar standard deviation to 1.5, producing a single boolean, not an element-wise mask.

#### Q20 Correct Answer: B

#### Q20 Distractor Analysis

The threshold for 1.5 standard deviations above the mean is `mean + 1.5 × std`. `np.std(arr)` computes the standard deviation and `np.mean(arr)` computes the mean; the expression `arr > np.mean(arr) + 1.5 * np.std(arr)` produces a boolean mask for filtering. A omits the standard deviation scaling. C returns a scalar value, not a mask. D applies `std()` as a scalar comparison to 1.5, which is conceptually wrong.

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
| 11 | B |
| 12 | A |
| 13 | C |
| 14 | B |
| 15 | B |
| 16 | A |
| 17 | A |
| 18 | A |
| 19 | B |
| 20 | B |

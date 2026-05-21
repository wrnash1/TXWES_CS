# Quiz: Module 09 - Python for Data Analytics – Pandas and NumPy
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

**Question 1**
An analyst loads a CSV file into Python and needs to check how many rows and columns the dataset contains, confirm each column's data type, and count null values per column before beginning any analysis. Which Pandas methods accomplish this profiling step?
*   A) `df.head()`, `df.tail()`, and `df.sample()`
*   B) `df.shape`, `df.dtypes`, and `df.isnull().sum()`
*   C) `df.sort_values()`, `df.dropna()`, and `df.reset_index()`
*   D) `df.merge()`, `df.concat()`, and `df.pivot_table()`
*   **Correct Answer:** B) `df.shape`, `df.dtypes`, and `df.isnull().sum()`
*   **Distractor Analysis:**
    *   *Why correct:* `df.shape` returns the (rows, columns) tuple; `df.dtypes` lists each column's data type; `df.isnull().sum()` counts NaN values per column. Together these three calls form a standard initial data profile.
    *   A) `head()`, `tail()`, and `sample()` preview row content but do not report dimensions, types, or null counts. C) These are cleaning and reshaping methods, not profiling methods. D) These are merging and aggregation methods unrelated to basic profiling.

---

**Question 2**
In Python data analytics, which of the following most accurately defines a **Pandas DataFrame**?
*   A) A one-dimensional labeled array representing a single column of data, with an index and a uniform data type, used as the building block for tabular structures.
*   B) A fixed-type multi-dimensional array provided by NumPy that supports vectorized arithmetic operations across entire arrays without Python loops.
*   C) A two-dimensional, labeled tabular data structure where each column is a named Series, each row is an indexed observation, and operations such as filtering, grouping, and merging are available.
*   D) A connection object that links a Python script to an external database and executes SQL queries, returning results as rows and columns.
*   **Correct Answer:** C) A two-dimensional, labeled tabular data structure where each column is a named Series, each row is an indexed observation, and operations such as filtering, grouping, and merging are available.
*   **Distractor Analysis:**
    *   *Why C is correct:* A DataFrame is Pandas' core tabular structure — the Python equivalent of a database table or spreadsheet, with named columns, row indices, and a rich API for data manipulation.
    *   *Why A is incorrect:* A one-dimensional labeled array describes a Pandas Series, which is a single column extracted from a DataFrame — not the DataFrame itself.
    *   *Why B is incorrect:* A fixed-type multi-dimensional array for vectorized arithmetic describes a NumPy ndarray, not a Pandas DataFrame.
    *   *Why D is incorrect:* A connection object for executing SQL queries describes a database connector (such as SQLAlchemy or psycopg2), not a DataFrame.

---

**Question 3**
A data analyst is working with a customer dataset where 42% of values in the `annual_income` column are missing. The income distribution is heavily right-skewed due to a small number of high earners. Which missing-value strategy is most appropriate?
*   A) Use `df.dropna(subset=['annual_income'])` to remove all rows with missing income, accepting the significant reduction in sample size.
*   B) Use `df.fillna(df['annual_income'].mean())` to replace missing values with the column mean.
*   C) Use `df.fillna(df['annual_income'].median())` to replace missing values with the column median, which is more resistant to the skewed distribution.
*   D) Leave the missing values as NaN and proceed with analysis, since Pandas handles NaN automatically in all operations.
*   **Correct Answer:** C) Use `df.fillna(df['annual_income'].median())` to replace missing values with the column median, which is more resistant to the skewed distribution.
*   **Distractor Analysis:**
    *   *Why C is correct:* With 42% missing and a right-skewed distribution, dropping rows would remove nearly half the dataset, introducing bias. The median is preferred over the mean for imputation because it is not pulled toward the high-earning outliers that cause the skew.
    *   *Why A is incorrect:* Dropping 42% of rows is a severe reduction that would likely bias the remaining sample toward lower-income customers, distorting any analysis.
    *   *Why B is incorrect:* In a right-skewed income distribution, the mean is significantly higher than the typical value due to high outliers. Imputing with the mean would inflate artificially the incomes of missing-value rows.
    *   *Why D is incorrect:* While Pandas skips NaNs in some aggregate functions, other operations (comparisons, machine learning inputs, exports) fail or produce incorrect results with NaNs present. Leaving them unresolved is not a valid strategy.

---

**Question 4**
An analyst needs to compute the total revenue and average order value for each product category in a Pandas DataFrame with columns `category`, `revenue`, and `order_value`. Which code correctly produces these grouped statistics?
*   A) `df.sort_values('category')[['revenue', 'order_value']].sum()`
*   B) `df.groupby('category')[['revenue', 'order_value']].agg({'revenue': 'sum', 'order_value': 'mean'})`
*   C) `df.pivot('category', 'revenue', 'order_value')`
*   D) `df.merge(df, on='category')[['revenue', 'order_value']].describe()`
*   **Correct Answer:** B) `df.groupby('category')[['revenue', 'order_value']].agg({'revenue': 'sum', 'order_value': 'mean'})`
*   **Distractor Analysis:**
    *   *Why B is correct:* `groupby('category')` splits the DataFrame by category, and `.agg()` applies different aggregation functions to each column — sum for revenue, mean for order_value. This is the direct Pandas equivalent of `SELECT category, SUM(revenue), AVG(order_value) FROM table GROUP BY category`.
    *   *Why A is incorrect:* `sort_values` orders rows alphabetically by category but does not group them. The `.sum()` call would then sum all rows, not per-category totals.
    *   *Why C is incorrect:* `df.pivot()` reshapes a DataFrame by spreading one column's values into new columns — it is a pivoting operation, not a grouped aggregation.
    *   *Why D is incorrect:* `df.merge(df, on='category')` performs a self-join, multiplying rows. `describe()` returns distribution statistics for the whole result, not per-category aggregations.

---

**Question 5**
A NumPy array `prices` contains 10,000 product prices. An analyst needs to add a 10% tax to every price and find the maximum taxed price. Which approach is most efficient in NumPy?
*   A) Write a Python `for` loop that iterates over each element, multiplies it by 1.10, appends it to a new list, then calls `max()` on the list.
*   B) Use `prices * 1.10` to apply the tax via vectorized multiplication, then call `(prices * 1.10).max()` to find the maximum.
*   C) Convert the array to a Pandas DataFrame, use `df['prices'].apply(lambda x: x * 1.10)`, then call `.max()` on the result.
*   D) Use `numpy.sort(prices)` to sort the array in descending order, multiply the first element by 1.10 to get the maximum taxed price.
*   **Correct Answer:** B) Use `prices * 1.10` to apply the tax via vectorized multiplication, then call `(prices * 1.10).max()` to find the maximum.
*   **Distractor Analysis:**
    *   *Why B is correct:* NumPy's vectorized operations apply the multiplication to every element in the array simultaneously using optimized C-level code — no Python loop is needed. This is both the idiomatic and the most performant approach for array-wide arithmetic.
    *   *Why A is incorrect:* A Python for loop achieves the same result but is orders of magnitude slower on 10,000 elements because it executes in interpreted Python rather than compiled code. It also produces a list, not a NumPy array.
    *   *Why C is incorrect:* Converting to a DataFrame and using `.apply()` introduces unnecessary overhead. `.apply()` with a lambda also iterates row by row in Python, losing the performance benefit of NumPy vectorization.
    *   *Why D is incorrect:* Sorting the entire array to find the maximum is an O(n log n) operation when `.max()` is O(n). More critically, sorting first and then multiplying only the first element does not apply the tax to the whole array.

# Quiz — Module 01: Data Analytics Fundamentals and Data Types

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1

---

## Question 1

What type of data is a database table containing customer names, transaction dates, and currency values classified as?

- A) Unstructured data
- B) Semi-structured data
- C) Structured data
- D) Qualitative data only

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A relational database table has a predefined schema with named columns and consistent data types across every row. That rigid, schema-enforced organization is the defining characteristic of structured data.
- **Why A is incorrect:** Unstructured data has no predefined schema. Examples include email bodies, audio files, and images — none of which conform to rows and columns.
- **Why B is incorrect:** Semi-structured data (JSON, XML) has partial organization through tags or keys but no rigid schema. A database table's schema is fully enforced, not partial.
- **Why D is incorrect:** The table contains both qualitative columns (names) and quantitative columns (currency values). Labeling the entire table "qualitative only" ignores the quantitative fields and the structure classification is separate from the qualitative/quantitative distinction.

---

## Question 2

Which of the following most accurately defines the difference between qualitative and quantitative variables?

- A) Quantitative variables are numeric measurements that support arithmetic operations such as averaging; qualitative variables represent labels or groups that cannot be meaningfully averaged.
- B) Quantitative variables are always stored as text in a database; qualitative variables are always stored as integers.
- C) Qualitative variables are the only type used in business intelligence dashboards; quantitative variables are reserved for scientific research.
- D) The distinction is purely theoretical and has no effect on which statistical methods an analyst should apply.

**Correct Answer:** A

**Distractor Analysis:**

- **Why A is correct:** This definition captures the operationally critical distinction. Quantitative variables support arithmetic (mean, sum, standard deviation); qualitative variables support counting and ranking at most.
- **Why B is incorrect:** Storage format — text vs. integer — does not determine the variable type. A zip code stored as an integer is still nominal qualitative; a Likert score stored as text is still ordinal.
- **Why C is incorrect:** Both variable types appear in business intelligence and scientific contexts. Revenue (quantitative) and region (qualitative) both appear on typical BI dashboards.
- **Why D is incorrect:** The distinction is practically significant. Averaging a qualitative variable like product category produces a meaningless number and misrepresents the data.

---

## Question 3

An analyst receives a folder of 5,000 customer feedback emails saved as plain text files. Which data type does this represent, and what is the correct first step?

- A) Structured data; load it directly into a relational database without modification.
- B) Unstructured data; apply a preprocessing step such as text parsing or NLP tokenization before analysis.
- C) Semi-structured data; query it directly with standard SQL without transformation.
- D) Quantitative data; calculate the mean of all emails to find the central tendency.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Plain text email bodies have no predefined schema and cannot be queried with SQL directly. They are unstructured and require preprocessing — tokenization, stop-word removal, or sentiment scoring — before meaningful analysis.
- **Why A is incorrect:** Loading raw unstructured text into a relational database without preprocessing produces uncategorized text blobs that cannot be aggregated or analyzed meaningfully.
- **Why C is incorrect:** Semi-structured data such as JSON has named keys that enable programmatic traversal. Free-text emails have no such markers and are not semi-structured.
- **Why D is incorrect:** Email text is qualitative, not quantitative. Computing a mean on text is not a valid operation.

---

## Question 4

During which phase of the data analytics lifecycle does an analyst create charts and dashboards to communicate findings to executives?

- A) Data collection
- B) Data cleaning and transformation
- C) Visualize and communicate
- D) Define the question

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The visualization and communication phase is specifically where analysts translate analytical results into charts, dashboards, and narratives for stakeholder audiences.
- **Why A is incorrect:** Data collection is the second lifecycle stage, focused on acquiring raw data from sources. No charts are produced here.
- **Why B is incorrect:** The cleaning and transformation stage addresses data quality issues and prepares data for analysis. Chart creation is not part of this stage.
- **Why D is incorrect:** Defining the question is the first lifecycle stage, focused on clarifying the business problem before any data is collected or analyzed.

---

## Question 5

A dataset contains the column "Customer Satisfaction Score" with integer values from 1 to 5. How should this variable be classified?

- A) Continuous quantitative, because it uses numbers.
- B) Ordinal qualitative, because the numbers represent ranked categories with unequal intervals.
- C) Nominal qualitative, because all five values are equally ranked with no ordering.
- D) Discrete quantitative, because it can only take whole-number values.

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A five-point Likert scale uses numbers as labels for ordered categories. The difference between a 1 and a 2 is not guaranteed to be psychologically equivalent to the difference between a 4 and a 5, so this is ordinal, not truly quantitative.
- **Why A is incorrect:** Being stored as a number does not make a variable continuous or quantitative. The measurement scale — not the storage format — determines the classification.
- **Why C is incorrect:** Nominal variables have no ordering. Satisfaction scores from 1 to 5 are clearly ordered: 5 is higher satisfaction than 1.
- **Why D is incorrect:** While whole numbers are involved, "discrete quantitative" implies meaningful arithmetic (e.g., count of transactions). Arithmetic on a satisfaction scale produces misleading results.

---

## Question 6

A supply chain team wants to know which delivery route to assign to each truck to minimize total fuel costs. Which type of analytics does this represent?

- A) Descriptive analytics
- B) Diagnostic analytics
- C) Predictive analytics
- D) Prescriptive analytics

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** Prescriptive analytics recommends a specific action — here, the optimal route assignment. It goes beyond predicting outcomes to recommending decisions.
- **Why A is incorrect:** Descriptive analytics summarizes what has already happened; it does not recommend future actions.
- **Why B is incorrect:** Diagnostic analytics investigates causes of past events; it does not assign routes or optimize future decisions.
- **Why C is incorrect:** Predictive analytics forecasts what is likely to happen (e.g., predicting fuel consumption for a given route) but does not itself recommend the action to take.

---

## Question 7

A JSON file returned from a weather API contains nested objects with location, temperature, and forecast data. Some records include an optional "alerts" array; others do not. How should this data be classified?

- A) Structured, because it contains named fields
- B) Unstructured, because the schema varies between records
- C) Semi-structured, because it uses named keys but does not enforce a rigid schema across all records
- D) Quantitative, because it includes numeric temperature values

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** JSON uses named keys (partial organization) but does not require every record to have identical keys or structure. This is the definition of semi-structured data.
- **Why A is incorrect:** Structured data requires every record to conform to the same predefined schema. Optional fields and nested arrays of variable length violate that constraint.
- **Why B is incorrect:** Unstructured data has no organizational tags or keys at all. JSON's key-value structure provides partial organization, placing it in the semi-structured category.
- **Why D is incorrect:** Quantitative vs. qualitative describes the nature of individual values, not the structural classification of an entire file format.

---

## Question 8

Which scale of measurement applies to the outdoor temperature recorded in degrees Celsius?

- A) Nominal
- B) Ordinal
- C) Interval
- D) Ratio

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Celsius temperature has equal intervals (each degree represents the same change in thermal energy) but no true zero point — 0 degrees Celsius does not mean the absence of heat. This is the defining characteristic of the interval scale.
- **Why A is incorrect:** Nominal scale applies to unordered categories. Temperature values are clearly ordered and numeric.
- **Why B is incorrect:** Ordinal scale applies to ordered categories with unequal intervals. Celsius has equal, known intervals between degrees.
- **Why D is incorrect:** Ratio scale requires a true zero point meaning the complete absence of the quantity. Zero Celsius is not the absence of heat; that distinction belongs to the Kelvin scale.

---

## Question 9

An analyst reviews last quarter's sales data and produces a summary report showing total revenue, units sold, and average order value by region. Which analytics type does this activity represent?

- A) Diagnostic
- B) Descriptive
- C) Predictive
- D) Prescriptive

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Summarizing historical data — revenue, units, and averages from last quarter — to answer "what happened?" is the definition of descriptive analytics.
- **Why A is incorrect:** Diagnostic analytics investigates causes. Simply reporting summary metrics from last quarter does not investigate why those metrics are at their current level.
- **Why C is incorrect:** Predictive analytics uses models to forecast future values. Summarizing past data does not constitute a forecast.
- **Why D is incorrect:** Prescriptive analytics recommends specific actions. A summary report does not prescribe any decision.

---

## Question 10

A data analyst is working with a dataset and needs to decide which statistical operations are valid for a given variable. What determines which operations are appropriate?

- A) The size of the dataset
- B) The file format in which the data is stored
- C) The scale of measurement of the variable
- D) The analyst's preferred software tool

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** The scale of measurement — nominal, ordinal, interval, or ratio — defines which mathematical and statistical operations produce meaningful results. Computing a mean on a nominal variable is mathematically possible but analytically meaningless.
- **Why A is incorrect:** Dataset size affects statistical power and computational requirements but does not determine which operations are logically valid for a variable type.
- **Why B is incorrect:** File format (CSV, JSON, Parquet) describes how data is stored, not the nature of the values. The same ordinal variable stored in CSV or a database is still ordinal.
- **Why D is incorrect:** Software tools can compute any operation mechanically. The tool's capability is not the standard for validity — the measurement scale is.

---

### Question 11 (5 points)

Which of the following is an example of ratio-scale data?

- A) A student's letter grade (A, B, C, D, F)
- B) Calendar year of a company's founding (e.g., 1995, 2003)
- C) Number of customer complaints received per week
- D) Temperature measured in degrees Fahrenheit

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** Weekly complaint count is ratio-scale — it has equal intervals, a true zero (zero complaints means no complaints), and supports all arithmetic operations including meaningful ratios.
  - **Why A is incorrect:** Letter grades are ordinal qualitative. The gap between A and B is not the same magnitude as between C and D, and no true zero exists.
  - **Why B is incorrect:** Calendar years are interval-scale, not ratio. The year 0 is a calendar convention, not the true absence of time, so ratios ("twice as old") are meaningless.
  - **Why D is incorrect:** Fahrenheit temperature is interval-scale because 0°F does not represent the absence of heat. Ratio statements like "60°F is twice as warm as 30°F" are invalid.

---

### Question 12 (5 points)

An analyst wants to investigate why a retailer's online conversion rate dropped 18 percent last month. Which analytics type best describes this investigation?

- A) Descriptive analytics
- B) Diagnostic analytics
- C) Predictive analytics
- D) Prescriptive analytics

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Diagnostic analytics investigates the root cause of a known event — here, explaining why the conversion rate fell. The defining question is "why did it happen?"
  - **Why A is incorrect:** Descriptive analytics would have produced the summary metric showing the 18-percent drop, but it does not investigate the cause.
  - **Why C is incorrect:** Predictive analytics would forecast future conversion rates, not explain what caused a past change.
  - **Why D is incorrect:** Prescriptive analytics would recommend specific actions to improve conversion; investigation of cause comes before any recommendation.

---

### Question 13 (5 points)

A healthcare organization stores patient MRI scan images in a cloud object store and radiology report text in a separate database table. How should these two data sources be classified?

- A) Both are unstructured
- B) MRI images are unstructured; radiology report text in a table is structured
- C) MRI images are semi-structured; radiology report text is unstructured
- D) Both are structured because they are organized in the same system

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Image files have no predefined schema and are unstructured. A database table with defined columns is structured, even if the text values inside one column vary in length.
  - **Why A is incorrect:** The radiology reports stored in a relational table with defined columns conform to a schema, making that source structured, not unstructured.
  - **Why C is incorrect:** Semi-structured data uses tags or keys (like JSON). Raw image files have no such organizational markup.
  - **Why D is incorrect:** Physical co-location in the same system does not determine structural classification. Schema enforcement determines structure.

---

### Question 14 (5 points)

In the data analytics lifecycle, which stage is most concerned with ensuring data quality dimensions such as completeness, consistency, and accuracy?

- A) Define the question
- B) Collect data
- C) Clean and transform
- D) Act and monitor

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** The clean and transform stage directly addresses data quality. Analysts handle null values, remove duplicates, correct inconsistencies, and standardize formats during this stage.
  - **Why A is incorrect:** Defining the question focuses on business problem scope and success criteria, not on the quality of raw data.
  - **Why B is incorrect:** Data collection focuses on acquiring raw data from sources. Quality issues are identified here but corrected in the next stage.
  - **Why D is incorrect:** Act and monitor measures outcomes after deployment. Data quality remediation has already occurred before reaching this stage.

---

### Question 15 (5 points)

A dataset column contains values such as "TX," "CA," "NY," and "FL" representing U.S. state abbreviations. Which classification and valid operation are correct?

- A) Ordinal qualitative; compute the median state abbreviation
- B) Nominal qualitative; compute the mode (most frequent state)
- C) Interval quantitative; compute the mean of state abbreviations
- D) Ratio quantitative; compute the sum of state abbreviations

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** State abbreviations are categories with no inherent order — nominal qualitative. The only meaningful summary is counting frequencies and identifying the most common value (mode).
  - **Why A is incorrect:** Ordinal requires a meaningful ordering. There is no natural ranking among state abbreviations, so ordinal classification is incorrect.
  - **Why C is incorrect:** State abbreviations are not numeric and have no quantitative meaning. Treating them as interval data and computing a mean is invalid.
  - **Why D is incorrect:** Abbreviations cannot be summed. They are categorical labels, not numeric quantities.

---

### Question 16 (5 points)

Which statement best explains why a data analyst must understand measurement scales before selecting a statistical method?

- A) Measurement scales determine how large the dataset must be before analysis can begin.
- B) Measurement scales dictate which mathematical and statistical operations produce meaningful results for a given variable.
- C) Measurement scales are only relevant when using spreadsheet software, not Python or SQL.
- D) Measurement scales affect only the visualization choice, not the underlying statistical test.

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Each measurement scale permits specific operations. Ratio-scale data supports all arithmetic; ordinal supports median but not mean; nominal supports only frequency counts. Applying an inappropriate operation produces misleading results.
  - **Why A is incorrect:** Dataset size affects statistical power and sampling considerations, but it is independent of measurement scale. A small ratio-scale dataset and a large nominal dataset both follow the same operational rules for their respective scales.
  - **Why C is incorrect:** Measurement scale is a property of the data, not the software. Python, SQL, Excel, and R all face the same validity constraints when operating on ordinal or nominal data.
  - **Why D is incorrect:** Measurement scale affects both visualization choices and statistical test selection. Choosing a bar chart vs. histogram is influenced by scale, but so is choosing a chi-square test vs. a t-test.

---

### Question 17 (5 points)

A logistics company builds a machine learning model that predicts parcel delivery delays 48 hours in advance based on weather, carrier load, and historical delay patterns. Which analytics type does this represent?

- A) Descriptive analytics
- B) Diagnostic analytics
- C) Predictive analytics
- D) Prescriptive analytics

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** Predictive analytics uses historical patterns and statistical models to forecast future outcomes. A model that predicts delays 48 hours in advance is squarely predictive.
  - **Why A is incorrect:** Descriptive analytics reports on what has already occurred. Forecasting a future event is not descriptive.
  - **Why B is incorrect:** Diagnostic analytics explains the cause of a past event, not a future one. The goal here is prediction, not root-cause investigation.
  - **Why D is incorrect:** Prescriptive analytics would go further by recommending specific actions — for example, suggesting which packages to reroute. Predicting a delay is not yet a recommendation.

---

### Question 18 (5 points)

Which pandas method is most appropriate for computing the frequency distribution of a nominal qualitative column such as "product_category"?

- A) `df["product_category"].mean()`
- B) `df["product_category"].describe()`
- C) `df["product_category"].value_counts()`
- D) `df["product_category"].std()`

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** `value_counts()` returns the count of each unique value in a Series, which is the appropriate summary for nominal qualitative data.
  - **Why A is incorrect:** `.mean()` requires numeric data and will raise a TypeError on a string column. Even if categories were encoded as integers, averaging nominal data is meaningless.
  - **Why B is incorrect:** `.describe()` on an object-dtype column returns count, unique, top, and frequency — partial information, but `value_counts()` provides a complete frequency table sorted by frequency, which is the standard approach.
  - **Why D is incorrect:** `.std()` computes standard deviation, a numeric operation that is invalid for nominal string data.

---

### Question 19 (5 points)

What distinguishes a data warehouse from a data lake in an analytics architecture?

- A) A data warehouse stores only unstructured data; a data lake stores only structured data.
- B) A data warehouse enforces a predefined schema and stores processed, structured data optimized for querying; a data lake stores raw data of any structure.
- C) A data lake requires SQL queries; a data warehouse uses Python scripts only.
- D) A data warehouse is hosted on-premises only; a data lake exists exclusively in the cloud.

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Data warehouses use schema-on-write — data is structured and cleaned before loading. Data lakes use schema-on-read — raw data in any format is stored first, and structure is applied at query time.
  - **Why A is incorrect:** This reverses the actual distinction. Warehouses store structured data; lakes store all types including unstructured.
  - **Why C is incorrect:** Both architectures support SQL and Python. Many data lake platforms (e.g., Databricks, AWS Athena) support SQL queries on raw files.
  - **Why D is incorrect:** Both data warehouses and data lakes can be on-premises or cloud-hosted. The distinction is about data structure and schema enforcement, not deployment location.

---

### Question 20 (5 points)

A dataset contains a "date_of_birth" column. What scale of measurement applies to this column, and which arithmetic operation is valid?

- A) Ratio scale; computing the average birth year is meaningful because year zero is a true zero point.
- B) Interval scale; computing the difference between two dates (elapsed days) is valid, but ratios such as "twice as old" are not.
- C) Ordinal scale; birth dates can only be ranked but differences cannot be computed.
- D) Nominal scale; birth dates are labels with no mathematical meaning.

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Calendar dates are interval-scale. The difference between dates is meaningful and equal-interval (elapsed days), but there is no true zero point — year zero is a calendar convention, not the absence of time — so ratios are invalid.
  - **Why A is incorrect:** Calendar year zero is not a true zero in the ratio-scale sense. Saying a person born in 2000 is "twice as old" as one born in 1000 is meaningless on the Gregorian calendar.
  - **Why C is incorrect:** Ordinal data supports ranking only, with unequal or unknown intervals. Date arithmetic produces precise, equal-interval differences in days, hours, or years, exceeding ordinal capability.
  - **Why D is incorrect:** Nominal data has no mathematical meaning. Dates clearly support subtraction (difference), which rules out nominal classification.

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

# Quiz — Module 02: Data Collection and Data Sources

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 20 (2 points each)
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1 and Domain 2

---

## Question 1

A marketing analyst designs and administers a new customer survey specifically to understand why churn increased last quarter. What type of data source does this represent?

- A) Secondary data, because the data already existed in the CRM system
- B) Primary data, because the analyst collected it directly for this specific analytical purpose
- C) Tertiary data, because it was derived from an existing business question
- D) Structured data, because surveys use fixed response categories

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Primary data is collected directly by the analyst or their organization for the specific current purpose. Designing and administering a new survey for this question is the definition of primary data collection.
- **Why A is incorrect:** The survey is new — the data does not exist yet in the CRM or anywhere else. CRM data would be secondary, but a newly designed and administered survey is primary.
- **Why C is incorrect:** "Tertiary data" is not a standard category in the CompTIA Data+ framework. The two-category distinction is primary and secondary.
- **Why D is incorrect:** Structured vs. unstructured describes the format and schema of data, not who collected it or for what purpose. Structure classification and source classification are independent.

---

## Question 2

A company's point-of-sale system records every transaction in real time, optimized for fast writes with a normalized schema. What type of database system is this?

- A) OLAP — Online Analytical Processing
- B) Data warehouse
- C) OLTP — Online Transaction Processing
- D) Data lake

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** OLTP systems are designed for operational transaction recording — fast writes, row-level access, normalized schemas. A point-of-sale system recording transactions in real time is a textbook OLTP example.
- **Why A is incorrect:** OLAP systems are designed for analytical queries on historical data with denormalized schemas. They do not record transactions in real time.
- **Why B is incorrect:** A data warehouse is an OLAP environment that stores integrated historical data for analysis. It does not serve as the live operational recording system for transactions.
- **Why D is incorrect:** A data lake stores raw data in native format, including unstructured data, and is used for broad analytical storage — not real-time transactional recording.

---

## Question 3

In a star schema, a central SALES_FACT table contains ORDER_ID, CUSTOMER_ID, PRODUCT_ID, DATE_ID, and AMOUNT. Three separate tables exist for CUSTOMER, PRODUCT, and DATE dimensions. The CUSTOMER dimension has no sub-tables. What schema pattern does this describe?

- A) Snowflake schema, because there are multiple dimension tables
- B) Third normal form, because the fact table references other tables
- C) Star schema, because the fact table connects directly to flat, un-normalized dimension tables
- D) Entity-relationship model, because primary and foreign keys are used

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** A star schema has a central fact table with foreign keys pointing directly to flat (un-normalized) dimension tables. The diagram resembles a star. The key distinguishing feature is that dimension tables are not further split into sub-tables.
- **Why A is incorrect:** A snowflake schema requires dimension tables to be further normalized into sub-dimension tables (e.g., CUSTOMER splits into CUSTOMER and CUSTOMER_ADDRESS). Flat, un-normalized dimension tables indicate a star schema.
- **Why B is incorrect:** Third normal form (3NF) is a normalization standard used primarily for OLTP operational systems. A fact-dimension design with denormalized dimensions is an OLAP pattern, not 3NF.
- **Why D is incorrect:** Entity-relationship model refers to a design notation and methodology, not a specific schema pattern. Both star and snowflake schemas use primary and foreign keys.

---

## Question 4

During an ETL pipeline, an engineer discovers that the COUNTRY column contains "US," "USA," "United States," and "U.S.A." for the same country. The engineer writes logic to standardize all variations to "United States." Which ETL stage does this activity belong to?

- A) Extract
- B) Transform
- C) Load
- D) Index

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** The Transform stage is where data is cleaned, standardized, and reshaped. Normalizing inconsistent string values to a canonical form is a classic transformation activity.
- **Why A is incorrect:** The Extract stage pulls data from source systems. It does not apply business logic or cleaning rules to the data.
- **Why C is incorrect:** The Load stage writes the already-transformed data to the target store. Standardization logic belongs before loading.
- **Why D is incorrect:** Index is not a standard ETL stage. Indexing is a database optimization activity that may happen after loading, but it is not part of the ETL acronym.

---

## Question 5

An analyst queries the company's production CRM database directly with a complex JOIN across six tables to generate a quarterly analysis report. This query takes 45 minutes to complete. What is the primary problem with this approach?

- A) The analyst should use Python instead of SQL for complex joins
- B) Joining six tables is not supported in relational databases
- C) Running heavy analytical queries on an OLTP system degrades performance for operational users and risks data integrity issues
- D) The query is too long to be valid SQL syntax

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** OLTP systems are optimized for short, fast transactional reads and writes. Long-running analytical queries compete with operational workloads, slow down the system for all users, and can create locking issues that threaten data integrity.
- **Why A is incorrect:** SQL is the appropriate tool for relational database queries. Using Python would not solve the underlying problem of querying an OLTP system with an analytical workload.
- **Why B is incorrect:** Relational databases fully support multi-table joins. There is no technical limit on the number of tables that can be joined.
- **Why D is incorrect:** SQL query length is not a validity constraint. The problem is operational impact, not syntax.

---

## Question 6

A developer inserts a new ORDERS record with CUSTOMER_ID = 7777, but no customer with ID 7777 exists in the CUSTOMERS table. What type of data integrity violation does this represent?

- A) Primary key violation
- B) Referential integrity violation
- C) Null constraint violation
- D) Uniqueness violation

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** A foreign key in the ORDERS table references the primary key of the CUSTOMERS table. Inserting a foreign key value that does not correspond to any existing primary key violates referential integrity — the core purpose of the foreign key constraint.
- **Why A is incorrect:** A primary key violation occurs when two rows have the same primary key value, or when a primary key value is null. The problem here is not the primary key of ORDERS but the foreign key reference.
- **Why C is incorrect:** A null constraint violation occurs when a required (NOT NULL) column receives a null value. The CUSTOMER_ID value is present — it is simply invalid.
- **Why D is incorrect:** A uniqueness violation occurs when a unique column receives a duplicate value. Again, the value 7777 is present and unique within ORDERS — the problem is that it references a non-existent row in another table.

---

## Question 7

A data team wants to store raw web logs, customer purchase records, social media posts, and product images in a single storage system. Which storage solution best fits this requirement?

- A) OLTP relational database
- B) Data warehouse with a star schema
- C) Relational data mart
- D) Data lake

**Correct Answer:** D

**Distractor Analysis:**

- **Why D is correct:** A data lake is designed to store raw data in native format across all data types — structured (purchase records), semi-structured (web logs), and unstructured (social media text, product images). It is the only option that handles all four source types without requiring schema enforcement.
- **Why A is incorrect:** A relational OLTP database requires structured data conforming to a defined schema. It cannot store images or social media text in their native unstructured form.
- **Why B is incorrect:** A data warehouse with a star schema stores processed, structured analytical data. It does not handle unstructured data like images or social media posts.
- **Why C is incorrect:** A data mart is a subject-specific subset of a data warehouse, also limited to structured processed data. It cannot store raw unstructured content.

---

## Question 8

A company collects customer feedback via a REST API that returns JSON. The JSON includes a "comments" key whose value is free text of variable length, and a "ratings" key whose value is an integer from 1 to 5. How should the "comments" field be classified?

- A) Structured and quantitative
- B) Structured and qualitative
- C) Unstructured and qualitative
- D) Semi-structured and quantitative

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** Free-text comment content has no predefined schema or format — its structure is unstructured. The content represents customer opinions and descriptions — qualitative. While the JSON wrapper is semi-structured, the value of the "comments" field itself is unstructured qualitative data.
- **Why A is incorrect:** Free text is neither structured (no schema) nor quantitative (cannot be arithmetically measured).
- **Why B is incorrect:** Free text is not structured. Structured data requires a predefined schema with consistent fields across records.
- **Why D is incorrect:** The JSON file as a whole is semi-structured, but the value of a free-text field within it is unstructured. And free text is qualitative, not quantitative.

---

## Question 9

Which of the following is the primary advantage of ELT over traditional ETL in a modern cloud analytics environment?

- A) ELT eliminates the need for any data transformation
- B) ELT is faster because it skips the Extract stage
- C) ELT preserves raw data in the target environment and leverages cloud compute power for transformation, enabling re-processing as business logic evolves
- D) ELT is only suitable for unstructured data sources

**Correct Answer:** C

**Distractor Analysis:**

- **Why C is correct:** In ELT, raw data is loaded first into the cloud analytical environment, and transformation occurs in-place using the platform's compute engine. This preserves the original raw data — enabling re-transformation when business rules change — and leverages scalable cloud compute that is unavailable in traditional on-premises ETL.
- **Why A is incorrect:** ELT still requires transformation — the "T" is present. The difference is where and when transformation happens, not whether it happens.
- **Why B is incorrect:** ELT still requires an Extract stage to pull data from source systems. The order changes (Extract → Load → Transform), but the Extract step is not eliminated.
- **Why D is incorrect:** ELT is used across all data types — structured, semi-structured, and unstructured. Its applicability is not limited to unstructured sources.

---

## Question 10

A data analyst wants to understand why customer churn increased by 15 percent in Q2. She pulls transaction history, support ticket records, and CRM data, then investigates correlations between specific customer behaviors and churn events. Which type of analytics does this represent?

- A) Descriptive analytics
- B) Diagnostic analytics
- C) Predictive analytics
- D) Prescriptive analytics

**Correct Answer:** B

**Distractor Analysis:**

- **Why B is correct:** Diagnostic analytics investigates the root cause of a known outcome. The analyst knows churn increased; she is now digging into data to find out why — the defining characteristic of diagnostic work.
- **Why A is incorrect:** Descriptive analytics summarizes what happened. Reporting that churn increased by 15 percent is descriptive. Investigating why it happened is diagnostic.
- **Why C is incorrect:** Predictive analytics uses models to forecast future outcomes. The analyst is looking backward to understand a past event, not forward to forecast future churn.
- **Why D is incorrect:** Prescriptive analytics recommends actions. The analyst is still in the investigation phase — no recommendations have been made yet.

---

### Question 11 (5 points)

A data engineer needs to move data from three operational databases into a cloud analytical platform. She loads raw data into the cloud store first, then runs SQL transformations inside the cloud platform. Which pipeline pattern does this represent?

- A) ETL — because data must always be transformed before loading
- B) ELT — because the load step precedes the transform step
- C) Reverse ETL — because data is moving from analytics to operations
- D) CDC — because changes are captured from source systems

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** ELT (Extract, Load, Transform) loads raw data into the target environment first and performs transformation inside that environment. This is the defining sequence described.
  - **Why A is incorrect:** ETL transforms data before loading it to the target. The scenario describes loading first, then transforming — the opposite sequence.
  - **Why C is incorrect:** Reverse ETL pushes data from an analytics warehouse back into operational systems (e.g., syncing a CRM from a warehouse). This scenario moves data from operational systems to analytics, not the reverse.
  - **Why D is incorrect:** Change Data Capture (CDC) tracks row-level inserts, updates, and deletes on a source system to enable incremental sync. The scenario describes a full pipeline pattern, not a CDC technique.

---

### Question 12 (5 points)

A snowflake schema differs from a star schema primarily because:

- A) A snowflake schema has no fact table
- B) Dimension tables in a snowflake schema are further normalized into sub-dimension hierarchies
- C) A snowflake schema stores only one dimension table per fact table
- D) A star schema supports only OLTP workloads; a snowflake schema supports only OLAP workloads

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** In a snowflake schema, dimension tables are normalized into smaller sub-dimension tables (e.g., a DATE dimension splitting into separate YEAR, MONTH, and DAY tables). This is the key structural difference from the flat dimension tables in a star schema.
  - **Why A is incorrect:** Both star and snowflake schemas have a central fact table. The presence of a fact table is a shared characteristic, not a distinguishing one.
  - **Why C is incorrect:** Both schemas can have multiple dimension tables. The number of dimensions does not distinguish the two patterns.
  - **Why D is incorrect:** Both star and snowflake schemas are OLAP patterns. Neither is used for OLTP, and the distinction between the two is not about system type.

---

### Question 13 (5 points)

Which data quality dimension is violated when the same customer appears in a database under two separate CUSTOMER_IDs because of a system migration error?

- A) Accuracy
- B) Timeliness
- C) Validity
- D) Uniqueness

- **Correct Answer:** D
- **Distractor Analysis:**
  - **Why D is correct:** Uniqueness requires each real-world entity to appear exactly once. Duplicate records for the same customer violate the uniqueness dimension.
  - **Why A is incorrect:** Accuracy means values reflect real-world truth. The customer records may contain accurate information — the problem is that the entity is represented twice, not that the values are wrong.
  - **Why B is incorrect:** Timeliness refers to data currency — whether data is up to date for the use case. Duplication is unrelated to when the data was collected or refreshed.
  - **Why C is incorrect:** Validity requires values to conform to format and range rules. Having two correctly formatted records for one customer is not a validity violation.

---

### Question 14 (5 points)

An analyst queries a REST API that returns weather data. The API response for some locations includes a nested `"alerts"` array with emergency warnings; for locations with no alerts, that key is absent entirely. What data collection risk does this represent?

- A) Response bias, because the API is omitting data intentionally
- B) Schema drift, because the response structure is inconsistent across records
- C) Primary key violation, because the alerts array lacks a unique identifier
- D) Null constraint violation, because missing keys mean null primary keys

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Schema drift occurs when the structure of incoming data changes or is inconsistent across records. Optional keys that appear in some records but not others represent structural variability that can break downstream parsing logic.
  - **Why A is incorrect:** Response bias is a survey methodology concept related to respondents answering inaccurately. It does not apply to API responses.
  - **Why C is incorrect:** A primary key violation is a relational database constraint issue. The API response is JSON, not a relational table, and the concern here is structural inconsistency, not key uniqueness.
  - **Why D is incorrect:** Null constraint violations occur in relational databases when a NOT NULL column receives a null. A missing JSON key in an API response is a schema consistency issue, not a database constraint violation.

---

### Question 15 (5 points)

A company has a 10-year history of customer transaction data in its OLTP system. A new analytics team wants to run quarterly trend reports on this data. What is the recommended approach?

- A) Run the quarterly reports directly against the OLTP database during off-peak hours
- B) Export a CSV snapshot monthly and analyze it in Excel
- C) Build a data warehouse, load the transaction history using an ETL pipeline, and run reports against the warehouse
- D) Delete historical records from the OLTP system to improve performance before running reports

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** A data warehouse is purpose-built for historical analytical queries. Loading OLTP transaction history via ETL separates the analytical workload from operational systems and enables fast, repeatable reporting without impacting production.
  - **Why A is incorrect:** Running heavy analytical queries against an OLTP system — even off-peak — degrades performance and risks locking issues. OLTP systems are not optimized for aggregate historical queries.
  - **Why B is incorrect:** Monthly CSV snapshots in Excel cannot efficiently support 10 years of transactional data. Excel has row limits and lacks the query performance of a purpose-built analytical system.
  - **Why D is incorrect:** Deleting historical records destroys the data needed for trend analysis. Data warehouses are specifically designed to preserve historical records that OLTP systems may archive or purge.

---

### Question 16 (5 points)

Which SQL clause is used to filter aggregated results — for example, returning only regions where total sales exceed $100,000?

- A) `WHERE`
- B) `GROUP BY`
- C) `HAVING`
- D) `ORDER BY`

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** `HAVING` filters the results of a `GROUP BY` aggregation. It applies conditions to aggregated values such as `SUM()`, `COUNT()`, or `AVG()` after grouping — the only way to filter on aggregate results.
  - **Why A is incorrect:** `WHERE` filters individual rows before aggregation. It cannot reference aggregate functions like `SUM(total_amount)` because aggregation has not yet occurred at the point WHERE is evaluated.
  - **Why B is incorrect:** `GROUP BY` groups rows by a column value and enables aggregate functions. It does not filter; it organizes.
  - **Why D is incorrect:** `ORDER BY` sorts the result set. It does not filter any rows.

---

### Question 17 (5 points)

A data team discovers that the HIRE_DATE column in the HR database contains the value "9999-12-31" for all currently employed staff who have no actual termination date. Which data quality dimension does this workaround most directly affect?

- A) Uniqueness
- B) Completeness
- C) Validity
- D) Timeliness

- **Correct Answer:** C
- **Distractor Analysis:**
  - **Why C is correct:** Validity requires values to conform to defined format and range rules. Using "9999-12-31" as a sentinel value for "no termination date" introduces values that do not represent a real business event, violating the validity of that column for its intended purpose.
  - **Why A is incorrect:** Uniqueness is about duplicate records. Every employee has their own row — there is no duplication issue here.
  - **Why B is incorrect:** Completeness checks for missing data. The "9999-12-31" value is present — the field is not null. The issue is that the value is a placeholder, not a real date.
  - **Why D is incorrect:** Timeliness refers to whether data is current enough for its use case. The sentinel value is not a staleness issue; it is a validity issue because the value does not reflect a real termination event.

---

### Question 18 (5 points)

Which of the following correctly describes the role of a foreign key in a relational database?

- A) A foreign key ensures every value in a column is unique across all rows in its table
- B) A foreign key references the primary key of another table to enforce referential integrity between related tables
- C) A foreign key speeds up query performance by creating an index on the referencing column
- D) A foreign key prevents null values from being inserted into the referencing column

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** A foreign key creates a dependency between tables by requiring that the referencing column's values match existing primary key values in the referenced table. This is the mechanism of referential integrity.
  - **Why A is incorrect:** Uniqueness is enforced by a UNIQUE constraint or primary key, not by a foreign key. A foreign key column can contain repeated values (many orders can reference the same customer).
  - **Why C is incorrect:** While databases often automatically create an index on foreign key columns for join performance, that is an implementation optimization, not the definition or purpose of the foreign key constraint itself.
  - **Why D is incorrect:** A foreign key does not enforce NOT NULL by default. A foreign key column can contain null values unless a separate NOT NULL constraint is applied.

---

### Question 19 (5 points)

A company wants to make their customer purchase data available to both their data science team (who need raw historical records) and their executive dashboard (which needs pre-aggregated KPIs). Which architecture best supports both use cases?

- A) Store everything in a single OLTP database and run all queries there
- B) Use a data lake for raw data and a data mart served from a data warehouse for pre-aggregated KPIs
- C) Export raw data to CSV files weekly and email them to each team
- D) Use two separate OLTP databases — one for data science, one for executives

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** A data lake stores raw historical records for flexible data science use. A data mart derived from a data warehouse provides pre-aggregated, governed KPIs optimized for executive dashboards. This two-tier architecture is the industry-standard solution for serving both audiences.
  - **Why A is incorrect:** A single OLTP system cannot efficiently serve both use cases. Heavy analytical queries degrade operational performance, and OLTP systems are not optimized for aggregate reporting.
  - **Why C is incorrect:** Weekly CSV exports are stale, limited in size, and not scalable. They do not provide the real-time or near-real-time KPIs executives need.
  - **Why D is incorrect:** Duplicating OLTP systems does not solve the analytical query performance problem. Both teams still lack purpose-built analytical infrastructure.

---

### Question 20 (5 points)

An analyst uses Python's `pandas.read_sql_query()` to load query results from a SQLite database into a DataFrame. The query joins the ORDERS and CUSTOMERS tables on CUSTOMER_ID. What is the primary advantage of this approach compared to exporting a CSV and loading it into pandas?

- A) SQL queries execute faster than pandas operations in all cases
- B) The join and filtering logic runs inside the database engine before data is transferred to Python, reducing memory usage in the Python process
- C) pandas cannot perform join operations, so SQL must be used for any multi-table analysis
- D) SQLite automatically enforces foreign keys when data is loaded into pandas

- **Correct Answer:** B
- **Distractor Analysis:**
  - **Why B is correct:** Executing the JOIN in SQL uses the database engine's optimized query processor and returns only the needed result set to Python. Loading full tables as CSVs into pandas and then joining in Python loads more data into memory and transfers more data across the connection.
  - **Why A is incorrect:** SQL is generally faster for set-based operations on large datasets, but pandas can be faster for certain in-memory transformations. The claim that SQL is always faster is incorrect.
  - **Why C is incorrect:** pandas fully supports join operations via `DataFrame.merge()`. SQL is not required for joins in pandas.
  - **Why D is incorrect:** SQLite's foreign key enforcement is a database-level constraint that is independent of how data is read into pandas. It does not activate or change based on the Python client.

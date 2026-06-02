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

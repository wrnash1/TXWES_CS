# Video Script — Module 02: Data Collection and Data Sources

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Estimated Runtime:** 20–24 minutes
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1: Data Concepts and Environments; Domain 2: Data Mining

---

## Segment 1 — Introduction (2 minutes)

Welcome back to CIS-4336. I am Professor Nash, and this is Module 02: Data Collection and Data Sources.

In Module 01 we established what data is and how to classify it. Now we need to answer the practical question every analyst faces at the start of every project: where does the data come from, and how do we get it?

By the end of this module, you will be able to:

- Identify primary and secondary data sources and explain the tradeoffs between them
- Describe the most common data collection methods used in business analytics
- Explain the Extract, Transform, Load process and its role in moving data into analytical environments
- Distinguish between OLTP and OLAP systems and explain why that distinction matters for analysts
- Recognize relational database concepts including primary keys, foreign keys, and schemas
- Apply these concepts to Data+ DA0-001 exam questions in Domain 1 and Domain 2

Let us get into it.

---

## Segment 2 — Primary vs. Secondary Data Sources (3 minutes)

Every dataset an analyst works with originated somewhere. Understanding the origin shapes every downstream decision about trust, validity, and methodology.

**Primary data** is data collected directly for the current analysis purpose. Surveys you design and administer, experiments you run, sensors you install — all of these produce primary data. Primary data is fresh and purpose-fit, but it is expensive and time-consuming to collect.

**Secondary data** is data that was collected by someone else for a different original purpose and is now being reused. Government census records, purchased demographic datasets, industry reports, and internal operational databases are all secondary. Secondary data is cheaper and faster to acquire, but you must carefully evaluate its relevance, recency, and reliability.

[SHOW CHART: Two-column comparison — Primary Data vs. Secondary Data — rows for collection method, cost, time, control over quality, examples, and common risks]

A common Data+ exam question asks you to identify whether an analyst is using primary or secondary data in a scenario. The key signal is: did this analyst or their organization collect the data directly for this purpose? If yes, primary. If not, secondary.

---

## Segment 3 — Data Collection Methods (4 minutes)

How data gets collected matters as much as what data is collected. Different collection methods produce different data types, different quality levels, and different biases.

**Surveys and questionnaires** are among the most common primary data collection tools in business analytics. Surveys produce structured responses — Likert scales, multiple choice, rankings — mixed with unstructured open-text. Sampling strategy matters enormously: a convenience sample from social media followers will produce very different results than a stratified random sample of all customers.

**Transactional data capture** happens automatically when business systems record operational events — purchases, logins, service requests, support tickets. This is secondary data from the analyst's perspective (the operational system collected it first), but it is the richest and most reliable source of behavioral data in most organizations.

**Observation and sensor data** includes IoT device readings, website click tracking, GPS telemetry, and manufacturing sensors. This data is typically high-frequency, timestamped, and semi-structured. It requires significant preprocessing before it is analytically useful.

**Interviews and focus groups** produce qualitative primary data — typically unstructured text. Useful for hypothesis generation but not for statistical generalization.

**Web scraping** extracts data from websites programmatically. The resulting data is typically semi-structured to unstructured and requires significant cleaning. Legal and ethical considerations apply — always review a site's terms of service before scraping.

**Application programming interfaces (APIs)** provide structured or semi-structured data on demand from external services. A REST API returning JSON is one of the most common data collection mechanisms in modern analytics pipelines.

[SHOW CHART: Collection method matrix — rows: Survey, Transactional, Sensor, Interview, Web Scraping, API — columns: Data Type, Structure, Primary/Secondary, Typical Quality, Key Risk]

---

## Segment 4 — Databases: OLTP vs. OLAP (4 minutes)

Two fundamentally different types of database systems exist in most organizations, and analysts must understand which type they are working with.

**OLTP — Online Transaction Processing** systems are built for operational speed. They record business transactions as they happen: sales, orders, inventory updates, account changes. OLTP databases are optimized for fast writes and row-level lookups. Schema design is typically highly normalized — data is split across many tables to eliminate redundancy and enable fast updates.

Examples of OLTP systems: point-of-sale databases, banking core systems, ERP systems, CRM databases.

**OLAP — Online Analytical Processing** systems are built for analytical queries. They store historical data in formats optimized for aggregation across large volumes of records. OLAP systems are optimized for fast reads across many rows. Schema design is typically denormalized — data is pre-joined and pre-aggregated to minimize query complexity.

Examples of OLAP systems: data warehouses, data marts, cloud analytics platforms like AWS Redshift or Google BigQuery.

[SHOW CHART: OLTP vs. OLAP comparison table — rows: Purpose, Optimization, Schema design, Query type, Data volume, Update frequency, Examples]

The practical implication for analysts: you should never run heavy analytical queries directly against an OLTP production database. You will degrade performance for operational users and risk data integrity issues. Analytical workloads belong in OLAP environments — data warehouses, data marts, or read replicas.

---

## Segment 5 — Relational Database Concepts (3 minutes)

Whether the database is OLTP or OLAP, relational databases share a common set of structural concepts that every data analyst must understand.

A **table** is a collection of related records organized into rows and columns. Each column has a defined data type. Each row represents one record.

A **primary key** is a column (or combination of columns) that uniquely identifies each row in a table. No two rows can share the same primary key value, and primary keys cannot be null.

A **foreign key** is a column in one table that references the primary key of another table. Foreign keys enforce referential integrity — they prevent orphaned records. A SALES record with a CUSTOMER_ID foreign key cannot exist if that CUSTOMER_ID does not exist in the CUSTOMERS table.

A **schema** defines the structure of a database: its tables, columns, data types, constraints, and relationships. Understanding the schema is the first step when working with any new data source.

[SHOW CHART: Entity-relationship diagram showing CUSTOMERS, ORDERS, and PRODUCTS tables with primary keys highlighted and foreign key relationships drawn as connecting lines]

**Star schema** and **snowflake schema** are two common OLAP schema patterns you will encounter on the Data+ exam.

In a **star schema**, a central fact table (containing measurable events like sales transactions) connects directly to multiple dimension tables (containing descriptive attributes like customer, product, date, and store). The diagram looks like a star.

In a **snowflake schema**, dimension tables are further normalized into sub-dimension tables. The diagram looks like a snowflake. Snowflake schemas reduce data redundancy but increase query complexity.

---

## Segment 6 — The ETL Process (3 minutes)

How does data get from an OLTP operational system into an OLAP analytical environment? Through the ETL pipeline: Extract, Transform, Load.

**Extract** — Data is pulled from one or more source systems. Sources might include relational databases, flat files, APIs, or streaming data platforms. Extraction must be carefully designed to minimize impact on source systems.

**Transform** — Raw extracted data is cleaned, normalized, and restructured for the target analytical environment. Transformations include: removing duplicates, handling null values, standardizing formats, joining tables, and computing derived fields.

**Load** — Transformed data is written into the target analytical store — a data warehouse, data mart, or data lake.

[SHOW CHART: Pipeline diagram showing Source Systems on the left, ETL processing in the middle with Extract, Transform, and Load stages labeled, and Target Data Warehouse on the right]

A modern variation is **ELT — Extract, Load, Transform** — where raw data is loaded into the target environment first, and transformation happens in place using the compute power of the analytical platform. Cloud platforms like Snowflake, BigQuery, and Databricks enable this pattern.

---

## Segment 7 — Data Quality at the Source (2 minutes)

Data quality problems are far cheaper to fix at the source than downstream. Understanding where data quality issues originate is a core analyst competency.

**Completeness** — Are all expected records and fields present? Missing records in an API extraction or null values in required columns reduce completeness.

**Accuracy** — Do the values reflect reality? A sensor with calibration drift produces inaccurate readings. A data entry form without input validation allows impossible values.

**Consistency** — Is the same entity represented the same way across systems? "United States," "US," "USA," and "U.S.A." all refer to the same country but will not match in a join.

**Timeliness** — Is the data current enough for the analytical purpose? A daily ETL job will produce data that is up to 24 hours stale.

**Uniqueness** — Does each entity appear exactly once? Duplicate records from system migrations or multi-channel data collection are common quality issues.

The Data+ exam tests all five of these data quality dimensions under Domain 3. We will cover data cleaning in depth in Module 03, but recognizing quality issues at the source is part of data collection competency.

---

## Segment 8 — Exam Alignment and Closing (2 minutes)

Today's content aligns with Data+ exam Domain 1 (Data Concepts and Environments) and Domain 2 (Data Mining). Expect scenario questions about:

- Identifying primary vs. secondary data sources
- Selecting the appropriate collection method for a given scenario
- Distinguishing OLTP from OLAP characteristics
- Identifying primary key and foreign key concepts
- Describing the ETL pipeline stages

For exam preparation, review the official objective list at comptia.org and work through Professor Messer's free study materials at professormesser.com.

Your assignments for Module 02 are:

- Complete the Reading Guide, focusing on the database concepts reference and ETL pipeline table
- Complete Lab 02 — SQL exercises on a provided relational schema
- Complete the ten-question quiz
- Post to the Discussion Board by Wednesday and respond to two classmates by Sunday

I will see you in Module 03, where we tackle data cleaning and transformation in depth.

---

End of Module 02 Video Script — Estimated runtime: 23 minutes

# Reading Guide — Module 02: Data Collection and Data Sources

**Course:** CIS-4336 Data Analytics — Texas Wesleyan University
**Instructor:** Professor Nash
**Certification Alignment:** CompTIA Data+ DA0-001 — Domain 1 and Domain 2

---

## Overview

This reading guide covers data collection methods, database structures, and ETL processes that appear on the CompTIA Data+ exam. Work through all sections before attempting the lab or quiz.

---

## Section 1 — Core Vocabulary

| Term | Definition |
|---|---|
| Primary data | Data collected directly for the current analytical purpose |
| Secondary data | Data originally collected for a different purpose, reused for analysis |
| OLTP | Online Transaction Processing — operational systems optimized for fast writes and row-level access |
| OLAP | Online Analytical Processing — analytical systems optimized for fast reads across large data volumes |
| ETL | Extract, Transform, Load — the pipeline for moving data from source to analytical target |
| ELT | Extract, Load, Transform — variant where transformation occurs inside the target environment |
| Primary key | A column or set of columns that uniquely identifies each row in a table; cannot be null |
| Foreign key | A column that references the primary key of another table to enforce referential integrity |
| Schema | The structural definition of a database: its tables, columns, data types, and relationships |
| Star schema | OLAP design with a central fact table connected directly to dimension tables |
| Snowflake schema | OLAP design where dimension tables are further normalized into sub-dimension hierarchies |
| Data warehouse | A central analytical repository storing integrated historical data from multiple sources |
| Data mart | A subject-specific subset of a data warehouse |
| Data lake | A large-scale repository storing raw data in native format, including unstructured data |
| API | Application Programming Interface — a defined contract for programmatic data exchange |
| Referential integrity | The rule that every foreign key value must match an existing primary key value in the referenced table |
| Normalization | Organizing database tables to reduce data redundancy and improve update consistency |
| Denormalization | Combining normalized tables to optimize read performance for analytical queries |

---

## Section 2 — Primary vs. Secondary Data Comparison

| Characteristic | Primary Data | Secondary Data |
|---|---|---|
| Who collected it | The analyst or their organization, for this purpose | Another party, for a different original purpose |
| Cost | Higher — survey design, administration, tooling | Lower — often free or purchased at scale |
| Time to acquire | Longer | Faster |
| Relevance fit | High — designed for the specific question | Variable — may not perfectly match the question |
| Quality control | Full control | Limited — must evaluate source credibility |
| Examples | Custom survey, A/B experiment, new sensor deployment | Census records, CRM history, purchased demographic data |

---

## Section 3 — Data Collection Method Reference

| Method | Primary or Secondary | Structure | Volume | Key Risk |
|---|---|---|---|---|
| Survey / questionnaire | Primary | Mixed (structured + unstructured) | Small to medium | Response bias, low completion rates |
| Transactional capture | Secondary (from analyst view) | Structured | High | Schema complexity, data sprawl |
| IoT / sensor data | Primary or secondary | Semi-structured, time-series | Very high | Sensor drift, missing timestamps |
| Interview / focus group | Primary | Unstructured | Very small | Not statistically generalizable |
| Web scraping | Primary collection | Semi-structured to unstructured | Medium to high | Legal risk, layout changes break scrapers |
| REST API | Primary or secondary | Semi-structured (JSON/XML) | Variable | Rate limits, versioning breaks |
| Direct database query | Secondary | Structured | High | OLTP performance impact if queried directly |
| Purchased dataset | Secondary | Structured or semi-structured | Variable | Unknown collection methodology |

---

## Section 4 — OLTP vs. OLAP Reference

| Characteristic | OLTP | OLAP |
|---|---|---|
| Purpose | Record operational transactions | Support analytical queries |
| Optimization | Fast writes, row-level access | Fast reads, column aggregation |
| Schema design | Highly normalized (3NF typical) | Denormalized (star or snowflake) |
| Query type | Short, targeted — single records or small sets | Long, aggregate — millions of rows |
| Data freshness | Real-time or near-real-time | Periodic refresh (hourly, daily, weekly) |
| Data history | Current state or short history | Long historical record |
| Should analysts run heavy queries here? | No — degrades operational performance | Yes — designed for this workload |
| Examples | POS systems, ERP, CRM, banking cores | Redshift, BigQuery, Snowflake, Azure Synapse |

---

## Section 5 — Relational Database Concepts

### Primary and Foreign Keys

A primary key uniquely identifies each row in a table. Three rules apply:

- Values must be unique across all rows in the table
- Values cannot be null
- Each table has exactly one primary key (which may span multiple columns, forming a composite key)

A foreign key in one table references the primary key of another table. The referential integrity constraint requires every foreign key value to either match an existing primary key in the referenced table or be null.

### Schema Patterns Compared

| Schema Type | Structure | Join Complexity | Storage Use | Best For |
|---|---|---|---|---|
| Third Normal Form (3NF) | Highly normalized, many small tables | High (many joins required) | Efficient | OLTP operational systems |
| Star schema | Fact table with flat dimension tables | Low (one join per dimension) | Moderate | Simple, fast OLAP queries |
| Snowflake schema | Fact table with normalized dimension hierarchies | Medium (more joins) | More efficient than star | Complex dimensional hierarchies |

---

## Section 6 — ETL Pipeline Reference

| Stage | Key Activities | Common Tools | Common Issues |
|---|---|---|---|
| Extract | Pull data from source systems via queries, API calls, or file exports | Python, SQL, Talend, Informatica | Incomplete extraction, source system load, schema drift |
| Transform | Clean, normalize, join, aggregate, and compute derived fields | Python/pandas, dbt, Apache Spark | Null handling logic, type mismatches, business rule errors |
| Load | Write transformed data to the target analytical store | SQL COPY/INSERT, cloud storage APIs | Duplicate loading, failed transactions, index rebuild time |

### ELT vs. ETL Decision Guide

Use ETL when:

- The target system has limited compute power for transformation
- Raw data should not be stored in the target for compliance reasons
- The transformation logic is mature and unlikely to change

Use ELT when:

- The target is a modern cloud platform (Snowflake, BigQuery, Databricks)
- You want to preserve raw data for re-processing as business logic evolves
- Transformation complexity benefits from the target's SQL compute engine

---

## Section 7 — Data Quality Dimensions

| Dimension | Definition | Example Issue | Detection Method |
|---|---|---|---|
| Completeness | All expected records and fields are present | Missing customer address fields | Count nulls per column; compare to expected row count |
| Accuracy | Values reflect real-world truth | Sensor calibration drift producing wrong temperature readings | Cross-reference with validated reference values |
| Consistency | Same entity represented identically across systems | "USA" vs. "U.S.A." vs. "United States" in different tables | Standardization checks, fuzzy matching |
| Timeliness | Data is current enough for the use case | 24-hour-stale metrics displayed on a real-time dashboard | Freshness timestamp checks |
| Uniqueness | Each entity appears exactly once | Duplicate customer records from a CRM migration | Deduplication checks on identifier columns |
| Validity | Values conform to defined format and range rules | Age field containing -5 or 999 | Range constraints, format pattern checks |

---

## Section 8 — Data+ Exam Tips

1. **Primary vs. secondary identification.** The key signal: did the analyst's organization collect it directly for this purpose? Yes means primary. No — reusing data collected by others — means secondary.

2. **OLTP is never the right answer for heavy analytics.** Any exam choice suggesting aggregate analytical queries should run against an OLTP production database is incorrect. Heavy reads belong in a data warehouse.

3. **Star vs. snowflake schema.** Star schema: fact table connects directly to flat dimension tables. Snowflake schema: dimension tables are further normalized. The exam may show a diagram and ask you to name the pattern.

4. **ETL stage mapping.** Know which activities belong in each stage. Removing duplicates is Transform. Pulling data from source is Extract. Writing to the warehouse is Load.

5. **Foreign key = referential integrity.** When an exam scenario describes a foreign key value that references a non-existent primary key, the violation is a referential integrity violation.

6. **Data lake vs. data warehouse.** A warehouse stores processed, structured analytical data. A lake stores raw data in native format, including unstructured data. The exam tests this distinction frequently.

7. **API responses are semi-structured.** JSON from a REST API is semi-structured, not structured. The schema is implied by keys, not enforced by a relational constraint.

8. **Survey bias types.** Non-response bias (those who do not respond differ from those who do) and response bias (respondents answer how they think they should) are the two main survey quality risks on the exam.

---

## Section 9 — Study Checklist

- [ ] Memorize all vocabulary terms in Section 1
- [ ] Distinguish primary from secondary data for five different scenarios
- [ ] Reproduce the OLTP vs. OLAP comparison table from memory
- [ ] Explain star schema and snowflake schema with a diagram
- [ ] Describe all three ETL stages with concrete examples
- [ ] List all six data quality dimensions and their detection methods
- [ ] Review all eight exam tips
- [ ] Review official CompTIA Data+ objectives at comptia.org
- [ ] Review Professor Messer's free study materials at professormesser.com
- [ ] Complete Lab 02
- [ ] Complete Quiz 02

---

## Additional Resources

- Official exam objectives: comptia.org (search "Data+ DA0-001 exam objectives")
- Professor Messer's free study guides: professormesser.com

## 9. Supplemental Resources

**1. Mode Analytics SQL Tutorial — Intermediate SQL**
<https://mode.com/sql-tutorial/introduction-to-sql>
A free, browser-based SQL course covering JOINs, GROUP BY, HAVING, and subqueries with real datasets. Directly reinforces the relational database and ETL concepts in this module.

**2. dbt (data build tool) — What is ELT? (Official Documentation)**
<https://docs.getdbt.com/terms/elt>
The team behind the most widely used ELT transformation tool explains the ELT pattern, its advantages over ETL, and when to use each. Practical and concise.

**3. Kimball Group — Star Schema in Depth**
<https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/>
Ralph Kimball's dimensional modeling techniques are the industry standard for data warehouse design. This page covers star schema, snowflake schema, fact tables, and dimension tables with authoritative depth.

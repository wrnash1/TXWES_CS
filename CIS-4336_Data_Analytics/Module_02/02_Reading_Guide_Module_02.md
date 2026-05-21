# Reading Guide: Module 02 - Data Collection and Data Sources
## Course: CIS-4336_Data_Analytics (CompTIA Data+)

---

### Introduction
Welcome to **Module 02 - Data Collection and Data Sources**! This module covers how organizations gather data from diverse sources — internal systems, third-party feeds, APIs, and public datasets — and how those sources determine the quality and usability of the data collected. These concepts map directly to the **CompTIA Data+** Data Concepts and Environments domain.

Understanding where data comes from, how it is acquired, and how schema design affects downstream analysis is essential. The exam tests your ability to identify the appropriate collection method for a given scenario and distinguish first-party, second-party, and third-party data.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **First-party, second-party, and third-party data**: First-party data is collected directly by an organization from its own customers or systems (e.g., a CRM database). Second-party data is another organization's first-party data shared through a direct partnership. Third-party data is collected by an external aggregator with no direct relationship to the consumer and carries the highest privacy and accuracy risks.
*   **Relational vs. non-relational databases**: A relational database stores data in structured tables linked by keys (e.g., MySQL, PostgreSQL). A non-relational (NoSQL) database stores data as documents, key-value pairs, graphs, or wide columns — suited for unstructured or high-volume data where rigid schemas are impractical.
*   **Primary keys and foreign keys**: A primary key is a column (or combination of columns) that uniquely identifies every row in a table — no nulls allowed, no duplicates. A foreign key is a column in one table that references the primary key in another, enforcing referential integrity and enabling JOIN operations across tables.
*   **Star schema vs. snowflake schema**: A star schema has a central fact table connected directly to denormalized dimension tables, making queries fast and simple. A snowflake schema normalizes the dimension tables into sub-tables, reducing data redundancy at the cost of more complex JOIN paths. The Data+ exam expects you to recognize which schema supports which reporting need.
*   **Data collection methods**: Methods include surveys, web scraping, API calls, database exports, sensor/IoT streams, transactional logs, and flat-file imports. Each method introduces different completeness, timeliness, and bias risks that must be managed before analysis.

---

### 2. Certification Exam Tips
*   **Domain weight:** Data Collection and Management falls within Domain 2 of the Data+ DA0-001 exam (approximately 25% of scored questions). Data source identification and schema design questions appear frequently.
*   **Exam trap — primary vs. foreign key confusion:** The exam often asks which key "enforces referential integrity." The answer is always the foreign key, not the primary key. The primary key enforces entity integrity within its own table.
*   **Exam trap — star vs. snowflake:** When a question asks which schema produces the fewest JOINs for a BI dashboard query, choose star schema. When it asks which schema minimizes storage redundancy through normalization, choose snowflake.
*   **Study Resource:** Work through the data wrangling chapters of [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/), which covers importing data from multiple source types including databases, flat files, and APIs with practical R examples translatable to any analytics workflow.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Read the chapters covering data import, tidy data principles, and relational data in the OER Textbook: [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/). These sections cover how data moves from raw sources into an analysis environment.
*   **Required Video:** Watch the data import and wrangling sections of the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238) — this free 4-hour course demonstrates reading data from CSVs, databases, and APIs using Pandas, directly applicable to Data+ practical scenarios.

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:
*   **Identify primary keys in a table layout**: Examine a provided schema diagram and annotate every primary key, explaining why each column qualifies (uniqueness, non-null).
*   **Link tables using foreign key relationships**: Write SQL statements that define a foreign key constraint between two tables, then verify referential integrity is enforced.
*   **Draw a basic star schema diagram**: Given a set of business requirements for a sales report, design a star schema with one fact table and at least three dimension tables, labeling all keys.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the data import and relational data chapters in [Introduction to Data Science by Rafael A. Irizarry](https://rafalab.github.io/dsbook/).
- [ ] Watch the [Data Analysis with Python Course by freeCodeCamp](https://www.youtube.com/watch?v=GPVsHOl2238).
- [ ] Review the lab instructions and understand what each task requires.
- [ ] Proceed to the weekly hands-on lab activity.

# Reading Guide: Module 09 - ERP Database Structures

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Introduction

Welcome to **Module 09 - ERP Database Structures**! ERP systems process millions of transactions daily, and their ability to do so reliably depends on carefully designed database architectures. This module examines how ERP platforms organize data — from normalized table structures to indexing strategies — and introduces the data dictionary concept that makes SAP's database schema self-documenting.

Understanding database structures is relevant to both certifications: SAP exam questions test knowledge of how data is organized in tables and transactions, while Salesforce exam questions test how the platform's object-oriented database (Salesforce Object Query Language / SOQL) models business data.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Normalized tables**: Database tables designed to minimize data redundancy by separating data into related tables connected by foreign keys. ERP systems use normalization (typically 3rd Normal Form) to ensure that a single data change (e.g., a vendor's bank account number) needs to be updated in only one place.
* **High transaction volume**: The characteristic of ERP databases that must handle hundreds of thousands of simultaneous writes and reads — payroll runs, inventory movements, financial postings — without performance degradation. ERP database architectures are specifically tuned for OLTP (Online Transaction Processing) workloads.
* **Indexing schemas**: Database indexes are data structures that allow the database engine to locate specific rows without scanning entire tables. ERP systems create indexes on frequently queried columns (e.g., document number, vendor ID, date) to maintain fast response times under high load.
* **Data dictionaries**: In SAP, the Data Dictionary (transaction SE11) is the central repository that defines the structure of all database tables, data elements, domains, and their relationships. It serves as the authoritative technical reference for every field in the system and is used by developers to understand data structures before writing ABAP programs.

---

### 2. Certification Exam Tips

* **SAP ABAP Data Dictionary:** Know that SE11 is the transaction for the ABAP Data Dictionary. It defines Tables, Views, Data Elements, Domains, and Search Helps. The difference between a Transparent Table (one-to-one mapping to a database table) and a Cluster/Pool Table (older SAP formats) may appear in technical exam questions.
* **Salesforce object model:** In Salesforce, the equivalent of a database table is a Salesforce Object (standard or custom). Fields on an object are like table columns. The Salesforce Schema Builder visually shows object relationships — analogous to an entity-relationship diagram. SOQL (Salesforce Object Query Language) queries these objects with SELECT, FROM, and WHERE clauses.
* **ACID properties:** ERP database transactions must satisfy ACID: Atomicity (all-or-nothing), Consistency (valid state after every transaction), Isolation (concurrent transactions do not interfere), Durability (committed data survives failures). Exam questions about why ERP uses relational databases often have ACID compliance as the correct answer.
* **Partitioning for performance:** Large ERP installations partition historical transaction tables (e.g., FI documents older than 2 years) into archive storage. This keeps the active transaction table small and fast — a technique that may appear in performance-tuning scenario questions.
* **Study Resource:** Review the Salesforce Trailhead module [Data Modeling](https://trailhead.salesforce.com/content/learn/modules/data_modeling) — a free unit that teaches how Salesforce's object-field-relationship model maps to relational database concepts tested on the Associate exam.

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** Complete the Salesforce Trailhead module [Data Modeling](https://trailhead.salesforce.com/content/learn/modules/data_modeling) — a free unit explaining Salesforce objects, fields, and relationships in terms that directly parallel relational database design.
* **Required Video:** Watch the video lecture on **ERP Database Structures** in the official course playlist: [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Analyze transactional table structures**: Given an entity-relationship diagram of three related ERP tables (Material Master, Purchase Order Header, Purchase Order Line Item), identify the primary keys, foreign keys, and the relationship type between each pair of tables.
* **Trace index usage on high-volume queries**: Given a sample slow-running query that scans a large invoice table without an index, explain what index you would add to the WHERE clause column and why it improves performance.
* **Examine ERP database schemas**: Using the Salesforce Schema Builder in your free Developer org, create a custom object with five fields and a lookup relationship to the standard Account object, then document the resulting schema diagram.

---

### 3. Study Checklist

* [ ] Read all glossary definitions and be able to explain why normalization prevents update anomalies.
* [ ] Complete [Data Modeling](https://trailhead.salesforce.com/content/learn/modules/data_modeling) on Trailhead (earn the badge).
* [ ] Watch the video lecture on **ERP Database Structures** in [Salesforce & SAP ERP Fundamentals Tutorial](https://www.youtube.com/playlist?list=PLD2549A0D756627C1).
* [ ] Complete the lab ER diagram analysis, index design exercise, and Salesforce Schema Builder activity.
* [ ] Proceed to the weekly quiz.

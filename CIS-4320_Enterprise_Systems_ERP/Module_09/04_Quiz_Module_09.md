# Quiz: Module 09 - ERP Database Structures

## Course: CIS-4320_Enterprise_Systems_ERP (Salesforce Certified Associate / SAP Certified Associate)

---

### Question 1

Why do ERP databases use strict indexing and normalization in their table designs?

* A) To prevent non-technical users from writing database queries directly
* B) To ensure high transactional integrity (ACID compliance) and prevent data duplication across millions of records processed daily
* C) To run faster than HTML rendering engines on client web browsers
* D) To bypass operating system memory management and access hardware directly

* **Correct Answer:** B) ERP databases handle millions of records daily; normalization prevents update anomalies and data inconsistency, while indexes speed up record lookups under heavy transaction loads.
* **Distractor Analysis:**
  * *Why B is correct:* ACID-compliant transactions with normalized tables ensure that a vendor bank account change updates exactly one record, not dozens of duplicates, while indexes keep query response times acceptable under ERP's high-volume OLTP workload.
  * *Why A is incorrect:* Normalization and indexes are performance and integrity design choices; they are not access control mechanisms that restrict user query writing.
  * *Why C is incorrect:* HTML rendering is a browser client activity; it has no architectural connection to database normalization or indexing strategy.
  * *Why D is incorrect:* Database engines operate through the OS and do not bypass memory management; hardware access is not a database design consideration.

---

### Question 2

In SAP, which transaction code opens the **ABAP Data Dictionary**, where developers can look up the structure of any database table?

* A) SM30 — Table maintenance generator for configuration tables
* B) SE16 — Data browser for viewing table contents
* C) SE11 — ABAP Data Dictionary for defining and inspecting table structures, data elements, and domains
* D) ST05 — SQL trace for monitoring active database queries

* **Correct Answer:** C) SE11 is the SAP ABAP Data Dictionary transaction, which is the authoritative source for the technical definition of every table, view, data element, and domain in the system.
* **Distractor Analysis:**
  * *Why C is correct:* SE11 shows the complete technical metadata for any SAP database object — field names, data types, lengths, foreign key relationships, and index definitions — making it the primary reference for ABAP developers and technical consultants.
  * *Why A is incorrect:* SM30 is used to maintain data in configuration tables (customizing), not to view or define their technical structure.
  * *Why B is incorrect:* SE16 displays the actual data rows stored in a table; it does not show or modify the table's structural definition.
  * *Why D is incorrect:* ST05 is a performance analysis tool that traces SQL statements being sent to the database; it is used for query tuning, not for looking up table structures.

---

### Question 3

A Salesforce developer needs to retrieve all Account records where the BillingState is "TX" and the AnnualRevenue is greater than 1,000,000. Which query correctly uses Salesforce Object Query Language (SOQL)?

* A) `GET * FROM Account WHERE BillingState = 'TX' AND AnnualRevenue > 1000000`
* B) `SELECT Id, Name FROM Account WHERE BillingState = 'TX' AND AnnualRevenue > 1000000`
* C) `FETCH Account WHERE State = 'TX' AND Revenue > 1000000`
* D) `FIND Account FILTER BillingState='TX' AND AnnualRevenue>1000000`

* **Correct Answer:** B) SOQL uses SELECT/FROM/WHERE syntax similar to SQL, with Salesforce object and field API names as the table and column references.
* **Distractor Analysis:**
  * *Why B is correct:* SOQL uses `SELECT [fields] FROM [Object] WHERE [conditions]` — the same structure as standard SQL. Field API names (BillingState, AnnualRevenue) must be used exactly as defined in the object schema.
  * *Why A is incorrect:* `GET` is not a valid SOQL keyword; SOQL uses `SELECT` for data retrieval.
  * *Why C is incorrect:* `FETCH` is not SOQL syntax, and `State` and `Revenue` are not the correct Salesforce field API names for those fields.
  * *Why D is incorrect:* `FIND` is the keyword for Salesforce Object Search Language (SOSL), which is used for text search across objects, not for structured field-condition queries.

---

### Question 4

An ERP system is experiencing slow response times when users search for customer invoices by document date. The database administrator runs an analysis and confirms that the invoice table has 50 million rows and no index on the document date column. What is the most direct performance remedy?

* A) Increase the number of application servers to distribute the user load
* B) Archive all invoices older than one year to a separate storage system
* C) Create a database index on the document date column of the invoice table
* D) Upgrade the database server to a model with more CPU cores

* **Correct Answer:** C) Creating an index on the document date column allows the database engine to locate matching rows in milliseconds instead of scanning all 50 million rows sequentially for every search.
* **Distractor Analysis:**
  * *Why C is correct:* A database index on a frequently queried column is the most targeted and cost-effective fix for a table scan performance problem. It directly addresses the root cause without requiring infrastructure changes.
  * *Why A is incorrect:* Adding application servers distributes user connection load but does not fix the underlying database scan problem; every server would still cause a full table scan.
  * *Why B is incorrect:* Archiving old records reduces table size and is a valid long-term strategy, but it does not fix the missing index problem for current-period searches.
  * *Why D is incorrect:* More CPU cores improve overall server throughput but do not eliminate the inefficiency of a full table scan; the index is the correct fix at the query level.

---

### Question 5

In Salesforce's data model, what is the equivalent of a foreign key relationship between two database tables?

* A) A Validation Rule that enforces data format requirements on a field
* B) A Lookup or Master-Detail relationship field on a Salesforce object that links records in one object to records in another
* C) A Workflow Rule that triggers an update to a related record when conditions are met
* D) A Permission Set that grants access to related object records

* **Correct Answer:** B) Lookup and Master-Detail relationship fields in Salesforce are the equivalent of foreign keys — they store a reference to the ID of a related record in another object, enforcing the link between the two objects.
* **Distractor Analysis:**
  * *Why B is correct:* A Lookup field on the Contact object pointing to Account is functionally identical to a foreign key in a relational database — it stores the Account ID and enforces referential integrity (Master-Detail enforces it strictly; Lookup allows the parent to be blank).
  * *Why A is incorrect:* A Validation Rule enforces field-level data quality rules (e.g., "email must contain @") but does not create relationships between objects.
  * *Why C is incorrect:* A Workflow Rule is an automation trigger; it can update related records but does not define the structural relationship between objects.
  * *Why D is incorrect:* A Permission Set controls user access to objects and fields; it is a security configuration, not a data relationship definition.

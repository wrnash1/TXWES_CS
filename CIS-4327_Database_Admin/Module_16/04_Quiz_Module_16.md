# Quiz: Module 16 - Final Exam Prep & Google Cloud Professional Cloud Database Engineer
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A startup is building a new SaaS application. The backend database must: (1) support standard SQL queries, (2) serve users in a single US region, (3) require minimal database administration overhead, (4) support ACID transactions, and (5) be cost-effective for a startup budget. Which GCP database service best meets all five requirements?
A) Cloud SQL for PostgreSQL
B) Cloud Spanner
C) Cloud Bigtable
D) Firestore in Native mode
*   **Correct Answer:** A) Cloud SQL for PostgreSQL
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud SQL for PostgreSQL satisfies all five requirements: it supports standard PostgreSQL SQL, serves a single US region, is a fully managed service that minimizes administrative overhead, provides full ACID compliance, and has the lowest cost of the relational GCP options — significantly cheaper than Cloud Spanner for single-region workloads.
    *   *Why B is incorrect:* Cloud Spanner satisfies requirements 1, 3, and 4 but is significantly more expensive than Cloud SQL for a startup with a single-region workload. Its global distribution and 5-nines SLA are capabilities the startup does not need and would be paying for unnecessarily.
    *   *Why C is incorrect:* Bigtable does not support SQL queries or ACID transactions, violating requirements 1 and 4. It is a NoSQL key-value store, not appropriate for a general SaaS application backend.
    *   *Why D is incorrect:* Firestore does not support SQL (it uses a proprietary query API), violating requirement 1. It is a document database optimized for mobile/web apps with offline sync, not a general-purpose relational backend.

---

---

**Question 2**
The Google Cloud Professional Cloud Database Engineer exam is scenario-based. Which of the following correctly describes the exam format and what it primarily tests?
A) The exam consists of approximately 50–60 scenario-based multiple-choice questions that test your ability to select the most appropriate GCP database service, configuration, and architecture for described business and technical requirements.
B) The exam consists of 100 fill-in-the-blank questions testing memorization of GCP CLI command syntax for each database service.
C) The exam includes a 4-hour hands-on lab component in GCP Qwiklabs where you must deploy and configure a Cloud SQL and Spanner environment from scratch.
D) The exam focuses exclusively on Cloud SQL and Cloud Spanner, ignoring Bigtable, Firestore, BigQuery, and AlloyDB.
*   **Correct Answer:** A) The exam consists of approximately 50–60 scenario-based multiple-choice questions that test your ability to select the most appropriate GCP database service, configuration, and architecture.
*   **Distractor Analysis:**
    *   *Why A is correct:* The GCP Professional Cloud Database Engineer exam is a multiple-choice scenario exam. Questions present real-world technical and business constraints and ask you to identify the best-fitting GCP service, architecture decision, security control, or operational procedure. No fill-in-the-blank or hands-on lab components exist.
    *   *Why B is incorrect:* The exam does not test CLI command syntax memorization through fill-in-the-blank questions. GCP professional exams are scenario-based multiple-choice, not command recall tests.
    *   *Why C is incorrect:* The GCP Professional Cloud Database Engineer exam does not include a hands-on lab component. It is a written scenario-based exam administered through Kryterion or Certiport.
    *   *Why D is incorrect:* The exam covers the full GCP database portfolio, including Cloud SQL, Cloud Spanner, Bigtable, Firestore, BigQuery, AlloyDB, Database Migration Service, Cloud Monitoring, and IAM security across all database services.

---

---

**Question 3**
A database administrator needs to **analyze the execution plan of a slow query on a Cloud SQL for PostgreSQL instance to identify whether an index scan or sequential scan is being used**. Which SQL command is most appropriate?
A) EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 'C001';
B) GRANT SELECT ON orders TO analyst_role;
C) CREATE INDEX idx_orders_customer ON orders(customer_id);
D) SELECT * FROM orders WHERE customer_id = 'C001';
*   **Correct Answer:** A) EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 'C001';
*   **Distractor Analysis:**
    *   *Why A is correct:* `EXPLAIN ANALYZE` executes the query and returns the actual execution plan, including whether the planner chose a `Seq Scan` (sequential scan, no index) or an `Index Scan` (index used), actual row counts, and actual execution time at each step. This is the definitive diagnostic tool for query performance in PostgreSQL and Cloud SQL for PostgreSQL.
    *   *Why B is incorrect:* `GRANT SELECT` assigns read privilege to a user or role; it does not execute a query or produce an execution plan.
    *   *Why C is incorrect:* `CREATE INDEX` creates a new index on a column; it does not analyze an existing query's execution plan.
    *   *Why D is incorrect:* `SELECT * FROM orders WHERE customer_id = 'C001'` executes the query and returns the result data, but without `EXPLAIN ANALYZE`, it does not reveal the execution plan, scan type, or performance characteristics.

---

**Question 4**
An enterprise is evaluating the Google Cloud Professional Cloud Database Engineer certification. Which exam domain represents the highest-stakes skill tested, where choosing the wrong answer due to service selection confusion most frequently causes candidates to fail?
A) Selecting the correct GCP database service based on workload characteristics — distinguishing when to use Cloud SQL vs. Cloud Spanner vs. Bigtable vs. Firestore vs. BigQuery vs. AlloyDB.
B) Memorizing the exact SQL syntax for creating indexes on every supported database engine.
C) Configuring VPC subnets and firewall rules for database connectivity.
D) Writing Cloud Monitoring alerting policy YAML configurations from memory.
*   **Correct Answer:** A) Selecting the correct GCP database service based on workload characteristics.
*   **Distractor Analysis:**
    *   *Why A is correct:* Service selection is the most heavily tested and most commonly missed domain on the GCP Professional Cloud Database Engineer exam. Candidates who do not clearly understand the specific use-case fit, limitations, and differentiators of each GCP database service frequently choose answers that are "close" but wrong — such as Spanner for a workload that only needs Cloud SQL, or Bigtable for a workload that needs SQL JOINs.
    *   *Why B is incorrect:* The exam does not test SQL syntax memorization. Scenario questions test architectural judgment and operational decision-making, not the exact syntax of DDL commands.
    *   *Why C is incorrect:* VPC and networking configuration is a supporting topic covered in security and connectivity scenarios, but it is not the primary domain where candidates fail. Service selection drives the majority of incorrect answers.
    *   *Why D is incorrect:* The exam does not require writing YAML configurations from memory. Cloud Monitoring configuration is a conceptual topic — you need to know what metrics exist and when to alert on them, not the exact YAML structure.

---

**Question 5**
A final exam preparation scenario: A company's compliance officer states that all database query logs must be retained for 7 years, immutably, and must be searchable using SQL. Which architecture satisfies all three requirements?
A) Configure a Cloud Logging log sink to export Cloud SQL query logs to a BigQuery dataset with a table expiration policy set to 2,557 days (7 years), and use BigQuery SQL to search the logs.
B) Enable Cloud SQL automated backups with a 7-year retention policy in the Cloud SQL settings.
C) Store query logs in a Cloud Firestore collection with a TTL policy set to never expire.
D) Export Cloud SQL logs to a Cloud Storage bucket with a 7-year lifecycle retention policy and use gsutil to search log files.
*   **Correct Answer:** A) Configure a Cloud Logging log sink to export Cloud SQL query logs to a BigQuery dataset with a table expiration policy set to 2,557 days, and use BigQuery SQL to search the logs.
*   **Distractor Analysis:**
    *   *Why A is correct:* A Cloud Logging log sink exports Cloud SQL query logs (Data Access logs, slow query logs) to BigQuery in near-real time. BigQuery's table expiration can be configured for any number of days (7 years = 2,557 days). Once in BigQuery, logs are immutable (historical rows cannot be updated) and fully searchable using standard SQL — satisfying all three requirements: 7-year retention, immutability, and SQL-searchable.
    *   *Why B is incorrect:* Cloud SQL automated backups retain database snapshot files, not query log records. Backups cannot be queried using SQL; they must be restored to an instance first. Additionally, Cloud SQL backup retention is configurable up to 365 days, not 7 years.
    *   *Why C is incorrect:* Firestore is a document database with a proprietary query API, not SQL. While Firestore can store log records as documents, the requirement for SQL-searchable logs is not satisfied by Firestore's query model.
    *   *Why D is incorrect:* Cloud Storage satisfies immutability (with Object Versioning and retention policies) and 7-year retention, but `gsutil` is a command-line file management tool, not a SQL query engine. Searching 7 years of logs with `gsutil` is impractical and does not satisfy the SQL-searchable requirement.

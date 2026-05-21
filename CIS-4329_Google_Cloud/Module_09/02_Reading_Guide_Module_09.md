# Reading Guide: Module 09 – Cloud SQL and Cloud Spanner: Managed Relational Databases
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

### Introduction
Welcome to **Module 09 – Cloud SQL and Cloud Spanner: Managed Relational Databases**! GCP provides several fully managed relational database services. This module covers Cloud SQL for familiar MySQL, PostgreSQL, and SQL Server workloads; Cloud Spanner for globally distributed, horizontally scalable relational databases; and Cloud Bigtable and Firestore for NoSQL alternatives. The ACE exam tests your ability to select the right database service for a given scenario and understand how these services handle availability, replication, and access control.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The ACE exam tests these concepts in scenario-based questions.

*   **Cloud SQL**: A fully managed relational database service supporting MySQL, PostgreSQL, and SQL Server. GCP handles patching, backups, replication, and failover. Cloud SQL instances run in a single region; a read replica or high availability (HA) configuration with a standby in the same region provides automatic failover. Maximum database size is in the terabyte range — suitable for most enterprise applications that do not need global distribution.

*   **Cloud Spanner**: A fully managed, globally distributed relational database that provides horizontal scalability with strong ANSI SQL support and external consistency (serializable transactions across regions). Use Cloud Spanner when you need both relational semantics and global scale — for example, a financial ledger or inventory system serving multiple continents with no downtime tolerance.

*   **Cloud SQL High Availability (HA)**: A Cloud SQL configuration that creates a primary instance and a standby instance in different zones within the same region. If the primary fails, Cloud SQL automatically promotes the standby. HA uses synchronous replication to ensure the standby has the latest data before acknowledging writes.

*   **Read Replica**: A Cloud SQL instance that serves read-only queries, reducing load on the primary. Read replicas use asynchronous replication, which means they may lag slightly behind the primary. They do not participate in automatic failover — they are for read scaling only.

*   **Cloud Bigtable**: A fully managed NoSQL wide-column database designed for very high throughput and low latency at petabyte scale. Ideal for time-series data, IoT telemetry, financial market data, and analytics pipelines. It is not relational — there is no SQL support and no ACID transactions across rows.

*   **Firestore**: A fully managed serverless NoSQL document database. Data is stored as documents within collections. Firestore supports ACID transactions within a single document and has a native mobile/web SDK. Use Firestore when you need flexible document storage, real-time sync, or offline support for mobile apps.

---

### 2. Certification Exam Tips

*   **Cloud SQL vs. Cloud Spanner — the key differentiator is global scale**: The ACE exam frequently presents scenarios that describe a regional MySQL or PostgreSQL workload — the answer is Cloud SQL. If the scenario mentions multiple regions, global consistency, or millions of transactions per second, the answer is Cloud Spanner. Spanner is significantly more expensive than Cloud SQL.

*   **Cloud SQL HA vs. Read Replica — different purposes**: HA provides automatic failover for availability; a read replica provides read scalability. The exam tests whether you understand that read replicas do not provide automatic failover. If a question asks how to ensure the database remains available during a zone failure, the answer is HA configuration, not a read replica.

*   **Cloud SQL Private IP and Cloud SQL Auth Proxy**: The recommended way to connect application code to Cloud SQL is via the Cloud SQL Auth Proxy, which handles encrypted connections and IAM-based authentication without requiring a public IP or VPC peering configuration. The exam may ask about secure Cloud SQL connectivity — prefer Auth Proxy over public IP with SSL.

*   **Choosing between Bigtable and Firestore**: The exam distinguishes use cases. Bigtable = high-throughput analytics/time-series at scale, row-key access patterns, no rich query support. Firestore = flexible document structure, rich queries, real-time sync, mobile apps. Neither is the right answer when the scenario describes a relational schema with JOINs.

*   **Study Resource**: The freeCodeCamp ACE course covers Cloud SQL, Spanner, Bigtable, and Firestore with side-by-side comparisons relevant to exam scenarios: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Databases chapter using the video index.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading**: Review Cloud SQL instance configuration including high availability, read replicas, and connection methods: [Cloud SQL Overview](https://cloud.google.com/sql/docs/mysql/introduction). Pay attention to the HA vs. read replica distinction and the Cloud SQL Auth Proxy.
*   **Required Reading**: Review the Cloud Spanner overview to understand when to choose Spanner over Cloud SQL: [Cloud Spanner Overview](https://cloud.google.com/spanner/docs/whatis). The comparison table between Spanner and Cloud SQL is directly exam-relevant.
*   **Required Video**: Watch the Databases segment of the ACE certification course: [Google Cloud ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ). Navigate to the Cloud SQL and Spanner chapter using the video index.

---

### Lab & Command Integration
In this module's lab, you will create a Cloud SQL instance, configure high availability, and connect to it using the Cloud SQL Auth Proxy. Key commands to practice:

*   `gcloud sql instances create my-instance --database-version=MYSQL_8_0 --tier=db-n1-standard-2 --region=us-central1` — creates a Cloud SQL MySQL instance
*   `gcloud sql instances patch my-instance --availability-type=REGIONAL` — enables high availability (regional) on an existing instance
*   `gcloud sql connect my-instance --user=root` — connects to Cloud SQL using the built-in proxy (for development)
*   `gcloud sql instances create my-replica --master-instance-name=my-instance --replica-type=READ` — creates a read replica

---

### 3. Study Checklist
- [ ] Read the glossary terms and be able to explain each in your own words.
- [ ] Read the [Cloud SQL Overview](https://cloud.google.com/sql/docs/mysql/introduction) documentation page.
- [ ] Read the [Cloud Spanner Overview](https://cloud.google.com/spanner/docs/whatis) documentation page.
- [ ] Watch the Databases segment of the [ACE Certification Course by freeCodeCamp](https://www.youtube.com/watch?v=UGRDM86MBIQ).
- [ ] Complete the module lab: create a Cloud SQL instance with HA and connect via Auth Proxy.
- [ ] Proceed to the weekly quiz.

# Quiz: Module 09 – Cloud SQL and Cloud Spanner: Managed Relational Databases
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company runs a customer-facing e-commerce application backed by a MySQL database in a single Compute Engine VM. You want to migrate to a fully managed database service that handles automated backups, patches, and provides automatic failover if the primary database zone goes down. Which GCP service and configuration should you use?

A) Cloud Spanner with a multi-region configuration
B) Cloud SQL for MySQL with a high availability (regional) configuration
C) Cloud SQL for MySQL with a read replica in a second zone
D) Cloud Bigtable with a MySQL-compatible schema

*   **Correct Answer:** B) Cloud SQL for MySQL with a high availability (regional) configuration
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud Spanner is a globally distributed database appropriate for workloads requiring horizontal scalability and global consistency. For a standard MySQL migration with zone-level failover, Cloud SQL HA is the correct and far more cost-effective choice.
    *   *Why C is incorrect:* A read replica serves read-only traffic and uses asynchronous replication. It does not participate in automatic failover — if the primary instance fails, the read replica does not automatically promote. High availability (regional) configuration is required for automatic failover.
    *   *Why D is incorrect:* Cloud Bigtable is a NoSQL wide-column database and is not MySQL-compatible. It does not support SQL queries, JOINs, or relational schemas, making it unsuitable for a MySQL application migration.

---

**Question 2**
You are designing a financial trading platform that requires a relational database supporting ANSI SQL with ACID transactions. The platform must serve users in North America, Europe, and Asia with strong consistency — every user must always read the latest committed data regardless of which region they connect to. Which database service meets these requirements?

A) Cloud SQL for PostgreSQL with read replicas in each region
B) Cloud Bigtable with a global replication profile
C) Cloud Spanner with a multi-region instance configuration
D) Firestore in Native mode with multi-region replication

*   **Correct Answer:** C) Cloud Spanner with a multi-region instance configuration
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud SQL read replicas use asynchronous replication, meaning replicas may lag behind the primary. Users reading from a replica could see stale data — this violates the strong consistency requirement. Cloud SQL also cannot serve writes from multiple regions simultaneously.
    *   *Why B is incorrect:* Cloud Bigtable does not support SQL or ACID transactions. It is designed for high-throughput analytics and time-series workloads using row-key access patterns, not for relational financial data with complex transactions and JOINs.
    *   *Why D is incorrect:* Firestore is a NoSQL document database. While it supports ACID transactions within a single document and multi-region replication, it does not support ANSI SQL or relational schemas with JOINs — it is not suitable for a SQL-based trading platform.

---

**Question 3**
A Cloud SQL instance in your project is configured with a public IP address. Your application running on a Compute Engine VM needs to connect securely to the database. The security team requires that database credentials not be embedded in application code and that the connection be encrypted. Which approach follows Google's recommended best practice?

A) Add the VM's external IP address to the Cloud SQL authorized networks list and connect using SSL certificates.
B) Use the Cloud SQL Auth Proxy running on the VM, which handles encryption and uses IAM-based authentication automatically.
C) Configure a VPN tunnel between the VM's VPC and the Cloud SQL network to establish a private connection.
D) Store the database password in a Compute Engine metadata key and retrieve it in the application startup script.

*   **Correct Answer:** B) Use the Cloud SQL Auth Proxy running on the VM, which handles encryption and uses IAM-based authentication automatically.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Adding a VM's external IP to the Cloud SQL authorized networks list exposes the database port to that IP over the public internet. While SSL encrypts the connection, it still requires managing SSL certificates manually and does not use IAM-based authentication — the Auth Proxy is simpler and more secure.
    *   *Why C is incorrect:* Cloud SQL instances do not reside in a customer VPC — they are managed by Google. There is no VPC network to tunnel into. The Cloud SQL Auth Proxy or Private IP with VPC peering are the correct connectivity patterns.
    *   *Why D is incorrect:* Storing a database password in Compute Engine instance metadata is a security anti-pattern — metadata is accessible to any process running on the VM and is not encrypted at rest in a secrets management system. Use Secret Manager or the Auth Proxy for credential-free connectivity.

---

**Question 4**
Your application writes time-series sensor data from 10,000 IoT devices at a sustained rate of 500,000 writes per second. Each record has a device ID, timestamp, and a set of numeric sensor readings. The data will be queried by device ID and time range for analytics pipelines. Relational JOIN queries are not required. Which GCP database service is most appropriate?

A) Cloud SQL for MySQL with a high-performance db-n1-highmem-96 instance
B) Cloud Spanner with a single-region configuration
C) Cloud Bigtable with a row key composed of device ID and reverse timestamp
D) Firestore with one document per sensor reading stored in a devices collection

*   **Correct Answer:** C) Cloud Bigtable with a row key composed of device ID and reverse timestamp
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Cloud SQL is a single-node relational database that cannot sustain 500,000 writes per second regardless of instance size. It is designed for transactional workloads with hundreds or thousands of concurrent connections, not petabyte-scale IoT ingestion.
    *   *Why B is incorrect:* Cloud Spanner scales horizontally and can handle high write throughput, but it is significantly more expensive than Bigtable and is optimized for relational workloads requiring ACID transactions and SQL JOINs — capabilities that are not needed here. Bigtable is the purpose-built service for this use case.
    *   *Why D is incorrect:* Firestore is a document database optimized for flexible schemas, real-time sync, and mobile applications. It has throughput and document size limits that make it unsuitable for 500,000 writes per second from IoT devices. It also lacks Bigtable's columnar storage efficiency for time-series data.

---

**Question 5**
You need to export a Cloud SQL database backup to Cloud Storage so it can be used to seed a development environment. You also want to automate this export to run every Sunday at 2:00 AM. Which combination of GCP features accomplishes this with the least operational overhead?

A) Write a cron job on a Compute Engine VM that runs `mysqldump` and uploads the output to Cloud Storage using `gsutil cp`.
B) Use Cloud SQL's built-in export feature triggered by Cloud Scheduler invoking a Cloud Function that calls the Cloud SQL Admin API.
C) Enable Cloud SQL automated backups and use Cloud Scheduler to trigger a snapshot of the backup storage bucket weekly.
D) Configure a Cloud SQL read replica and take a Compute Engine persistent disk snapshot of the replica's underlying storage every Sunday.

*   **Correct Answer:** B) Use Cloud SQL's built-in export feature triggered by Cloud Scheduler invoking a Cloud Function that calls the Cloud SQL Admin API.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Running `mysqldump` from a Compute Engine VM requires maintaining a VM, managing credentials, handling network connectivity, and monitoring the cron job. This adds significant operational overhead compared to using Cloud SQL's native export API with Cloud Scheduler.
    *   *Why C is incorrect:* Cloud SQL automated backups create internal backups managed by Cloud SQL — they are not stored in a customer-accessible Cloud Storage bucket. There is no mechanism to snapshot the automated backup storage directly; the correct approach is to use the Cloud SQL export API to write a SQL dump to Cloud Storage.
    *   *Why D is incorrect:* Cloud SQL instances run on Google-managed infrastructure — you do not have access to take Compute Engine persistent disk snapshots of the underlying storage. Read replicas cannot be snapshotted at the disk level by the customer.

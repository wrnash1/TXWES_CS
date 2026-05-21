# Quiz: Module 06 - RDS and Aurora – Managed Relational Databases
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company's MySQL database on RDS experiences slow query performance during business hours due to high read traffic from reporting workloads. Writes are minimal. Which RDS feature should the solutions architect implement to improve read performance without impacting the primary instance?
*   A) Enable RDS Multi-AZ to distribute read queries to the standby instance.
*   B) Create one or more RDS Read Replicas and direct reporting traffic to the Read Replica endpoint.
*   C) Increase the RDS instance type to a larger size to handle more concurrent connections.
*   D) Enable RDS automated backups to free up I/O on the primary instance.
*   **Correct Answer:** B) RDS Read Replicas are asynchronous copies of the primary designed to serve read traffic, directly offloading read queries from the primary instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The Multi-AZ standby instance does NOT serve read traffic. It is a passive failover target only. Directing queries to it is not possible through the standard endpoint configuration. This is the most common RDS exam trap.
    *   *Why B is correct:* Read Replicas have a separate endpoint that accepts SELECT queries. The reporting application connects to the Read Replica endpoint, distributing the read load. Asynchronous replication means minimal impact on the primary write performance.
    *   *Why C is incorrect:* Scaling up (vertical scaling) improves throughput for the primary but does not distribute the read load. The same primary instance still handles all queries, and vertical scaling increases cost linearly. Read Replicas scale horizontally for reads specifically.
    *   *Why D is incorrect:* Automated backups use transaction log streaming to S3 and can create some I/O overhead, but disabling them does not meaningfully address read query bottlenecks and is inadvisable from a durability standpoint.

---

**Question 2**
Which of the following is the most accurate description of **Amazon Aurora's storage architecture** compared to standard Amazon RDS?
*   A) Aurora uses EBS volumes attached to a single EC2-backed database server, identical to how standard RDS engines store data.
*   B) Aurora stores data across three Availability Zones with six copies of every data page, uses a distributed self-healing storage layer that automatically grows up to 128 TB, and does not require manual storage provisioning.
*   C) Aurora replicates data synchronously to a standby replica in one additional AZ, identical to RDS Multi-AZ, providing high availability at the cost of higher write latency.
*   D) Aurora uses S3 as its primary storage backend, storing all data as objects and using SQL-to-S3 translation layers to execute queries.
*   **Correct Answer:** B) Aurora's distributed storage layer writes to six copies across three AZs, automatically scales storage, and provides faster recovery than traditional RDS because the storage is decoupled from compute.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Aurora does not use EBS volumes attached to a single server. Its storage is a purpose-built distributed shared storage layer, fundamentally different from standard RDS engine storage.
    *   *Why B is correct:* Aurora's log-structured distributed storage is one of its key differentiators. Six copies across three AZs means Aurora can tolerate two AZ failures without data loss. Auto-grow to 128 TB eliminates manual storage provisioning. This architecture enables Aurora's faster failover (30 seconds vs. 60–120 seconds for RDS Multi-AZ).
    *   *Why C is incorrect:* Aurora's storage redundancy is built into the storage layer itself, not a Multi-AZ standby compute instance. Aurora Replicas (read replicas) share the same underlying storage rather than replicating data separately — this is architecturally different from RDS Multi-AZ.
    *   *Why D is incorrect:* Aurora does not use S3 as its primary query storage. Aurora exports backups to S3 and integrates with S3 for some features, but query data resides in Aurora's proprietary distributed storage cluster, not S3 objects.

---

**Question 3**
A company is designing a disaster recovery strategy for a critical RDS PostgreSQL database. Their RPO (Recovery Point Objective) is 5 minutes and their RTO (Recovery Time Objective) is 30 minutes. Which configuration best meets these requirements?
*   A) Enable automated backups with a 7-day retention period and rely on point-in-time recovery for all disaster scenarios.
*   B) Enable RDS Multi-AZ for automatic synchronous replication and failover, combined with automated backups for point-in-time recovery.
*   C) Create a nightly manual snapshot and restore from it during a disaster event.
*   D) Enable Cross-Region Read Replicas in a secondary Region and rely on asynchronous replication lag for recovery.
*   **Correct Answer:** B) Multi-AZ provides automatic failover within 60–120 seconds (meeting the 30-minute RTO) with synchronous replication (zero data loss, meeting the 5-minute RPO). Automated backups provide PITR for additional scenarios.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Point-in-time recovery restores to a new RDS instance, which takes time proportional to the database size — potentially hours. This cannot reliably meet a 30-minute RTO for a large database. Also, automated backups alone do not provide automatic failover.
    *   *Why B is correct:* Multi-AZ synchronous replication means zero data loss (RPO = 0, which satisfies the 5-minute RPO requirement). Automatic failover to the standby completes in 60–120 seconds, well within the 30-minute RTO. This is the standard HA+DR configuration for RDS.
    *   *Why C is incorrect:* A nightly snapshot has an RPO of up to 24 hours — far exceeding the 5-minute requirement. Restoring from a snapshot also takes time proportional to database size and likely exceeds the 30-minute RTO.
    *   *Why D is incorrect:* Cross-Region Read Replicas use asynchronous replication with variable lag. For a 5-minute RPO guarantee, asynchronous replication is insufficient. Promoting a Read Replica is also a manual process that may take longer than 30 minutes depending on replication lag and database size.

---

**Question 4**
An operations team needs to enable encryption at rest for an existing unencrypted RDS MySQL database that is already in production. Which procedure is required?
*   A) Enable encryption in the RDS console by toggling the "Encryption" setting on the running instance — it applies immediately without downtime.
*   B) Create an encrypted Read Replica and promote it to a new primary after replication catches up.
*   C) Take a snapshot of the unencrypted instance, copy the snapshot with the "Enable Encryption" option, restore a new encrypted RDS instance from the encrypted snapshot, and update the application's connection string.
*   D) Modify the RDS parameter group to enable AES-256 encryption, then restart the instance to apply the setting.
*   **Correct Answer:** C) RDS encryption can only be enabled at creation time; the supported migration path is snapshot → encrypted copy → restore as a new encrypted instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* AWS does not allow enabling encryption on an existing RDS instance in place. The encryption setting is immutable after instance creation. There is no toggle that enables encryption without data migration.
    *   *Why B is incorrect:* You cannot create an encrypted Read Replica from an unencrypted primary. RDS requires the source to be encrypted if the Read Replica is to be encrypted. This path is not available for the described scenario.
    *   *Why C is correct:* This is the AWS-documented procedure for encrypting an existing unencrypted RDS database. The key steps are: snapshot the source → copy snapshot with encryption → restore from the encrypted copy. The application connection string must be updated to point to the new endpoint.
    *   *Why D is incorrect:* RDS parameter groups control engine-level settings (like `max_connections` or `innodb_buffer_pool_size`), not storage encryption. Storage-at-rest encryption is a host-level EBS encryption feature, not a database engine parameter.

---

**Question 5**
A startup needs a relational database for a new application with unpredictable and variable traffic — ranging from zero activity overnight to thousands of connections during peak events. They want to minimize costs during idle periods and avoid managing database capacity manually. Which database option is most appropriate?
*   A) RDS MySQL with Multi-AZ enabled in the largest available instance size to handle any peak load.
*   B) RDS PostgreSQL with Auto Scaling enabled on Read Replicas to handle traffic spikes.
*   C) Amazon Aurora Serverless v2, which automatically scales compute capacity from a minimum (including near-zero during idle) to a maximum based on actual load.
*   D) Amazon DynamoDB with strong consistency reads and Global Tables for SQL compatibility.
*   **Correct Answer:** C) Aurora Serverless v2 is purpose-built for variable and unpredictable workloads, scaling database compute capacity automatically and billing only for consumed capacity — ideal for cost minimization with zero idle waste.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Over-provisioning to the largest instance size wastes significant money during the overnight idle periods. Multi-AZ doubles the instance cost. This is the opposite of cost optimization for variable workloads.
    *   *Why B is incorrect:* Auto Scaling on RDS Read Replicas scales read capacity, not the primary write instance capacity. The primary instance must still be statically sized. This does not address the idle-period cost problem.
    *   *Why C is correct:* Aurora Serverless v2 adjusts Aurora Capacity Units (ACUs) in fine-grained increments and can scale to near-zero during idle periods. You pay per ACU-second consumed rather than per hour of provisioned capacity. This is the canonical answer for "relational database with variable/unpredictable workload."
    *   *Why D is incorrect:* DynamoDB is a NoSQL key-value/document database — it does not support SQL, relational schemas, or JOIN operations. Suggesting it for an application requiring relational data with SQL queries is architecturally incorrect.


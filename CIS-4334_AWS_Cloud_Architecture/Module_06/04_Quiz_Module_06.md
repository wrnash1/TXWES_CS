# Quiz: Module 06 - RDS and Aurora: Managed Relational Databases

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

A solutions architect is designing a database tier for an application that runs heavy reporting queries. The reporting queries are causing performance problems for the transactional workload. Which RDS feature should the architect implement to offload the reporting queries?

- A) Enable RDS Multi-AZ to distribute read traffic to the standby instance
- B) Increase the DB instance class to a larger size to handle both workloads
- C) Create one or more Read Replicas and direct reporting queries to the Read Replica endpoint
- D) Enable RDS storage autoscaling to automatically increase IOPS for the queries

### Answer 1

Correct Answer: C

### Explanation 1

- A is incorrect: The Multi-AZ standby instance does not serve any read traffic. It exists only as a hot standby for automatic failover and is completely invisible to the application.
- B is incorrect: Scaling up the DB instance class increases capacity but does not architecturally separate the workloads. The reporting queries still compete with transactions for the same CPU, I/O, and memory resources.
- C is correct: Read Replicas receive asynchronous replication from the primary and can serve SELECT queries. Directing the reporting team to use the Read Replica endpoint offloads read traffic from the primary, freeing its resources for transactional workloads.
- D is incorrect: Storage autoscaling adjusts storage capacity (size) not IOPS allocation. It does not address the resource contention between reporting and transactional workloads.

---

## Question 2

An RDS for MySQL database is currently unencrypted. A security audit requires all production databases to be encrypted at rest using AWS KMS. What is the correct process to encrypt the existing database?

- A) Modify the DB instance in the console to enable encryption — the change takes effect during the next maintenance window
- B) Take a snapshot of the unencrypted instance, copy the snapshot with encryption enabled, and restore a new DB instance from the encrypted snapshot
- C) Enable encryption in the RDS parameter group — it applies to all new data written after the change
- D) Stop the DB instance, enable encryption via the AWS CLI, then restart the instance

### Answer 2

Correct Answer: B

### Explanation 2

- A is incorrect: RDS does not support enabling encryption on an existing unencrypted DB instance through a modify operation. The encryption setting cannot be changed after instance creation.
- B is correct: The only supported process to encrypt an existing unencrypted RDS instance is the three-step snapshot process: (1) create a snapshot of the unencrypted instance, (2) copy the snapshot and enable encryption during the copy operation, (3) restore a new DB instance from the encrypted snapshot. All automated backups, snapshots, and Read Replicas of the new instance will also be encrypted.
- C is incorrect: There is no RDS parameter group setting that enables encryption at rest. Encryption must be enabled at the instance level during creation.
- D is incorrect: Stopping and restarting an RDS instance does not enable encryption. Encryption cannot be enabled on an instance that was created without it.

---

## Question 3

A company requires their database to remain available during an Availability Zone failure with automatic failover and zero data loss. Which RDS configuration satisfies both requirements?

- A) RDS with a Read Replica in a different AZ with automatic promotion
- B) RDS Multi-AZ with a synchronous standby in a different AZ
- C) RDS with automated daily backups and a 7-day retention period
- D) RDS with a Read Replica in a different Region

### Answer 3

Correct Answer: B

### Explanation 3

- A is incorrect: Read Replicas use asynchronous replication, which means there can be replication lag and potential data loss during failover. Read Replica promotion is not automatic — it requires a manual action.
- B is correct: RDS Multi-AZ uses synchronous replication — every transaction is committed on the primary AND the standby before the application receives acknowledgment. This guarantees zero data loss (RPO of 0). Failover is automatic when the primary fails.
- C is incorrect: Automated backups enable point-in-time recovery but do not provide automatic failover or real-time standby capacity. Recovery from backup requires creating a new instance.
- D is incorrect: Cross-region Read Replicas use asynchronous replication (with potential data loss) and require manual promotion. They are a DR strategy, not a same-Region HA solution.

---

## Question 4

A company's application uses AWS Lambda functions that open a new database connection to Amazon RDS for MySQL on every invocation. During peak traffic, the Lambda functions receive 5,000 concurrent invocations, causing RDS to hit its maximum connection limit and refusing new connections. Which solution resolves this problem?

- A) Increase the RDS instance class to a larger size to support more connections
- B) Enable RDS Multi-AZ to distribute connections between the primary and standby
- C) Use Amazon RDS Proxy to pool database connections between Lambda and RDS
- D) Create additional Read Replicas to distribute the Lambda connections

### Answer 4

Correct Answer: C

### Explanation 4

- A is incorrect: Increasing the instance class increases the maximum connection limit, but this is a temporary solution. As Lambda concurrency grows, any fixed limit will eventually be hit. The architectural problem is the connection-per-invocation pattern.
- B is incorrect: The Multi-AZ standby does not serve connections. It exists only for failover.
- C is correct: RDS Proxy maintains a pool of database connections and multiplexes many Lambda invocations over a smaller number of long-lived database connections. 5,000 Lambda invocations might use only 50-100 actual database connections through the proxy, well within RDS limits. RDS Proxy is the AWS-recommended solution specifically for Lambda-to-RDS connection management.
- D is incorrect: Read Replicas can serve read queries but cannot accept write transactions. If the Lambda functions include writes (INSERT, UPDATE, DELETE), directing them to Read Replicas is not possible.

---

## Question 5

What is the primary architectural advantage of Amazon Aurora over standard Amazon RDS?

- A) Aurora supports more database engines than RDS
- B) Aurora uses a distributed shared storage layer that stores 6 copies of data across 3 AZs and enables faster failover by eliminating storage replication during failover
- C) Aurora automatically encrypts all data without any configuration
- D) Aurora supports larger instance sizes than standard RDS

### Answer 5

Correct Answer: B

### Explanation 5

- A is incorrect: Aurora supports fewer engines than RDS (MySQL-compatible and PostgreSQL-compatible only, versus six engines for RDS). Aurora's advantage is not in breadth of engine support.
- B is correct: Aurora's defining architectural difference is its distributed shared storage layer, which stores 6 copies of data across 3 AZs automatically. During failover, a new primary instance simply takes over the shared storage without waiting for replication to catch up — enabling approximately 30-second failover compared to 60-120 seconds for standard RDS Multi-AZ.
- C is incorrect: Aurora encryption requires explicit enablement at instance creation, just like standard RDS. Encryption is not automatic by default.
- D is incorrect: Aurora and standard RDS support overlapping instance size ranges. Aurora's advantage is in architecture and performance, not maximum instance size.

---

## Question 6

A solutions architect needs to design a database solution for a new SaaS application. The application has unpredictable traffic — sometimes receiving thousands of requests per minute, other times receiving no requests for hours. Cost must be minimized and the team does not want to pay for idle database capacity. Which database deployment option best meets these requirements?

- A) RDS for MySQL with a large DB instance class to handle peak load
- B) Amazon Aurora Serverless v2
- C) RDS for MySQL with Read Replicas for scaling
- D) Amazon Aurora with provisioned instances in a Multi-AZ cluster

### Answer 6

Correct Answer: B

### Explanation 6

- A is incorrect: A large RDS instance runs at full price 24/7 regardless of load. During idle periods, the company pays for capacity it is not using. This is not cost-efficient for variable workloads.
- B is correct: Aurora Serverless v2 automatically scales database capacity in fine-grained ACU increments based on actual demand. During low-traffic periods, it scales down to minimum capacity (potentially 0 ACUs with a cold start delay). The company pays only for the capacity consumed, which matches the unpredictable traffic pattern perfectly.
- C is incorrect: Read Replicas scale read throughput but do not scale compute capacity automatically. They also do not address the idle cost problem.
- D is incorrect: A provisioned Aurora cluster runs continuously at a fixed cost regardless of load. It is more cost-effective than RDS for high-performance workloads but still wastes money during idle periods.

---

## Question 7

An Aurora cluster experiences a failure of the primary (writer) instance. The cluster has two Aurora Replicas. What is the expected behavior?

- A) The cluster becomes unavailable until the primary instance is manually replaced
- B) Aurora automatically promotes one of the Aurora Replicas to the primary role in approximately 30 seconds
- C) The cluster fails over to a standby instance in a different Region automatically
- D) Traffic is automatically redirected to the Read Replicas, which now accept write traffic

### Answer 7

Correct Answer: B

### Explanation 7

- A is incorrect: Aurora failover is automatic and does not require manual intervention.
- B is correct: When an Aurora primary fails, Aurora automatically selects the highest-priority (or highest-priority tier) Aurora Replica and promotes it to the writer role. This happens in approximately 30 seconds. The cluster writer endpoint is automatically updated to point to the new primary.
- C is incorrect: Aurora Regional clusters do not automatically fail over to a different Region. Cross-region failover requires Aurora Global Database and is a manual or semi-manual operation.
- D is incorrect: Aurora Replicas serve read-only traffic until promoted. They do not automatically accept write traffic without being promoted to primary. Writing to a Read Replica endpoint before promotion would result in an error.

---

## Question 8

A company wants to enable automatic rotation of database passwords for their RDS for PostgreSQL instance. The passwords should rotate every 30 days without requiring application code changes. Which AWS service provides this capability?

- A) AWS IAM with automated key rotation configured
- B) AWS Systems Manager Parameter Store with a scheduled Lambda rotation function
- C) AWS Secrets Manager with rotation enabled for RDS credentials
- D) Amazon CloudWatch scheduled events triggering a Lambda function to update the password

### Answer 8

Correct Answer: C

### Explanation 8

- A is incorrect: IAM key rotation applies to IAM user access keys, not database passwords. IAM does not manage relational database credentials.
- B is incorrect: Parameter Store can store passwords but does not have native RDS rotation built in. While you could build a rotation solution, it requires custom Lambda functions and is significantly more complex than Secrets Manager.
- C is correct: AWS Secrets Manager natively integrates with Amazon RDS to automatically rotate database credentials. When rotation is enabled, Secrets Manager generates a new password, updates the RDS instance, and updates the secret — all transparently. Applications retrieve the current password by calling Secrets Manager; the rotation is invisible to application code.
- D is incorrect: This is a custom solution that would require writing and maintaining a rotation Lambda function. Secrets Manager provides this capability as a managed native integration.

---

## Question 9

A company uses Amazon Aurora MySQL with automated backups and a 7-day retention period. At 2:00 PM on a Wednesday, a developer accidentally drops the customer table. The error is discovered at 2:30 PM. Can the company recover the customer table to its state at 1:59 PM?

- A) No — Aurora automated backups only capture the database at the daily backup window, so recovery is limited to the previous night's backup
- B) Yes — Aurora's automated backup system captures both daily snapshots and continuous transaction logs, enabling point-in-time recovery to any second within the 7-day retention window
- C) No — Aurora stores backups in Glacier, making retrieval take 3-5 hours
- D) Yes — but only if a manual snapshot was taken before 2:00 PM that day

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: Aurora (and RDS) automated backups consist of both daily database snapshots AND continuous transaction log backups. The transaction logs are captured continuously and stored in S3, enabling recovery to any specific second within the retention window.
- B is correct: Aurora automated backups capture transaction logs continuously in addition to daily snapshots. Point-in-time recovery allows restoring to any second within the retention period. Recovering to 1:59 PM (1 minute before the table drop) is possible.
- C is incorrect: Aurora automated backups are stored in Amazon S3, not Glacier. Restore from automated backup creates a new DB instance and typically completes within minutes to tens of minutes depending on database size.
- D is incorrect: Manual snapshots are not required for point-in-time recovery. Automated backups combined with transaction logs provide continuous recovery capability.

---

## Question 10

A company needs a database solution for a global application that serves users in North America, Europe, and Asia Pacific. Users in each region should read data with the lowest possible latency, and the system must recover from a full regional failure of the primary region within 1 minute. Which solution meets all requirements?

- A) RDS for MySQL with Multi-AZ enabled in the primary Region and Read Replicas in each secondary Region
- B) Amazon Aurora Global Database with a primary Region and secondary Regions in Europe and Asia Pacific
- C) Three separate RDS instances, one in each Region, synchronized using application-level replication
- D) Amazon Aurora Multi-AZ cluster in the primary Region with CloudFront caching for global read performance

### Answer 10

Correct Answer: B

### Explanation 10

- A is incorrect: Cross-region Read Replicas for standard RDS use asynchronous replication. Promotion of a Read Replica to primary after a regional failure takes 30-60 minutes and requires manual intervention. This does not meet the 1-minute RTO requirement.
- B is correct: Aurora Global Database provides sub-second cross-region replication and supports managed failover with RTO under 1 minute. Users in each Region can read from their local Aurora Replicas for low latency. In a regional failure, the secondary Region can be promoted to primary quickly.
- C is incorrect: Application-level replication introduces significant complexity, potential data consistency issues, and operational overhead. It is not a best-practice AWS architecture for this requirement.
- D is incorrect: CloudFront caches static content — it cannot serve dynamic database reads. A Multi-AZ cluster in a single Region provides HA within that Region but does not address the global latency or cross-region failover requirements.

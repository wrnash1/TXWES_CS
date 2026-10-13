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

---

## Question 11

A company runs an RDS for PostgreSQL database that processes thousands of short-lived database connections from Lambda functions. The Lambda functions are invoked up to 2,000 times per minute, each opening and closing a new database connection. The database is experiencing connection exhaustion. Which AWS service is specifically designed to address this problem?

- A) Amazon ElastiCache for Redis as a connection pooling proxy in front of RDS
- B) Amazon RDS Proxy, which pools and multiplexes application connections to the database
- C) Enable RDS Multi-AZ to distribute connections between the primary and standby instances
- D) Increase the max_connections parameter on the RDS instance to accommodate all Lambda connections

### Answer 11

Correct Answer: B

### Explanation 11

- A is incorrect: ElastiCache for Redis is an in-memory cache for caching data, not a database connection proxy. It cannot pool PostgreSQL database connections or serve as a proxy to RDS.
- B is correct: Amazon RDS Proxy is a fully managed, highly available database proxy that pools and multiplexes application connections. Lambda functions connect to the RDS Proxy endpoint instead of directly to RDS. The proxy maintains a pool of established connections to the database and reuses them, reducing the number of actual database connections to a fraction of the application connections. RDS Proxy supports RDS for MySQL, PostgreSQL, MariaDB, Aurora MySQL, and Aurora PostgreSQL.
- C is incorrect: RDS Multi-AZ maintains a synchronous standby replica for failover. The standby instance does not serve any read or write traffic during normal operation. It does not solve the connection exhaustion problem.
- D is incorrect: The max_connections parameter is limited by the instance's available memory. Increasing it beyond the database's capacity causes memory exhaustion and instability. The fundamental problem is the connection-per-invocation pattern of Lambda, which requires connection pooling, not simply a higher connection limit.

---

## Question 12

A solutions architect is comparing RDS Multi-AZ and RDS Read Replicas for a high-availability use case. An application requires that if the primary database fails, the application can resume writes within 2 minutes with no DNS endpoint changes. Which configuration satisfies this requirement?

- A) RDS Read Replica with automatic promotion configured
- B) RDS Multi-AZ deployment using synchronous replication
- C) Amazon Aurora with three Read Replicas and manual failover scripts
- D) RDS for MySQL with a cross-region Read Replica for failover

### Answer 12

Correct Answer: B

### Explanation 12

- A is incorrect: RDS Read Replicas use asynchronous replication. Promoting a Read Replica to primary requires a manual action or custom automation, takes several minutes, and results in a new instance with a different endpoint DNS name. The application would need to be updated with the new endpoint unless DNS is manually updated.
- B is correct: RDS Multi-AZ uses synchronous replication to a standby replica in a second AZ. On primary failure, RDS automatically promotes the standby in 60-120 seconds and updates the existing endpoint DNS record to point to the new primary. The application connection string does not change, satisfying the "no DNS endpoint changes" requirement within 2 minutes.
- C is incorrect: Aurora Read Replicas support automatic failover, but the question specifies RDS Multi-AZ behavior specifically (synchronous replication, automatic failover, same endpoint). Aurora has different characteristics than standard RDS for this scenario.
- D is incorrect: Cross-region Read Replicas are for disaster recovery, not same-region high availability. Cross-region promotion takes significantly longer than 2 minutes and requires manual intervention.

---

## Question 13

A development team needs to create multiple isolated copies of a production Aurora MySQL database for testing without impacting production performance and without waiting for a full database snapshot restore. Which Aurora feature provides near-instant database clones?

- A) Aurora Read Replicas provisioned in a separate Aurora cluster
- B) Aurora Fast Cloning using copy-on-write, which creates a clone without copying data until it diverges
- C) AWS Database Migration Service to replicate the database to a separate cluster
- D) RDS point-in-time restore to a new Aurora cluster for each testing environment

### Answer 13

Correct Answer: B

### Explanation 13

- A is incorrect: Aurora Read Replicas are connected to the source cluster and share the same storage volume. They serve reads from the primary cluster but are not isolated for destructive testing. Read Replicas cannot be promoted to independent clusters for testing without disrupting replication.
- B is correct: Aurora Fast Cloning uses a copy-on-write mechanism. The clone initially points to the same underlying storage pages as the original cluster. Data is only physically copied when either the clone or the original cluster modifies a page. This makes cloning nearly instantaneous regardless of database size. Testing environments can make destructive changes without affecting production data.
- C is incorrect: AWS Database Migration Service performs a full data copy from source to target, which takes significant time proportional to database size. It also imposes replication load on the source database. This is not equivalent to Fast Cloning's instantaneous copy-on-write approach.
- D is incorrect: RDS point-in-time restore creates a new instance from a backup snapshot and transaction logs. The restore time is proportional to database size and can take tens of minutes to hours. For creating multiple isolated test environments quickly, Fast Cloning is orders of magnitude faster.

---

## Question 14

An application uses Amazon RDS for MySQL with automated backups retained for 7 days. A DBA accidentally runs a `DROP TABLE` command at 3:15 PM that deletes critical production data. The DBA needs to recover the deleted data with minimal data loss. What is the correct recovery approach?

- A) Restore the most recent daily automated backup snapshot from yesterday, losing approximately 24 hours of data
- B) Use RDS point-in-time restore to create a new DB instance at 3:14 PM (one minute before the DROP TABLE), then migrate the recovered data back to the production instance
- C) Enable Multi-AZ on the RDS instance to restore from the standby replica, which was not affected by the DROP TABLE command
- D) Use AWS Backup to restore the table from the most recent hourly backup taken before 3:15 PM

### Answer 14

Correct Answer: B

### Explanation 14

- A is incorrect: Restoring the most recent daily snapshot would recover to approximately the same time the previous day's backup was taken — potentially 24 hours before the data loss. With 7-day backup retention and continuous transaction logs, point-in-time recovery to one minute before the incident is possible.
- B is correct: RDS point-in-time restore uses automated backups (daily snapshots) combined with continuously captured transaction logs stored in S3. Recovery to 3:14 PM is feasible because transaction logs are applied on top of the daily snapshot to reconstruct the database state at the specified second. The restore creates a new DB instance (not the original) to avoid additional risk. The missing data can then be exported from the recovery instance and imported into the production instance.
- C is incorrect: RDS Multi-AZ standby replication is synchronous — the `DROP TABLE` command was replicated to the standby instance immediately. The standby is not a separate backup that avoids replication of destructive operations. Multi-AZ provides HA for infrastructure failures, not protection against logical errors.
- D is incorrect: AWS Backup integrates with RDS but uses the same automated backup mechanism (daily snapshots + transaction logs). AWS Backup does not provide hourly snapshots by default for RDS unless a custom backup plan is configured. Even if available, point-in-time restore is more precise than restoring from an hourly backup.

---

## Question 15

A financial services company needs to migrate from an Oracle database to a managed AWS database service. The application uses Oracle-specific stored procedures, PL/SQL packages, and Oracle's analytical functions extensively. The migration timeline is 18 months. Which migration path aligns best with AWS recommendations for this scenario?

- A) Migrate directly to Amazon Aurora PostgreSQL and rewrite all Oracle-specific code immediately
- B) Migrate to Amazon RDS for Oracle (Bring Your Own License) to maintain compatibility, then plan a gradual refactoring to Aurora PostgreSQL using Schema Conversion Tool
- C) Migrate to Amazon DynamoDB and convert all relational queries to NoSQL key-value operations
- D) Continue running Oracle on EC2 instances in AWS to avoid any refactoring cost

### Answer 15

Correct Answer: B

### Explanation 15

- A is incorrect: Migrating directly to Aurora PostgreSQL requires rewriting all Oracle-specific PL/SQL code, stored procedures, and Oracle analytical functions before migration. With a complex Oracle workload, an immediate full rewrite within 18 months carries high risk of regressions and project failure.
- B is correct: RDS for Oracle allows a lift-and-shift migration with full Oracle compatibility, immediately reducing operational overhead (AWS manages backups, patching, hardware) while maintaining application compatibility. The AWS Schema Conversion Tool (SCT) and Database Migration Service (DMS) can then be used to gradually refactor and migrate to Aurora PostgreSQL over the 18-month timeline. This two-phase approach reduces risk while achieving the cloud migration goal.
- C is incorrect: DynamoDB is a NoSQL key-value and document database. Converting a relational Oracle database with complex stored procedures and analytical functions to DynamoDB would require a fundamental redesign of the data model and application logic. This is a multi-year effort, not a 18-month migration.
- D is incorrect: Running Oracle on EC2 gives no managed service benefits. The customer still manages OS patching, storage, backups, replication, and hardware provisioning — the same operational burden as on-premises. This option does not achieve any cloud adoption benefit.

---

## Question 16

A company uses Amazon Aurora PostgreSQL. A database administrator notices that during peak hours, the primary writer instance CPU reaches 95% while the two Aurora Reader instances are only at 15% CPU. Application read queries are being routed to the writer instance. What is the most likely cause?

- A) Aurora Reader instances cannot serve read traffic until explicitly promoted to writer
- B) The application is using the cluster endpoint (writer endpoint) for all queries instead of the reader endpoint
- C) Aurora Reader instances do not support complex read queries — only simple SELECT statements
- D) The Aurora cluster parameter group is configured to route all traffic to the writer for consistency

### Answer 16

Correct Answer: B

### Explanation 16

- A is incorrect: Aurora Reader instances serve read traffic by default and automatically when the application connects to the reader endpoint. They do not require promotion to serve read queries.
- B is correct: Aurora provides two primary endpoints: the cluster endpoint (which always routes to the current writer) and the reader endpoint (which load-balances across all Reader instances). If the application is using the cluster endpoint for all queries — including read queries — all traffic reaches the writer. The fix is to update read-heavy operations in the application to use the reader endpoint.
- C is incorrect: Aurora Reader instances fully support all PostgreSQL read query types including complex analytical queries, aggregations, joins, and stored procedure calls. They are identical in capability to the writer for read operations.
- D is incorrect: Aurora cluster parameter groups configure database-level settings (like connection timeout, log settings), not traffic routing. Traffic routing is determined by which endpoint the application uses.

---

## Question 17

A solutions architect needs to ensure that an Amazon RDS for MySQL database instance cannot be accessed from the public internet. The application tier runs in EC2 instances in private subnets within the same VPC. Which configuration correctly implements private-only database access?

- A) Disable the RDS instance's public accessibility setting, deploy the instance in a private subnet, and configure the database security group to allow inbound MySQL traffic only from the application tier's security group
- B) Enable the RDS instance's public accessibility setting but restrict the security group to the EC2 instances' IP addresses
- C) Deploy the RDS instance in a public subnet with a Network ACL blocking all traffic from 0.0.0.0/0
- D) Enable RDS Multi-AZ to move the primary database instance to a private subnet while the standby remains in a public subnet

### Answer 17

Correct Answer: A

### Explanation 17

- A is correct: This is the correct three-part configuration: (1) disable public accessibility (no public IP assigned to the RDS instance); (2) deploy in a private subnet (no route to an Internet Gateway); (3) security group allows port 3306 inbound from the application tier security group only. This ensures the database is completely isolated from the public internet.
- B is incorrect: Enabling public accessibility assigns a public IP to the RDS instance, making it DNS-resolvable from the internet. While the security group restricts access, EC2 IP addresses can change, and relying on IP-based security group rules for RDS access is an anti-pattern. Security group references (by SG ID) are the correct approach.
- C is incorrect: Deploying RDS in a public subnet with public accessibility enabled means the database has a publicly routable IP address. NACL rules add a layer but are not the correct primary control for this requirement — the instance should be in a private subnet with no public accessibility.
- D is incorrect: Both the primary and standby instances in an RDS Multi-AZ deployment follow the same subnet and public accessibility configuration. Multi-AZ does not allow different accessibility settings for primary vs. standby.

---

## Question 18

A company is evaluating Amazon Aurora Serverless v2 for a new application. The application has unpredictable traffic — virtually idle for most of the day but with occasional spikes to high load. Which characteristic of Aurora Serverless v2 is most relevant to this use case?

- A) Aurora Serverless v2 automatically scales storage capacity but uses fixed compute capacity
- B) Aurora Serverless v2 automatically scales compute capacity (ACUs) in fine-grained increments in response to load changes without pausing connections
- C) Aurora Serverless v2 pauses the database after 5 minutes of inactivity, resuming on the first connection with a brief cold start delay
- D) Aurora Serverless v2 is only available for development workloads and cannot be used in production

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: Aurora Serverless v2 scales both compute and storage automatically. Compute is measured in Aurora Capacity Units (ACUs) that scale in 0.5 ACU increments. Storage scales independently as data grows.
- B is correct: Aurora Serverless v2 continuously scales compute capacity from a configured minimum to maximum ACU value. Scaling is nearly instantaneous and does not drop existing connections. This makes it ideal for applications with unpredictable workloads that need to go from near-zero to high capacity quickly without over-provisioning.
- C is incorrect: Pausing after inactivity with a cold-start resume time is a characteristic of Aurora Serverless v1, not v2. Aurora Serverless v2 does not pause — it scales down to the configured minimum ACUs but remains continuously running with no cold-start delay. The pause-and-resume behavior of v1 is what made it unsuitable for production workloads.
- D is incorrect: Aurora Serverless v2 is production-ready and supports all Aurora features including Multi-AZ, Read Replicas, Global Database, and RDS Proxy. It can be used for production workloads.

---

## Question 19

An RDS for MySQL instance is encrypted with an AWS KMS customer-managed key. A data analyst needs to share a copy of a database snapshot with a second AWS account for analysis. What are the required steps?

- A) Export the snapshot to S3 and share the S3 bucket with the second account using a bucket policy
- B) Copy the snapshot, share the KMS key policy to grant the second account kms:Decrypt and kms:CreateGrant permissions, then share the encrypted snapshot with the second account
- C) Disable encryption on the snapshot before sharing, as encrypted snapshots cannot be shared between accounts
- D) Enable cross-region replication on the RDS instance, then share the replicated instance with the second account

### Answer 19

Correct Answer: B

### Explanation 19

- A is incorrect: Exporting a snapshot to S3 is a separate feature for data extraction to Parquet format. It does not create a sharable RDS snapshot copy in another account. The analyst would receive raw Parquet files, not a usable RDS instance.
- B is correct: Sharing an encrypted RDS snapshot with another account requires: (1) copying the snapshot (optionally to ensure it is encrypted with a customer-managed key rather than the default KMS key, which cannot be shared); (2) modifying the KMS key policy to grant the destination account `kms:Decrypt` and `kms:CreateGrant` permissions; (3) sharing the snapshot with the destination account ID. The destination account can then copy the snapshot using the shared key and restore it.
- C is incorrect: Encrypted RDS snapshots CAN be shared between accounts, but only when encrypted with a customer-managed KMS key (not the default AWS-managed key). The solution is proper KMS key sharing, not disabling encryption.
- D is incorrect: Cross-region replication creates Read Replicas in another Region, not in another AWS account. RDS Read Replicas cannot be transferred to a different AWS account.

---

## Question 20

A company runs Amazon Aurora MySQL with one writer and three reader instances. During a maintenance window, the writer instance fails. What happens to the Aurora cluster?

- A) All Aurora instances stop functioning until the writer is manually replaced from a snapshot
- B) Aurora automatically promotes one of the reader instances to writer based on replica promotion tier priority with no data loss due to Aurora's shared storage architecture
- C) The reader instances continue serving read traffic but write operations fail until the writer is manually restored
- D) Aurora Multi-AZ standby promotes to writer, and the three reader instances remain as readers

### Answer 20

Correct Answer: B

### Explanation 20

- A is incorrect: Aurora does not require manual recovery from a snapshot for writer instance failure. Aurora's automatic failover promotes a reader to writer in typically under 30 seconds.
- B is correct: Aurora uses a shared distributed storage volume that all instances (writer and readers) connect to. Because the storage layer is separate from the compute layer, there is no data loss during failover — the new writer connects to the same storage volume. Aurora automatically promotes the reader with the highest priority promotion tier to become the new writer. The failover typically completes within 30 seconds.
- C is incorrect: While readers continue serving reads during a brief failover window, Aurora automatically promotes a reader to writer without manual intervention. Write operations are unavailable only during the short promotion window (typically 30 seconds).
- D is incorrect: Aurora does not use a separate Multi-AZ "standby" instance in the same way as standard RDS Multi-AZ. Aurora Reader instances are the replicas, and one of them is promoted to writer on failure. There is no separate standby that is distinct from the readers.

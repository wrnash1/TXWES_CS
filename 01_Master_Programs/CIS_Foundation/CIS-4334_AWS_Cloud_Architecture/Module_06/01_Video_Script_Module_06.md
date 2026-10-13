# Video Script: Module 06 - RDS and Aurora: Managed Relational Databases

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome back. I am Professor Nash and this is Module 06: RDS and Aurora — Managed Relational Databases.

Relational databases are at the core of most enterprise applications. AWS offers Amazon RDS as a managed relational database service supporting six database engines, and Amazon Aurora as AWS's own high-performance cloud-native relational engine. The SAA-C03 exam tests your ability to choose between RDS and Aurora, configure high availability and read scaling, design backup and recovery strategies, and understand when a managed database is the right choice versus running a database on EC2.

By the end of this module you will be able to:

- Select the correct RDS database engine for a given workload
- Configure RDS Multi-AZ for high availability
- Design Read Replicas for read scaling
- Explain Aurora's architecture and its advantages over standard RDS
- Configure automated backups, snapshots, and point-in-time recovery
- Apply RDS security controls including encryption and network isolation

---

## [01:30 - 06:00] RDS Core Concepts

[SHOW DIAGRAM]

Amazon RDS is a managed relational database service. "Managed" means AWS handles the hardware provisioning, database setup, patching (of the OS and database engine), automated backups, and failover. You manage the schema, queries, users, and application-level configuration.

RDS supports six database engines:

- MySQL — most widely deployed open-source relational database
- PostgreSQL — advanced open-source with strong standards compliance
- MariaDB — MySQL-compatible community fork
- Oracle — enterprise relational database (BYOL or license-included)
- Microsoft SQL Server — enterprise relational database for Windows-based applications
- Amazon Aurora — AWS's cloud-native engine (MySQL-compatible or PostgreSQL-compatible)

For the SAA-C03 exam: if a scenario mentions migrating a MySQL or PostgreSQL workload to AWS with minimal refactoring, RDS for MySQL or RDS for PostgreSQL is the answer. If the scenario mentions higher performance and availability requirements, Aurora is the answer.

**RDS instance types** follow the same family naming convention as EC2. The db.r6g and db.r5 families are memory-optimized and commonly used for production databases. The db.t3 burstable family is appropriate for development and low-traffic instances. Instance size determines CPU, memory, and network bandwidth.

**RDS storage** uses EBS volumes. Three storage types:

- General Purpose SSD (gp2/gp3): balanced price/performance; gp3 allows independent IOPS configuration without paying for a higher storage size
- Provisioned IOPS SSD (io1/io2): for I/O-intensive workloads requiring consistent, high IOPS
- Magnetic: legacy; do not use for new deployments

Storage autoscaling automatically increases storage capacity when available space falls below a threshold. No downtime required. You set a maximum storage limit to prevent runaway growth.

---

## [06:00 - 11:00] High Availability: Multi-AZ Deployments

[SHOW DIAGRAM]

RDS Multi-AZ is the primary HA mechanism for RDS. When you enable Multi-AZ, AWS provisions a standby DB instance in a different AZ within the same Region. The primary and standby instances are synchronized using synchronous replication — every transaction committed on the primary is simultaneously committed on the standby before the application receives acknowledgment.

If the primary instance fails — due to hardware failure, AZ-level failure, OS crash, or maintenance — RDS automatically fails over to the standby. The failover typically completes in 60-120 seconds. The DNS name for the database endpoint is automatically updated to point to the standby. Your application reconnects using the same endpoint — no code change required.

Critical exam points about Multi-AZ:

- Multi-AZ is for availability, not read performance. The standby instance does not serve read traffic.
- Failover is automatic and handled by AWS.
- Failover triggers include: primary instance failure, primary AZ failure, primary DB instance OS failure, manual failover initiation, and certain maintenance events.
- Multi-AZ does not protect against logical data corruption or accidental DELETE statements — that is what backups and point-in-time recovery address.

[SHOW DIAGRAM]

RDS Multi-AZ Cluster (introduced after Multi-AZ Instance) deploys one writer and two reader DB instances across three AZs using semi-synchronous replication. Reads can be distributed to the reader instances. This provides both HA and limited read scaling in one deployment. It is currently available for MySQL and PostgreSQL.

---

## [11:00 - 15:00] Read Replicas for Horizontal Read Scaling

[SHOW DIAGRAM]

Read Replicas are separate DB instances that receive asynchronous replication from the primary (or another Read Replica). They serve read traffic — SELECT queries — without adding load to the primary instance.

Key Read Replica characteristics:

- Asynchronous replication — there is replication lag. Reads may return slightly stale data.
- Up to 5 Read Replicas per source DB instance (more for Aurora)
- Read Replicas can be in the same Region, a different Region (cross-region Read Replicas), or even a different AWS account
- Read Replicas have their own DNS endpoint — you must configure your application to send reads to the replica endpoint and writes to the primary endpoint
- Read Replicas can be promoted to independent databases for disaster recovery or migration

Read Replicas vs. Multi-AZ:

| Feature | Multi-AZ | Read Replica |
|---|---|---|
| Purpose | High availability | Read scalability |
| Replication | Synchronous | Asynchronous |
| Serves traffic | Standby: no | Yes (reads only) |
| Automatic failover | Yes | No (must be promoted manually) |
| Cross-region | Yes (standby in different Region with Aurora Multi-Region) | Yes |

For the SAA-C03 exam: if a scenario mentions reducing read load on the primary database or scaling read throughput, the answer is Read Replicas. If a scenario mentions automatic failover or database HA, the answer is Multi-AZ.

---

## [15:00 - 19:00] Amazon Aurora

[SHOW DIAGRAM]

Amazon Aurora is AWS's cloud-native relational database engine. It is MySQL-compatible or PostgreSQL-compatible, meaning you can use the same application drivers and tools as MySQL or PostgreSQL. However, Aurora's underlying storage and replication architecture is fundamentally different.

**Aurora storage architecture:** Aurora separates compute from storage. The data is stored in a distributed storage layer that automatically replicates across 6 copies in 3 AZs within the Region. The storage layer self-heals — if a storage node fails, it is replaced automatically without any impact on the running database instances.

**Aurora cluster:** An Aurora cluster has one primary (read-write) instance and up to 15 Aurora Replicas (read-only) that all connect to the same shared storage layer. Failover to an Aurora Replica takes about 30 seconds — faster than standard RDS Multi-AZ because the new primary does not need to wait for replication catchup.

**Aurora performance:** Aurora is up to 5x faster than MySQL and up to 3x faster than PostgreSQL on the same hardware, according to AWS benchmarks. It achieves this through the distributed storage layer, write-ahead log optimization, and buffer cache sharing across readers.

**Aurora Serverless** — Aurora Serverless v2 is an auto-scaling configuration for Aurora that scales database compute capacity automatically based on application demand. It scales in fine-grained increments (ACUs — Aurora Capacity Units). Use Aurora Serverless for applications with highly variable or unpredictable workloads — development databases, infrequently used applications.

**Aurora Global Database** — extends Aurora to multiple Regions with sub-second cross-region replication. One primary Region and up to 5 secondary Regions. Each secondary Region has up to 16 read-only Aurora Replicas. For disaster recovery: if the primary Region fails, promote a secondary Region to primary in under a minute. Use Aurora Global Database for: global applications needing low-latency reads worldwide, or RPO/RTO requirements that require cross-region HA.

---

## [19:00 - 22:00] Backup, Security, and Operational Topics

**Automated Backups** — RDS automatically takes daily snapshots and captures transaction logs. Retention period: 1 to 35 days (default 7 days). Point-in-time recovery lets you restore the database to any second within the retention window. Automated backups are stored in S3 and do not count against your RDS storage.

**Manual Snapshots** — user-initiated snapshots of the DB instance stored in S3. Unlike automated backups, manual snapshots do not expire automatically. They persist until you delete them. Copy snapshots to another Region for cross-region backup.

**Encryption** — enable encryption at rest when creating the RDS instance. Uses AWS KMS. Encrypted instances have encrypted storage, automated backups, snapshots, and Read Replicas. You cannot encrypt an existing unencrypted instance — you must create a snapshot, copy it with encryption enabled, and restore from the encrypted snapshot.

[SHOW DIAGRAM]

**Network isolation** — deploy RDS instances in private subnets (DB Subnet Group). Security groups control network access. No public IP address should be assigned to production RDS instances. VPC Endpoint connections to RDS are not available — all RDS connections go through the private VPC network or VPN/Direct Connect.

**IAM Database Authentication** — enables authentication to MySQL and PostgreSQL RDS using IAM credentials instead of a database password. The application calls the RDS API to generate a short-lived authentication token (15 minutes). The token is used to connect. No password stored in the application. Works with EC2 instance roles for fully passwordless authentication.

---

## [22:00 - 24:00] Module Summary

RDS manages six database engines with managed patching, backups, and failover. Multi-AZ provides synchronous standby for automatic failover — availability, not performance. Read Replicas provide asynchronous read copies for scaling reads — not for automatic failover.

Aurora separates compute and storage with 6 copies across 3 AZs. Aurora Replicas fail over in 30 seconds. Aurora Serverless scales automatically for variable workloads. Aurora Global Database spans Regions for low-latency reads and cross-region DR.

Automated backups support point-in-time recovery. Manual snapshots persist until deleted. Encryption must be enabled at creation. Deploy in private subnets and control access with security groups.

In the lab this week you will explore RDS configuration using the AWS CLI and design a HA database architecture. The Reading Guide has a complete RDS vs. Aurora comparison table, backup strategy reference, and security checklist.

For your certification study: <aws.amazon.com/certification>

---

End of Module 06 Video Script

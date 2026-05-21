# Reading Guide: Module 06 - RDS and Aurora – Managed Relational Databases
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 06 - RDS and Aurora – Managed Relational Databases**! Amazon Relational Database Service (RDS) and Amazon Aurora are AWS's primary managed relational database offerings. This module covers the database engines supported by RDS, the high-availability mechanisms of Multi-AZ deployments, the performance benefits of Read Replicas, and how Aurora differs from standard RDS in architecture and scaling. Database selection and HA configuration are among the most common scenario questions on the SAA-C03 exam.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Amazon RDS**: A managed relational database service that handles routine database administration tasks — hardware provisioning, OS patching, database software installation, backups, and failure detection. RDS supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Amazon Aurora. The customer manages schema design, query optimization, and application-level database configuration. RDS cannot be accessed at the OS level (no SSH to the database server).

*   **RDS Multi-AZ Deployment**: A high-availability configuration that maintains a synchronous standby replica of the primary database in a different Availability Zone. If the primary instance fails (hardware, network, or OS failure), RDS automatically fails over to the standby with a typical downtime of 60–120 seconds. Multi-AZ is for HA and durability — the standby cannot serve read traffic. The failover is managed automatically without changing the database endpoint (CNAME flips).

*   **RDS Read Replicas**: Asynchronous copies of the primary database used to offload read queries and improve aggregate read throughput. Read Replicas can be in the same AZ, a different AZ, or a different Region (Cross-Region Read Replicas for disaster recovery). Up to 5 Read Replicas per primary (15 for Aurora). They are NOT for HA failover — they are for read scaling and can be promoted to standalone in a disaster recovery scenario.

*   **Amazon Aurora**: A MySQL- and PostgreSQL-compatible relational database rebuilt by AWS for the cloud, offering 3–5x the throughput of standard RDS MySQL. Aurora stores data in a distributed, self-healing storage layer across 3 AZs (6 copies of data), automatically growing storage up to 128 TB. Aurora Serverless v2 scales compute capacity automatically based on demand. Aurora Global Database spans multiple Regions with sub-second replication.

*   **RDS Automated Backups and Snapshots**: RDS automatically backs up the database to S3 daily (transaction logs are backed up every 5 minutes), enabling point-in-time recovery (PITR) for any second within the retention period (1–35 days). Manual DB Snapshots are user-initiated backups that persist until explicitly deleted, useful for pre-migration checkpoints. Backups do not replace Multi-AZ for HA — they serve data recovery, not uptime.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** RDS/Aurora content primarily appears in Design Resilient Architectures (26%) and Design High-Performing Architectures (24%). Multi-AZ vs. Read Replica selection is the most common RDS exam trap.

*   **Multi-AZ vs. Read Replica Exam Trap:** Multi-AZ = high availability (automatic failover, no read traffic, synchronous replication). Read Replica = read scaling (serves read traffic, asynchronous replication, manual promotion). The exam presents scenarios and expects you to choose the right feature for the stated goal.

*   **Aurora vs. RDS Exam Selection:** Choose Aurora when a question describes requirements for high throughput, automatic storage scaling, multi-Region replication with low RPO (Aurora Global Database), or serverless auto-scaling compute. Choose standard RDS when the question specifies a third-party engine (e.g., Oracle SE2, SQL Server) or when Aurora's additional cost is a factor in cost optimization scenarios.

*   **RDS Storage Options:** gp2 and gp3 SSD for general workloads. io1 for high IOPS requiring provisioned performance (OLTP databases). Magnetic (standard) is legacy and not recommended. io1 is the answer when a question specifies IOPS requirements above gp3 limits.

*   **Encryption at Rest:** RDS encryption must be enabled at creation time — you cannot encrypt an existing unencrypted instance in place. The workaround is to create a snapshot, copy the snapshot with encryption enabled, and restore from the encrypted snapshot.

*   **Study Resource:** The Amazon RDS User Guide covers Multi-AZ, Read Replicas, and Aurora: [Amazon RDS User Guide](https://docs.aws.amazon.com/rds/index.html). Review the "High availability" and "Read Replicas" chapters specifically.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the RDS and Aurora chapters in the AWS Solutions Architect study materials. Review the [Amazon Aurora User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) to understand Aurora's distributed storage architecture and how it differs from RDS. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Disaster Recovery of Workloads on AWS" whitepaper, which covers RDS Multi-AZ and Read Replica patterns in the context of RTO/RPO.

*   **Required Video:** Watch the RDS and Aurora module in the official course playlist, focusing on the architectural diagrams for Multi-AZ deployment, Read Replica topology, and Aurora's distributed storage layer: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Launch an RDS MySQL instance with Multi-AZ enabled:** Create an RDS MySQL instance in a private subnet group with Multi-AZ enabled. Observe the primary and standby AZ placement. Use the RDS console to initiate a forced failover and measure the time to reconnect.

*   **Create a Read Replica and test read offloading:** From the Multi-AZ primary, create a Read Replica in a different AZ. Connect a read-heavy application to the Read Replica endpoint and verify that reads do not impact the primary's performance metrics in CloudWatch.

*   **Configure automated backup retention and test PITR:** Set the backup retention window to 7 days. Modify a table row, note the timestamp, then restore to a point in time 5 minutes before the modification using the "Restore to Point in Time" action and verify the row state.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand the difference between Multi-AZ (HA) and Read Replicas (read scaling) at [https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html).
- [ ] Review Aurora architecture at [https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.html).
- [ ] Watch the RDS/Aurora video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab provisioning RDS, configuring Multi-AZ, creating a Read Replica, and testing PITR.
- [ ] Proceed to the weekly quiz.

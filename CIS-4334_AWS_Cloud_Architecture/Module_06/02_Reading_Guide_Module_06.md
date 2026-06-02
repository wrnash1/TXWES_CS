# Reading Guide: Module 06 - RDS and Aurora: Managed Relational Databases

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

Amazon RDS and Aurora are the primary managed relational database services on AWS. The SAA-C03 exam tests database architecture decisions across multiple domains: selecting the right engine for a workload, configuring availability and read scaling, designing backup strategies, and securing database access. This reading guide provides the complete reference tables, architecture comparisons, and security configurations needed to answer exam scenario questions accurately.

---

## Section 1: RDS vs. Aurora Comparison

### 1.1 Core Comparison Table

| Feature | Amazon RDS | Amazon Aurora |
|---|---|---|
| Engines | MySQL, PostgreSQL, MariaDB, Oracle, SQL Server | MySQL-compatible, PostgreSQL-compatible |
| Storage | EBS (per-instance) | Distributed shared storage (auto-scaled) |
| Storage replication | N/A (EBS snapshot-based) | 6 copies across 3 AZs automatically |
| Max Read Replicas | 5 | 15 |
| Failover time (Multi-AZ) | 60-120 seconds | ~30 seconds (Aurora Replica promotion) |
| Storage auto-scaling | Yes (within EBS limits) | Yes (auto-grows up to 128 TiB) |
| Serverless option | No | Aurora Serverless v2 |
| Global database | No | Aurora Global Database |
| Performance vs. MySQL | Comparable | Up to 5x faster |
| Performance vs. PostgreSQL | Comparable | Up to 3x faster |
| Cost | Lower for small instances | Higher per-instance; lower per-replica cost |

### 1.2 Engine Selection Guide

| Scenario | Recommended Engine |
|---|---|
| Open-source workload, cost-sensitive, MySQL-compatible | RDS for MySQL |
| Open-source workload, strong SQL standards compliance, JSON support | RDS for PostgreSQL |
| MySQL workload requiring higher performance and HA | Aurora MySQL |
| PostgreSQL workload requiring higher performance and HA | Aurora PostgreSQL |
| SAP, Oracle APEX, existing Oracle license (BYOL) | RDS for Oracle |
| .NET application, Windows Server, existing SQL Server license | RDS for SQL Server |
| Variable/unpredictable workload, development, pay-per-use | Aurora Serverless v2 |
| Multi-region low-latency reads or cross-region DR | Aurora Global Database |

### 1.3 Multi-AZ vs. Read Replica Decision

| Requirement | Solution |
|---|---|
| Automatic failover during AZ outage | Multi-AZ |
| High availability with no data loss | Multi-AZ (synchronous replication) |
| Reduce read load on primary | Read Replica |
| Scale read throughput horizontally | Read Replica |
| Cross-region disaster recovery | Cross-region Read Replica (RDS) or Aurora Global |
| Reporting queries that cannot impact primary | Read Replica |
| Development copy of production database | Read Replica (promote to independent) |

---

## Section 2: RDS High Availability Architecture

### 2.1 Multi-AZ Deployment

In a Multi-AZ deployment, AWS provisions a synchronous standby in a different AZ. The standby is not accessible for reads or writes — it exists only as a hot standby for automatic failover.

Failover triggers:

- Primary DB instance failure
- Primary AZ failure
- Primary DB instance OS crash
- DB instance server type change (maintenance)
- Manual failover using Reboot with failover

Failover behavior:

- DNS CNAME for the database endpoint is updated to point to the standby
- Application must reconnect (most connection pools handle this automatically)
- Typical failover: 60-120 seconds for standard RDS; ~30 seconds for Aurora

### 2.2 RDS Multi-AZ Cluster

The RDS Multi-AZ Cluster configuration (for MySQL and PostgreSQL) deploys a writer and two readers across three AZs with semi-synchronous replication. Benefits over Multi-AZ Instance:

- Faster failover (semi-sync commit means reader is nearly caught up)
- Readers can serve traffic, providing limited read scaling
- All three instances write to storage in their own AZ

### 2.3 Aurora Cluster Architecture

```text
Aurora Cluster (us-east-1)

Writer instance (us-east-1a) ─────────────────────┐
                                                    │
Reader instance (us-east-1b) ───────────────────── Aurora Shared Storage
                                                    │ (6 copies across 3 AZs)
Reader instance (us-east-1c) ─────────────────────┘

Cluster endpoints:
  Writer endpoint: mydb.cluster-xxxxx.us-east-1.rds.amazonaws.com
  Reader endpoint: mydb.cluster-ro-xxxxx.us-east-1.rds.amazonaws.com (load balances reads)
  Instance endpoint: mydb-instance-1.xxxxx.us-east-1.rds.amazonaws.com (specific instance)
```

Aurora endpoints:

- Cluster (writer) endpoint: always routes to current writer; fails over automatically
- Reader endpoint: load balances across all Aurora Replicas
- Instance endpoint: routes to a specific instance; use when you need to control which instance receives traffic

---

## Section 3: Backup and Recovery

### 3.1 Backup Types Comparison

| Feature | Automated Backups | Manual Snapshots |
|---|---|---|
| Initiation | Automatic (daily + transaction logs) | User-initiated at any time |
| Retention | 1-35 days (configurable) | Until manually deleted |
| Point-in-time recovery | Yes (to any second in retention window) | No (restore to snapshot point only) |
| Storage | Charged against backup storage quota | Charged as EBS snapshot storage |
| Cross-region copy | Via automated backup replication | Manually copy snapshot to another Region |
| Restores to | New DB instance (same or different AZ) | New DB instance |

### 3.2 Recovery Point Objective and Recovery Time Objective

| Recovery Scenario | RPO | RTO | Mechanism |
|---|---|---|---|
| AZ failure | 0 (synchronous) | 60-120 seconds | RDS Multi-AZ failover |
| Accidental data deletion (last hour) | Minutes (replication lag) | 5-30 minutes | Point-in-time recovery |
| Region failure | Minutes to hours | 30-60 minutes | Cross-region snapshot restore |
| Region failure (Aurora) | Seconds (Aurora Global) | Under 1 minute | Aurora Global Database failover |

---

## Section 4: RDS Security Controls

### 4.1 Security Checklist

| Control | Implementation |
|---|---|
| Network isolation | Deploy in private subnets (DB Subnet Group); no public IP |
| Security group | Allow DB port only from application tier security group |
| Encryption at rest | Enable AWS KMS encryption at instance creation |
| Encryption in transit | Force SSL/TLS in parameter group (require_secure_transport=ON for MySQL) |
| IAM DB authentication | Enable for MySQL/PostgreSQL; use short-lived tokens instead of passwords |
| Secrets Manager | Store and rotate DB credentials automatically; integrate with RDS |
| Audit logging | Enable general log, slow query log, error log to CloudWatch Logs |
| Parameter group | Restrict dangerous settings (disable local_infile for MySQL) |

### 4.2 Encryption Constraints

- Encryption must be enabled when the DB instance is created
- Encrypted instances produce encrypted automated backups, snapshots, and Read Replicas
- To encrypt an unencrypted instance: take a snapshot, copy the snapshot with encryption enabled, restore a new instance from the encrypted snapshot
- Read Replicas of encrypted instances must also be encrypted
- Encrypted instances in one Region can only use KMS keys from that Region

### 4.3 IAM Database Authentication Flow

```text
Application (EC2 with IAM role)
  1. Calls rds-db:connect via AWS SDK to generate auth token
  2. Auth token (valid 15 minutes) is passed as database password
  3. RDS validates token against IAM and grants connection
  4. No static database password stored in application or Secrets Manager
```

IAM DB authentication is supported for MySQL and PostgreSQL RDS engines and Aurora MySQL/PostgreSQL.

---

## Section 5: Aurora Serverless and Global Database

### 5.1 Aurora Serverless v2

Aurora Serverless v2 scales database capacity automatically in fine-grained increments measured in Aurora Capacity Units (ACUs). Key characteristics:

- Scales from 0.5 ACUs to 128 ACUs (each ACU is approximately 2 GB RAM plus proportional CPU)
- Scaling happens within seconds in response to changes in load
- Can scale to zero when no connections are active (cold start takes a few seconds)
- Can be used as the writer or as read replicas in an Aurora cluster
- Supports Multi-AZ and read replicas like standard Aurora

Best use cases: development and test databases, SaaS applications with variable workloads, intermittently used applications, new applications where sizing is uncertain.

### 5.2 Aurora Global Database

Aurora Global Database spans up to 6 Regions. One primary Region with a full Aurora cluster; up to 5 secondary Regions with read-only replicas. Cross-region replication uses dedicated replication infrastructure — typically sub-1-second lag.

Disaster recovery:

- If primary Region fails, promote a secondary Region to primary
- RTO: under 1 minute for planned promotion; slightly longer for unplanned
- RPO: typically under 5 seconds (replication lag)

Read scaling:

- Route read queries to the nearest secondary Region for lower latency global users
- Secondary Regions support up to 16 read-only Aurora Replicas each

---

## Section 6: RDS Proxy

RDS Proxy sits between your application and the RDS or Aurora database. It maintains a pool of database connections and multiplexes many application connections over a smaller number of database connections. Key benefits:

- Reduces connection overhead for serverless applications (Lambda functions that open many short-lived connections)
- Handles failover transparently — application connects to the proxy endpoint; the proxy reconnects to the new primary after failover
- Enforces IAM and Secrets Manager-based authentication
- Reduces max connections pressure on the database during traffic spikes

For the SAA-C03 exam: if a scenario mentions Lambda functions connecting to RDS and causing connection exhaustion or pool errors, RDS Proxy is the solution.

---

## Section 7: SAA-C03 Exam Tips for Module 06

**Exam Tip 1 — Multi-AZ is HA, not read scaling:**
The standby in a Multi-AZ deployment cannot serve read traffic. If a question says "reduce read load on the primary" or "scale read throughput," the answer is Read Replicas, not Multi-AZ.

**Exam Tip 2 — Read Replica replication is asynchronous:**
Read Replicas have replication lag. If the application requires guaranteed up-to-date data for reads, the query must go to the primary. Use Read Replicas only for eventually consistent read workloads.

**Exam Tip 3 — Aurora failover is faster than RDS Multi-AZ:**
Aurora Replica failover takes approximately 30 seconds because the new primary takes over the shared storage immediately. Standard RDS Multi-AZ failover takes 60-120 seconds because the standby must complete the transition.

**Exam Tip 4 — Encrypting an existing unencrypted RDS instance:**
You cannot enable encryption on a running unencrypted RDS instance directly. The process is: create a snapshot, copy the snapshot with encryption, restore from the encrypted snapshot, update application connection strings. Know this three-step process.

**Exam Tip 5 — Aurora Serverless for variable workloads:**
When a scenario describes highly variable, unpredictable, or intermittent database usage, Aurora Serverless v2 is the answer. It is not appropriate for steady-state, high-throughput workloads where provisioned Aurora offers better performance per dollar.

**Exam Tip 6 — RDS Proxy for Lambda connections:**
Lambda functions create new connections on every invocation. Without connection pooling, this exhausts RDS's maximum connections. RDS Proxy pools connections and is the SAA-C03-recommended solution for Lambda-to-RDS connectivity.

**Exam Tip 7 — Aurora Global Database for cross-region DR:**
If a scenario mentions a Recovery Time Objective under 1 minute for a regional failure or requires global low-latency reads, Aurora Global Database is the answer. Standard RDS cross-region Read Replicas have higher promotion times and are not appropriate for sub-minute RTO requirements.

**Exam Tip 8 — DB Subnet Group requirement:**
RDS instances must be deployed in a DB Subnet Group — a collection of subnets in at least two AZs. Even if you are not using Multi-AZ, you must create a DB Subnet Group with subnets in at least two AZs.

---

## Section 8: Key CLI Commands for Module 06

Describe RDS DB instances:

```bash
aws rds describe-db-instances \
  --query "DBInstances[*].{ID:DBInstanceIdentifier,Engine:Engine,Class:DBInstanceClass,MultiAZ:MultiAZ,Status:DBInstanceStatus}" \
  --output table
```

Describe DB snapshots:

```bash
aws rds describe-db-snapshots \
  --query "DBSnapshots[*].{ID:DBSnapshotIdentifier,Status:Status,Created:SnapshotCreateTime}" \
  --output table
```

Describe Aurora clusters:

```bash
aws rds describe-db-clusters \
  --query "DBClusters[*].{ID:DBClusterIdentifier,Engine:Engine,Status:Status,MultiAZ:MultiAZ}" \
  --output table
```

Create a manual DB snapshot:

```bash
aws rds create-db-snapshot \
  --db-instance-identifier mydb \
  --db-snapshot-identifier mydb-snapshot-manual-$(date +%Y%m%d)
```

---

## Section 9: Study Checklist

- [ ] Name all six RDS engines and their primary use case from memory
- [ ] Explain the difference between Multi-AZ and Read Replicas on replication type, reads served, and failover behavior
- [ ] Describe Aurora's storage architecture and why it enables faster failover than standard RDS Multi-AZ
- [ ] Explain the three-step process to encrypt an existing unencrypted RDS instance
- [ ] Describe when to use Aurora Serverless v2 vs. provisioned Aurora
- [ ] Explain why RDS Proxy is recommended for Lambda-to-RDS connections
- [ ] Identify the Aurora endpoint types (cluster, reader, instance) and when to use each
- [ ] Run the CLI commands in Section 8 and record the output
- [ ] Complete the Module 06 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 06 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: aws.amazon.com/certification

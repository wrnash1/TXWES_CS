# Reading Guide: Module 07 — MySQL and Cloud SQL

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

## Overview

This reading guide accompanies the Module 07 video lectures and lab. MySQL is one of the most widely deployed databases in the world and is a primary engine option on Cloud SQL. This guide reinforces InnoDB internals, MySQL user management, and all Cloud SQL configuration concepts tested on the Google Cloud Professional Database Engineer exam.

---

## Section 1 — MySQL Architecture Recap

### 1.1 Layer Summary

| Layer | Components | Key Responsibility |
|---|---|---|
| Connection Layer | Thread manager, thread cache, authentication | Accept and authenticate client connections |
| SQL Layer | Parser, optimizer, execution engine | Parse, optimize, and execute SQL |
| Storage Engine Layer | InnoDB, MyISAM, Memory, etc. | Physical read/write, locking, transactions |

The storage engine abstraction is MySQL's defining architectural feature. The SQL layer passes data operations to whichever engine manages a given table.

### 1.2 Thread Cache

MySQL reuses idle threads via the thread cache (`thread_cache_size`). A value of 16–32 is appropriate for most workloads. Monitor `Threads_created` status variable — high values relative to `Connections` indicate the thread cache is too small:

```sql
SHOW GLOBAL STATUS LIKE 'Threads%';
SHOW GLOBAL STATUS LIKE 'Connections';
```

---

## Section 2 — InnoDB Deep Dive

### 2.1 Buffer Pool

The InnoDB buffer pool is the most performance-critical memory structure. It caches:

- Data pages (16 KB default page size)
- Index pages
- Change buffer pages
- Adaptive hash index entries

Target: `innodb_buffer_pool_size` = 70–80% of dedicated server RAM.

For buffer pools larger than 1 GB, increase `innodb_buffer_pool_instances` (one per GB, up to 8) to reduce contention on the pool mutex.

Monitor buffer pool efficiency:

```sql
SHOW GLOBAL STATUS LIKE 'Innodb_buffer_pool%';
-- Key metric: Innodb_buffer_pool_read_requests vs Innodb_buffer_pool_reads
-- Hit rate = (read_requests - reads) / read_requests * 100
-- Target: > 99%
```

### 2.2 Redo Log

The InnoDB redo log is a circular log stored in `ib_logfile0` and `ib_logfile1`. Changes are written here before being applied to data pages. During crash recovery, InnoDB replays the redo log to bring the data files to a consistent state.

`innodb_log_file_size` controls the size of each redo log file. Larger redo logs mean fewer checkpoints and better write throughput but slower crash recovery. A starting value of 1–2 GB per file is common for busy OLTP systems.

In MySQL 8.0.30+, redo log files are managed dynamically (`innodb_redo_log_capacity`) rather than static file pairs.

### 2.3 Doublewrite Buffer

Before InnoDB writes a page to its final location, it first writes the page to the doublewrite buffer (a sequential write). If a crash occurs mid-page-write (a partial page write), InnoDB can recover the page from the doublewrite buffer. This protects against torn page corruption on systems without atomic 16 KB writes.

On filesystems and hardware that guarantee atomic writes (like AWS EBS with ext4+FUA, or certain NVMe configurations), the doublewrite buffer can be disabled (`innodb_doublewrite = OFF`) for performance. On Cloud SQL, Google handles this at the infrastructure layer.

### 2.4 Change Buffer

The change buffer reduces I/O by batching writes to secondary index pages. When a row is inserted, updated, or deleted, the change to a non-unique secondary index that is not currently in the buffer pool is buffered in the change buffer and merged lazily. This avoids random I/O for each secondary index update.

### 2.5 MVCC and Undo Logs

InnoDB maintains undo log records for each changed row. Active transactions read old row versions from the undo log, ensuring consistent reads. Long-running transactions accumulate large undo logs, which can cause performance degradation — always commit or roll back transactions promptly.

Monitor undo log history length:

```sql
SELECT count FROM information_schema.INNODB_METRICS
WHERE name = 'trx_rseg_history_len';
```

Values above 10,000 indicate long-running uncommitted transactions. Values above 1,000,000 are a serious problem.

---

## Section 3 — MySQL vs. MyISAM Decision Matrix

| Feature | InnoDB | MyISAM |
|---|---|---|
| Transactions | Full ACID | None |
| Locking | Row-level | Table-level |
| Foreign keys | Enforced | Not supported |
| Crash recovery | Automatic (redo log) | Manual repair required |
| Full-text search | Yes (since 5.6) | Yes |
| MVCC | Yes | No |
| Cloud SQL support | Yes | No |
| Recommended for | All production tables | Not recommended |

---

## Section 4 — MySQL User and Privilege Management

### 4.1 User Account Identity

MySQL accounts are `'user'@'host'` pairs. These are completely distinct accounts:

- `'alice'@'localhost'` — Alice connecting from the local machine
- `'alice'@'%'` — Alice connecting from any host
- `'alice'@'10.0.1.0/255.255.255.0'` — Alice from a specific subnet

### 4.2 Authentication Plugins

| Plugin | MySQL Default | Cloud SQL Default | Security |
|---|---|---|---|
| `caching_sha2_password` | 8.0+ | No | Strong |
| `mysql_native_password` | 5.7 | Yes | Moderate |
| `sha256_password` | Optional | No | Strong |

Cloud SQL retains `mysql_native_password` as the default for broad client compatibility. The exam may test this difference.

### 4.3 Privilege Levels

```sql
-- Show current user's privileges
SHOW GRANTS FOR CURRENT_USER();

-- Show another user's privileges
SHOW GRANTS FOR 'appuser'@'10.0.1.5';

-- Revoke specific privilege
REVOKE INSERT ON myapp.orders FROM 'appuser'@'10.0.1.5';

-- Drop user entirely
DROP USER 'olduser'@'%';
```

### 4.4 MySQL 8.0 Roles

```sql
-- Mandatory roles (applied automatically at login)
SET PERSIST mandatory_roles = 'app_read';

-- View active roles in session
SELECT CURRENT_ROLE();
```

---

## Section 5 — Cloud SQL for MySQL Configuration

### 5.1 Instance Tiers

| Tier | vCPUs | RAM | Use Case |
|---|---|---|---|
| db-f1-micro | shared | 0.6 GB | Development only |
| db-g1-small | shared | 1.7 GB | Light dev/test |
| db-n1-standard-2 | 2 | 7.5 GB | Small production |
| db-n1-standard-8 | 8 | 30 GB | Medium production |
| db-n1-highmem-32 | 32 | 208 GB | Large OLTP |

### 5.2 Important Database Flags for Cloud SQL MySQL

| Flag | Recommended Value | Notes |
|---|---|---|
| `innodb_buffer_pool_size` | 70-75% of RAM (bytes) | Most impactful performance flag |
| `max_connections` | 200–500 | Balance with available RAM |
| `slow_query_log` | ON | Enable in production |
| `long_query_time` | 1 | Log queries taking > 1 second |
| `log_queries_not_using_indexes` | ON | Identify full table scans |
| `character_set_server` | utf8mb4 | Support full Unicode including emoji |
| `collation_server` | utf8mb4_unicode_ci | Case-insensitive Unicode collation |

### 5.3 Backup Configuration

Cloud SQL for MySQL automated backups use `mysqldump` for the initial export and binary log positions for PITR. Backups are stored in Google-managed Cloud Storage and retained for 7 days by default (configurable 1–365 days).

```bash
# Configure backup retention
gcloud sql instances patch my-mysql-ha \
  --backup-start-time=02:00 \
  --retained-backups-count=14 \
  --retained-transaction-log-days=7 \
  --project=my-gcp-project
```

---

## Section 6 — High Availability Architecture

### 6.1 HA with Regional Persistent Disk

Cloud SQL HA in the regional configuration uses Google's **regional persistent disk** technology. Both the primary and standby share the same underlying disk, replicated synchronously across two zones. This means:

- Failover is fast (no data replay needed)
- RPO (Recovery Point Objective) ≈ 0 — no data loss
- RTO (Recovery Time Objective) ≈ 60–120 seconds

### 6.2 HA vs. Read Replica Comparison

| Feature | HA Standby | Read Replica |
|---|---|---|
| Purpose | Failover resilience | Read scalability |
| Replication type | Synchronous | Asynchronous |
| Can serve reads? | No | Yes |
| Auto-promotes on failure? | Yes | No (manual) |
| Cross-region? | No (same region) | Yes |
| Additional cost | Yes (doubles instance cost) | Yes (separate instance) |

---

## Section 7 — Cloud SQL Auth Proxy Deep Dive

### 7.1 Security Model

The Auth Proxy eliminates three common security risks:

1. **No need to whitelist application server IPs** — the proxy authenticates via IAM, not network location.
2. **No need to manage SSL certificates manually** — the proxy handles TLS encryption automatically.
3. **Short-lived credentials** — IAM tokens expire and rotate automatically.

### 7.2 Connection Name Format

```text
PROJECT_ID:REGION:INSTANCE_NAME
```

Example: `my-company-prod:us-central1:mysql-primary`

### 7.3 Private IP Architecture (Production Recommended)

```text
VPC Network
├── App Server (10.0.1.5)    ─────────────────────────────┐
│                                                           │
├── Cloud SQL Private IP (10.1.0.3)  ◄────── Private Service Access
│   (no public IP)
└── Cloud NAT (for outbound only)
```

Private IP requires configuring Private Service Access (VPC peering to the `servicenetworking.googleapis.com` network) before creating the Cloud SQL instance.

---

## Section 8 — Key Terms

| Term | Definition |
|---|---|
| InnoDB | MySQL's default transactional storage engine |
| Buffer pool | InnoDB's in-memory page cache |
| Redo log | InnoDB's crash recovery log (analogous to PostgreSQL WAL) |
| MVCC | Multi-Version Concurrency Control in InnoDB |
| Doublewrite buffer | Protects against partial page write corruption |
| Cloud SQL HA | Regional standby with automatic failover |
| Read replica | Async replication target for read offloading |
| Cloud SQL Auth Proxy | IAM-authenticated encrypted tunnel to Cloud SQL |
| Binary log | MySQL replication and PITR log |
| ROW binlog format | Records full before/after row images; recommended for replication |

---

## Study Questions

1. Why is `innodb_flush_log_at_trx_commit = 2` faster than `= 1`? What is the risk?

2. Explain the difference between a Cloud SQL HA standby and a read replica in terms of replication type and automatic failover capability.

3. A MySQL account `'alice'@'%'` exists. A new account `'alice'@'localhost'` is created. Alice connects from localhost — which account is used and why?

4. What is the role of the doublewrite buffer, and when might you safely disable it?

5. Why does Cloud SQL use `mysql_native_password` as the default authentication plugin instead of `caching_sha2_password`?

6. Describe the three security benefits of the Cloud SQL Auth Proxy over direct SSL connections with authorized networks.

---

## Certification Exam Checklist

Before the exam, confirm you can answer these:

- [ ] `innodb_buffer_pool_size` sizing rule for dedicated MySQL server
- [ ] Difference between HA standby and read replica (sync vs async, auto-failover)
- [ ] gcloud command to create a Cloud SQL MySQL instance with HA enabled
- [ ] Cloud SQL Auth Proxy connection name format and IAM role required
- [ ] Binary log requirement for PITR and replication
- [ ] MySQL user identity format: `'user'@'host'`
- [ ] `binlog_format = ROW` recommendation and why
- [ ] Private IP vs authorized networks tradeoffs

---

## 9. Supplemental Resources

**1. Cloud SQL for MySQL — Official Documentation**
https://cloud.google.com/sql/docs/mysql
Complete reference for Cloud SQL MySQL instance configuration, high availability, read replicas, binary log settings, and Auth Proxy setup.

**2. MySQL 8.0 Reference Manual — InnoDB Configuration**
https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html
Detailed descriptions of all InnoDB configuration variables including innodb_buffer_pool_size, innodb_flush_log_at_trx_commit, innodb_log_file_size, and the doublewrite buffer.

**3. Cloud SQL Query Insights — Documentation**
https://cloud.google.com/sql/docs/mysql/using-query-insights
Guide to using Cloud SQL's built-in Query Insights feature for identifying slow queries, visualizing query plans, and monitoring query performance on Cloud SQL for MySQL instances.

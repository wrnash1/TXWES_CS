# Video Script: Module 07 — MySQL and Cloud SQL (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Data Engineer / Database Engineer

---

## Introduction

Welcome back to CIS-4327. I am Professor Nash, and this is Module 07: MySQL and Cloud SQL.

MySQL is the world's most widely deployed open-source relational database. It powers countless web applications, and it is one of the two primary database engines available on Cloud SQL — the other being PostgreSQL, which we covered in Module 06. In Part 1 we focus on MySQL architecture, storage engines, and user management. In Part 2 we move to Cloud SQL configuration, high availability, read replicas, and the Cloud SQL Auth Proxy.

---

## Section 1 — MySQL Architecture

MySQL has a layered architecture. Understanding the layers helps you make informed decisions about configuration and troubleshooting.

### The Connection Layer

At the top sits the connection layer. When a client connects to MySQL, the server authenticates the connection, establishes a session, and assigns a thread to that client. MySQL uses a **thread-per-connection** model — unlike PostgreSQL's process-per-connection model, MySQL spawns a thread rather than a full OS process per connection. Threads are lighter weight and share memory within the server process.

The **thread cache** (`thread_cache_size`) keeps idle threads alive for reuse rather than destroying them after a client disconnects. This reduces the overhead of thread creation for new connections.

### The SQL Layer

The SQL layer handles query parsing, optimization, and execution. Key components:

- **Parser** — tokenizes and validates SQL syntax.
- **Query optimizer** — generates and selects an execution plan using cost-based optimization.
- **Query cache** — deprecated as of MySQL 5.7 and removed in MySQL 8.0. Do not reference it in certification exam answers.
- **Stored procedure engine** — executes stored procedures, triggers, and events.

### The Storage Engine Layer

The storage engine is where MySQL's power and flexibility come from. Unlike most databases, MySQL separates the SQL processing layer from the storage layer. Different tables can use different storage engines within the same database. The storage engine handles how data is physically read from and written to disk.

The two most important storage engines are InnoDB and MyISAM.

---

## Section 2 — InnoDB: The Default Storage Engine

InnoDB has been the default MySQL storage engine since version 5.5 and is the only storage engine you should use for any table that requires transactions, foreign keys, or crash recovery.

### InnoDB Key Features

**ACID transactions** — InnoDB is fully ACID-compliant. Every INSERT, UPDATE, and DELETE is wrapped in a transaction, either explicitly or implicitly.

**Row-level locking** — InnoDB uses row-level locks for DML operations, not table-level locks. This allows high concurrency — multiple users can modify different rows of the same table simultaneously.

**MVCC (Multi-Version Concurrency Control)** — Similar to PostgreSQL, InnoDB keeps old row versions to support consistent reads without locking. Readers never block writers and writers never block readers.

**Foreign key enforcement** — InnoDB enforces referential integrity constraints. MyISAM does not.

**Crash recovery** — InnoDB uses its own redo log (similar to PostgreSQL's WAL) and the doublewrite buffer to guarantee that data is recoverable after a crash.

**Buffer pool** — The InnoDB buffer pool is InnoDB's in-memory page cache. It caches both data and index pages. This is the single most important memory structure in MySQL. Size it to `innodb_buffer_pool_size` — typically 70–80% of available RAM on a dedicated MySQL server.

### InnoDB File Structure

```
/var/lib/mysql/
├── ibdata1              ← shared tablespace (undo logs, data dictionary)
├── ib_logfile0          ← InnoDB redo log file 0
├── ib_logfile1          ← InnoDB redo log file 1
├── mysql/               ← system schema
└── mydb/
    ├── orders.ibd       ← per-table tablespace (innodb_file_per_table=ON)
    └── customers.ibd
```

`innodb_file_per_table = ON` (default since MySQL 5.6) stores each table's data and indexes in its own `.ibd` file. This makes it easy to reclaim space after large deletes and to move tables between tablespaces.

### InnoDB Configuration Parameters

The most important InnoDB parameters:

```ini
innodb_buffer_pool_size = 12G        # 75% of 16 GB RAM
innodb_buffer_pool_instances = 8     # One per GB, up to 8
innodb_log_file_size = 1G            # Larger = fewer checkpoints, faster writes
innodb_flush_log_at_trx_commit = 1   # 1=ACID durable, 2=fast but 1s data risk
innodb_flush_method = O_DIRECT       # Bypass OS cache, avoid double buffering
innodb_file_per_table = ON
```

`innodb_flush_log_at_trx_commit = 1` is the fully durable setting — every transaction commit flushes the redo log to disk. Setting it to `2` improves write performance but risks losing up to one second of transactions if the OS crashes. For Cloud SQL, Google manages flush settings and durability guarantees.

---

## Section 3 — MyISAM and When Not to Use It

MyISAM was MySQL's original default storage engine. You will see it referenced in legacy code and older documentation.

**MyISAM characteristics:**

- Table-level locking — only one writer at a time per table
- No transactions — changes cannot be rolled back
- No foreign key support
- No crash recovery — a crash can corrupt MyISAM tables
- Faster full-table reads for some read-only analytics workloads

**When is MyISAM appropriate?** Almost never in modern applications. The only valid remaining use case is read-only reference tables that are loaded via bulk import and never modified during runtime. For everything else, use InnoDB.

**Exam note:** Cloud SQL for MySQL only supports InnoDB. If a question describes a Cloud SQL scenario, the storage engine is InnoDB.

---

## Section 4 — MySQL User Management

MySQL user accounts are identified by both a username and a host — written as `'username'@'host'`. The same username from different hosts is treated as a completely separate account.

### Creating Users

```sql
-- User from a specific host
CREATE USER 'appuser'@'10.0.1.5' IDENTIFIED BY 'StrongPass2024!';

-- User from any host in a subnet (wildcard %)
CREATE USER 'reportuser'@'%' IDENTIFIED BY 'ReportPass2024!';

-- User from localhost only
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'AdminPass2024!';
```

The `%` wildcard matches any host. Limit it by subnet or IP in production.

### Authentication Plugins

MySQL 8.0 changed the default authentication plugin from `mysql_native_password` to `caching_sha2_password`. This is more secure but requires newer client drivers. Legacy drivers may not support it and require explicit downgrade:

```sql
CREATE USER 'legacy'@'%' IDENTIFIED WITH mysql_native_password BY 'LegacyPass!';
```

On Cloud SQL for MySQL, the default remains `mysql_native_password` for compatibility. Be aware of this difference.

---

## Section 5 — MySQL Privilege System

MySQL uses a multi-level privilege system evaluated in this order:

1. Global privileges (apply to all databases)
2. Database-level privileges
3. Table-level privileges
4. Column-level privileges

```sql
-- Global privileges
GRANT ALL PRIVILEGES ON *.* TO 'dba'@'localhost' WITH GRANT OPTION;

-- Database-level privileges
GRANT SELECT, INSERT, UPDATE, DELETE ON myapp.* TO 'appuser'@'10.0.1.5';

-- Table-level
GRANT SELECT ON myapp.products TO 'reportuser'@'%';

-- Column-level (most restrictive)
GRANT SELECT (product_id, product_name, price)
  ON myapp.products TO 'apiuser'@'%';

-- Flush to ensure changes take effect (required in older versions)
FLUSH PRIVILEGES;
```

In MySQL 8.0, `FLUSH PRIVILEGES` is only needed when you directly modify grant tables. DDL privilege statements (`GRANT`, `REVOKE`, `CREATE USER`) automatically flush.

### Roles in MySQL 8.0

MySQL 8.0 introduced roles, similar to PostgreSQL:

```sql
-- Create roles
CREATE ROLE 'app_read', 'app_write';

-- Grant privileges to roles
GRANT SELECT ON myapp.* TO 'app_read';
GRANT SELECT, INSERT, UPDATE, DELETE ON myapp.* TO 'app_write';

-- Assign roles to users
GRANT 'app_read' TO 'reportuser'@'%';
GRANT 'app_write' TO 'appuser'@'10.0.1.5';

-- Activate roles (users must activate roles or set mandatory roles)
SET DEFAULT ROLE ALL TO 'reportuser'@'%';
SET DEFAULT ROLE ALL TO 'appuser'@'10.0.1.5';
```

---

## Section 6 — MySQL System Variables and my.cnf

MySQL configuration lives in `my.cnf` (Linux) or `my.ini` (Windows). The key sections are `[mysqld]` for server options and `[client]` for client defaults.

```ini
[mysqld]
# Connection
max_connections = 150
thread_cache_size = 16

# InnoDB
innodb_buffer_pool_size = 12G
innodb_buffer_pool_instances = 8
innodb_log_file_size = 1G
innodb_flush_log_at_trx_commit = 1
innodb_flush_method = O_DIRECT

# Logging
slow_query_log = ON
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 1
log_queries_not_using_indexes = ON

# Binary log (required for replication)
log_bin = /var/log/mysql/mysql-bin
binlog_format = ROW
expire_logs_days = 7
server_id = 1
```

`binlog_format = ROW` is the recommended binary log format for replication. Row-based replication records the before and after image of each changed row, making it reliable across schema differences between primary and replica. Statement-based replication can produce divergent results with non-deterministic functions.

---

## Section 7 — Exam Summary for Part 1

Key points for the Google Cloud Database Engineer exam from Part 1:

- InnoDB is the only supported storage engine on Cloud SQL for MySQL
- `innodb_buffer_pool_size` should be 70–80% of dedicated server RAM
- `innodb_flush_log_at_trx_commit = 1` provides full ACID durability; value `2` sacrifices up to 1 second of commits for performance
- MySQL users are identified by `username@host` — the same username from different hosts is a different account
- MySQL 8.0 default authentication plugin is `caching_sha2_password`; Cloud SQL default is `mysql_native_password`
- `binlog_format = ROW` is required for reliable replication

---

## Closing

That is Part 1 of Module 07. You now understand MySQL's layered architecture, InnoDB's role as the production storage engine, user management, and the key configuration parameters.

In Part 2 we cover Cloud SQL for MySQL — creating instances, configuring high availability, adding read replicas, and using the Cloud SQL Auth Proxy to secure connections. See you there.

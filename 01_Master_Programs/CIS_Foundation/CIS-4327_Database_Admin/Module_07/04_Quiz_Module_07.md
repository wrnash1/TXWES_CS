# Quiz: Module 07 — MySQL and Cloud SQL

## Course: CIS-4327 Database Administration

**Certification Alignment:** Google Cloud Professional Database Engineer

---

Instructions: Select the single best answer for each question. Each question is worth 10 points.

---

### Question 1

Which InnoDB configuration parameter has the single greatest impact on MySQL read performance on a dedicated 32 GB database server?

- A) `innodb_log_file_size`
- B) `innodb_buffer_pool_size`
- C) `innodb_flush_method`
- D) `innodb_file_per_table`

**Answer: B** — The InnoDB buffer pool caches data and index pages in memory. Sizing it to 70–80% of RAM (approximately 22–25 GB on a 32 GB server) is the single most impactful performance tuning change for MySQL. The other options affect write performance or storage management, not read caching.

---

### Question 2

A Cloud SQL for MySQL instance is configured with `--availability-type=REGIONAL`. What does this provide?

- A) A read replica in a different region for disaster recovery
- B) A synchronous standby in a different zone within the same region with automatic failover
- C) An asynchronous read replica in the same region
- D) Cross-region replication with zero RPO

**Answer: B** — `REGIONAL` availability type deploys a hot standby using synchronous replication in a different zone within the same region. Failover is automatic. RPO is near zero and RTO is 60–120 seconds.

---

### Question 3

An application team asks for a MySQL read replica in a different region for disaster recovery. Which statement about cross-region read replicas is accurate?

- A) Cross-region replicas provide automatic failover if the primary region fails.
- B) Cross-region replicas use synchronous replication to ensure zero data loss.
- C) Cross-region replicas must be manually promoted and use asynchronous replication.
- D) Cross-region replicas are not supported on Cloud SQL.

**Answer: C** — Cloud SQL read replicas use asynchronous replication regardless of region. Promotion to primary requires a manual operation. They are supported across regions and serve as a DR strategy with a manual runbook.

---

### Question 4

MySQL accounts `'alice'@'localhost'` and `'alice'@'%'` both exist. Alice connects from the local machine. Which account is matched?

- A) `'alice'@'%'` because it is more permissive
- B) `'alice'@'localhost'` because MySQL matches the most specific host first
- C) Both accounts are merged
- D) MySQL returns an error for ambiguous accounts

**Answer: B** — MySQL evaluates account matches by host specificity: literal hostnames are more specific than wildcards. `localhost` takes precedence over `%` for local connections.

---

### Question 5

You are connecting an application running in GKE to a Cloud SQL for MySQL instance. Which connection method does Google recommend for GKE workloads?

- A) Add the GKE node pool IP range to Cloud SQL Authorized Networks
- B) Use Private IP with no proxy
- C) Run the Cloud SQL Auth Proxy as a sidecar container in the application pod
- D) Connect using SSL certificates downloaded from the Cloud Console

**Answer: C** — For GKE workloads, the recommended pattern is the Cloud SQL Auth Proxy sidecar container. It handles IAM authentication, TLS encryption, and connection routing without requiring static IP allowlisting or manual certificate management.

---

### Question 6

What binary log format is recommended for MySQL replication and why?

- A) STATEMENT — smallest log size, fastest replication
- B) MIXED — automatically switches between STATEMENT and ROW
- C) ROW — records full before/after row images ensuring replica consistency with non-deterministic functions
- D) COMPACT — a new MySQL 8.0 format optimized for Cloud SQL

**Answer: C** — ROW format records actual row values before and after each change. This ensures replicas produce identical results even when statements use non-deterministic functions like `NOW()` or `UUID()`. STATEMENT format can produce divergent replica data in these cases.

---

### Question 7

Which flag must be enabled to support point-in-time recovery on Cloud SQL for MySQL?

- A) `--enable-point-in-time-recovery`
- B) `--enable-bin-log`
- C) `--binlog-format=ROW`
- D) `--archive-logs=true`

**Answer: B** — PITR on Cloud SQL for MySQL requires the binary log (`--enable-bin-log`). The binary log records all changes, allowing Cloud SQL to replay them to a specific timestamp during a restore operation.

---

### Question 8

After a MySQL client library upgrade, the application receives: `Authentication plugin 'caching_sha2_password' cannot be loaded`. What is the most likely cause?

- A) The Cloud SQL instance needs to be restarted.
- B) The application is using an older MySQL client library that does not support `caching_sha2_password`.
- C) The user's password has expired.
- D) SSL is not configured correctly.

**Answer: B** — If a user account was created with `caching_sha2_password` (MySQL 8.0 default), older client libraries that only support `mysql_native_password` will fail to authenticate. The solution is to upgrade the client library or recreate the user specifying `mysql_native_password`.

---

### Question 9

You need to set `innodb_buffer_pool_size` to 4 GB using `gcloud sql instances patch`. What is the correct flag value?

- A) `innodb_buffer_pool_size=4G`
- B) `innodb_buffer_pool_size=4096`
- C) `innodb_buffer_pool_size=4294967296`
- D) `innodb_buffer_pool_size=4096MB`

**Answer: C** — Cloud SQL database flags require `innodb_buffer_pool_size` in bytes. 4 GB = 4 × 1024³ = 4,294,967,296 bytes. String suffixes such as `4G` or `4096MB` are not accepted.

---

### Question 10

After a Cloud SQL HA failover, what must the application do to reconnect to the new primary?

- A) Update the connection string with the new primary's IP address.
- B) Nothing — Cloud SQL updates DNS automatically so the connection name still resolves to the new primary.
- C) Reconnect using the standby's connection name.
- D) Wait 10 minutes for automatic failback to the original primary.

**Answer: B** — Cloud SQL updates the DNS record for the instance endpoint automatically during failover. Applications using the standard Cloud SQL connection name (not a hardcoded IP) reconnect to the new primary transparently after the failover window.

---

### Question 11 (5 points)

A Cloud SQL for MySQL 8.0 instance has `innodb_flush_log_at_trx_commit = 2`. Which statement accurately describes the durability trade-off of this setting compared to the default value of 1?

- A) Setting 2 flushes the log buffer to the OS cache on every commit but only syncs to disk once per second, meaning up to one second of committed transactions could be lost in an OS crash.
- B) Setting 2 is identical to setting 1 but reduces write amplification by batching log writes.
- C) Setting 2 disables the InnoDB redo log entirely, relying on the doublewrite buffer for crash recovery.
- D) Setting 2 flushes to disk every two seconds regardless of transaction commit frequency.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Settings 1 and 2 differ meaningfully in durability: setting 1 syncs to disk on every commit; setting 2 writes to the OS cache on every commit and syncs once per second — they are not identical.
  - C) Setting 2 does not disable the redo log; it changes the fsync frequency from per-commit to per-second; the redo log remains fully active.
  - D) The flush happens to the OS cache on every commit; the disk sync occurs approximately once per second, not every two seconds; the number 2 refers to the setting value, not a time interval.

---

### Question 12 (5 points)

A MySQL DBA runs `SHOW REPLICA STATUS\G` on a read replica and observes `Seconds_Behind_Source: 3600`. What does this indicate and what is the most likely cause?

- A) The replica is 3,600 seconds (one hour) behind the source; the replica's SQL thread cannot apply binary log events as fast as the source generates them, typically due to heavy write load or insufficient replica hardware.
- B) The replica has been disconnected from the source for 3,600 seconds and needs to be re-initialized.
- C) The replica's network connection to the source has a 3,600-millisecond round-trip latency.
- D) The replica is 3,600 transactions behind; each transaction takes approximately one second to apply.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `Seconds_Behind_Source` measures lag in the SQL thread (applying events), not disconnection time; a disconnected replica would show `NULL` for this field, not a numeric value.
  - C) `Seconds_Behind_Source` measures replication lag in seconds of applied event time, not network round-trip latency; network latency would affect the I/O thread, not this metric.
  - D) `Seconds_Behind_Source` is time-based (seconds of lag in event timestamps), not a transaction count; it cannot be interpreted as a number of transactions.

---

### Question 13 (5 points)

Which MySQL statement correctly grants a user `appuser@'%'` the ability to read all tables in the `inventory` database but prevents them from modifying data?

- A) `GRANT SELECT ON inventory.* TO 'appuser'@'%';`
- B) `GRANT READ ON inventory.* TO 'appuser'@'%';`
- C) `GRANT SELECT, SHOW DATABASES ON *.* TO 'appuser'@'%';`
- D) `GRANT USAGE ON inventory.* TO 'appuser'@'%';`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `READ` is not a valid MySQL privilege name; the correct privilege for query-only access is `SELECT`.
  - C) `GRANT SELECT ON *.*` would grant SELECT on all databases, not just the `inventory` database; scoping to a specific database requires the `database.*` syntax.
  - D) `USAGE` is MySQL's "no privileges" grant — it allows a user to connect and execute statements that require no special privileges, but it does not grant SELECT access to tables.

---

### Question 14 (5 points)

A Cloud SQL for MySQL instance is using 95% of its allocated storage and `storage_auto_increase` is disabled. The DBA wants to increase storage to 500 GB without losing data. Which approach is correct?

- A) Run `gcloud sql instances patch INSTANCE_NAME --storage-size=500GB` to increase storage on the running instance.
- B) Export the database to Cloud Storage, delete the instance, create a new 500 GB instance, and import.
- C) Increase the machine tier to a higher CPU configuration, which automatically increases storage proportionally.
- D) Storage cannot be changed on a running Cloud SQL instance; a maintenance window is required.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Exporting and recreating is a valid but unnecessarily disruptive approach; storage can be increased on a running instance with a single patch command.
  - C) Machine tier (CPU/RAM) and storage are independently configured in Cloud SQL; changing the machine tier does not affect storage allocation.
  - D) Storage increases on Cloud SQL are online operations that do not require a maintenance window or instance restart.

---

### Question 15 (5 points)

A MySQL table `orders` uses the default InnoDB storage engine and has no explicit primary key defined. How does InnoDB handle this?

- A) InnoDB internally generates a hidden 6-byte `ROW_ID` as the clustered index key since no primary key was defined.
- B) InnoDB uses the first NOT NULL UNIQUE column as the primary key if no PRIMARY KEY is defined.
- C) InnoDB refuses to create the table and returns an error if no PRIMARY KEY is specified.
- D) InnoDB creates the table as a heap (unordered) without any clustered index.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The hidden `ROW_ID` is used only as a last resort when no PRIMARY KEY and no NOT NULL UNIQUE column exists; it is the third fallback, not the first.
  - C) InnoDB does not refuse table creation without a PRIMARY KEY; it silently selects an alternative clustered index.
  - D) InnoDB always organizes data in a B-tree clustered index structure; there is no heap storage mode in InnoDB.

---

### Question 16 (5 points)

An application running in Cloud Run needs to connect to a Cloud SQL for MySQL instance using the Cloud SQL Auth Proxy. The Cloud Run service account is `run-sa@project.iam.gserviceaccount.com`. Which IAM role must be granted to this service account?

- A) `roles/cloudsql.client`
- B) `roles/cloudsql.admin`
- C) `roles/iam.serviceAccountUser`
- D) `roles/cloudsql.instanceUser`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `roles/cloudsql.admin` grants full administrative control over Cloud SQL instances including create, delete, and configure permissions; this is far more permissive than required for application connections.
  - C) `roles/iam.serviceAccountUser` allows acting as a service account (impersonation); it has no Cloud SQL connection permissions.
  - D) `roles/cloudsql.instanceUser` is a more granular role that grants IAM database authentication login rights; `roles/cloudsql.client` is the standard role required for Auth Proxy connections.

---

### Question 17 (5 points)

What is the purpose of the InnoDB doublewrite buffer?

- A) It prevents data corruption from partial page writes by writing each 16 KB page to the doublewrite buffer area before writing it to the actual table location on disk.
- B) It doubles write throughput by writing each transaction to two separate disk locations simultaneously.
- C) It maintains two copies of the redo log to ensure crash recovery survives a single log file corruption.
- D) It caches write operations in memory and flushes them in batches to reduce disk I/O frequency.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The doublewrite buffer does not increase write throughput; it adds a small overhead to protect against partial writes; the name refers to writing twice (buffer then destination), not writing to two locations for performance.
  - C) The doublewrite buffer protects data pages, not redo log files; redo log durability is handled by `innodb_flush_log_at_trx_commit`.
  - D) The doublewrite buffer is a crash-safety mechanism, not a write-batching cache; InnoDB's buffer pool handles write caching.

---

### Question 18 (5 points)

A DBA needs to identify the top 10 slowest queries on a Cloud SQL for MySQL instance over the past 24 hours. Which built-in MySQL feature provides this information after being enabled?

- A) The slow query log with `long_query_time` set to an appropriate threshold, analyzed with `mysqldumpslow` or the Cloud SQL Query Insights feature.
- B) The `INFORMATION_SCHEMA.PROCESSLIST` table, which stores historical query execution times.
- C) The binary log, which records all queries along with their execution durations.
- D) The InnoDB status output from `SHOW ENGINE INNODB STATUS`, which includes a list of the 10 slowest queries.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `INFORMATION_SCHEMA.PROCESSLIST` shows currently active connections and their current query; it does not store historical query execution times.
  - C) The binary log records data changes for replication and PITR purposes; it does not record query execution durations.
  - D) `SHOW ENGINE INNODB STATUS` shows current InnoDB internals (transactions, locks, buffer pool usage); it does not maintain a historical slow query list.

---

### Question 19 (5 points)

A MySQL DBA creates a user with `CREATE USER 'svc_account'@'%' IDENTIFIED WITH caching_sha2_password BY 'P@ssw0rd!';` An older Java application that uses the MySQL Connector/J 5.x fails to connect. What is the simplest fix that maintains security?

- A) Recreate the user specifying `IDENTIFIED WITH mysql_native_password BY 'P@ssw0rd!'` and update the MySQL Connector/J to version 8.x in the application.
- B) Change the Cloud SQL instance flag `default_authentication_plugin` to `caching_sha2_password`.
- C) Grant the user `SUPER` privileges so the auth plugin restriction is bypassed.
- D) Disable SSL on the Cloud SQL instance so the authentication plugin negotiation works with older clients.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) The instance flag `default_authentication_plugin` controls the default for new users; the existing `svc_account` user was already created with `caching_sha2_password`, so changing the default does not affect it.
  - C) `SUPER` privilege grants administrative capabilities; it has no effect on authentication plugin compatibility.
  - D) SSL configuration is independent of authentication plugin negotiation; disabling SSL would be a security regression and would not resolve the authentication plugin mismatch.

---

### Question 20 (5 points)

A Cloud SQL for MySQL instance receives a sudden spike of 800 concurrent connections from an application server pool. The `max_connections` flag is set to 500, and the remaining 300 connections above `nonsuper_reserved_connections` are reserved for superusers. What happens to the 300 excess connection attempts?

- A) They are rejected with "Too many connections" error; the application must implement connection pooling to stay within the limit.
- B) Cloud SQL automatically scales `max_connections` to accommodate the spike.
- C) The excess connections are queued and processed as existing connections close.
- D) Cloud SQL scales the instance machine type automatically to increase the connection limit.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud SQL does not automatically increase `max_connections`; it is a configured database flag that requires a manual patch and instance restart to change.
  - C) MySQL does not have a connection queue; connections that exceed `max_connections` are immediately rejected, not queued.
  - D) Cloud SQL does not auto-scale the machine type in response to connection spikes; instance scaling requires a manual configuration change.

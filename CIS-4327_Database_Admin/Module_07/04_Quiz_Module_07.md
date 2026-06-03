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

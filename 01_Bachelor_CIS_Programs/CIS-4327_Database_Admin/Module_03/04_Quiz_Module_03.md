# Quiz: Module 03 — Cloud SQL: MySQL and PostgreSQL on GCP

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis is provided to reinforce exam-level reasoning.

---

### Question 1

Your team is deploying a Python application on Google Kubernetes Engine that needs to connect to a Cloud SQL for PostgreSQL instance. The security team requires that no database passwords be stored in application environment variables. Which connection approach best meets this requirement?

- A) Use the Cloud SQL Auth Proxy with IAM database authentication via the GKE workload identity.
- B) Use a Public IP connection with an authorized networks entry for the GKE cluster IP range.
- C) Store the database password in a Kubernetes Secret and mount it as an environment variable.
- D) Use Private IP connectivity and hard-code the database password in a config file on the container image.

Correct Answer: A — The Cloud SQL Auth Proxy combined with IAM database authentication (using GKE Workload Identity) allows the application to authenticate to Cloud SQL using its GCP service account identity rather than a password. No password needs to be stored anywhere. This is the documented GCP best practice for Kubernetes-based applications connecting to Cloud SQL.

Distractor analysis: B is incorrect because Public IP with authorized networks still requires a database password; it only controls which source IPs can attempt a connection. C is incorrect because it uses a Kubernetes Secret to store a password — the password still exists in the cluster's secrets store, which violates the requirement. D is incorrect because hard-coding a password in a container image is a critical security vulnerability that violates credential management best practices.

---

### Question 2

A Cloud SQL for MySQL instance is running out of disk space and causing application errors. Automated storage auto-increase was not enabled. What is the fastest way to restore availability?

- A) Patch the instance to enable storage auto-increase; Cloud SQL will immediately allocate additional storage.
- B) Create a new larger instance, export data from the current instance, and import into the new instance.
- C) Delete the oldest backup files from the instance to free up storage space.
- D) Increase the machine type to a higher tier, which also increases available storage.

Correct Answer: A — Enabling storage auto-increase on a running Cloud SQL instance via `gcloud sql instances patch` triggers an immediate storage expansion. This is the fastest path to restoring availability without data migration or downtime. The storage increase is applied online.

Distractor analysis: B is incorrect as the fastest option; export and import is a multi-hour process depending on data volume and would extend the outage significantly. C is incorrect because backup files in Cloud SQL are managed by GCP and are stored in separate GCP-managed storage, not on the instance's own disk; deleting them does not free instance storage. D is incorrect because changing the machine tier does not increase storage; storage and machine type are independently configured.

---

### Question 3

A Cloud SQL for PostgreSQL production instance loses its primary zone due to an infrastructure failure. Approximately how long should the application team expect the database to be unavailable before automatic failover completes, assuming high availability is enabled?

- A) Approximately 60 seconds
- B) Approximately 5 minutes
- C) Less than 1 second (transparent, no interruption)
- D) The database does not recover automatically; manual promotion is required

Correct Answer: A — Cloud SQL HA automatic failover takes approximately 60 seconds. The standby instance in the secondary zone is promoted to primary and the DNS entry is updated. Applications must handle the brief connection interruption with retry logic.

Distractor analysis: B is incorrect because 5 minutes significantly overstates the failover duration for Cloud SQL HA. C is incorrect because Cloud SQL HA does have a brief outage during failover — sub-second transparent failover is a characteristic of Cloud Spanner, not Cloud SQL. D is incorrect because Cloud SQL HA failover is fully automatic when `--availability-type=REGIONAL` is configured; manual intervention is not required.

---

### Question 4

You need to restore a Cloud SQL for PostgreSQL database to its exact state at 3:14:27 PM yesterday after a developer accidentally executed `DELETE FROM orders WHERE 1=1;`. Point-in-time recovery is available. What must have been configured before this event for PITR to be possible?

- A) WAL archiving must have been enabled on the instance before the deletion occurred.
- B) A manual on-demand backup must have been triggered within 15 minutes before the deletion.
- C) The instance must have been running Cloud SQL Enterprise Plus edition.
- D) The database schema must have been exported to Cloud Storage before the deletion.

Correct Answer: A — Point-in-time recovery for PostgreSQL requires WAL (Write-Ahead Log) archiving to be enabled. WAL archiving continuously captures transaction log records that enable recovery to any point within the retention window. This must be enabled before the data loss event — you cannot retroactively enable PITR to recover past a point where logs were not being captured.

Distractor analysis: B is incorrect because a manual backup captures a point-in-time snapshot but does not enable recovery to an arbitrary second; without WAL logs, you can only restore to backup checkpoint times. C is incorrect because PITR is available on both Cloud SQL Enterprise and Enterprise Plus editions; edition tier does not determine PITR availability. D is incorrect because a schema export to Cloud Storage does not capture data; it would not allow row-level recovery.

---

### Question 5

Your organization requires that the Cloud SQL instance for a financial application never be reachable from the public internet. Which configuration achieves this?

- A) Configure the Cloud SQL instance with Private IP only, using Private Services Access on the application's VPC.
- B) Enable the Cloud SQL Auth Proxy on all connecting applications and disable all authorized networks entries.
- C) Set the instance firewall rules to block all inbound traffic from 0.0.0.0/0.
- D) Enable Cloud Armor on the Cloud SQL instance to filter incoming connection attempts.

Correct Answer: A — Configuring Cloud SQL with Private IP only and no public IP address means the instance has no internet-routable endpoint. It is only reachable through the VPC network using Private Services Access peering. This is the documented architecture for isolating Cloud SQL from the public internet.

Distractor analysis: B is incorrect because the Auth Proxy manages authentication and encryption but does not remove the public IP endpoint if one is assigned; the instance would still be reachable from the internet. C is incorrect because Cloud SQL instances are not directly configured with VPC firewall rules; instance-level network access is controlled through Private IP vs. Public IP configuration and authorized networks, not VPC firewall rules. D is incorrect because Cloud Armor is a DDoS protection and WAF service for HTTP(S) Load Balancers; it does not apply to Cloud SQL TCP connections.

---

### Question 6

An application runs batch analytics reports every evening that generate heavy read load on the production Cloud SQL instance. Application transaction response times degrade significantly during the report window. What is the most cost-effective solution?

- A) Create a read replica and direct reporting queries to the replica connection string.
- B) Upgrade the primary instance to a higher machine type with more CPU and RAM.
- C) Enable Cloud SQL Enterprise Plus edition to access the data cache feature.
- D) Export the data to BigQuery every evening and run reports there instead.

Correct Answer: A — A read replica offloads read-heavy reporting queries from the primary instance without requiring a primary instance upgrade. The replica is asynchronously updated and accepts read-only connections. Directing reporting queries to the replica connection string eliminates read contention on the primary.

Distractor analysis: B is incorrect because upgrading the primary machine type is more expensive than a replica and requires a restart, causing downtime. A replica can be added without touching the primary. C is incorrect because the data cache in Enterprise Plus improves in-memory performance for all queries but does not eliminate the I/O contention problem from analytics queries competing with transactional ones. D is incorrect because exporting to BigQuery every evening adds operational complexity and latency; it is the right solution for truly analytical workloads but is disproportionate for a nightly reporting window that can be addressed with a replica.

---

### Question 7

Which Cloud SQL storage configuration change requires creating a new instance rather than patching the existing one?

- A) Decreasing the storage allocation from 500 GB to 200 GB
- B) Increasing the storage allocation from 200 GB to 500 GB
- C) Switching from SSD to HDD storage type on a running instance
- D) Enabling storage auto-increase on a running instance

Correct Answer: A — Cloud SQL storage auto-increase is one-directional. Once storage is expanded, it cannot be reduced on the same instance. Decreasing storage requires creating a new smaller instance, exporting data from the current instance, and importing it into the new one.

Distractor analysis: B is incorrect because increasing storage can be done via `gcloud sql instances patch --storage-size`; no new instance is required. C is incorrect because switching storage type between SSD and HDD can be done by patching the instance, though it requires a restart. D is incorrect because enabling storage auto-increase is a patch operation on the existing instance and takes effect immediately.

---

### Question 8

A development team is testing a new feature on a copy of the production Cloud SQL database. They want an exact snapshot copy as quickly as possible without affecting the production instance. Which Cloud SQL feature is most appropriate?

- A) Clone the production instance using the Cloud SQL clone operation.
- B) Create a read replica and promote it to a standalone instance.
- C) Run `pg_dump` on the production instance and restore it to a new instance.
- D) Use Database Migration Service to copy the production schema to a new instance.

Correct Answer: A — Cloud SQL instance cloning creates an exact copy of the source instance at a specific point in time. The clone is created quickly without generating load on the source instance because it uses a copy-on-write snapshot of the underlying storage. It is the fastest way to get a development copy of a production database.

Distractor analysis: B is incorrect because creating and promoting a replica requires waiting for full replication synchronization and the promotion step; it is slower than cloning and also temporarily affects the replica count. C is incorrect because pg_dump generates a logical backup that must be fully transferred and restored, which is slow for large databases and generates read load on the production instance during the dump. D is incorrect because Database Migration Service is designed for heterogeneous migrations between different database engines or environments; it is not the appropriate tool for creating a quick development copy within the same project.

---

### Question 9

You need to compare Cloud SQL Enterprise and Cloud SQL Enterprise Plus to determine which edition meets a contractual SLA requirement of 99.99% uptime. Which statement is accurate?

- A) Cloud SQL Enterprise Plus provides a 99.99% SLA; Cloud SQL Enterprise provides 99.95% for HA instances.
- B) Both editions provide a 99.99% SLA when high availability is enabled.
- C) Cloud SQL Enterprise provides 99.99% SLA; Enterprise Plus is only relevant for performance, not availability.
- D) Neither edition provides a 99.99% SLA; Cloud Spanner is required for 99.999% availability.

Correct Answer: A — Cloud SQL Enterprise Plus provides a 99.99% SLA for HA instances along with near-zero downtime maintenance windows. Cloud SQL Enterprise provides 99.95% SLA for HA instances. For contractual requirements above 99.95%, Enterprise Plus is required.

Distractor analysis: B is incorrect because Enterprise edition offers 99.95%, not 99.99%, even with HA enabled. C is incorrect because Enterprise Plus provides both higher availability (99.99% SLA) and better I/O performance; it is not relevant only for performance. D is incorrect because Cloud SQL Enterprise Plus does achieve 99.99% SLA; Cloud Spanner provides 99.999% (five nines), which is a separate and higher tier.

---

### Question 10

An application connects to Cloud SQL using the Public IP method with an authorized networks entry of `203.0.113.0/24`. The security team audits the configuration and classifies it as a risk. Which two changes would reduce the attack surface while maintaining application connectivity?

- A) Switch to Private IP connectivity and replace the authorized networks entry with the VPC internal IP range.
- B) Remove the authorized networks entry and require all connections to use the Cloud SQL Auth Proxy with IAM authentication.
- C) Change the authorized networks entry from `/24` to `/32` to restrict to a single IP address.
- D) Enable SSL certificate verification for all connections to the Public IP endpoint.

Correct Answer: A — Switching to Private IP removes the public internet endpoint entirely, eliminating the exposure of the database to internet-based attacks. This is the most comprehensive reduction of attack surface. Option B is also a valid improvement but still leaves the public IP accessible to anyone who can attempt an IAM-authenticated connection.

Distractor analysis: The question asks for the changes that most reduce attack surface. A is the best single answer because Private IP eliminates the public endpoint entirely. B is a valid answer but technically the Auth Proxy still uses the public endpoint unless Private IP is also configured. C is incorrect because narrowing the authorized network to /32 reduces the allowed source IP range but does not remove the public endpoint. D is incorrect because SSL verification protects data in transit but does not reduce network-level attack surface; the endpoint remains publicly accessible.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A Cloud SQL for MySQL instance has `--availability-type=ZONAL`. A zone outage occurs. What happens to the database?

- A) The instance becomes unavailable until the zone recovers; no automatic failover occurs because HA is not enabled.
- B) Cloud SQL automatically fails over to a standby in another zone within approximately 60 seconds.
- C) The instance is automatically migrated to a new zone and resumes with no data loss.
- D) Cloud SQL activates a read replica in another zone and promotes it to primary automatically.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Automatic failover to a standby in another zone requires `--availability-type=REGIONAL` (HA enabled); ZONAL instances have no standby in a separate zone.
  - C) Automatic live migration to a new zone does not occur for ZONAL instances during a zone outage; the instance remains down until the zone recovers.
  - D) Read replicas are not automatically promoted during a primary failure; promotion requires a manual `gcloud sql instances promote-replica` command.

---

### Question 12 (5 points)

A DBA needs to apply a new database flag to a Cloud SQL for PostgreSQL instance. The gcloud command completes successfully, but the change does not take effect until the next maintenance window. What does this indicate about the flag that was changed?

- A) The flag requires a database restart to take effect and was not applied with `--database-flags` in a way that triggered an immediate restart.
- B) The flag is not supported on Cloud SQL PostgreSQL and was silently ignored.
- C) The instance is in a read replica configuration and flags propagate from primary to replica on a delay.
- D) The flag requires Cloud SQL Enterprise Plus edition which is not currently active on the instance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) If a flag were unsupported, the gcloud command would return an error, not succeed silently; all accepted flags are validated before applying.
  - C) Database flags are set per-instance, not propagated from primary to replica; replicas have their own flag configurations.
  - D) Most database flags are available on both Enterprise and Enterprise Plus editions; edition is not the reason a flag waits for a maintenance window.

---

### Question 13 (5 points)

Which command correctly creates a Cloud SQL for PostgreSQL read replica of an existing instance named `prod-pg-01` in the same region?

- A) `gcloud sql instances create prod-pg-replica --master-instance-name=prod-pg-01 --region=us-central1`
- B) `gcloud sql instances clone prod-pg-01 prod-pg-replica --point-in-time=now`
- C) `gcloud sql instances patch prod-pg-01 --replica-names=prod-pg-replica`
- D) `gcloud sql replicas create prod-pg-replica --source=prod-pg-01`

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `gcloud sql instances clone` creates a copy of the instance at a point in time; it produces an independent instance, not a continuously updated read replica.
  - C) `gcloud sql instances patch` modifies existing instance properties; there is no `--replica-names` flag to create new replicas via a patch command.
  - D) `gcloud sql replicas` is not a valid gcloud command group; read replicas are created using `gcloud sql instances create` with the `--master-instance-name` flag.

---

### Question 14 (5 points)

A Cloud SQL for PostgreSQL instance is using the `pg_audit` extension to log all DDL statements. The DBA notices the audit log volume is extremely high, causing excessive storage costs. Which change best reduces log volume while retaining DDL audit coverage?

- A) Set `pgaudit.log = 'ddl'` to log only DDL statements rather than all statement classes.
- B) Disable the `pg_audit` extension entirely and rely on Cloud Logging for query auditing.
- C) Switch the instance to Cloud SQL Enterprise Plus to get the built-in data cache that reduces log I/O.
- D) Increase the `log_min_duration_statement` threshold so only slow DDL statements are logged.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Disabling `pg_audit` removes DDL audit coverage entirely, which violates the requirement to retain it; the goal is to reduce volume while keeping DDL logging.
  - C) The data cache in Enterprise Plus reduces read I/O for query data, not log write volume; it has no effect on audit log generation rate.
  - D) `log_min_duration_statement` controls logging of slow queries based on execution time; it does not apply to `pg_audit` DDL logging, which logs all DDL regardless of duration.

---

### Question 15 (5 points)

An application uses a Cloud SQL for MySQL instance. After enabling SSL, some legacy application clients fail to connect with the error "SSL connection error." The DBA confirms SSL is required on the instance. What is the most likely cause?

- A) The legacy clients are not configured with the server's CA certificate and are failing the SSL handshake.
- B) The Cloud SQL instance does not support SSL for MySQL; only PostgreSQL supports SSL connections.
- C) The MySQL port 3306 is blocked by a VPC firewall rule that is not aware of SSL traffic.
- D) SSL requires the Cloud SQL Enterprise Plus edition which is not enabled on the instance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Cloud SQL for MySQL fully supports SSL/TLS connections; SSL is available and configurable on all Cloud SQL MySQL instances.
  - C) VPC firewall rules operate at the IP/port level; port 3306 is the same whether SSL is used or not; SSL does not require a separate port or firewall rule change.
  - D) SSL is available on both Enterprise and Enterprise Plus editions of Cloud SQL; edition tier does not determine SSL availability.

---

### Question 16 (5 points)

A DBA wants to verify that a Cloud SQL automated backup completed successfully and determine the backup's exact creation timestamp. Which method is correct?

- A) Run `gcloud sql backups list --instance=INSTANCE_NAME` and inspect the STATUS and END_TIME columns.
- B) Connect to the instance via Cloud Shell and query the `information_schema.BACKUP_STATUS` table.
- C) Navigate to Cloud Storage and list the contents of the automatic backup bucket for the instance.
- D) Check the Cloud SQL slow query log for entries tagged with BACKUP type.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) There is no `information_schema.BACKUP_STATUS` table in PostgreSQL or MySQL; backup metadata is managed by Cloud SQL and is only accessible via the Cloud SQL API or gcloud CLI.
  - C) Cloud SQL automated backups are stored in GCP-managed storage buckets that are not directly accessible to the user; there is no user-visible Cloud Storage bucket to browse.
  - D) The slow query log records slow SQL queries; backup operations are not recorded as SQL query log entries.

---

### Question 17 (5 points)

Your Cloud SQL for PostgreSQL instance is handling peak write load. You observe that `pg_stat_bgwriter` shows a very high `checkpoint_write_time` and frequent checkpoints. What is the most appropriate tuning action?

- A) Increase `max_wal_size` (or `checkpoint_segments` in older versions) to allow larger WAL accumulation between checkpoints, reducing checkpoint frequency.
- B) Decrease `checkpoint_completion_target` to make each checkpoint complete faster.
- C) Disable WAL archiving to reduce the I/O overhead of checkpoint operations.
- D) Add more read replicas to distribute the checkpoint write load across multiple instances.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) `checkpoint_completion_target` controls how much of the checkpoint interval is used for spreading writes; decreasing it concentrates writes into a shorter burst, which typically worsens I/O pressure, not reduces it.
  - C) Disabling WAL archiving removes the ability to perform point-in-time recovery; checkpoints are part of the core WAL management process and disabling archiving does not reduce checkpoint frequency.
  - D) Read replicas receive WAL from the primary but do not participate in the primary's checkpoint operations; adding replicas has no effect on primary checkpoint frequency or write time.

---

### Question 18 (5 points)

A developer reports that a query runs in 200ms on the development Cloud SQL instance but takes 8 seconds on the production instance with the same data volume. Both instances have identical schemas and indexes. What is the most likely cause?

- A) Table statistics are stale on the production instance, causing the query planner to choose an inefficient execution plan.
- B) The production instance has more concurrent connections that are blocking the query.
- C) The development instance uses a faster machine type than the production instance.
- D) The production instance has SSL enabled, adding encryption overhead to each query.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Lock blocking would show the query in a "waiting" state in `pg_stat_activity`; a 40x slowdown without waiting is more characteristic of a bad query plan than lock contention.
  - C) The question states both instances have identical data volume; if the dev instance had a faster machine type, it would typically be faster on all queries equally, not only some — and the scenario describes a single query performing poorly.
  - D) SSL adds minimal TLS handshake overhead (milliseconds) at connection establishment, not per-query execution time; it cannot account for a 40x difference in query execution time.

---

### Question 19 (5 points)

Which Cloud SQL feature allows an administrator to restore a deleted Cloud SQL instance within a limited window after deletion?

- A) Instance recovery using `gcloud sql instances restore` within the retention window before the instance data is purged.
- B) Restoring from the most recent automated backup to a new instance using `gcloud sql backups restore`.
- C) Recovering from a WAL archive by replaying transactions from the last full backup.
- D) Using Database Migration Service to recreate the instance from Cloud Logging audit records.

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) There is no `gcloud sql instances restore` command for recovering a deleted instance by name; once an instance is deleted, the instance object is gone and recovery proceeds through backup restore to a new instance.
  - C) WAL archive replay (PITR) requires a running Cloud SQL instance as the target; it cannot recreate a deleted instance from scratch without first creating a new instance.
  - D) Cloud Logging audit records capture API calls and SQL statements for audit purposes; they are not a backup medium and cannot be used to recreate a database through Database Migration Service.

---

### Question 20 (5 points)

A Cloud SQL for PostgreSQL instance has both a public IP and Private IP configured. The application connects via Private IP through Private Services Access. The security team discovers the public IP is still enabled. What is the correct remediation?

- A) Disable the public IP on the instance using `gcloud sql instances patch --no-assign-ip` to remove the internet-facing endpoint.
- B) Add an authorized networks entry of `0.0.0.0/0` with a deny rule to block all public connections.
- C) Enable Cloud SQL Auth Proxy on the public IP to add an authentication layer in front of it.
- D) Delete and recreate the instance with Private IP only, as public IP cannot be disabled on a running instance.

- **Correct Answer:** A
- **Distractor Analysis:**
  - B) Authorized networks in Cloud SQL only support allow-listed CIDR ranges; there is no deny rule mechanism; removing the public IP is the correct action, not adding an allow-all-then-deny entry.
  - C) The Auth Proxy adds authentication but does not remove the public endpoint; the IP address remains reachable on the network even when Auth Proxy is used.
  - D) Public IP can be disabled on a running instance using `gcloud sql instances patch --no-assign-ip` without deleting and recreating the instance; deletion is unnecessary.

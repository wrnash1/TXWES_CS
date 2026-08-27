# Quiz: Module 15 — Database Automation and Monitoring

## Course: CIS-4327 Database Administration

## Texas Wesleyan University — Professor Nash

## Google Cloud Professional Cloud Database Engineer Alignment

---

### Instructions

This quiz contains 10 questions. Each question is worth 10 points. Select the single best answer. Distractor analysis follows each question.

---

### Question 1

A Cloud SQL for PostgreSQL instance has `max_connections = 100`. The monitoring team wants an alert when active connections exceed 80% of capacity. Which Cloud Monitoring metric and threshold correctly implements this alerting policy?

- A) Metric: `database/cpu/utilization`; Threshold: 0.80
- B) Metric: `database/postgresql/num_backends`; Threshold: 80 (absolute count)
- C) Metric: `database/memory/utilization`; Threshold: 0.80
- D) Metric: `database/disk/utilization`; Threshold: 0.80

Correct Answer: B — `database/postgresql/num_backends` reports the current number of active database connections (backends). With `max_connections = 100`, setting the threshold at 80 represents exactly 80% of capacity. This metric is specific to PostgreSQL connections and is the correct one to alert on connection pool pressure.

Distractor analysis: A is incorrect because `database/cpu/utilization` measures CPU consumption as a fraction of available CPU, not connection count. High CPU does not necessarily correlate with high connection count, and 0.80 CPU utilization would not alert at 80% of connection capacity. C is incorrect because `database/memory/utilization` measures RAM usage, not connection count. D is incorrect because `database/disk/utilization` measures disk space consumption, not connections.

---

### Question 2

A DBA needs to understand which specific SQL queries are consuming the most CPU time on a Cloud SQL for PostgreSQL instance. Which GCP feature provides this query-level breakdown directly in the Cloud Console without requiring additional configuration or extensions?

- A) Cloud SQL Audit Logs in Cloud Logging — captures all executed SQL with resource consumption
- B) Cloud SQL Query Insights — continuously samples and aggregates database queries ranked by CPU time and latency
- C) Cloud Monitoring custom metrics with a pgaudit filter configuration
- D) BigQuery `INFORMATION_SCHEMA.JOBS_BY_PROJECT` — the GCP-standard query performance view

Correct Answer: B — Cloud SQL Query Insights is built into the Cloud SQL service. It automatically samples active queries, aggregates them by normalized query text, and ranks them by CPU time, execution count, average latency, and bytes processed — all viewable in the Cloud Console without modifying application code or enabling extensions.

Distractor analysis: A is incorrect because Cloud SQL Audit Logs record who executed what action (access events) but do not provide CPU consumption or latency breakdown per query pattern. C is incorrect because pgaudit logs SQL statements for audit purposes and Cloud Monitoring custom metrics require manual configuration; this approach is significantly more complex than Query Insights and does not provide the same aggregated performance view. D is incorrect because `INFORMATION_SCHEMA.JOBS_BY_PROJECT` is a BigQuery-specific system view for BigQuery job analysis, not a Cloud SQL feature.

---

### Question 3

A production Terraform configuration for a Cloud SQL instance does not include `deletion_protection = true`. A junior engineer accidentally runs `terraform destroy` against the production environment. What is the result?

- A) Terraform warns but does not destroy the instance because Cloud SQL has built-in protection against accidental deletion
- B) Terraform destroys the instance, deleting all databases and data permanently
- C) Terraform creates an automated backup before destroying the instance as a safety measure
- D) The GCP console blocks the destroy operation because the instance has active connections

Correct Answer: B — Without `deletion_protection = true` in the Terraform resource definition (or equivalently without `--deletion-protection` set on the Cloud SQL instance), `terraform destroy` submits the delete API call to Cloud SQL and the instance is permanently deleted along with all its databases, data, and backups. There is no automatic safety net.

Distractor analysis: A is incorrect because Cloud SQL does not have built-in protection against Terraform-initiated deletes. Cloud SQL's `deletion-protection` flag must be explicitly enabled. Without it, the instance is deleted when Terraform destroys it. C is incorrect because Terraform does not automatically create backups before destructive operations. On-demand backup creation would require a separate Terraform resource or manual intervention. D is incorrect because active connections do not prevent Cloud SQL instance deletion via the API or Terraform.

---

### Question 4

A DBA needs to prevent Cloud SQL automatic maintenance from occurring during the company's peak sales period from December 20 through January 5. Which Cloud SQL feature accomplishes this?

- A) Configure the maintenance window to a 1-hour daily window during this period to limit disruption
- B) Create a deny maintenance period covering December 20 to January 5, which blocks all maintenance during that range
- C) Pause the Cloud SQL instance for the duration of the peak period
- D) Disable automatic backups during the period, which also suppresses maintenance operations

Correct Answer: B — Cloud SQL supports deny maintenance periods — configurable date ranges during which Cloud SQL will not perform any maintenance operations (version updates, patches). Any pending maintenance is deferred until after the deny period ends.

Distractor analysis: A is incorrect because a maintenance window specifies when maintenance can occur, not when it cannot. Setting a 1-hour window still allows maintenance to run during peak season. C is incorrect because Cloud SQL instances cannot be "paused" — they are running or stopped, and stopping an instance makes it unavailable to the application, which defeats the purpose. D is incorrect because disabling automated backups does not suppress maintenance operations; backups and maintenance are independent features with separate configuration.

---

### Question 5

A Cloud SQL HA Regional instance failover is triggered. How long does the application typically need to wait before successfully reconnecting to the new primary?

- A) 0–5 seconds — Cloud SQL uses a virtual IP that switches instantaneously
- B) 30–120 seconds — the standby is promoted and the connection endpoint DNS is updated
- C) 5–15 minutes — data must be fully synchronized from the primary to the standby before promotion can occur
- D) No wait is required — the application needs only to retry the connection once and it immediately succeeds

Correct Answer: B — Cloud SQL HA failover typically takes 30–120 seconds from the time of failover trigger to when the new primary (former standby) is accepting connections. This includes time for standby promotion, connection endpoint update, and the TCP reset that causes clients to drop and retry connections.

Distractor analysis: A is incorrect because Cloud SQL HA does not use a virtual IP (VIP) with sub-second failover. The failover involves actual standby promotion and DNS update, which takes tens of seconds. C is incorrect because Cloud SQL HA uses synchronous replication — the standby is always current. No data synchronization is needed before promotion because the standby already has all committed data. D is incorrect because the application must wait for the failover process to complete (30–120 seconds) before connections succeed. A single immediate retry will fail if issued during the failover window.

---

### Question 6

Which Terraform resource configuration block prevents a Cloud SQL instance from being destroyed, causing `terraform destroy` and any `terraform apply` that would delete the resource to produce an error?

- A) `depends_on = [google_project_service.sql_api]`
- B) `lifecycle { prevent_destroy = true }`
- C) `deletion_protection = false` inside the resource settings block
- D) `lifecycle { ignore_changes = [all] }` inside the resource block

Correct Answer: B — The `lifecycle { prevent_destroy = true }` meta-argument in a Terraform resource block causes Terraform to return an error if any plan would destroy that resource. This applies to both explicit `terraform destroy` and `terraform apply` operations that would delete the resource as a side effect.

Distractor analysis: A is incorrect because `depends_on` establishes an ordering dependency between resources but does not prevent destruction. C is incorrect because `deletion_protection = false` is the Cloud SQL resource argument that explicitly allows deletion; setting it to `false` means deletion is permitted. The correct Terraform protection is `lifecycle { prevent_destroy = true }`. D is incorrect because `ignore_changes = [all]` instructs Terraform to ignore any configuration drift for the resource (not update it when changes are detected), but it does not prevent the resource from being deleted.

---

### Question 7

A data engineering team stores their Terraform state in a local file on each developer's laptop. A developer's laptop is stolen. What is the primary operational risk to the Terraform-managed infrastructure?

- A) Terraform cannot manage, update, or destroy the GCP resources that were in the stolen state file without state recovery
- B) Local state files are automatically synchronized to GCP; the state on the stolen laptop is just a cached copy
- C) Terraform will automatically rebuild the state from the actual GCP resources using `terraform refresh`
- D) Only the stolen developer's resources are affected; other developers' Terraform state files are independent and unaffected

Correct Answer: A — Terraform state records the mapping between Terraform resource definitions and actual GCP resource IDs. Without the state file, Terraform does not know that its configuration corresponds to existing GCP resources and will attempt to create new resources rather than modify the existing ones. State recovery requires importing existing resources with `terraform import`, which is time-consuming and error-prone.

Distractor analysis: B is incorrect because Terraform local state files are not automatically synced to GCP. Local state is a plain file on disk with no built-in sync mechanism. This is why remote state backends (Cloud Storage, Terraform Cloud) are recommended for teams. C is incorrect because `terraform refresh` reads current GCP resource attributes into the existing state file but cannot rebuild a state file from scratch if the file is missing — it requires an existing state to update. D is incorrect because team infrastructure typically shares a single state file or uses a remote backend. If the stolen laptop had the only copy of shared state, the entire team's infrastructure management is compromised.

---

### Question 8

A Cloud Monitoring alerting policy is configured for Cloud SQL CPU utilization with a threshold of 80% and an alert duration of 5 minutes (meaning the condition must be true for 5 continuous minutes to fire). The CPU spikes to 95% for 3 minutes and then drops to 40%. Does the alert fire?

- A) Yes — the CPU exceeded 80%, which triggers the alert immediately when the threshold is crossed
- B) No — the 5-minute sustained condition was not met because the CPU was only above 80% for 3 minutes
- C) Yes — any spike above 80% triggers an alert regardless of the duration setting
- D) No — 3 minutes of high CPU is within the normal operating range and Cloud Monitoring suppresses brief spikes

Correct Answer: B — Cloud Monitoring alerting policies with a duration condition (also called an alignment period condition) require the metric to continuously exceed the threshold for the full configured duration before the alert fires. A 3-minute spike that resolves before reaching the 5-minute requirement does not trigger the alert. This design prevents alert storms from transient spikes.

Distractor analysis: A is incorrect because the alert duration setting exists precisely to prevent immediate-fire behavior on threshold crossings. The policy is configured with a 5-minute duration requirement, so threshold crossings that last fewer than 5 minutes are suppressed. C is incorrect because the duration parameter explicitly overrides the "fire immediately on threshold crossing" behavior. D is incorrect because Cloud Monitoring does not have a built-in "normal operating range" concept for CPU — the suppression in this case is due to the 5-minute duration condition, not automatic spike filtering.

---

### Question 9

A database reliability engineer wants to create an alert when PostgreSQL lock wait events appear in Cloud SQL logs. Cloud Monitoring does not have a built-in metric for lock waits. Which feature creates an alertable metric from this log data?

- A) Cloud SQL Insights with lock event tracking enabled in the Query Insights configuration
- B) A log-based metric in Cloud Monitoring derived from Cloud Logging log entries that match the lock wait log pattern
- C) The pgaudit extension with `pgaudit.log_lock_waits = on` that publishes metrics automatically to Cloud Monitoring
- D) Cloud Trace with PostgreSQL span-level lock tracking enabled via the Cloud SQL flag

Correct Answer: B — Cloud Monitoring log-based metrics allow you to create a custom metric from any log entry pattern in Cloud Logging. By defining a filter that matches the PostgreSQL lock wait log pattern (e.g., `LOG: process acquired lock waits`), you create a metric that counts matching log entries over time. This metric can then be used in an alerting policy like any other Cloud Monitoring metric.

Distractor analysis: A is incorrect because Cloud SQL Query Insights does not have a separate lock event tracking feature; it focuses on query latency and CPU, not wait event monitoring at the lock level. C is incorrect because pgaudit logs SQL statements for audit purposes and does not publish custom metrics to Cloud Monitoring; a log-based metric is still required to convert log entries into alertable metrics. D is incorrect because Cloud Trace is used for distributed tracing of application requests, not for PostgreSQL lock event monitoring; it does not integrate with Cloud SQL lock waits.

---

### Question 10

After a Cloud SQL HA failover completes (75 seconds), the application takes an additional 3 minutes to successfully reconnect. The application uses HikariCP connection pooling. What is the most likely cause of the 3-minute gap?

- A) The new primary requires 3 minutes to load the database schema and buffer pool into memory before accepting queries
- B) HikariCP's connection pool holds stale connections from the old primary until the `connectionTimeout` or `keepaliveTime` period expires, causing reconnection retries to fail until the pool evicts dead connections
- C) Cloud SQL requires a 3-minute warm-up period after every HA failover before it accepts new connections
- D) The DNS TTL for the Cloud SQL private IP connection endpoint is 3 minutes by default

Correct Answer: B — After failover, connections in the HikariCP pool point to the old primary, which is no longer accepting connections. HikariCP does not immediately detect dead connections unless `keepaliveTime` and `connectionTestQuery` are configured. Stale connections are held in the pool and returned to the application, which then fails. The pool only evicts dead connections and reconnects after `connectionTimeout` or `keepaliveTime` fires, which can take minutes with default settings.

Distractor analysis: A is incorrect because Cloud SQL instances do not require a warm-up period for schema or buffer pool loading; the promoted standby is already running and ready to accept connections as soon as promotion completes (within the 75 seconds). C is incorrect because Cloud SQL has no built-in 3-minute post-failover warm-up requirement; the instance is ready immediately after promotion. D is incorrect because the Cloud SQL connection name resolves through Cloud SQL's proxy infrastructure, which updates the routing at promotion time; the application delay is in the connection pool behavior, not in DNS TTL.

---

Reference: cloud.google.com/learn

---

### Question 11 (5 points)

A Cloud SQL for PostgreSQL instance is running out of storage during peak hours due to large transaction logs and temporary files. The DBA wants Cloud SQL to automatically increase storage when usage reaches 90% without manual intervention. Which configuration achieves this?

A) Enable `automatic storage increase` on the Cloud SQL instance with a storage increase limit set to the maximum needed capacity.
B) Create a Cloud Monitoring alert on `database/disk/utilization > 0.90` that triggers a Cloud Function to resize the instance.
C) Set `max_wal_size` to a larger value in Cloud SQL flags to allow WAL to grow without triggering storage limits.
D) Enable scheduled snapshots to free up space before the 90% threshold is reached.

**Correct Answer:** A

**Distractor Analysis:**

- B) While a Cloud Function-triggered resize is technically possible, it is operationally complex and introduces automation lag; Cloud SQL's built-in automatic storage increase is the purpose-built, immediate solution.
- C) `max_wal_size` controls the maximum WAL size before a checkpoint is forced; it does not prevent total storage from filling up and does not automatically increase provisioned disk capacity.
- D) Scheduled snapshots back up data for recovery purposes; they do not free disk space on the running instance — they add snapshot storage, which is billed separately.

---

### Question 12 (5 points)

A DBA is reviewing a Cloud SQL for PostgreSQL `pg_stat_activity` query and sees many connections with `state = 'idle in transaction'` and `wait_event_type = 'Lock'`. What does this indicate and what is the most appropriate action?

A) The connections are waiting to acquire locks held by long-running open transactions; investigate and terminate the blocking transaction using `SELECT pg_terminate_backend(pid)`.
B) The connections are idle and waiting for new queries from the application; this is normal connection pool behavior.
C) The connections have exceeded `idle_in_transaction_session_timeout`; they will be terminated automatically in 30 seconds.
D) The connections are blocked by autovacuum holding an exclusive lock; pause autovacuum on the affected table.

**Correct Answer:** A

**Distractor Analysis:**

- B) `idle in transaction` is distinct from `idle` — `idle` means the session has no open transaction; `idle in transaction` means the session is inside an explicit transaction that has not committed or rolled back, which is a concerning state for locks.
- C) `idle_in_transaction_session_timeout` will terminate such sessions if configured with a non-zero value, but this does not indicate the connections will resolve on their own in 30 seconds — the default is 0 (disabled), meaning they persist indefinitely.
- D) Autovacuum holds only `ShareUpdateExclusiveLock`, which does not block regular DML; it is unlikely to be the cause of lock waits that show `Lock` wait events in `pg_stat_activity`.

---

### Question 13 (5 points)

A team uses Terraform to manage Cloud SQL instances. They need to rotate the `postgres` user password without downtime. Which Terraform approach correctly handles this?

A) Update the `password` attribute in the `google_sql_user` resource and run `terraform apply`; Cloud SQL updates the password without restarting the instance.
B) Destroy and recreate the `google_sql_user` resource with a new password using `terraform taint`.
C) Terraform cannot manage database user passwords; they must be rotated manually via `gcloud sql users set-password`.
D) Use `terraform refresh` to pull the current password from Cloud SQL into the state file before updating.

**Correct Answer:** A

**Distractor Analysis:**

- B) Destroying and recreating the user would drop the user and all associated grants, potentially causing an outage; `terraform apply` on a changed `password` attribute performs an in-place update without recreating the user.
- C) Terraform's `google_sql_user` resource does manage passwords; the `password` attribute is writable and applied via `terraform apply` without manual `gcloud` commands.
- D) `terraform refresh` reads current resource state from GCP into the state file but cannot read the current password (it is write-only and not returned by the API); refreshing before an apply is unnecessary for a password update.

---

### Question 14 (5 points)

A Cloud Monitoring dashboard shows that `database/postgresql/num_backends` has been at 98 out of `max_connections = 100` for the past 6 hours. The DBA adds `max_connections = 200` as a Cloud SQL flag. What happens immediately after applying this change?

A) The Cloud SQL instance restarts to apply the new `max_connections` value; new connections can reach 200 after the restart.
B) The `max_connections` change is applied live without a restart; 200 connections are immediately available.
C) The flag change is queued for the next maintenance window and will not take effect until then.
D) Cloud SQL automatically rejects the change because `max_connections = 200` exceeds the instance's memory capacity.

**Correct Answer:** A

**Distractor Analysis:**

- B) `max_connections` is a PostgreSQL parameter that requires a server restart to take effect; it cannot be changed live. Cloud SQL applies the flag change and restarts the instance, which causes a brief connection interruption.
- C) Database flag changes in Cloud SQL take effect immediately (with a restart for parameters that require it), not at the next maintenance window; maintenance windows apply to scheduled software updates, not manual flag changes.
- D) Cloud SQL validates that `max_connections` is within the supported range for the instance tier but does not reject values below the tier maximum; 200 connections is well within limits for most instance tiers.

---

### Question 15 (5 points)

A Terraform `google_sql_database_instance` resource has `deletion_protection = true` set. A DBA attempts `terraform destroy`. What happens?

A) Terraform returns an error: the API rejects the delete request because `deletion_protection` is enabled at the Cloud SQL level.
B) Terraform succeeds but Cloud SQL marks the instance for deletion with a 7-day retention period.
C) Terraform's `lifecycle { prevent_destroy = true }` overrides the Cloud SQL deletion protection, but `deletion_protection = true` does not affect Terraform.
D) Terraform disables `deletion_protection` automatically before deleting the instance.

**Correct Answer:** A

**Distractor Analysis:**

- B) Cloud SQL does not have a 7-day deletion retention period (that is BigQuery time travel); `deletion_protection = true` causes the API call to be rejected immediately.
- C) `deletion_protection` in the Terraform resource maps to the Cloud SQL API flag; when set to `true`, any delete API call (including from Terraform) is rejected by the Cloud SQL API regardless of Terraform-level `lifecycle` settings.
- D) Terraform does not automatically modify `deletion_protection` before destruction; it submits the delete request, which is rejected by Cloud SQL. To destroy the instance, the DBA must first set `deletion_protection = false` and apply, then run `terraform destroy`.

---

### Question 16 (5 points)

A DBA wants to receive an alert when any Cloud SQL instance in a GCP project has been without a successful backup for more than 24 hours. Which Cloud Monitoring approach creates this alert?

A) Create a metric absence alert on `database/backup/last_successful_backup_time` that fires if the metric has not been reported for 24 hours.
B) Query `INFORMATION_SCHEMA.BACKUP_HISTORY` in Cloud SQL every hour and alert if the last backup is older than 24 hours.
C) Enable Admin Activity audit logs and filter for backup creation events; alert if no backup event appears in 24 hours.
D) Set a Cloud Scheduler job to verify backups via `gcloud sql backups list` every hour and publish a custom metric.

**Correct Answer:** A

**Distractor Analysis:**

- B) `INFORMATION_SCHEMA.BACKUP_HISTORY` is a SQL Server system table, not a Cloud SQL feature; Cloud SQL does not expose backup history through a SQL query interface.
- C) Admin Activity logs do capture backup events, but building a 24-hour absence alert from log events requires a log-based metric with an absence condition, which is more complex than using the built-in backup metric; Cloud Monitoring's native metric is the simpler and more reliable approach.
- D) While a Cloud Scheduler + custom metric approach works, it requires building and maintaining custom automation; the built-in Cloud Monitoring metric is available natively and requires no custom code.

---

### Question 17 (5 points)

A Terraform configuration manages a Cloud SQL instance. A developer manually adds a database flag directly in the Cloud Console (not via Terraform). What will happen the next time `terraform apply` is run?

A) Terraform detects the configuration drift and reverts the manually added flag to match the Terraform configuration.
B) Terraform imports the manual change into the state file and the flag becomes part of the managed configuration.
C) Terraform ignores the manual change because it was made outside Terraform's scope.
D) Terraform generates an error because the state and actual configuration are out of sync.

**Correct Answer:** A

**Distractor Analysis:**

- B) Terraform does not automatically import manual changes into the state file; `terraform import` is a manual command. On `terraform apply`, Terraform computes the diff between its state and the desired configuration and applies changes to reconcile them, which means reverting the manual flag.
- C) Terraform does not ignore drift unless `lifecycle { ignore_changes = [...] }` is specifically configured for the `database_flags` attribute; by default, all attributes are managed.
- D) State/configuration divergence does not cause an error in Terraform; it causes a plan showing changes to reconcile the drift, which is applied on `terraform apply`.

---

### Question 18 (5 points)

A Cloud SQL for PostgreSQL instance shows a `database/disk/utilization` metric of 0.95 (95%) in Cloud Monitoring. The DBA checks the database and confirms that data size is only 40% of provisioned storage. What is the most likely cause of the high disk utilization?

A) Write-Ahead Log (WAL) files and temporary files are consuming the remaining 55% of disk space, which is separate from data file size.
B) Cloud SQL is pre-allocating storage for future growth as part of automatic storage management.
C) The 40% data size is measured before compression; the actual uncompressed data is 95% of disk.
D) Cloud SQL read replicas are stored on the same disk as the primary, causing shared storage utilization.

**Correct Answer:** A

**Distractor Analysis:**

- B) Cloud SQL does not pre-allocate large chunks of storage; automatic storage increase only adds storage when usage is high, not in advance.
- C) PostgreSQL does not use transparent compression for heap storage; data stored in tables occupies its uncompressed size on disk.
- D) Cloud SQL read replicas are separate instances with their own storage; they do not share disk with the primary instance.

---

### Question 19 (5 points)

A team's Cloud Monitoring dashboard shows that a Cloud SQL for PostgreSQL instance's `database/replication/replica_lag` metric is steadily increasing over an 8-hour period, currently showing 3,200 seconds of lag. What is the most appropriate immediate action?

A) Scale up the read replica's machine type to increase its write throughput so it can apply WAL faster than the primary generates it.
B) Delete and recreate the read replica from scratch to reset the lag counter.
C) Increase `max_wal_senders` on the primary to allow more replication connections.
D) Promote the read replica to primary to stop the lag accumulation.

**Correct Answer:** A

**Distractor Analysis:**

- B) Deleting and recreating the replica recreates it from a fresh base backup, temporarily clearing the lag, but does not fix the root cause (insufficient replica compute); the lag will accumulate again if the replica tier is unchanged.
- C) `max_wal_senders` on Cloud SQL is a managed parameter; increasing it does not affect the replica's ability to apply WAL — the bottleneck is the replica's write throughput, not the number of sender connections.
- D) Promoting the read replica converts it to an independent primary, permanently severing it from the original primary's replication stream; this removes the replica entirely and does not resolve the lag issue.

---

### Question 20 (5 points)

A security engineer wants to ensure that all Terraform-managed Cloud SQL instances in a project have `backup_configuration.enabled = true`. Which Google Cloud service can automatically detect and alert on Cloud SQL instances that are not compliant with this requirement without modifying Terraform code?

A) Cloud Security Command Center with a custom finding for Cloud SQL backup configuration.
B) Cloud Asset Inventory with Organization Policy constraints that enforce backup configuration.
C) Security Health Analytics in Security Command Center, which includes a managed detector for Cloud SQL instances with backups disabled.
D) Cloud Armor, which enforces database configuration policies at the network layer.

**Correct Answer:** C

**Distractor Analysis:**

- A) Cloud Security Command Center supports custom findings but requires writing a custom integration; Security Health Analytics provides built-in managed detectors for common misconfigurations including disabled backups, without custom code.
- B) Organization Policy constraints control what configurations are allowed when resources are created or modified; they can enforce backup settings but do not audit existing resources that were created before the constraint was applied.
- D) Cloud Armor is a WAF and DDoS protection service for HTTP workloads; it has no capability to inspect or enforce Cloud SQL configuration settings.

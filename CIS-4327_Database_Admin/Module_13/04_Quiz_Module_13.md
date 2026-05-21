# Quiz: Module 13 - Monitoring with Cloud Monitoring and Logging
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

**Question 1**
A Cloud SQL for MySQL instance is approaching its maximum connection limit during peak hours, causing connection timeouts for users. You need to set up an automated alert that notifies the operations team when the connection count exceeds 90% of the maximum. Which GCP service and feature should you use?
A) Create a Cloud Monitoring alerting policy on the `cloudsql.googleapis.com/database/network/connections` metric with a threshold at 90% of the instance's maximum connections, configured with an email notification channel.
B) Enable Cloud SQL Data Access audit logs and create a log-based alert for connection events.
C) Configure a Cloud SQL flag to automatically send an email when the connection limit is reached.
D) Enable Cloud SQL Insights and set the "maximum connections" threshold in the Query Insights console.
*   **Correct Answer:** A) Create a Cloud Monitoring alerting policy on the `cloudsql.googleapis.com/database/network/connections` metric with a threshold at 90% of the instance's maximum connections, configured with an email notification channel.
*   **Distractor Analysis:**
    *   *Why A is correct:* Cloud Monitoring tracks the `network/connections` metric for Cloud SQL in real time. An alerting policy with a threshold condition on this metric and an email notification channel is the standard GCP approach for proactive connection exhaustion alerts.
    *   *Why B is incorrect:* Cloud Audit Data Access logs record which queries were run, not the number of concurrent connections. Log-based alerts on connection events are not the same as a real-time metric threshold on connection count.
    *   *Why C is incorrect:* Cloud SQL database flags control engine-level behavior (buffer sizes, timeout values, etc.); there is no built-in flag that sends email alerts. Alerting is handled by Cloud Monitoring.
    *   *Why D is incorrect:* Cloud SQL Query Insights is a performance analysis tool for identifying slow queries; it does not have a configuration option for connection count alerting.

---

---

**Question 2**
A compliance team requires that all administrative changes to Cloud SQL instances (such as creating users, modifying database flags, and deleting instances) be retained in immutable logs for 2 years. Cloud Logging's default retention is 30 days. Which configuration satisfies this requirement?
A) Enable Cloud SQL Data Access audit logs and set the log retention period to 2 years in the Cloud Logging settings.
B) Create a Cloud Logging log sink that exports `cloudaudit.googleapis.com/activity` log entries to a Cloud Storage bucket with a 2-year object lifecycle policy.
C) Enable CMEK on Cloud Logging to prevent log entries from being deleted before 2 years.
D) Configure Cloud SQL automated backups to include audit log files in each daily backup.
*   **Correct Answer:** B) Create a Cloud Logging log sink that exports `cloudaudit.googleapis.com/activity` log entries to a Cloud Storage bucket with a 2-year object lifecycle policy.
*   **Distractor Analysis:**
    *   *Why B is correct:* Admin Activity audit logs (`cloudaudit.googleapis.com/activity`) record all administrative changes. Exporting them to Cloud Storage via a log sink provides long-term, low-cost retention. Setting a Cloud Storage object lifecycle rule to retain objects for 730 days (2 years) before deletion satisfies the 2-year immutable retention requirement.
    *   *Why A is incorrect:* Data Access audit logs record data-plane operations (queries, reads, writes), not administrative changes. Also, Cloud Logging's maximum configurable retention for most log buckets is 3,650 days (10 years) in custom log buckets, but the default `_Default` bucket has a fixed 30-day retention that cannot be extended — a custom bucket or log sink is required.
    *   *Why C is incorrect:* CMEK encrypts log data at rest for confidentiality but does not prevent authorized users from deleting log entries or control retention duration.
    *   *Why D is incorrect:* Cloud SQL automated backups contain database data, not audit log files. Audit logs are managed by Cloud Logging independently of database backups.

---

---

**Question 3**
A database administrator needs to **query Cloud Logging to find all Cloud SQL slow query log entries from the past 24 hours that took longer than 5 seconds to execute**. Which Log Analytics or Logs Explorer query approach is most appropriate?
A) Use the Logs Explorer with a filter: `resource.type="cloudsql_database" AND textPayload:"Query_time: [5-9]" AND timestamp > "24h ago"`.
B) Run `EXPLAIN ANALYZE SELECT * FROM cloud_logging WHERE duration > 5` in the Cloud SQL Query Insights console.
C) Create a Cloud Monitoring alerting policy on the `query_duration_seconds` metric with a threshold of 5 seconds.
D) Run `SELECT * FROM cloudsql_logs WHERE query_time > 5 ORDER BY timestamp DESC` in BigQuery.
*   **Correct Answer:** A) Use the Logs Explorer with a filter: `resource.type="cloudsql_database" AND textPayload:"Query_time: [5-9]" AND timestamp > "24h ago"`.
*   **Distractor Analysis:**
    *   *Why A is correct:* The Cloud Logging Logs Explorer is the correct tool for querying log entries. Cloud SQL slow query logs appear as `textPayload` entries with `Query_time` in the MySQL slow query log format. Filtering by `resource.type="cloudsql_database"` scopes the search to Cloud SQL, and the timestamp filter limits results to the past 24 hours.
    *   *Why B is incorrect:* `EXPLAIN ANALYZE` is a PostgreSQL/MySQL command executed against a database engine; it does not query Cloud Logging. Cloud SQL Query Insights does not accept SQL queries against log data.
    *   *Why C is incorrect:* A Cloud Monitoring alerting policy monitors a numeric metric over time and triggers notifications; it does not provide a way to query or retrieve specific historical log entries.
    *   *Why D is incorrect:* Cloud Logging logs are not automatically available in BigQuery unless a log sink has been configured to export them there. Even then, the query syntax would need to match the actual BigQuery dataset and table structure created by the sink.

---

**Question 4**
A Cloud SQL for PostgreSQL instance's replication lag metric (`cloudsql.googleapis.com/database/replication/replica_lag`) has been steadily increasing over the past hour on a read replica. The primary instance CPU is at 30%. What is the most likely cause of the increasing lag?
A) The read replica does not have enough CPU or disk I/O capacity to apply incoming replication changes at the rate they are being generated on the primary.
B) The HA standby instance in the same region is competing with the read replica for replication bandwidth.
C) The replica's automated backups are running simultaneously with the replication stream, causing I/O contention.
D) The Cloud SQL primary instance's network connection to the replica has reached the maximum VPC bandwidth limit.
*   **Correct Answer:** A) The read replica does not have enough CPU or disk I/O capacity to apply incoming replication changes at the rate they are being generated on the primary.
*   **Distractor Analysis:**
    *   *Why A is correct:* Read replica lag increases when the replica cannot apply WAL changes (PostgreSQL) or binary log events (MySQL) as fast as the primary is generating them. This is typically caused by the replica having a smaller machine type than the primary, or the primary experiencing a burst of writes that temporarily exceeds the replica's apply throughput. The fix is to scale up the replica machine type or reduce write load on the primary.
    *   *Why B is incorrect:* Cloud SQL HA standby instances receive their own dedicated synchronous replication stream; they do not share bandwidth with read replicas.
    *   *Why C is incorrect:* Cloud SQL automated backups run on the secondary (standby) for HA instances, not on read replicas. Read replicas do not have automated backups that would compete with replication.
    *   *Why D is incorrect:* Cloud SQL replication uses Google's internal network, which has very high bandwidth. Replication bandwidth is typically not the bottleneck; replica apply throughput is.

---

**Question 5**
When monitoring a Cloud SQL database for security events, you need to mitigate the risk of **a malicious insider using a legitimate database account to exfiltrate data through a large SELECT query without triggering any alerts**. Which monitoring configuration best detects this behavior?
A) Enable Cloud SQL Data Access audit logs, create a log-based metric counting `DATA_READ` events per user per hour, and set a Cloud Monitoring alert on anomalously high read counts for any individual user.
B) Enable Cloud SQL Admin Activity audit logs, which automatically record all SELECT queries.
C) Configure Cloud SQL Query Insights to block queries that return more than 1,000 rows.
D) Set a Cloud Monitoring alert on the `cloudsql.googleapis.com/database/cpu/utilization` metric to detect large queries consuming high CPU.
*   **Correct Answer:** A) Enable Cloud SQL Data Access audit logs, create a log-based metric counting `DATA_READ` events per user per hour, and set a Cloud Monitoring alert on anomalously high read counts for any individual user.
*   **Distractor Analysis:**
    *   *Why A is correct:* Data Access audit logs (DATA_READ events) record each data retrieval operation along with the identity of the user. A log-based metric on DATA_READ events per user, combined with a Cloud Monitoring alert for anomalously high volumes, detects bulk data exfiltration attempts by identifying users reading significantly more data than their normal baseline.
    *   *Why B is incorrect:* Admin Activity audit logs record control-plane operations (creating instances, modifying users, changing flags) — not SQL data queries. SELECT statements do not appear in Admin Activity logs; they appear in Data Access logs, which must be separately enabled.
    *   *Why C is incorrect:* Cloud SQL Query Insights is a performance analysis tool; it does not have the capability to block query execution or enforce row count limits.
    *   *Why D is incorrect:* CPU utilization is an indirect signal — a large exfiltration query will increase CPU, but many legitimate operations also increase CPU. This approach generates false positives and does not identify the specific user or query performing the exfiltration.

# Reading Guide: Module 13 - Monitoring with Cloud Monitoring and Logging
## Course: CIS-4327_Database_Admin (4327_Database_Admin - Google Cloud Professional Cloud Database Engineer)

---

### Introduction
Welcome to **Module 13 - Monitoring with Cloud Monitoring and Logging**! This week focuses on observing the health, performance, and security of GCP database services using Google Cloud's native monitoring and logging stack: Cloud Monitoring, Cloud Logging, and Cloud Audit Logs. Proactive monitoring is essential for maintaining SLAs in production and is tested on the GCP Professional Cloud Database Engineer exam through operational scenario questions.

You will learn how to configure dashboards, set alerting policies, query logs, and use database-specific monitoring features (Cloud SQL Query Insights, Spanner CPU/storage metrics) to identify and resolve issues before they impact users.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Cloud Monitoring**: The GCP service for collecting, storing, and visualizing time-series metrics from GCP resources including Cloud SQL, Cloud Spanner, Bigtable, AlloyDB, and BigQuery. Cloud Monitoring provides pre-built dashboards for each database service and allows you to create custom dashboards and alerting policies based on any metric.
*   **Cloud Logging**: The GCP service for collecting, storing, and querying log data from GCP services. Database administrators use Cloud Logging to view Cloud SQL error logs, slow query logs, PostgreSQL log files, and application-generated logs. Logs can be exported to Cloud Storage, BigQuery, or Pub/Sub for long-term retention or analytics.
*   **Alerting Policy**: A Cloud Monitoring configuration that defines a condition (e.g., "Cloud SQL CPU utilization > 80% for 5 minutes"), a notification channel (email, PagerDuty, Slack), and an incident response. Alerting policies are the primary mechanism for proactive detection of database performance and availability issues.
*   **Cloud SQL Metrics**: Key Cloud SQL metrics to know for the exam include: `cloudsql.googleapis.com/database/cpu/utilization` (CPU %), `cloudsql.googleapis.com/database/memory/utilization` (RAM %), `cloudsql.googleapis.com/database/disk/utilization` (disk %), `cloudsql.googleapis.com/database/network/connections` (active connections), and `cloudsql.googleapis.com/database/replication/replica_lag` (replication lag in seconds for read replicas).
*   **Log-Based Metrics**: Custom Cloud Monitoring metrics created from log entries using filter expressions. For example, you can create a log-based metric that counts the number of Cloud SQL authentication failures per minute and then set an alert on that metric to detect brute-force login attempts.

---

### 2. Certification Exam Tips
*   **Cloud Monitoring vs. Cloud Logging**: Know the distinction. Cloud Monitoring handles structured numeric metrics and time-series data for dashboards and alerts. Cloud Logging handles unstructured and semi-structured text log records for troubleshooting, audit, and compliance. Many exam scenarios require combining both.
*   **Key Metrics to Alert On**: For Cloud SQL, always monitor: CPU utilization (high CPU → query tuning needed), disk utilization (high disk → storage auto-resize or table cleanup needed), connection count (near maximum → add connection pooling), and replication lag (high lag → replica falling behind source). Know which metric indicates which problem.
*   **Audit Logs for Compliance**: Cloud Audit Logs has two categories: Admin Activity (always enabled, records control-plane operations like creating/deleting instances) and Data Access (disabled by default, must be enabled, records data reads and writes). The exam tests which category records what type of event and what must be done to enable Data Access logging.
*   **Log Export and Retention**: Cloud Logging retains logs for 30 days by default. For compliance requirements exceeding 30 days, you must configure a log sink to export logs to Cloud Storage (long-term, low-cost), BigQuery (queryable analytics), or Pub/Sub (real-time streaming to SIEM).
*   **Study Resource:** The official Cloud Monitoring documentation for Cloud SQL is the primary reference: [Cloud SQL Monitoring – Google Cloud](https://cloud.google.com/sql/docs/postgres/monitor-instance). The freeCodeCamp database course covers foundational DBA monitoring concepts: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:
*   **Required Reading:** Use *Database Design* by Adrienne Watt to reinforce the database administration concepts that drive monitoring requirements (performance, security, integrity): [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
*   **Required Video:** This comprehensive free lecture covers database administration fundamentals including monitoring and troubleshooting approaches applicable to GCP: [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).

---

### Lab & Command Integration
In this week's hands-on lab, you will create Cloud Monitoring dashboards for Cloud SQL metrics, configure an alerting policy for high CPU utilization and disk usage, enable Cloud SQL Data Access audit logs, create a log sink to export slow query logs to BigQuery, and run Log Analytics queries to identify anomalous database behavior.

---

### 3. Study Checklist
- [ ] Read the glossary terms and memorize their definitions.
- [ ] Read the database administration and monitoring chapters in [Database Design by Adrienne Watt](https://opentextbc.ca/dbdesign01/).
- [ ] Watch the database operations and monitoring segments in [SQL and Database Administration – freeCodeCamp](https://www.youtube.com/watch?v=HXV3zeQKqGY).
- [ ] Review the Cloud Monitoring dashboard and alerting policy setup in the lab instructions.
- [ ] Proceed to the weekly hands-on lab activity.

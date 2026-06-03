# Video Script: Module 15 — Database Automation and Monitoring (Part 1 of 2)

## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Professional Database Engineer

---

## SLIDE 1 — Welcome and Module Overview

Welcome to Module 15. I'm Professor Nash, and today we cover database automation
and monitoring — two disciplines that separate operational databases from
well-managed production databases.

In Part 1 we cover:

- Cloud Monitoring for databases: metrics, dashboards, and alerting
- Database health indicators and what they mean
- Maintenance windows and automated patching

In Part 2 we cover:

- Terraform for database infrastructure provisioning
- Automated failover testing
- Infrastructure as Code best practices for GCP databases

---

## SLIDE 2 — Why Monitoring Matters

A database that is not monitored is a database that will fail silently. Monitoring
provides three capabilities:

1. **Visibility**: You can see what is happening inside the database right now.
2. **Alerting**: You are notified when something goes wrong before users are impacted.
3. **Historical analysis**: You can look back at metrics to diagnose incidents and
   plan capacity.

For the Google Cloud Professional Database Engineer exam, you need to know:

- Which metrics are most important for Cloud SQL, Spanner, and BigQuery
- How to create alerting policies in Cloud Monitoring
- How to use Cloud Logging for database events
- How dashboards are constructed with custom metrics

---

## SLIDE 3 — Cloud Monitoring Architecture for Databases

Cloud Monitoring is the central observability platform for all GCP resources.
For databases, it collects metrics automatically without any agent installation.

Key components:

**Metrics**: Numeric time-series data collected at regular intervals. Examples:
CPU utilization, active connections, disk I/O, replication lag.

**Alerting policies**: Rules that fire when a metric crosses a threshold for a
sustained duration. Alert notifications go to notification channels (email, PagerDuty,
Slack, PubSub).

**Dashboards**: Visual panels showing multiple metrics side by side, enabling
at-a-glance health assessment.

**Uptime checks**: Periodic probes that verify a service endpoint is reachable.
For Cloud SQL, uptime checks verify that the instance accepts connections.

**Log-based metrics**: Custom metrics derived from log entries in Cloud Logging.
For example, counting the number of `pgaudit` log entries per minute, which tracks
query activity rate.

---

## SLIDE 4 — Critical Cloud SQL Metrics

For the exam and for operations, these are the most important Cloud SQL metrics:

**CPU utilization** (`cloudsql.googleapis.com/database/cpu/utilization`):

- Range: 0.0 to 1.0 (0–100%)
- Alert threshold: > 0.80 (80%) sustained for 5 minutes
- Action: Scale up to a larger instance tier or optimize slow queries

**Memory utilization** (`cloudsql.googleapis.com/database/memory/utilization`):

- Range: 0.0 to 1.0
- Alert threshold: > 0.90 (90%)
- Action: Review memory-intensive queries; scale instance; tune memory flags

**Active connections** (`cloudsql.googleapis.com/database/postgresql/num_backends`
for PostgreSQL):

- Alert threshold: > 80% of the instance's max_connections
- Action: Enable connection pooling (Cloud SQL Proxy + PgBouncer or
  Cloud SQL integrated connection pooler)

**Disk utilization** (`cloudsql.googleapis.com/database/disk/utilization`):

- Alert threshold: > 0.85 (85%)
- Action: Enable auto-storage increase (Cloud SQL feature), or manually increase
  disk size

**Replication lag** (for read replicas):
`cloudsql.googleapis.com/database/replication/replica_lag`

- Alert threshold: > 30 seconds
- Action: Investigate write-heavy workloads; consider cross-region replication
  latency as a baseline

---

## SLIDE 5 — Creating an Alerting Policy for Cloud SQL

Let's walk through creating a CPU utilization alert in Cloud Monitoring.

**Step 1**: Navigate to Monitoring → Alerting → Create Policy.

**Step 2**: Click "Add Condition" and select the metric:

- Resource type: Cloud SQL Database
- Metric: `database/cpu/utilization`
- Filter: `database_id = "PROJECT:INSTANCE_NAME"`

**Step 3**: Set the alert threshold:

- Condition type: Threshold
- Trigger: Any time series violates
- Threshold value: 0.80
- Duration: 5 minutes (sustained violation)

**Step 4**: Add a notification channel (email, PagerDuty, Slack).

**Step 5**: Set the alert name and documentation:

```text
Alert: Cloud SQL CPU Utilization High
Documentation: Instance CPU above 80% for 5 minutes.
Check for long-running queries: SELECT pid, query, state, query_start
FROM pg_stat_activity WHERE state != 'idle' ORDER BY query_start;
```

Including runbook steps in the alert documentation accelerates incident response.

**Using gcloud**:

```bash
gcloud monitoring policies create \
  --policy-from-file=alert-cpu-policy.json
```

---

## SLIDE 6 — Cloud SQL Insights

Cloud SQL Insights is a built-in query performance analysis tool that is enabled
separately from basic Cloud Monitoring. It provides:

- **Top queries by CPU time**: Identifies the queries consuming the most CPU
- **Query latency percentiles**: P50, P95, P99 latency breakdown
- **Execution plan analysis**: Visual explain plan for selected queries
- **Wait event analysis**: Identifies what queries are waiting for (locks, I/O, etc.)

Enabling Insights:

```bash
gcloud sql instances patch my-pg-instance \
  --insights-config-query-insights-enabled \
  --insights-config-query-string-length=1024 \
  --insights-config-record-application-tags \
  --insights-config-record-client-address
```

Insights is available for Cloud SQL for PostgreSQL and MySQL. It is the first tool
to reach for when optimizing a slow application against Cloud SQL.

For the exam: Cloud SQL Insights provides query-level performance data. Cloud
Monitoring provides instance-level resource metrics. Use both together for
comprehensive observability.

---

## SLIDE 7 — Cloud Spanner Monitoring

Cloud Spanner has its own set of critical metrics. The most important ones:

**CPU utilization** (`spanner.googleapis.com/instance/cpu/utilization`):

- Spanner has two types of CPU: regional (per-region) and multi-region
- **High-priority CPU**: CPU used for user-facing requests. Alert if > 65%.
- **Total CPU**: All CPU including background tasks. Alert if > 90%.
- Unlike Cloud SQL, Spanner's CPU is a pooled resource across compute nodes.

**Storage utilization** (`spanner.googleapis.com/instance/storage/utilization`):

- Range: 0.0 to 1.0 (percentage of provisioned storage)
- Spanner auto-scales storage, but extremely high utilization can indicate
  unexpected data growth.

**API request counts** (`spanner.googleapis.com/api/request_count`):

- Broken down by method (reads vs. mutations), status code, and database
- Monitor for error rate spikes (4xx or 5xx status codes)

**Query latency** (`spanner.googleapis.com/api/request_latencies`):

- P50/P95/P99 distribution
- Spanner's SLA target is P99 < 5ms for reads, P99 < 10ms for writes

---

## SLIDE 8 — BigQuery Monitoring

BigQuery monitoring works differently because BigQuery is serverless — there are no
instances to monitor. Instead, you monitor job-level metrics.

**Slot utilization** (`bigquery.googleapis.com/storage/table_count`):

- For flat-rate pricing: monitor slot utilization to ensure you have enough capacity
- Alert if slot utilization > 90% for sustained periods (queries queued)

**Bytes processed** (from `INFORMATION_SCHEMA.JOBS_BY_PROJECT`):

- Not a Cloud Monitoring metric — query directly from BigQuery
- Monitor daily bytes processed trends to detect unexpected query cost spikes

**Job failure rate** (`bigquery.googleapis.com/job/num_failed_jobs`):

- Alert if > 0 failed jobs per hour in production pipelines
- Failed jobs indicate pipeline health problems

**Log-based metric for BigQuery**:

Create a log-based metric counting `bigquery.googleapis.com/data_access` log
entries with `status.code != 0` to track query errors in real time.

---

## SLIDE 9 — Maintenance Windows

Cloud SQL maintenance windows define when Google applies automatic updates —
security patches, engine minor version upgrades, and infrastructure maintenance.

Configuring a maintenance window:

```bash
gcloud sql instances patch my-pg-instance \
  --maintenance-window-day=SUNDAY \
  --maintenance-window-hour=3
```

Best practices:

- Set maintenance windows to low-traffic periods (e.g., Sunday 3 AM)
- For high-availability instances, maintenance is performed as a live migration
  with only a brief reconnection event (typically under 60 seconds)
- For non-HA instances, maintenance requires a restart — plan for 2–5 minutes
  of downtime during the maintenance window

**Deny maintenance period**: You can specify a period during which maintenance is
blocked (e.g., Black Friday through Cyber Monday for a retail company):

```bash
gcloud sql instances patch my-pg-instance \
  --deny-maintenance-period-start-date=2025-11-27 \
  --deny-maintenance-period-end-date=2025-12-02 \
  --deny-maintenance-period-time=00:00:00
```

---

## SLIDE 10 — Automated Database Backups

Cloud SQL automated backups run on a configurable schedule. Key settings:

```bash
gcloud sql instances patch my-pg-instance \
  --backup-start-time=02:00 \
  --retained-backups-count=30 \
  --retained-transaction-log-days=7
```

Backup details:

- `--backup-start-time`: The start of a 4-hour backup window (e.g., 02:00 means
  2:00 AM to 6:00 AM)
- `--retained-backups-count`: Number of automated backups to retain (max 365)
- `--retained-transaction-log-days`: Days of transaction logs to keep for
  point-in-time recovery (PITR). Maximum 7 days.

Point-in-time recovery restores the database to any second within the PITR window:

```bash
gcloud sql instances clone my-pg-instance my-pg-restore \
  --point-in-time=2025-06-01T14:30:00Z
```

For the exam: Automated backups and PITR are distinct. Automated backups are
full backups taken daily. PITR uses transaction logs to replay changes up to
any specific second.

---

## SLIDE 11 — Part 1 Summary

Key concepts from Part 1:

- Cloud Monitoring collects metrics automatically for all GCP database services
- Critical Cloud SQL metrics: CPU, memory, connections, disk, replication lag
- Cloud SQL Insights provides query-level performance analysis
- Spanner CPU alert threshold: high-priority CPU > 65%
- BigQuery monitoring centers on slot utilization and INFORMATION_SCHEMA job data
- Maintenance windows schedule patching during off-peak hours
- Deny maintenance periods block updates during critical business periods
- Automated backups + PITR provide different recovery granularities

In Part 2 we cover Terraform for database provisioning and automated failover testing.

---

*End of Part 1 Script*

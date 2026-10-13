# Reading Guide: Module 15 — Database Automation and Monitoring

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4327 &BULL; DATABASE ADMINISTRATION & SQL OPTIMIZATION</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4327 Database Administration

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Professional Database Engineer

---

## Overview

This reading guide supports Module 15 on database automation and monitoring. Monitoring
and automation are operational competencies that keep production databases healthy,
available, and cost-efficient. The exam tests your knowledge of Cloud Monitoring
configuration, metric selection, and Terraform for IaC provisioning.

**Estimated reading time**: 55–70 minutes

---

## Section 1 — Cloud Monitoring Fundamentals

### 1.1 Metric Descriptor Structure

Every Cloud Monitoring metric has a descriptor that defines its properties:

- **Metric type**: The full name, e.g., `cloudsql.googleapis.com/database/cpu/utilization`
- **Kind**: `GAUGE` (point-in-time value), `DELTA` (change since last measurement),
  or `CUMULATIVE` (total since resource creation)
- **Value type**: BOOL, INT64, DOUBLE, STRING, or DISTRIBUTION
- **Labels**: Key-value pairs that distinguish between metric streams (e.g.,
  `database_id`, `region`)

Understanding metric kind matters for alert configuration:

- GAUGE metrics: alert when the current value exceeds a threshold
- DELTA metrics: alert when the rate of change exceeds a threshold (useful for
  detecting sudden spikes in error counts)
- CUMULATIVE metrics: must be converted to a rate before alerting

### 1.2 Alerting Policy Components

A complete alerting policy in Cloud Monitoring has:

**Conditions**: One or more metric conditions that, when true, trigger the alert.
Multiple conditions can be combined with AND or OR logic.

**Notification channels**: Where alerts are sent. Types include:

- Email
- SMS
- Slack webhook
- PagerDuty
- Cloud Pub/Sub (for programmatic handling)
- Webhook (for custom integrations)

**Documentation**: Markdown text attached to the alert that provides context and
runbook steps. This text appears in the alert notification, so include actionable
steps for the on-call engineer.

**Alert duration**: How long the condition must be true before the alert fires.
This prevents flapping alerts from brief metric spikes.

### 1.3 Uptime Checks

Uptime checks are distinct from metric-based alerts. They proactively test whether
an endpoint is reachable and responding correctly.

For Cloud SQL, configure an uptime check that:

1. Connects to the Cloud SQL Auth Proxy or private IP
2. Executes a trivial SQL query (e.g., `SELECT 1`)
3. Expects a response within a timeout threshold

If the uptime check fails from multiple geographic locations, the alert fires.

Uptime checks complement metric alerts: a metric alert fires when the database is
degraded but still running; an uptime check alert fires when the database is
completely unreachable.

---

## Section 2 — Advanced Monitoring Patterns

### 2.1 Log-Based Metrics

Some database health signals are expressed in logs rather than metrics. Log-based
metrics let you create custom metrics derived from log content.

Example: Count lock wait events in PostgreSQL logs.

Step 1 — Identify the log pattern. Cloud SQL PostgreSQL logs lock waits as:

```text
LOG: process 12345 still waiting for ShareLock on transaction 67890 after 1000.123 ms
```

Step 2 — Create a log-based metric in Cloud Logging:

```bash
gcloud logging metrics create pg-lock-waits \
  --description="PostgreSQL lock wait events" \
  --log-filter='resource.type="cloudsql_database" textPayload:"still waiting for"' \
  --metric-descriptor-type=logging.googleapis.com/user/pg-lock-waits \
  --value-extractor=EXTRACT(textPayload)
```

Step 3 — Create an alerting policy on the log-based metric.

### 2.2 Synthetic Monitors

A synthetic monitor runs a Cloud Function on a schedule to perform a realistic
user journey against the application. For databases, this means connecting to the
database, running a realistic query, and checking the result.

Example use case: Alert if a specific slow query that should complete in < 500ms
starts taking > 2 seconds, indicating a performance degradation not visible from
generic CPU/memory metrics.

### 2.3 SLOs in Cloud Monitoring

Service Level Objectives (SLOs) formalize reliability commitments. Cloud Monitoring
supports SLO tracking with automatic error budget calculation.

For a Cloud SQL instance, an example SLO:

- **SLI**: Fraction of 1-minute windows in which instance CPU < 80%
- **SLO**: 99.5% of windows over a 30-day rolling window meet the SLI
- **Error budget**: 0.5% of windows (approximately 3.6 hours/month) can violate the SLI

When the error budget is consumed, Cloud Monitoring can alert you to stop non-emergency
changes that might impact reliability.

---

## Section 3 — Terraform for GCP Databases

### 3.1 Terraform Workflow in a CI/CD Pipeline

In a production environment, Terraform changes follow this workflow:

1. Developer writes HCL changes and opens a pull request.
2. CI (Cloud Build or GitHub Actions) runs `terraform plan` and posts the plan output
   as a PR comment.
3. Reviewer approves the PR after reviewing the plan.
4. Merge triggers `terraform apply` in the CD pipeline.
5. Terraform applies changes and updates the state file in GCS.

This workflow ensures every infrastructure change is reviewed, planned, and applied
consistently — the same discipline applied to application code.

### 3.2 Terraform Modules for Databases

Terraform modules encapsulate reusable infrastructure patterns. A Cloud SQL module
might expose these input variables:

```hcl
variable "instance_name"    { type = string }
variable "database_version" { type = string  default = "POSTGRES_15" }
variable "tier"             { type = string  default = "db-n1-standard-4" }
variable "region"           { type = string }
variable "enable_ha"        { type = bool    default = true }
variable "private_network"  { type = string }
variable "backup_start_time"{ type = string  default = "02:00" }
```

Using the module:

```hcl
module "prod_database" {
  source          = "./modules/cloud-sql"
  instance_name   = "prod-pg-v2"
  region          = "us-central1"
  enable_ha       = true
  private_network = google_compute_network.prod_vpc.self_link
}
```

Modules enforce organizational standards — every database created through the
module gets HA, private IP, and automated backups by default.

### 3.3 Importing Existing Resources

If a database was created manually before Terraform adoption, you can bring it
under Terraform management using `terraform import`:

```bash
terraform import google_sql_database_instance.primary \
  projects/PROJECT_ID/instances/INSTANCE_NAME
```

After import, Terraform knows about the existing resource. Future `terraform plan`
runs will show only actual configuration differences.

### 3.4 Terraform Security Best Practices

- Never store database passwords in `terraform.tfvars` — use Secret Manager
  and retrieve them with the `google_secret_manager_secret_version` data source.
- Enable `deletion_protection = true` on all production resources.
- Use `prevent_destroy = true` in lifecycle blocks for critical resources.
- Review `terraform plan` output carefully before applying — accidental `destroy`
  operations can be catastrophic for databases.

```hcl
resource "google_sql_database_instance" "primary" {
  lifecycle {
    prevent_destroy = true
  }
}
```

---

## Section 4 — Failover and Disaster Recovery Testing

### 4.1 Cloud SQL HA Architecture

Cloud SQL HA (Regional availability type) uses:

- A **primary instance** in one zone
- A **standby instance** (replica) in a different zone in the same region
- Synchronous replication between primary and standby using disk-level replication

During failover:

1. The primary becomes unavailable (failure or forced failover).
2. Cloud SQL automatically promotes the standby to primary.
3. The old primary, once recovered, becomes the new standby.
4. Applications using the Cloud SQL instance connection name reconnect automatically
   (connection name does not change during failover).

Key metric: **Failover time**. For Cloud SQL, failover typically takes 30–120 seconds
from failure detection to the new primary accepting connections.

### 4.2 Testing Connection String Resilience

Applications that do not handle reconnection correctly will stay broken after failover
even though the database has recovered. Test the following scenarios:

- **Connection pool reconnection**: Does the pool retry connections automatically?
  Configure `connectionTestQuery`, `minimumIdle`, and retry logic in HikariCP or similar.
- **Prepared statement caching**: Some connection pools cache prepared statements.
  After failover, old prepared statement IDs are invalid. Pools must recreate them.
- **DNS caching**: If the application caches DNS responses for the Cloud SQL private IP,
  it may connect to the old (now standby) IP after failover. Verify DNS TTL is low or
  use the Cloud SQL Auth Proxy, which handles reconnection automatically.

### 4.3 Spanner Automatic Failover

Cloud Spanner handles node failures automatically without any manual intervention.
Spanner distributes data across multiple nodes and zones (or regions for multi-region).
When a node fails, queries are automatically routed to surviving nodes. There is no
`failover` command for Spanner — resilience is built into the architecture.

For regional Spanner instances: three zones in a region, majority write quorum.
For multi-region: minimum three read-write regions, automatic leader election.

---

## Section 5 — Key Terms

**Cloud Monitoring**: GCP's unified metrics, alerting, and dashboard service.

**GAUGE metric**: A metric that represents a point-in-time value (e.g., current CPU utilization).

**Alerting policy**: A rule that monitors one or more metrics and sends notifications when conditions are met.

**Cloud SQL Insights**: Built-in query performance analysis for Cloud SQL that surfaces slow queries and wait events.

**Maintenance window**: A configured time period during which Cloud SQL applies automatic updates.

**Deny maintenance period**: A time range during which Cloud SQL maintenance is blocked.

**Terraform**: HashiCorp's declarative IaC tool for provisioning and managing GCP infrastructure.

**Terraform state**: A file (stored remotely in GCS) that maps Terraform resource definitions to actual deployed resources.

**Terraform module**: A reusable package of Terraform configuration encapsulating a standard infrastructure pattern.

**Forced failover**: Triggering a Cloud SQL HA failover manually using `gcloud sql instances failover`.

**Log-based metric**: A custom Cloud Monitoring metric derived from log entries using a filter and value extractor.

---

## Section 6 — Review Questions

1. What is the difference between a GAUGE and a DELTA metric in Cloud Monitoring? Give a database example of each.

2. For a Cloud SQL for PostgreSQL instance, what metric should you alert on to detect that the connection pool is near exhaustion? What action would you take?

3. What is Cloud SQL Insights, and how does it differ from standard Cloud Monitoring metrics?

4. A Cloud SQL HA failover takes 90 seconds, but the application takes 5 minutes to recover. What application-side issues might explain this gap?

5. Explain why `deletion_protection = true` is important in a Terraform Cloud SQL resource. What happens if you try to run `terraform destroy` without it?

6. What Terraform command imports an existing manually-created Cloud SQL instance into Terraform state? Why is this useful?

7. A Cloud SQL maintenance window is configured for Sunday at 3 AM. The database has `availability_type = "REGIONAL"` (HA). What does the user experience during maintenance?

8. How would you monitor for a sudden spike in lock wait events in Cloud SQL for PostgreSQL? What Cloud Monitoring feature would you use?

9. What is the purpose of a Terraform GCS backend? What problems does it solve compared to local state?

10. You run `gcloud sql instances failover prod-pg`. The instance recovers in 75 seconds but user-facing errors persist for 4 minutes. What is the most likely cause?

---

## Section 7 — Certification Exam Alignment

Monitoring and automation appear in multiple exam domains:

- **Section 1 (Design)**: Choosing monitoring strategy, SLO definition, HA configuration
- **Section 2 (Ingest and manage)**: Maintenance windows, backup configuration via Terraform
- **Section 4 (Secure)**: Audit log-based metrics for security monitoring
- **Section 5 (Monitor)**: Full domain — metrics, dashboards, alerting, Insights, failover testing

The exam frequently presents scenarios where you must select the correct metric and
threshold combination for a described problem, or choose the right Terraform resource
attribute to meet a stated requirement.

---

## Recommended Resources

- Cloud Monitoring metric catalog: cloud.google.com/monitoring/api/metrics_gcp
- Cloud SQL Insights: cloud.google.com/sql/docs/postgres/using-insights
- Terraform Google provider docs: registry.terraform.io/providers/hashicorp/google
- Cloud SQL HA overview: cloud.google.com/sql/docs/postgres/high-availability
- Cloud Monitoring alerting: cloud.google.com/monitoring/alerts

---

---

## 9. Supplemental Resources

The following free, open-access resources support Module 15 topics:

**1. [Google Cloud — Cloud Monitoring Metrics for Cloud SQL](https://cloud.google.com/monitoring/api/metrics_gcp#gcp-cloudsql)**
Complete reference for all Cloud SQL metrics available in Cloud Monitoring, including connection count, CPU, memory, disk, replication lag, and backup metrics with their units and descriptions.

**2. [Terraform Registry — Google Cloud SQL Instance Resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)**
Official Terraform provider documentation for `google_sql_database_instance`, covering all configurable attributes including `deletion_protection`, `backup_configuration`, `database_flags`, `maintenance_window`, and `deny_maintenance_period`.

**3. [Google Cloud — Cloud SQL Query Insights](https://cloud.google.com/sql/docs/postgres/using-insights)**
Explains how to enable and use Query Insights for Cloud SQL, including how to interpret the query latency distribution, top queries by CPU, and per-query wait event breakdown.

**4. [Google Cloud — Cloud Monitoring Alerting Policies](https://cloud.google.com/monitoring/alerts/using-alerting-ui)**
Covers creating alerting policies with threshold conditions, duration settings, notification channels, and log-based metrics — including how to create absence alerts for missing metric data.

---

Module 15 Reading Guide — CIS-4327 Database Administration

Texas Wesleyan University | Proprietary and Confidential. Not for disclosure outside of course participants.

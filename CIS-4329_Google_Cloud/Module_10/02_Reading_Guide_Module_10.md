# Reading Guide: Module 10 — Cloud Operations: Monitoring and Logging

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This reading guide accompanies the Module 10 video lectures on Cloud Operations. It
covers Cloud Monitoring, Cloud Logging, Cloud Trace, Cloud Profiler, and Error Reporting.

**Estimated reading time**: 60–75 minutes

---

### Learning Objectives

After completing this module's readings you will be able to:

- Describe the Cloud Operations product family and each service's purpose
- Configure Cloud Monitoring dashboards, uptime checks, and alerting policies
- Create log sinks to export logs to Cloud Storage, BigQuery, and Pub/Sub
- Write Logging Query Language filters to find specific log entries
- Explain the four types of audit logs and their default retention and cost
- Describe the purpose of Cloud Trace, Cloud Profiler, and Error Reporting
- Install the Ops Agent on a GCE VM to collect memory and disk metrics

---

### Required Reading 1: Cloud Monitoring

**Source**: Google Cloud Documentation — Cloud Monitoring Overview

**URL**: `https://cloud.google.com/monitoring/docs/monitoring-overview`

#### Cloud Monitoring Key Terms

- **Metric**: A time-series measurement of a resource attribute (e.g., CPU utilization,
  request latency, disk bytes written)
- **Metric type**: A fully qualified string identifying the metric, such as
  `compute.googleapis.com/instance/cpu/utilization`
- **Time series**: A sequence of data points for a metric collected at regular intervals
- **Alerting policy**: Defines a condition, a duration, and one or more notification
  channels; fires when the condition is met for the specified duration
- **Notification channel**: Destination for alert notifications; options include email,
  PagerDuty, Slack, SMS, Pub/Sub, and webhooks
- **Uptime check**: A synthetic probe that verifies endpoint availability from multiple
  global locations
- **Ops Agent**: The recommended unified agent for collecting OS-level metrics (memory,
  disk, process) and application logs from GCE VMs

#### Cloud Monitoring ACE Exam Focus Points

- GCE VMs do NOT report memory utilization or disk utilization to Cloud Monitoring by
  default — the Ops Agent must be installed
- An alerting policy can target a log-based metric, allowing alerts on log patterns
- Uptime checks use multiple global probe locations; GCP marks an endpoint down when a
  majority of probers fail
- Workspaces can aggregate monitoring data from multiple GCP projects into one view
- Alert conditions have a `duration` field — the condition must be met continuously for
  this duration before the alert fires (prevents false positives from momentary spikes)

#### Cloud Monitoring Review Questions

1. Which agent must you install on a GCE VM to report memory utilization to Cloud
   Monitoring?
2. What is the purpose of a notification channel in an alerting policy?
3. What does the `duration` field in an alerting condition control?

---

### Required Reading 2: Cloud Logging

**Source**: Google Cloud Documentation — Cloud Logging Overview

**URL**: `https://cloud.google.com/logging/docs/overview`

#### Cloud Logging Key Terms

- **Log entry**: A single structured record written to Cloud Logging; includes a payload,
  resource descriptor, severity, and timestamp
- **Log bucket**: Storage location for log entries within Cloud Logging; `_Default` and
  `_Required` buckets are created automatically
- **Log sink**: A configuration that routes matching log entries to an external
  destination (Cloud Storage, BigQuery, Pub/Sub, or another log bucket)
- **Log exclusion**: A filter applied in the log router that permanently drops matching
  entries before ingestion
- **Log router**: Processes all incoming log entries through sinks and exclusions in
  sequence
- **Logs Explorer**: The Cloud Console UI for querying and viewing log entries
- **Writer identity**: The service account that a log sink uses to write to its
  destination; must be granted appropriate permissions on the destination

#### Log Bucket Defaults

| Bucket | Retention | Notes |
|---|---|---|
| `_Required` | 400 days | Audit logs; cannot be shortened or deleted |
| `_Default` | 30 days | All other logs; retention is configurable |

#### Cloud Logging ACE Exam Focus Points

- Exclusions permanently drop log entries — they will not appear anywhere, including
  in sinks
- After creating a sink, you must grant the sink's writer identity write access to the
  destination (Cloud Storage: `storage.objectCreator`; BigQuery: `bigquery.dataEditor`)
- The `--use-partitioned-tables` flag for BigQuery sinks creates date-partitioned tables,
  which reduces query cost
- Log sinks can have inclusion filters to export only matching entries (e.g., only
  audit logs, only ERROR severity)
- Organization-level sinks aggregate logs from all projects in an organization

#### Cloud Logging Review Questions

1. What must you do after creating a log sink before it can write to its destination?
2. What is the difference between a log exclusion and a log sink with an inclusion
   filter?
3. What is the default retention period for logs in the `_Default` log bucket?

---

### Required Reading 3: Audit Logs

**Source**: Google Cloud Documentation — Cloud Audit Logs

**URL**: `https://cloud.google.com/logging/docs/audit`

#### Audit Log Key Terms

- **Admin Activity logs**: Record API calls and administrative actions that modify
  resources (e.g., create VM, delete bucket); always enabled; always free; retained 400
  days
- **Data Access logs**: Record API calls that read resource data or metadata; disabled
  by default; must be enabled per service; may incur charges at high volume
- **System Event logs**: Record Google-initiated system events such as live migration;
  always enabled; free; retained 400 days
- **Policy Denied logs**: Record when access is denied by VPC Service Controls or Cloud
  Armor; always enabled; free

#### Audit Log ACE Exam Focus Points

- Admin Activity logs are always on — you cannot disable them
- Data Access logs are off by default — enable them only for services where you need
  data-level audit trails
- All four audit log types are written to the `_Required` bucket with 400-day retention
- Data Access logs for BigQuery are enabled by default because BigQuery data access is
  already audited at no charge; other services require manual enablement
- Audit logs can be exported via log sinks for long-term retention beyond 400 days

#### Audit Log Review Questions

1. Which audit log type records when a user creates or deletes a GCE instance?
2. Which audit log type must be explicitly enabled per service?
3. Where are all four audit log types stored within Cloud Logging?

---

### Required Reading 4: Cloud Trace and Cloud Profiler

**Source**: Google Cloud Documentation — Cloud Trace Overview

**URL**: `https://cloud.google.com/trace/docs/overview`

#### Cloud Trace Key Terms

- **Distributed trace**: A record of a request's journey across multiple services,
  capturing the latency of each hop
- **Span**: A single named and timed unit of work within a trace (e.g., one database
  query, one HTTP call)
- **Trace ID**: A unique identifier that links all spans belonging to the same request
- **Latency distribution**: Cloud Trace analyzes traces and shows percentile latency
  (p50, p95, p99) to surface high-latency outliers

#### Cloud Profiler Key Terms

- **CPU profiling**: Samples the call stack to identify which functions consume the most
  CPU time
- **Heap profiling**: Samples memory allocation to identify which code paths allocate
  the most memory
- **Flame graph**: Visualization of profiling data showing the call hierarchy and
  relative time or memory spent in each function

#### Trace and Profiler ACE Exam Focus Points

- Cloud Trace is for latency analysis — "which part of the request is slow?"
- Cloud Profiler is for performance optimization — "which function uses the most CPU
  or memory?"
- App Engine, Cloud Run, and GKE integrate with Cloud Trace automatically when using
  supported frameworks
- Cloud Profiler requires a client library and a brief initialization call in application
  code; it operates continuously with less than 1% overhead

---

### Required Reading 5: Error Reporting

**Source**: Google Cloud Documentation — Error Reporting Overview

**URL**: `https://cloud.google.com/error-reporting/docs/overview`

#### Error Reporting Key Terms

- **Error group**: A cluster of similar exceptions/crashes grouped by stack trace
  signature
- **First seen / last seen**: Timestamps tracking when the error group was first observed
  and when it most recently occurred
- **New error alert**: Error Reporting notifies you when a new error group appears that
  has not been seen before

#### Error Reporting ACE Exam Focus Points

- Error Reporting automatically integrates with App Engine, Cloud Functions, Cloud Run,
  and GKE — no configuration required for these services
- For GCE VMs, errors must be written to Cloud Logging in a structured format that Error
  Reporting can parse
- Error Reporting does NOT replace Cloud Monitoring alerts — it specifically focuses on
  exceptions and crashes, not metric thresholds

---

### Cloud Operations Summary

| Service | Primary purpose | ACE trigger phrase |
|---|---|---|
| Cloud Monitoring | Metrics, dashboards, alerts | "Alert when CPU exceeds 80%" |
| Cloud Logging | Log storage, routing, querying | "Export logs to BigQuery" |
| Cloud Trace | Request latency analysis | "Identify slow API endpoints" |
| Cloud Profiler | CPU/memory profiling | "Identify CPU hotspots in code" |
| Error Reporting | Exception aggregation | "Alert on new application errors" |

---

### Pre-Lab Checklist

Before starting Lab 10, confirm you can answer yes to each item:

- I can explain what the Ops Agent does and why it is needed for GCE memory metrics
- I understand the difference between a log sink and a log exclusion
- I know that Admin Activity audit logs are always enabled and free
- I can write a basic Logging Query Language filter
- I understand that after creating a sink I must grant permissions to the writer identity

---

### Additional Resources

- Cloud Monitoring documentation:
  `https://cloud.google.com/monitoring/docs`
- Cloud Logging documentation:
  `https://cloud.google.com/logging/docs`
- Ops Agent installation:
  `https://cloud.google.com/stackdriver/docs/solutions/agents/ops-agent`
- Logging Query Language reference:
  `https://cloud.google.com/logging/docs/view/logging-query-language`
- ACE exam guide:
  `https://cloud.google.com/certification/guides/cloud-engineer`

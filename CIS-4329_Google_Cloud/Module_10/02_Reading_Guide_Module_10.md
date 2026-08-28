# Reading Guide: Module 10 — Cloud Operations: Monitoring and Logging

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4329 &BULL; GOOGLE CLOUD PLATFORM (GCP) CLOUD ARCHITECTURE</text>
    
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

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud Monitoring Alerting Policies**
<https://cloud.google.com/monitoring/alerts>
Complete guide to creating and managing alerting policies in Cloud Monitoring, including condition types, notification channels, alert duration, and the requirement to verify notification channel email addresses before alerts will fire.

**2. Google Cloud Skills Boost — Cloud Monitoring: Qwik Start**
<https://www.cloudskillsboost.google/focuses/10599>
Hands-on lab covering Ops Agent installation on a Compute Engine VM, creating custom dashboards, configuring uptime checks, and setting up alerting policies — all core ACE exam operational topics.

**3. Google Cloud Documentation — Logging Query Language**
<https://cloud.google.com/logging/docs/view/logging-query-language>
Reference for the Logging Query Language (LQL) including comparison operators, severity filtering with `>=`, resource type filters, and structured log field extraction — essential for both the ACE exam and the log-based metrics lab exercises.

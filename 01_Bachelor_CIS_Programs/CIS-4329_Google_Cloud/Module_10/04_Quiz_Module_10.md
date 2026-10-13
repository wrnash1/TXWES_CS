# Quiz: Module 10 — Cloud Operations: Monitoring and Logging

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Instructions

Select the single best answer for each question. Each question is worth 10 points.
Total: 100 points.

---

### Question 1

A team has deployed a web application on Compute Engine VMs. They want to alert when
memory utilization exceeds 85% for more than 5 minutes. After configuring an alerting
policy in Cloud Monitoring, they notice that memory metrics are not available. What is
the most likely cause?

- A) Memory metrics require a paid Cloud Monitoring subscription
- B) The Ops Agent has not been installed on the VMs
- C) Memory metrics are only available for GKE nodes, not GCE VMs
- D) The alerting policy threshold is too high

Correct answer: B — GCE VMs do not report memory utilization to Cloud Monitoring by
default. The Ops Agent (formerly the Monitoring and Logging agents) must be installed to
collect OS-level metrics including memory, disk, and process utilization. Without the
agent, only hypervisor-level metrics like CPU utilization and network traffic are
available.

---

### Question 2

You need to export all Admin Activity audit logs from a GCP project to a BigQuery dataset
for long-term analysis and SQL querying. Which Cloud Logging feature should you use?

- A) Log exclusion
- B) Log bucket with extended retention
- C) Log sink targeting BigQuery
- D) Data Access audit log configuration

Correct answer: C — A log sink exports matching log entries to an external destination.
Configuring a sink with a filter for Admin Activity audit logs and a BigQuery dataset as
the destination routes those logs to BigQuery for SQL analysis. Log exclusions drop logs,
not export them. A log bucket stores logs within Cloud Logging. Data Access audit log
configuration controls which data access events are captured, not where they are sent.

---

### Question 3

After creating a log sink to export logs to a Cloud Storage bucket, you discover that no
logs are being written to the bucket. The sink configuration looks correct. What is the
most likely cause?

- A) The log filter on the sink is excluding all logs
- B) Cloud Logging does not support Cloud Storage as a sink destination
- C) The sink's writer identity has not been granted write access to the bucket
- D) Log sinks have a 24-hour propagation delay before they begin writing

Correct answer: C — Every log sink has a writer identity (a service account). After
creating the sink, you must grant that service account at minimum the
`storage.objectCreator` role on the destination bucket. If this permission is missing,
the sink silently fails to write. This is the most common post-creation configuration
mistake with log sinks.

---

### Question 4

Which of the following statements about Admin Activity audit logs is correct?

- A) Admin Activity logs are disabled by default and must be enabled per service
- B) Admin Activity logs are always enabled, cannot be disabled, and are retained for 400 days
- C) Admin Activity logs are free for the first 30 days and then charged per GB
- D) Admin Activity logs are only generated for project Owner and Editor role actions

Correct answer: B — Admin Activity audit logs are always enabled and cannot be disabled.
They record all administrative API calls that create, modify, or delete GCP resources.
They are stored in the `_Required` log bucket with a fixed 400-day retention period and
are always free. Data Access logs, not Admin Activity logs, must be explicitly enabled.

---

### Question 5

A developer wants to alert on the number of HTTP 500 errors returned by an application
running on App Engine. App Engine does not expose an HTTP 500 error count as a built-in
Cloud Monitoring metric. What is the recommended approach?

- A) Use Cloud Trace to count error spans
- B) Create a log-based metric from the App Engine request logs and use it in an alerting
   policy
- C) Use Error Reporting to trigger Cloud Monitoring alerts
- D) Enable Data Access audit logs and filter for 500 responses

Correct answer: B — Log-based metrics extract numeric data from log entries and make them
available as Cloud Monitoring metrics. You create a log-based metric with a filter that
matches HTTP 500 log entries, then reference that metric in an alerting policy. This is
the standard pattern for alerting on application-level events that are captured in logs
but not available as native metrics.

---

### Question 6

You need to reduce Cloud Logging storage costs by preventing DEBUG-level logs from being
ingested at all. These logs are not needed for any operational or compliance purpose.
Which approach permanently prevents these logs from being stored?

- A) Create a log sink with a filter that excludes DEBUG logs
- B) Configure the application to not emit DEBUG logs
- C) Create a log exclusion with a filter matching DEBUG severity
- D) Set the `_Default` log bucket retention to 1 day

Correct answer: C — A log exclusion permanently drops matching log entries in the log
router before ingestion, meaning they never reach any log bucket or sink. A log sink
still allows the logs to be ingested and stored in the `_Default` bucket unless they are
also excluded. Reducing retention does not prevent ingestion. Configuring the application
is valid but not a Cloud Logging feature.

---

### Question 7

An organization wants to understand the end-to-end latency of API requests as they flow
through multiple microservices. Which GCP Cloud Operations service is designed for this
purpose?

- A) Cloud Monitoring with custom metrics
- B) Cloud Logging with structured request logs
- C) Cloud Trace
- D) Cloud Profiler

Correct answer: C — Cloud Trace is the distributed tracing service designed to visualize
the end-to-end journey and latency of a request across multiple services. Each service
contributes spans to a trace, allowing you to see exactly where time is spent. Cloud
Profiler analyzes CPU and memory usage within a single service's code. Cloud Monitoring
tracks aggregate metrics. Cloud Logging captures log records but does not provide the
trace visualization model.

---

### Question 8

Which Cloud Operations service would you use to identify which specific function in your
Python application is responsible for excessive memory allocation in production?

- A) Cloud Trace
- B) Cloud Profiler
- C) Error Reporting
- D) Cloud Monitoring with the Ops Agent

Correct answer: B — Cloud Profiler continuously profiles CPU usage and heap memory
allocation in production applications. It provides flame graphs showing the call hierarchy
and relative memory allocated by each function. Cloud Trace tracks request latency across
services, not memory allocation within a single function. Error Reporting captures
exceptions. The Ops Agent collects OS-level memory metrics, not per-function heap
profiling.

---

### Question 9

A team needs to export logs from all projects in an organization to a centralized BigQuery
dataset for security analysis. Which log sink scope should they configure?

- A) A project-level sink in each project, each targeting the same BigQuery dataset
- B) An organization-level aggregated sink targeting the centralized BigQuery dataset
- C) A folder-level sink per folder with individual BigQuery datasets
- D) Cloud Monitoring workspace that spans all projects

Correct answer: B — An organization-level aggregated sink collects logs from all projects
within the organization and routes them to a single destination. This avoids creating and
maintaining individual sinks in each project. Folder-level sinks cover all projects within
a folder. Project-level sinks would require one per project and do not scale well across
a large organization.

---

### Question 10

You are reviewing audit logs to determine which user created a specific Cloud Storage
bucket 3 weeks ago. Which log type would contain this event, and where is it stored?

- A) Data Access log; stored in the `_Default` log bucket, retained 30 days
- B) System Event log; stored in the `_Required` log bucket, retained 400 days
- C) Admin Activity log; stored in the `_Required` log bucket, retained 400 days
- D) Policy Denied log; stored in the `_Default` log bucket, retained 30 days

Correct answer: C — Creating a Cloud Storage bucket is an administrative action that
modifies GCP resource configuration, so it is captured in the Admin Activity audit log.
Admin Activity logs are stored in the `_Required` bucket with 400-day retention — so
a 3-week-old event would still be available. Data Access logs capture data reads and
writes to bucket objects, not bucket creation. System Event logs capture Google-initiated
events, not user actions.

---

### Question 11 (5 points)

A team configures a Cloud Monitoring alerting policy with a condition that triggers
when CPU utilization exceeds 90%. The notification channel is an email address. After
24 hours no alerts have fired despite CPU exceeding 90% several times. What is the
most likely cause?

- A) Cloud Monitoring only sends alerts for resource types with the Ops Agent installed
- B) The alerting policy was saved in draft state and is not active
- C) The notification channel email address has not been verified
- D) CPU metrics require Data Access audit logs to be enabled

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) CPU utilization is a hypervisor-level metric available for all GCE VMs without the Ops Agent; it does not require the Ops Agent.
  - B) Cloud Monitoring alerting policies do not have a draft state; once created, they are immediately active.
  - D) Data Access audit logs record API calls to GCP data services; they are unrelated to Compute Engine CPU metrics or alerting policies.

---

### Question 12 (5 points)

Which Logging Query Language (LQL) filter expression correctly matches all log
entries with severity ERROR or higher?

- A) `severity = "ERROR"`
- B) `severity >= ERROR`
- C) `logName = "ERROR"`
- D) `severity IN ("ERROR", "CRITICAL", "ALERT", "EMERGENCY")`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `severity = "ERROR"` matches only ERROR severity exactly; it does not match CRITICAL, ALERT, or EMERGENCY, which are higher severity levels.
  - C) `logName` is the full resource path of the log (e.g., `projects/PROJECT_ID/logs/cloudaudit.googleapis.com`), not a severity value; this expression is syntactically incorrect for severity filtering.
  - D) While option D would technically match the four listed severities, it is verbose and would miss any future severity levels; `severity >= ERROR` is the idiomatic and comprehensive LQL expression.

---

### Question 13 (5 points)

A Cloud Logging sink exports logs to a Cloud Storage bucket. Two weeks after
configuration, you notice the sink is exporting logs but the GCS bucket storage
cost is unexpectedly high. Which action reduces storage cost without disabling
the sink?

- A) Delete the sink and recreate it with a more restrictive filter
- B) Enable log exclusions to drop the high-volume log types before they reach the sink
- C) Set the GCS bucket storage class to Nearline
- D) Reduce the sink's batch export interval

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Deleting and recreating the sink changes the filter going forward, but all already-exported objects remain in the bucket and continue to incur storage costs; the exclusion approach is less disruptive.
  - C) Changing the storage class to Nearline reduces per-GB storage cost but introduces a 30-day minimum storage duration charge per object; for frequently accessed or frequently deleted log objects, this can increase total cost.
  - D) Cloud Logging sinks do not have a configurable batch export interval that affects cost; sink exports are managed by the logging service and the batch timing is not a user-configurable parameter.

---

### Question 14 (5 points)

You need to monitor a custom application metric: the number of orders processed
per minute. The application runs on GCE and writes this value to its logs as
structured JSON. Which approach makes this metric available in Cloud Monitoring
for alerting?

- A) Install Cloud Profiler on the VM to track the order count
- B) Create a log-based metric using a filter that extracts the order count field
   from the structured log entries
- C) Use Cloud Trace to count spans with the order processing label
- D) Enable Data Access audit logs and filter for order processing API calls

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Profiler analyzes CPU and memory usage in application code; it does not extract business metrics from logs.
  - C) Cloud Trace tracks distributed request latency; it does not count business events or provide a mechanism to define alertable custom metrics from log fields.
  - D) Data Access audit logs capture GCP API calls (reads/writes to GCP services); they do not capture application-level business events written to structured logs.

---

### Question 15 (5 points)

What is the default retention period for logs stored in the `_Default` log bucket
in Cloud Logging?

- A) 7 days
- B) 30 days
- C) 90 days
- D) 400 days

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) 7 days is not the default retention for the `_Default` bucket; this figure does not correspond to any standard Cloud Logging bucket default.
  - C) 90 days is not the default; it can be configured as a custom retention period but is not the out-of-the-box default.
  - D) 400 days is the fixed retention period for the `_Required` log bucket (which stores Admin Activity and System Event audit logs), not the `_Default` bucket.

---

### Question 16 (5 points)

A Cloud Monitoring uptime check is configured to test an HTTPS endpoint every
minute from multiple global regions. The check fails with `CONNECTION_TIMEOUT`
from all regions. The application responds correctly to curl from Cloud Shell.
What is the most likely cause?

- A) The SSL certificate on the endpoint has expired
- B) A firewall rule is blocking inbound traffic from the uptime check IP ranges
   used by Cloud Monitoring
- C) The uptime check interval is too short for the application to respond
- D) Cloud Monitoring uptime checks cannot test HTTPS endpoints

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) An expired SSL certificate would cause `SSL_ERROR` or `CERTIFICATE_EXPIRED` failure, not `CONNECTION_TIMEOUT`; a timeout indicates the TCP connection is not reaching the server.
  - C) Cloud Monitoring uptime checks have a 10-second default timeout, which is far longer than typical web response times; the 1-minute interval is the check frequency, not the timeout.
  - D) Cloud Monitoring uptime checks support HTTP, HTTPS, and TCP protocols; HTTPS is fully supported.

---

### Question 17 (5 points)

You use Cloud Error Reporting to monitor a Node.js application. A new deployment
causes an increase in unhandled exception reports. Which action in Error Reporting
lets you suppress a known, non-critical error while continuing to track new errors?

- A) Create a log exclusion matching the error message pattern
- B) Mute the specific error group in Error Reporting
- C) Increase the alerting policy threshold to ignore low-frequency errors
- D) Disable Error Reporting for the affected service

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) A log exclusion would prevent the error from being ingested into Cloud Logging at all; this could mask the error completely and remove the ability to review it later, which is more destructive than muting.
  - C) Alerting policy thresholds apply to Cloud Monitoring metrics; Error Reporting uses its own notification system separate from Monitoring alerting policies.
  - D) Disabling Error Reporting for the service removes visibility into all errors from that service, not just the known non-critical one.

---

### Question 18 (5 points)

A security team requires that VPC flow logs from all subnets in a project be
retained for 1 year for compliance. VPC flow logs are exported to Cloud Logging
by default with a 30-day retention. What is the correct approach?

- A) Change the `_Default` log bucket retention to 365 days
- B) Create a log sink routing VPC flow logs to a Cloud Storage bucket with a
   365-day object lifecycle, and optionally create a log exclusion to drop them
   from the `_Default` bucket
- C) Enable Admin Activity audit logs with a 365-day retention override
- D) Configure each subnet's flow log sampling rate to 100% to ensure all logs
   are captured before the 30-day expiry

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Changing the `_Default` bucket retention to 365 days would retain ALL logs in that bucket for a year, significantly increasing Cloud Logging storage costs for logs that do not need long retention.
  - C) Admin Activity audit logs are already retained for 400 days in the `_Required` bucket; they are a separate log type from VPC flow logs and the retention is not configurable.
  - D) Sampling rate affects what fraction of flows are logged; it does not extend the storage retention period or prevent expiry after 30 days.

---

### Question 19 (5 points)

Cloud Profiler is enabled on a Java application running on App Engine Standard.
Which two types of profiling data does Cloud Profiler collect by default?

- A) Network throughput and disk I/O
- B) CPU time and heap memory allocation
- C) Request latency and error rate
- D) Log entry count and severity distribution

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Network throughput and disk I/O are OS-level metrics collected by the Ops Agent and surfaced in Cloud Monitoring; they are not profiling dimensions tracked by Cloud Profiler.
  - C) Request latency and error rate are distributed tracing and monitoring metrics tracked by Cloud Trace and Cloud Monitoring respectively; Cloud Profiler focuses on in-process resource consumption.
  - D) Log entry count and severity distribution are Cloud Logging metrics; they describe log volume, not code-level resource consumption within the application.

---

### Question 20 (5 points)

You need to grant a teammate read-only access to view logs and dashboards in
Cloud Monitoring for a single GCP project. Which IAM role provides these
permissions with least privilege?

- A) `roles/monitoring.admin`
- B) `roles/monitoring.viewer`
- C) `roles/logging.admin`
- D) `roles/viewer`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `roles/monitoring.admin` grants full administrative access to Cloud Monitoring including creating, modifying, and deleting alerting policies, dashboards, and notification channels — far more than read-only viewing requires.
  - C) `roles/logging.admin` grants full administrative access to Cloud Logging; it includes the ability to delete log buckets, create sinks, and modify exclusions — not appropriate for a read-only viewer.
  - D) `roles/viewer` is a basic project-level role that grants read access to all GCP resources; while it technically allows viewing logs and metrics, it grants far broader access than a monitoring-specific viewer role and violates least privilege.

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

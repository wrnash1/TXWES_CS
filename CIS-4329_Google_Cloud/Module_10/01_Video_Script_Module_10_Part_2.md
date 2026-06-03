# Video Script: Module 10 — Cloud Operations: Monitoring and Logging (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction to Part 2

Welcome back. In Part 1 we covered Cloud Monitoring — metrics, dashboards, alerts, and
Cloud Logging fundamentals. In Part 2 we go deeper into Cloud Logging — sinks, query
language, and exclusions — then cover Cloud Trace, Cloud Profiler, and Error Reporting.

---

### Section 1: Cloud Logging — Log Sinks

Log sinks export copies of log entries to external destinations. Common use cases:

- Long-term archival in Cloud Storage
- Analytics and querying in BigQuery
- Real-time processing via Pub/Sub
- Aggregation in a Security Information and Event Management (SIEM) system

#### Sink Destinations

| Destination | Use case |
|---|---|
| Cloud Storage bucket | Long-term archival; logs stored as JSON files |
| BigQuery dataset | SQL-based log analytics and reporting |
| Pub/Sub topic | Real-time streaming to external systems or Cloud Functions |
| Log bucket (another project) | Centralized log aggregation across an organization |

#### Creating Log Sinks

```bash
# Create a sink to export all logs to Cloud Storage
gcloud logging sinks create my-gcs-sink \
  storage.googleapis.com/my-audit-log-bucket \
  --log-filter='logName:"cloudaudit.googleapis.com"' \
  --description="Audit log archival to GCS"

# Create a sink to export to BigQuery
gcloud logging sinks create my-bq-sink \
  bigquery.googleapis.com/projects/MY_PROJECT/datasets/my_logs_dataset \
  --log-filter='resource.type="gce_instance"' \
  --use-partitioned-tables

# Create a sink to export to Pub/Sub
gcloud logging sinks create my-pubsub-sink \
  pubsub.googleapis.com/projects/MY_PROJECT/topics/log-stream \
  --log-filter='severity>=ERROR'

# List all sinks
gcloud logging sinks list

# Describe a specific sink
gcloud logging sinks describe my-gcs-sink
```

After creating a sink, GCP creates a service account for the sink. You must grant that
service account write permissions on the destination:

```bash
# Get the sink's service account
SINK_SA=$(gcloud logging sinks describe my-gcs-sink \
  --format="value(writerIdentity)")
echo $SINK_SA

# Grant Storage Object Creator on the destination bucket
gsutil iam ch ${SINK_SA}:roles/storage.objectCreator \
  gs://my-audit-log-bucket
```

---

### Section 2: Log Exclusions

Log exclusions drop matching log entries before they are ingested, reducing storage costs
and noise. They are applied in the log router before logs reach any bucket or sink.

```bash
# Exclude debug-level logs from a specific service
gcloud logging exclusions create exclude-debug-logs \
  --description="Drop DEBUG logs from App Engine" \
  --log-filter='resource.type="gae_app" AND severity=DEBUG'

# List exclusions
gcloud logging exclusions list

# Disable an exclusion (temporarily stop excluding)
gcloud logging exclusions update exclude-debug-logs --disabled
```

Exclusions apply globally across all sinks in the project. An excluded log entry is
permanently dropped — it will not appear in any sink, bucket, or the Logs Explorer.

---

### Section 3: Cloud Logging Query Language

The Logging Query Language (LQL) is used in the Logs Explorer and in sink filters. Key
operators:

```text
resource.type="gce_instance"
AND resource.labels.instance_id="1234567890"
AND severity>=WARNING
AND timestamp>="2024-01-01T00:00:00Z"
```

Common patterns:

```bash
# View logs for a specific GCE instance
gcloud logging read 'resource.type="gce_instance" AND
  resource.labels.instance_id="INSTANCE_ID"' \
  --limit=50 \
  --format=json

# View audit logs for a specific user
gcloud logging read 'logName="projects/MY_PROJECT/logs/cloudaudit.googleapis.com%2Factivity"
  AND protoPayload.authenticationInfo.principalEmail="user@example.com"' \
  --limit=20

# View all ERROR and CRITICAL logs in the last hour
gcloud logging read 'severity>=ERROR AND
  timestamp>="2024-01-15T00:00:00Z"' \
  --freshness=1h \
  --limit=100
```

---

### Section 4: Audit Logs

GCP generates four types of audit logs:

- **Admin Activity logs** — record administrative actions (create/delete/modify
  resources); always enabled; retained 400 days; cannot be disabled
- **Data Access logs** — record data reads and data modification API calls; disabled
  by default (can generate large volume); must be explicitly enabled
- **System Event logs** — record GCP system events (e.g., live migration); always
  enabled; cannot be disabled
- **Policy Denied logs** — record when Cloud Armor or VPC Service Controls deny a
  request; always enabled

```bash
# Enable Data Access audit logs for Cloud Storage
gcloud projects get-iam-policy MY_PROJECT --format=json > policy.json
# Edit policy.json to add auditConfigs for storage.googleapis.com
# Then update the policy:
gcloud projects set-iam-policy MY_PROJECT policy.json
```

For the ACE exam: Admin Activity logs are always on, free, and retained 400 days. Data
Access logs must be explicitly enabled and may incur charges for high volume.

---

### Section 5: Cloud Trace

Cloud Trace is a distributed tracing system that helps you understand latency in your
application. It collects timing data for requests as they travel through services.

Key concepts:

- **Trace** — the complete timeline of a single request across all services
- **Span** — a single operation within a trace (e.g., an RPC call, a database query)
- **Latency analysis** — Cloud Trace automatically analyzes trace data and surfaces
  high-latency requests

For GKE and App Engine applications, Cloud Trace integration is automatic. For other
environments, use the Cloud Trace API or OpenTelemetry:

```bash
# View traces via gcloud (programmatic access)
# Most trace interactions happen in the Console under Cloud Trace

# Install OpenTelemetry in Python for custom instrumentation
pip install opentelemetry-sdk opentelemetry-exporter-gcp-trace
```

Cloud Trace integrates with Cloud Logging — you can click a log entry to see the trace
that generated it, and vice versa.

---

### Section 6: Cloud Profiler

Cloud Profiler continuously profiles your application's CPU usage and memory allocation
with minimal overhead. It is useful for identifying performance hotspots in production
code.

Key characteristics:

- Samples CPU usage and heap allocation continuously
- Statistical profiling — low overhead (less than 1% CPU)
- Supports Go, Java, Node.js, and Python
- Profiles stored in Cloud Profiler for historical analysis

To enable Cloud Profiler in a Python application:

```bash
pip install google-cloud-profiler
```

```python
import googlecloudprofiler
googlecloudprofiler.start(
    service='my-service',
    service_version='1.0.0',
    verbose=3,
)
```

---

### Section 7: Error Reporting

Error Reporting automatically aggregates and counts application crashes and exceptions
from Cloud Logging. It groups similar errors together and alerts you when new error
types appear.

Supported sources:

- App Engine (automatic)
- Cloud Functions (automatic)
- GKE (via structured logging)
- Compute Engine (via Cloud Logging with error format)
- Cloud Run (automatic)

```bash
# View current error groups
gcloud beta error-reporting events list \
  --service=my-service \
  --version=1.0

# Error Reporting is primarily used via the Console
# Navigate to: Cloud Console → Error Reporting
```

---

### Module 10 Summary

Module 10 covered the complete Cloud Operations observability stack:

- **Cloud Monitoring** — metrics, dashboards, uptime checks, alerting, log-based metrics
- **Cloud Logging** — log buckets, sinks (GCS/BigQuery/Pub/Sub), exclusions, audit logs
- **Cloud Trace** — distributed tracing for latency analysis
- **Cloud Profiler** — continuous CPU and memory profiling with low overhead
- **Error Reporting** — automatic exception aggregation and new-error alerting

For the ACE exam: know how to create log sinks, understand audit log types (especially
that Admin Activity logs are always on and free), know how to create alerting policies
with notification channels, and understand that memory metrics on GCE require the Ops
Agent.

Complete the lab, take the quiz, and join the discussion. Module 11 covers Infrastructure
as Code with Cloud Deployment Manager and Terraform.

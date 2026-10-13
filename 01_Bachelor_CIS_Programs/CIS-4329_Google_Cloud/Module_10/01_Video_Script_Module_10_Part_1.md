# Video Script: Module 10 — Cloud Operations: Monitoring and Logging (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 10. I am Professor Nash. Today we cover Cloud Operations — the suite
of observability tools on GCP that helps you monitor, log, trace, and profile your
applications.

Google Cloud Operations was formerly known as "Stackdriver" — you may see that name in
older documentation. The modern product family includes Cloud Monitoring, Cloud Logging,
Cloud Trace, Cloud Profiler, and Error Reporting.

Observability is a significant portion of the ACE exam domain **Ensuring Successful
Operation of a Cloud Solution**. You are expected to configure monitoring, respond to
alerts, query logs, and understand how logs flow to external destinations.

---

### Section 1: Cloud Monitoring Overview

Cloud Monitoring provides visibility into the performance, uptime, and health of your
GCP resources. It collects metrics automatically from GCP services — CPU utilization,
network traffic, request counts, latency — with no additional configuration required.

Key concepts:

- **Metrics** — time-series numeric data points (e.g., `compute.googleapis.com/instance/cpu/utilization`)
- **Workspaces** — organizational unit for monitoring; a workspace can monitor multiple
  GCP projects
- **Dashboards** — customizable views of metrics in charts and scorecards
- **Uptime checks** — synthetic monitors that probe URLs or TCP ports from multiple
  global locations
- **Alerting policies** — define conditions that trigger notifications when metrics
  cross thresholds

#### Metric Types

Cloud Monitoring collects three categories of metrics:

- **GCP metrics** — automatically collected from all GCP services (no agent required)
- **Agent metrics** — collected by the Cloud Monitoring agent installed on GCE VMs;
  provides OS-level metrics (memory, disk, process)
- **Custom metrics** — application-defined metrics written via the Cloud Monitoring API
  or OpenTelemetry

#### Monitoring Agent for GCE

GCE VMs do not report memory utilization or disk utilization by default. Install the
Ops Agent to collect these:

```bash
# Install the Ops Agent on a Debian/Ubuntu GCE VM
curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install
sudo systemctl status google-cloud-ops-agent
```

---

### Section 2: Dashboards

Dashboards aggregate metrics from multiple resources into a single view. You can use
pre-built dashboards (automatically created for GKE, Cloud SQL, App Engine, etc.) or
create custom dashboards.

```bash
# List available dashboards via Cloud Monitoring API
gcloud monitoring dashboards list

# Describe a specific dashboard
gcloud monitoring dashboards describe DASHBOARD_ID
```

Custom dashboards are created in the Console (Cloud Monitoring → Dashboards → Create
Dashboard). Each chart widget supports:

- **Line charts** for time-series metrics
- **Scorecard widgets** for current metric value vs. threshold
- **Table widgets** for multi-resource comparisons

---

### Section 3: Uptime Checks

Uptime checks probe your application from multiple global locations. They verify that
your service is reachable and returning expected responses.

```bash
# Create an uptime check for an HTTP endpoint
gcloud monitoring uptime-checks create http my-uptime-check \
  --display-name="My Web App Uptime" \
  --hostname=www.example.com \
  --path=/health \
  --port=443 \
  --use-ssl \
  --check-interval=60 \
  --timeout=10

# List uptime checks
gcloud monitoring uptime-checks list
```

Uptime checks report from multiple regions simultaneously. GCP considers an endpoint
"down" when a majority of check locations fail.

---

### Section 4: Alerting Policies

Alerting policies define conditions that trigger notifications. They consist of:

- **Condition** — a metric threshold, uptime check failure, or log-based metric
  threshold
- **Notification channels** — where alerts are sent (email, PagerDuty, Slack, Pub/Sub,
  webhook, SMS)
- **Alert documentation** — runbook text included in the notification

```bash
# Create a notification channel (email)
gcloud monitoring channels create \
  --display-name="Ops Team Email" \
  --type=email \
  --channel-labels=email_address=ops@example.com

# List notification channels
gcloud monitoring channels list

# Create an alerting policy via a JSON/YAML file
# (Console is more practical for complex policies, but gcloud supports it)
gcloud monitoring policies create \
  --notification-channels=CHANNEL_ID \
  --policy-from-file=alert-policy.yaml
```

A basic alerting policy YAML structure:

```yaml
displayName: "High CPU Alert"
conditions:
  - displayName: "CPU above 80%"
    conditionThreshold:
      filter: >
        resource.type="gce_instance"
        AND metric.type="compute.googleapis.com/instance/cpu/utilization"
      comparison: COMPARISON_GT
      thresholdValue: 0.8
      duration: 300s
combiner: OR
notificationChannels:
  - projects/MY_PROJECT/notificationChannels/CHANNEL_ID
```

---

### Section 5: Log-Based Metrics

Cloud Monitoring can generate metrics from log entries. This lets you alert on log
patterns — for example, count the number of HTTP 500 errors per minute.

```bash
# Create a log-based metric counting HTTP 500 errors
gcloud logging metrics create http-500-errors \
  --description="Count of HTTP 500 errors" \
  --log-filter='resource.type="gce_instance" AND
    textPayload:"HTTP/1.1 500"'
```

Once created, the log-based metric appears in Cloud Monitoring and can be used in
alerting policies and dashboards just like any other metric.

---

### Section 6: Cloud Logging Overview

Cloud Logging is the centralized log management service for GCP. All GCP services write
logs automatically — you do not need to configure anything to start collecting logs.

Key concepts:

- **Log bucket** — where logs are stored; the default `_Default` bucket retains logs for
  30 days
- **Log sink** — exports logs from Cloud Logging to an external destination
- **Log exclusion** — drops matching log entries before they are ingested (saves cost)
- **Log router** — processes all incoming logs through sinks and exclusions
- **Audit logs** — Admin Activity, Data Access, System Event, and Policy Denied logs

#### Log Buckets and Retention

```bash
# List log buckets in a project
gcloud logging buckets list --location=global

# Create a custom log bucket with 365-day retention
gcloud logging buckets create my-long-term-logs \
  --location=global \
  --retention-days=365 \
  --description="Long-term audit log storage"

# Update retention on the default bucket
gcloud logging buckets update _Default \
  --location=global \
  --retention-days=90
```

---

### Closing — Part 1

In Part 1 we covered:

- Cloud Monitoring: metrics, dashboards, uptime checks, and alerting policies
- The Ops Agent for GCE memory and disk metrics
- Log-based metrics for alerting on log patterns
- Cloud Logging concepts: log buckets, sinks, exclusions, and audit logs

In Part 2 we cover log sinks for routing to BigQuery and Cloud Storage, log queries with
the Logging Query Language, Cloud Trace, Cloud Profiler, and Error Reporting.

See you in Part 2.

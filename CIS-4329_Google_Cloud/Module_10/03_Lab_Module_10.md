# Lab: Module 10 — Cloud Operations: Monitoring and Logging

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Lab Overview

In this lab you will configure Cloud Monitoring and Cloud Logging for a Compute Engine
VM. You will install the Ops Agent, create a dashboard, set up an alerting policy, create
a log sink to export to Cloud Storage, and query logs using the Logging Query Language.

**Estimated time**: 60–75 minutes

**Cost estimate**: Under $1.00 USD if completed and cleaned up within the session

---

### Prerequisites

- A GCP project with billing enabled
- Cloud Shell or gcloud CLI authenticated
- Compute Engine API and Cloud Monitoring API enabled

```bash
gcloud services enable compute.googleapis.com monitoring.googleapis.com logging.googleapis.com
```

---

### Part 1: Create a VM and Install the Ops Agent

#### Task 1.1: Create a Compute Engine VM

```bash
gcloud config set project YOUR_PROJECT_ID

gcloud compute instances create lab10-vm \
  --machine-type=e2-micro \
  --zone=us-central1-a \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --scopes=https://www.googleapis.com/auth/cloud-platform
```

The `--scopes=cloud-platform` flag grants the VM access to Cloud Monitoring and Cloud
Logging APIs.

#### Task 1.2: Install the Ops Agent

SSH into the VM and install the Ops Agent:

```bash
# SSH into the VM
gcloud compute ssh lab10-vm --zone=us-central1-a

# On the VM: install the Ops Agent
curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
sudo bash add-google-cloud-ops-agent-repo.sh --also-install

# Verify the agent is running
sudo systemctl status google-cloud-ops-agent

# Exit the VM
exit
```

#### Task 1.3: Verify Metrics Are Flowing

After installing the Ops Agent, wait 2–3 minutes, then check that memory metrics are
appearing:

```bash
# Query the memory utilization metric (requires gcloud beta)
gcloud monitoring time-series list \
  --filter='metric.type="agent.googleapis.com/memory/percent_used"
    AND resource.labels.instance_id!=""' \
  --project=YOUR_PROJECT_ID
```

Alternatively, open Cloud Console → Monitoring → Metrics Explorer and search for
`agent.googleapis.com/memory/percent_used`.

---

### Part 2: Create a Dashboard and Alerting Policy

#### Task 2.1: Create an Uptime Check

```bash
# Create an uptime check targeting an external URL
# (Using google.com as the target since our VM doesn't serve HTTP)
gcloud monitoring uptime-checks create http lab10-uptime-check \
  --display-name="Lab 10 HTTP Check" \
  --hostname=www.google.com \
  --path=/ \
  --port=443 \
  --use-ssl \
  --check-interval=60 \
  --timeout=10

# List uptime checks
gcloud monitoring uptime-checks list
```

#### Task 2.2: Create a Notification Channel

```bash
# Create an email notification channel
# Replace with your email address
gcloud monitoring channels create \
  --display-name="Lab10 Email Alert" \
  --type=email \
  --channel-labels=email_address=YOUR_EMAIL@example.com

# List notification channels and capture the channel ID
gcloud monitoring channels list
```

Note the channel ID from the output — you will need it for the alerting policy.

#### Task 2.3: Create a Dashboard via the Console

1. Navigate to **Cloud Monitoring** → **Dashboards** → **Create Dashboard**.
2. Name the dashboard `Lab 10 VM Monitor`.
3. Add a **Line Chart** widget with metric `compute.googleapis.com/instance/cpu/utilization`
   filtered to `lab10-vm`.
4. Add a second **Line Chart** with metric `agent.googleapis.com/memory/percent_used`
   filtered to `lab10-vm`.
5. Save the dashboard.

Record the dashboard URL for your submission.

---

### Part 3: Configure Cloud Logging

#### Task 3.1: Create a Cloud Storage Bucket for Log Export

```bash
gsutil mb -l us-central1 gs://YOUR_PROJECT_ID-lab10-logs/
```

#### Task 3.2: Create a Log Sink

```bash
# Create a log sink exporting audit logs to Cloud Storage
gcloud logging sinks create lab10-audit-sink \
  storage.googleapis.com/YOUR_PROJECT_ID-lab10-logs \
  --log-filter='logName:"cloudaudit.googleapis.com%2Factivity"' \
  --description="Audit log export to GCS"

# Get the sink's writer identity
SINK_SA=$(gcloud logging sinks describe lab10-audit-sink \
  --format="value(writerIdentity)")
echo "Sink service account: $SINK_SA"

# Grant the sink's service account write access to the bucket
gsutil iam ch ${SINK_SA}:roles/storage.objectCreator \
  gs://YOUR_PROJECT_ID-lab10-logs/
```

#### Task 3.3: Generate Audit Log Events

Perform some actions that generate audit log entries:

```bash
# Create and immediately delete a firewall rule to generate audit events
gcloud compute firewall-rules create temp-fw-rule \
  --network=default --action=ALLOW --rules=tcp:9999 \
  --source-ranges=10.0.0.0/8

gcloud compute firewall-rules delete temp-fw-rule --quiet

# List recent audit log entries
gcloud logging read \
  'logName="projects/YOUR_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"' \
  --limit=10 \
  --format="table(timestamp,protoPayload.methodName,protoPayload.authenticationInfo.principalEmail)"
```

#### Task 3.4: Verify Export to Cloud Storage

After a few minutes, verify that log files have appeared in the bucket:

```bash
gsutil ls gs://YOUR_PROJECT_ID-lab10-logs/
```

---

### Part 4: Logging Query Language Practice

Run each of the following queries in the **Logs Explorer** (Cloud Console → Logging →
Logs Explorer) and note what you observe:

Query 1 — All ERROR and CRITICAL logs:

```text
severity>=ERROR
```

Query 2 — Logs from the lab10-vm instance:

```text
resource.type="gce_instance"
AND resource.labels.instance_name="lab10-vm"
```

Query 3 — Admin Activity audit logs for the current user:

```text
logName="projects/YOUR_PROJECT_ID/logs/cloudaudit.googleapis.com%2Factivity"
AND protoPayload.methodName:"firewall"
```

Record a screenshot or describe what results each query returns in your submission.

---

### Part 5: Reflection Questions

1. What metrics are available on a GCE VM WITHOUT installing the Ops Agent, and which
   metrics require the Ops Agent?
2. Explain the purpose of the writer identity created with a log sink. What happens if
   you forget to grant it permissions?
3. In the log sink you created, the filter targets `cloudaudit.googleapis.com%2Factivity`
   logs. What type of events does this capture?
4. What is the difference between a log exclusion and a log sink with an inclusion filter?
   If you wanted to reduce logging costs without losing data, which would you use?
5. Why would an alerting policy have a `duration` field set to 5 minutes rather than
   firing immediately when a threshold is crossed?

---

### Part 6: Cleanup

```bash
# Delete the log sink
gcloud logging sinks delete lab10-audit-sink --quiet

# Delete the GCS bucket and its contents
gsutil rm -r gs://YOUR_PROJECT_ID-lab10-logs/

# Delete the uptime check
UPTIME_ID=$(gcloud monitoring uptime-checks list \
  --format="value(name)" | grep lab10)
gcloud monitoring uptime-checks delete $UPTIME_ID --quiet

# Delete the notification channel
CHANNEL_ID=$(gcloud monitoring channels list \
  --filter="displayName='Lab10 Email Alert'" \
  --format="value(name)")
gcloud monitoring channels delete $CHANNEL_ID --quiet

# Delete the VM
gcloud compute instances delete lab10-vm \
  --zone=us-central1-a --quiet
```

---

### Submission Checklist

- Ops Agent installed and memory metrics verified in Cloud Monitoring
- Uptime check created
- Notification channel created
- Dashboard created with CPU and memory charts
- Log sink created and writer identity granted permissions
- Audit log events generated and verified in Logs Explorer
- Export to Cloud Storage verified
- All 4 Logging Query Language queries run with results noted
- All 5 reflection questions answered
- All resources cleaned up

---

### Grading Rubric

| Task | Points |
|---|---|
| Ops Agent installed and metrics flowing | 15 |
| Uptime check and notification channel | 10 |
| Dashboard with 2 metric charts | 15 |
| Log sink created with correct permissions | 20 |
| LQL queries run with results documented | 20 |
| Reflection questions answered | 15 |
| Resources cleaned up | 5 |
| **Total** | **100** |

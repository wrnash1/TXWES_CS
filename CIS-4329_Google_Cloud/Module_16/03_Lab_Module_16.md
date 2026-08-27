# Lab Activity: Module 16 — ACE Exam Preparation and GCP Capstone

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 90–120 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Overview

This capstone lab brings together the major domains of CIS-4329. You will deploy a multi-tier web application on GCP using Compute Engine, Cloud SQL, Cloud Storage, Cloud Run, and Cloud Load Balancing — each with appropriate IAM controls and monitoring. You will then complete an ACE exam scenario exercise applying the two-constraint elimination method to five scenario questions.

---

### Learning Objectives

By completing this lab you will be able to:

- Deploy a Compute Engine VM with a scoped service account and startup script
- Create a Cloud SQL instance and connect to it from a Compute Engine VM via the Cloud SQL Auth Proxy
- Configure a Cloud Storage bucket with a lifecycle policy and IAM controls
- Deploy a containerized API to Cloud Run with IAM-restricted access
- Configure a Cloud Monitoring uptime check and alerting policy
- Apply the two-constraint method to ACE exam scenario questions

---

### Prerequisites

- A GCP project with billing enabled
- Owner or Editor IAM role on the project
- `gcloud` CLI installed and authenticated
- Docker installed (for Part 4 container build)

---

### Part 1: Compute Engine with Service Account (20 minutes)

#### Task 1.1 — Create a service account for the web server

```bash
export PROJECT_ID=$(gcloud config get-value project)

# Create service account
gcloud iam service-accounts create web-sa \
  --display-name="Web Server Service Account"

# Grant Cloud SQL client role (for Cloud SQL Auth Proxy)
gcloud projects add-iam-policy-binding ${PROJECT_ID} \
  --member="serviceAccount:web-sa@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"

# Grant Cloud Storage object viewer on the assets bucket (next task)
# (We will add this after creating the bucket)
```

#### Task 1.2 — Create the web server VM

```bash
gcloud compute instances create web-server \
  --zone=us-central1-a \
  --machine-type=e2-medium \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --service-account=web-sa@${PROJECT_ID}.iam.gserviceaccount.com \
  --scopes=cloud-platform \
  --metadata=startup-script='#!/bin/bash
apt-get update
apt-get install -y nginx
systemctl start nginx
systemctl enable nginx'
```

#### Task 1.3 — Verify the VM is running

```bash
gcloud compute instances list --zones=us-central1-a
gcloud compute ssh web-server --zone=us-central1-a --command="curl -s localhost"
```

Expected: HTML output from the nginx default page.

#### Deliverable 1

Terminal output showing `gcloud compute instances list` with `web-server` in RUNNING status, and the `curl localhost` output confirming nginx is serving.

---

### Part 2: Cloud SQL Instance and Connection (25 minutes)

#### Task 2.1 — Create a Cloud SQL PostgreSQL instance

```bash
gcloud sql instances create app-db \
  --database-version=POSTGRES_14 \
  --tier=db-f1-micro \
  --region=us-central1 \
  --no-backup
```

Note: `db-f1-micro` is the smallest tier — use for lab purposes only. `--no-backup` reduces lab cost.

Wait for the instance to be created (2–4 minutes).

#### Task 2.2 — Create a database and user

```bash
gcloud sql databases create appdb --instance=app-db

gcloud sql users create appuser \
  --instance=app-db \
  --password=LabPassword123
```

#### Task 2.3 — Connect from the VM using Cloud SQL Auth Proxy

SSH to the web server VM:

```bash
gcloud compute ssh web-server --zone=us-central1-a
```

Inside the VM, install the Cloud SQL Auth Proxy and connect:

```bash
# Install the proxy
curl -o cloud-sql-proxy https://storage.googleapis.com/cloud-sql-connectors/cloud-sql-proxy/v2.0.0/cloud-sql-proxy.linux.amd64
chmod +x cloud-sql-proxy

# Get the connection name
# Format: PROJECT_ID:REGION:INSTANCE_NAME
# Example: my-project:us-central1:app-db

# Start the proxy (background)
./cloud-sql-proxy PROJECT_ID:us-central1:app-db &

# Connect with psql
sudo apt-get install -y postgresql-client
psql -h 127.0.0.1 -U appuser -d appdb
```

Inside psql, create a test table:

```sql
CREATE TABLE lab_test (id SERIAL PRIMARY KEY, message TEXT);
INSERT INTO lab_test (message) VALUES ('Cloud SQL connection successful');
SELECT * FROM lab_test;
\q
```

Exit the VM:

```bash
exit
```

#### Deliverable 2

Terminal output showing the `SELECT * FROM lab_test` query result confirming the connection worked.

---

### Part 3: Cloud Storage Bucket with Lifecycle Policy (15 minutes)

#### Task 3.1 — Create a storage bucket

```bash
gsutil mb -l us-central1 gs://${PROJECT_ID}-app-assets
```

#### Task 3.2 — Grant the web server service account read access

```bash
gsutil iam ch \
  serviceAccount:web-sa@${PROJECT_ID}.iam.gserviceaccount.com:roles/storage.objectViewer \
  gs://${PROJECT_ID}-app-assets
```

#### Task 3.3 — Apply a lifecycle policy

Create `lifecycle.json`:

```json
{
  "lifecycle": {
    "rule": [
      {
        "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
        "condition": {"age": 30}
      },
      {
        "action": {"type": "Delete"},
        "condition": {"age": 365}
      }
    ]
  }
}
```

Apply the policy:

```bash
gsutil lifecycle set lifecycle.json gs://${PROJECT_ID}-app-assets
gsutil lifecycle get gs://${PROJECT_ID}-app-assets
```

#### Task 3.4 — Test access from the VM

```bash
# Upload a test file
echo "test asset" | gsutil cp - gs://${PROJECT_ID}-app-assets/test.txt

# Verify the web server VM's service account can read the file
gcloud compute ssh web-server --zone=us-central1-a \
  --command="curl -H 'Authorization: Bearer $(gcloud auth print-access-token)' \
  https://storage.googleapis.com/storage/v1/b/${PROJECT_ID}-app-assets/o/test.txt?alt=media"
```

#### Deliverable 3

Terminal output showing `gsutil lifecycle get` confirming two rules and the file read confirming service account access.

---

### Part 4: Cloud Run API Deployment (20 minutes)

#### Task 4.1 — Create a simple containerized API

Create a directory `hello-api/` with the following files:

`hello-api/app.py`:

```python
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/message')
def message():
    return jsonify({"message": "Hello from Cloud Run"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

`hello-api/requirements.txt`:

```text
flask==2.3.0
gunicorn==21.2.0
```

`hello-api/Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
```

#### Task 4.2 — Build and push the container image

```bash
cd hello-api

# Build and push to Artifact Registry (or Container Registry)
gcloud builds submit --tag gcr.io/${PROJECT_ID}/hello-api:v1

cd ..
```

#### Task 4.3 — Deploy to Cloud Run (authenticated)

```bash
gcloud run deploy hello-api \
  --image=gcr.io/${PROJECT_ID}/hello-api:v1 \
  --region=us-central1 \
  --platform=managed \
  --no-allow-unauthenticated
```

#### Task 4.4 — Test the authenticated endpoint

```bash
# Get the Cloud Run service URL
export SERVICE_URL=$(gcloud run services describe hello-api \
  --region=us-central1 --format="value(status.url)")

# Call with authentication (using your identity token)
curl -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  ${SERVICE_URL}/health
```

Expected output: `{"status": "ok"}`

#### Deliverable 4

Terminal output showing the authenticated Cloud Run health check returning `{"status": "ok"}`.

---

### Part 5: Cloud Monitoring Uptime Check (10 minutes)

#### Task 5.1 — Create an uptime check for the web server

Get the web server's external IP:

```bash
gcloud compute instances describe web-server --zone=us-central1-a \
  --format="value(networkInterfaces[0].accessConfigs[0].natIP)"
```

Create an uptime check (via Cloud Console — uptime checks are not fully supported in gcloud CLI):

1. Navigate to Cloud Monitoring → Uptime Checks → Create Uptime Check
2. Protocol: HTTP
3. Resource type: URL
4. Hostname: [web server external IP]
5. Path: /
6. Check frequency: 1 minute
7. Click Save

After saving, create an alerting policy:

1. In the uptime check, click "Create Alerting Policy"
2. Set alert when uptime check fails from any location for 1 minute
3. Add a notification channel (email) if desired
4. Save the policy

#### Deliverable 5

Screenshot of the Cloud Monitoring uptime check showing green/passing status for the web server.

---

### Part 6: ACE Exam Scenario Exercise (10 minutes)

For each scenario, apply the two-constraint method: identify the primary constraint, eliminate wrong answers, then select the correct answer with a one-sentence justification.

#### Scenario A

A company needs to run a stateful application that requires a PostgreSQL database with 2 TB of data and custom stored procedures. The application must be highly available across two zones. What GCP services should they use?

Options:

1. Cloud Spanner + GKE
2. Bigtable + Compute Engine
3. Cloud SQL (PostgreSQL) with High Availability configuration + GKE
4. Firestore + Cloud Run

Write your primary constraint, elimination, and answer.

#### Scenario B

An engineer wants to ensure that all log entries with severity ERROR from a production project are automatically exported to a Cloud Storage bucket for 90-day retention and analysis. What is the minimum configuration required?

Options:

1. Enable Cloud Trace and configure a trace export to Cloud Storage
2. Create a log sink in Cloud Logging with filter `severity=ERROR` targeting the Cloud Storage bucket; set a retention policy on the bucket
3. Create a Cloud Monitoring alert on error log count; configure the alert notification to write to Cloud Storage
4. Enable audit logging for all data access events and export to Cloud Storage

Write your primary constraint, elimination, and answer.

#### Scenario C

A GCP project has VMs that need to communicate with each other privately but must not be accessible from the internet. All existing VMs have external IP addresses. What is the most effective long-term solution?

Options:

1. Create firewall rules denying all ingress from 0.0.0.0/0
2. Create a new VPC with no external IPs assigned (`--no-address` flag on all future VMs), migrate workloads to the new VPC, and use Internal HTTP(S) Load Balancers for internal service communication
3. Remove the external IPs from existing VMs using `gcloud compute instances delete-access-config`
4. Set an Organization Policy `compute.vmExternalIpAddress` to prevent new VMs from having external IPs

Write your primary constraint, elimination, and answer.

---

### Deliverables Summary

| Deliverable | Description |
|---|---|
| Deliverable 1 | VM running status + nginx curl output |
| Deliverable 2 | Cloud SQL psql query result |
| Deliverable 3 | Lifecycle policy confirmation + service account access test |
| Deliverable 4 | Cloud Run authenticated health check response |
| Deliverable 5 | Screenshot: Cloud Monitoring uptime check passing |
| Deliverable 6 | Written ACE scenario answers with two-constraint analysis |

Submit all deliverables as a single document via Canvas LMS.

---

### Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Compute Engine (Part 1) | 15 | VM running; nginx confirmed; service account correctly assigned |
| Cloud SQL (Part 2) | 20 | Instance created; connection via proxy confirmed; query result shown |
| Cloud Storage (Part 3) | 15 | Bucket created; lifecycle policy applied; service account access confirmed |
| Cloud Run (Part 4) | 20 | Service deployed without public access; authenticated call succeeds |
| Cloud Monitoring (Part 5) | 15 | Uptime check configured; screenshot shows passing status |
| ACE Exam Scenarios (Part 6) | 15 | Two-constraint method applied; correct answers with justification |
| **Total** | **100** | |

---

## Part 9 — Challenge Exercise

### Challenge 1: Shared VPC for Centralized Network Control

Set up a Shared VPC architecture where a host project controls the network and a service project deploys workloads — demonstrating the cross-project IAM and network delegation pattern tested on the ACE exam.

1. Enable the Shared VPC API in both projects:

```bash
export HOST_PROJECT_ID=YOUR_HOST_PROJECT_ID
export SERVICE_PROJECT_ID=YOUR_SERVICE_PROJECT_ID

gcloud services enable compute.googleapis.com \
  --project=${HOST_PROJECT_ID}
gcloud services enable compute.googleapis.com \
  --project=${SERVICE_PROJECT_ID}
```

1. Enable Shared VPC on the host project and attach the service project:

```bash
# Enable Shared VPC hosting on the host project (requires Organization Admin or Shared VPC Admin)
gcloud compute shared-vpc enable ${HOST_PROJECT_ID}

# Attach the service project to the host project
gcloud compute shared-vpc associated-projects add ${SERVICE_PROJECT_ID} \
  --host-project=${HOST_PROJECT_ID}
```

1. Grant the service project's Compute Engine default service account the Network User role in the host project so it can use host project subnets:

```bash
SERVICE_PROJECT_NUMBER=$(gcloud projects describe ${SERVICE_PROJECT_ID} \
  --format='value(projectNumber)')

gcloud projects add-iam-policy-binding ${HOST_PROJECT_ID} \
  --member="serviceAccount:${SERVICE_PROJECT_NUMBER}-compute@developer.gserviceaccount.com" \
  --role="roles/compute.networkUser"
```

1. Create a VM in the service project that uses the host project's shared subnet:

```bash
# List shared subnets visible from the service project
gcloud compute networks subnets list-usable \
  --project=${SERVICE_PROJECT_ID}

# Create a VM in the service project using the shared VPC subnet
gcloud compute instances create shared-vpc-vm \
  --project=${SERVICE_PROJECT_ID} \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --subnet=projects/${HOST_PROJECT_ID}/regions/us-central1/subnetworks/default \
  --no-address
```

1. Verify the VM was created in the service project but uses the host project network:

```bash
gcloud compute instances describe shared-vpc-vm \
  --project=${SERVICE_PROJECT_ID} \
  --zone=us-central1-a \
  --format="value(networkInterfaces[0].subnetwork)"
```

The output should show the host project's subnet path.

### Challenge 2: Cloud Armor Security Policy with Geo-Block

Configure a Cloud Armor security policy on an external HTTP(S) load balancer that blocks traffic from a specific country and allows only the corporate IP range — implementing the access control pattern tested on the ACE exam.

1. Create a backend service and external HTTP(S) load balancer (simplified for lab):

```bash
export PROJECT_ID=$(gcloud config get-value project)

# Create a backend bucket (simpler than a VM backend for this challenge)
gsutil mb -l us-central1 gs://${PROJECT_ID}-armor-test
echo "<h1>Cloud Armor Test</h1>" | gsutil cp - gs://${PROJECT_ID}-armor-test/index.html
gsutil iam ch allUsers:roles/storage.objectViewer gs://${PROJECT_ID}-armor-test

gcloud compute backend-buckets create armor-backend \
  --gcs-bucket-name=${PROJECT_ID}-armor-test \
  --enable-cdn

gcloud compute url-maps create armor-url-map \
  --default-backend-bucket=armor-backend

gcloud compute target-http-proxies create armor-http-proxy \
  --url-map=armor-url-map

gcloud compute forwarding-rules create armor-forwarding-rule \
  --global \
  --target-http-proxy=armor-http-proxy \
  --ports=80
```

1. Create a Cloud Armor security policy:

```bash
gcloud compute security-policies create lab16-armor-policy \
  --description="Lab 16 geo-block policy"
```

1. Add a geo-block rule to deny traffic from a specific country (using CN as an example):

```bash
gcloud compute security-policies rules create 1000 \
  --security-policy=lab16-armor-policy \
  --expression="origin.region_code == 'CN'" \
  --action=deny-403 \
  --description="Block traffic from CN"
```

1. Add an allow rule for a specific IP range (simulating a corporate office):

```bash
gcloud compute security-policies rules create 500 \
  --security-policy=lab16-armor-policy \
  --src-ip-ranges="203.0.113.0/24" \
  --action=allow \
  --description="Allow corporate office range"
```

1. Update the default rule to deny all traffic not matched by higher-priority rules:

```bash
gcloud compute security-policies rules update 2147483647 \
  --security-policy=lab16-armor-policy \
  --action=deny-403
```

1. Attach the security policy to the backend bucket:

```bash
gcloud compute backend-buckets update armor-backend \
  --security-policy=lab16-armor-policy
```

1. List all rules to verify the policy is configured correctly:

```bash
gcloud compute security-policies describe lab16-armor-policy \
  --format="table(rules[].priority,rules[].action,rules[].description)"
```

### Reflection Questions

1. In Challenge 1, the Shared VPC model centralizes network control in the host project while workloads run in service projects. Explain two operational advantages this architecture provides over giving each team their own independent VPC, and describe one trade-off or complexity it introduces compared to fully independent project VPCs.

2. In Challenge 2, the Cloud Armor rules are evaluated in priority order (lower number = higher priority). A request arrives from IP address `203.0.113.50` in China (region code `CN`). Trace the policy evaluation: which rule matches first, what action is taken, and does the geo-block rule (priority 1000) or the allow rule (priority 500) determine the outcome? Explain why Cloud Armor rule priority order is critical to get correct in production security policies.

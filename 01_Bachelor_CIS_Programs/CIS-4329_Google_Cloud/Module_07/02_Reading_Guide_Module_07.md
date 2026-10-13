# Reading Guide: Module 07 — Cloud Run and Serverless Computing

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

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This reading guide covers GCP's serverless compute platform: Cloud Run, Cloud
Functions, App Engine, Eventarc, and Cloud Tasks. Serverless services are
increasingly tested on the ACE exam as they represent the modern direction of
application deployment on GCP.

**Estimated Reading Time:** 50–60 minutes

---

## Section 1 — Cloud Run

### 1.1 Architecture

Cloud Run is GCP's serverless container platform for running stateless HTTP
workloads. It is built on Knative and runs on Google's managed infrastructure.

Deployment model:

- You build a container image and push it to Artifact Registry or Container
  Registry
- You deploy the image to Cloud Run as a service
- Cloud Run manages instances, networking, and TLS termination
- The service gets a stable HTTPS URL: `https://SERVICE-HASH-REGION.a.run.app`

### 1.2 Revisions and Traffic Splitting

Every `gcloud run deploy` creates a new immutable revision. Traffic can be split
across revisions for canary deployments.

```bash
# Deploy a service (creates first revision)
gcloud run deploy my-api \
  --image=REGION-docker.pkg.dev/PROJECT/repo/my-api:v1 \
  --region=us-central1 \
  --allow-unauthenticated

# Deploy new version (creates second revision)
gcloud run deploy my-api \
  --image=REGION-docker.pkg.dev/PROJECT/repo/my-api:v2 \
  --region=us-central1 \
  --no-traffic   # Don't send traffic to new revision yet

# Canary: 10% to v2
gcloud run services update-traffic my-api \
  --region=us-central1 \
  --to-revisions=my-api-v2=10,my-api-v1=90
```

### 1.3 Configuration Parameters

| Parameter | Description | Default |
|---|---|---|
| `--cpu` | vCPU allocated per instance | 1 |
| `--memory` | Memory per instance | 512Mi |
| `--concurrency` | Max concurrent requests per instance | 80 |
| `--max-instances` | Maximum number of instances | 1000 |
| `--min-instances` | Warm instances to reduce cold starts | 0 |
| `--timeout` | Max request duration | 300s |
| `--port` | Port the container listens on | 8080 |

### 1.4 Authentication

Cloud Run services can be:

- **Publicly accessible**: `--allow-unauthenticated` — anyone can invoke
- **Authenticated only**: Requires a valid Google identity token in the
  Authorization header; used for internal service-to-service calls

```bash
# Invoke an authenticated service using a service account token
TOKEN=$(gcloud auth print-identity-token)
curl -H "Authorization: Bearer $TOKEN" \
  https://my-service-hash-uc.a.run.app/endpoint
```

### 1.5 VPC Connector

To access VPC resources (Cloud SQL, Redis, private VMs) from Cloud Run, use
a Serverless VPC Access connector:

```bash
# Create a VPC connector
gcloud compute networks vpc-access connectors create my-connector \
  --region=us-central1 \
  --network=default \
  --range=10.8.0.0/28

# Deploy Cloud Run with VPC access
gcloud run deploy my-service \
  --image=... \
  --region=us-central1 \
  --vpc-connector=my-connector \
  --vpc-egress=private-ranges-only
```

---

## Section 2 — Cloud Functions

### 2.1 Gen 1 vs. Gen 2

| Feature | Gen 1 | Gen 2 |
|---|---|---|
| Infrastructure | Proprietary GCF runtime | Cloud Run + Eventarc |
| Concurrency | 1 request per instance | Up to 1000 concurrent requests |
| Max timeout | 540 seconds (9 min) | 3600 seconds (60 min) |
| Max memory | 8 GiB | 32 GiB |
| Traffic splitting | No | Yes (like Cloud Run) |
| Event triggers | Direct bindings | Via Eventarc |
| Preferred for new work | No | Yes |

### 2.2 Trigger Types

#### HTTP trigger

Function is invoked by an HTTP request (GET, POST, etc.).

```python
# main.py — HTTP trigger function
import functions_framework

@functions_framework.http
def hello_world(request):
    return "Hello, World!", 200
```

#### Background event trigger (Gen 1) / Eventarc trigger (Gen 2)

Function is invoked in response to a GCP event.

```python
# main.py — Storage event trigger
import functions_framework

@functions_framework.cloud_event
def process_upload(cloud_event):
    data = cloud_event.data
    bucket = data["bucket"]
    name = data["name"]
    print(f"New file: gs://{bucket}/{name}")
```

### 2.3 Deployment

```bash
# Gen 2 HTTP function
gcloud functions deploy hello-fn \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=hello_world \
  --trigger-http \
  --allow-unauthenticated

# Gen 2 Storage trigger
gcloud functions deploy storage-fn \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=process_upload \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=BUCKET_NAME" \
  --service-account=fn-sa@PROJECT_ID.iam.gserviceaccount.com
```

---

## Section 3 — App Engine

### 3.1 Standard vs. Flexible

| Feature | Standard | Flexible |
|---|---|---|
| Container type | Sandbox (not Docker) | Docker container on GCE |
| Scale to zero | Yes | No (min 1 instance) |
| Startup time | Milliseconds | Minutes |
| Supported runtimes | Fixed list (Python, Java, Go, etc.) | Any via Dockerfile |
| OS access | Restricted | Full container |
| Pricing when idle | $0 | Min 1 VM cost |

### 3.2 app.yaml

App Engine is configured via `app.yaml`:

```yaml
runtime: python311
instance_class: F2
automatic_scaling:
  min_instances: 0
  max_instances: 10
  target_cpu_utilization: 0.6
env_variables:
  DB_HOST: "10.0.0.1"
handlers:
  - url: /static
    static_dir: static/
  - url: /.*
    script: auto
```

### 3.3 Services and Versions

App Engine supports multiple services (formerly "modules") within one
application:

```bash
# Deploy to a named service
gcloud app deploy service-api.yaml

# Deploy to the default service
gcloud app deploy app.yaml

# Split traffic
gcloud app services set-traffic default \
  --splits=v2=90,v1=10 \
  --split-by=random

# Stop an old version (stops its billing)
gcloud app versions stop v1 --service=default
```

---

## Section 4 — Eventarc

### 4.1 Event Flow

```text
Event Source → Eventarc → Destination
(Cloud Storage, Pub/Sub, Audit Logs)    (Cloud Run, Cloud Functions Gen 2)
```

### 4.2 Trigger Configuration

```bash
# Create a trigger for Cloud Storage → Cloud Run
gcloud eventarc triggers create gcs-trigger \
  --location=us-central1 \
  --destination-run-service=my-processor \
  --destination-run-region=us-central1 \
  --event-filters="type=google.cloud.storage.object.v1.finalized" \
  --event-filters="bucket=my-bucket" \
  --service-account=eventarc-sa@PROJECT_ID.iam.gserviceaccount.com

# Create a trigger for Audit Log event (any API call)
gcloud eventarc triggers create audit-trigger \
  --location=us-central1 \
  --destination-run-service=audit-logger \
  --destination-run-region=us-central1 \
  --event-filters="type=google.cloud.audit.log.v1.written" \
  --event-filters="serviceName=compute.googleapis.com" \
  --event-filters="methodName=v1.compute.instances.insert" \
  --service-account=eventarc-sa@PROJECT_ID.iam.gserviceaccount.com
```

### 4.3 CloudEvents Format

Eventarc delivers events in the CloudEvents format (CNCF standard). The event
arrives at the Cloud Run service as an HTTP POST with:

- `Content-Type: application/cloudevents+json`
- Structured event payload in the request body

---

## Section 5 — Cloud Tasks

### 5.1 Queue and Task Model

A Cloud Tasks **queue** holds tasks waiting to be executed. Each **task** specifies:

- A target URL (Cloud Run, App Engine, or external HTTPS)
- An HTTP method and body
- An optional schedule time (future delivery)
- Retry configuration

### 5.2 Creating Tasks

```bash
# Create a task queue
gcloud tasks queues create my-queue \
  --location=us-central1

# Create a task targeting a Cloud Run service
gcloud tasks create-http-task \
  --queue=my-queue \
  --location=us-central1 \
  --url=https://my-service-hash-uc.a.run.app/process \
  --method=POST \
  --body-content='{"order_id": "12345"}' \
  --header=Content-Type:application/json \
  --oidc-service-account-email=tasks-sa@PROJECT_ID.iam.gserviceaccount.com

# Schedule a task for the future (ISO 8601 format)
gcloud tasks create-http-task \
  --queue=my-queue \
  --location=us-central1 \
  --url=https://my-service-hash-uc.a.run.app/remind \
  --schedule-time=2026-12-31T23:00:00Z \
  --method=POST
```

### 5.3 Cloud Tasks vs. Pub/Sub

| Criteria | Use Cloud Tasks | Use Pub/Sub |
|---|---|---|
| Exactly one target | Yes | No (fan-out) |
| Future scheduling | Yes | No |
| Rate limiting | Yes (configurable) | No |
| Multiple subscribers | No | Yes |
| Best for | Task queues, deferred work | Event streaming, fan-out |

---

## Key Terms Glossary

| Term | Definition |
|---|---|
| Cloud Run | Serverless container platform for stateless HTTP workloads |
| Revision | Immutable snapshot of a Cloud Run service deployment |
| Traffic splitting | Routing percentages of requests to different revisions |
| Concurrency | Number of simultaneous requests handled by one Cloud Run instance |
| Cold start | Latency when a new instance must be created for a request |
| Cloud Functions | FaaS offering for event-driven single functions |
| Gen 2 | Cloud Functions built on Cloud Run; higher concurrency, longer timeout |
| App Engine Standard | Sandbox PaaS; scale to zero; fixed runtimes |
| App Engine Flexible | Docker-based PaaS; custom runtimes; always-on |
| Eventarc | Managed event routing from GCP services to Cloud Run / CF Gen 2 |
| CloudEvents | CNCF standard event format used by Eventarc |
| Cloud Tasks | Managed task queue with scheduling, rate limiting, and retry |
| VPC connector | Serverless VPC Access for reaching private resources from Cloud Run |

---

## ACE Exam Focus Areas — Module 07

- Identify when Cloud Run is the correct choice vs. GKE, Cloud Functions, or
  App Engine.
- Describe the difference between Cloud Functions Gen 1 and Gen 2.
- Explain App Engine Standard vs. Flexible and when each applies.
- Explain what Eventarc is and which services it routes events to.
- Distinguish Cloud Tasks from Pub/Sub for a described messaging scenario.
- Explain traffic splitting in Cloud Run and App Engine.
- Describe what min-instances and max-instances control in Cloud Run.

---

## Further Reading

- Cloud Run: cloud.google.com/run/docs
- Cloud Functions: cloud.google.com/functions/docs
- App Engine: cloud.google.com/appengine/docs
- Eventarc: cloud.google.com/eventarc/docs
- Cloud Tasks: cloud.google.com/tasks/docs
- Serverless VPC Access: cloud.google.com/vpc/docs/serverless-vpc-access

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud Run: Deploying Container Images**
<https://cloud.google.com/run/docs/deploying>
Complete guide to deploying services on Cloud Run including traffic splitting,
revision management, min/max instance configuration, and VPC connector setup.

**2. Google Cloud Skills Boost — Serverless Cloud Run Development**
<https://www.cloudskillsboost.google/focuses/21058>
Hands-on lab covering Cloud Run service deployment, traffic splitting between
revisions, and Eventarc trigger configuration for event-driven serverless
architectures.

**3. Google Cloud Documentation — Choosing an App Engine Environment**
<https://cloud.google.com/appengine/docs/the-appengine-environments>
Official comparison of App Engine Standard versus Flexible environments
covering runtime support, scaling behavior, pricing model, and guidance on
which to use for specific workload requirements.

# Reading Guide: Module 07 — Cloud Run and Serverless Computing

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

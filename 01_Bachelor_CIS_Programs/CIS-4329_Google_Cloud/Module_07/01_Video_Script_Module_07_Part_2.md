# Video Script: Module 07 — Cloud Run and Serverless Computing (Part 2 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

## Segment 1 — Recap and Agenda (1 minute)

Welcome back. In Part 1 we covered Cloud Run, Cloud Functions generations, and
App Engine environments. In Part 2 we cover:

- Eventarc for event-driven serverless architectures
- Cloud Tasks for asynchronous work queues
- Serverless design patterns
- Console and gcloud CLI walkthrough
- ACE exam strategy for serverless questions

---

## Segment 2 — Eventarc (3 minutes)

### What is Eventarc?

Eventarc is GCP's managed event routing service. It routes events from GCP
services (and custom sources) to Cloud Run, Cloud Functions Gen 2, GKE, and
Workflows.

Instead of building custom Pub/Sub subscriptions and routing logic, Eventarc
provides a declarative way to say: "When this event happens in this GCP service,
trigger this Cloud Run service."

### Event Sources

Eventarc can receive events from:

- **Direct event sources**: Cloud Storage, Pub/Sub, Firestore, BigQuery,
  Artifact Registry, Cloud Audit Logs, and more
- **Custom sources**: Custom events published via the Eventarc API
- **Pub/Sub topics**: Any message published to a Pub/Sub topic

### Creating Eventarc Triggers

```bash
# Trigger a Cloud Run service when a file is uploaded to Cloud Storage
gcloud eventarc triggers create storage-trigger \
  --location=us-central1 \
  --destination-run-service=my-processor \
  --destination-run-region=us-central1 \
  --event-filters="type=google.cloud.storage.object.v1.finalized" \
  --event-filters="bucket=my-upload-bucket" \
  --service-account=eventarc-sa@PROJECT_ID.iam.gserviceaccount.com

# Trigger a Cloud Run service from a Pub/Sub topic
gcloud eventarc triggers create pubsub-trigger \
  --location=us-central1 \
  --destination-run-service=my-processor \
  --destination-run-region=us-central1 \
  --event-filters="type=google.cloud.pubsub.topic.v1.messagePublished" \
  --transport-topic=my-topic \
  --service-account=eventarc-sa@PROJECT_ID.iam.gserviceaccount.com

# List triggers
gcloud eventarc triggers list --location=us-central1
```

**ACE Exam Tip:** Eventarc replaces the direct trigger mechanism used in Cloud
Functions Gen 1. For Gen 2 functions and Cloud Run, use Eventarc triggers. The
event format follows the CloudEvents specification.

---

## Segment 3 — Cloud Tasks (2 minutes)

### What is Cloud Tasks?

Cloud Tasks is a fully managed service for asynchronous task execution. You
enqueue tasks — each task targets an HTTP endpoint (Cloud Run, App Engine,
or any URL) — and Cloud Tasks delivers them reliably, with retry on failure,
deduplication, and rate limiting.

Use cases:

- Decouple a user-facing API from slow backend processing
- Rate-limit calls to external APIs
- Guarantee at-least-once task delivery
- Schedule tasks to run at a future time

### Cloud Tasks vs. Pub/Sub

Both handle message passing, but they differ:

| Feature | Cloud Tasks | Pub/Sub |
|---|---|---|
| Delivery | Exactly-once targeting | Fan-out to multiple subscribers |
| Scheduling | Supports future scheduled delivery | Deliver immediately |
| Rate limiting | Built-in rate control | No built-in rate limiting |
| Explicit targeting | One specific endpoint per task | Subscriber pulls or is pushed |

**ACE Exam Tip:** Use Cloud Tasks when you need scheduled, rate-limited, or
exactly-targeted task delivery. Use Pub/Sub for fan-out messaging where multiple
subscribers process the same message.

---

## Segment 4 — Serverless Design Patterns (3 minutes)

### Pattern 1 — Event-Driven Image Processing

A user uploads a photo to Cloud Storage. Cloud Storage emits an event. Eventarc
routes it to a Cloud Run service that resizes and watermarks the image.

```text
User → Cloud Storage → Eventarc trigger → Cloud Run (resize service)
                                               ↓
                                         Cloud Storage (processed/)
```

### Pattern 2 — Decoupled API and Background Processing

A web API receives an order. It immediately returns a 202 Accepted response
while enqueuing the order processing to Cloud Tasks. Cloud Tasks invokes a
Cloud Run worker that processes the order asynchronously.

```text
User → Cloud Run API → Cloud Tasks queue → Cloud Run worker
                              ↓
                    (retry on failure, rate limiting)
```

### Pattern 3 — Scheduled Batch Processing

A CronJob-like pattern using Cloud Scheduler + Cloud Tasks + Cloud Run:

```text
Cloud Scheduler → Pub/Sub topic → Cloud Run (fan-out task creator)
                                        ↓
                               Cloud Tasks (one task per item)
                                        ↓
                              Cloud Run (processor)
```

### Pattern 4 — Fan-out Event Processing

A Pub/Sub topic receives analytics events. Multiple Cloud Functions subscribe
to process the events in different ways simultaneously:

```text
Client → Pub/Sub topic
              ├── Cloud Function: write to BigQuery
              ├── Cloud Function: update Firestore counters
              └── Cloud Run: send real-time notifications
```

---

## Segment 5 — Console and gcloud CLI Walkthrough (4 minutes)

### Cloud Run

```bash
# Deploy a new Cloud Run service
gcloud run deploy my-service \
  --image=gcr.io/PROJECT_ID/my-image:latest \
  --region=us-central1 \
  --platform=managed \
  --concurrency=80 \
  --max-instances=10 \
  --min-instances=0 \
  --memory=512Mi \
  --cpu=1 \
  --timeout=300 \
  --allow-unauthenticated

# Update an existing service (creates new revision)
gcloud run services update my-service \
  --region=us-central1 \
  --memory=1Gi \
  --max-instances=20

# Traffic splitting (canary deployment)
gcloud run services update-traffic my-service \
  --region=us-central1 \
  --to-revisions=my-service-00002-abc=10,LATEST=90

# Roll back to a previous revision
gcloud run services update-traffic my-service \
  --region=us-central1 \
  --to-revisions=my-service-00001-xyz=100

# View logs
gcloud run services logs read my-service --region=us-central1
```

### Cloud Functions

```bash
# Deploy an HTTP function (Gen 2)
gcloud functions deploy my-function \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=handle_request \
  --trigger-http \
  --allow-unauthenticated \
  --memory=256MiB \
  --timeout=60s

# List functions
gcloud functions list --gen2 --region=us-central1

# Describe a function
gcloud functions describe my-function \
  --gen2 --region=us-central1

# View function logs
gcloud functions logs read my-function \
  --gen2 --region=us-central1

# Delete a function
gcloud functions delete my-function \
  --gen2 --region=us-central1 --quiet
```

### App Engine

```bash
# Initialize App Engine in a project
gcloud app create --region=us-central1

# Deploy (reads app.yaml from current directory)
gcloud app deploy

# Browse the deployed app
gcloud app browse

# List versions of a service
gcloud app versions list

# Split traffic between versions
gcloud app services set-traffic default \
  --splits=v2=0.9,v1=0.1 \
  --split-by=random

# Stop a version (stops billing for it)
gcloud app versions stop v1

# Delete a version
gcloud app versions delete v1 --quiet
```

---

## Segment 6 — ACE Exam Tips for Serverless (1 minute)

Key serverless patterns on the ACE exam:

- **Cloud Run**: Stateless HTTP containers; scale to zero; good for variable
  traffic. Best when you have an existing Docker container to deploy.
- **Cloud Functions**: Event-driven single functions; less overhead than Cloud
  Run for simple triggers. Gen 2 is preferred; Gen 2 is built on Cloud Run.
- **App Engine Standard**: Variable traffic web apps that need scale-to-zero
  and fast startup. No custom runtimes.
- **App Engine Flexible**: Custom Docker containers or runtimes; always-on
  minimum billing; slower scaling.
- **Eventarc**: The modern event routing layer for Cloud Run and Cloud
  Functions Gen 2.
- **Cloud Tasks vs. Pub/Sub**: Tasks = exactly-targeted, rate-limited,
  schedulable. Pub/Sub = fan-out messaging.

---

## Summary — Module 07

Across both parts we covered:

- Cloud Run: serverless containers, revisions, traffic splitting, concurrency
- Cloud Functions Gen 1 vs. Gen 2 and key differences
- App Engine Standard vs. Flexible environments
- Eventarc: event routing from GCP services to Cloud Run and Cloud Functions
- Cloud Tasks: asynchronous, rate-limited, exactly-targeted task queues
- Serverless design patterns: event-driven image processing, decoupled APIs,
  scheduled batch, fan-out event processing
- Console and gcloud CLI for all three serverless services

The lab will have you deploy a Cloud Run service, write a Cloud Function, and
connect them with an Eventarc trigger.

---

End of Part 2 — Module 07

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/run/docs | cloud.google.com/functions/docs

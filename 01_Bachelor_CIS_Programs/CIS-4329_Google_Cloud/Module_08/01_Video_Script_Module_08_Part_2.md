# Video Script — Module 08, Part 2

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Functions, Platform Selection, and gcloud Commands

### Estimated Duration: 10–12 minutes

---

## Introduction to Part 2

Welcome back to Module 08. In Part 1 we covered Cloud Run and App Engine Standard and Flexible environments. In Part 2 we cover Cloud Functions for event-driven workloads, work through a platform selection decision matrix, and walk through the gcloud commands you will use in the lab.

---

## Section 1: Cloud Functions

**[SHOW SLIDE: Event sources pointing to Cloud Function which executes code and returns result]**

Cloud Functions is GCP's function-as-a-service platform. You deploy a single function and it executes in response to an event.

### Cloud Functions Generations

GCP has two generations of Cloud Functions:

- Cloud Functions 1st gen: older, simpler, lower maximum instances
- Cloud Functions 2nd gen: built on Cloud Run infrastructure, higher maximum execution time (up to 60 minutes), supports more concurrent instances

For new deployments, use 2nd gen unless you have a specific reason to use 1st gen.

### Trigger Types

| Trigger | Description |
|---|---|
| HTTP trigger | Function runs when an HTTPS request hits its endpoint |
| Pub/Sub trigger | Function runs when a message is published to a Pub/Sub topic |
| Cloud Storage trigger | Function runs when an object is created, updated, or deleted |
| Firestore trigger | Function runs when a Firestore document is written |
| Cloud Scheduler trigger | Function runs on a cron schedule via Pub/Sub |

### Example: Cloud Storage Trigger

```bash
gcloud functions deploy process-new-file \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=process_file \
  --trigger-bucket=my-input-bucket
```

This deploys a Python function that runs whenever a new file is finalized in `my-input-bucket`.

### Example: HTTP Trigger

```bash
gcloud functions deploy my-http-function \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=handle_request \
  --trigger-http \
  --allow-unauthenticated
```

### Cloud Functions Limits

| Limit | Value |
|---|---|
| Maximum execution time | 60 minutes (2nd gen) |
| Maximum memory | 32 GB (2nd gen) |
| Maximum concurrency per instance | 1 (1st gen), up to 1000 (2nd gen) |
| Supported runtimes | Node.js, Python, Go, Java, Ruby, PHP, .NET |

### When to Use Cloud Functions vs. Cloud Run

Cloud Functions is best when:

- The workload is triggered by a specific GCP event (Pub/Sub, Cloud Storage, Firestore)
- The function is short-lived and lightweight (data transformation, notification, webhook handler)
- You do not need a container image — you just want to upload source code

Cloud Run is better when:

- You need a persistent HTTP service rather than event-triggered
- You need custom system libraries via a container
- You have complex multi-file applications
- You need higher concurrency or longer execution

---

## Section 2: Serverless Platform Selection Decision Matrix

**[SHOW SLIDE: Decision table with checkmarks for each platform]**

The ACE exam tests platform selection across these four services. Use this matrix:

| Requirement | Cloud Functions | Cloud Run | App Engine Standard | App Engine Flexible |
|---|---|---|---|---|
| Event-driven (Pub/Sub, GCS) | Best | Yes (via Pub/Sub push) | No | No |
| Container-based | No | Yes | No | Yes |
| Any programming language | No | Yes | No | Yes |
| Scale to zero | Yes | Yes | Yes | No |
| Supported framework (Flask, Django) | No | Yes | Yes | Yes |
| Long-running background processes | No | No | No | Yes |
| Minimum operational overhead | Yes | Medium | Low | Medium |

### Quick Selection Rules

Rule 1: Event from Pub/Sub, Cloud Storage, or Firestore, short execution → Cloud Functions

Rule 2: Containerized HTTP service, any language, scale-to-zero → Cloud Run

Rule 3: Python/Java/Node.js web app, no special dependencies, simplest deployment → App Engine Standard

Rule 4: Custom runtime, background threads, need filesystem access, no scale-to-zero requirement → App Engine Flexible

Rule 5: The exam says "no server management" plus "container" → Cloud Run. "No server management" plus "source code" plus supported framework → App Engine Standard.

---

## Section 3: gcloud Commands for Cloud Run and App Engine

**[SHOW CONSOLE: Cloud Shell with deploy and traffic management commands]**

### Cloud Run Commands

Deploy a service:

```bash
gcloud run deploy SERVICE_NAME \
  --image=IMAGE_URL \
  --region=REGION \
  --platform=managed
```

List services:

```bash
gcloud run services list --region=REGION
```

Describe a service:

```bash
gcloud run services describe SERVICE_NAME \
  --region=REGION
```

Update traffic:

```bash
gcloud run services update-traffic SERVICE_NAME \
  --to-revisions=REVISION=PERCENTAGE \
  --region=REGION
```

Send all traffic to latest revision:

```bash
gcloud run services update-traffic SERVICE_NAME \
  --to-latest \
  --region=REGION
```

Delete a service:

```bash
gcloud run services delete SERVICE_NAME \
  --region=REGION
```

### App Engine Commands

Deploy an application:

```bash
gcloud app deploy app.yaml
```

List versions:

```bash
gcloud app versions list
```

Migrate traffic to a specific version:

```bash
gcloud app services set-traffic default \
  --splits=VERSION_ID=1 \
  --migrate
```

Stop a version:

```bash
gcloud app versions stop VERSION_ID
```

Browse the deployed application:

```bash
gcloud app browse
```

---

## Module 08 Summary

**[SHOW SLIDE: Summary bullet list]**

Let's wrap up Module 08. GCP serverless compute spans Cloud Functions, Cloud Run, and App Engine. Cloud Functions is event-driven — it executes in response to Pub/Sub messages, Cloud Storage events, or HTTP triggers. Cloud Run runs containers with scale-to-zero and request-driven billing, supporting any language and runtime. App Engine Standard provides the simplest deployment for supported language frameworks with scale-to-zero. App Engine Flexible runs Docker containers on VMs without scale-to-zero.

For the ACE exam: containers plus serverless equals Cloud Run. Events plus lightweight function equals Cloud Functions. Existing web framework plus no custom dependencies equals App Engine Standard. Custom runtime plus background threads equals App Engine Flexible.

Complete the lab, take the quiz, and post to the discussion. Module 09 covers Cloud SQL and Cloud Spanner — managed relational databases.

---

End of Part 2 — Module 08

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

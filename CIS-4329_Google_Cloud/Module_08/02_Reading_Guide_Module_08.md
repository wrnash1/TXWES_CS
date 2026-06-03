# Reading Guide — Module 08

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Run, App Engine, and Cloud Functions — Serverless Compute

### Certification Target: Google Cloud Associate Cloud Engineer

---

## Introduction

GCP's serverless compute portfolio — Cloud Functions, Cloud Run, and App Engine — is one of the highest-frequency ACE exam topic areas. The exam consistently presents scenarios requiring you to choose the correct platform. This reading guide provides a comprehensive comparison of all three platforms, their scaling behavior, deployment commands, and the key selection criteria that determine the correct answer on the exam.

---

## 1. Platform Comparison

### Serverless Compute Overview

| Feature | Cloud Functions | Cloud Run | App Engine Standard | App Engine Flexible |
|---|---|---|---|---|
| Deployment unit | Single function | Container image | Application source + app.yaml | Docker container |
| Scale to zero | Yes | Yes | Yes | No |
| Any language | No (8 runtimes) | Yes | No (6 runtimes) | Yes |
| Container required | No | Yes | No | Yes |
| Event-driven triggers | Yes (native) | Yes (via Pub/Sub push) | Via task queues | Via task queues |
| Maximum execution time | 60 min (2nd gen) | 60 min | 10 min (standard) | Unlimited |
| Background processes | No | No | No | Yes |
| Filesystem access | /tmp only | Writable /tmp | Restricted | Full |
| Billing unit | Per invocation | Per 100ms CPU/memory | Per instance-hour | Per VM-hour |

### Scale-to-Zero Behavior

Scale-to-zero means the platform shuts down all instances when there are no active requests. You pay nothing during idle periods. The tradeoff is a cold start delay when the first request arrives after an idle period.

App Engine Flexible does NOT scale to zero. It always keeps at least one instance running, meaning continuous billing even with zero traffic.

---

## 2. Cloud Run

### Key Concepts

A Cloud Run service is a deployed container that receives HTTP requests. Each deployment creates a new revision — an immutable snapshot of the container image and configuration.

```text
Cloud Run Service
├── Revision 1 (old) — 0% traffic
├── Revision 2 (stable) — 90% traffic
└── Revision 3 (new) — 10% traffic (canary)
```

### gcloud run Commands

| Command | Description |
|---|---|
| `gcloud run deploy SVC --image=IMG --region=R` | Deploy or update a service |
| `gcloud run services list --region=R` | List services |
| `gcloud run services describe SVC --region=R` | Service details |
| `gcloud run services update-traffic SVC --to-revisions=REV=PCT --region=R` | Traffic split |
| `gcloud run services update-traffic SVC --to-latest --region=R` | Send all traffic to latest |
| `gcloud run services delete SVC --region=R` | Delete service |
| `gcloud run revisions list --service=SVC --region=R` | List revisions |

### Concurrency and Scaling

Default concurrency: 80 requests per instance. Set to 1 for CPU-intensive tasks. Use `--min-instances=1` to prevent cold starts at the cost of continuous billing for one warm instance.

```bash
gcloud run deploy my-service \
  --image=IMAGE \
  --concurrency=1 \
  --max-instances=100 \
  --min-instances=1 \
  --region=us-central1
```

---

## 3. App Engine

### Standard Environment app.yaml

```yaml
runtime: python39
service: default

automatic_scaling:
  min_instances: 0
  max_instances: 10
  target_cpu_utilization: 0.65
```

### App Engine gcloud Commands

| Command | Description |
|---|---|
| `gcloud app deploy app.yaml` | Deploy application |
| `gcloud app deploy app.yaml --no-promote` | Deploy without shifting traffic |
| `gcloud app services list` | List services |
| `gcloud app versions list` | List all versions |
| `gcloud app services set-traffic default --splits=V=1 --migrate` | Route all traffic to version V |
| `gcloud app versions stop VERSION` | Stop a version |
| `gcloud app versions delete VERSION` | Delete a version |
| `gcloud app browse` | Open service URL in browser |

### Traffic Splitting

```bash
gcloud app services set-traffic default \
  --splits=v1=0.9,v2=0.1 \
  --split-by=random
```

`--split-by` options: `random` (per-request), `ip` (sticky by client IP), `cookie` (sticky by session).

---

## 4. Cloud Functions

### Trigger Types

| Trigger | When it fires |
|---|---|
| HTTP | HTTPS request to function URL |
| Pub/Sub | Message published to a topic |
| Cloud Storage | Object created, updated, finalized, or deleted |
| Firestore | Document created, updated, or deleted |
| Cloud Scheduler | Cron-based schedule via Pub/Sub |

### Deployment Command

```bash
gcloud functions deploy FUNCTION_NAME \
  --gen2 \
  --runtime=python311 \
  --region=REGION \
  --source=. \
  --entry-point=FUNCTION_HANDLER \
  --trigger-bucket=BUCKET_NAME
```

---

## 5. Platform Selection Decision Rules

Rule 1: Event from Cloud Storage, Pub/Sub, or Firestore + short execution + no container → Cloud Functions

Rule 2: Container + serverless + any language + scale-to-zero → Cloud Run

Rule 3: Source code + supported framework (Flask, Django, Spring) + no custom system libs → App Engine Standard

Rule 4: Custom runtime + background threads + no scale-to-zero requirement → App Engine Flexible

Rule 5: "No server management" eliminates Compute Engine and GKE. Use the other rules to choose among the serverless options.

---

## 6. ACE Exam Tips

1. Scale-to-zero is the most tested behavioral difference. Standard and Cloud Run scale to zero; Flexible does not. "Pay only when requests are being handled" means Standard or Cloud Run, never Flexible.

2. Cloud Run requires a container. If a scenario describes a simple Python Flask app with no custom dependencies, App Engine Standard is simpler — no Dockerfile needed.

3. Traffic splitting is built into both Cloud Run and App Engine. Know both commands: `gcloud run services update-traffic` and `gcloud app services set-traffic`.

4. Cloud Functions is the only native event-driven option. "Run code when a file is uploaded" or "process each Pub/Sub message" → Cloud Functions.

5. App Engine Flexible is rarely the right ACE exam answer. Only choose it when the scenario requires custom system libraries, unlimited background processes, or full filesystem access.

6. `--no-promote` in App Engine deploys a version without routing traffic to it — useful for staging before promotion.

7. Cloud Run services can be triggered by events via Pub/Sub push or Eventarc. This is more complex than Cloud Functions but valid for containerized event-driven workloads.

8. Cloud Functions 2nd gen is built on Cloud Run. For the ACE exam, treat them as separate services and select based on use case, not implementation.

---

## 7. Study Checklist

- [ ] Explain the difference between Cloud Run, App Engine Standard, App Engine Flexible, and Cloud Functions and state when to use each
- [ ] Describe what scale-to-zero means and which platforms support it
- [ ] State the deployment unit for each platform (container, source code, function)
- [ ] List the Cloud Functions trigger types and give a use case for each
- [ ] Write a minimal app.yaml for App Engine Standard from memory
- [ ] Explain Cloud Run traffic splitting and write the gcloud command to route 10% of traffic to a new revision
- [ ] Apply the platform selection rules to a scenario you have not seen before
- [ ] Complete the Module 08 lab
- [ ] Take the Module 08 quiz
- [ ] Post your Module 08 discussion response

---

End of Reading Guide — Module 08

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

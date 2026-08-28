# Reading Guide — Module 08

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

---

## 9. Supplemental Resources

**1. Google Cloud Documentation — Cloud SQL Overview**
<https://cloud.google.com/sql/docs/introduction>
Official introduction to Cloud SQL covering supported database engines (MySQL, PostgreSQL, SQL Server), instance tiers, high availability configuration, read replicas, and connection methods including the Cloud SQL Auth Proxy.

**2. Google Cloud Skills Boost — Cloud SQL for PostgreSQL: Qwik Start**
<https://www.cloudskillsboost.google/focuses/937>
Hands-on lab walking through creating a Cloud SQL for PostgreSQL instance, connecting via Cloud Shell, creating databases and tables, and running queries — directly applicable to the ACE exam scenario questions.

**3. Google Cloud Documentation — Firestore Data Model**
<https://firebase.google.com/docs/firestore/data-model>
Comprehensive guide to the Firestore document-collection data model, including nested collections, document size limits, and the distinction between Native mode and Datastore mode that is a recurring ACE exam topic.

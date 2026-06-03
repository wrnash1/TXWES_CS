# Video Script — Module 08, Part 1

## CIS-4329: Google Cloud Platform | Texas Wesleyan University

### Topic: Cloud Run and App Engine — Serverless Compute

### Estimated Duration: 12–14 minutes

---

## Introduction

Welcome to Module 08. I'm Professor Nash, and today we cover serverless compute on GCP: Cloud Run and App Engine. Serverless means you deploy your code or container and GCP handles everything else — servers, operating systems, scaling, load balancing. You pay only for the resources consumed during request processing.

These two services are consistently tested on the ACE exam. The exam presents a scenario and asks you to choose the right compute platform. By the end of this module you will be able to distinguish Cloud Run from App Engine Standard from App Engine Flexible, understand their scaling behavior, and deploy to each.

---

## Section 1: The Serverless Compute Spectrum

**[SHOW SLIDE: Spectrum from most control to least control: Compute Engine, GKE, Cloud Run, App Engine, Cloud Functions]**

GCP has multiple compute options on a spectrum from maximum control to maximum abstraction:

- Compute Engine: you manage everything — OS, patches, scaling, software
- GKE: you manage node pools and Kubernetes objects; Google manages the control plane
- Cloud Run: you provide a container image; Google manages everything else
- App Engine: you provide code in a supported framework; Google manages the runtime, scaling, and infrastructure
- Cloud Functions: you provide a single function; Google manages everything for event-driven invocations

Today we focus on Cloud Run and App Engine — the two primary serverless web platforms.

---

## Section 2: Cloud Run

**[SHOW SLIDE: Container image arrow to Cloud Run service arrow to HTTPS endpoint with auto-scaling and scale-to-zero]**

Cloud Run is GCP's fully managed container runtime. You push a container image and Cloud Run provides an HTTPS endpoint, handles load balancing, and scales automatically.

### Key Cloud Run Characteristics

- Container-based: you provide any container image — no language restrictions
- Scales to zero: when no requests are incoming, Cloud Run shuts down all instances and you pay nothing
- Request-driven billing: you pay per 100 milliseconds of CPU and memory used during active request handling
- HTTPS by default: every Cloud Run service gets an HTTPS endpoint automatically
- Concurrency: each instance handles up to 80 concurrent requests by default (configurable)

### Deploying to Cloud Run

```bash
gcloud run deploy my-service \
  --image=gcr.io/PROJECT_ID/my-app:latest \
  --region=us-central1 \
  --platform=managed \
  --allow-unauthenticated
```

The `--allow-unauthenticated` flag makes the service publicly accessible. For internal services, omit this flag — all requests must be authenticated with an OIDC token.

After deployment, Cloud Run returns the service URL. Retrieve it:

```bash
gcloud run services describe my-service \
  --region=us-central1 \
  --format="value(status.url)"
```

### Revisions and Traffic Splitting

Every deployment creates a new revision — an immutable snapshot of the container image and configuration. By default, 100% of traffic goes to the latest revision.

Cloud Run allows weighted traffic splitting across revisions for canary deployments:

```bash
gcloud run services update-traffic my-service \
  --to-revisions=NEW_REVISION=10,STABLE_REVISION=90 \
  --region=us-central1
```

This routes 10% of requests to the new revision for testing. Once validated, promote it:

```bash
gcloud run services update-traffic my-service \
  --to-latest \
  --region=us-central1
```

### Concurrency

The concurrency setting controls how many simultaneous requests one Cloud Run instance handles:

- Default: 80 (efficient for most HTTP services)
- Set to 1 for CPU-intensive workloads that need dedicated processing per request
- Higher values reduce cold starts by keeping fewer instances active

```bash
gcloud run deploy my-service \
  --image=IMAGE \
  --concurrency=1 \
  --region=us-central1
```

### When to Use Cloud Run

Use Cloud Run when:

- Your workload is containerized and stateless
- Traffic is unpredictable or bursty including scale-to-zero periods
- You want to run any programming language or custom runtime
- You want serverless without language restrictions

---

## Section 3: App Engine Standard Environment

**[SHOW SLIDE: App Engine diagram showing web app to app.yaml to gcloud app deploy to automatic HTTPS scaling monitoring]**

App Engine is GCP's original platform-as-a-service. You deploy code in a supported language framework and App Engine handles everything else.

### App Engine Standard vs. Flexible

| Feature | Standard | Flexible |
|---|---|---|
| Runtime | Python, Java, Node.js, Go, PHP, Ruby (specific versions) | Any language via Docker |
| Scale to zero | Yes | No — minimum 1 instance always running |
| Cold starts | Yes (short) | Yes (slower VM startup) |
| Filesystem access | Restricted sandbox | Full access via container |
| Background threads | Limited | Full support |
| Billing | Per request | Per VM instance-hour |

### App Engine Standard Deployment

App Engine Standard applications require an `app.yaml` configuration file:

```yaml
runtime: python39
service: default

automatic_scaling:
  min_instances: 0
  max_instances: 10
  target_cpu_utilization: 0.65
```

Deploy the application:

```bash
gcloud app deploy app.yaml
```

App Engine creates a new version and promotes it to serve 100% of traffic by default.

Deploy without promoting:

```bash
gcloud app deploy app.yaml --no-promote
```

This creates a new version that receives no traffic — useful for testing before promotion.

### App Engine Traffic Migration

App Engine supports traffic splitting across versions. Migrate all traffic to a new version:

```bash
gcloud app services set-traffic default \
  --splits=v2=1 \
  --migrate
```

Gradual migration:

```bash
gcloud app services set-traffic default \
  --splits=v1=0.9,v2=0.1 \
  --split-by=random
```

### App Engine Flexible Environment

Flexible environment uses Docker containers running on Compute Engine VMs. Use Flexible when:

- Your application requires custom system libraries not available in the Standard sandbox
- You need long-running background processes
- You need direct filesystem access
- You are using a language or runtime version not supported by Standard

The key limitation: Flexible always keeps at least one instance running, which means continuous billing even with zero traffic.

---

## Closing — Part 1

To summarize Part 1: Cloud Run runs containers with full scale-to-zero, request-driven billing, and traffic splitting via revisions. App Engine Standard runs code in predefined language runtimes with scale-to-zero and the simplest deployment experience. App Engine Flexible runs Docker containers on VMs but never scales to zero. The exam tests platform selection based on container vs. code, scale-to-zero requirements, and custom runtime needs.

In Part 2 we will cover Cloud Functions for event-driven workloads, compare all three serverless platforms in a decision matrix, and walk through the gcloud commands for the lab.

---

End of Part 1 — Module 08

Course: CIS-4329 Google Cloud Platform | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/learn

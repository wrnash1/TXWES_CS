# Video Script: Module 07 — Cloud Run and Serverless Computing (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 15 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

<!-- TEXAS WESLEYAN VENDOR VIDEO EMBED -->
<div class="video-container-card" style="background: #ffffff; border: 1px solid #cbd5e1; border-radius: 10px; margin: 24px 0; overflow: hidden; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.06);">
  <div style="background: #1b365d; color: #ffffff; padding: 12px 20px; display: flex; justify-content: space-between; align-items: center;">
    <div>
      <span style="background: #d9a74a; color: #0f172a; font-weight: 800; font-size: 11px; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Vendor Video Lecture</span>
      <strong style="margin-left: 10px; font-size: 14px;">freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer &bull; Module 07</strong>
    </div>
    <a href="https://www.youtube.com/watch?v=UGRDM86MBIQ" target="_blank" rel="noopener noreferrer" style="color: #cbd5e1; font-size: 12px; text-decoration: none; font-weight: 600;">↗ Open in YouTube</a>
  </div>
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; background: #0f172a;">
    <iframe src="https://www.youtube.com/embed/UGRDM86MBIQ" title="freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer" style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  </div>
  <div style="padding: 12px 20px; background: #f8fafc; border-top: 1px solid #e2e8f0; font-size: 13px; color: #475569;">
    <strong>Recommended Viewing:</strong> <em>freeCodeCamp / Andrew Brown &bull; Google Cloud Associate Cloud Engineer</em>. This vendor-aligned lecture stream reinforces this module's theoretical principles, certification blueprints, and hands-on laboratory benchmarks.
  </div>
</div>
<!-- END TEXAS WESLEYAN VENDOR VIDEO EMBED -->

---

## Segment 1 — Introduction (1 minute)

Welcome to Module 07. This module covers GCP's serverless compute offerings:
Cloud Run, Cloud Functions, App Engine, and the event-driven architecture
patterns that connect them.

Serverless computing removes infrastructure management from the developer.
You focus on code; Google handles servers, scaling, and availability. This
module covers some of the most rapidly evolving GCP services and represents
the modern direction of cloud application deployment.

In Part 1 we cover Cloud Run architecture, Cloud Functions generations, and
App Engine fundamentals. In Part 2 we cover Eventarc, Cloud Tasks, serverless
patterns, and the CLI walkthroughs.

---

## Segment 2 — Cloud Run (5 minutes)

### What is Cloud Run?

Cloud Run is GCP's fully managed serverless container platform. You package
your application in a container, deploy it to Cloud Run, and Google handles
the infrastructure — auto-scaling from zero to thousands of instances, with
no cluster to manage.

Key characteristics:

- Runs any containerized workload (HTTP-serving applications)
- Scales to zero when there is no traffic — no charges when idle
- Scales up automatically based on incoming requests
- Request concurrency: each instance handles multiple requests simultaneously
- Billing: per 100ms of CPU and memory when actively processing requests

### Cloud Run Architecture

A Cloud Run deployment consists of:

- **Service**: The deployed application; has a stable HTTPS URL
- **Revision**: An immutable snapshot of a specific container image and
  configuration. Every deployment creates a new revision.
- **Traffic splitting**: Route a percentage of traffic to different revisions
  for canary deployments or rollbacks

```bash
# Deploy a container to Cloud Run
gcloud run deploy hello-service \
  --image=gcr.io/google-samples/hello-app:1.0 \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated

# View service details
gcloud run services describe hello-service \
  --region=us-central1

# List all Cloud Run services
gcloud run services list --region=us-central1
```

### Cloud Run Configuration

Key configuration parameters:

- **CPU**: 0.08 to 8 vCPU; default is 1
- **Memory**: 128 MiB to 32 GiB; default is 512 MiB
- **Concurrency**: Number of concurrent requests per instance; default is 80
- **Max instances**: Caps the number of instances to control cost or database
  connection limits
- **Min instances**: Keeps warm instances to eliminate cold starts
- **Timeout**: Maximum request duration; default 300 seconds, max 3600 seconds
- **VPC connector**: Route traffic to a VPC for private resource access

### Cloud Run vs. GKE

| Feature | Cloud Run | GKE |
|---|---|---|
| Infrastructure management | None (Google manages) | Node pools (Standard) or none (Autopilot) |
| Container support | HTTP-serving only | Any container |
| Scaling | 0 to N, request-based | Pod count, HPA |
| Billing | Per request | Per node (Standard) or per pod (Autopilot) |
| Complexity | Low | High |

**ACE Exam Tip:** Cloud Run is ideal when: you have an HTTP/HTTPS service,
traffic is variable or unpredictable, you want zero infrastructure management,
and you want zero cost when idle. GKE is better for complex multi-service
architectures, non-HTTP workloads, or stateful applications.

---

## Segment 3 — Cloud Functions (4 minutes)

### What are Cloud Functions?

Cloud Functions is GCP's Function as a Service (FaaS) offering. You deploy
a single function — a small piece of code — and it runs in response to events
or HTTP requests. No container required; just write code.

### Generation 1 vs. Generation 2

#### Cloud Functions Gen 1

- Deployed in GCP's original Functions infrastructure
- Supports HTTP triggers and background event triggers
- Limited runtime concurrency (one request per instance)
- Supported languages: Node.js, Python, Go, Java, Ruby, .NET, PHP
- Maximum function timeout: 540 seconds

#### Cloud Functions Gen 2

- Built on Cloud Run under the hood
- **Higher concurrency**: Multiple concurrent requests per instance
- **Longer timeouts**: Up to 3600 seconds (60 minutes)
- **Larger instances**: Up to 16 GiB memory, 4 vCPU
- **Traffic splitting**: Canary deployments like Cloud Run
- **Eventarc integration**: Broader range of trigger sources
- Recommended for new deployments

```bash
# Deploy a Gen 2 HTTP function (Python)
gcloud functions deploy hello-function \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=hello_world \
  --trigger-http \
  --allow-unauthenticated

# Deploy a Gen 2 function triggered by Cloud Storage
gcloud functions deploy process-upload \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=process_file \
  --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
  --trigger-event-filters="bucket=my-upload-bucket"
```

**ACE Exam Tip:** Cloud Functions Gen 2 is built on Cloud Run. For the ACE exam,
know that Gen 2 supports higher concurrency, longer timeouts, and Eventarc.
When a question asks which is newer/preferred, the answer is Gen 2.

---

## Segment 4 — App Engine (3 minutes)

### What is App Engine?

App Engine is GCP's original PaaS offering — a fully managed platform for
deploying web applications without managing infrastructure.

### Standard vs. Flexible Environment

#### Standard Environment

- Runs in a sandbox with restricted access to OS
- Scales to zero when idle (no traffic = no cost)
- Fast startup (milliseconds)
- Supported runtimes: Python, Java, Go, Node.js, PHP, Ruby (specific versions)
- Each request runs in an isolated sandbox instance
- Ideal for web apps, APIs, and backends with variable traffic

#### Flexible Environment

- Runs in Docker containers on Compute Engine VMs
- Always has at least one instance running (minimum 1)
- Supports any language via custom Docker containers
- More access to OS and hardware
- Slower scaling (minutes)
- Higher minimum cost (always-on)

| Feature | Standard | Flexible |
|---|---|---|
| Scale to zero | Yes | No |
| Startup time | Milliseconds | Minutes |
| Custom runtimes | Limited | Full (Docker) |
| Minimum cost | $0 when idle | At least 1 VM always running |
| OS access | Restricted sandbox | Full container |

**ACE Exam Tip:** App Engine Standard is for variable traffic applications
that benefit from scaling to zero. Flexible is for custom runtimes or
applications needing OS-level access. Know that Flexible has a minimum of one
instance always running.

### App Engine Concepts

- **Application**: One App Engine app per GCP project
- **Service**: A logical component of the app (formerly "module")
- **Version**: An immutable deployment of a service
- **Traffic splitting**: Route percentages to different versions

```bash
# Deploy an App Engine app
gcloud app deploy app.yaml

# List all versions
gcloud app versions list

# Route traffic (canary deployment: 90% to v1, 10% to v2)
gcloud app services set-traffic default \
  --splits=v1=9,v2=1 \
  --split-by=random
```

---

## Summary — Part 1

In Part 1 we covered:

- Cloud Run: serverless containers, revisions, traffic splitting, key config
- Cloud Functions: Gen 1 vs. Gen 2 differences
- App Engine: Standard vs. Flexible environments, services, versions, traffic
  splitting

In Part 2 we cover Eventarc, Cloud Tasks, serverless design patterns, and
CLI walkthroughs for all three services.

See you in Part 2.

---

End of Part 1 — Module 07

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

Certification Target: Google Cloud Associate Cloud Engineer

Reference: cloud.google.com/run/docs

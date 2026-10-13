# Quiz: Module 07 — Cloud Run and Serverless Computing

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points.
This quiz covers Cloud Run, Cloud Functions, App Engine, Eventarc, Cloud Tasks,
and serverless design patterns.

---

## Question 1

A development team has a containerized Python web service that receives HTTP
requests. Traffic is highly variable — near zero overnight and peaks at 500
requests per second during business hours. The team wants zero cost when idle
and no infrastructure to manage. Which service is the best fit?

- A) Compute Engine with autoscaling managed instance group
- B) GKE Standard cluster with Horizontal Pod Autoscaler
- C) Cloud Run with min-instances=0
- D) App Engine Flexible environment

**Correct Answer:** C

**Explanation:** Cloud Run is designed exactly for this scenario — it is a
serverless container platform that scales to zero (billing drops to $0 when
there is no traffic) and scales up automatically to handle bursts. No
infrastructure management is required. App Engine Flexible (option D) always
maintains at least one running instance, which incurs ongoing cost.

---

## Question 2

Which statement correctly describes the difference between Cloud Functions
Generation 1 and Generation 2?

- A) Gen 1 supports Python; Gen 2 supports all languages via Docker containers
- B) Gen 2 is built on Cloud Run, supports higher concurrency (up to 1000
     requests per instance), and allows timeouts up to 60 minutes
- C) Gen 1 is the newer, recommended generation; Gen 2 was deprecated in 2024
- D) Gen 2 functions cannot be triggered by HTTP requests

**Correct Answer:** B

**Explanation:** Cloud Functions Gen 2 is built on Cloud Run under the hood
and inherits Cloud Run's capabilities: up to 1000 concurrent requests per
instance (vs. 1 for Gen 1), timeouts up to 3600 seconds (60 minutes vs. Gen 1's
9 minutes), and traffic splitting. Gen 2 is the recommended generation for new
deployments. Gen 1 is still supported but is not the preferred option.

---

## Question 3

An App Engine application serves web traffic with very unpredictable load.
Occasionally there is no traffic for several hours. The application must cost
as little as possible and uses a supported Python runtime. Which App Engine
environment should be used?

- A) Flexible environment with min-instances=0
- B) Standard environment
- C) Flexible environment with custom Docker container
- D) Standard environment with always-on configuration

**Correct Answer:** B

**Explanation:** App Engine Standard environment scales to zero when there is
no traffic, costing nothing during idle periods. It has fast startup times
(milliseconds) and supports Python as a standard runtime. App Engine Flexible
always maintains at least one running instance, incurring minimum VM cost even
when idle. Standard is the correct choice for cost optimization with variable
traffic using a supported runtime.

---

## Question 4

You deploy a Cloud Run service with `--concurrency=80` and `--max-instances=10`.
At peak load, 1,000 concurrent requests arrive simultaneously. How many instances
will Cloud Run create?

- A) 1,000 instances (one per request)
- B) 13 instances (1,000 / 80, rounded up)
- C) 10 instances (bounded by max-instances)
- D) 80 instances (equal to the concurrency setting)

**Correct Answer:** C

**Explanation:** Cloud Run will attempt to scale to handle 1,000 concurrent
requests at 80 per instance, which would require approximately 13 instances.
However, `--max-instances=10` caps the scaling at 10 instances. The 10 instances
can handle 800 concurrent requests at the concurrency limit; the remaining 200
requests will either queue, experience latency, or receive 429/503 errors
depending on the timeout configuration.

---

## Question 5

What is an Eventarc trigger used for?

- A) Scheduling Cloud Run services to run at specific times
- B) Routing events from GCP services (such as Cloud Storage or Pub/Sub)
     to Cloud Run or Cloud Functions Gen 2 destinations
- C) Providing rate limiting for Cloud Run services
- D) Monitoring Cloud Run services and sending alerts to Cloud Monitoring

**Correct Answer:** B

**Explanation:** Eventarc is GCP's managed event routing service. It listens
for events from GCP sources (Cloud Storage object creation, Audit Log writes,
Pub/Sub messages, etc.) and routes them to Cloud Run services or Cloud Functions
Gen 2. It uses the CloudEvents standard format for event payloads. Scheduling
is handled by Cloud Scheduler; rate limiting by Cloud Armor or Cloud Tasks.

---

## Question 6

A team needs to process user-submitted tasks asynchronously. Each task must be
delivered to exactly one processing endpoint. Some tasks should be delayed by
up to 30 minutes before execution. The system must not overwhelm the endpoint
with more than 5 task executions per second. Which GCP service should they use?

- A) Cloud Pub/Sub with a push subscription
- B) Cloud Tasks with rate limit configuration
- C) Eventarc with a Cloud Storage trigger
- D) Cloud Scheduler with a Pub/Sub topic

**Correct Answer:** B

**Explanation:** Cloud Tasks provides exactly the required capabilities: tasks
target a single specific endpoint (not fan-out), tasks can be scheduled for
future delivery (up to 30-day delay), and the queue supports configurable
dispatch rate (`max-concurrent-dispatches` and dispatch rate settings). Pub/Sub
(option A) is for fan-out messaging to multiple subscribers and does not support
per-task scheduling.

---

## Question 7

A Cloud Run service needs to connect to a private Cloud SQL instance in the
same VPC. The Cloud Run service has no external IP. What enables this
connectivity?

- A) VPC peering between Google's managed network and the customer VPC
- B) A Serverless VPC Access connector configured on the subnet
- C) A Cloud VPN tunnel from Cloud Run to the VPC
- D) Opening a public IP on the Cloud SQL instance

**Correct Answer:** B

**Explanation:** Serverless VPC Access connectors allow Cloud Run services
(and Cloud Functions, App Engine Standard) to send traffic to resources in
a VPC using private IP addresses. The connector bridges Google's serverless
infrastructure with the customer's VPC network, enabling access to Cloud SQL
private IPs, Memorystore, and other private resources without requiring public
IPs.

---

## Question 8

A Cloud Run service has two revisions: `my-service-v1` receiving 100% of traffic
and `my-service-v2` receiving 0%. You want to test v2 with 5% of production
traffic. Which command accomplishes this?

- A) `gcloud run services update my-service --version=v2 --traffic=5`
- B) `gcloud run services update-traffic my-service --to-revisions=my-service-v2=5,my-service-v1=95 --region=us-central1`
- C) `gcloud run revisions update my-service-v2 --traffic=5`
- D) `gcloud run deploy my-service --traffic-percent=5`

**Correct Answer:** B

**Explanation:** `gcloud run services update-traffic` is the correct command to
split traffic between revisions. It accepts `--to-revisions` with a
comma-separated list of `REVISION=PERCENTAGE` pairs that must sum to 100.
Option A uses incorrect syntax. Options C and D do not exist as valid Cloud Run
commands.

---

## Question 9

You have a Cloud Functions Gen 1 function that is triggered by new object
creation events in Cloud Storage. You want to migrate this function to Gen 2.
Which change must you make to the trigger configuration?

- A) No change — Gen 1 and Gen 2 use identical trigger syntax
- B) Replace the direct Cloud Storage trigger with an Eventarc trigger using
     the `google.cloud.storage.object.v1.finalized` event type
- C) Add the bucket as a Pub/Sub subscriber and consume messages in the function
- D) Gen 2 functions cannot be triggered by Cloud Storage events

**Correct Answer:** B

**Explanation:** Cloud Functions Gen 2 uses Eventarc for event triggers rather
than the direct background event bindings used in Gen 1. For Cloud Storage
events, you create an Eventarc trigger with the event type
`google.cloud.storage.object.v1.finalized` and the bucket filter. The function
code receives the event in CloudEvents format rather than the Gen 1 background
event format, which also requires updating the function handler signature.

---

## Question 10

Which of the following is NOT a characteristic of App Engine Flexible environment?

- A) Supports custom Docker containers for any runtime
- B) Always maintains at least one instance running (cannot scale to zero)
- C) Provides millisecond startup times like the Standard environment
- D) Runs on Compute Engine virtual machines

**Correct Answer:** C

**Explanation:** App Engine Flexible runs on Compute Engine VMs inside Docker
containers. VM startup takes minutes, not milliseconds. App Engine Standard uses
a lightweight sandbox that starts in milliseconds. Options A, B, and D are all
accurate descriptions of the Flexible environment: custom Docker containers,
minimum one always-on instance, and Compute Engine-based infrastructure.

---

End of Quiz — Module 07

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

---

### Question 11 (5 points)

A Cloud Run service is deployed with `--min-instances=3`. What is the effect
of this setting?

- A) Cloud Run will never scale above 3 instances regardless of traffic
- B) Cloud Run always keeps at least 3 instances warm, eliminating cold starts
   for the first 3 concurrent requests
- C) Cloud Run scales down to 3 instances after a period of low traffic but
   can still reach zero under sustained idleness
- D) The setting limits the total lifetime instance count to 3

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `--min-instances` sets the floor, not the ceiling; `--max-instances` controls the upper bound.
  - C) With `--min-instances=3`, Cloud Run will never scale below 3 — it will not reach zero, which is the key purpose of this setting for latency-sensitive services.
  - D) `--min-instances` is a live concurrency floor, not a lifetime counter; instances can be replaced and new instances created beyond this minimum count.

---

### Question 12 (5 points)

Which App Engine environment supports gRPC and allows you to install custom
OS packages via a Dockerfile?

- A) Standard environment — it supports all protocols via its sandbox
- B) Flexible environment — it runs in Docker containers on Compute Engine VMs
- C) Standard environment with the Java 21 runtime
- D) Neither — gRPC is not supported on App Engine

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) App Engine Standard runs in a language-specific sandbox that does not support arbitrary OS packages or gRPC; it is restricted to HTTP/HTTPS.
  - C) The Java 21 runtime is a Standard environment runtime and inherits Standard's sandbox restrictions; it does not support gRPC or custom OS packages.
  - D) gRPC is supported in App Engine Flexible because Flexible uses real Docker containers on Compute Engine VMs with full OS access.

---

### Question 13 (5 points)

A Cloud Function Gen 2 needs to write to a Cloud Firestore database. No
service account is explicitly configured. Which identity does the function
use by default?

- A) The Compute Engine default service account
- B) The App Engine default service account
- C) The function uses no identity — unauthenticated calls to Firestore are
   allowed by default
- D) The Cloud Functions service agent account specific to the function

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) The Compute Engine default service account is associated with GCE VMs, not Cloud Functions; the two services use different default identities.
  - C) Firestore requires authentication; Cloud Functions always use a service account identity, never unauthenticated.
  - D) Cloud Functions Gen 2 uses the App Engine default service account (`PROJECT_ID@appspot.gserviceaccount.com`) as the default runtime identity; you can override this by specifying a custom service account at deployment.

---

### Question 14 (5 points)

You need to invoke a Cloud Run service from a Pub/Sub push subscription.
The Cloud Run service requires authenticated requests. What must be configured
on the Pub/Sub push subscription?

- A) The Pub/Sub subscription must use pull delivery instead of push
- B) The Pub/Sub subscription must be configured with a service account that
   has `roles/run.invoker` on the Cloud Run service, and the push endpoint
   must use the service URL
- C) The Cloud Run service must be set to allow unauthenticated invocations
- D) The Pub/Sub topic must be in the same project as the Cloud Run service

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Push subscriptions can invoke authenticated Cloud Run services; pull delivery would require a separate consumer process, adding complexity.
  - C) Allowing unauthenticated invocations weakens security; the correct approach is to configure a service account with the invoker role on the push subscription, not to open the service to the public.
  - D) Pub/Sub topics and Cloud Run services can be in different projects as long as IAM permissions are correctly configured; same-project is not required.

---

### Question 15 (5 points)

What is the maximum timeout duration for a Cloud Run request?

- A) 60 seconds
- B) 5 minutes
- C) 60 minutes
- D) 24 hours

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) 60 seconds was an early Cloud Run limit; the current maximum is 60 minutes (3600 seconds).
  - B) 5 minutes is below the current maximum; this figure is not a documented Cloud Run timeout limit.
  - D) 24 hours is the maximum for Cloud Run jobs (batch mode), not for request-serving Cloud Run services.

---

### Question 16 (5 points)

A Cloud Functions Gen 1 function is triggered every time an object is
finalized in a Cloud Storage bucket. The function processes images. Recently
the same image has been processed multiple times. What is the likely cause
and recommended mitigation?

- A) Cloud Functions triggers fire exactly once per event; duplicate processing
   indicates a bug in the function code
- B) Cloud Pub/Sub delivery (which underlies Storage triggers) is at-least-once;
   functions must be designed to be idempotent to handle duplicate invocations
- C) The bucket has object versioning enabled, which fires multiple events per
   upload
- D) The function's retry-on-failure setting is causing successful invocations
   to be replicated

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Functions delivers events at-least-once; duplicate delivery is an expected behavior, not necessarily a code bug.
  - C) Object versioning creates new object versions but does not multiply `OBJECT_FINALIZE` events for a single upload; each version finalize fires one event.
  - D) Retry-on-failure only re-invokes a function if the previous invocation returned an error; it does not duplicate successful invocations.

---

### Question 17 (5 points)

Which Cloud Run feature allows you to serve two different container images
from the same service URL, routing a percentage of requests to each?

- A) Cloud Run jobs with parallel task execution
- B) Revision traffic splitting configured via `gcloud run services
   update-traffic`
- C) Cloud Load Balancing with two separate Cloud Run services as backends
- D) Cloud Run multi-region deployment with latency-based routing

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) Cloud Run jobs run batch tasks to completion; they do not serve HTTP traffic or support traffic splitting.
  - C) Using two separate Cloud Run services behind a load balancer would work for A/B testing but is not the Cloud Run-native traffic splitting feature; it also routes to entirely separate services, not revisions of the same service.
  - D) Multi-region deployment routes traffic based on geography, not percentage; this serves latency optimization, not A/B testing or canary deployments.

---

### Question 18 (5 points)

App Engine dispatch rules allow you to route requests to different App Engine
services based on URL path. Which file defines dispatch rules in an App Engine
application?

- A) `app.yaml`
- B) `dispatch.yaml`
- C) `cron.yaml`
- D) `index.yaml`

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) `app.yaml` defines a single service's configuration (runtime, scaling, environment variables); it does not define cross-service URL routing rules.
  - C) `cron.yaml` defines scheduled task configurations for App Engine cron jobs; it is unrelated to request routing.
  - D) `index.yaml` defines Cloud Datastore/Firestore composite indexes for the application; it has nothing to do with URL routing.

---

### Question 19 (5 points)

You want a Cloud Function to execute every day at 9 AM UTC. Which GCP service
orchestrates this scheduled invocation?

- A) Cloud Tasks with a delay set to the next 9 AM UTC
- B) Eventarc with a scheduled trigger
- C) Cloud Scheduler with a cron job that publishes to a Pub/Sub topic, which
   triggers the function
- D) App Engine cron jobs configured in `cron.yaml`

- **Correct Answer:** C
- **Distractor Analysis:**
  - A) Cloud Tasks supports task-level delay (up to 30 days) but is not designed for recurring cron-style schedules; scheduling a new task each day for the next day requires a separate orchestration layer.
  - B) Eventarc does not have a time-based scheduling feature; it routes events from GCP service operations, not calendar-based triggers.
  - D) App Engine cron jobs can schedule HTTP requests but are specific to App Engine services; for Cloud Functions, Cloud Scheduler with Pub/Sub or a direct HTTP target is the standard approach.

---

### Question 20 (5 points)

A Serverless VPC Access connector is created in `us-central1` with CIDR
`10.8.0.0/28`. A Cloud Run service in `us-central1` sends a request to a
Compute Engine VM at `10.0.1.5` via this connector. From the VM's perspective,
what is the source IP of the incoming request?

- A) The Cloud Run service's public internet IP
- B) An IP address from the connector's CIDR range `10.8.0.0/28`
- C) The VM's own IP address due to source NAT
- D) `169.254.x.x` — the serverless metadata IP range

- **Correct Answer:** B
- **Distractor Analysis:**
  - A) When traffic flows through a Serverless VPC Access connector, it enters the VPC from the connector's IP range, not from a public internet IP; the VM sees a private RFC 1918 source IP.
  - C) Source NAT to the destination VM's own IP would make the connection appear to come from itself, which is not the connector's behavior.
  - D) `169.254.x.x` is the link-local range used for GCP metadata server access (`169.254.169.254`); it is not used for connector-sourced traffic.

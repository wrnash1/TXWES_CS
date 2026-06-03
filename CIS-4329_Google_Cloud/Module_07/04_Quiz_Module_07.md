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

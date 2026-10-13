# Discussion: Module 07 — Cloud Run and Serverless Computing

## Course: CIS-4329 Google Cloud Computing

**Certification Alignment:** Google Cloud Associate Cloud Engineer (ACE)

---

## Overview

This discussion asks you to design and evaluate serverless architectures using
GCP's compute and eventing services. Choosing the right serverless platform
and composing them with event-driven patterns is a practical skill tested on
the ACE exam and valued in the field.

**Due:** See course calendar for deadlines.

**Grading:** Initial post (60 points) + two peer responses (20 points each) = 100 points

---

## Prompt A — Serverless Architecture Design (Choose One)

A mid-sized retail company wants to build the following systems on GCP using
serverless services:

- A public product catalog API serving millions of requests per day with
  unpredictable traffic spikes during sales events
- An order processing pipeline: customers submit orders via the API; orders
  must be processed reliably even if backend services are temporarily
  unavailable
- A nightly report generator that aggregates the day's sales data from Cloud
  Storage and writes summaries to BigQuery
- An image resizing service: when a product image is uploaded to Cloud Storage,
  it should automatically create three thumbnail sizes

Design the full serverless architecture:

1. For each of the four systems, specify which GCP serverless service(s) you
   would use (Cloud Run, Cloud Functions Gen 2, App Engine) and justify the
   choice.
2. Describe how you would use Eventarc or Pub/Sub to connect the image upload
   event to the thumbnail service.
3. Explain how you would use Cloud Tasks to make the order processing pipeline
   reliable even during backend outages.
4. For the product catalog API, describe Cloud Run configuration settings
   (min-instances, max-instances, concurrency) appropriate for the described
   traffic pattern. Explain the cost implications of each setting.

---

## Prompt B — Serverless Migration Analysis (Choose One)

A startup currently runs all of its backend services on a single Compute Engine
VM. The VM runs:

- A Node.js REST API receiving HTTP requests
- A Python script that polls an S3-compatible storage bucket every 5 minutes
  for new files and processes them
- A daily database backup job that runs at 2 AM
- A webhook handler that receives payment events from Stripe and updates a
  Firestore database

The team is growing and wants to modernize the architecture to be more scalable,
cost-efficient, and maintainable. Propose a serverless migration for each
workload:

1. For each of the four workloads, propose a target GCP serverless service
   and explain the migration approach.
2. Compare the current monolithic VM approach to the proposed serverless
   architecture in terms of cost at low traffic, cost at high traffic,
   operational overhead, and fault isolation.
3. Identify which workloads are best suited for Cloud Run vs. Cloud Functions
   and explain the deciding factors.
4. Describe potential cold start issues with the proposed architecture and
   explain how you would mitigate them for the most latency-sensitive workload.

---

## Response Requirements

Your initial post must be at least 300 words and include:

- Specific GCP service names and feature names (e.g., Eventarc, Cloud Tasks,
  `--min-instances`, `--concurrency`)
- Cost reasoning where applicable (scale to zero, minimum instances, billing
  models)
- At least one explicit trade-off you considered and resolved

Your two peer responses must each be at least 100 words and do one of the
following:

- Challenge a service choice with a concrete alternative and justification
- Identify a failure mode the original design does not handle
- Add a security or compliance consideration the post did not address

---

## Discussion Tips

- Cloud Run documentation at cloud.google.com/run/docs has detailed guidance
  on configuration parameters and their cost implications.
- Think about cold starts: a `--min-instances=0` service is cheaper but has
  latency on the first request after an idle period. For user-facing APIs,
  even a few seconds of cold start can impact user experience.
- Eventarc vs. Pub/Sub: both can connect storage events to functions, but they
  differ in routing model and event format. Know which is appropriate for
  Cloud Functions Gen 2 vs. Gen 1.

---

## Reflection Question (Optional — Extra Credit)

The serverless model shifts operational responsibility from the customer to
the cloud provider. Discuss the security implications of this trade-off.
What security controls do you lose? What security controls does Google provide
automatically? How does this affect your organization's shared responsibility
model under something like PCI-DSS or HIPAA? Minimum 150 words.

---

End of Discussion — Module 07

Course: CIS-4329 Google Cloud Computing | Texas Wesleyan University | Professor Nash

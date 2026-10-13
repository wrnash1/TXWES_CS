# Video Script: Module 11 — Infrastructure as Code on GCP

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Note: This module's video content is split across two files

## See: 01_Video_Script_Module_11_Part_1.md (Deployment Manager)

## See: 01_Video_Script_Module_11_Part_2.md (Terraform)

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 11. I am Professor Nash. This module covers Cloud Pub/Sub — Google
Cloud's fully managed messaging service — and Cloud Functions, the serverless
event-driven compute service. Together these two services form the backbone of
event-driven architectures on GCP.

In Part 1 we cover Pub/Sub end-to-end: topics, subscriptions, push vs. pull delivery,
at-least-once delivery semantics, message ordering, and dead letter topics. In Part 2
we connect Pub/Sub to Cloud Functions and cover Eventarc for routing GCP service events
to serverless handlers.

Event-driven architecture appears frequently on the ACE exam in scenarios involving data
pipelines, IoT ingestion, microservice decoupling, and serverless compute triggers.

---

### Section 1: Why Event-Driven Architecture

Traditional request-response architectures couple services tightly. If Service B is
unavailable, Service A fails. Event-driven architecture solves this by introducing a
message broker:

- **Producer** — publishes an event to the broker
- **Broker** — stores and routes the event reliably
- **Consumer** — receives and processes the event independently

Cloud Pub/Sub is GCP's managed message broker. It scales to millions of messages per
second with no infrastructure to manage.

---

### Section 2: Topics and Subscriptions

A **topic** is a named resource that receives published messages. A **subscription**
represents a named stream of messages from one topic for a specific consumer.

The key architectural rule: **one topic can have multiple subscriptions**. Each
subscription independently receives a copy of every message. This is the fan-out
pattern — publish once, deliver to many consumers.

```bash
# Create a topic
gcloud pubsub topics create my-orders-topic

# Create two subscriptions (each gets its own copy of every message)
gcloud pubsub subscriptions create inventory-sub \
  --topic=my-orders-topic

gcloud pubsub subscriptions create analytics-sub \
  --topic=my-orders-topic

# Publish a test message
gcloud pubsub topics publish my-orders-topic \
  --message='{"orderId": "12345"}' \
  --attribute=eventType=OrderPlaced

# Pull a message from the first subscription
gcloud pubsub subscriptions pull inventory-sub --auto-ack --limit=5
```

---

### Section 3: Push vs. Pull Delivery

#### Pull Delivery

The subscriber calls the API to fetch messages. Use pull for batch jobs, worker
processes, and GKE pods that process at their own rate.

#### Push Delivery

Pub/Sub POSTs messages to an HTTPS endpoint. Use push for Cloud Run and App Engine
services that should react immediately without polling.

```bash
# Create a push subscription to a Cloud Run service
gcloud pubsub subscriptions create my-push-sub \
  --topic=my-orders-topic \
  --push-endpoint=https://my-service-abc123-uc.a.run.app/pubsub
```

| Characteristic | Pull | Push |
|---|---|---|
| Who initiates | Subscriber calls API | Pub/Sub POSTs to endpoint |
| Best for | Batch jobs, GKE workers | Cloud Run, App Engine |
| Rate control | Subscriber controls | Pub/Sub controls |

---

### Section 4: At-Least-Once Delivery and Idempotency

Pub/Sub guarantees **at-least-once delivery** — every message is delivered at least
once per subscription but may be delivered more than once if the subscriber does not
acknowledge within the acknowledgment deadline (default 10 seconds, max 600 seconds).

Design implication: consumers must be **idempotent** — processing the same message
twice must produce the same result as processing it once.

---

### Section 5: Message Ordering

By default, Pub/Sub does not guarantee message order. Enable ordering on the
subscription and include an ordering key in each published message:

```bash
# Enable message ordering on a subscription
gcloud pubsub subscriptions create ordered-sub \
  --topic=my-orders-topic \
  --enable-message-ordering
```

All messages with the same ordering key are delivered to the same subscriber partition
in the order they were published.

---

### Section 6: Dead Letter Topics

Messages that fail processing repeatedly need a safety valve. A **dead letter topic**
receives messages that exceed the maximum delivery attempt count:

```bash
# Create dead letter infrastructure
gcloud pubsub topics create my-orders-dead-letter

gcloud pubsub subscriptions create inventory-sub \
  --topic=my-orders-topic \
  --dead-letter-topic=my-orders-dead-letter \
  --max-delivery-attempts=5
```

After 5 failed deliveries, the message moves to the dead letter topic for investigation
rather than retrying indefinitely.

---

### Section 7: Message Retention and Replay

Undelivered messages are retained for up to 7 days. Enable topic-level retention and
seek a subscription backward to replay historical events:

```bash
# Enable retention on topic
gcloud pubsub topics update my-orders-topic \
  --message-retention-duration=7d

# Replay from 2 hours ago
gcloud pubsub subscriptions seek inventory-sub \
  --time=2024-01-15T10:00:00Z
```

---

### Closing — Part 1

In Part 1 we covered Cloud Pub/Sub: topics, subscriptions, push vs. pull delivery,
at-least-once delivery with idempotency, message ordering, dead letter topics, and
replay. In Part 2 we build event-driven pipelines by connecting Pub/Sub to Cloud
Functions and Eventarc.

See you in Part 2.

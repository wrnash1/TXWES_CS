# Video Script: Module 10 — Pub/Sub and Event-Driven Architecture (Part 1 of 2)

## Course: CIS-4329 Google Cloud Computing

## Texas Wesleyan University | Professor Nash

## Estimated Duration: 14 minutes

## Certification Alignment: Google Cloud Associate Cloud Engineer (ACE)

---

### Introduction

Welcome to Module 10. I am Professor Nash. This module covers Cloud Pub/Sub — Google
Cloud's fully managed messaging service — and how it enables event-driven, decoupled
architectures on GCP.

In Part 1 we build a complete understanding of Pub/Sub: what it is, how topics and
subscriptions work, the difference between push and pull delivery, message ordering,
and how to configure dead letter topics for failure handling. In Part 2 we connect
Pub/Sub to Cloud Functions and Eventarc to build reactive serverless pipelines.

Event-driven architecture is tested on the ACE exam in the context of data pipelines,
microservice integration, and IoT ingestion. Knowing when to use Pub/Sub and how
subscriptions route messages is frequently required.

---

### Section 1: Why Event-Driven Architecture

Traditional request-response architectures are tightly coupled. Service A calls Service B
directly. If Service B is slow or unavailable, Service A is blocked or fails.

Event-driven architecture decouples producers from consumers by introducing a message
broker in the middle:

- **Producer** — publishes an event (e.g., "order placed") to the broker
- **Broker** — stores and routes the event reliably
- **Consumer** — receives and processes the event independently, at its own pace

Benefits:

- **Decoupling** — the producer does not need to know which consumers exist
- **Fan-out** — a single event can trigger multiple independent consumers simultaneously
- **Buffering** — the broker absorbs traffic spikes, preventing consumers from being
  overwhelmed
- **Retry** — if a consumer fails, the broker retains the message and retries delivery

Cloud Pub/Sub is GCP's managed message broker for event-driven architectures.

---

### Section 2: Cloud Pub/Sub Fundamentals

Cloud Pub/Sub is a fully managed, globally distributed publish/subscribe messaging
service. It scales automatically from zero to millions of messages per second with no
infrastructure to manage.

#### Topics

A **topic** is a named resource to which publishers send messages. The topic itself
stores nothing permanently — it is a logical channel. Messages are delivered to
subscribers through subscriptions.

```bash
# Create a Pub/Sub topic
gcloud pubsub topics create my-orders-topic

# List topics
gcloud pubsub topics list

# Delete a topic
gcloud pubsub topics delete my-orders-topic
```

#### Subscriptions

A **subscription** attaches to a topic and represents a stream of messages for a
specific consumer. Each subscription receives a copy of every message published to the
topic after the subscription was created.

Key point: **one topic can have multiple subscriptions**. This is the fan-out pattern —
publish once, deliver to many consumers.

```bash
# Create a pull subscription
gcloud pubsub subscriptions create my-inventory-sub \
  --topic=my-orders-topic

# Create a second subscription (different consumer gets same messages)
gcloud pubsub subscriptions create my-analytics-sub \
  --topic=my-orders-topic

# List subscriptions
gcloud pubsub subscriptions list
```

#### Message Anatomy

A Pub/Sub message has:

- **Data** — the message body, base64-encoded (up to 10 MB)
- **Attributes** — key-value pairs for metadata (e.g., `eventType=OrderPlaced`)
- **Message ID** — assigned by Pub/Sub on publish
- **Publish time** — timestamp when the message was received by Pub/Sub

```bash
# Publish a test message
gcloud pubsub topics publish my-orders-topic \
  --message='{"orderId": "12345", "total": 99.99}' \
  --attribute=eventType=OrderPlaced,region=us-east

# Pull a message (for testing)
gcloud pubsub subscriptions pull my-inventory-sub \
  --auto-ack \
  --limit=5
```

---

### Section 3: Push vs. Pull Delivery

Pub/Sub supports two delivery modes. Choosing the correct mode is important for both
architecture and ACE exam scenarios.

#### Pull Delivery

In pull delivery, the subscriber calls the Pub/Sub API to fetch messages. The subscriber
controls its own consumption rate.

```bash
# Pull up to 10 messages without auto-acknowledge
gcloud pubsub subscriptions pull my-inventory-sub \
  --limit=10

# Acknowledge a message after processing
gcloud pubsub subscriptions ack my-inventory-sub \
  --ack-ids=ACK_ID_1,ACK_ID_2
```

**Use pull when:**

- The subscriber is a batch job or worker that processes messages in bursts
- The subscriber needs to control its own rate to avoid overwhelming downstream systems
- The subscriber is running on Compute Engine, GKE, or any always-on process

#### Push Delivery

In push delivery, Pub/Sub proactively delivers messages to an HTTPS endpoint. The
endpoint must respond with HTTP 2xx to acknowledge the message.

```bash
# Create a push subscription targeting a Cloud Run URL
gcloud pubsub subscriptions create my-push-sub \
  --topic=my-orders-topic \
  --push-endpoint=https://my-service-abc123-uc.a.run.app/pubsub
```

**Use push when:**

- The subscriber is a Cloud Run service, App Engine app, or any HTTP endpoint
- You want Pub/Sub to drive event delivery without the subscriber polling
- You need low-latency, near-real-time delivery

#### Pull vs. Push Summary

| Characteristic | Pull | Push |
|---|---|---|
| Who initiates delivery | Subscriber calls API | Pub/Sub POSTs to endpoint |
| Subscriber type | Worker process, batch job | HTTP endpoint |
| Rate control | Subscriber controls | Pub/Sub controls |
| Typical use | Batch processing, GKE workers | Cloud Run, App Engine |

---

### Section 4: Acknowledgment and At-Least-Once Delivery

Pub/Sub guarantees **at-least-once delivery** — every published message is delivered to
each subscription at least once, but may be delivered more than once.

The **acknowledgment deadline** controls how long Pub/Sub waits before redelivering:

- Default: **10 seconds**
- Maximum: **600 seconds** (10 minutes)

If a subscriber receives a message but crashes before acknowledging, Pub/Sub redelivers
after the deadline expires. This ensures no messages are lost — but the same message
can be processed twice.

**Design implication**: Consumer code must be **idempotent** — processing the same
message twice must produce the same result as processing it once.

---

### Section 5: Message Ordering

By default, Pub/Sub does not guarantee message order. Enable ordering on a subscription
when sequence matters:

```bash
# Create a subscription with message ordering enabled
gcloud pubsub subscriptions create my-ordered-sub \
  --topic=my-orders-topic \
  --enable-message-ordering
```

Publishers must include an **ordering key** — all messages with the same key are
delivered in publish order to the same subscriber partition.

**ACE exam rule**: Ordering keys only work when message ordering is enabled on the
subscription. Without ordering keys, enabling ordering has no effect.

---

### Section 6: Dead Letter Topics

Some messages fail permanently — due to malformed data or consumer bugs. Without a
safety valve, these loop forever. A **dead letter topic** captures messages that exceed
the maximum delivery attempt count:

```bash
# Create a dead letter topic
gcloud pubsub topics create my-orders-dead-letter

# Create a subscription with dead letter topic
gcloud pubsub subscriptions create my-inventory-sub \
  --topic=my-orders-topic \
  --dead-letter-topic=my-orders-dead-letter \
  --max-delivery-attempts=5
```

After 5 failed deliveries, the message is forwarded to `my-orders-dead-letter` for
investigation rather than retried indefinitely.

---

### Section 7: Message Retention and Replay

Pub/Sub retains undelivered messages for up to **7 days**. Enable topic-level retention
and seek a subscription backward to replay historical messages:

```bash
# Enable 7-day message retention on the topic
gcloud pubsub topics update my-orders-topic \
  --message-retention-duration=7d

# Replay: seek subscription to 2 hours ago
gcloud pubsub subscriptions seek my-inventory-sub \
  --time=2024-01-15T10:00:00Z
```

Replay is useful after fixing a consumer bug — you can reprocess all events that were
mishandled without republishing from the source system.

---

### Closing — Part 1

In Part 1 we covered:

- The Pub/Sub model: topics, subscriptions, and the fan-out pattern
- Push vs. pull delivery — when to use each
- At-least-once delivery and idempotency requirements
- Message ordering with ordering keys
- Dead letter topics for permanent failures
- Message retention and replay

In Part 2 we connect Pub/Sub to Cloud Functions — building event-driven serverless
pipelines — and cover Eventarc for routing GCP service events to Cloud Run targets.

See you in Part 2.

# Reading Guide: Module 10 — SQS, SNS, and Event-Driven Architecture

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Module:** 10 of 16
**Instructor:** Professor Nash

---

## Purpose of This Guide

This reading guide accompanies the Module 10 video lecture. Use it to reinforce the core concepts, clarify terminology, and focus your exam preparation. The SAA-C03 exam tests messaging and event-driven architecture patterns in nearly every practice exam session.

---

## Core Concept 1 — Amazon SQS

### What SQS Is

Amazon Simple Queue Service is a fully managed, durable message queue. Producers write messages to the queue. Consumers poll the queue, retrieve messages, process them, and delete them when complete. The queue decouples producer throughput from consumer throughput — neither side needs to know the other is running.

### SQS Standard Queue vs. FIFO Queue

| Characteristic | Standard Queue | FIFO Queue |
|---|---|---|
| Delivery guarantee | At-least-once | Exactly-once |
| Message ordering | Best-effort | Strict FIFO within a message group |
| Maximum throughput | Nearly unlimited | 300 TPS; 3,000 TPS with batching |
| Duplicate messages | Possible | Eliminated via deduplication ID |
| Use case | High-throughput, order-tolerant workloads | Financial transactions, order pipelines |

Exam rule: if the scenario says "order matters" or "no duplicates allowed," the answer is FIFO. If the scenario says "maximum throughput" or "order not required," the answer is Standard.

### Key Configuration Parameters

**Visibility timeout:** After a consumer receives a message, SQS hides it from other consumers for the visibility timeout duration. If the consumer successfully processes and deletes the message before the timeout expires, the message is permanently removed. If the consumer fails and does not delete the message, the timeout expires and the message becomes visible again for another consumer. The default is 30 seconds; the range is 0 seconds to 12 hours.

Setting visibility timeout correctly: the visibility timeout must be longer than the maximum expected processing time. If processing takes 3 minutes, set the timeout to at least 5 minutes. A timeout that is too short causes duplicate processing; a timeout that is too long delays retry after consumer failure.

**Message retention period:** How long SQS stores a message if no consumer deletes it. Default is 4 days; range is 1 minute to 14 days.

**Delivery delay:** A delay applied to new messages before they become visible to consumers. Range is 0 to 15 minutes. Useful when downstream systems need time to prepare before receiving a message.

**Long polling:** When a consumer calls ReceiveMessage and the queue is empty, short polling (the default) returns immediately with an empty response, consuming an API call. Long polling waits up to 20 seconds for a message to arrive before returning. Long polling reduces empty responses, reduces cost, and reduces CPU usage in consumers. Always use long polling in production by setting `WaitTimeSeconds=20`.

**Message size limit:** Up to 256 KB per message. For larger payloads, store the payload in S3 and include the S3 object reference in the SQS message — this is the Extended Client Library pattern.

### Dead-Letter Queues

A Dead-Letter Queue is a separate SQS queue. The source queue's redrive policy specifies a `maxReceiveCount`. When a message has been received more than `maxReceiveCount` times without being successfully deleted, SQS automatically moves it to the DLQ.

This mechanism isolates "poison pill" messages — malformed, unparseable, or logically invalid messages that will never process successfully — so they cannot block or consume resources from the main queue. Monitor the DLQ depth with a CloudWatch alarm. When the alarm fires, inspect the DLQ messages to diagnose the failure root cause.

Both Standard and FIFO queues support DLQs. A FIFO queue's DLQ must also be a FIFO queue.

---

## Core Concept 2 — Amazon SNS

### What SNS Is

Amazon Simple Notification Service is a fully managed publish/subscribe (pub/sub) messaging service. Publishers send a message to an SNS topic. Every subscriber to the topic receives a copy of the message immediately — this is the fan-out pattern.

SNS is push-based: the service delivers to subscribers. SQS is pull-based: consumers poll for messages. This distinction is frequently tested.

### SNS Subscription Types

| Subscription Type | Description |
|---|---|
| Amazon SQS | Deliver the message to an SQS queue for durable buffering |
| AWS Lambda | Invoke a Lambda function asynchronously with the message payload |
| HTTP/HTTPS | Send an HTTP POST request with the message to an endpoint |
| Email | Send the message as an email; requires subscriber confirmation |
| SMS | Send the message as an SMS to a phone number |
| Amazon Kinesis Data Firehose | Deliver the message to a Kinesis delivery stream |

### SNS Message Filtering

By default, every subscriber receives every message published to the topic. SNS message filtering lets you attach a filter policy to an individual subscription. The filter policy contains attribute conditions — if a message's attributes do not match the filter, SNS does not deliver the message to that subscription.

Example: a logistics SNS topic receives shipment events. A filter policy on the US-processing SQS subscription matches messages where `region = US`. A filter policy on the EU-processing SQS subscription matches messages where `region = EU`. Each queue receives only the relevant shipments without any routing logic in the producer code.

### SNS Fan-Out to SQS (The Standard Pattern)

Without fan-out, a producer that must notify multiple downstream services must call each service directly. Adding a new downstream consumer requires modifying the producer. The producer becomes tightly coupled to the list of consumers.

With SNS fan-out:

1. The producer publishes one message to an SNS topic.
2. Multiple SQS queues subscribe to the topic.
3. SNS delivers a copy of the message to every subscribed SQS queue simultaneously.
4. Each queue provides durable, independent buffering for its consumer.
5. Adding a new consumer requires only adding a new SQS subscription — the producer code does not change.

If one consumer's queue falls behind, it does not affect other consumers. If one consumer's service goes offline, its SQS queue accumulates messages until the service recovers. This is the canonical AWS decoupling architecture.

---

## Core Concept 3 — Amazon EventBridge

EventBridge is a serverless event bus. It was formerly called CloudWatch Events. EventBridge receives events from three sources: AWS services (EC2 state changes, S3 uploads, CodePipeline state transitions), custom applications (your own code publishing to a custom event bus), and SaaS partners (Datadog, Zendesk, and others).

EventBridge rules match events based on their content — the event payload JSON structure. A rule targets one or more resources: Lambda functions, SQS queues, SNS topics, Step Functions state machines, and more.

EventBridge also supports scheduled rules (cron expressions and rate expressions) for triggering targets on a time-based schedule.

### SQS vs. SNS vs. EventBridge Decision Table

| Characteristic | SQS | SNS | EventBridge |
|---|---|---|---|
| Pull or push | Pull (consumer polls) | Push (SNS delivers) | Push (EventBridge routes) |
| Primary role | Task queue and workload buffer | Fan-out notification | Event routing and filtering |
| Routing capability | None at queue level | Filter policies per subscription | Content-based routing rules |
| Event sources | Your application code | Your application code | AWS services, custom, SaaS |
| Scheduled triggers | No | No | Yes (cron and rate) |
| Use case | Decouple producer/consumer throughput | Fan-out same event to many consumers | React to AWS service events, automate with schedules |

Exam rules:

- "Multiple services must receive the same event independently" → SNS fan-out to SQS queues
- "React to an EC2 instance stopping or a CodePipeline stage completing" → EventBridge
- "Run a Lambda function every hour" → EventBridge scheduled rule
- "Decouple a web tier from a processing tier to absorb traffic spikes" → SQS

---

## Core Concept 4 — Amazon Kinesis Data Streams

Kinesis Data Streams is for high-throughput real-time streaming: clickstream data, application logs, IoT sensor readings, financial market feeds. It is fundamentally different from SQS.

| Characteristic | SQS | Kinesis Data Streams |
|---|---|---|
| Message model | Queue (messages deleted after processing) | Log (records retained regardless of reads) |
| Consumer model | Competing consumers (one processes each message) | Multiple independent consumers, each with its own position |
| Ordering | Best-effort (Standard) or per group (FIFO) | Guaranteed within a shard |
| Retention | 1 minute to 14 days; deleted on processing | 24 hours default; up to 365 days |
| Replay | No | Yes — consumers can re-read old records |
| Throughput unit | Per-message | Shards (1 MB/s write, 2 MB/s read each) |
| Use case | Task queue (process each item once) | Data streaming (multiple consumers, replay, time-series) |

Exam rule: "Multiple consumers must independently read the same data stream" or "replay capability is required" or "real-time analytics from IoT/clickstream data" → Kinesis Data Streams. "Each task should be processed once by one consumer" → SQS.

---

## Architecture Patterns Summary

### Pattern 1 — SQS Workload Decoupling

A web application writes orders to an SQS queue instead of processing them inline. A fleet of EC2 instances or Lambda functions polls the queue and processes orders asynchronously. The queue absorbs traffic spikes. If processing goes offline, orders queue safely until processing resumes.

### Pattern 2 — SNS Fan-Out to Multiple SQS Queues

An order event is published to an SNS topic. Three SQS queues subscribe: inventory service, shipping service, analytics service. All three receive the event simultaneously. If analytics is slow, its queue grows without affecting inventory or shipping.

### Pattern 3 — SQS + Lambda Serverless Processing

Application writes image jobs to SQS. Lambda polls via event source mapping. Lambda scales concurrency based on queue depth. Failed messages return to the queue up to `maxReceiveCount` times then go to the DLQ.

---

## Exam Tips for Module 10

1. SQS visibility timeout is not a retry delay — it is the window during which a message is locked to one consumer. After it expires, the message is available again.
2. Long polling reduces cost. Short polling wastes API calls. The exam may describe a system generating excessive SQS API costs — the answer is long polling.
3. SNS does not store messages durably. If a subscriber is unavailable and not backed by SQS, messages may be lost. The fix is SNS-to-SQS fan-out, not raw SNS.
4. EventBridge is the right choice when the trigger is an AWS service event. SNS and SQS are for application-generated events.
5. Kinesis retains data as a log. SQS deletes messages after processing. "Multiple independent consumers" or "replay" → Kinesis.
6. A DLQ is not a retry mechanism — it receives messages that have failed too many times. The source queue handles retries via visibility timeout; the DLQ captures what could not be recovered.

---

## Certification Study

For practice exams, official documentation, and study resources: <aws.amazon.com/certification>

---

*Proprietary and Confidential. Not for disclosure outside of Texas Wesleyan University.*

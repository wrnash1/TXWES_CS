# Reading Guide: Module 12 — Serverless Architecture on AWS

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Explain the Lambda execution lifecycle, including cold starts and warm reuse
2. Configure Lambda triggers across synchronous, asynchronous, and poll-based sources
3. Design APIs using API Gateway REST, HTTP, and WebSocket types with appropriate authorizers
4. Select between SQS Standard and FIFO queues based on application requirements
5. Implement the SNS fan-out pattern with SQS for durable, decoupled messaging
6. Design event-driven workflows using EventBridge rules and Step Functions state machines
7. Use DynamoDB Streams to trigger reactive data pipelines
8. Apply serverless architectural patterns to SAA-C03 scenario questions

---

## Section 1: AWS Lambda Fundamentals

### 1.1 The Execution Environment

Every Lambda invocation runs inside an execution environment — an isolated, secure runtime container managed by AWS. The environment lifecycle has three phases:

**Init phase** — Lambda downloads the deployment package, starts the runtime, and runs all initialization code outside the handler. This phase occurs only during cold starts.

**Invoke phase** — Lambda calls your handler function with the event payload. This phase repeats for each invocation in a warm environment.

**Shutdown phase** — After a period of inactivity, Lambda terminates the execution environment.

During the Invoke phase, Lambda reuses global variables, database connections, and any state established during Init. This is why placing expensive initialization (SDK clients, database connections, large config parsing) outside the handler function is a critical best practice. On a warm invocation, that initialization is already complete.

### 1.2 Deployment Packages and Container Images

Lambda supports two deployment formats:

**ZIP deployment package** — a ZIP archive containing your function code and dependencies. Maximum unzipped size is 250 MB (including layers). Maximum ZIP size for direct upload is 50 MB; for S3 upload it is 250 MB.

**Container image** — a Docker-compatible OCI image stored in Amazon ECR. Maximum image size is 10 GB. Container images allow use of familiar Docker tooling and support much larger dependencies.

### 1.3 Function URLs

Lambda Function URLs provide a dedicated HTTPS endpoint for your function without requiring API Gateway. They support IAM authentication or unauthenticated (public) access with CORS configuration. Useful for simple webhooks and single-function APIs.

### 1.4 Lambda Power Tuning

AWS Lambda Power Tuning (open-source AWS Step Functions state machine) tests your function at multiple memory configurations and reports the cost-performance tradeoff curve. Use it to find the optimal memory setting: higher memory often costs the same or less due to shorter execution time.

---

## Section 2: Lambda Triggers Reference

### 2.1 Synchronous Triggers

With synchronous triggers, the event source waits for Lambda to complete and return a response. Any errors must be handled by the caller.

| Trigger | Notes |
|---|---|
| API Gateway | REST, HTTP, WebSocket APIs |
| Application Load Balancer | Lambda as a target group |
| Cognito | Pre/post authentication, pre-token generation |
| Lex | Chatbot fulfillment |
| CloudFront (Lambda@Edge) | Viewer/origin request and response |
| Alexa Skills | Smart home and custom skills |

### 2.2 Asynchronous Triggers

Lambda queues the event internally and processes it. Retries occur twice on failure (configurable). Use Destinations or DLQs to capture unprocessable events.

| Trigger | Notes |
|---|---|
| S3 | Object created, deleted, restore events |
| SNS | Topic subscription |
| EventBridge | Rule targets |
| SES | Email receiving actions |
| CloudWatch Logs | Subscription filters |
| CodeCommit / CodePipeline | CI/CD events |

### 2.3 Poll-Based (Stream and Queue) Triggers

Lambda polls the source on your behalf using an Event Source Mapping. Lambda manages the polling, batching, error handling, and retry behavior.

| Trigger | Ordering | Delivery |
|---|---|---|
| SQS Standard | Best-effort | At-least-once |
| SQS FIFO | Strict per group | Exactly-once |
| DynamoDB Streams | Per-shard ordered | At-least-once |
| Kinesis Data Streams | Per-shard ordered | At-least-once |
| MSK / Self-managed Kafka | Per-partition | At-least-once |

---

## Section 3: Amazon API Gateway

### 3.1 Choosing an API Type

Use this decision framework:

- Need request/response transformation, usage plans, or API keys? → **REST API**
- Need low cost, low latency, JWT auth with Lambda proxy? → **HTTP API**
- Need persistent bidirectional connections? → **WebSocket API**

### 3.2 Integration Types

**Lambda Proxy Integration** — API Gateway passes the full HTTP request as a structured event to Lambda. Lambda must return a response in a specific JSON format (statusCode, headers, body). This is the standard and recommended pattern.

**Lambda Non-Proxy (Custom) Integration** — API Gateway can transform the request using mapping templates before passing it to Lambda, and transform Lambda's response before returning it to the client. Requires VTL mapping templates. More complex, rarely needed for new architectures.

**HTTP Integration** — forwards requests to HTTP endpoints (other APIs, on-premises services). Supports proxy and non-proxy modes.

**Mock Integration** — returns a hardcoded response without invoking a backend. Useful for API design and testing.

**AWS Service Integration** — directly integrates with AWS services (DynamoDB, S3, SQS) without Lambda in the middle. Reduces latency and cost for simple CRUD operations.

### 3.3 Stages and Deployments

API Gateway requires explicit deployments. Changes to an API are not live until deployed to a stage. Stages represent environments (dev, test, prod). Stage variables act like environment variables — reference them in integration URIs to point different stages at different Lambda aliases or endpoints.

### 3.4 Canary Deployments

REST APIs support canary releases: a percentage of traffic goes to the new deployment (canary stage), the rest to the current stage. Promote the canary when satisfied or roll back by disabling it.

### 3.5 API Gateway Caching

Response caching is available on REST APIs. Cache is created per stage. Parameters to the cache key are configurable (query strings, headers). Cache TTL range: 0–3,600 seconds. When a cached response exists, API Gateway returns it without invoking Lambda. Clients can invalidate cache entries with the `Cache-Control: max-age=0` header (if you enable that setting).

---

## Section 4: Amazon SQS Deep Dive

### 4.1 Standard vs. FIFO Comparison

| Feature | Standard | FIFO |
|---|---|---|
| Throughput | Unlimited | 300 TPS (3,000 with batching) |
| Ordering | Best-effort | Strict (per message group) |
| Delivery | At-least-once | Exactly-once (deduplication window) |
| Deduplication | No | Yes (5-minute window) |
| Use case | High throughput, loose coupling | Ordered workflows, financial |

### 4.2 Visibility Timeout Strategy

Set Visibility Timeout = (function processing time) × 1.25 as a starting point. If your Lambda processes SQS messages and takes up to 30 seconds per batch, set Visibility Timeout to 37–40 seconds. If you extend processing time dynamically, call `ChangeMessageVisibility` to extend the timeout before it expires.

### 4.3 Dead-Letter Queues

Configure a DLQ on every production SQS queue. Set `maxReceiveCount` based on your retry tolerance. After that many receive attempts, SQS moves the message to the DLQ. Set up a CloudWatch alarm on the DLQ's `ApproximateNumberOfMessagesVisible` metric to alert on failures.

DLQs must be the same type as the source queue: Standard queues use Standard DLQs; FIFO queues use FIFO DLQs.

### 4.4 Lambda and SQS — Batch Processing

When Lambda polls SQS, it reads up to the configured batch size (default 10, maximum 10,000 for Standard; 10 for FIFO). Lambda invokes your function with a batch of messages as a list in `event.Records`.

**Partial batch failure.** If your function fails, the default behavior retries the entire batch. To report individual message failures, return `batchItemFailures` in your response — a list of message IDs that failed. Lambda retries only those messages, not the successful ones.

### 4.5 SQS Extended Client Library

Standard SQS messages are limited to 256 KB. The SQS Extended Client Library (Java, Python) stores the message body in S3 and sends a reference pointer in SQS. The consumer library automatically retrieves the full payload from S3. Maximum payload size is 2 GB (S3 object limit).

---

## Section 5: Amazon SNS

### 5.1 Topic Types

**Standard Topics** — unlimited throughput, best-effort ordering, at-least-once delivery to subscribed endpoints. Support all subscription protocols.

**FIFO Topics** — strict ordering, deduplication, high throughput. Only SQS FIFO queues and Lambda can subscribe to FIFO topics.

### 5.2 Message Filtering

Every subscription can have a filter policy with up to five attributes. If an attribute is absent from the filter, all values are accepted for that attribute. Filtering reduces the number of deliveries and decreases downstream processing costs.

Example use case: An e-commerce order topic. An `order_status` attribute filters messages to specific queues — `PLACED` events go to the fulfillment queue, `SHIPPED` events go to the notification queue, `RETURNED` events go to the returns queue.

### 5.3 SNS Message Encryption

SNS supports server-side encryption (SSE) using AWS KMS. Messages are encrypted before being stored in SNS and decrypted when delivered to endpoints. Use SSE for sensitive data (PII, financial records).

### 5.4 SNS + Lambda Failure Handling

When SNS invokes Lambda and Lambda fails (after retries), SNS can send the failed message to an SNS DLQ (an SQS queue set on the subscription). Configure this for every production SNS→Lambda subscription.

---

## Section 6: Amazon EventBridge

### 6.1 Event Bus Types

**Default event bus** — receives events from AWS services automatically. Cannot be deleted.

**Custom event bus** — receives events from your applications via `PutEvents`. Isolate events by domain or application.

**Partner event bus** — created when you subscribe to a SaaS partner (Zendesk, Datadog, PagerDuty, GitHub, etc.). Partner events arrive directly without polling or webhooks.

### 6.2 Event Pattern Matching

EventBridge uses exact value matching, prefix matching, anything-but matching, numeric matching, and IP address (CIDR) matching. Patterns are JSON objects specifying the conditions on event fields. The event must match ALL conditions (logical AND).

### 6.3 Schema Registry

EventBridge can automatically discover and register schemas for events on your event buses. Use the Schema Registry to generate code bindings (Java, Python, TypeScript) that strongly type your event objects.

### 6.4 EventBridge vs. SNS Decision Guide

| Scenario | Recommendation |
|---|---|
| Fan-out to multiple services, simple attribute filtering | SNS |
| Complex event routing, content-based routing | EventBridge |
| Third-party SaaS integration | EventBridge (partner buses) |
| Schema discovery and code generation | EventBridge |
| Lowest possible latency pub/sub | SNS |

---

## Section 7: AWS Step Functions

### 7.1 State Types Reference

| State | Purpose |
|---|---|
| Task | Calls a service integration (Lambda, DynamoDB, ECS, SageMaker, etc.) |
| Choice | Conditional branch based on input data |
| Wait | Pauses execution for a duration or timestamp |
| Parallel | Runs multiple branches concurrently |
| Map | Iterates over an array of items |
| Pass | Transforms input to output with no service call |
| Succeed | Terminates with success |
| Fail | Terminates with failure and error/cause |

### 7.2 Service Integrations

Step Functions integrates with over 200 AWS services directly — no Lambda needed as a middleman. Integration patterns:

- **Request-Response** — Step Functions sends a request and immediately moves to the next state. Does not wait for job completion.
- **Synchronous (`.sync`)** — Step Functions waits for the job to complete before transitioning. Supports ECS, Glue, SageMaker, Athena, CodeBuild, and others.
- **Wait for Callback (`.waitForTaskToken`)** — pauses execution until a callback is sent with a task token. Used for human approval, external systems, or long-running asynchronous operations.

### 7.3 Error Handling in ASL

Every Task state can define `Catch` and `Retry` blocks:

- `Retry` — specifies error types, initial interval, backoff rate, and max attempts
- `Catch` — catches specific errors and routes to a fallback state (compensating transaction, error logging, etc.)

This declarative error handling is a key advantage of Step Functions over Lambda-chaining patterns.

### 7.4 Standard vs. Express Comparison

| Feature | Standard | Express |
|---|---|---|
| Max duration | 1 year | 5 minutes |
| Execution semantics | Exactly-once | At-least-once |
| Execution history | Step Functions console | CloudWatch Logs only |
| Pricing | Per state transition | Per execution duration + GB |
| Best for | Business workflows, approvals | High-volume event processing |

---

## Section 8: DynamoDB Streams

### 8.1 Stream View Types

- `KEYS_ONLY` — key attributes only. Smallest payload, lowest processing cost. Use when you only need to know which item changed.
- `NEW_IMAGE` — full item after modification. Use for replication, cache population.
- `OLD_IMAGE` — full item before modification. Use for audit logs of what was deleted or overwritten.
- `NEW_AND_OLD_IMAGES` — both. Use for change-data-capture pipelines that compute the delta.

### 8.2 Shards and Lambda Polling

DynamoDB Streams partitions the stream into shards. Lambda reads each shard in order. Lambda scales the number of parallel pollers from 1 to 1,000 per shard (concurrency scaling). Set `BisectBatchOnFunctionError` to split a failing batch in half — quickly isolates individual problematic records.

### 8.3 Kinesis Data Streams as DynamoDB Alternative

DynamoDB Kinesis streaming exports item changes to a Kinesis Data Stream. This provides longer retention (up to 365 days vs. 24 hours for DynamoDB Streams), fanout to multiple consumers, and integration with Kinesis analytics services.

---

## Section 9: Serverless Architectural Patterns

### 9.1 The Synchronous API Pattern

Client → API Gateway → Lambda → DynamoDB. The simplest pattern. Use for low-latency CRUD operations where the client needs an immediate response.

### 9.2 The Asynchronous Offload Pattern

Client → API Gateway → Lambda → SQS → Worker Lambda. The API returns 202 Accepted immediately. A worker Lambda processes the job asynchronously. Use for long-running operations (report generation, image processing, email sending).

### 9.3 The Fan-Out Pattern

Producer Lambda → SNS → multiple SQS queues → multiple consumer Lambdas. Use when one event must trigger multiple independent downstream workflows.

### 9.4 The Event Sourcing Pattern

All state changes are stored as immutable events in DynamoDB. Current state is derived by replaying events. DynamoDB Streams feeds projections to read-optimized stores.

### 9.5 The Saga Orchestration Pattern

Step Functions coordinates multi-step distributed transactions. On any step failure, Step Functions executes compensating transactions (refund payment, release inventory, cancel reservation) to maintain consistency without distributed locking.

---

## Key Terms

- **Cold Start** — initialization delay when Lambda creates a new execution environment
- **Provisioned Concurrency** — pre-warmed Lambda execution environments that eliminate cold starts
- **Reserved Concurrency** — maximum concurrent executions cap for a specific function
- **Dead-Letter Queue (DLQ)** — destination queue for messages/events that repeatedly fail processing
- **Fan-out** — distributing one event to multiple independent subscribers simultaneously
- **Event Source Mapping** — Lambda configuration linking a stream/queue to a function
- **Amazon States Language (ASL)** — JSON-based DSL for defining Step Functions state machines
- **FIFO** — First-In-First-Out; queue/topic type guaranteeing ordered, exactly-once processing

---

## SAA-C03 Exam Tips

- SQS FIFO = ordered + exactly-once; Standard = high throughput + best-effort
- SNS fan-out to SQS = durable fan-out (SNS alone is not durable)
- Provisioned Concurrency eliminates cold starts; Reserved Concurrency caps a function's concurrency
- Step Functions Standard = long-running workflows with full history; Express = high-volume short workflows
- API Gateway HTTP API is cheaper and faster than REST API; use REST when you need caching or API keys
- Lambda asynchronous failures route to DLQ or Destinations (not retried by the caller)
- DynamoDB Streams retention: 24 hours. For longer retention, use Kinesis Data Streams.
- EventBridge is the right answer for SaaS event integration and complex content-based routing

---

## 10. Supplemental Resources

**1. AWS Documentation — AWS Lambda Developer Guide**
https://docs.aws.amazon.com/lambda/latest/dg/welcome.html
Complete reference for Lambda function configuration, execution environments, concurrency models, event source mappings, and cold start optimization — directly aligned to the Lambda topics in Module 12 and the SAA-C03 Serverless domain.

**2. AWS Skill Builder — AWS Lambda Foundations**
https://skillbuilder.aws/learn/course/external/view/elearning/1034/aws-lambda-foundations
Free course covering Lambda invocation models, execution lifecycle, concurrency controls, error handling, and deployment packaging — supporting the hands-on lab and exam preparation for this module.

**3. AWS Documentation — AWS Step Functions Developer Guide**
https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html
Authoritative guide to Step Functions Standard and Express workflows, Amazon States Language, error handling with Catch and Retry, and integration patterns with Lambda, DynamoDB, and SQS — the reference for the orchestration patterns covered in Section 9.

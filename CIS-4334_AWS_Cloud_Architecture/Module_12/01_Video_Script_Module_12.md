# Video Script: Module 12 — Serverless Architecture on AWS

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Segment 1: What Is Serverless?

Welcome back to CIS-4334. Module 12 is about serverless architecture — one of the highest-impact topics on the SAA-C03 exam and one of the most practical skills you can take into any AWS role.

Let's clear up a common misconception first. Serverless does not mean no servers exist. It means you no longer manage servers. AWS handles all provisioning, patching, scaling, and capacity planning. You provide code and configuration. AWS provides execution.

The benefits are significant:

- No infrastructure to manage or patch
- Automatic scaling from zero to millions of requests
- Pay-per-execution billing — you pay only when code runs
- Built-in high availability across multiple Availability Zones

The trade-offs are also real:

- Cold start latency for infrequently invoked functions
- 15-minute maximum execution duration for Lambda
- Stateless execution — no persistent local storage between invocations
- Vendor lock-in on proprietary APIs

For the SAA-C03 exam, the primary serverless services are Lambda, API Gateway, SQS, SNS, EventBridge, Step Functions, and DynamoDB Streams. This module covers each one in depth.

---

## Segment 2: AWS Lambda — Execution Model

Lambda is the compute engine of serverless AWS. You upload a deployment package, choose a runtime, set memory and timeout, and attach an event trigger.

**Runtime options** include Python, Node.js, Java, .NET, Go, Ruby, and custom runtimes via the Lambda Runtime API. Custom runtimes let you use any language that can read from and write to standard input/output.

**Memory and CPU.** You configure memory from 128 MB to 10,240 MB in 1 MB increments. CPU is allocated proportionally to memory. A 1,769 MB function receives exactly one full vCPU. To maximize CPU-intensive workloads, allocate higher memory.

**Timeout.** Functions run for 1 second to 15 minutes maximum. Design your functions to complete well within this limit. For long-running jobs, use Step Functions, ECS, or Batch instead.

**Execution environment lifecycle.** When Lambda receives an invocation, it checks for a warm (already-initialized) execution environment. If one is available, it reuses it — the handler runs immediately. If not, Lambda must initialize a new environment. This initialization is called a **cold start**.

---

## Segment 3: Cold Starts and Provisioned Concurrency

Cold starts happen when Lambda creates a fresh execution environment. The initialization phase includes:

1. Downloading the deployment package or container image
2. Starting the runtime (Node.js, Python JVM, .NET CLR, etc.)
3. Running initialization code outside the handler function

For Python and Node.js functions with small packages, cold starts are typically 100–300 milliseconds. For Java and .NET with large packages, cold starts can reach 1–3 seconds or more.

**Strategies to minimize cold start impact:**

- **Provisioned Concurrency** — pre-initializes a specified number of execution environments. They are always warm, eliminating cold starts for those invocations. This has an additional cost.
- **Lambda SnapStart** — available for Java 11+ runtimes. Takes a snapshot of the initialized execution environment and restores it instead of repeating initialization. Dramatically reduces Java cold starts.
- **Keep packages small** — fewer dependencies means faster downloads and runtime startup.
- **Move heavy initialization outside the handler** — connections to databases, loading ML models, and parsing large configs should be done at the module level so they are reused across warm invocations.

**Concurrency model.** Lambda creates additional execution environments in parallel to handle concurrent invocations. Each environment processes one request at a time.

Two types of concurrency limits exist:

- **Reserved Concurrency** — sets a maximum AND guarantees that capacity for the function. Other functions cannot use those slots. Setting it to zero effectively disables the function.
- **Provisioned Concurrency** — pre-warms a set number of environments. Different from Reserved — Provisioned is about latency, Reserved is about capacity allocation.

The account-level concurrency limit defaults to 1,000 per region. Submit a support request to increase it.

---

## Segment 4: Lambda Triggers and Event Sources

Lambda integrates with dozens of AWS services as event sources. For SAA-C03, these are the most critical:

**Synchronous invocation sources** — the caller waits for Lambda to complete and return a response:

- API Gateway (REST, HTTP, WebSocket)
- Application Load Balancer
- Cognito (pre-token generation, custom auth)
- Lex, Alexa Skills

**Asynchronous invocation sources** — the caller hands off the event and Lambda processes it independently. Retries on failure (twice by default):

- S3 event notifications (object created, deleted)
- SNS (topic subscription)
- EventBridge rules
- CloudFormation custom resources
- CodeCommit, CodePipeline

**Poll-based (stream/queue) sources** — Lambda polls on your behalf:

- SQS — Lambda polls the queue, batches messages, invokes function
- DynamoDB Streams — processes change records in order
- Kinesis Data Streams — processes shards in parallel
- Managed Streaming for Kafka (MSK)

Understanding which invocation model applies to each source is tested directly on the exam.

---

## Segment 5: Lambda Layers and Destinations

**Lambda Layers** are versioned ZIP archives containing shared libraries, custom runtimes, configuration files, or binary assets. Layers let multiple functions share common dependencies without duplicating them in each deployment package.

Each function can attach up to five layers. Layers are extracted to the `/opt` directory in the execution environment. The combined unzipped size of all layers and the function code must not exceed 250 MB.

Layers are immutable — once published, a version cannot be changed. Create a new version to update a layer.

Use case: A team of five Lambda functions all use the same data-processing library and common logging utilities. Package those into a layer instead of including them in each function's ZIP file.

**Lambda Destinations** configure where Lambda routes the result of an asynchronous invocation:

- On success: SQS queue, SNS topic, EventBridge event bus, or another Lambda function
- On failure: SQS queue, SNS topic, EventBridge event bus, or another Lambda function

Destinations are preferred over Dead-Letter Queues (DLQs) for asynchronous invocations because they provide richer metadata (including the full request and response) and support both success and failure paths. DLQs only handle failures.

---

## Segment 6: Amazon API Gateway

API Gateway is the managed entry point for serverless APIs. Three API types exist:

**REST APIs** — the original API Gateway API type. Supports all features: caching, request/response transformation via Velocity Template Language (VTL) mapping templates, usage plans, API keys, and custom domain names with ACM certificates.

**HTTP APIs** — newer and simpler. Lower latency (approximately 60% faster) and lower cost (approximately 70% cheaper) than REST APIs. Supports JWT authorizers natively (Cognito and third-party OIDC providers). Recommended for Lambda proxy integrations when you do not need REST API's advanced transformation features.

**WebSocket APIs** — persistent bidirectional connections. Used for real-time applications: chat, live dashboards, collaborative tools, streaming data display.

**Authorizer types:**

- **IAM Authorizer** — requires callers to sign requests with AWS Signature Version 4. Best for service-to-service calls within AWS.
- **Cognito User Pool Authorizer** — validates JWTs issued by Amazon Cognito. Simple and built-in for user authentication.
- **Lambda Authorizer** — a custom Lambda function validates the request (token or request parameters) and returns an IAM policy. Use for custom auth systems, OAuth token introspection, or legacy auth.

**Throttling and caching.** Default account-level throttle: 10,000 requests per second steady-state, burst up to 5,000. Configure per-stage and per-method throttling for finer control. REST APIs support response caching per stage: 0.5 GB to 237 GB, TTL 0–3,600 seconds.

---

## Segment 7: Amazon SQS

SQS is a fully managed message queuing service. It decouples producers from consumers, enabling independent scaling and fault tolerance.

**Queue types:**

**Standard Queue** — near-unlimited throughput (no TPS limit per queue). Messages are delivered at least once and may be delivered out of order (best-effort ordering). Use when throughput matters more than strict ordering and deduplication.

**FIFO Queue** — exactly-once processing (within a message group) and strict first-in-first-out ordering. Throughput is 300 transactions per second (TPS) without batching, 3,000 TPS with batching. Use for financial transactions, inventory management, and any workflow where order and deduplication are critical.

**Key SQS configuration parameters:**

- **Visibility Timeout** — after a consumer receives a message, it becomes invisible to other consumers for this duration. Default: 30 seconds. Range: 0 seconds to 12 hours. Set this to slightly longer than your processing time.
- **Message Retention Period** — how long SQS retains messages. Default: 4 days. Range: 1 minute to 14 days.
- **Dead-Letter Queue (DLQ)** — a separate queue that receives messages exceeding the `maxReceiveCount`. Isolates poison-pill messages that repeatedly fail processing.
- **Long Polling** — `WaitTimeSeconds` (1–20 seconds). Lambda and consumers wait for messages rather than immediately returning empty responses. Reduces API calls and cost.
- **Maximum Message Size** — 256 KB. For larger payloads, use the SQS Extended Client Library to store the payload in S3 and send a reference.

---

## Segment 8: Amazon SNS and the Fan-Out Pattern

SNS is a fully managed pub/sub messaging service. A publisher sends a message to a topic; SNS immediately pushes it to all subscribed endpoints.

**Subscription protocols:** Lambda, SQS, HTTP/HTTPS endpoints, email, SMS, mobile push notifications (APNS, GCM/FCM), and Kinesis Data Firehose.

**Message filtering.** Subscriptions can include a filter policy — a JSON object with attribute conditions. SNS evaluates incoming message attributes against the filter and delivers only matching messages to that subscriber. This reduces cost and unnecessary processing at the consumer.

**Fan-out pattern with SQS.** This is a critical SAA-C03 pattern:

1. Event source publishes to an SNS topic
2. SNS fans out to multiple SQS queues simultaneously
3. Each SQS queue feeds a different downstream processing pipeline

Benefits: publishers are decoupled from all consumers, messages are durably buffered in SQS, each consumer scales independently, and individual consumer failures do not block others.

**SNS FIFO topics** support ordered delivery and deduplication to FIFO SQS queue subscribers. Use for cases where ordered fan-out is required.

---

## Segment 9: Amazon EventBridge and AWS Step Functions

**Amazon EventBridge** is a serverless event bus for event-driven architecture. Events flow from sources to rules, and rules route matching events to targets.

Event sources include:

- AWS services (over 200 service integrations)
- Custom applications (via `PutEvents` API)
- Third-party SaaS partners (Zendesk, Salesforce, Datadog, etc.) via partner event buses

Rules use JSON pattern matching. A rule fires when an incoming event's structure matches the pattern. Targets include Lambda, Step Functions, SQS, SNS, ECS tasks, Kinesis, and API Gateway.

**EventBridge Scheduler** replaces CloudWatch Events cron. Create schedules for one-time or recurring invocations without managing rules.

**EventBridge Pipes** connect a source (SQS, DynamoDB Streams, Kinesis) directly to a target with optional filtering and enrichment via Lambda.

**AWS Step Functions** orchestrates distributed workflows. Define a state machine in Amazon States Language (ASL) JSON.

**Standard vs. Express Workflows:**

- Standard: up to 1-year duration, exactly-once execution, full audit history in Step Functions console. Priced per state transition.
- Express: up to 5-minute duration, at-least-once execution, high throughput (100,000 state transitions per second). Priced per execution duration. Logs sent to CloudWatch.

Use Step Functions when your workflow involves multiple steps, error handling, conditional branching, parallel execution, or human approval steps.

---

## Segment 10: DynamoDB Streams and Serverless Patterns

**DynamoDB Streams** capture a time-ordered log of item-level changes. Four stream view types:

- `KEYS_ONLY` — only the key attributes of modified items
- `NEW_IMAGE` — the entire item after modification
- `OLD_IMAGE` — the entire item before modification
- `NEW_AND_OLD_IMAGES` — both before and after states

Lambda reads from DynamoDB Streams using an event source mapping. Lambda polls the stream shard, batches records, and invokes your function. On failure, Lambda retries the batch until it succeeds or expires, then can route to a DLQ or Destination.

**Common use cases:** real-time aggregation, cross-region replication, cache invalidation, audit logging, triggering downstream workflows on data change.

**Serverless architectural patterns for SAA-C03:**

The **Event-Driven Microservices** pattern: services communicate via events on EventBridge or SNS/SQS rather than direct synchronous calls. Loosely coupled, independently deployable.

The **Saga Pattern** using Step Functions: coordinates multi-step distributed transactions with compensating transactions on failure.

The **CQRS Pattern**: Command side writes via Lambda to DynamoDB; Query side reads from a read-optimized store populated by DynamoDB Streams.

---

## Closing Summary

You now have a complete mental model of serverless architecture on AWS. Lambda handles event-driven compute with cold starts mitigated by Provisioned Concurrency. API Gateway provides the managed HTTP entry point. SQS decouples and buffers; SNS broadcasts and fans out. EventBridge routes events across AWS and SaaS. Step Functions orchestrates complex workflows. DynamoDB Streams enables reactive data pipelines.

In your lab this week, you will deploy a serverless order pipeline: API Gateway receives orders, Lambda validates and stores them in DynamoDB, DynamoDB Streams triggers fulfillment, and Step Functions orchestrates the multi-step workflow. See you in the lab instructions.

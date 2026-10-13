# Quiz: Module 12 — Serverless Architecture on AWS

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Answer key and distractor analysis follow each question.

---

## Question 1

A Lambda function processes images uploaded to S3. A Python library takes 4 seconds to initialize. Users report that occasional requests take 6–7 seconds while most complete in under 2 seconds. Which action MOST effectively eliminates the long-tail latency?

- A. Increase the Lambda function memory to 10,240 MB
- B. Enable Provisioned Concurrency for the Lambda function
- C. Package the library as a Lambda Layer
- D. Set Reserved Concurrency to 100

### Q1 Answer: B

### Q1 Analysis

A is incorrect. Increasing memory speeds up CPU-bound work but does not eliminate cold starts. Slow initialization is the problem, not processing speed.

B is correct. Provisioned Concurrency pre-initializes execution environments including all Init phase code. These environments are always warm, eliminating cold start latency.

C is incorrect. Lambda Layers reorganize deployment packages but do not eliminate initialization time. The library still runs during the Init phase whether it arrives via a layer or a ZIP.

D is incorrect. Reserved Concurrency caps maximum concurrent executions. It does not warm environments or prevent cold starts.

---

## Question 2

An e-commerce platform publishes an `OrderPlaced` event that must trigger three independent downstream systems simultaneously — inventory, fulfillment, and analytics. Each system must process the event independently without affecting the others. Which architecture BEST satisfies these requirements?

- A. Publish to an SQS FIFO queue; all three systems poll the same queue
- B. Publish to an SNS topic with three SQS queue subscriptions, one per system
- C. Publish to EventBridge; create one rule targeting all three Lambda functions directly
- D. Chain three Lambda functions so each passes the event to the next

### Q2 Answer: B

### Q2 Analysis

A is incorrect. A single SQS queue allows only one consumer to process each message. The three systems cannot independently consume the same message from one queue.

B is correct. The SNS fan-out to SQS pattern delivers the event to all three queues simultaneously. Each queue buffers messages independently, and each system scales and fails independently.

C is incorrect. Direct Lambda invocation from EventBridge provides no durable buffering. A downstream Lambda failure loses the event unless a DLQ is configured on each function separately.

D is incorrect. Chaining Lambda functions creates tight coupling and sequential processing. If one function fails, downstream functions do not execute.

---

## Question 3

A developer needs a Lambda function to compute the exact delta of attribute changes on every DynamoDB item update, requiring both old and new values. Which DynamoDB Streams view type should be configured?

- A. KEYS_ONLY
- B. NEW_IMAGE
- C. OLD_IMAGE
- D. NEW_AND_OLD_IMAGES

### Q3 Answer: D

### Q3 Analysis

A is incorrect. KEYS_ONLY provides only key attributes — no attribute values before or after the change.

B is incorrect. NEW_IMAGE provides the full item after modification but does not include the previous state.

C is incorrect. OLD_IMAGE provides the full item before modification but does not include the new state.

D is correct. NEW_AND_OLD_IMAGES includes the complete before-state and after-state of each modified item, enabling delta computation.

---

## Question 4

A company's REST API on API Gateway and Lambda spikes to 8,000 requests per second during flash sales. Backend Lambda functions must never receive more than 2,000 concurrent executions to protect downstream databases. Which configuration achieves this?

- A. Set API Gateway stage throttling to 2,000 RPS
- B. Set Reserved Concurrency on the Lambda function to 2,000
- C. Enable Provisioned Concurrency set to 2,000
- D. Set the Lambda timeout to 1 second

### Q4 Answer: B

### Q4 Analysis

A is incorrect. API Gateway throttling limits requests per second (rate) but does not cap concurrent Lambda executions. High concurrency can still occur when many overlapping requests are in flight simultaneously.

B is correct. Reserved Concurrency sets a hard maximum on concurrent executions for the function. Invocations exceeding this limit receive a 429 throttling error.

C is incorrect. Provisioned Concurrency pre-warms environments but does not cap concurrency. The function can still exceed 2,000 concurrent executions dynamically.

D is incorrect. Reducing timeout causes functions to fail faster but does not limit the number of concurrent invocations.

---

## Question 5

A company uses an HTTP API on API Gateway. They want to allow only requests from users authenticated through their corporate identity provider using OAuth 2.0 JWT tokens. Which authorizer type is MOST appropriate?

- A. IAM authorizer
- B. Cognito User Pool authorizer
- C. Lambda authorizer
- D. JWT authorizer (HTTP API native)

### Q5 Answer: D

### Q5 Analysis

A is incorrect. IAM authorizers require AWS Signature Version 4 signing. Corporate IdP users do not generate AWS credentials.

B is incorrect. Cognito User Pool authorizers validate tokens issued by Amazon Cognito only. The scenario specifies a third-party corporate IdP.

C is incorrect. A Lambda authorizer could work but requires writing and maintaining custom authorization code. HTTP APIs support native JWT authorizers that validate OIDC/OAuth 2.0 JWTs natively.

D is correct. HTTP API JWT authorizers validate JWTs from any OIDC-compliant identity provider by configuring the `issuer` and `audience` claims. No custom Lambda code is required.

---

## Question 6

A financial services application requires payment processing messages to be handled in strict first-in-first-out order with no duplicate processing at 500 messages per second. Which SQS configuration should be used?

- A. Standard queue with a DLQ
- B. FIFO queue without batching
- C. FIFO queue with batching (10 messages per batch)
- D. Standard queue with Visibility Timeout set to 0

### Q6 Answer: C

### Q6 Analysis

A is incorrect. Standard queues provide best-effort ordering, not strict FIFO. Duplicate messages can occur. A DLQ does not change delivery semantics.

B is incorrect. FIFO queues without batching support only 300 TPS. At 500 TPS the queue would throttle.

C is correct. FIFO queues with batching support up to 3,000 TPS, covering 500 TPS. FIFO queues guarantee strict ordering and exactly-once processing within each message group.

D is incorrect. Setting Visibility Timeout to 0 on a Standard queue does not provide ordering or exactly-once delivery.

---

## Question 7

An application uses Step Functions to coordinate a multi-step order workflow. A business analyst must review and approve high-value orders before fulfillment proceeds. Approval may take up to 48 hours. Which Step Functions feature handles this requirement?

- A. Wait state with a 48-hour duration
- B. Task state with `.waitForTaskToken` integration
- C. Choice state with a 48-hour timeout
- D. Express Workflow with a human activity task

### Q7 Answer: B

### Q7 Analysis

A is incorrect. A Wait state pauses for a fixed duration and resumes automatically — it does not wait for human input or external confirmation.

B is correct. The `.waitForTaskToken` pattern pauses execution until an external system calls `SendTaskSuccess` or `SendTaskFailure` with the task token. Standard Workflows can wait up to one year.

C is incorrect. Choice states evaluate data conditions to branch — they do not pause for external input.

D is incorrect. Express Workflows have a maximum duration of 5 minutes. A 48-hour approval window requires a Standard Workflow.

---

## Question 8

A Lambda function triggered by SQS processes batches of 10 messages. One specific message format causes an unhandled exception. All 10 messages are retried repeatedly. Which change ensures only the failing message is retried while the other 9 are deleted?

- A. Set the SQS Visibility Timeout to 0 seconds
- B. Return `batchItemFailures` in the Lambda response reporting only the failing message ID
- C. Switch from SQS Standard to a FIFO queue
- D. Increase the Lambda timeout to 15 minutes

### Q8 Answer: B

### Q8 Analysis

A is incorrect. Setting Visibility Timeout to 0 makes all messages immediately visible again after receipt, worsening the retry storm for all 10 messages.

B is correct. Returning `batchItemFailures` with the failing message's `itemIdentifier` tells Lambda to delete successfully processed messages and return only the failing one to the queue for retry.

C is incorrect. Switching queue type changes ordering and deduplication but does not affect partial batch failure handling. FIFO queues block subsequent message groups when one fails.

D is incorrect. Extending the timeout gives more execution time but does not change how the function reports partial failures to SQS.

---

## Question 9

A company uses EventBridge to route order events to different Lambda functions based on the `orderType` attribute — `RETAIL` to Lambda A and `WHOLESALE` to Lambda B. Which EventBridge feature enables this content-based routing without a routing Lambda?

- A. Event bus resource policy
- B. Two rules with event pattern matching on the `orderType` field
- C. Schema Registry auto-discovery
- D. EventBridge Pipes with a filter

### Q9 Answer: B

### Q9 Analysis

A is incorrect. Event bus resource policies control which AWS accounts can publish to the bus — they are not used for content-based routing.

B is correct. Create two EventBridge rules: one matching `{"detail": {"orderType": ["RETAIL"]}}` targeting Lambda A, and one matching `{"detail": {"orderType": ["WHOLESALE"]}}` targeting Lambda B. EventBridge evaluates both rules against every event.

C is incorrect. Schema Registry discovers and documents event schemas but does not route events.

D is incorrect. EventBridge Pipes connect a single source to a single target. Two pipes would still be required, adding complexity compared to standard rules.

---

## Question 10

A Lambda function's 180 MB deployment package causes 3.2-second cold starts for a real-time API. Provisioned Concurrency has not been approved due to cost. Which TWO actions would reduce cold start duration? (Select TWO.)

- A. Move infrequently used library imports to inside the handler function
- B. Increase Reserved Concurrency from 10 to 100
- C. Remove unused dependencies to reduce the deployment package size
- D. Switch to a container image deployment format
- E. Change the function timeout from 30 seconds to 15 minutes

### Q10 Answer: A and C

### Q10 Analysis

A is correct. Moving heavy imports inside the handler defers their execution out of the Init phase, reducing initialization duration on cold starts.

B is incorrect. Increasing Reserved Concurrency changes the capacity cap for the function but does not affect initialization time.

C is correct. Smaller packages download faster during environment initialization. Removing unused libraries directly reduces the Init phase duration.

D is incorrect. Container images support larger packages but do not inherently reduce initialization time and can increase it due to image-pull overhead.

E is incorrect. Changing the timeout affects maximum execution duration per invocation, not cold start initialization time.

---

### Question 11 (5 points)

A company runs a Lambda function that processes customer orders. The function is invoked synchronously via API Gateway. During a traffic spike, 500 concurrent requests arrive simultaneously. The function has Reserved Concurrency set to 100. What happens to the remaining 400 requests?

A. They queue automatically in Lambda's internal buffer and execute when concurrency is available

B. They are throttled and API Gateway returns a 429 Too Many Requests response to the caller

C. Lambda automatically scales beyond the Reserved Concurrency limit to handle all 500 requests

D. They route to the Dead-Letter Queue configured on the function

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Lambda does not have an internal request buffer for synchronous invocations. When Reserved Concurrency is exhausted, synchronous invocations are immediately throttled — they are not queued.
- B is correct. Reserved Concurrency is a hard cap. When all 100 reserved concurrent executions are in use, additional synchronous invocations are throttled. API Gateway translates the Lambda throttle response into an HTTP 429 error returned to the caller.
- C is incorrect. Reserved Concurrency explicitly prevents scaling beyond the configured limit. It is a ceiling, not a soft target. Lambda will not exceed Reserved Concurrency regardless of available account-level concurrency.
- D is incorrect. Dead-Letter Queues only apply to asynchronous Lambda invocations (event-driven, not synchronous). Synchronously throttled requests are returned as errors to the caller, not routed to a DLQ.

---

### Question 12 (5 points)

A developer wants a Lambda function to process S3 object creation events but only for `.jpg` files in a specific prefix. Where should the filtering be configured?

A. Inside the Lambda function code using an if-statement that checks the S3 key and returns early for non-matching objects

B. In the S3 event notification configuration using prefix and suffix filters before the event reaches Lambda

C. In an EventBridge rule with an event pattern matching the S3 event source and object key

D. In an SQS queue between S3 and Lambda, with a message filter policy

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. While filtering inside the function is technically possible, it still invokes Lambda for every S3 object creation event — consuming invocation capacity and cost. Filtering at the source eliminates unnecessary invocations.
- B is correct. S3 event notifications support native prefix and suffix filter rules. Configuring `prefix: images/` and `suffix: .jpg` ensures that only matching object creation events trigger Lambda. No unnecessary invocations occur for non-matching objects.
- C is incorrect. EventBridge S3 integration is possible but requires enabling S3 EventBridge notifications, adding latency and architectural complexity. Native S3 notification filters are the simpler, purpose-built solution for this use case.
- D is incorrect. SQS does not support message filtering based on S3 object key attributes. SQS message filter policies apply to SNS subscription attributes, not S3 event content.

---

### Question 13 (5 points)

A Step Functions Standard workflow orchestrates an order fulfillment process. One state calls an external payment API that occasionally takes up to 72 hours to respond. What is the correct way to handle this long-running external call in Step Functions?

A. Increase the Lambda function timeout to 72 hours to wait for the payment API response

B. Use a Step Functions Wait state with a fixed 72-hour timer

C. Use the Step Functions callback pattern with a task token — pause the workflow and resume it when the external system sends a callback

D. Use Step Functions Express Workflows instead, which support longer execution times for external integrations

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Lambda has a maximum timeout of 15 minutes. A 72-hour wait inside a Lambda function is technically impossible, and even shorter waits would waste compute cost while the function is idle.
- B is incorrect. A Wait state pauses the workflow for a fixed duration, but it resumes after the timer expires regardless of whether the external API has responded. This would not correctly wait for the actual payment confirmation.
- C is correct. The callback pattern (`.waitForTaskToken`) pauses the workflow at that state and returns a task token to the external system. The workflow resumes only when the external system calls `SendTaskSuccess` or `SendTaskFailure` with the token — handling the 72-hour window without consuming compute resources.
- D is incorrect. Step Functions Express Workflows have a maximum execution duration of 5 minutes, making them unsuitable for workflows requiring 72-hour waits. Standard Workflows support up to 1 year of execution duration.

---

### Question 14 (5 points)

An API Gateway REST API is deployed to a stage. A developer changes a Lambda function behind one of the routes but the API continues returning old responses. What is the most likely cause?

A. The Lambda function alias used by API Gateway points to the old function version

B. API Gateway has a stage-level cache enabled and is returning cached responses

C. The Lambda function's Reserved Concurrency is set to zero

D. The API Gateway stage has not been redeployed after the Lambda change

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Lambda aliases and versions would cause this if the API Gateway integration used an explicit version ARN rather than `$LATEST`. However, this is less common than the caching scenario described and not the most likely cause when a deployed change isn't reflected.
- B is correct. API Gateway REST APIs support response caching at the stage level with a configurable TTL (default 300 seconds). If caching is enabled, API Gateway returns cached responses without invoking Lambda until the TTL expires or the cache is invalidated. This is the most likely cause of stale responses after a Lambda update.
- C is incorrect. Reserved Concurrency of zero would throttle all Lambda invocations, resulting in 429 errors — not stale responses from the old function.
- D is incorrect. Lambda function changes (code updates to `$LATEST`) do not require API Gateway redeployment. The API Gateway integration continues to invoke the updated Lambda code automatically. Redeployment is required only when API Gateway configuration changes (routes, authorizers, integrations).

---

### Question 15 (5 points)

A company uses Lambda to process messages from an SQS Standard queue. The Lambda function fails on 10% of messages due to a parsing error. These messages reappear in the queue after the visibility timeout and are retried. What is the correct configuration to prevent these messages from being retried indefinitely?

A. Increase the Lambda function memory to handle larger payloads without parsing errors

B. Configure a Dead-Letter Queue on the SQS source queue with a maxReceiveCount of 3

C. Enable Lambda Destinations with an OnFailure destination pointing to an S3 bucket

D. Set the Lambda function Reserved Concurrency to 1 to process messages sequentially

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The failures are due to parsing errors — they are data errors, not resource constraints. Increasing memory would not fix messages that fail due to malformed content.
- B is correct. Configuring a DLQ on the SQS queue with a `maxReceiveCount` (redrive policy) causes messages that fail processing `maxReceiveCount` times to be moved to the DLQ automatically. This prevents infinite retry loops for persistently failing messages and allows them to be inspected and reprocessed separately.
- C is incorrect. Lambda Destinations (OnFailure) apply to asynchronous Lambda invocations. When Lambda is invoked by an SQS event source mapping, the SQS queue's own DLQ configuration — not Lambda Destinations — controls message retry behavior.
- D is incorrect. Setting concurrency to 1 processes messages one at a time but does not prevent retry loops. Failed messages will still be re-queued and retried indefinitely without a DLQ.

---

### Question 16 (5 points)

A company wants to expose a serverless API that authenticates callers using JWTs from their corporate identity provider (IdP). They need to validate the JWT without writing custom Lambda code. Which API Gateway feature handles this?

A. API Gateway resource policies that allow requests from the IdP's IP address range

B. API Gateway Lambda authorizer that calls the IdP to validate each token

C. API Gateway JWT authorizer (HTTP API) configured with the IdP's issuer URL and audience

D. API Gateway usage plans with API keys distributed to the IdP

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Resource policies control which AWS accounts, VPCs, or IP addresses can call the API — they do not validate JWT tokens or authenticate individual users.
- B is incorrect. A Lambda authorizer can validate JWTs but requires writing and maintaining custom Lambda code, adding operational overhead. When the IdP supports OIDC discovery (which most modern IdPs do), the native JWT authorizer handles validation without custom code.
- C is correct. API Gateway HTTP APIs support native JWT authorizers that validate tokens using the IdP's OIDC discovery endpoint. The authorizer verifies the signature, issuer, audience, and expiry automatically — no Lambda code required. This is the correct approach for OIDC/OAuth2 JWT validation.
- D is incorrect. API keys in usage plans are opaque strings for identifying API consumers and enforcing rate limits — they are not authentication tokens and cannot validate identity provider JWTs.

---

### Question 17 (5 points)

A Lambda function writes processed results to DynamoDB. During load testing, the function receives ThrottlingException errors from DynamoDB on write operations. The Lambda function has no retry logic. What is the BEST architectural fix?

A. Increase Lambda Reserved Concurrency to match DynamoDB write capacity

B. Add an SQS queue between the event source and Lambda to buffer writes, and add DynamoDB retry logic with exponential backoff in the Lambda function

C. Switch the DynamoDB table from provisioned to on-demand capacity mode

D. Increase the Lambda function timeout to allow writes to complete after throttling

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Lambda concurrency and DynamoDB write capacity are independent. Matching Lambda concurrency to DynamoDB WCUs does not prevent throttling if write rates exceed provisioned capacity — it just ensures Lambda is available to attempt (and fail) the writes.
- B is incorrect. Adding SQS buffering helps if the issue is burst traffic exceeding DynamoDB capacity temporarily, but it does not fix the root cause and adds architectural complexity. On-demand capacity is a simpler fix if the workload is variable.
- C is correct. Switching to on-demand capacity mode allows DynamoDB to scale write capacity automatically with traffic. This eliminates ThrottlingExceptions from capacity exhaustion without requiring SQS buffering or application-level retry tuning for the provisioned capacity scenario described.
- D is incorrect. Increasing Lambda timeout allows a single invocation to wait longer, but DynamoDB throttling under sustained load will not resolve itself within the timeout window. Timeout changes address response latency, not write capacity limitations.

---

### Question 18 (5 points)

A developer is designing a serverless event pipeline. Multiple downstream services (billing, inventory, notifications) each need to receive and independently process every order event. Each service has different processing speeds. Which architecture correctly implements this?

A. API Gateway → Lambda → synchronous calls to each downstream service in sequence

B. API Gateway → Lambda → SNS topic with one SQS queue per downstream service subscribed to the topic

C. API Gateway → Lambda → single SQS FIFO queue shared by all three downstream services

D. API Gateway → Lambda → EventBridge event bus with a separate Lambda per downstream service

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Synchronous sequential calls mean a failure or slowdown in one downstream service blocks or delays all others. Services are tightly coupled and do not process independently.
- B is correct. The SNS-to-SQS fan-out pattern delivers a copy of each message to every subscribed SQS queue. Each downstream service has its own queue and processes at its own pace, independently of others. A failure in one service does not affect others, and messages are durably stored in each queue.
- C is incorrect. A single shared FIFO queue means only one service consumes each message — messages are not duplicated per consumer. Shared queues are for competing consumer patterns, not fan-out.
- D is incorrect. EventBridge is suitable for content-based routing to different targets, but adds complexity compared to the direct SNS-SQS fan-out pattern when all consumers need every event and independent buffering is required per consumer.

---

### Question 19 (5 points)

A company's Lambda function is triggered by DynamoDB Streams to process item changes. The function must process changes in the exact order they were made to each item. A developer notices that some items are being processed out of order. What is the most likely cause?

A. The DynamoDB table does not have Streams enabled with the NEW_AND_OLD_IMAGES stream view type

B. The Lambda event source mapping is processing records from multiple shards in parallel, and items for the same key can land in different shards

C. The Lambda function's Reserved Concurrency is too high, causing parallel processing of the same shard

D. DynamoDB Streams does not guarantee ordering — Kinesis Data Streams should be used instead

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The stream view type (KEYS_ONLY, NEW_IMAGE, OLD_IMAGE, NEW_AND_OLD_IMAGES) controls what data is included in stream records but does not affect ordering guarantees.
- B is correct. DynamoDB Streams are sharded. Within a single shard, records are ordered. However, items with different partition keys can be distributed across multiple shards. Lambda processes each shard sequentially but processes multiple shards in parallel — so items in different shards can be processed concurrently and out of relative order across partition keys. Items for the same partition key always land in the same shard and are processed in order.
- C is incorrect. Reserved Concurrency limits total concurrent Lambda executions. The Lambda event source mapping for DynamoDB Streams processes one batch per shard at a time — Reserved Concurrency does not cause parallel processing within the same shard.
- D is incorrect. DynamoDB Streams does guarantee ordering within a shard (per partition key). The issue is cross-shard parallelism, not a fundamental ordering limitation of DynamoDB Streams itself.

---

### Question 20 (5 points)

A company needs to run a nightly data aggregation job that queries 50 million DynamoDB records and produces a summary report. The job takes approximately 45 minutes. Lambda is proposed as the compute layer. What is the critical limitation that makes Lambda unsuitable without architectural changes?

A. Lambda cannot query DynamoDB — it can only be triggered by DynamoDB Streams

B. Lambda has a maximum execution timeout of 15 minutes, which is insufficient for a 45-minute job

C. Lambda does not support the memory required to process 50 million records in a single invocation

D. Lambda cannot be invoked on a schedule — EventBridge rules only support API calls, not Lambda

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Lambda can query DynamoDB using the AWS SDK from within the function code. Lambda can use Scan, Query, and all DynamoDB API operations. Being triggered by DynamoDB Streams is one invocation model, not a constraint on what Lambda can access.
- B is correct. Lambda has an absolute maximum execution timeout of 15 minutes. A job requiring 45 minutes cannot run as a single Lambda invocation. The architectural fix is to either break the job into parallel Lambda functions (each processing a partition of data), use Step Functions to orchestrate multiple Lambda invocations, or use a different compute service like AWS Batch or Fargate for long-running jobs.
- C is incorrect. Lambda supports up to 10 GB of memory. The 50 million records would not be loaded into memory simultaneously — they would typically be paginated through using DynamoDB Scan with pagination tokens. Memory is not the primary constraint here.
- D is incorrect. EventBridge Scheduler and EventBridge rules both support Lambda as a target on a cron schedule. Scheduled Lambda invocations are a standard, well-supported pattern.

---

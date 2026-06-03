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

# Lab Activity: Module 16 - Final Exam Submission
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

## Objective
Schedule and complete the official **AWS Certified Developer - Associate** industry certification exam, and submit your score verification report to Professor Nash.

## Instructions
1.  Register for the exam at the on-campus testing center or an authorized provider.
2.  Complete the exam.
3.  Obtain your official score report PDF showing your name, passing status, and date.
4.  Upload the official score report PDF to the Canvas LMS assignment box for this module to receive final credit.

---

## Part 9 — Challenge Exercise

### Challenge 1: Architecture Design Review — Serverless Order Processing System

Design and document a complete serverless order processing system on AWS using the services covered across Modules 08–16. This exercise tests your ability to select and connect AWS services correctly — the same skill tested in DVA-C02 architecture scenario questions.

**System requirements:**

- Customers submit orders via a REST API (authenticated)
- Orders are processed asynchronously — the API response must not block on processing
- Failed orders must not be lost — they must be retryable
- Order data must be stored durably and queryable by customer ID
- Processing latency must be visible for debugging

**Your deliverable: a written architecture document with these five sections:**

1. **Service selection** — List each AWS service you would use and one sentence explaining why it was chosen over an alternative (e.g., "DynamoDB instead of RDS because orders require flexible schema and high throughput without complex joins").

2. **Request flow** — Write a numbered step-by-step description of what happens from the moment a customer submits `POST /orders` to the moment the order record is persisted. Include the IAM role each Lambda uses and the minimum permission it needs.

3. **Failure handling** — Describe what happens when the order-processing Lambda throws an unhandled error. Name the SQS configuration values that control how many retries occur before the message is moved to the DLQ.

4. **SAM template outline** — Write a partial `template.yaml` that defines at minimum: the API Lambda function, the SQS queue, the DLQ, and the DynamoDB table. You do not need to implement the Lambda code — define only the SAM resources and their event source mappings.

5. **Observability** — Describe two CloudWatch or X-Ray actions a developer would take after receiving a report that "some orders are processing slowly." Reference specific CloudWatch Logs Insights query clauses or X-Ray features by name.

**Evaluation criteria:** Each section should demonstrate that you can justify service choices using DVA-C02 exam reasoning (partition key design, visibility timeout math, least-privilege IAM, batchItemFailures pattern, canary deployment option for the Lambda).

---

### Challenge 2: Mock Exam Timed Review

Complete the following timed review scenario. Set a timer for 26 minutes (the approximate time budget for 13 questions at 2 minutes each on the real exam). Answer each question in writing before checking the answer key below.

**Questions:**

1. A Lambda function connects to RDS PostgreSQL and times out under high concurrency. What is the most likely cause and the recommended fix?

2. An API Gateway REST API returns `502 Bad Gateway` intermittently. The Lambda logs show no errors. What is the most likely cause?

3. A DynamoDB table stores user sessions keyed on `userId` (partition key) and `sessionId` (sort key). A developer needs all sessions for a given user. Which DynamoDB operation should be used, and what parameter is required?

4. A developer needs to process S3 upload events, send an email notification, and write a record to DynamoDB — all from a single S3 `PutObject` event. What is the recommended architecture?

5. A Lambda function reads a database password from an environment variable set to a plaintext value. What is the security risk and the correct remediation?

6. A CodePipeline Deploy stage fails with "The deployment failed because no instances were found." The Build stage succeeded. What is the most likely cause?

7. A Lambda function needs to be updated with zero downtime. Ten percent of traffic should go to the new version initially. Which Lambda feature enables this?

8. A developer wants to find all Lambda invocations that took longer than 3000 ms in the last 24 hours without reading individual log streams. Which AWS service and which feature should they use?

9. A DynamoDB `Scan` on a 50 GB table is causing high costs and latency. The access pattern is always "get all orders for a given customerId." What schema change and operation change should be made?

10. An S3 static website returns `403 Forbidden` when users navigate directly to `https://example.com/dashboard`. The React app uses client-side routing. What two configuration changes fix this?

11. A Lambda function deployed in a VPC cannot reach DynamoDB. No errors appear in X-Ray for the DynamoDB segment — the call simply hangs. What is the most likely missing configuration?

12. A developer sets `maxReceiveCount: 1` on an SQS queue's DLQ redrive policy. An order-processing Lambda throws an error on the first attempt. How many times is the message processed before it moves to the DLQ?

13. A SAM template includes `TracingConfig: Active` on a Lambda function. After deployment, X-Ray shows no traces. What is the missing configuration?

---

**Answer Key:**

1. Lambda opens a new database connection per invocation, exhausting the RDS connection pool. Fix: add RDS Proxy between Lambda and RDS; Lambda connects to the proxy, which pools connections.

2. The Lambda function returned a response body that is not a string (e.g., a JavaScript object instead of `JSON.stringify(object)`). API Gateway requires `body` to be a string.

3. `Query` operation. The `KeyConditionExpression` must include the partition key (`userId = :uid`). A `Scan` would work but reads the entire table — always wrong when the partition key is known.

4. S3 Event Notification → SNS topic → three SQS queues (one per consumer: Lambda for email, Lambda for DynamoDB write, and a third if needed). The SNS fan-out pattern delivers one S3 event to all subscribers simultaneously.

5. Plaintext secrets in environment variables are visible in the AWS console and in Lambda configuration exports. Remediation: store the password in AWS Secrets Manager; retrieve it at runtime using the SDK inside the Lambda handler (or cache it outside the handler for reuse across warm invocations).

6. The CodeDeploy deployment group has no EC2 instances registered with the correct deployment group tag. Verify that the target EC2 instances have the `Name` or custom tag that matches the CodeDeploy deployment group's EC2 tag filter.

7. Lambda weighted aliases. Create a new version, then update the alias to send 10% of traffic to the new version (`weight: 0.1`) and 90% to the previous version. Use `CodeDeployLambdaAliasUpdate` in the SAM template for automatic canary promotion.

8. CloudWatch Logs Insights. Navigate to Logs Insights, select the Lambda log group (`/aws/lambda/FunctionName`), and run: `filter @duration > 3000 | stats count() by bin(1h)`.

9. Schema change: add `customerId` as the partition key (if not already) and use a GSI if `customerId` is not the current partition key. Operation change: replace `Scan` with `Query` using `KeyConditionExpression: 'customerId = :cid'`.

10. (1) In the S3 bucket static website hosting settings, set the error document to `index.html`. (2) In the CloudFront distribution, add a custom error response mapping HTTP 403 → `/index.html` with HTTP response code 200 (and the same for 404).

11. A VPC endpoint for DynamoDB is missing. Lambda functions in a VPC cannot reach AWS public endpoints (including DynamoDB) over the public internet without either a NAT Gateway or a VPC endpoint (Gateway type for DynamoDB, free).

12. Once. `maxReceiveCount: 1` means the message moves to the DLQ after 1 failed receive (the first attempt counts as the first receive). The message is processed once, fails, and is immediately moved to the DLQ.

13. The Lambda execution role is missing the `xray:PutTraceSegments` and `xray:PutTelemetryRecords` permissions. `TracingConfig: Active` enables tracing in the Lambda configuration, but the execution role must grant the IAM permissions for X-Ray to accept the trace data. Add the `AWSXRayDaemonWriteAccess` managed policy to the role.

---

### Reflection Questions

1. In Challenge 1, you chose between DynamoDB and RDS for order storage. The DVA-C02 exam frequently presents scenarios where both could work. Write a decision rule with three criteria — if all three are true, choose DynamoDB; if any one is false, evaluate RDS instead. Justify each criterion using a concrete exam scenario.

2. In Challenge 2, Question 12 asks about `maxReceiveCount: 1`. A teammate argues the message should be retried at least three times before going to the DLQ to allow for transient failures. Write the counter-argument: describe a scenario where `maxReceiveCount: 1` is the correct setting, and explain how transient failure tolerance should be implemented inside the Lambda handler rather than through SQS retry configuration.

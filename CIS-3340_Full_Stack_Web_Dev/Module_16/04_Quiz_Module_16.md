# Quiz: Module 16 - Final Exam Prep & AWS Developer Associate Certification
## Course: CIS-3340_Full_Stack_Web_Dev (AWS Certified Developer - Associate)

---

**Question 1**
A developer needs to store application secrets (database passwords, API keys) securely in AWS and have them automatically injected into a Lambda function at runtime. Which AWS service is most appropriate?
*   A) Amazon S3 — store secrets as objects in a private bucket and fetch them at runtime with `getObject()`.
*   B) AWS Secrets Manager — stores, rotates, and retrieves secrets programmatically; Lambda functions read secrets via the AWS SDK with automatic decryption.
*   C) Amazon DynamoDB — store secrets as encrypted attribute values in a table and retrieve them with `GetItem`.
*   D) AWS CloudTrail — logs all API calls including credential usage and retrieves secrets on demand.
*   **Correct Answer:** B) AWS Secrets Manager is the purpose-built service for storing, rotating, and securely retrieving application secrets. Lambda functions access secrets via the Secrets Manager SDK or the Lambda extension — no plaintext credentials in code or environment variables.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 is not designed for secrets management — there is no automatic rotation, audit trail, or fine-grained access control optimized for credentials.
    *   *Why B is correct:* AWS Secrets Manager is the DVA-C02 exam's recommended service for secret storage — it supports automatic rotation for RDS credentials and provides SDK-based retrieval.
    *   *Why C is incorrect:* DynamoDB is a database — while you could store encrypted values there, it lacks Secrets Manager's automatic rotation, IAM-scoped access policies, and native Lambda integration.
    *   *Why D is incorrect:* CloudTrail is an audit logging service — it records API calls but does not store or retrieve secrets.

---

**Question 2**
Which of the following is the most accurate description of **Core Operations** in the AWS DVA-C02 exam context?
*   A) The standard operating procedures for escalating a support ticket with AWS Premium Support when a production service is experiencing an outage.
*   B) The application development skills tested in Domain 1 of the DVA-C02 exam — including writing Lambda handlers, consuming DynamoDB via the AWS SDK, processing SQS/SNS messages, and building API Gateway integrations.
*   C) The AWS Management Console navigation skills required to configure EC2 instances, S3 buckets, and IAM policies using only the graphical interface.
*   D) The operational metrics (CPU utilization, memory usage, error rate) monitored in CloudWatch dashboards to detect production application health issues.
*   **Correct Answer:** B) The application development skills tested in Domain 1 of the DVA-C02 exam — including writing Lambda handlers, consuming DynamoDB via the AWS SDK, processing SQS/SNS messages, and building API Gateway integrations.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Support ticket escalation procedures are not tested on the DVA-C02 exam.
    *   *Why B is correct:* Domain 1 (Development with AWS Services) is the largest exam domain at ~32% of scored questions — it tests practical application development against AWS services.
    *   *Why C is incorrect:* Console navigation skills are not the focus of DVA-C02 — the exam tests architectural and coding knowledge, not click-by-click console proficiency.
    *   *Why D is incorrect:* This describes CloudWatch monitoring operations — which are tested in Domain 4 (Troubleshooting and Optimization), not "Core Operations" in the Domain 1 sense.

---

**Question 3**
A developer is designing a serverless architecture where an S3 upload automatically triggers image processing and stores results in DynamoDB. Which AWS service combination is most appropriate?
*   A) S3 upload → EC2 instance polling S3 every minute → Python script → RDS PostgreSQL
*   B) S3 upload → S3 Event Notification → AWS Lambda function → DynamoDB `PutItem`
*   C) S3 upload → AWS CloudTrail log → AWS Glue ETL job → Amazon Redshift
*   D) S3 upload → SQS FIFO queue → EC2 Auto Scaling group → ElastiCache
*   **Correct Answer:** B) S3 upload → S3 Event Notification → AWS Lambda function → DynamoDB `PutItem` — this is the standard event-driven serverless pattern for triggered processing on AWS.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* EC2 polling is the opposite of event-driven — it wastes compute resources and introduces processing latency. This pattern is not considered best practice.
    *   *Why B is correct:* S3 Event Notifications trigger Lambda functions on object creation events — Lambda processes the file and writes results to DynamoDB in a fully serverless, event-driven flow.
    *   *Why C is incorrect:* CloudTrail captures API audit logs — it is not an event streaming service for triggering processing pipelines. Glue and Redshift are analytics services for batch ETL, not real-time processing.
    *   *Why D is incorrect:* SQS to EC2 Auto Scaling is a valid pattern for queue-based scaling, but it is not serverless and does not fit the direct S3 → processing pattern as cleanly as Lambda.

---

**Question 4**
Which AWS deployment strategy releases an update to a small percentage of production traffic first, gradually increasing the percentage while monitoring error rates before completing the rollout?
*   A) Blue/Green deployment — traffic shifts 100% from the old environment (Blue) to a new identical environment (Green) in a single cutover.
*   B) All-at-once deployment — the new version is deployed simultaneously to all instances, replacing the old version immediately.
*   C) Canary deployment — a small percentage of traffic is routed to the new version first; if metrics remain healthy, the percentage increases incrementally until the rollout completes.
*   D) Immutable deployment — new instances are launched alongside old instances; traffic shifts only after all new instances pass health checks, then old instances are terminated.
*   **Correct Answer:** C) Canary deployment gradually shifts traffic to the new version in configurable increments — minimizing blast radius if the new version has bugs, because the majority of users continue on the stable version until the canary is proven healthy.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Blue/Green shifts all traffic at once to a completely separate environment — it does not gradually increase the percentage.
    *   *Why B is incorrect:* All-at-once deploys to all instances simultaneously — it is the highest-risk strategy because all users are immediately on the new version.
    *   *Why C is correct:* Canary deployments (supported by AWS CodeDeploy and Lambda aliases with weighted traffic) are the incremental, low-risk strategy described in the question.
    *   *Why D is incorrect:* Immutable deployments launch a parallel set of new instances before switching — but traffic shifts in a single step after health checks pass, not gradually.

---

**Question 5**
A full-stack application built in this course uses React (S3 + CloudFront), API Gateway, Lambda, and DynamoDB. A new requirement asks for user authentication with Google Sign-In and automatic JWT issuance. Which AWS service integrates these requirements with minimal custom code?
*   A) Build a custom OAuth 2.0 server on EC2 that handles Google sign-in and issues JWTs signed with a self-managed secret.
*   B) AWS Cognito User Pools with a Google social identity provider — Cognito handles the OAuth 2.0 flow, creates user records, and issues standardized JWTs (ID, access, and refresh tokens) automatically.
*   C) Store Google OAuth tokens directly in DynamoDB and validate them on every API request by calling the Google tokeninfo endpoint from Lambda.
*   D) Use AWS IAM Identity Center (SSO) to federate Google Workspace users into AWS console access — then derive application JWTs from the IAM session credentials.
*   **Correct Answer:** B) AWS Cognito User Pools with a Google social identity provider — Cognito manages the OAuth 2.0 flow with Google, creates user pool entries, and issues standardized JWTs that API Gateway Cognito authorizers can validate automatically.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A custom OAuth server on EC2 requires significant ongoing maintenance and security responsibility — AWS Cognito provides this capability as a managed service.
    *   *Why B is correct:* Cognito User Pools support social identity providers (Google, Facebook, Apple) and issue standardized JWTs compatible with API Gateway authorizers — the standard DVA-C02 exam answer for managed user authentication.
    *   *Why C is incorrect:* Calling the Google tokeninfo endpoint on every request adds external API latency and coupling — and does not issue application-scoped JWTs for your own API authorization.
    *   *Why D is incorrect:* IAM Identity Center is designed for AWS console/service access by employees — not for consumer application authentication.

---

### Question 6 (5 points)

A Lambda function processes SQS messages. After processing fails, the message becomes visible again and is retried three times. On the fourth attempt, it still fails. Where should failed messages be sent to prevent indefinite retries?

*   A) They should be logged to CloudWatch and deleted — repeated processing is too expensive.
*   B) They should be sent to a Dead Letter Queue (DLQ) configured on the SQS source queue. The `maxReceiveCount` parameter controls how many retries occur before the message is moved to the DLQ.
*   C) The Lambda function should catch all exceptions and return a `200` response so SQS considers every message successfully processed.
*   D) Enable SQS FIFO mode — FIFO queues automatically move failed messages to a secondary queue after three failures.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Deleting without processing means the data is lost. A DLQ preserves failed messages for later inspection and reprocessing.
    *   Why B is correct: A DLQ is the standard pattern for handling poison-pill messages. After `maxReceiveCount` retries, SQS moves the message to the DLQ where it can be inspected, debugged, and requeued.
    *   Why C is incorrect: Swallowing exceptions and returning 200 hides failures. The message is marked as processed successfully even when processing failed — the data is silently lost.
    *   Why D is incorrect: FIFO queues ensure ordering and exactly-once processing but do not automatically create a secondary failure queue. DLQ must be explicitly configured on both standard and FIFO queues.

---

### Question 7 (5 points)

A developer writes a Lambda function that initializes a PostgreSQL connection pool inside the handler function body. Under moderate load, the RDS instance starts throwing "too many connections" errors. What is the most effective fix?

*   A) Increase the RDS instance size to `db.r5.large` — larger instances accept more connections.
*   B) Move the connection pool initialization to the module level (outside the handler function). Warm Lambda execution environments reuse the existing pool. Add RDS Proxy to multiplex connections from multiple concurrent Lambda instances.
*   C) Add `await pool.end()` at the end of every Lambda invocation to close connections and free slots.
*   D) Set the Lambda reserved concurrency to `1` to ensure only one instance runs at a time.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Larger instances allow more connections, but connection exhaustion at scale is architectural, not a sizing problem. The cost is also disproportionate.
    *   Why B is correct: Module-level initialization means warm Lambda environments reuse the existing pool (zero new connections per invocation). RDS Proxy then multiplexes connections from many Lambda instances through a small pool, solving the connection count problem at scale.
    *   Why C is incorrect: Opening and closing a connection pool on every invocation is the worst possible approach — each invocation establishes and tears down connections, adding latency and consuming connection slots at peak load.
    *   Why D is incorrect: Limiting concurrency to 1 eliminates Lambda's scalability entirely. Under load, all requests queue up and timeout.

---

### Question 8 (5 points)

A developer deploys an Express REST API to AWS Lambda using the `serverless-http` adapter. A `POST /api/books` request returns `502 Bad Gateway` from API Gateway. The Lambda logs show the handler ran successfully. What is the most likely cause?

*   A) The `serverless-http` adapter is not compatible with POST requests — use `GET` only on Lambda.
*   B) The Lambda function returned a response where `body` is a JavaScript object instead of a JSON string. API Gateway requires `body` to be a string; an object causes a 502.
*   C) The Lambda function execution role lacks `execute-api:Invoke` permission.
*   D) API Gateway requires a `Content-Type: text/plain` header — JSON responses cause 502.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: `serverless-http` supports all HTTP methods. POST is fully supported.
    *   Why B is correct: The API Gateway Lambda proxy integration requires the `body` field of the Lambda response to be a string. If the function or adapter returns `body: { ... }` (an object), API Gateway cannot serialize it and returns 502. The fix is `JSON.stringify(body)`.
    *   Why C is incorrect: `execute-api:Invoke` is a permission for callers of the API, not for the Lambda function itself. The Lambda execution role needs permissions to call other AWS services (DynamoDB, S3), not to invoke itself.
    *   Why D is incorrect: API Gateway accepts `application/json` responses. There is no requirement for `text/plain`.

---

### Question 9 (5 points)

Which DynamoDB operation reads all items in a table regardless of partition key values, consumes read capacity based on the total data scanned, and should be avoided in high-traffic production applications?

*   A) `GetItem` — reads a single item by primary key; efficient but reads the whole table internally.
*   B) `Query` — efficiently retrieves all items with a given partition key.
*   C) `Scan` — reads every item in the table, consuming RCU proportional to total table size.
*   D) `TransactGetItems` — atomically reads multiple items by key; scans the table for each key.

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   Why A is incorrect: `GetItem` reads exactly one item by its full primary key — it does not scan the table.
    *   Why B is incorrect: `Query` is the efficient, key-based retrieval operation — it reads only items matching the specified partition key and optional sort key conditions.
    *   Why C is correct: `Scan` reads every item in the table. On a large table, this consumes significant read capacity, is slow, and can exhaust provisioned throughput. Use `Query` with appropriate keys and GSIs to avoid Scans.
    *   Why D is incorrect: `TransactGetItems` atomically reads up to 25 items by their specific primary keys — it is not a scan operation.

---

### Question 10 (5 points)

An S3 bucket hosts a React SPA. A user navigates directly to `https://bucket.s3-website.amazonaws.com/dashboard`. They receive an S3 error page instead of the React application. The CloudFront distribution in front of this bucket is configured correctly. What additional step resolves this issue?

*   A) Add a `dashboard.html` file to the bucket for each React route.
*   B) Configure a CloudFront custom error response that maps 403 and 404 HTTP errors to `/index.html` with an HTTP 200 status code.
*   C) Enable versioning on the S3 bucket to allow CloudFront to serve older versions of `index.html`.
*   D) Deploy the React app to Elastic Beanstalk — S3 static hosting does not support single-page applications.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Creating separate HTML files for every route defeats the purpose of a SPA — it would also break React Router's client-side navigation model.
    *   Why B is correct: When S3 cannot find a key matching `/dashboard`, it returns a 403 or 404. CloudFront custom error responses intercept these and return `index.html` (with HTTP 200), allowing React Router to handle the `/dashboard` path client-side.
    *   Why C is incorrect: S3 versioning stores multiple versions of objects — it does not affect routing behavior.
    *   Why D is incorrect: S3 static hosting is the standard deployment target for React SPAs when combined with CloudFront custom error responses.

---

### Question 11 (5 points)

An SNS topic has three SQS queue subscriptions. A Lambda function publishes one message to the topic. How many times is the message processed?

*   A) Once — SNS delivers the message to one subscriber using round-robin.
*   B) Three times — each SQS queue receives an independent copy of the message.
*   C) Zero times — SNS topics do not support SQS as a subscriber type.
*   D) Three times, but only if all three SQS queues are in the same AWS region.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: SNS is a pub/sub service, not a load balancer. All subscribers receive every message — there is no round-robin distribution.
    *   Why B is correct: SNS fan-out delivers a copy of each published message to every subscriber. Three SQS queues means three independent copies, each processed independently by their respective consumers. This is the SNS + SQS fan-out pattern.
    *   Why C is incorrect: SQS is one of the native subscriber types for SNS, along with Lambda, HTTP/HTTPS endpoints, email, and SMS.
    *   Why D is incorrect: SNS supports cross-region subscriptions. Fan-out behavior is independent of region.

---

### Question 12 (5 points)

A Lambda function has a 30-second timeout. An SQS trigger has a visibility timeout of 20 seconds. What happens when the Lambda function takes 25 seconds to process a message?

*   A) The message is deleted successfully after 25 seconds when processing completes.
*   B) After 20 seconds, the visibility timeout expires. SQS makes the message visible again — another Lambda invocation picks it up and starts processing. The original invocation may also complete, resulting in the message being processed twice.
*   C) Lambda extends the SQS visibility timeout automatically to match the Lambda timeout.
*   D) The Lambda function is terminated at 20 seconds to match the SQS visibility timeout.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: SQS does not wait for Lambda to finish — visibility timeout is set when the message is received. It expires at 20 seconds regardless of Lambda's processing time.
    *   Why B is correct: A visibility timeout shorter than the Lambda timeout causes duplicate processing. Best practice: set visibility timeout to at least 6x the Lambda timeout to allow retries without overlap. Also configure a DLQ for messages that fail repeatedly.
    *   Why C is incorrect: Lambda does not automatically extend SQS visibility timeouts. This must be done programmatically using `ChangeMessageVisibility` in the function code if needed.
    *   Why D is incorrect: Lambda runs until its own timeout (30 seconds here). SQS visibility timeout expiry and Lambda execution timeout are independent.

---

### Question 13 (5 points)

A developer generates an S3 presigned URL with `expiresIn: 3600`. An end user receives the URL 30 minutes after it was generated and tries to access it 45 minutes later. What happens?

*   A) The URL works because presigned URLs are valid for 24 hours by default.
*   B) The URL works because the 3600-second expiry is measured from the time the user first accesses it, not from when it was generated.
*   C) The URL fails with `403 Forbidden` because 75 minutes total have elapsed since generation (30-minute delivery delay + 45-minute wait), but the URL expired after 60 minutes from generation.
*   D) The URL works because the URL is valid as long as the IAM credentials used to generate it are still valid.

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   Why A is incorrect: Presigned URLs expire based on the `expiresIn` value set when the URL is generated, not a 24-hour default.
    *   Why B is incorrect: The expiry is calculated from the time of generation (when `getSignedUrl` is called), not from first access.
    *   Why C is correct: The URL was generated with a 3600-second (60-minute) lifetime. The user accesses it 75 minutes after generation — the expiry was 60 minutes, so the URL is expired and S3 returns 403.
    *   Why D is incorrect: Once the presigned URL is generated, its expiry is baked into the URL signature. Even if the IAM credentials are still valid, a URL past its `expiresIn` is rejected by S3.

---

### Question 14 (5 points)

A SAM template defines a Lambda function with `Timeout: 3` (seconds). The function calls an external API that occasionally takes 5 seconds to respond. What is the observed behavior?

*   A) Lambda automatically extends the timeout to accommodate the slow API call.
*   B) After 3 seconds, Lambda terminates the function invocation and returns an error. The invocation is logged as an error in CloudWatch with `Task timed out after 3.00 seconds`.
*   C) The function waits indefinitely until the external API responds — `Timeout` is a soft limit.
*   D) Lambda retries the function automatically with a doubled timeout on the next attempt.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Lambda does not extend timeouts dynamically. The configured timeout is a hard limit.
    *   Why B is correct: When the configured timeout is reached, Lambda forcibly terminates the execution. CloudWatch logs the `Task timed out` error. The function must be configured with a timeout greater than the maximum expected duration of all I/O operations.
    *   Why C is incorrect: Lambda timeout is a hard limit — not a guideline. Execution is forcibly stopped.
    *   Why D is incorrect: Lambda does not auto-retry on timeout or automatically adjust timeout on retry. Retry behavior depends on the event source — for API Gateway integrations, timeouts are immediately surfaced as 504 errors.

---

### Question 15 (5 points)

A developer needs to grant a Lambda function read access to a specific DynamoDB table. Following the principle of least privilege, which IAM policy is correct?

*   A) `{ "Effect": "Allow", "Action": "*", "Resource": "*" }`
*   B) `{ "Effect": "Allow", "Action": "dynamodb:*", "Resource": "arn:aws:dynamodb:us-east-1:123456789:table/Orders" }`
*   C) `{ "Effect": "Allow", "Action": ["dynamodb:GetItem", "dynamodb:Query", "dynamodb:Scan"], "Resource": "arn:aws:dynamodb:us-east-1:123456789:table/Orders" }`
*   D) `{ "Effect": "Allow", "Action": "dynamodb:GetItem", "Resource": "*" }`

*   **Correct Answer:** C
*   **Distractor Analysis:**
    *   Why A is incorrect: `Action: "*", Resource: "*"` grants administrator-level access to all AWS services. This violates least privilege and is the most dangerous policy possible.
    *   Why B is incorrect: `dynamodb:*` grants write, delete, and admin operations on the table — far more than read-only access requires.
    *   Why C is correct: Only the read operations needed (`GetItem`, `Query`, `Scan`) are allowed, scoped to the exact table ARN. This is the minimum necessary permission.
    *   Why D is incorrect: `Resource: "*"` scopes the permission to all DynamoDB tables in all accounts and regions. Scoping to the specific table ARN is required for least privilege.

---

### Question 16 (5 points)

AWS X-Ray is enabled on a Lambda function. The X-Ray service map shows the function is spending 80% of its execution time in a segment labeled `DynamoDB`. What is the most appropriate next step?

*   A) Increase the Lambda memory allocation — more memory increases CPU speed and speeds up DynamoDB calls.
*   B) Investigate whether the DynamoDB operation is a `Scan` that could be replaced with a `Query`, and consider adding a GSI or enabling DAX for read-heavy workloads.
*   C) Switch from DynamoDB to RDS PostgreSQL — relational databases are faster than NoSQL for all query types.
*   D) Add `X-Ray.setDaemonAddress()` in the Lambda function to reduce X-Ray overhead on DynamoDB calls.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Lambda memory/CPU affects compute-bound work — DynamoDB call latency is dominated by network I/O and read capacity, not Lambda CPU.
    *   Why B is correct: 80% of time in DynamoDB calls is a data access pattern problem, not a Lambda problem. A `Scan` on a large table is the most common cause of slow DynamoDB segments. Converting to `Query` with a GSI or adding DAX (in-memory caching for DynamoDB) are the correct optimizations.
    *   Why C is incorrect: This is a drastic architectural change that may not improve performance — DynamoDB at its designed access patterns is extremely fast. The issue is likely query design, not the service choice.
    *   Why D is incorrect: `setDaemonAddress` configures where X-Ray trace data is sent — it does not affect DynamoDB query latency.

---

### Question 17 (5 points)

A developer uses AWS CodePipeline with three stages: Source (CodeCommit), Build (CodeBuild), and Deploy (CodeDeploy to Lambda). The Build stage runs `npm test` and exits with code `1` because a test fails. What happens to the Deploy stage?

*   A) CodePipeline continues to the Deploy stage regardless of the Build stage exit code.
*   B) The Build stage fails and CodePipeline stops execution — the Deploy stage is not invoked. The previous deployed version continues to run.
*   C) CodePipeline skips the failing test and deploys the last successful build artifact.
*   D) CodeBuild automatically retries the build three times before failing the pipeline.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: A non-zero exit code from CodeBuild marks the Build stage as Failed. CodePipeline does not proceed to subsequent stages after a failed stage.
    *   Why B is correct: CodePipeline is sequential — a failed stage halts the pipeline. The Lambda function already in production continues running with the previously deployed version. This is precisely the value of CI/CD: catching failures before they reach production.
    *   Why C is incorrect: CodePipeline does not have a "skip failing tests" mode. The pipeline either passes all stages or stops.
    *   Why D is incorrect: CodeBuild does not auto-retry build failures. The developer must manually restart the pipeline or fix the code and push a new commit to trigger a new execution.

---

### Question 18 (5 points)

A developer wants to give 5% of production Lambda invocations to a new version while 95% continue on the stable version. Which feature enables this?

*   A) Lambda layers — attach the new version as a layer with `weight: 0.05`.
*   B) Lambda aliases with weighted routing — create a `production` alias pointing to both versions with `AdditionalVersionWeights: { "v2": 0.05 }`.
*   C) API Gateway stage variables — set `lambdaVersion: v2` on 5% of requests.
*   D) AWS CodeDeploy `Canary10Percent5Minutes` deployment configuration — deploys 10% then waits 5 minutes.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Lambda layers contain shared dependencies or code libraries — they have no weight or traffic routing capability.
    *   Why B is correct: Lambda weighted aliases allow traffic splitting between two specific Lambda versions by percentage. This is the canary deployment pattern for Lambda — 5% to the new version, 95% to the stable version. If issues are detected, the alias can be updated to 0% on the new version instantly.
    *   Why C is incorrect: API Gateway stage variables can reference Lambda aliases, but they do not provide percentage-based traffic splitting by themselves.
    *   Why D is incorrect: `Canary10Percent5Minutes` is a CodeDeploy configuration that shifts 10% initially — not 5%. Also, CodeDeploy canary shifts to 100% after the interval — it is not a persistent split like a weighted alias.

---

### Question 19 (5 points)

A developer discovers that a Lambda function's CloudWatch log group (`/aws/lambda/MyFunction`) contains logs from thousands of invocations but they need to find all invocations that logged the string `"payment failed"` in the last 24 hours. Which tool provides this capability most efficiently?

*   A) Download all log files from the CloudWatch console and use `grep` locally.
*   B) Use CloudWatch Logs Insights with a query like `fields @timestamp, @message | filter @message like /payment failed/ | sort @timestamp desc`.
*   C) Enable X-Ray on the Lambda function — X-Ray automatically indexes log message strings.
*   D) Add a CloudWatch alarm on the metric `Errors` — it will notify when "payment failed" occurs.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: Downloading gigabytes of log files for local grep is impractical at scale and incurs data transfer costs. CloudWatch Logs Insights queries run in-place on the log data.
    *   Why B is correct: CloudWatch Logs Insights is the purpose-built tool for querying log data at scale. The `filter` command matches log messages by pattern, and results are returned within seconds regardless of log volume. Time range selection (last 24 hours) is built into the interface.
    *   Why C is incorrect: X-Ray traces requests and records subsegment timing — it does not index arbitrary log message strings.
    *   Why D is incorrect: CloudWatch alarms trigger on numeric metrics (error count, latency) — not on log message content strings.

---

### Question 20 (5 points)

Throughout this course, the full-stack architecture evolved from local HTML files to a deployed cloud application. Which statement best describes the relationship between Express middleware and AWS Lambda authorizers?

*   A) They are unrelated — Express middleware is a Node.js library concept and Lambda authorizers are a cloud service configuration. They share no conceptual overlap.
*   B) Both implement the same pattern: a function receives an incoming request context, performs validation or transformation, and either passes control to the next handler or rejects the request. Express middleware calls `next(err)` to reject; a Lambda authorizer returns a Deny policy or throws an `Unauthorized` error.
*   C) Lambda authorizers replaced Express middleware — you should never use Express middleware if your API is on API Gateway.
*   D) Express middleware runs on the server; Lambda authorizers run on the client. They cover different parts of the request lifecycle.

*   **Correct Answer:** B
*   **Distractor Analysis:**
    *   Why A is incorrect: They are conceptually identical — a function that intercepts a request, validates it, and decides whether to proceed. Understanding Express middleware deeply is the best preparation for understanding Lambda authorizers.
    *   Why B is correct: This is the core conceptual connection of the course. `requireAuth` in Express and a Lambda authorizer both: (1) read a token from the request, (2) verify it, (3) either enrich the request context with user data and call next/return Allow, or reject with 401/Deny. The mechanics differ but the pattern is identical.
    *   Why C is incorrect: Express middleware and Lambda authorizers solve the same problem at different layers. Using Express on Lambda (via `serverless-http`) still uses Express middleware; Lambda authorizers can additionally guard at the API Gateway layer.
    *   Why D is incorrect: Lambda authorizers run server-side in the AWS cloud — they are not client-side components.

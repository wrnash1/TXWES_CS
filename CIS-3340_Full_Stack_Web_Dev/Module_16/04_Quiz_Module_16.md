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

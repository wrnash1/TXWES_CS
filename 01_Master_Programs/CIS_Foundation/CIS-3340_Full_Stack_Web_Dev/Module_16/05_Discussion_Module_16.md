# Discussion Forum: Module 16 — Final Exam Prep & AWS Developer Associate Certification

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This final discussion is your opportunity to synthesize the full-stack and AWS concepts from the entire course. Choose one scenario and write an initial post addressing all three sub-questions. These scenarios reflect the style and difficulty of DVA-C02 exam questions.

---

## Scenario A: Serverless API Architecture

A startup is migrating their monolithic Node.js Express API from a single EC2 instance to a serverless architecture. The current API has 12 endpoints across three resources: users, orders, and products. The team is evaluating two migration approaches:

- **Option A:** One Lambda function per endpoint (12 Lambda functions), each deployed individually with its own `handler.js` file
- **Option B:** One Lambda function per resource (3 Lambda functions), each using `express` and `serverless-http` to route internally

The API connects to RDS PostgreSQL. The team expects bursty traffic — quiet for most of the day with peaks during business hours.

Address all three of the following in your post:

1. Evaluate Option A vs Option B. Describe one concrete operational advantage of Option A (fine-grained deployment and permissions) and one concrete operational advantage of Option B (code reuse and Express middleware). Explain which approach AWS SAM templates favor and why.
2. Both options face the same Lambda-to-RDS connection problem. Describe what happens to RDS connections during a traffic burst (when Lambda concurrency jumps from 0 to 50 in seconds), why this causes "too many clients" errors, and which AWS service solves this without application code changes.
3. The team is debating between RDS PostgreSQL and DynamoDB for the migration. The orders table has complex join queries across users, products, and shipping data. Identify which database is more appropriate for this use case and explain the primary reason. Then describe the scenario in which DynamoDB would be the better choice.

Your initial post should be 175 to 225 words.

---

## Scenario B: Securing a Production API

A team's production API has the following security configuration after a rushed launch:

- Lambda functions have IAM execution roles with `Action: "*", Resource: "*"` (AdministratorAccess)
- The RDS database password is stored in a Lambda environment variable: `DB_PASSWORD=prod-password-here`
- API Gateway has no authorizer — all endpoints are publicly accessible
- The S3 bucket containing user-uploaded files has `BlockPublicAccess: false` and a bucket policy allowing `s3:GetObject` for `*` (the entire internet)

A security audit flags all four items as critical vulnerabilities.

Address all three of the following in your post:

1. Explain the specific risk of each configuration. For the IAM role, explain what an attacker who exploits an application vulnerability could do with AdministratorAccess. For the environment variable, explain how the password is exposed if the Lambda function has an unhandled error or if a team member with console access runs a test invocation.
2. Describe the correct replacement for each vulnerability. Use specific AWS service names: what replaces the overpermissioned IAM role, what replaces the environment variable for the database password, what replaces the missing API Gateway authorization, and what replaces the public S3 bucket access.
3. The team asks whether S3 presigned URLs are a secure alternative to the public bucket policy for serving user files. Explain how presigned URLs work, what the `Expires` parameter controls, and one scenario in which presigned URLs are preferable to a CloudFront distribution with an origin access identity.

Your initial post should be 175 to 225 words.

---

## Scenario C: Debugging and Observability

A production Lambda function processes SQS messages from an order processing queue. The function has been running for two weeks. The team observes:

- Approximately 3% of messages fail with an unhandled exception
- Failed messages disappear from the queue after the failure (they are not retried)
- CloudWatch shows the Lambda function has a maximum duration of 28 seconds (the timeout is 30 seconds)
- On peak days, some orders report never being processed — no CloudWatch log entry exists for those messages at all

Address all three of the following in your post:

1. Identify the configuration error that causes failed messages to disappear instead of being retried. Explain the SQS visibility timeout, what `maxReceiveCount` controls, and what a dead-letter queue (DLQ) does. Describe the correct configuration to retain failed messages for analysis.
2. The Lambda function approaching its 30-second timeout indicates a performance problem. Name two Lambda configuration changes (not code changes) that can address a function that consistently runs near its timeout limit. For each, explain the mechanism — why does changing that configuration improve duration?
3. For the messages that show no CloudWatch log entry, explain two possible root causes: one related to Lambda concurrency limits and one related to SQS visibility timeout and message in-flight limits. For each root cause, describe the CloudWatch metric or SQS attribute that would confirm it.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific AWS service name or behavior, or
- Add a DVA-C02 exam tip that connects the scenario to a likely exam question pattern, or
- Present an alternative architecture or configuration with trade-off analysis

---

## Due Dates

- Initial post: Wednesday by 11:59 PM
- Peer responses (at least two): Sunday by 11:59 PM

---

## Grading Rubric

| Criterion | Points |
|---|---|
| Initial post addresses all three sub-questions with technical accuracy | 3 |
| Initial post meets the 175 to 225 word count requirement | 1 |
| Initial post uses correct AWS service names and DVA-C02 terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

These three scenarios are not hypotheticals invented for a class assignment. They describe real production systems I have seen or consulted on. Lambda functions with AdministratorAccess roles exist in production today — developers create them during testing and never restrict them. RDS passwords in environment variables are common. Public S3 buckets containing private user files make news every few months.

The DVA-C02 exam tests your ability to reason about these scenarios correctly under time pressure. If you can explain why AdministratorAccess on a Lambda execution role is dangerous, name the correct replacement (a scoped IAM role with specific actions on specific resource ARNs), and connect that to the principle of least privilege — you are prepared for Domain 2.

For Scenario C: the "no log entry" problem is one of my favorite exam questions because it has two correct answers depending on which constraint you hit first. Lambda reserved concurrency limits and SQS in-flight message limits are both invisible until you hit them — and when you do, messages silently fail to reach your function. Knowing which CloudWatch metric to check (`ConcurrentExecutions` vs `ApproximateNumberOfMessagesNotVisible`) is the difference between a 30-minute diagnosis and a 3-hour incident.

This is your final post. Make it count — show what you have learned.

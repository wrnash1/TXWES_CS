# Discussion Forum: Module 14 — Cloud Deployment with AWS

**Course:** CIS-3340 Full Stack Web Development
**Texas Wesleyan University | Professor Nash**

---

## Overview

This week's discussion connects AWS deployment decisions to real engineering trade-offs: service selection, security configuration, environment management, and cost. Choose one scenario and write an initial post addressing all three sub-questions.

---

## Scenario A: SPA Routing on S3 and CloudFront

A team deploys a React SPA to S3 with CloudFront. The application has client-side routes including `/dashboard`, `/profile/:id`, and `/settings/notifications`. After deployment, the following problems are reported:

- Navigating to `/dashboard` from the root URL works correctly (React Router handles it)
- Refreshing the browser on `/dashboard` returns a 403 error
- A user who bookmarked `/profile/42` cannot access it directly

Address all three of the following in your post:

1. Explain why navigation from within the app works but direct URL access fails. Trace exactly what happens at the network level when a browser requests `/dashboard` from a CloudFront distribution whose S3 origin has no object at that path.
2. The team is using an S3 static website endpoint as the CloudFront origin. Describe two configuration changes — one at the S3 level and one at the CloudFront level — that each independently solve the routing problem. Explain the mechanism by which each fix works.
3. After applying the CloudFront custom error response fix, a developer observes in the browser Network tab that a request to `/dashboard` returns HTTP status `200` but the response body is `index.html`. Why does CloudFront return `200` instead of the original `404`, and is this the correct behavior for a React SPA deployment? Explain the reason for mapping the error to `200`.

Your initial post should be 175 to 225 words.

---

## Scenario B: Secrets Management and Elastic Beanstalk Configuration

A startup ships their Node.js API to Elastic Beanstalk. Their deployment process: the developer runs `zip -r app.zip .` (including `node_modules` and `.env`) and uploads the zip through the console. The `.env` file contains `JWT_SECRET`, `DB_PASSWORD`, and `STRIPE_SECRET_KEY`. A code reviewer catches the `.env` in the zip before it reaches production.

Address all three of the following in your post:

1. Identify three distinct security and operational risks of including `.env` in the deployment zip and committing it to the git repository. Consider who can access the zip artifact, what happens if the repository is made public, and what the risk is if a team member leaves the organization.
2. Describe the correct process for providing secrets to an Elastic Beanstalk application. Explain where secrets should be stored, how the Node.js application accesses them at runtime, and what the correct `zip` command looks like to exclude the `.env` file.
3. For a production application with high security requirements, Elastic Beanstalk environment properties store values in the EB configuration (not ideal for very sensitive secrets). Identify the two AWS services designed specifically for secrets storage and describe one advantage each has over storing secrets in EB environment properties.

Your initial post should be 175 to 225 words.

---

## Scenario C: RDS Architecture, VPC Security, and RDS Proxy

A team's Node.js API is deployed to Elastic Beanstalk and connects to RDS PostgreSQL. After three months of steady usage, the team adds a serverless component: a Lambda function that processes nightly batch imports. During the first batch run, the RDS instance begins logging "FATAL: sorry, too many clients already" and rejecting connections from both the Lambda function and the Elastic Beanstalk Express API.

Address all three of the following in your post:

1. Explain the root cause of the connection exhaustion problem. Describe the difference in how a persistent Node.js server (Express on EC2/EB) and AWS Lambda functions each manage database connections — and why Lambda's behavior is the specific cause of the problem even though it is a single batch job.
2. Identify the AWS service that solves this problem without application code changes. Describe precisely what it does between Lambda and RDS, how it is configured (at the infrastructure level, not application code), and what the application's connection string change looks like after adding this service.
3. The team's security engineer also reviews the RDS configuration and finds "Public access: Yes" with a security group allowing `0.0.0.0/0` on port 5432. Describe why this is a critical vulnerability, what the correct network configuration should be (VPC subnets, security group rules), and whether this change requires any Express application code modifications.

Your initial post should be 175 to 225 words.

---

## Peer Response Instructions

Write a substantive reply to at least two classmates who chose scenarios different from yours. Each peer response must be at least 75 words and must:

- Correct a technical inaccuracy with a specific explanation, or
- Add AWS-specific context or a deployment principle that strengthens the answer, or
- Present an alternative approach with trade-off analysis

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
| Initial post uses correct AWS service names and terminology | 1 |
| First peer response is substantive (75+ words, adds value) | 2 |
| Second peer response is substantive (75+ words, adds value) | 2 |
| Posts submitted by the stated deadlines | 1 |
| **Total** | **10** |

---

## Professor Nash Note

The RDS with public access and `0.0.0.0/0` security group in Scenario C is not a hypothetical. It is one of the most common cloud security incidents reported to AWS each year. Developers expose a database to the internet "just temporarily" while testing, forget to close it, and six months later there is a breach. The correct configuration takes less than five minutes and costs nothing. Private subnet, EB security group as the only inbound source, no public access. That is the rule. Memorize it.

# Discussion: Module 12 — Serverless Architecture on AWS

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Overview

This week's discussion asks you to apply serverless architectural reasoning to realistic business scenarios. Choose ONE of the three scenarios below. Write an initial post of 175–225 words, then respond substantively to at least TWO classmates who selected different scenarios.

---

## Scenario A — Cold Start SLA Conflict

A healthcare startup runs a patient-facing symptom checker built on Lambda and API Gateway. The product team committed to sub-500ms response times for all API calls. The engineering team discovers that Python cold starts with their ML inference library average 1.8 seconds. The infrastructure budget is $800/month and Provisioned Concurrency for the function at their scale would cost approximately $420/month additional. The team is debating two alternatives: (1) migrate the ML inference to a containerized ECS Fargate service behind an ALB, removing Lambda entirely, or (2) keep Lambda but restructure the code to reduce package size and defer non-critical imports, accepting that cold starts will still occasionally occur.

In your post, recommend one approach and justify it using at least two technical criteria. Address the following: What is the patient safety implication of a 1.8-second latency spike in a healthcare context? Does the $420/month cost difference justify the architectural simplicity of staying serverless? What architectural safeguard — beyond Provisioned Concurrency — could reduce cold start frequency without eliminating Lambda?

---

## Scenario B — SQS vs. SNS Fan-Out Design

A retail company processes 15,000 order events per minute during peak hours. When an order is placed, four downstream systems must each receive and process the event: warehouse management, fraud detection, loyalty points, and customer email. The engineering team is debating two designs. Design 1 uses a single SQS Standard queue that all four consumer services poll. Design 2 uses an SNS Standard topic with four SQS queue subscriptions, one per service.

In your post, evaluate both designs against these criteria: fault isolation (if fraud detection is down, does it affect warehouse processing?), independent scaling, message durability, and operational complexity. Identify the specific failure mode in Design 1 that makes it unsuitable for this use case. Then explain one scenario where Design 1 would actually be preferable to Design 2.

---

## Scenario C — Step Functions vs. Lambda Chaining

A fintech company processes loan applications through a five-step workflow: credit score check, income verification, regulatory compliance scan, underwriting decision, and notification dispatch. Currently, each step is a Lambda function that invokes the next function directly by passing the result as a payload. The team is evaluating migrating to AWS Step Functions Standard Workflow.

In your post, identify three specific operational problems that can arise from the current Lambda-chaining approach in a five-step financial workflow. Explain how Step Functions addresses each problem. Address the cost tradeoff: Step Functions charges per state transition ($0.000025 per transition). At 10,000 loan applications per day with 5 states each, calculate the daily Step Functions cost and argue whether it is justified.

---

## Peer Response Guidelines

When responding to classmates:

- Identify one point of agreement and explain why the technical reasoning is sound
- Offer one substantive challenge or alternative consideration they may not have addressed
- If they selected a different scenario, briefly note whether a concept from your scenario applies to theirs

Responses must be 75–100 words and must engage with the technical content, not just offer agreement.

---

## Grading Rubric (10 points)

| Criterion | Points |
|---|---|
| Initial post addresses the scenario's specific technical question | 3 |
| At least two technical criteria used to justify recommendation | 2 |
| Initial post is 175–225 words | 1 |
| First peer response is substantive (75–100 words, technical engagement) | 2 |
| Second peer response is substantive (75–100 words, technical engagement) | 2 |

### Total: 10 points

Posts are due by 11:59 PM Wednesday. Peer responses are due by 11:59 PM Sunday.

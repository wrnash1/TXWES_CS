# Discussion: Module 14 — AWS Cost Optimization

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Overview

This week's discussion asks you to apply cost optimization reasoning to realistic business scenarios. Choose ONE of the three scenarios below. Write an initial post of 175–225 words, then respond substantively to at least TWO classmates who selected different scenarios.

---

## Scenario A — Reserved Instances vs. Savings Plans

A mid-size SaaS company has been running on AWS for two years entirely on On-Demand EC2 instances. Their workload is stable — 40 m5.2xlarge instances running 24/7 in us-east-1 for their application tier, and 10 r5.xlarge instances running 24/7 for their caching layer. The CTO wants to reduce compute spending by at least 40% without changing the application architecture. The FinOps team is debating three options: (1) purchase 1-year Standard Reserved Instances for all 50 instances, (2) purchase a 3-year Compute Savings Plan, or (3) purchase a mix of EC2 Instance Savings Plans for the stable tier and keep the caching layer On-Demand.

In your post, analyze all three options against two criteria: maximum discount achievable and flexibility if the company decides to change instance types or regions within 18 months. Which option would you recommend and why? Address the operational overhead of managing 50 individual RIs versus a single Savings Plan commitment. If the company launches a new Lambda-based microservices layer in 6 months, which option positions them best?

---

## Scenario B — S3 Cost Optimization for a Data Lake

A media company stores 500 TB of video content in S3 Standard. Content is streamed heavily for the first 90 days after upload, then accessed for re-runs and licensing approximately twice per year for 5 years, then rarely accessed for archival compliance for 10 years total. Current monthly S3 storage cost is approximately $11,500. The engineering team wants to reduce this by at least 60% without changing the access latency for the active content.

In your post, design a complete S3 storage strategy including storage class selection for each phase and a Lifecycle policy timeline. Calculate the approximate monthly storage cost after your optimization (use public AWS pricing: S3 Standard $0.023/GB, Standard-IA $0.0125/GB, Glacier Flexible Retrieval $0.004/GB, Glacier Deep Archive $0.00099/GB). Explain the trade-off your architecture makes regarding retrieval time for archived content. Address whether Intelligent-Tiering would be more or less cost-effective than your Lifecycle policy for this specific workload.

---

## Scenario C — Rightsizing and Compute Optimizer

A financial services firm has 200 EC2 instances across their production environment. AWS Compute Optimizer has generated recommendations showing that 60 instances are over-provisioned by at least one instance size, representing an estimated $18,000/month in savings. The infrastructure team is hesitant to apply the recommendations because they are concerned about performance degradation during quarter-end processing, when transaction volumes spike 4x above normal.

In your post, propose a process for safely validating and applying rightsizing recommendations without risking production performance. Address: Why is Compute Optimizer's default 14-day analysis window potentially misleading for this workload? What data source would you use to analyze peak utilization during quarter-end specifically? How would you use Auto Scaling as an alternative to static rightsizing to handle the 4x spike? Finally, calculate the payback period if migrating to smaller instances costs $5,000 in engineering time and testing.

---

## Peer Response Guidelines

When responding to classmates:

- Identify one calculation or recommendation they made that is technically sound and explain why
- Challenge one assumption or suggest an alternative approach with a specific technical justification
- If they chose a different scenario, note whether a concept from your scenario applies to theirs

Responses must be 75–100 words and engage with the technical content.

---

## Grading Rubric (10 points)

| Criterion | Points |
|---|---|
| Initial post addresses the scenario's specific cost optimization question | 3 |
| At least one cost calculation or quantitative comparison included | 2 |
| Initial post is 175–225 words | 1 |
| First peer response is substantive (75–100 words, technical engagement) | 2 |
| Second peer response is substantive (75–100 words, technical engagement) | 2 |

### Total: 10 points

Posts are due by 11:59 PM Wednesday. Peer responses are due by 11:59 PM Sunday.

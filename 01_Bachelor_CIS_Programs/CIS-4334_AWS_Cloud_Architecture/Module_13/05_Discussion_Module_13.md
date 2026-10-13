# Discussion: Module 13 — AWS Monitoring, Logging, and Operations

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Overview

This week's discussion applies observability and operational excellence thinking to realistic production scenarios. Choose ONE of the three scenarios below. Write an initial post of 175–225 words, then respond substantively to at least TWO classmates who selected different scenarios.

---

## Scenario A — Observability Stack Design

A Series B startup is preparing to onboard enterprise customers who require documented SLAs: 99.9% API availability, p99 response time under 500 ms, and a mean time to detect (MTTD) of under 5 minutes for any availability degradation. The platform is built on API Gateway, Lambda, and DynamoDB. The engineering team currently has no monitoring in place — they rely on customer support tickets to learn about outages.

In your post, design a minimal but production-grade observability stack using native AWS services only. Address: Which CloudWatch metrics are most critical to monitor for each service layer? What alarm thresholds would you set to achieve a 5-minute MTTD? How would you use CloudWatch Synthetics alongside reactive alarms to detect issues before customers do? What is the role of X-Ray in this stack, and is it worth the added complexity for a startup?

---

## Scenario B — CloudTrail vs. Config for Compliance

A healthcare company operating under HIPAA must provide evidence to auditors that (1) no unauthorized user accessed or modified PHI-containing S3 buckets during a 90-day audit period, and (2) all EC2 instances had encrypted EBS volumes throughout the same period. The company currently uses only CloudTrail.

In your post, explain what CloudTrail alone can and cannot prove for each of the two audit requirements. Identify exactly which Config rules would provide continuous compliance evidence for the EBS encryption requirement. Explain why Config's configuration timeline is a fundamentally different type of evidence than CloudTrail's API call log. Then assess: is there any scenario where CloudTrail data alone would satisfy both requirements?

---

## Scenario C — Session Manager Migration

A large enterprise has 800 EC2 instances across three AWS accounts. All instances currently allow SSH on port 22 from a centralized bastion host subnet. The security team has mandated that within 90 days, all SSH access must be replaced with Session Manager, all port 22 security group rules must be removed, and all shell session activity must be logged to a central S3 bucket with 1-year retention.

In your post, outline a migration plan with at least three distinct implementation phases. Address: What must be true about every EC2 instance before you can safely remove port 22 rules? How do you handle instances in private subnets without internet access (what VPC endpoints are required)? How do you configure session logging to a central S3 bucket when the instances span three AWS accounts? What IAM changes are needed to control who can start a Session Manager session?

---

## Peer Response Guidelines

When responding to classmates:

- Identify one technical detail in their design that is correct and explain why it works
- Offer one gap or alternative they did not address — be specific about the service or configuration
- If they chose a different scenario, note whether a concept from your scenario applies to theirs

Responses must be 75–100 words and engage with the technical content.

---

## Grading Rubric (10 points)

| Criterion | Points |
|---|---|
| Initial post addresses the scenario's specific technical questions | 3 |
| At least two AWS services named and correctly applied | 2 |
| Initial post is 175–225 words | 1 |
| First peer response is substantive (75–100 words, technical engagement) | 2 |
| Second peer response is substantive (75–100 words, technical engagement) | 2 |

### Total: 10 points

Posts are due by 11:59 PM Wednesday. Peer responses are due by 11:59 PM Sunday.

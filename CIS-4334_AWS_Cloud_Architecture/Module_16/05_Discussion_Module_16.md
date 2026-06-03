# Discussion: Module 16 — SAA-C03 Capstone and Course Reflection

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Overview

This final discussion serves two purposes: architectural synthesis and course capstone reflection. You will apply everything you have learned across 16 modules to evaluate a complex real-world architectural scenario, and you will reflect on your most significant learning and how it applies to your professional goals.

Choose ONE of the three scenarios below for your initial post of 175–225 words. Then respond substantively to at least TWO classmates.

---

## Scenario A — Architectural Trade-Off Analysis

A financial technology company is designing a new payment processing platform. Their CTO has defined the following non-negotiable requirements: (1) all API transactions must complete in under 200 ms at p99; (2) the platform must survive the loss of an entire AWS region without data loss; (3) no payment transaction can be processed more than once; (4) all data must be encrypted with customer-managed KMS keys and key usage must be auditable; (5) monthly infrastructure cost must not exceed $50,000.

In your post, identify the single most difficult architectural tension in this set of requirements and explain why it is difficult. Select two of the five requirements and propose the specific AWS services and configurations that satisfy each one. Then address this question: Does the $50,000/month budget constraint change any of your service choices compared to if budget were unlimited? If yes, which service would you choose differently and why?

---

## Scenario B — Certification Strategy Reflection

You are advising a colleague who has just started an entry-level cloud support role. They have no AWS certifications and want to become a solutions architect within 3 years. They have completed an introductory cloud fundamentals course and are now deciding whether to pursue the AWS Certified Cloud Practitioner (CCP) first or go directly for the Solutions Architect Associate (SAA-C03).

In your post, recommend one certification path and justify it with at least three specific reasons based on what you now know about the SAA-C03 exam content after completing this course. Address: Which specific modules or topics in CIS-4334 most directly map to SAA-C03 exam content? What is the single most important hands-on skill someone should have before taking the SAA-C03 exam? What would you tell your colleague about the gap between passing a certification exam and being able to independently design production AWS architectures?

---

## Scenario C — Architecture Evolution

A startup built their entire application on a single t3.medium EC2 instance running Ubuntu with a MySQL database co-located on the same server. The application is a web-based project management tool. They have recently signed their first enterprise customer, who requires 99.9% uptime SLA, encryption of all customer data, and the ability to restore to any point in the last 30 days within 2 hours.

In your post, design the evolutionary path from their current single-server architecture to one that satisfies all three enterprise requirements. Address: What is the MINIMUM set of changes required (not a complete redesign) that achieves the uptime SLA? Which specific AWS service replaces the co-located MySQL and why? How is the 30-day PITR requirement satisfied, and what is the RPO of your solution? Identify one risk in your evolutionary migration approach that could cause unplanned downtime during the transition.

---

## Peer Response Guidelines

When responding to classmates:

- Identify one architectural decision they made that you agree with and provide a technical reason for your agreement
- Offer one alternative service or configuration they could consider — explain the specific trade-off
- Connect their scenario to your own: note one concept from your scenario that applies to theirs

Responses must be 75–100 words and engage with the technical content.

---

## Course Closing Note

You have completed all 16 modules of CIS-4334 AWS Cloud Architecture. The skills you have developed — designing resilient, performant, secure, and cost-optimized architectures — are directly applicable to professional AWS roles and are tested on the SAA-C03 certification exam.

The AWS Well-Architected Framework is not a one-time checklist. It is a lens for continuous improvement. Every architecture you design will have trade-offs. Your value as a solutions architect is in making those trade-offs consciously, with clear technical justification, and with an understanding of how to evolve the architecture as requirements change.

Good luck on the SAA-C03 exam. You are ready.

---

## Grading Rubric (10 points)

| Criterion | Points |
|---|---|
| Initial post engages substantively with the scenario's specific architectural or strategic question | 3 |
| At least two specific AWS services named and applied correctly | 2 |
| Initial post is 175–225 words | 1 |
| First peer response is substantive (75–100 words, technical engagement) | 2 |
| Second peer response is substantive (75–100 words, technical engagement) | 2 |

### Total: 10 points

Initial posts are due by 11:59 PM Wednesday. Peer responses are due by 11:59 PM Sunday.

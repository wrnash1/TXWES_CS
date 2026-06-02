# Discussion Forum: Module 01 - AWS Global Infrastructure and Core Services Overview

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Instructions

Read all three scenarios below and select one to address in your initial post. Your initial post must be 175-225 words, technically precise, and reference at least one specific AWS service or infrastructure concept from the module. Respond to at least two classmates who chose different scenarios from yours.

Initial post due: Wednesday at 11:59 PM
Peer responses due: Sunday at 11:59 PM

---

## Scenario A - Regional Expansion Decision

A US-based healthcare company is expanding its patient records platform to serve clients in Germany. The platform currently runs entirely in us-east-1 (N. Virginia). The CTO proposes simply keeping all data in us-east-1 and relying on CloudFront Edge Locations in Europe to reduce latency. Describe the flaw in this proposal from both a compliance and an architectural standpoint. What AWS infrastructure decisions would you recommend instead, and how does the Shared Responsibility Model affect the company's obligations under GDPR? Your response should identify the specific Region or Regions you would use and explain why.

---

## Scenario B - Availability Zone Failure Planning

A retail company runs a critical order-processing application on three EC2 instances, all deployed in us-west-2a. During an infrastructure review, an engineer proposes that because each EC2 instance has a separate EBS volume, the application is already highly available. Evaluate this claim. Explain what would happen to the application if us-west-2a experienced an outage, and describe the minimum architecture changes needed to achieve genuine high availability. Include in your response the specific AWS services that would enforce availability across fault domains and explain what role the Shared Responsibility Model plays in ensuring the application stays available during an AZ failure.

---

## Scenario C - Service Responsibility Confusion

A startup's developer deployed a MySQL database on an Amazon RDS instance and told the CTO: "We don't need to worry about database security — it's all managed by AWS." Identify at least three specific security or operational tasks that remain the customer's responsibility for an RDS instance, and explain why each task is classified as the customer's responsibility under the Shared Responsibility Model. Then explain how this responsibility profile differs from running MySQL on an EC2 instance. What additional tasks would the team own if they moved from RDS to a self-managed EC2 deployment?

---

## Discussion Rubric

| Criteria | Points | Description |
|---|---|---|
| Initial post — technical accuracy | 3 | Correctly applies AWS infrastructure concepts; no factual errors about services, responsibility model, or infrastructure components |
| Initial post — depth and completeness | 2 | Addresses all parts of the chosen scenario; meets 175-225 word count; uses specific AWS service names |
| Initial post — clarity | 1 | Well-organized, professional tone, correct terminology |
| Peer response 1 — substantive engagement | 2 | Adds new technical detail, a counter-argument, or a real-world extension; minimum 50 words |
| Peer response 2 — substantive engagement | 2 | Adds new technical detail, a counter-argument, or a real-world extension; minimum 50 words |
| **Total** | **10** | |

---

## Professor Nash Note

Responses that simply restate the scenario or list definitions without applying them to the specific situation will not earn full credit. Strong posts take a position, justify it with AWS infrastructure reasoning, and engage with the tradeoffs. If you are responding to a peer, challenge or extend their thinking — do not just agree and summarize what they said.

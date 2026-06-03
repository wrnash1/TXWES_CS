# Discussion: Module 15 — AWS Migration and Hybrid Architectures

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Overview

This week's discussion asks you to apply migration and hybrid architecture reasoning to realistic enterprise scenarios. Choose ONE of the three scenarios below. Write an initial post of 175–225 words, then respond substantively to at least TWO classmates who selected different scenarios.

---

## Scenario A — Choosing the Right Migration Strategy

A regional hospital system is planning to migrate its IT infrastructure to AWS over 24 months. The portfolio includes: (1) a modern electronic health records (EHR) system built on .NET and SQL Server that processes real-time patient data 24/7; (2) a legacy radiology imaging system running on Windows Server 2008 R2 that the vendor no longer supports; (3) a commercial HR management platform with a 3-year SaaS contract signed last year; (4) a custom Python analytics pipeline that runs nightly batch jobs; (5) a VMware-based internal wiki server used by 50 staff.

In your post, assign one of the 7 R migration strategies to each of the five systems and justify your choice for each with at least one technical or business reason. Identify which system presents the highest technical risk during migration and explain why. Address the compliance implication of HIPAA for the EHR system specifically: does the migration strategy change based on compliance requirements?

---

## Scenario B — Direct Connect vs. VPN Design

A logistics company processes 500 GB of shipment data per day between its on-premises warehouse management system and AWS. The data includes proprietary route optimization algorithms that the company considers highly confidential. The company's on-premises network team has no experience managing BGP or physical colocation infrastructure. They have a reliable 1 Gbps internet connection at headquarters. Their AWS architect is evaluating Direct Connect (10 Gbps dedicated, 12-week lead time, $3,000/month) versus Site-to-Site VPN ($0.05/hour + data transfer, setup in 1 hour).

In your post, recommend one connectivity option with a full technical and business justification. Address: Is 500 GB/day within the bandwidth of a Site-to-Site VPN? Does encryption matter differently for these two options? What does the 12-week Direct Connect lead time mean for the migration timeline? If you choose VPN, what is the specific risk you accept, and how could you mitigate it architecturally?

---

## Scenario C — Hybrid Architecture for a Factory Floor

An automotive manufacturer runs robotic welding equipment controlled by software that requires sub-10ms response time to a compute backend. The factory has poor internet connectivity but a reliable private fiber connection to a regional data center. The manufacturer wants to use AWS services (EC2, ECS, S3) for the compute backend but cannot move the control system to a cloud region because latency to the nearest region is 45ms.

In your post, propose an AWS architecture that satisfies the latency requirement while still using AWS managed services and the AWS console for management. Address: Which AWS product eliminates the latency problem? What network path does control traffic take to the compute backend? What happens to factory operations if the connection from the factory to the AWS infrastructure is interrupted? How does AWS Outposts differ architecturally from simply running your own servers in the data center, and what is the business value of that difference?

---

## Peer Response Guidelines

When responding to classmates:

- Identify one technical justification in their recommendation that is well-reasoned and explain why
- Raise one risk or constraint they did not address — be specific about the service or architectural detail
- If they chose a different scenario, connect a concept from your scenario to theirs

Responses must be 75–100 words and engage with the technical content.

---

## Grading Rubric (10 points)

| Criterion | Points |
|---|---|
| Initial post assigns or applies specific AWS services or strategies to the scenario | 3 |
| At least two technical or business trade-offs explicitly addressed | 2 |
| Initial post is 175–225 words | 1 |
| First peer response is substantive (75–100 words, technical engagement) | 2 |
| Second peer response is substantive (75–100 words, technical engagement) | 2 |

### Total: 10 points

Posts are due by 11:59 PM Wednesday. Peer responses are due by 11:59 PM Sunday.

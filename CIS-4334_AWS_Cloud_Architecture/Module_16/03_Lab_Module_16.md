# Lab: Module 16 — SAA-C03 Capstone Architecture Review

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Lab Overview

This capstone lab is a design and analysis exercise. Rather than clicking through the AWS console, you will design a complete multi-tier AWS architecture that meets a comprehensive set of requirements spanning all four SAA-C03 exam domains. You will document your design decisions, justify service choices, and identify potential failure points and their mitigations.

This lab simulates the kind of architectural reasoning you will apply on the SAA-C03 exam and in professional AWS work.

**Estimated Time:** 90 minutes

**AWS Services Referenced:** Multiple (see requirements)

**Cost:** $0 — this is a design exercise; no resources are deployed.

---

## Prerequisites

- Modules 1–15 completed
- Familiarity with all major AWS service categories covered in this course

---

## Scenario: HealthTrack — A Healthcare SaaS Platform

HealthTrack is a healthcare SaaS company building a new patient engagement platform on AWS. The platform must meet strict regulatory, performance, availability, and cost requirements. Your task is to design the complete AWS architecture.

---

## Platform Requirements

### Functional Requirements

- Web and mobile clients access the platform over HTTPS
- Patient profile data and medical records are stored persistently
- Appointment scheduling uses real-time notifications
- Nightly batch processing generates personalized health reports
- Administrative dashboard provides aggregate health metrics across patient population

### Non-Functional Requirements

**Availability and Resilience:**

- API availability SLA: 99.95%
- RPO: 1 hour for patient data
- RTO: 15 minutes for full platform recovery
- All compute and database layers must survive the loss of a single Availability Zone

**Security and Compliance:**

- Platform handles Protected Health Information (PHI) — HIPAA compliance required
- All data at rest must be encrypted with customer-managed KMS keys
- All data in transit must use TLS 1.2 or higher
- No EC2 instances accessible via SSH from the internet
- Access logging for all API calls and data access events

**Performance:**

- API response time p99 under 300 ms for 95% of traffic
- Patient profile reads should be served from cache when possible
- Mobile push notifications must be delivered within 5 seconds of trigger event

**Cost Optimization:**

- Application tier workload is predictable (9 AM–9 PM peak, minimal overnight)
- Batch reporting jobs run nightly for 4 hours and can be interrupted and restarted
- Cold patient records (not accessed in 12+ months) should use lowest-cost storage

---

## Part 1: Design the Network Architecture

In your design document, describe and justify:

1. VPC CIDR range and subnet layout. How many AZs? How many public vs. private subnets? What goes in public subnets vs. private subnets?

2. How do web clients access the platform? What load balancing and edge services sit in front of the application?

3. How do EC2 instances or containers access the internet for software updates without being publicly accessible? How do engineers access instances for administration without SSH?

4. Which VPC Endpoints are needed and for which services? Justify each endpoint in terms of security (no internet transit for PHI) and cost (eliminate NAT Gateway charges for specific traffic).

5. How is traffic between the application tier and the database tier controlled? Which security group rules exist?

---

## Part 2: Design the Compute and API Layer

In your design document, describe and justify:

1. How is the web/API application layer deployed? Choose between EC2 Auto Scaling, ECS Fargate, or Lambda + API Gateway. Justify your choice based on the predictable workload pattern and the operational overhead requirement.

2. Given the 9 AM–9 PM peak pattern, which Auto Scaling policy type is most appropriate? What scaling metric would you use?

3. How are the nightly batch reporting jobs run? Which EC2 purchasing model minimizes cost for a 4-hour interruptible nightly job?

4. How are real-time patient appointment notifications delivered? Which AWS messaging service is appropriate, and which notification delivery protocol reaches mobile devices?

---

## Part 3: Design the Data Layer

In your design document, describe and justify:

1. Which database service stores patient profiles and medical records? Justify the choice for HIPAA compliance (at-rest encryption with CMK), high availability (Multi-AZ), and backup (automated backups with PITR).

2. Which caching layer reduces read load on the primary database? Where in the request path does caching occur?

3. Cold patient records not accessed in 12+ months are currently stored in the same database. Propose an archival strategy using S3 storage classes. Which S3 storage class is appropriate for records accessed "rarely" (estimated 1–2 times per year)? Write a Lifecycle policy rule that moves records to that tier after 365 days.

4. Where are audit logs, application logs, and CloudTrail events stored? How long are they retained, and in which storage tier?

---

## Part 4: Design the Security Architecture

In your design document, describe and justify:

1. Which IAM entity (role, instance profile, or user) is used by the application tier to access the database and S3? Why is an IAM role preferred over hardcoded credentials?

2. Which services provide HIPAA-aligned threat detection and sensitive data discovery for PHI in S3? Name two specific services and what each one detects.

3. How is the platform protected against Layer 7 web application attacks (SQL injection, cross-site scripting)? Name the service and at least two rule types to enable.

4. Which service provides centralized aggregation of security findings from GuardDuty, Macie, and Inspector? How would the security team be notified of critical findings?

5. How is access to PHI in the database and S3 audited? Name two specific audit services/features and what each one records.

---

## Part 5: Design the Monitoring and Operations Architecture

In your design document, describe and justify:

1. Which CloudWatch metrics are most critical to alarm on for the API layer, database layer, and batch processing layer? Name at least two alarms per layer and specify approximate threshold values.

2. How does the team diagnose a slow API request that passes through API Gateway, Lambda (or EC2), and RDS? Which service and feature provides the end-to-end request trace?

3. How is the nightly batch job monitored? What happens if the batch job fails at 2 AM? Which AWS service detects the failure and which service delivers the alert?

4. Which service enforces that all EBS volumes and RDS instances are encrypted? What happens when a new non-compliant resource is detected?

---

## Part 6: Cost Optimization Summary

In your design document, complete this cost optimization table:

| Layer | Cost Risk | Mitigation Strategy |
|---|---|---|
| Application compute (EC2 or ECS) | Idle capacity overnight | |
| Batch compute | Full On-Demand pricing | |
| Database | Continuous provisioned capacity | |
| Cold patient records | Expensive storage class | |
| Data transfer | Cross-AZ and egress charges | |
| API access logging | CloudWatch Logs storage | |

Fill in the Mitigation Strategy column for each row using specific AWS purchasing models, storage classes, or configuration choices from this course.

---

## Submission Requirements

Submit a single PDF or Word document containing:

1. A network architecture diagram (hand-drawn, diagramming tool, or text-based ASCII — any format is acceptable as long as it is legible)
2. Written answers to all questions in Parts 1–6
3. A completed cost optimization table (Part 6)
4. A one-paragraph executive summary explaining your top three architectural decisions and why they are appropriate for a HIPAA-regulated healthcare SaaS platform

**Length:** There is no minimum or maximum length. Aim for thoroughness and clarity. A well-reasoned 8–12 page document is appropriate.

**Grading Note:** This lab is worth 50 points (separate from the module quiz). See the course rubric in the LMS for the full breakdown. Partial credit is awarded for well-reasoned justifications even when the specific service choice differs from the model answer.

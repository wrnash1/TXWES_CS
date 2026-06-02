# Reading Guide: Module 01 - AWS Global Infrastructure and Core Services Overview

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)

---

## Introduction

Module 01 establishes the physical and logical foundation of every architectural decision you will make in this course and on the SAA-C03 exam. AWS does not operate like a single data center — it operates as a globally distributed system of independent fault domains. Understanding how those fault domains are organized, how services are categorized, and where responsibility boundaries fall is prerequisite knowledge for every module that follows.

This reading guide expands on the video lecture with detailed tables, policy examples, exam traps, and a study checklist.

---

## Section 1: AWS Global Infrastructure Components

### 1.1 Regions

An AWS Region is a geographically distinct area that contains a collection of Availability Zones. Regions are designed to be fully independent from one another. Each Region has:

- Independent power infrastructure
- Independent network connectivity to the internet and to other Regions via the AWS global backbone
- Independent control planes for AWS services
- Its own pricing tier (prices vary by Region)

Region names follow a convention: geographic area + cardinal direction + number. Examples: `us-east-1` (N. Virginia), `us-west-2` (Oregon), `eu-west-1` (Ireland), `ap-southeast-1` (Singapore).

You select a Region when you create most AWS resources. Resources are scoped to a Region unless they are explicitly global services (IAM, Route 53, CloudFront, AWS Organizations).

### 1.2 Availability Zones

Each Region contains a minimum of two Availability Zones; most contain three or more. An AZ is one or more physically discrete data centers with:

- Redundant power (multiple utility feeds plus UPS and generators)
- Redundant networking (multiple ISPs and AWS backbone connections)
- Redundant cooling
- Physical separation from other AZs in the same Region (typically tens of miles apart)

AZs within a Region are connected by AWS private fiber links with latency under 2 milliseconds round-trip. This low latency supports synchronous replication — the mechanism behind RDS Multi-AZ, and the reason you can treat a multi-AZ deployment as a single logical application.

AZ identifiers use a letter suffix: `us-east-1a`, `us-east-1b`, `us-east-1c`. Note that the mapping between AZ name and physical AZ is randomized per AWS account. Your `us-east-1a` and a colleague's `us-east-1a` may map to different physical facilities. AWS uses AZ IDs (such as `use1-az1`) for consistent physical identification across accounts.

### 1.3 Edge Locations and Regional Edge Caches

Edge Locations are Points of Presence (PoPs) located in major cities globally. They are used by:

- **Amazon CloudFront** — to cache content close to end users, reducing latency for HTTP/S requests
- **Amazon Route 53** — to answer DNS queries from the nearest PoP

Regional Edge Caches sit between origin servers and Edge Locations. They hold larger amounts of content that is not popular enough to remain in individual Edge Locations. When a user requests content not at the local Edge Location, the request goes to the Regional Edge Cache before hitting the origin.

As of 2024, there are more than 400 Edge Locations in over 90 cities across more than 40 countries — far more locations than Regions.

### 1.4 Local Zones and Wavelength Zones

| Feature | Local Zones | Wavelength Zones |
|---|---|---|
| Purpose | Ultra-low latency to metro users | Mobile edge computing on 5G networks |
| Operator | AWS | AWS + Telecom carrier partner |
| Typical latency | Single-digit milliseconds | Sub-10 milliseconds to 5G devices |
| Primary use case | Video rendering, gaming, live media | AR/VR on mobile, autonomous vehicles, industrial IoT |
| Parent Region | Logically attached to nearest Region | Logically attached to home Region |
| Service subset | EC2, EBS, ECS, RDS (subset) | EC2, EBS (subset) |

### 1.5 AWS Outposts

AWS Outposts delivers AWS infrastructure, services, APIs, and tools to your on-premises data center or co-location facility. Outposts racks are physically shipped to your facility and managed remotely by AWS. They are used when data residency, latency, or local data processing requirements prevent running workloads in an AWS Region. From the exam perspective, Outposts is the answer when a scenario requires AWS-native APIs but the workload must physically remain on-premises.

---

## Section 2: AWS Core Service Categories

### 2.1 Service Domain Overview

| Domain | Representative Services | Primary Use Cases |
|---|---|---|
| Compute | EC2, Lambda, ECS, EKS, Elastic Beanstalk, Batch | Run application code, containers, batch jobs |
| Storage | S3, EBS, EFS, FSx, Storage Gateway, Glacier | Object, block, file, archive, hybrid storage |
| Database | RDS, Aurora, DynamoDB, ElastiCache, Redshift | Relational, NoSQL, in-memory, data warehouse |
| Networking | VPC, Route 53, CloudFront, ELB, Direct Connect, Transit Gateway | Private networking, DNS, CDN, load balancing, connectivity |
| Security | IAM, KMS, Secrets Manager, WAF, Shield, GuardDuty, Macie | Identity, encryption, threat detection, compliance |
| Management | CloudWatch, CloudTrail, Config, Systems Manager, Trusted Advisor | Monitoring, auditing, configuration, operations |
| Application Integration | SQS, SNS, EventBridge, Step Functions, API Gateway | Messaging, event routing, workflow orchestration |
| Developer Tools | CodeCommit, CodeBuild, CodeDeploy, CodePipeline | CI/CD, source control, automated deployment |
| Machine Learning | SageMaker, Rekognition, Comprehend, Translate | Model training, inference, AI APIs |
| Analytics | Athena, Glue, Kinesis, EMR, QuickSight | Data pipelines, querying, streaming, visualization |

### 2.2 Global vs. Regional vs. AZ-Scoped Services

Understanding which services are global, regional, or AZ-scoped is essential for exam scenario questions.

| Scope | Examples | Implication |
|---|---|---|
| Global | IAM, Route 53, CloudFront, AWS Organizations, WAF (global) | Resources exist once, not per Region |
| Regional | S3 buckets, VPCs, Lambda functions, RDS instances | Created in a specific Region; replicate manually if needed |
| AZ-scoped | EBS volumes, subnets, EC2 instances | Tied to a single AZ; use multi-AZ deployment for resilience |

A common exam trap: S3 buckets are regional resources but S3 data is automatically replicated across at least three AZs within that Region. You do not configure this — AWS handles it automatically as part of S3's durability guarantee.

---

## Section 3: AWS Shared Responsibility Model

### 3.1 The Core Division

| Responsibility Category | AWS Owns | Customer Owns |
|---|---|---|
| Physical security | Data center access, guards, cameras, biometrics | Nothing — no physical access |
| Hardware | Servers, network devices, storage arrays | Nothing — no hardware access |
| Hypervisor | Virtualization layer, host OS | Nothing |
| Guest OS | Nothing | Patching, hardening, configuration |
| Networking | Physical network, backbone, BGP routing | VPC configuration, security groups, NACLs, route tables |
| Identity | Nothing | IAM users, roles, policies, MFA enforcement |
| Data | Nothing | Encryption at rest, encryption in transit, data classification |
| Application | Nothing | Application code, dependencies, configuration |
| Managed service platform | Database engine patching (RDS), Lambda runtime, S3 infrastructure | IAM permissions, encryption settings, network access |

### 3.2 Responsibility Shifts by Service Type

| Service Type | Example | AWS Manages | Customer Manages |
|---|---|---|---|
| IaaS | EC2 | Physical host, hypervisor | Guest OS, patches, app, firewall rules |
| PaaS | Elastic Beanstalk, RDS | OS, platform, engine patches | App code, IAM, network access, encryption |
| SaaS / Serverless | Lambda, S3, DynamoDB | Everything below the API | Function code, IAM, data, triggers |

The key exam pattern: the more managed the service, the less OS-level responsibility the customer carries — but the customer always retains responsibility for IAM configuration, data encryption choices, and network access controls.

### 3.3 Compliance Under the Shared Model

Even though AWS manages physical security and achieves certifications like SOC 2, ISO 27001, FedRAMP, and PCI DSS for its infrastructure, those certifications do not automatically cover your workloads. You must configure your application, your IAM policies, your encryption, and your network controls to satisfy your own compliance obligations. AWS Artifact provides access to AWS compliance reports and agreements for use in your own audits.

---

## Section 4: Region Selection Decision Framework

When selecting an AWS Region, evaluate these four criteria in priority order:

1. **Compliance and data residency** — Regulatory, contractual, or legal requirements that mandate data remain within specific geographic boundaries. Examples: GDPR (EU data must stay in EU), FedRAMP (US government data must stay in US govCloud), healthcare regulations. This factor overrides all others.

2. **Latency to users** — Deploy in the Region geographically closest to the majority of your user base. Use CloudFront Edge Locations to further reduce latency for cacheable content. Test latency from your target user locations to candidate Regions using tools like the AWS latency test page.

3. **Service availability** — Not all AWS services are available in all Regions. Verify that every service in your target architecture is available in your chosen Region before committing. The AWS Regional Services List is the authoritative reference.

4. **Cost optimization** — Pricing varies by Region. US East 1 (N. Virginia) is typically the lowest-cost Region for most services. Cost should be considered but should not override compliance, latency, or service availability requirements.

---

## Section 5: AWS Certification Exam Tips for SAA-C03

**Exam Tip 1 — AZ vs. Region failure protection:**
Multi-AZ within a single Region protects against AZ failures (high availability). Multi-Region deployment protects against full Region failures (disaster recovery). The exam tests this distinction constantly. Know which deployment strategy addresses which failure domain.

**Exam Tip 2 — Shared Responsibility Model for managed services:**
For every service the exam mentions, ask: is the customer running something on a guest OS? If yes, the customer patches the OS. If the service is managed (RDS, Lambda, S3), AWS patches the underlying platform. But the customer always manages IAM, encryption choices, and network access.

**Exam Tip 3 — Local Zone vs. Wavelength Zone selection:**
Local Zone = metro area, ultra-low latency, NOT 5G. Wavelength Zone = 5G carrier network embedded compute. If the scenario says "5G" or "mobile carrier edge," choose Wavelength Zone.

**Exam Tip 4 — Global service vs. regional service:**
IAM, Route 53, and CloudFront are global. When a question asks about making IAM changes, there is no Region selection — it is global. When a question asks about deploying an EC2 instance, you always pick a Region and an AZ.

**Exam Tip 5 — AZ ID vs. AZ name:**
AZ names (us-east-1a) are account-specific mappings. AZ IDs (use1-az1) are consistent across accounts. This matters for resource sharing between AWS accounts — use AZ IDs, not AZ names.

**Exam Tip 6 — S3 durability is automatic:**
S3 Standard provides 11 nines of durability by automatically replicating objects across at least three AZs within the Region. You do not configure this — it is built in. Cross-region replication is a separate optional feature for compliance or latency use cases.

**Exam Tip 7 — Outposts for on-premises requirements:**
When a scenario includes "on-premises" AND "AWS-native APIs" or "low latency to local systems" AND "cannot use public cloud," the answer is AWS Outposts.

**Exam Tip 8 — SAA-C03 domain weights:**
Design Secure Architectures: 30%. Design Resilient Architectures: 26%. Design High-Performing Architectures: 24%. Design Cost-Optimized Architectures: 20%. Modules 01-05 lay the groundwork for all four domains.

---

## Section 6: Key CLI Commands for Module 01

[SHOW CONSOLE]

List all available AWS Regions:

```bash
aws ec2 describe-regions --output table
```

List Availability Zones in a specific Region:

```bash
aws ec2 describe-availability-zones --region us-east-1 --output table
```

List AZ IDs (consistent cross-account identifiers):

```bash
aws ec2 describe-availability-zones \
  --region us-east-1 \
  --query "AvailabilityZones[*].{Name:ZoneName,ID:ZoneId,State:State}" \
  --output table
```

Describe Local Zones in a Region:

```bash
aws ec2 describe-availability-zones \
  --region us-west-2 \
  --filters Name=zone-type,Values=local-zone \
  --output table
```

---

## Section 7: Architecture Diagram — Multi-AZ Three-Tier Web Application

[SHOW DIAGRAM]

A standard three-tier web application deployed across two AZs in us-east-1:

```text
Internet
    |
[Route 53] --> [CloudFront Edge Location]
                        |
              [Application Load Balancer]
             /                          \
   [AZ us-east-1a]              [AZ us-east-1b]
   Web Tier: EC2                Web Tier: EC2
   App Tier: EC2                App Tier: EC2
   DB Tier: RDS Primary         DB Tier: RDS Standby (sync replication)
```

Customer responsibility in this diagram: EC2 guest OS patching, security group rules on each tier, RDS credentials and encryption settings, IAM roles for EC2 instances, application code.

AWS responsibility: physical data centers for both AZs, fiber connection between AZs, the hypervisor running EC2, RDS engine patching, the load balancer hardware and software platform.

---

## Section 8: Study Checklist

- [ ] Define Region, Availability Zone, Edge Location, Local Zone, Wavelength Zone, and AWS Outposts in your own words without referencing notes
- [ ] Explain the difference between AZ name and AZ ID and why the distinction matters for cross-account resource sharing
- [ ] List the four factors for Region selection and explain why compliance takes priority
- [ ] Draw the AWS Shared Responsibility Model boundary for EC2, for RDS, and for Lambda from memory
- [ ] Identify five examples of AWS-managed responsibilities and five examples of customer-managed responsibilities
- [ ] Run the CLI commands in Section 6 and record the output in your lab notebook
- [ ] List three services that are global in scope and three services that are regional in scope
- [ ] Explain why multi-AZ deployment does not protect against a full Region outage
- [ ] Complete the Module 01 quiz with a score of at least 80 percent
- [ ] Post your initial response in the Module 01 discussion forum by the Wednesday deadline

---

## References

All certification study materials and exam registration: aws.amazon.com/certification

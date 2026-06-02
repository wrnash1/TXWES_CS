# Video Script: Module 01 - AWS Global Infrastructure and Core Services Overview

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Estimated Duration:** 20-24 minutes
**Instructor:** Professor Nash

---

## [00:00 - 01:30] Opening and Module Objectives

Welcome to CIS-4334, AWS Cloud Architecture. I am Professor Nash, and this is Module 01: AWS Global Infrastructure and Core Services Overview.

Before we get into the technical content, let me tell you why this module matters. The AWS Solutions Architect Associate exam — exam code SAA-C03 — tests your ability to design resilient, high-performing, secure, and cost-optimized architectures on AWS. Every single design decision you will make on that exam traces back to the foundational concepts we cover today. If you do not understand Regions, Availability Zones, and the Shared Responsibility Model cold, you will miss questions on every other topic in this course.

By the end of this module you will be able to:

- Describe the physical layout of AWS Global Infrastructure including Regions, Availability Zones, and Edge Locations
- Explain the purpose of Local Zones and Wavelength Zones and identify their specific use cases
- Categorize AWS services into their core service domains
- Apply the AWS Shared Responsibility Model to determine what the customer manages versus what AWS manages
- Select the correct infrastructure deployment strategy for a given availability requirement

Let us get started.

---

## [01:30 - 06:00] AWS Regions and Availability Zones

[SHOW DIAGRAM]

Look at this world map. The colored circles represent AWS Regions. As of 2024, AWS operates more than 30 geographic Regions worldwide, with more announced regularly. Each Region is a distinct geographic area — think US East Northern Virginia, US West Oregon, EU Ireland, Asia Pacific Tokyo.

Here is what makes a Region special: it is completely independent. Each Region has its own power grid, its own network connectivity, its own cooling infrastructure. If there is a major event in US East 1 — a power failure, a network issue, a natural disaster — it does not propagate to US West 2. They are isolated by design.

Now look inside a single Region. Each Region contains a minimum of two Availability Zones, and most Regions have three or more. In US East 1 Northern Virginia, there are six Availability Zones: us-east-1a through us-east-1f.

[SHOW DIAGRAM]

What is an Availability Zone? An AZ is one or more discrete data centers — sometimes a campus of buildings — with redundant power, redundant networking, and redundant cooling. The key word is redundant. If one power feed fails, a backup kicks in. If one network path fails, another takes over.

AZs within a Region are connected to each other by AWS's private high-speed fiber network. The latency between AZs within a Region is typically under 2 milliseconds. That is fast enough for synchronous database replication — which is exactly how Amazon RDS Multi-AZ works. The primary database in AZ-a synchronously replicates every write to the standby in AZ-b in near real time.

Here is the critical exam concept: AZs are physically separated from each other far enough that a single failure event — a tornado, a flooding event, a fire — cannot take out two AZs simultaneously. But they are close enough together that the network latency between them is low enough for synchronous replication.

When you deploy across multiple AZs, you achieve high availability. If AZ-a fails, your application keeps running in AZ-b and AZ-c without interruption.

[SHOW DIAGRAM]

Now let me be precise about something the exam tests constantly. Multi-AZ deployment within a single Region gives you high availability protection against AZ-level failures. It does NOT protect you against a full Region outage. For regional disaster recovery, you must deploy across multiple Regions. We will cover multi-region architectures in detail when we get to Route 53 and disaster recovery patterns.

---

## [06:00 - 10:00] Edge Locations, Local Zones, and Wavelength Zones

AWS Global Infrastructure extends beyond Regions and AZs. There are three additional infrastructure types you must know for the SAA-C03 exam.

**Edge Locations** are Points of Presence distributed globally — over 400 locations in 90-plus cities across 40-plus countries. Edge Locations are used by Amazon CloudFront for content delivery caching and by Amazon Route 53 for DNS query resolution. When a user in Austin, Texas requests content from your website hosted in US East 1, CloudFront serves that content from an Edge Location in Dallas or Austin — not from the origin server in Virginia. The user gets the content in tens of milliseconds instead of hundreds.

There are many more Edge Locations than Regions. Think of it this way: Regions are where you deploy your workloads. Edge Locations are where AWS puts cached copies of your content and DNS answers close to your users.

[SHOW DIAGRAM]

**Local Zones** are an extension of an AWS Region to a specific metropolitan area. They let you run latency-sensitive applications — like video rendering, gaming, live streaming — within single-digit millisecond latency of a major population center. For example, the AWS Local Zone in Los Angeles lets you place EC2 instances and EBS storage physically in the Los Angeles metro area while the workload is still logically attached to the US West 2 Oregon Region. Local Zones are great for hybrid scenarios where on-premises systems need ultra-low latency access to AWS compute.

**Wavelength Zones** embed AWS compute and storage services at the edge of 5G carrier networks. This eliminates the network hops between a mobile device and the application. The use case is mobile edge computing — imagine a self-driving vehicle application, an augmented reality app running on a 5G phone, or real-time IoT processing for industrial equipment. The application runs inside the carrier's 5G network at sub-10-millisecond latency.

[SHOW DIAGRAM]

The SAA-C03 exam will give you a scenario and ask you to choose between Regions, Local Zones, and Wavelength Zones. The pattern is: if the requirement mentions 5G mobile edge computing, the answer is Wavelength Zone. If the requirement mentions sub-millisecond latency for on-premises or metro users without 5G, the answer is Local Zone. If the requirement mentions global distribution or disaster recovery, the answer involves multiple Regions.

---

## [10:00 - 14:30] AWS Core Service Categories

AWS offers over 200 services. The SAA-C03 exam does not test all of them equally. It focuses heavily on core services grouped into these categories. Let me walk through each one.

[SHOW DIAGRAM]

**Compute services** are the workhorses of AWS. Amazon EC2 gives you virtual servers — pick your CPU, memory, and storage, install your OS and application. EC2 Auto Scaling automatically adjusts the number of instances based on demand. AWS Lambda is serverless compute — you provide a function, AWS runs it on demand without you provisioning servers. Amazon ECS and EKS run Docker containers. AWS Elastic Beanstalk is a platform-as-a-service that deploys and manages applications automatically.

**Storage services** cover every type of data storage need. Amazon S3 is object storage — designed for durability at 11 nines (99.999999999%), used for backup, static website hosting, data lakes, and more. Amazon EBS is block storage for EC2 instances — think of it as a hard drive attached to your virtual server. Amazon EFS is elastic file system storage — shared file storage accessible from multiple EC2 instances simultaneously. Amazon Glacier is low-cost archival storage.

**Database services** include Amazon RDS for managed relational databases (MySQL, PostgreSQL, Oracle, SQL Server, MariaDB), Amazon Aurora for AWS's own high-performance relational engine, Amazon DynamoDB for NoSQL key-value and document storage, and Amazon ElastiCache for in-memory caching with Redis or Memcached.

**Networking services** start with Amazon VPC — Virtual Private Cloud — your own isolated private network within AWS. Amazon Route 53 is the DNS service. Amazon CloudFront is the content delivery network. Elastic Load Balancing distributes traffic across multiple targets. AWS Direct Connect provides dedicated private network connectivity between your data center and AWS.

**Security services** include AWS IAM for identity and access management, AWS KMS for encryption key management, AWS WAF for web application firewall, AWS Shield for DDoS protection, and Amazon GuardDuty for threat detection.

**Management and monitoring services** include Amazon CloudWatch for metrics and alarms, AWS CloudTrail for API call logging and auditing, and AWS Config for configuration compliance tracking.

These categories map directly to the SAA-C03 exam domains. Knowing which service belongs to which category and when to use each service is the core skill the exam tests.

---

## [14:30 - 19:00] The AWS Shared Responsibility Model

[SHOW DIAGRAM]

The Shared Responsibility Model is one of the most important concepts for both the exam and for professional cloud practice. Misunderstanding who is responsible for what leads to security gaps in production systems. Let me make this crystal clear.

AWS is responsible for security **of** the cloud. That means AWS owns and secures:

- The physical data center facilities — buildings, fences, guards, cameras
- The physical hardware — servers, network switches, storage arrays
- The hypervisor layer that runs the virtual machines
- The global network infrastructure connecting Regions and AZs
- The managed service infrastructure — the hardware and software that runs S3, RDS, Lambda, and other managed services

You never touch any of that. You never see it. AWS handles it completely.

You are responsible for security **in** the cloud. That means you are responsible for:

- Everything you put inside the virtual machines — guest operating system patches, application code, runtime libraries
- Network controls — configuring security groups, Network ACLs, routing tables in your VPC
- Identity and access management — creating IAM users, groups, roles, and policies; enforcing MFA; managing permissions
- Data protection — choosing to encrypt data at rest, encrypting data in transit, managing encryption keys
- Application security — your application code, its dependencies, its configuration

[SHOW DIAGRAM]

Here is where it gets nuanced — and where the SAA-C03 exam loves to test you. The responsibility boundary shifts depending on the service model.

For EC2 — Infrastructure as a Service — you manage the most. You pick the OS, you patch it, you install the software, you configure the firewall rules. AWS manages the physical host beneath your instance.

For RDS — Managed Database Service — AWS manages more. AWS patches the database engine, manages the underlying OS, handles hardware failure, and performs automated backups. But you still manage: the database schema, the access credentials, IAM authentication, network access via security groups, and whether to enable encryption.

For Lambda — Serverless — AWS manages almost everything. AWS manages the execution environment, the OS, the runtime patching. You are responsible for the function code, the IAM execution role it runs under, and the input/output security of what triggers the function.

A critical exam pattern: for any managed service, always ask yourself — who owns the OS patching? If the customer deploys it on EC2, the customer patches it. If it is a managed service like RDS, Elastic Beanstalk, or EMR, AWS patches the underlying OS and platform. But the customer always owns IAM policies, data encryption decisions, and application-layer security.

---

## [19:00 - 22:00] Selecting the Right Region

Region selection is an architectural decision with implications for compliance, performance, cost, and service availability. The SAA-C03 exam will present scenarios requiring you to justify Region selection. Here are the four factors you must consider.

**Data residency and compliance** comes first. Many industries and countries have laws requiring that certain data must stay within specific geographic boundaries. Healthcare data in Europe may fall under GDPR, requiring data to stay in EU Regions. Financial data for a US federal agency may require storage in US Regions only. Compliance requirements always override other factors.

**Latency to end users** comes second. Deploy your workload in the Region geographically closest to your primary user base. An application serving customers in Southeast Asia should deploy in the Asia Pacific Singapore or Tokyo Regions, not in US East 1. Use CloudFront Edge Locations to further reduce latency for static content and cached assets.

**Service availability** comes third. Not all AWS services are available in all Regions. Before designing an architecture, verify that every service you plan to use is available in your target Region. The AWS Regional Services List documents service availability per Region.

**Cost** comes last. AWS pricing varies by Region. US East 1 Northern Virginia is historically the lowest-cost Region for most services because it was the first Region and has the most infrastructure density. Running the same workload in Asia Pacific Sydney may cost 15-20% more. Cost optimization is valid, but it should not override compliance or latency requirements.

---

## [22:00 - 24:00] Module Summary and Exam Preview

Let me summarize what you need to know cold for the SAA-C03 exam.

A Region is a geographic area with full independence from other Regions. An Availability Zone is a physically separate data center cluster within a Region. Multi-AZ deployments protect against AZ failures. Multi-Region deployments protect against full Regional failures. Edge Locations serve CloudFront CDN and Route 53 DNS traffic. Local Zones extend AWS to metro areas for single-digit millisecond latency. Wavelength Zones embed AWS compute inside 5G carrier networks.

The AWS Shared Responsibility Model: AWS owns security of the cloud — physical hardware, hypervisor, managed service infrastructure. You own security in the cloud — OS patching on EC2, IAM configuration, network controls, data encryption, application code.

Region selection factors: compliance first, latency second, service availability third, cost fourth.

In the lab this week, you will use the AWS CLI to explore Regions and Availability Zones hands-on. In the Reading Guide, you will find detailed exam tips, service comparison tables, and a study checklist.

For your certification study, the official SAA-C03 exam guide and practice resources are available at aws.amazon.com/certification. I will see you in the next module.

---

End of Module 01 Video Script

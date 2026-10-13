# Video Script: Module 16 — SAA-C03 Exam Preparation and Capstone

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Segment 1: About the SAA-C03 Exam

Welcome to Module 16 — the capstone of CIS-4334 and your direct preparation for the AWS Certified Solutions Architect — Associate exam.

The SAA-C03 exam has the following structure:

- 65 questions total (scored questions and unscored pilot questions)
- Time limit: 130 minutes
- Passing score: 720 out of 1000
- Question types: Single answer multiple choice and multiple response (select two or three)
- Delivery: Pearson VUE testing center or online proctored exam
- Cost: $150 USD (or $75 with AWS Certification vouchers available at some universities)

The exam is organized into four domains with the following weightings:

- Domain 1: Design Resilient Architectures — 26%
- Domain 2: Design High-Performing Architectures — 24%
- Domain 3: Design Secure Architectures — 30%
- Domain 4: Design Cost-Optimized Architectures — 20%

Security (Domain 3) is the largest domain. Pay close attention to IAM, encryption, network security, and data protection.

---

## Segment 2: Domain 1 — Design Resilient Architectures

Resilient architectures survive component failures without total system failure. Key concepts:

**Multi-AZ deployments.** Every core AWS service has a Multi-AZ option. RDS Multi-AZ provides synchronous replication and automatic failover in under 2 minutes. ALB distributes traffic across multiple AZs. EC2 Auto Scaling groups span multiple AZs. S3 replicates data across at least three AZs by default.

**Decoupling.** Tightly coupled systems fail together. SQS between tiers ensures that a backend failure does not cascade to the frontend. Lambda retries on async invocations. Step Functions orchestrates retries with exponential backoff.

**Backup and Recovery.** Know the difference between RTO (Recovery Time Objective — how long you can be down) and RPO (Recovery Point Objective — how much data you can lose). For low RTO/RPO, use Multi-AZ and Read Replicas with Point-in-Time Recovery. For extreme requirements, use multi-region active-active with Route 53 health checks and global failover.

**Disaster Recovery patterns on the exam:**

- Backup and Restore — cheapest, highest RTO/RPO
- Pilot Light — minimal resources always running; scale up on disaster
- Warm Standby — reduced-scale running copy; scale to full on disaster
- Multi-Site Active-Active — full capacity in two regions simultaneously; lowest RTO/RPO, highest cost

**Auto Scaling.** Know the three scaling policy types: simple (step), target tracking, and scheduled. Target tracking is the easiest and most common exam answer for "automatically scale to maintain a metric target."

---

## Segment 3: Domain 2 — Design High-Performing Architectures

Performance efficiency means using AWS resources efficiently and adapting to workload changes.

**Compute performance.** Choose instance types appropriate for workload: compute-optimized (c-family) for CPU-intensive work, memory-optimized (r-family) for in-memory databases, storage-optimized (i-family) for high IOPS, and accelerated computing (p/g-family) for GPU workloads.

**Database performance.** Read replicas offload read traffic from the primary. ElastiCache (Redis or Memcached) caches frequently accessed query results. DynamoDB DAX provides in-memory caching specifically for DynamoDB with microsecond read latency. Aurora Serverless v2 automatically scales database capacity.

**Network performance.** Placement groups reduce latency between instances: Cluster placement group = lowest inter-instance latency (same rack, same AZ); Partition placement group = distributed fault isolation for HDFS/Cassandra/Kafka; Spread placement group = maximum isolation across racks.

**Content delivery.** CloudFront caches at edge locations globally. Lambda@Edge and CloudFront Functions execute logic at the edge. S3 Transfer Acceleration speeds uploads from distant locations.

**Caching layers.** Understand which cache is appropriate: CloudFront for static/dynamic HTTP content, ElastiCache Redis for session data and complex data structures, ElastiCache Memcached for simple key-value caching with multi-threading, DynamoDB DAX for DynamoDB queries specifically, API Gateway response cache for REST API responses.

---

## Segment 4: Domain 3 — Design Secure Architectures

Security is the highest-weighted domain. The exam tests defense in depth across multiple layers.

**Identity and Access Management.** IAM policies: Allow/Deny, Resource, Condition. Know the policy evaluation order: explicit Deny always wins. Use IAM Roles for EC2 and Lambda — never hardcode credentials. Use IAM Permission Boundaries to set maximum permissions. Use AWS Organizations SCPs to restrict entire accounts.

**Data protection at rest.** S3 SSE: SSE-S3 (AWS managed keys), SSE-KMS (customer-controlled KMS keys with audit trail), SSE-C (customer-provided keys). EBS volumes: KMS encryption at volume creation. RDS: KMS encryption at instance creation. You cannot enable encryption on an existing unencrypted volume — create encrypted snapshot, copy with encryption, restore.

**Data protection in transit.** TLS 1.2+ for all API communications. ACM manages TLS certificates for ALB and CloudFront. Enforce HTTPS on S3 using bucket policies (`"aws:SecureTransport": "false"` deny). VPN encrypts on-premises connections.

**Network security.** Security groups are stateful (return traffic allowed automatically). NACLs are stateless (must explicitly allow return traffic). Security groups operate at the instance level; NACLs at the subnet level. Place sensitive resources in private subnets. Use VPC endpoints (Gateway for S3/DynamoDB, Interface for other services) to prevent traffic from traversing the internet.

**Monitoring and threat detection.** GuardDuty detects threats using ML on CloudTrail, VPC Flow Logs, and DNS logs. Macie discovers and protects sensitive data (PII, PHI) in S3. Security Hub aggregates findings from GuardDuty, Macie, Inspector, Config, and partner tools.

**Incident response.** WAF protects against web exploits (SQL injection, XSS, Layer 7 DDoS). Shield Standard is free and automatic. Shield Advanced provides DDoS response team access and cost protection.

---

## Segment 5: Domain 4 — Design Cost-Optimized Architectures

Cost optimization questions on SAA-C03 test your ability to select the right pricing model and resource type.

**Compute cost.** Use Reserved Instances or Savings Plans for predictable workloads. Use Spot for interruptible batch workloads. Use Lambda for event-driven workloads that benefit from zero-cost idle time. Use Fargate for containerized workloads without EC2 management overhead.

**Storage cost.** Match S3 storage class to access frequency. Use S3 Lifecycle policies to transition and expire objects. Use EBS gp3 instead of gp2 (same performance baseline, lower cost). Delete unattached EBS volumes and unused snapshots.

**Database cost.** Use Aurora Serverless for variable/unpredictable database workloads — scales to zero when idle. Use DynamoDB On-Demand mode for unpredictable access patterns.

**Network cost.** Use VPC Gateway Endpoints for S3 and DynamoDB to eliminate NAT Gateway charges. Use CloudFront to reduce origin egress. Transfer data within the same AZ when possible.

**Architecting for cost.** Serverless eliminates idle-capacity costs. Managed services reduce operational overhead cost. Auto Scaling eliminates over-provisioning. Cost Anomaly Detection catches unexpected spending early.

---

## Segment 6: Key Service Decision Tables

These tables summarize the most common "choose the right service" exam patterns.

**Database selection:**

| Requirement | Service |
|---|---|
| Relational, fully managed, MySQL/PostgreSQL compatible | Amazon Aurora |
| Relational, standard MySQL/PostgreSQL/SQL Server/Oracle | RDS |
| Key-value / document, single-digit ms latency | DynamoDB |
| In-memory cache for DynamoDB | DynamoDB DAX |
| In-memory cache for RDS / application cache | ElastiCache |
| Data warehousing / analytics | Redshift |
| Graph database | Neptune |
| Time-series | Timestream |
| Ledger / append-only | QLDB |

**Messaging and integration:**

| Requirement | Service |
|---|---|
| Point-to-point queue, durable buffering | SQS |
| FIFO order + exactly-once | SQS FIFO |
| Fan-out to multiple consumers | SNS |
| Event routing with complex filtering | EventBridge |
| Real-time streaming, ordered per shard | Kinesis Data Streams |
| Real-time delivery to S3/Redshift/OpenSearch | Kinesis Firehose |
| Workflow orchestration | Step Functions |

**Storage:**

| Requirement | Service |
|---|---|
| Scalable object storage | S3 |
| Block storage for EC2 | EBS |
| Shared file system for Linux (NFS) | EFS |
| Shared file system for Windows (SMB) | FSx for Windows File Server |
| High-performance HPC file system | FSx for Lustre |

---

## Segment 7: Exam Strategy

**Time management.** 130 minutes for 65 questions = 2 minutes per question. Use this rule: if you are confident, answer and move on. If uncertain, mark for review and continue. Never leave a question blank — there is no penalty for wrong answers.

**Eliminate distractors.** Most exam questions have two clearly wrong answers you can eliminate immediately. The real question is choosing between the two plausible remaining options. Ask yourself: which one is simpler, more managed, and more directly addresses the stated requirement?

**Read the requirement carefully.** SAA-C03 questions always embed key constraints: "minimum operational overhead," "most cost-effective," "highly available," "least privilege," "no changes to existing code." These constraints determine the correct answer.

**Common traps:**

- "Most cost-effective" + always-on workload → RI or Savings Plan, not On-Demand
- "No downtime" database migration → DMS with CDC, not full-load
- "No SSH / no port 22" → Session Manager, not bastion host
- "Static website" → S3 static website hosting + CloudFront, not EC2 web server
- "Multi-region active-active" → Route 53 latency-based or weighted routing + failover, not just Multi-AZ
- "Data residency, ultra-low latency on-premises" → AWS Outposts
- "Unknown access pattern" S3 → Intelligent-Tiering
- "Exactly-once processing, strict order" → SQS FIFO
- "Fan-out to multiple services" → SNS + SQS, not just SNS alone

**On exam day:** Get good sleep. Read every word of the question. Trust your first instinct when uncertain. Use the scratch paper (or whiteboard) provided. Flag and return to difficult questions.

---

## Closing: Capstone Reflection

You have now covered all four SAA-C03 exam domains across 16 modules:

- Modules 1–3: Foundations, IAM, and compute
- Modules 4–6: Networking and storage
- Modules 7–9: Databases, high availability, and DNS
- Modules 10–11: Containers and deployment automation
- Module 12: Serverless architecture
- Module 13: Monitoring and operations
- Module 14: Cost optimization
- Module 15: Migration and hybrid
- Module 16: Exam preparation

The skills you have built in this course are directly applicable to real-world AWS architectural work. Whether you are building your first cloud application or designing enterprise-scale infrastructure, the patterns and principles you have learned here are the foundation.

Complete the practice quiz, participate in the capstone discussion, and schedule your SAA-C03 exam. You are ready. Good luck.

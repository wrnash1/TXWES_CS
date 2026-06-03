# Reading Guide: Module 16 — SAA-C03 Exam Preparation and Capstone

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Identify the four SAA-C03 exam domains and their percentage weightings
2. Apply the correct AWS service or architectural pattern to scenario questions in all four domains
3. Distinguish between similar services using key differentiating criteria
4. Use elimination strategies to narrow multiple-choice options on exam questions
5. Identify common distractor patterns used in SAA-C03 exam questions
6. Create a personal study plan targeting individual knowledge gaps

---

## Section 1: Exam Structure and Scoring

### 1.1 Exam Facts

| Attribute | Value |
|---|---|
| Number of questions | 65 (scored + unscored pilot) |
| Time limit | 130 minutes |
| Passing score | 720 / 1000 |
| Question format | Single-answer and multi-select multiple choice |
| Exam delivery | Pearson VUE (test center or online proctored) |
| Exam fee | $150 USD |

### 1.2 Domain Weightings

| Domain | Topic | Weight |
|---|---|---|
| 1 | Design Resilient Architectures | 26% |
| 2 | Design High-Performing Architectures | 24% |
| 3 | Design Secure Architectures | 30% |
| 4 | Design Cost-Optimized Architectures | 20% |

Domain 3 (Security) is the highest-weighted domain at 30%. Allocate proportionally more study time to IAM, encryption, network security, and data protection.

### 1.3 Scoring Model

AWS uses scaled scoring from 100–1000. Passing score is 720. The scaling means the difficulty of your specific question set affects the score. Always answer every question — there is no penalty for wrong answers. Unanswered questions count as wrong.

---

## Section 2: Domain 1 Deep Review — Resilient Architectures

### 2.1 High Availability vs. Fault Tolerance

- **High Availability (HA)** — the system remains operational despite component failures; brief interruptions are acceptable during failover. Example: RDS Multi-AZ (automatic failover in under 2 minutes).
- **Fault Tolerance** — the system continues operating without any degradation even during failures. Higher standard. Example: S3 (11 nines durability, internal redundancy transparent to users).

### 2.2 Disaster Recovery Patterns

| DR Pattern | RTO | RPO | Key Services | Cost Tier |
|---|---|---|---|---|
| Backup and Restore | Hours | Hours | S3, AWS Backup, Snapshots | Lowest |
| Pilot Light | 10–30 min | Minutes | RDS, minimal EC2, Route 53 failover | Low |
| Warm Standby | Minutes | Seconds | Reduced-scale running environment | Medium |
| Multi-Site Active-Active | Seconds | Near-zero | Route 53 latency routing, global databases | Highest |

### 2.3 Auto Scaling Policy Comparison

| Policy | Mechanism | Best For |
|---|---|---|
| Target Tracking | Maintains a metric (e.g., CPU at 60%) automatically | Most general workloads |
| Step Scaling | Scales by defined amounts at defined thresholds | Aggressive, tiered scaling |
| Scheduled Scaling | Scale at specific times | Predictable patterns (business hours) |
| Predictive Scaling | ML-based forecast; pre-scales before demand | Cyclical daily/weekly patterns |

### 2.4 Decoupling Patterns

Decoupling prevents failure propagation across tiers. Key exam patterns:

- Synchronous call → failed backend brings down frontend: add SQS between tiers
- Lambda retry for async events: configure DLQ or Destination on failure
- Step Functions with `Retry` and `Catch` blocks: declarative retry/compensating logic
- ALB with health checks: routes traffic only to healthy instances

---

## Section 3: Domain 2 Deep Review — High-Performing Architectures

### 3.1 Database Performance Toolbox

| Problem | Solution |
|---|---|
| Too many reads on RDS | Add Read Replicas |
| Expensive repeated RDS queries | Add ElastiCache (Redis or Memcached) in front |
| DynamoDB read latency | Enable DAX cluster |
| Variable database load | Use Aurora Serverless v2 |
| Analytics on operational data | Replicate to Redshift via DMS or Kinesis Firehose |
| Session storage at scale | ElastiCache Redis |

### 3.2 Network Performance Patterns

- **Cluster Placement Group** — instances in the same rack in the same AZ. Lowest inter-instance network latency (10 Gbps+). Use for HPC and tightly coupled distributed computing.
- **Partition Placement Group** — instances spread across partitions (racks) in one or more AZs. Used for HDFS, Cassandra, Kafka — isolates rack-level failures.
- **Spread Placement Group** — each instance on a separate rack. Maximum fault isolation for critical instances. Limit of 7 instances per AZ.

### 3.3 CloudFront Performance Optimization

- **Origin failover** — configure a primary and secondary origin; CloudFront automatically fails over on 5xx errors
- **Lambda@Edge** — runs Node.js/Python at CloudFront edge locations; used for A/B testing, auth token validation, URL rewriting
- **CloudFront Functions** — lightweight JavaScript executed at the edge for header manipulation and URL redirects; faster and cheaper than Lambda@Edge for simple logic
- **OAC (Origin Access Control)** — restricts S3 bucket access to CloudFront only; prevents direct S3 URL access

---

## Section 4: Domain 3 Deep Review — Secure Architectures

### 4.1 IAM Reference

| IAM Feature | Purpose |
|---|---|
| IAM Role | Grant permissions to services (EC2, Lambda, ECS tasks) |
| IAM Instance Profile | Container for an IAM Role attached to an EC2 instance |
| Permission Boundary | Maximum permissions cap for a user or role |
| Service Control Policy (SCP) | Maximum permissions cap for an AWS account in Organizations |
| Resource-based Policy | Grants access from a specific principal to a specific resource |
| Identity-based Policy | Grants permissions to a specific principal |

### 4.2 Encryption Quick Reference

| Resource | How to Encrypt |
|---|---|
| S3 objects | SSE-S3, SSE-KMS, SSE-C, or Client-side |
| EBS volumes | Enable encryption at volume creation time (KMS) |
| RDS databases | Enable encryption at DB instance creation time (KMS) |
| Aurora | Enable encryption at cluster creation (KMS) |
| EFS | Enable encryption at file system creation (KMS) |
| DynamoDB | Enabled by default (AWS-owned key); optionally use CMK |
| SQS | Server-side encryption with KMS; enable on queue creation |
| SNS | Server-side encryption with KMS; enable on topic creation |
| Lambda environment variables | Encrypt with KMS key |
| Secrets Manager | Always encrypted with KMS |

Cannot encrypt an existing unencrypted RDS instance or EBS volume directly — must create encrypted copy via snapshot.

### 4.3 VPC Security Layering

Defense in depth for VPC security:

1. **Internet Gateway / NAT Gateway** — control what can reach the internet
2. **Security Groups** — stateful, instance-level allow rules
3. **Network ACLs** — stateless, subnet-level allow/deny rules
4. **VPC Flow Logs** — record all traffic metadata for analysis
5. **AWS Network Firewall** — deep packet inspection, IPS/IDS capabilities at VPC perimeter
6. **GuardDuty** — ML threat detection using Flow Logs + CloudTrail + DNS

### 4.4 Data Residency and Sovereignty

For data residency requirements:

- Use AWS Config rules to detect and alert on resources created in disallowed regions
- Use SCPs to deny resource creation in all regions except approved regions
- Use S3 Object Lock for regulatory compliance (WORM storage — Write Once Read Many)
- Use AWS Artifact to access AWS compliance reports for your audit team

---

## Section 5: Domain 4 Deep Review — Cost-Optimized Architectures

### 5.1 Idle Capacity Elimination

| Pattern | How It Eliminates Idle Cost |
|---|---|
| Lambda (serverless) | No cost when no invocations; pay per execution |
| Fargate | No EC2 instances to pay for when no tasks run |
| Aurora Serverless v2 | Database scales to minimum ACUs when idle |
| DynamoDB On-Demand | No provisioned capacity cost; pay per request |
| Auto Scaling to zero | Scale EC2 ASG to 0 instances during off-hours |
| S3 vs. EBS for infrequent data | S3 storage is cheaper than EBS for inactive data |

### 5.2 Cost Monitoring and Governance

| Service | Purpose |
|---|---|
| Cost Explorer | Visualize and analyze historical and forecast spend |
| AWS Budgets | Set spend/usage limits with alerts and automated actions |
| Cost Anomaly Detection | ML-based unusual spend detection |
| Cost and Usage Report | Most granular billing data; delivered to S3 |
| Compute Optimizer | ML-based rightsizing recommendations |
| Trusted Advisor | Best practice recommendations including cost checks |

### 5.3 Network Cost Reduction

- S3 Gateway Endpoint: eliminates NAT Gateway charges for S3 traffic from private subnets
- Interface VPC Endpoints: keep traffic private; per-endpoint hourly charge but no data transfer charge to internet
- CloudFront: origin egress at CloudFront prices (lower than direct EC2 egress); caching reduces total origin fetches
- Same-AZ placement: intra-AZ data transfer is free; cross-AZ is charged ($0.01/GB each direction)

---

## Section 6: Common Exam Distractor Patterns

### 6.1 Multi-AZ vs. Read Replica

Exam trap: "Add Read Replicas to improve availability." Read Replicas improve read scalability — they are NOT automatic failover targets. Multi-AZ is required for HA and automatic failover. However, RDS can promote a Read Replica to a standalone DB manually (not automatic).

### 6.2 CloudFront vs. Global Accelerator

- **CloudFront** — CDN optimized for HTTP/HTTPS content caching. Reduces latency via edge cache hits.
- **Global Accelerator** — Layer 4 (TCP/UDP) traffic routing using AWS global network. Does not cache content. Reduces latency for dynamic content, gaming, IoT, VoIP.

Exam: "Static website" → CloudFront. "UDP gaming application with global users" → Global Accelerator.

### 6.3 S3 Transfer Acceleration vs. CloudFront

- **S3 Transfer Acceleration** — speeds up S3 uploads from distant clients using CloudFront edge locations as upload proxies. For upload, not download caching.
- **CloudFront** — speeds up download/read access to S3 content through caching.

### 6.4 DynamoDB Global Tables vs. RDS Cross-Region Read Replicas

- **DynamoDB Global Tables** — active-active, multi-region. Writes can occur in any region. Sub-second replication.
- **RDS Cross-Region Read Replicas** — active-passive. Reads from replica, writes to primary only. Can be promoted on DR.

Exam: "Multi-region active-active with single-digit millisecond writes" → DynamoDB Global Tables.

---

## Key Terms (Capstone Reference)

- **RTO** — maximum acceptable downtime after a failure
- **RPO** — maximum acceptable data loss in time
- **Target Tracking** — Auto Scaling policy that maintains a specific metric value automatically
- **Placement Group** — logical EC2 grouping for latency optimization or fault isolation
- **Permission Boundary** — maximum permissions ceiling for an IAM entity
- **SCP** — Service Control Policy; restricts maximum permissions for an AWS Organizations account
- **CloudFront OAC** — Origin Access Control; restricts S3 bucket access to CloudFront only
- **Lambda@Edge** — Lambda functions executed at CloudFront edge locations
- **DAX** — DynamoDB Accelerator; in-memory cache providing microsecond DynamoDB read latency
- **S3 Transfer Acceleration** — speeds S3 uploads from distant clients via CloudFront edge infrastructure
- **Global Accelerator** — routes TCP/UDP traffic through AWS global network for consistent low latency
- **S3 Object Lock** — WORM (Write Once Read Many) protection for regulatory compliance

---

## Final Exam Study Checklist

Work through this list in the week before your exam:

- Review all 16 module video scripts for key service definitions
- Complete at least two full-length practice exams (65 questions, 130 minutes each)
- Score each practice exam and categorize missed questions by domain
- Re-read AWS documentation FAQs for the 5 services where you missed the most questions
- Build and review flashcards for all service comparison tables in this guide
- Confirm your exam appointment, testing center location, and ID requirements
- Get 8 hours of sleep the night before the exam

# Quiz: Module 16 - Final Exam Prep & AWS Solutions Architect Associate
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
A company needs to design a three-tier web application that can withstand the failure of any single Availability Zone without user-visible downtime. The application tier must scale automatically during traffic spikes. Which architecture correctly implements these requirements?
*   A) Deploy all tiers in a single AZ with an Application Load Balancer; enable detailed monitoring to detect failures quickly.
*   B) Deploy an ALB in two public subnets (one per AZ), EC2 instances in an Auto Scaling Group across two private subnets (one per AZ), and an RDS Multi-AZ instance in two isolated subnets (one per AZ).
*   C) Deploy EC2 instances in a single AZ with a reserved instance commitment and daily RDS snapshots for recovery.
*   D) Deploy a CloudFront distribution in front of a single EC2 instance; CloudFront's edge redundancy compensates for single-AZ backend failures.
*   **Correct Answer:** B) Multi-AZ ALB, multi-AZ ASG, and RDS Multi-AZ together eliminate every single-AZ single point of failure across the web, application, and data tiers.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single-AZ deployment with an ALB is still a single fault domain — if that AZ fails, the entire application goes down regardless of monitoring. Detailed monitoring detects failures but does nothing to prevent them.
    *   *Why B is correct:* This is the canonical three-tier HA architecture for SAA-C03. The ALB distributes traffic across both AZs; ASG maintains the desired instance count and replaces failed instances; RDS Multi-AZ provides synchronous standby and automatic failover. Every tier is fault-isolated across two AZs.
    *   *Why C is incorrect:* A single-AZ deployment with Reserved Instances is a cost optimization, not an HA design. Reserved Instances guarantee capacity billing commitment, not AZ redundancy. Daily snapshots provide backup but require hours to restore — not "without user-visible downtime."
    *   *Why D is incorrect:* CloudFront caches and delivers content from edge locations but it is NOT a substitute for backend high availability. If the single EC2 origin instance fails, CloudFront can serve cached responses briefly but ultimately returns errors for non-cached or dynamic requests. CloudFront does not run your application — it proxies to it.

---

**Question 2**
Which of the following most accurately describes the SAA-C03 exam's four domain weightings?
*   A) Compute Services (35%), Storage Services (25%), Database Services (25%), Networking (15%)
*   B) Design Secure Architectures (30%), Design Resilient Architectures (26%), Design High-Performing Architectures (24%), Design Cost-Optimized Architectures (20%)
*   C) IAM and Security (40%), Networking and VPC (30%), Compute and Serverless (20%), Databases and Storage (10%)
*   D) Design Secure Architectures (25%), Design Resilient Architectures (25%), Design High-Performing Architectures (25%), Design Cost-Optimized Architectures (25%)
*   **Correct Answer:** B) The official SAA-C03 exam guide specifies: Secure (30%), Resilient (26%), High-Performing (24%), Cost-Optimized (20%).
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The SAA-C03 exam is organized by architectural dimensions (security, resilience, performance, cost), not by AWS service categories. AWS does not publish an exam guide organized by compute/storage/database/networking percentages.
    *   *Why B is correct:* These are the exact domain weightings published in the official AWS SAA-C03 Exam Guide. Security being the highest-weighted domain (30%) reflects AWS's emphasis on security-first architecture thinking. Knowing these weightings helps candidates allocate study time proportionally.
    *   *Why C is incorrect:* These percentages and category names do not match the official SAA-C03 exam guide. The actual domains are architectural quality dimensions, not AWS service families.
    *   *Why D is incorrect:* An equal 25% split across four domains is not the actual SAA-C03 distribution. Security is disproportionately weighted at 30% because it appears as a requirement in almost every architectural scenario, even those primarily about resilience, performance, or cost.

---

**Question 3**
A media company currently hosts a static website on on-premises servers. They want to migrate to AWS with the following requirements: global low-latency delivery to users worldwide, secure access to the S3 origin (no direct public S3 URL access), ability to filter malicious HTTP requests, and DDoS protection. Which combination of AWS services satisfies all four requirements?
*   A) S3 static website hosting with public read access, Route 53 latency-based routing, and AWS Shield Standard.
*   B) S3 bucket (private) with Origin Access Control, CloudFront distribution with WAF Web ACL and AWS Shield Standard (included automatically), and Route 53 for DNS.
*   C) EC2 instances with an Application Load Balancer, CloudFront distribution, and AWS WAF on the ALB.
*   D) S3 bucket with public read, Amazon CloudFront, and a Network Load Balancer for DDoS protection.
*   **Correct Answer:** B) Private S3 + CloudFront OAC provides secure origin access; CloudFront delivers globally at low latency; WAF filters malicious requests; Shield Standard is automatically included with CloudFront.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* S3 static website hosting with public read access exposes the S3 URL directly — violating the "no direct public S3 URL access" requirement. Route 53 provides DNS but not CDN or WAF protection. Shield Standard is included but WAF is missing.
    *   *Why B is correct:* This is the complete, production-grade static website architecture on AWS. OAC restricts S3 access to the CloudFront distribution only. CloudFront delivers from 400+ global edge locations. WAF Web ACL on the distribution filters SQL injection, XSS, and bot traffic. Shield Standard is automatically active on all CloudFront distributions at no additional cost.
    *   *Why C is incorrect:* EC2 instances are unnecessary for a static website — this adds cost and operational overhead. A static website is purely S3-served content; no server-side compute is required. Adding EC2 violates the simplicity principle and increases cost without benefit.
    *   *Why D is incorrect:* Network Load Balancers operate at Layer 4 and are not DDoS protection services — they are traffic distribution services. NLBs do not provide WAF, edge caching, or DDoS mitigation. Additionally, making S3 public undermines the origin security requirement.

---

**Question 4**
A startup receives inconsistent traffic — sometimes zero requests, sometimes thousands per second with no predictable pattern. They need a backend API that scales to zero when idle (no idle cost) and handles spikes automatically without pre-provisioning. Which compute approach satisfies these requirements?
*   A) EC2 Auto Scaling with a minimum of 0 instances — the ASG scales from zero when traffic begins.
*   B) AWS Lambda with API Gateway — Lambda scales automatically per request and costs nothing when idle, with no minimum provisioned capacity.
*   C) Amazon ECS with Fargate — Fargate scales to minimum 1 task when idle to maintain readiness.
*   D) EC2 Reserved Instances — commit to 1-year term for cost predictability; the reserved instance always runs.
*   **Correct Answer:** B) Lambda + API Gateway scales to zero (no invocations = no charges) and scales horizontally to thousands of concurrent executions for spikes, making it ideal for unpredictable variable workloads.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* EC2 Auto Scaling with minimum 0 instances is technically possible, but "scale from zero" for EC2 is slow (2–3 minutes to launch, configure, and pass health checks) — inadequate for handling sudden traffic spikes. Additionally, there is no built-in HTTP request handling; you still need an ALB, which has a minimum hourly cost regardless of traffic.
    *   *Why B is correct:* Lambda has no minimum provisioned instances. When there are zero invocations, there is zero cost. When traffic spikes, Lambda automatically provisions hundreds of concurrent execution environments within seconds. API Gateway routes HTTP requests to Lambda with no idle infrastructure cost. This is the "scale to zero" serverless pattern.
    *   *Why C is incorrect:* Fargate ECS tasks have a minimum running task configuration to maintain service availability. While ECS Service Auto Scaling can scale to 1 task minimum, that 1 task has a continuous Fargate compute cost even during idle periods. Fargate does not scale to zero for long-running services.
    *   *Why D is incorrect:* Reserved Instances require a 1- or 3-year commitment with continuous hourly billing regardless of utilization. For a workload with periods of zero traffic, Reserved Instances generate 100% idle cost during those periods — the worst cost outcome for variable workloads.

---

**Question 5**
A solutions architect is finalizing an architecture review. The application stores user PII (Personally Identifiable Information) in an S3 bucket, uses RDS MySQL for transactional data, runs on EC2 in private subnets, and receives public traffic through an ALB. To satisfy a compliance audit requiring encryption of all data at rest with auditable key usage logs, which configuration is required?
*   A) Enable S3 default encryption with SSE-S3, enable RDS encryption at creation using AWS-managed keys, and enable EBS encryption on EC2 volumes — no key audit logging configuration required.
*   B) Enable SSE-KMS on the S3 bucket using a Customer Managed Key, enable RDS encryption at creation using a KMS CMK, and enable EBS volume encryption with a KMS CMK — KMS automatically logs all key usage to CloudTrail.
*   C) Install PGP encryption on the EC2 instances and encrypt all data before writing to S3 and RDS; store PGP keys in EC2 instance local storage for fastest access.
*   D) Enable S3 Transfer Acceleration for encrypted transfers to S3, enable RDS SSL connections, and configure VPC Flow Logs to record network traffic.
*   **Correct Answer:** B) SSE-KMS with Customer Managed Keys on S3, RDS, and EBS provides encryption at rest across all data stores, and every KMS API call (GenerateDataKey, Decrypt) is automatically logged to CloudTrail — satisfying the key usage audit requirement.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* SSE-S3 and AWS-managed RDS encryption do encrypt data at rest, but key usage is NOT logged to CloudTrail for SSE-S3 or AWS-managed keys. The compliance requirement explicitly requires "auditable key usage logs," which is only provided by KMS Customer Managed Keys integrated with CloudTrail.
    *   *Why B is correct:* KMS CMKs are the compliance answer for "auditable key usage." Every KMS API call — including the Decrypt calls made when reading S3 objects, RDS backups, or EBS snapshots — is logged to CloudTrail with the IAM principal identity, timestamp, and key ARN. This provides the complete audit trail required by PCI DSS, HIPAA, and SOC 2.
    *   *Why C is incorrect:* Client-side PGP encryption is technically valid but requires the customer to manage all key material outside of AWS, is not integrated with CloudTrail for audit logging, and storing keys in EC2 instance local storage is a critical security anti-pattern (keys are lost if the instance terminates, and accessible to anyone with OS access).
    *   *Why D is incorrect:* S3 Transfer Acceleration is a network performance feature for uploads; SSL/TLS on RDS is encryption in transit (not at rest); VPC Flow Logs capture network metadata. None of these address the encryption-at-rest or key audit logging requirements. In-transit encryption (TLS) and at-rest encryption (KMS) are complementary but separate requirements.


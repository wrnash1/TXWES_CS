# Quiz: Module 16 — SAA-C03 Exam Preparation (20 Practice Questions)

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Instructions

This practice quiz contains 20 questions spanning all four SAA-C03 exam domains. It simulates exam-style questions with the same structure, distractor patterns, and domain coverage as the actual SAA-C03 exam. Attempt all questions before reviewing the answer key. Each question is worth 5 points (100 points total).

---

## Question 1 — Domain 1: Resilient Architectures

A company runs a three-tier web application on EC2. The database is a single RDS MySQL instance in one Availability Zone. The company wants to achieve an RTO of under 10 minutes for a database AZ failure without application code changes. Which solution achieves this at the LOWEST cost?

- A. Enable RDS Read Replicas in a second AZ and manually promote on failure
- B. Enable RDS Multi-AZ on the existing instance
- C. Migrate to Aurora Global Database with a secondary region
- D. Create daily RDS snapshots and restore from the latest snapshot on failure

### Q1 Answer: B

### Q1 Analysis

A is incorrect. Read Replicas use asynchronous replication and are not designed for automatic failover. Promoting a Read Replica is a manual process and can take longer than 10 minutes. They also do not meet the "without application code changes" requirement if the endpoint changes.

B is correct. RDS Multi-AZ maintains a synchronous standby replica in a second AZ. On AZ failure, RDS automatically fails over to the standby in typically 60–120 seconds, well within the 10-minute RTO. The endpoint DNS name remains the same — no application changes required.

C is incorrect. Aurora Global Database spans multiple AWS regions. This is appropriate for multi-region DR, not single-region AZ failure. It is also significantly more expensive than Multi-AZ.

D is incorrect. Restoring from a snapshot creates a new RDS instance from scratch — this takes 20–40 minutes or more depending on database size, far exceeding the 10-minute RTO.

---

## Question 2 — Domain 3: Secure Architectures

A company stores sensitive financial documents in an S3 bucket. The security team requires that all objects be encrypted with a customer-managed KMS key so that key usage is auditable via CloudTrail. They also want to enforce that objects CANNOT be uploaded without encryption. Which combination achieves both requirements?

- A. Enable SSE-S3 default encryption and apply an S3 bucket policy denying uploads without `x-amz-server-side-encryption: AES256`
- B. Enable SSE-KMS with a customer-managed key as the default encryption, and apply an S3 bucket policy denying uploads that do not specify `x-amz-server-side-encryption: aws:kms`
- C. Enable SSE-S3 and enable CloudTrail data events on the bucket
- D. Enable SSE-KMS and rely on default bucket encryption without a bucket policy

### Q2 Answer: B

### Q2 Analysis

A is incorrect. SSE-S3 (`AES256`) uses AWS-managed keys and does not generate CloudTrail key usage events. The question requires a customer-managed KMS key with an audit trail.

B is correct. SSE-KMS with a customer-managed key generates a CloudTrail event every time the key is used to encrypt or decrypt an object — providing the required audit trail. The S3 bucket policy with a Deny condition on requests missing `aws:kms` server-side-encryption ensures all uploads are encrypted. Default encryption alone does not prevent uploads with no encryption header.

C is incorrect. SSE-S3 does not use KMS and does not generate CloudTrail key usage events. CloudTrail data events capture S3 API calls but not individual key usage.

D is incorrect. Default encryption with SSE-KMS encrypts objects uploaded without an explicit encryption header. However, without the bucket policy, an object could theoretically be uploaded with SSE-S3 encryption instead of SSE-KMS, bypassing the KMS audit requirement.

---

## Question 3 — Domain 2: High-Performing Architectures

A mobile app backend uses DynamoDB as its primary data store. Analytics queries on historical data are causing throttling on the DynamoDB table and degrading real-time user experience. The analytics queries read large amounts of data infrequently. Which solution addresses the performance issue with MINIMAL changes to the existing architecture?

- A. Increase DynamoDB RCUs provisioned on the main table to handle analytics workload
- B. Enable DynamoDB Streams and use Kinesis Firehose to deliver historical data to Amazon S3 for Athena queries
- C. Add a DAX cluster in front of DynamoDB to accelerate analytics queries
- D. Enable DynamoDB global tables in a second region for analytics

### Q3 Answer: B

### Q3 Analysis

A is incorrect. Increasing RCUs raises the cost continuously to accommodate infrequent analytics queries. This does not solve the throttling architecture problem — it just makes throttling less frequent while paying for unused capacity.

B is correct. DynamoDB Streams export change data to Kinesis Firehose, which delivers it to S3. Athena queries S3 directly without touching DynamoDB at all. Historical analytics are offloaded entirely from the operational DynamoDB table, eliminating interference with real-time users. S3 + Athena is also significantly cheaper for analytical queries than DynamoDB RCU consumption.

C is incorrect. DAX is an in-memory cache that accelerates DynamoDB reads for frequently accessed items. Analytics queries read large, infrequently accessed historical data — DAX cache hit rates would be low, providing minimal benefit.

D is incorrect. Global tables replicate the full DynamoDB table to a second region for multi-region writes. Querying the replica still consumes RCUs from the same table and does not offload the workload from the primary table's capacity.

---

## Question 4 — Domain 4: Cost-Optimized Architectures

A startup runs a development environment with EC2 instances that are only used during business hours (8 AM–6 PM Monday–Friday). The instances are m5.xlarge and run a total of 50 hours per week. Which EC2 purchasing configuration minimizes cost?

- A. Reserved Instances (1-year, All Upfront) for all instances
- B. On-Demand Instances with scheduled stop/start via Lambda and EventBridge
- C. Spot Instances with a persistent request
- D. Dedicated Hosts with a 1-year commitment

### Q4 Answer: B

### Q4 Analysis

A is incorrect. Reserved Instances provide a discount for committed, continuous usage. At 50 hours/week (30% of available hours), the RI commitment pays for idle capacity. The effective hourly cost with an RI is higher than On-Demand for a 30% utilization rate.

B is correct. On-Demand instances stopped during non-business hours (nights and weekends) incur no instance-hour charges while stopped. A simple Lambda function triggered by EventBridge on a cron schedule can start and stop the instances automatically. With ~50 hours of weekly usage, On-Demand with stop/start is the most cost-effective approach.

C is incorrect. Spot Instances can be interrupted at any time. A development environment that disappears mid-afternoon when a developer is actively working is unacceptable.

D is incorrect. Dedicated Hosts are the most expensive EC2 option. They are used for per-socket software licensing requirements, which is not mentioned here.

---

## Question 5 — Domain 1: Resilient Architectures

An application processes financial transactions. Requirements state that no transaction can be processed more than once and transactions must be processed in the order they were received. The processing Lambda function takes up to 45 seconds per transaction. Which SQS configuration satisfies ALL requirements?

- A. SQS Standard queue with Visibility Timeout set to 60 seconds
- B. SQS FIFO queue with Visibility Timeout set to 60 seconds and a DLQ
- C. SQS Standard queue with a DLQ and deduplication logic in the Lambda function
- D. SQS FIFO queue with a message group ID per transaction batch and Visibility Timeout set to 60 seconds

### Q5 Answer: D

### Q5 Analysis

A is incorrect. SQS Standard queues provide best-effort ordering, not strict FIFO, and at-least-once delivery — not exactly-once. Financial transaction processing cannot accept out-of-order or duplicate processing.

B is incorrect. A generic FIFO queue with a single message group would process all transactions strictly in order but sequentially (one at a time). For financial transactions, each independent transaction needs its own message group to enable parallel processing while maintaining per-group order. However, if transactions are truly globally sequential (no parallelism needed), B would work. The question does not specify independent groups.

C is incorrect. SQS Standard queues cannot guarantee ordering regardless of Lambda deduplication logic.

D is correct. SQS FIFO provides exactly-once processing and strict ordering. Using a message group ID per logical transaction batch allows parallel processing of independent batches while maintaining order within each group. Visibility Timeout of 60 seconds (greater than the 45-second processing time) prevents the message from becoming visible to other consumers while being processed.

---

## Question 6 — Domain 3: Secure Architectures

A company's EC2 instances in private subnets need to access Amazon S3 without traversing the internet. The company also wants to ensure that S3 bucket access is restricted to requests originating from the VPC. Which TWO configurations achieve this? (Select TWO.)

- A. Create an S3 VPC Gateway Endpoint and update the route tables in the private subnets
- B. Configure the S3 bucket policy to deny requests where `aws:sourceVpce` does not match the endpoint ID
- C. Configure the S3 bucket policy to allow only the EC2 instance IAM role
- D. Enable S3 Transfer Acceleration on the bucket
- E. Create a NAT Gateway in a public subnet and route S3 traffic through it

### Q6 Answer: A and B

### Q6 Analysis

A is correct. An S3 Gateway VPC Endpoint routes S3 traffic from the VPC through the AWS private network. Traffic never traverses the public internet. Route table entries in the private subnets must be updated to direct S3-destined traffic to the endpoint.

B is correct. Adding a bucket policy condition `"aws:sourceVpce": "vpce-xxxx"` (or `"aws:sourceVpc": "vpc-xxxx"`) denies requests from outside the VPC, ensuring only VPC-originating requests reach the bucket. This enforces the network-level access restriction at the bucket policy level.

C is incorrect. Restricting the bucket policy to an EC2 IAM role controls who can access the bucket but does not prevent access from outside the VPC. An attacker with the same IAM credentials from outside the VPC could still access the bucket.

D is incorrect. S3 Transfer Acceleration speeds up uploads from distant clients over the internet — it does not restrict access to VPC-originating traffic.

E is incorrect. Routing S3 traffic through a NAT Gateway sends it over the internet, which is exactly what the question aims to avoid. NAT Gateway also incurs data processing charges per GB.

---

## Question 7 — Domain 2: High-Performing Architectures

A global e-commerce company serves customers across North America, Europe, and Asia. Static product images and JavaScript bundles are served from an S3 bucket in us-east-1. Users in Asia report 3-4 second load times for the images. Which solution reduces Asia load times to under 500 ms with MINIMAL architectural changes?

- A. Create S3 buckets in ap-southeast-1 and ap-northeast-1 and replicate objects via S3 Cross-Region Replication
- B. Deploy an Application Load Balancer in ap-southeast-1 and configure it to proxy requests to the S3 bucket in us-east-1
- C. Configure Amazon CloudFront with the S3 bucket as the origin and enable geo-restriction to all regions
- D. Configure Amazon CloudFront with the S3 bucket as the origin, no geo-restriction

### Q7 Answer: D

### Q7 Analysis

A is incorrect. Creating multiple S3 buckets with CRR requires updating application code to use different bucket URLs per region, or adding a routing layer. This is not "minimal architectural changes."

B is incorrect. An ALB in ap-southeast-1 proxying to us-east-1 still sends every request across the Pacific — it adds the ALB hop without reducing latency.

C is incorrect. Geo-restriction on CloudFront blocks specific countries or regions from accessing content — it does not optimize delivery to those regions. Restricting Asia defeats the purpose.

D is correct. CloudFront caches static content at 450+ global edge locations. Users in Asia are served from the nearest edge location — typically within 20–50 ms. The first request for each object fetches from the S3 origin (us-east-1), but subsequent requests are served from cache. No application code changes are needed — CloudFront uses the existing S3 URL as origin. Origin Access Control (OAC) restricts direct S3 bucket access.

---

## Question 8 — Domain 1: Resilient Architectures

A company wants to implement a disaster recovery strategy where a minimal set of AWS resources are always running in a secondary region to reduce recovery time. If a disaster occurs in the primary region, the team scales up the secondary region to full capacity within 15 minutes. Which DR strategy is described?

- A. Backup and Restore
- B. Multi-Site Active-Active
- C. Pilot Light
- D. Warm Standby

### Q8 Answer: C

### Q8 Analysis

A is incorrect. Backup and Restore has no continuously running resources in the secondary region. All resources must be created from backups on disaster, resulting in hours-long RTO.

B is incorrect. Multi-Site Active-Active runs full production capacity in two regions simultaneously with near-zero RTO. The description states "minimal set of resources" running, not full capacity.

C is correct. Pilot Light maintains a minimal set of core infrastructure always running in the secondary region (database replication, a minimal instance or container). On disaster, scale up around the core. 15-minute RTO is consistent with Pilot Light.

D is incorrect. Warm Standby runs a scaled-down but fully functional copy of the production environment — not a "minimal set" of core resources. Warm Standby provides shorter RTO (minutes) but at higher cost than Pilot Light.

---

## Question 9 — Domain 4: Cost-Optimized Architectures

A data analytics company processes large datasets using EMR (Hadoop) clusters. Jobs run every night for 6 hours. Clusters are terminated after each job completes. The team has been using On-Demand EC2 instances for the core and task nodes. Which change reduces cost the MOST?

- A. Purchase Reserved Instances for the task nodes since they run nightly
- B. Use Spot Instances for the task nodes and On-Demand for the core nodes
- C. Use Spot Instances for all nodes including core nodes
- D. Switch from EMR to AWS Glue for ETL processing

### Q9 Answer: B

### Q9 Analysis

A is incorrect. Reserved Instances for nightly 6-hour workloads represent 25% utilization (6 hours / 24 hours). At 25% utilization, the RI discount (up to 72%) does not offset the 75% idle capacity cost compared to On-Demand with automatic termination.

B is correct. EMR best practice splits the cluster into core nodes (use On-Demand for reliability — losing core nodes can fail the job) and task nodes (use Spot for up to 90% discount — task nodes are stateless and can be replaced if interrupted). This achieves maximum savings while protecting the job from catastrophic failure.

C is incorrect. Core nodes store HDFS data. If Spot Instances are interrupted on core nodes, HDFS data blocks are lost and the job fails. Using Spot for core nodes is inappropriate for reliable production workloads.

D is incorrect. Switching to Glue is a refactoring decision that may not be feasible or desirable for Hadoop-dependent workloads. The question asks for the most cost-effective change within the existing EMR architecture.

---

## Question 10 — Domain 3: Secure Architectures

A solutions architect is designing an architecture where Lambda functions need to access an RDS PostgreSQL database in a private subnet. The database credentials must not be hardcoded and must be automatically rotated every 30 days. Which approach satisfies BOTH requirements?

- A. Store credentials in SSM Parameter Store (SecureString); manually rotate every 30 days using a Lambda function
- B. Store credentials in AWS Secrets Manager and enable automatic rotation with the RDS rotation Lambda
- C. Store credentials as Lambda environment variables encrypted with KMS; manually rotate every 30 days
- D. Create an IAM role for Lambda with `rds:Connect` permissions; use IAM database authentication

### Q10 Answer: B

### Q10 Analysis

A is incorrect. SSM Parameter Store does not support automatic rotation natively. Manual rotation every 30 days requires human intervention and creates an operational burden. The question requires automatic rotation.

B is correct. AWS Secrets Manager stores the database credentials securely, integrated with KMS for encryption. The built-in RDS rotation Lambda function automatically rotates credentials on the configured schedule (every 30 days). Lambda functions retrieve the current credential from Secrets Manager at runtime using the Secrets Manager API — no hardcoded credentials.

C is incorrect. Lambda environment variables cannot be automatically rotated. Environment variables require a Lambda function redeployment or explicit update to change their values.

D is incorrect. IAM database authentication (using IAM role + RDS auth token) is an excellent approach that eliminates long-lived credentials entirely. However, it requires the Lambda function to generate a temporary auth token on each connection and requires RDS to have IAM authentication enabled. While technically valid, the question specifically asks about credentials management with rotation, which Secrets Manager directly addresses.

---

## Question 11 — Domain 2: High-Performing Architectures

A media streaming company needs to serve live video to 500,000 concurrent viewers globally. The video stream originates from a single encoding server in us-east-1. Which architecture BEST handles the viewer scale?

- A. Deploy ALBs in every region and use Route 53 geolocation routing to direct viewers to the nearest ALB
- B. Use Amazon CloudFront with an EC2 origin and configure streaming with CloudFront's media streaming protocols
- C. Use Amazon CloudFront with Amazon IVS (Interactive Video Service) or Elemental MediaPackage as origin
- D. Deploy EC2 instances with an Elastic IP in every region and use Route 53 weighted routing

### Q11 Answer: C

### Q11 Analysis

A is incorrect. ALBs in multiple regions with manual EC2 origin replication do not natively handle live video streaming at scale. This architecture requires significant custom engineering for stream distribution.

B is incorrect. While CloudFront with an EC2 origin works for static content, a single EC2 origin cannot handle 500,000 concurrent live stream requests even with CloudFront caching, because live streams generate origin requests per viewer per segment.

C is correct. MediaPackage (or IVS) is a managed video packaging and origination service designed for live streaming at massive scale. CloudFront distributes the packaged segments to 450+ edge locations globally, dramatically reducing origin load. This is the AWS reference architecture for large-scale live streaming.

D is incorrect. Deploying EC2 in every region with Route 53 routing requires identical stream ingest and distribution infrastructure in every region — operationally complex and cost-prohibitive. This does not leverage AWS's managed media services.

---

## Question 12 — Domain 1: Resilient Architectures

An application stores session state in a single EC2-hosted Redis cache. If the instance fails, all user sessions are lost and users must log in again. The operations team wants to eliminate this single point of failure. Which solution provides Redis session storage with automatic failover at the LOWEST operational overhead?

- A. Deploy two EC2 instances running Redis with manual failover scripts
- B. Use Amazon ElastiCache for Redis with Multi-AZ and automatic failover enabled
- C. Use Amazon DynamoDB to store session data instead of Redis
- D. Use Amazon RDS with a read replica in a second AZ for session storage

### Q12 Answer: B

### Q12 Analysis

A is incorrect. Manual failover scripts add operational complexity and introduce human latency into the recovery process. This is the exact undifferentiated heavy lifting that managed services eliminate.

B is correct. ElastiCache for Redis with Multi-AZ maintains a synchronous standby replica in a second AZ. On primary node failure, ElastiCache automatically promotes the standby in under 60 seconds. The endpoint DNS name remains the same. Zero operational overhead for failover management.

C is incorrect. DynamoDB can store session data, but DynamoDB is a NoSQL database, not an in-memory cache. Sessions stored in DynamoDB have millisecond latency (vs. microsecond for Redis), and DynamoDB access costs more for high-frequency small reads than ElastiCache.

D is incorrect. RDS is a relational database designed for durable structured data, not ephemeral session data. Using RDS for session storage is architecturally inappropriate and expensive for high-frequency short-lived data.

---

## Question 13 — Domain 3: Secure Architectures

A company recently experienced a security incident where an EC2 instance was communicating with a known cryptocurrency mining command-and-control server. The security team wants to detect similar threats automatically in the future across all AWS accounts in their AWS Organization. Which service detects this threat and how should it be deployed?

- A. Enable Amazon Inspector on all EC2 instances; scan for vulnerability CVEs
- B. Enable Amazon GuardDuty at the organization level from the management account; enable all finding types
- C. Enable AWS Config rules for network compliance across all accounts
- D. Enable VPC Flow Logs and write custom CloudWatch Metric Filters to detect outbound connections to threat feeds

### Q13 Answer: B

### Q13 Analysis

A is incorrect. Amazon Inspector scans for software vulnerabilities (CVEs), network reachability, and unintended network exposure. It does not monitor for active threat actor communication or cryptocurrency mining behavior at runtime.

B is correct. GuardDuty specifically detects `CryptoCurrency:EC2/BitcoinTool.B!DNS` and similar findings by analyzing DNS logs and VPC Flow Logs using ML-based threat intelligence. Enabling GuardDuty at the organization level from the management account deploys it automatically across all member accounts and aggregates findings centrally.

C is incorrect. AWS Config evaluates resource configurations for compliance policies (encrypted volumes, open security groups). It does not analyze network traffic for active threat actor communication.

D is incorrect. Writing custom metric filters against Flow Logs to detect specific IPs from threat feeds is technically possible but requires maintaining a threat feed database, writing custom logic, and ongoing maintenance. This is an extremely high-operational-overhead solution compared to enabling GuardDuty.

---

## Question 14 — Domain 4: Cost-Optimized Architectures

A company's AWS bill shows $4,200/month in NAT Gateway data processing charges. Investigation reveals that most of the traffic is EC2 instances in private subnets accessing Amazon S3 and DynamoDB. Which change eliminates the NAT Gateway charges for THIS specific traffic?

- A. Move all EC2 instances from private subnets to public subnets
- B. Create S3 and DynamoDB VPC Gateway Endpoints and update private subnet route tables
- C. Replace the NAT Gateway with a NAT instance on a t3.micro for lower cost
- D. Enable S3 Transfer Acceleration to bypass NAT Gateway

### Q14 Answer: B

### Q14 Analysis

A is incorrect. Moving instances to public subnets introduces significant security risk by exposing them directly to the internet. This is not an acceptable cost optimization strategy for production workloads.

B is correct. S3 and DynamoDB Gateway Endpoints route traffic through the AWS private network, bypassing the NAT Gateway entirely. There is no per-GB charge for Gateway Endpoint traffic. Route table entries direct S3/DynamoDB-destined traffic to the endpoint instead of the NAT Gateway. This can eliminate the majority of NAT Gateway data processing charges when S3 and DynamoDB are the primary traffic sources.

C is incorrect. A NAT instance still processes the data — it just has a lower hourly rate than NAT Gateway. It does not eliminate the data processing charges and introduces management overhead (patching, HA configuration).

D is incorrect. S3 Transfer Acceleration speeds up uploads from distant internet clients. It does not affect traffic routing between EC2 instances in private subnets and S3, and it does not bypass NAT Gateway.

---

## Question 15 — Domain 1: Resilient Architectures

A global company runs a DynamoDB table used by applications in us-east-1. They want to expand to ap-southeast-1 so that users in Asia can write and read data with low latency, and data written in Asia is automatically available in North America within seconds. Which DynamoDB feature satisfies this requirement?

- A. DynamoDB Read Replicas in ap-southeast-1
- B. DynamoDB global tables with replicas in both regions
- C. DynamoDB Streams with a Lambda function replicating writes to a second table in ap-southeast-1
- D. DynamoDB Cross-Region Backup Restore from us-east-1 to ap-southeast-1 daily

### Q15 Answer: B

### Q15 Analysis

A is incorrect. DynamoDB does not have Read Replicas in the same sense as RDS. DynamoDB global tables provide multi-region replication — there is no "Read Replica only" feature for cross-region DynamoDB.

B is correct. DynamoDB global tables provide active-active, multi-region replication. Applications in both regions can write to their local replica, and DynamoDB automatically replicates changes to all other replicas typically within 1 second. This exactly satisfies the requirement for low-latency reads and writes in Asia with automatic propagation to North America.

C is incorrect. Custom Lambda-based replication via DynamoDB Streams is brittle, adds latency, and introduces replication bugs and failure modes. AWS provides global tables as a managed solution specifically for this use case.

D is incorrect. Daily backup restore provides data once per day, not within seconds. This provides no real-time replication.

---

## Question 16 — Domain 3: Secure Architectures

A company needs to grant a third-party auditing firm temporary, read-only access to specific AWS resources in their account. The auditors use their own AWS account. Which approach follows AWS security best practices for this cross-account access?

- A. Create an IAM user in the company's account with a long-term access key; share the access key with the auditors
- B. Create an IAM role in the company's account with a trust policy allowing the auditing firm's AWS account to assume it
- C. Create an IAM group with read-only permissions and add the auditors as IAM users in the company's account
- D. Share AWS account root credentials temporarily with the auditing firm

### Q16 Answer: B

### Q16 Analysis

A is incorrect. Long-term access keys are a security risk — they do not expire, can be accidentally exposed, and are not tied to specific individuals. Creating a shared key for an entire auditing firm provides no individual accountability.

B is correct. An IAM Role with a cross-account trust policy allows the auditing firm to assume the role using their own IAM identities. Temporary credentials are generated for the session (maximum 12 hours). When the audit is complete, simply delete the trust policy or the role. No long-term credentials are created or shared.

C is incorrect. Creating IAM users in the company's account for third-party personnel is an anti-pattern. Long-term credentials are created, and offboarding requires explicitly deleting each user account.

D is incorrect. Sharing root credentials is never acceptable under any circumstances. Root credentials provide unrestricted access to all AWS services and resources.

---

## Question 17 — Domain 2: High-Performing Architectures

An application runs on EC2 and writes large sequential log files to EBS. The volumes frequently hit IOPS limits, causing write throttling. The team wants to eliminate throttling for sequential writes at the lowest cost. Which EBS volume type change addresses this?

- A. Switch from gp3 to io2 Block Express for maximum IOPS
- B. Switch from gp3 to st1 (Throughput Optimized HDD)
- C. Switch from gp3 to sc1 (Cold HDD)
- D. Increase the gp3 volume size to automatically increase IOPS

### Q17 Answer: B

### Q17 Analysis

A is incorrect. io2 Block Express is optimized for high random IOPS workloads (databases requiring up to 256,000 IOPS). Sequential log writes are a throughput-bound, not IOPS-bound, workload. io2 is significantly more expensive with no benefit for sequential writes.

B is correct. st1 (Throughput Optimized HDD) is designed specifically for large, sequential workloads — Kafka logs, big data processing, ETL pipelines. It provides up to 500 MB/s throughput at a lower cost than SSD-based volumes. Throttling on sequential writes is eliminated by choosing the throughput-optimized volume type.

C is incorrect. sc1 (Cold HDD) is for infrequent large sequential access — it provides lower throughput than st1 (up to 250 MB/s) and is not appropriate for active log write workloads.

D is incorrect. gp3 IOPS and throughput are decoupled from volume size — you can configure IOPS independently. However, gp3 max throughput is 1,000 MB/s, which is sufficient for most workloads. If the issue is truly IOPS throttling on sequential writes, st1's throughput model is more appropriate and cheaper.

---

## Question 18 — Domain 1: Resilient Architectures

A company processes insurance claims through a 7-step workflow: intake, validation, fraud check, underwriting, approval, payment, and notification. Each step is currently a Lambda function invoking the next via direct SDK call. The team reports that when any step fails, they cannot determine which step failed, and failed workflows cannot be resumed from the failed step without reprocessing the entire claim. Which AWS service change resolves BOTH issues?

- A. Add CloudWatch Alarms on Lambda error metrics for each function
- B. Migrate the workflow to AWS Step Functions Standard Workflow
- C. Add SQS queues between every pair of Lambda functions
- D. Enable X-Ray Active Tracing on all Lambda functions

### Q18 Answer: B

### Q18 Analysis

A is incorrect. CloudWatch Alarms alert when a function errors but do not identify which step in a workflow failed for a specific execution, nor do they enable resuming from a failed step.

B is correct. Step Functions provides: (1) full execution history showing exactly which state failed, what the input was, and what the error was; and (2) error handling with `Catch` and `Retry` blocks at each state that can route to failure compensation steps. Executions can be re-run from the beginning with corrected input, or human approval can be added at the failed step. Step Functions directly resolves both problems.

C is incorrect. Adding SQS queues between Lambda functions improves decoupling but does not provide workflow visibility or the ability to resume a workflow from a specific failed step.

D is incorrect. X-Ray tracing identifies where latency or errors occur within a single invocation. It does not provide workflow-level execution history across multiple Lambda functions over the course of a multi-step business process.

---

## Question 19 — Domain 4: Cost-Optimized Architectures

A company runs 100 m5.2xlarge On-Demand EC2 instances continuously. AWS Compute Optimizer recommends downsizing 40 of them to m5.xlarge. The team accepts 30 of the recommendations but decides to keep 10 at m5.2xlarge due to an upcoming product launch driving higher load for 2 months. Which COMBINATION of purchasing options minimizes cost for the entire fleet?

- A. All 100 instances: On-Demand
- B. 30 downsized instances: 1-year EC2 Instance Savings Plan; 60 remaining m5.2xlarge: On-Demand
- C. 30 downsized instances: 1-year EC2 Instance Savings Plan; 60 remaining m5.2xlarge: 1-year RI
- D. 30 downsized instances: 1-year Compute Savings Plan; 60 remaining m5.2xlarge: 1-year Compute Savings Plan

### Q19 Answer: D

### Q19 Analysis

A is incorrect. 100 instances continuously on On-Demand means paying full price with no commitment discounts. After the 2-month product launch, the 60 m5.2xlarge instances will likely be downsized — a Savings Plan on Compute covers that eventual transition.

B is incorrect. On-Demand for 60 continuously running m5.2xlarge instances wastes the discount opportunity for steady-state workloads.

C is incorrect. A 1-year RI for the 60 m5.2xlarge instances locks in that specific instance type for the full year. If the team downsizes those instances after the 2-month product launch, the RI commitment still charges for m5.2xlarge even if running smaller instances.

D is correct. Compute Savings Plans apply to any EC2 instance family, size, OS, and tenancy. If the 60 m5.2xlarge instances are downsized after the product launch, the Compute Savings Plan automatically applies to the smaller instances. Maximum flexibility with up to 66% discount.

---

## Question 20 — Domain 3: Secure Architectures

A company must ensure that an S3 bucket containing financial audit logs cannot have objects deleted or overwritten for 7 years, regardless of which IAM user or role (including the root account) makes the deletion request. Which S3 feature enforces this?

- A. S3 Versioning with MFA Delete enabled
- B. S3 Object Lock in Compliance mode with a 7-year retention period
- C. S3 Object Lock in Governance mode with a 7-year retention period
- D. S3 Bucket Policy denying `s3:DeleteObject` for all principals

### Q20 Answer: B

### Q20 Analysis

A is incorrect. MFA Delete requires multi-factor authentication to permanently delete versioned objects or suspend versioning. It is a deterrent but can be disabled by an administrator with root account access. It does not prevent deletion by all principals including root.

B is correct. S3 Object Lock in Compliance mode prevents ANY user, including the root account, from overwriting, deleting, or modifying the retention settings for the duration of the retention period. This is the only mechanism that truly protects against deletion by all principals for the retention duration. Compliance mode is required for SEC Rule 17a-4(f), FINRA, and similar regulations.

C is incorrect. S3 Object Lock in Governance mode can be overridden by users with the `s3:BypassGovernanceRetention` IAM permission. This does not protect against authorized IAM administrators. Governance mode is appropriate when you want protection with an administrative override capability.

D is incorrect. An S3 Bucket Policy denying DeleteObject can be modified or deleted by an IAM user or role with `s3:PutBucketPolicy` permission, including the root account. Bucket policies do not provide immutable protection.

---

## Question 21 — Domain 1: Design Resilient Architectures

A company's e-commerce application serves customers globally. The application runs on EC2 in `us-east-1` and `eu-west-1` with Route 53 latency-based routing. During a full `us-east-1` regional outage, Route 53 continues directing 50% of traffic there because health checks are not configured. What is the correct fix?

- A. Switch from latency-based routing to geolocation routing
- B. Add Route 53 health checks to each regional endpoint and associate them with the latency routing records
- C. Enable Route 53 DNSSEC to detect and block unhealthy endpoints automatically
- D. Increase the TTL on Route 53 records so clients cache the healthy endpoint longer

### Q21 Answer: B

### Q21 Analysis

A is incorrect. Geolocation routing directs traffic based on the requester's geographic location — it does not perform health-based failover. Clients in North America would still be directed to `us-east-1` even if it is unavailable.

B is correct. Route 53 routing policies (latency, weighted, geolocation) only perform failover when health checks are associated with the records. Without health checks, Route 53 continues to return all records regardless of endpoint health. Adding health checks to each regional record causes Route 53 to stop returning the `us-east-1` record when it fails, directing all traffic to `eu-west-1`.

C is incorrect. DNSSEC validates the authenticity and integrity of DNS responses to prevent spoofing — it has no relationship to endpoint health monitoring or failover behavior.

D is incorrect. Increasing TTL makes clients cache DNS responses longer, which would worsen the situation during a regional outage — clients that cached the `us-east-1` address would continue using it longer before receiving an updated healthy record.

---

## Question 22 — Domain 2: Design High-Performing Architectures

A video streaming company stores large video files in S3 in `us-east-1`. Users in Southeast Asia report slow initial load times and buffering. Which solution provides the greatest improvement in streaming performance for these users?

- A. Enable S3 Transfer Acceleration on the bucket
- B. Deploy Amazon CloudFront with the S3 bucket as the origin and edge locations serving Southeast Asia
- C. Create an S3 bucket replica in `ap-southeast-1` using S3 Cross-Region Replication
- D. Increase the EC2 instance size of the application server that generates presigned S3 URLs

### Q22 Answer: B

### Q22 Analysis

A is incorrect. S3 Transfer Acceleration speeds up uploads TO S3 from distant clients — it accelerates write operations, not download or streaming performance for end users reading from S3.

B is correct. CloudFront caches video content at edge locations geographically close to Southeast Asian viewers. Subsequent requests for the same content are served from the edge location with sub-millisecond response times, eliminating the cross-Pacific round-trip latency that causes buffering.

C is incorrect. S3 CRR replicates objects to a bucket in `ap-southeast-1`, which would reduce latency for direct S3 access — but requires application changes to route Southeast Asian users to the replica bucket. It also does not provide the edge caching benefit of CloudFront for repeated access to the same content.

D is incorrect. The application server generates presigned URLs for S3 access — its size does not affect the actual video streaming performance. The bottleneck is the geographic distance between the S3 bucket and the end user, not the application server.

---

## Question 23 — Domain 3: Secure Architectures

A company has multiple AWS accounts in an AWS Organization. The security team wants to prevent any account from disabling AWS CloudTrail — even account administrators. Which control achieves this?

- A. Apply an IAM permission boundary to all IAM roles in each account, denying `cloudtrail:StopLogging`
- B. Apply an SCP to the Organization root or relevant OUs that denies `cloudtrail:StopLogging` and `cloudtrail:DeleteTrail`
- C. Enable AWS Config with a rule that detects and automatically re-enables CloudTrail when it is disabled
- D. Configure CloudTrail log file integrity validation so tampering is detectable after the fact

### Q23 Answer: B

### Q23 Analysis

A is incorrect. Permission boundaries apply to individual IAM roles and only limit the maximum permissions of that role. They do not apply to all principals automatically and can be modified by an IAM administrator with the `iam:PutRolePermissionsBoundary` permission.

B is correct. SCPs apply to all principals (IAM users, roles, and the root user within member accounts) across all accounts in the OU or Organization. An SCP denying `cloudtrail:StopLogging` and `cloudtrail:DeleteTrail` cannot be overridden by any IAM policy within the member accounts — it is enforced at the organization boundary.

C is incorrect. AWS Config with auto-remediation can re-enable CloudTrail after it is disabled, but there is a detection and remediation lag window during which CloudTrail is not recording. Prevention via SCP is the correct control for this requirement.

D is incorrect. Log file integrity validation detects whether logs were tampered with after the fact — it does not prevent CloudTrail from being disabled in the first place.

---

## Question 24 — Domain 4: Design Cost-Optimized Architectures

A company runs a web application with consistent 24/7 traffic on 20 `m5.large` On-Demand EC2 instances. They also run nightly batch jobs using 50 `c5.xlarge` instances from 11 PM to 5 AM. Which combination of purchasing options minimizes total cost?

- A. All 70 instances: On-Demand
- B. 20 `m5.large`: 1-year Standard Reserved Instances; 50 `c5.xlarge`: Spot Instances
- C. 20 `m5.large`: 1-year Compute Savings Plan; 50 `c5.xlarge`: 1-year Compute Savings Plan
- D. All 70 instances: 3-year All Upfront Standard Reserved Instances

### Q24 Answer: B

### Q24 Analysis

A is incorrect. On-Demand for all instances pays full price for both steady-state and batch workloads — no discounts applied.

B is correct. The 20 `m5.large` instances run 24/7 with predictable usage — 1-year Standard RIs provide up to 40% discount on steady, known instance types. The 50 `c5.xlarge` batch instances run only 6 hours per night and are fault-tolerant batch workloads — Spot Instances provide up to 90% discount and are the correct choice when interruption risk is acceptable.

C is incorrect. Purchasing Savings Plan coverage for 50 instances that run only 25% of the day wastes commitment spend. A Savings Plan charges the committed $/hour regardless of whether the batch instances are running — you pay for the other 18 hours of unused commitment.

D is incorrect. 3-year All Upfront RIs for short-running batch instances guarantees payment for 24 hours per day even though they only run 6 hours. The upfront cost and idle commitment make this far more expensive than Spot for transient batch workloads.

---

## Question 25 — Domain 1: Design Resilient Architectures

An application writes to an SQS Standard queue. Occasionally, the same message is processed twice by the consumer Lambda function, causing duplicate database records. The team cannot change the Lambda function code. What is the MOST effective architectural change?

- A. Increase the SQS visibility timeout to be longer than the Lambda function's maximum execution time
- B. Switch from an SQS Standard queue to an SQS FIFO queue
- C. Enable SQS long polling on the queue
- D. Add a Dead-Letter Queue to capture messages that fail processing

### Q25 Answer: B

### Q25 Analysis

A is incorrect. Increasing the visibility timeout reduces the likelihood of a second consumer receiving a message while the first is still processing, but SQS Standard queues still guarantee at-least-once delivery — the same message may be delivered more than once. This is a mitigation, not a solution.

B is correct. SQS FIFO queues provide exactly-once processing within a 5-minute deduplication window. Each message has a deduplication ID, and FIFO queues reject duplicate messages sent within the window. Switching to FIFO eliminates duplicate deliveries at the queue level without requiring Lambda code changes.

C is incorrect. Long polling reduces the number of empty API responses by waiting up to 20 seconds for a message to arrive — it optimizes cost and latency but has no effect on duplicate message delivery.

D is incorrect. A DLQ captures messages that fail processing repeatedly — it handles failures, not duplicates. Adding a DLQ does not prevent the same message from being delivered to the consumer multiple times.

---

## Question 26 — Domain 2: Design High-Performing Architectures

A DynamoDB table has a partition key of `DeviceId` (10,000 unique devices) and a sort key of `Timestamp`. An IoT application writes sensor readings continuously. After deployment, some writes are throttled even though the table's total provisioned WCUs are not exhausted. What is the most likely cause?

- A. The table needs a GSI on `Timestamp` to distribute writes more evenly
- B. A subset of devices generates significantly more writes than others, creating hot partitions that exceed per-partition throughput limits
- C. The sort key `Timestamp` is causing partition collisions because many writes share the same timestamp value
- D. DynamoDB on-demand mode should be used instead of provisioned mode for IoT workloads

### Q26 Answer: B

### Q26 Analysis

A is incorrect. Adding a GSI on `Timestamp` creates a secondary index for querying by time — it does not change how writes are distributed to the base table partitions and would not resolve hot partition throttling.

B is correct. DynamoDB distributes data across partitions based on the partition key hash. Each partition has a maximum throughput limit. If a small number of `DeviceId` values generate the majority of writes, those partitions become hot and throttle even when the table's total WCU capacity is not exhausted. This is the classic hot partition problem.

C is incorrect. The sort key does not determine partition placement — only the partition key (hash) determines which partition an item lands on. Multiple items with different `DeviceId` values but the same `Timestamp` go to different partitions.

D is incorrect. Switching to on-demand mode scales per-partition limits as well, making it a valid mitigation — but the question asks for the cause of the throttling, not the fix.

---

## Question 27 — Domain 3: Secure Architectures

A company's application stores sensitive customer PII in RDS. The security team requires that database credentials are rotated every 30 days and that the application never stores credentials in environment variables or configuration files. Which combination of services meets both requirements?

- A. AWS Systems Manager Parameter Store (SecureString) + Lambda rotation function triggered by EventBridge
- B. AWS Secrets Manager with automatic rotation enabled + application retrieves credentials via Secrets Manager API at runtime
- C. AWS KMS Customer Managed Key with automatic annual rotation + RDS native IAM database authentication
- D. HashiCorp Vault deployed on EC2 + application retrieves credentials from the Vault API

### Q27 Answer: B

### Q27 Analysis

A is incorrect. Parameter Store SecureString can store credentials securely, but it does not have native built-in rotation — a custom Lambda and EventBridge schedule must be built and maintained. This meets the requirement but is more complex than the purpose-built Secrets Manager solution.

B is correct. AWS Secrets Manager has native RDS integration with built-in rotation Lambda functions that rotate the database password in both RDS and the secret automatically on the configured schedule (every 30 days). Applications call the Secrets Manager API at runtime to retrieve current credentials — no environment variables or config files needed.

C is incorrect. KMS key rotation rotates encryption key material, not database user passwords. RDS IAM authentication eliminates password credentials for supported engines, but the question specifies credential rotation as a requirement — indicating passwords are in use.

D is incorrect. HashiCorp Vault is a valid secrets management solution but requires deploying, patching, scaling, and operating the Vault cluster on EC2 — adding significant operational overhead compared to the AWS-native Secrets Manager.

---

## Question 28 — Domain 4: Design Cost-Optimized Architectures

A startup is designing a new REST API. Expected traffic is 10,000 requests per day during weekdays and near-zero on weekends. The API calls a Lambda function that executes in under 200ms. Which compute and API layer is most cost-optimized for this traffic pattern?

- A. EC2 `t3.micro` with a self-managed NGINX reverse proxy and Auto Scaling
- B. API Gateway HTTP API + AWS Lambda
- C. API Gateway REST API + EC2 with Application Load Balancer
- D. AWS Fargate container running a Node.js Express server + Application Load Balancer

### Q28 Answer: B

### Q28 Analysis

A is incorrect. An EC2 instance incurs hourly charges continuously, including during the weekend zero-traffic period. For 10,000 requests per day with near-zero weekend traffic, paying for idle EC2 capacity is wasteful compared to serverless invocation pricing.

B is correct. API Gateway HTTP API charges per request ($1.00 per million requests) and Lambda charges per invocation and duration with a generous free tier. At 10,000 requests per day on weekdays, total monthly cost is well under $1. During weekends with zero traffic, there is zero cost. This is the optimal serverless pricing model for intermittent traffic.

C is incorrect. REST API Gateway charges more per request than HTTP API, and EC2 plus ALB incurs continuous hourly charges regardless of traffic volume.

D is incorrect. Fargate containers have a minimum charge per task per second they are running. Even with zero traffic on weekends, if tasks remain running, charges accumulate. Fargate is appropriate for longer-running containerized workloads, not sub-200ms API handlers with intermittent traffic.

---

## Question 29 — Domain 1: Design Resilient Architectures

A financial application processes transactions using Step Functions. Each workflow involves five Lambda functions in sequence. If any function fails permanently (invalid data), the entire transaction must be rolled back. How should permanent rollback be implemented in Step Functions?

- A. Add a Retry block with MaxAttempts=0 to skip retries for permanent failures
- B. In the Catch block for permanent errors, transition to a dedicated rollback state that invokes compensating Lambda functions in reverse order
- C. Enable Step Functions Express Workflows — they support automatic transaction rollback natively
- D. Configure DynamoDB transactions within each Lambda function so DynamoDB handles the rollback automatically

### Q29 Answer: B

### Q29 Analysis

A is incorrect. MaxAttempts=0 in a Retry block prevents retries for that error type, but it does not implement rollback logic — after skipping retries, the workflow still needs a Catch block to route to compensating states.

B is correct. The Step Functions Saga orchestration pattern implements distributed transaction rollback by catching permanent failures and transitioning to compensating transactions — a sequence of states that reverse the effects of completed steps in reverse order. This is the idiomatic Step Functions approach for distributed transaction management.

C is incorrect. Step Functions Express Workflows are optimized for high-volume, short-duration workflows — they do not provide automatic transaction rollback. Both Standard and Express workflows require explicit Catch and compensation state design for rollback.

D is incorrect. DynamoDB transactions handle atomicity for operations within a single DynamoDB TransactWrite call, but they cannot roll back side effects that occurred in other AWS services (SNS notifications sent, SQS messages published, external API calls made) during earlier completed Lambda steps.

---

## Question 30 — Domain 2: Design High-Performing Architectures

A company's Aurora MySQL cluster serves a read-heavy analytics workload. The reader endpoint load-balances across 3 read replicas. Business analysts report that some queries return stale data — results that do not reflect writes made seconds earlier. What is the architectural explanation?

- A. Aurora read replicas use synchronous replication; stale reads are caused by network congestion between the writer and replicas
- B. Aurora uses asynchronous replication from the writer to read replicas; replicas may lag behind the writer by a small duration
- C. The Aurora reader endpoint always routes to the replica with the lowest CPU utilization, which may be the most lagged replica
- D. The analysts are connected to the Aurora cluster writer endpoint instead of the reader endpoint

### Q30 Answer: B

### Q30 Analysis

A is incorrect. Aurora read replica replication is asynchronous (typically sub-10ms lag under normal load), not synchronous. Synchronous replication is used for Multi-AZ standby in standard RDS — Aurora's shared storage architecture means replicas replay log records asynchronously.

B is correct. Aurora read replicas receive log records from the writer asynchronously. Under normal conditions, replica lag is very low (sub-10ms), but it is never zero. Applications that write and immediately read within milliseconds may observe stale data on the reader endpoint. The solution for read-your-writes consistency is to direct those specific queries to the writer endpoint.

C is incorrect. The Aurora reader endpoint uses a round-robin load balancing algorithm across available read replicas — it does not route based on CPU utilization or replica lag.

D is incorrect. If analysts were connected to the writer endpoint, they would see the most current data — not stale data. Stale reads are characteristic of read replica lag on the reader endpoint, not of using the writer.

# Quiz: Module 01 - AWS Global Infrastructure and Core Services Overview

**Course:** CIS-4334 AWS Cloud Architecture
**Certification Target:** AWS Solutions Architect Associate (SAA-C03)
**Total Questions:** 10

---

## Question 1

Which AWS infrastructure component consists of one or more discrete data centers with redundant power, networking, and connectivity, designed so that failures in one component are isolated from others?

- A) AWS Region
- B) Edge Location
- C) Availability Zone
- D) Local Zone

### Answer 1

Correct Answer: C

### Explanation 1

- A is incorrect: A Region is the broader geographic container that holds multiple AZs; it is not itself a discrete data center cluster.
- B is incorrect: Edge Locations are Points of Presence used by CloudFront and Route 53 for content caching and DNS, not general-purpose compute infrastructure.
- C is correct: An Availability Zone is the physical fault-isolation unit within a Region. Each AZ has independent power, cooling, and networking, connected by high-bandwidth, low-latency fiber.
- D is incorrect: A Local Zone extends AWS infrastructure to a metropolitan area for ultra-low latency but is not the standard high-availability unit described in the question.

---

## Question 2

Which of the following is the most accurate definition of an AWS Availability Zone in the context of cloud architecture?

- A) A global content delivery network node that caches static assets closer to end users to reduce latency
- B) One or more physically separated, redundant data centers within a Region, connected by high-bandwidth fiber, designed to isolate faults and enable high-availability deployments
- C) A logical grouping of AWS accounts used to apply organizational policies and service control policies across an enterprise
- D) A dedicated physical server allocated to a single AWS customer to meet licensing or compliance requirements

### Answer 2

Correct Answer: B

### Explanation 2

- A is incorrect: This describes an Edge Location (CloudFront PoP), not an AZ.
- B is correct: This is the precise AWS definition of an AZ — the primary unit of physical fault isolation used for high-availability design on SAA-C03.
- C is incorrect: This describes AWS Organizations and organizational units, not infrastructure geography.
- D is incorrect: This describes a Dedicated Host, which is a billing and licensing construct, not an infrastructure topology concept.

---

## Question 3

A solutions architect needs to design a web application that remains available if a single AWS data center loses power. Which deployment strategy directly addresses this requirement?

- A) Deploy all EC2 instances in a single Availability Zone and enable detailed CloudWatch monitoring
- B) Deploy EC2 instances across at least two Availability Zones in the same Region behind an Application Load Balancer
- C) Store all application data in S3 Standard storage class and enable versioning on the bucket
- D) Purchase Reserved Instances to reduce cost and guarantee capacity in one AZ

### Answer 3

Correct Answer: B

### Explanation 3

- A is incorrect: A single AZ is a single fault domain — losing that data center takes down the entire application regardless of monitoring granularity.
- B is correct: Multi-AZ deployment with an ALB distributes traffic and automatically routes away from an unhealthy AZ, directly satisfying the single-data-center failure requirement.
- C is incorrect: S3 versioning protects against accidental deletion of objects but does nothing to keep a web application available during a data center outage.
- D is incorrect: Reserved Instances are a cost-optimization commitment, not an availability mechanism.

---

## Question 4

Under the AWS Shared Responsibility Model, which of the following is the customer's responsibility when running an application on Amazon EC2?

- A) Maintaining the physical security of the data center where the EC2 host server resides
- B) Patching and updating the hypervisor software running beneath the EC2 instance
- C) Patching the guest operating system and managing security group rules for the instance
- D) Replacing failed hardware components in the underlying EC2 host server

### Answer 4

Correct Answer: C

### Explanation 4

- A is incorrect: Physical data center security is AWS's responsibility — customers never have physical access to AWS facilities.
- B is incorrect: AWS owns and patches the hypervisor. Customers have no access to or responsibility for the virtualization layer.
- C is correct: The guest OS, application code, IAM configuration, firewall rules (security groups), and data encryption are all customer responsibilities under the Shared Responsibility Model.
- D is incorrect: Hardware maintenance and replacement is AWS's responsibility as part of their security-of-the-cloud obligation.

---

## Question 5

When designing a globally distributed application, a solutions architect wants to minimize the risk of a full Region outage taking down all user-facing traffic. Which of the following is the best architectural control to implement?

- A) Deploy the application in a single Region with EC2 instances spread across all available AZs
- B) Enable automatic snapshots on all EBS volumes and store copies in the same Region
- C) Deploy the application in multiple AWS Regions and use Route 53 with failover or latency-based routing to direct traffic
- D) Enable AWS Shield Standard on the application to protect against regional infrastructure failures

### Answer 5

Correct Answer: C

### Explanation 5

- A is incorrect: Multi-AZ within a single Region protects against individual AZ failures, not a full Region outage.
- B is incorrect: EBS snapshots protect data durability but do not keep the application running during a Region outage — there is no compute to serve traffic.
- C is correct: Multi-Region deployments with Route 53 routing is the canonical SAA-C03 pattern for regional fault tolerance and global disaster recovery.
- D is incorrect: AWS Shield Standard protects against DDoS attacks, not infrastructure or Region-level outages.

---

## Question 6

A company has a regulatory requirement that all customer data must remain within the European Union. Which factor should drive the AWS Region selection decision above all others?

- A) Choosing the Region with the lowest per-GB storage cost
- B) Choosing the Region closest to the company's development team's office
- C) Choosing a Region located within the EU to satisfy data residency requirements
- D) Choosing the Region with the largest number of available Availability Zones

### Answer 6

Correct Answer: C

### Explanation 6

- A is incorrect: Cost optimization is a valid consideration but is subordinate to compliance requirements. Choosing a non-EU Region to save money would violate the regulatory mandate.
- B is incorrect: Proximity to the development team is irrelevant for data residency compliance. The Region must match where data is legally permitted to reside.
- C is correct: Compliance and data residency requirements always take priority over other Region selection factors. EU Regions such as eu-west-1 (Ireland) and eu-central-1 (Frankfurt) satisfy EU data residency requirements.
- D is incorrect: The number of AZs in a Region is a resilience consideration, not a compliance factor.

---

## Question 7

Which AWS infrastructure option should a solutions architect recommend when a mobile gaming company needs to deliver compute-intensive game logic to 5G smartphone users with sub-10-millisecond latency?

- A) Deploy EC2 instances in the nearest AWS Region to the user base
- B) Use AWS Local Zones to extend compute to metro areas near the users
- C) Use AWS Wavelength Zones embedded in the 5G carrier network
- D) Deploy EC2 instances at AWS Edge Locations using CloudFront Functions

### Answer 7

Correct Answer: C

### Explanation 7

- A is incorrect: A standard Region deployment will have 20-80 ms latency to mobile users due to internet routing hops, which does not meet the sub-10 ms requirement.
- B is incorrect: Local Zones provide single-digit millisecond latency to metro areas but are not embedded in 5G carrier infrastructure. The 5G context points specifically to Wavelength Zones.
- C is correct: AWS Wavelength Zones are co-located inside 5G carrier networks, eliminating the backhaul from the device to an AWS Region and achieving sub-10 ms latency for 5G applications.
- D is incorrect: CloudFront Functions run at Edge Locations but are limited to lightweight HTTP request/response manipulation, not compute-intensive game server logic.

---

## Question 8

A solutions architect is reviewing an architecture where an Amazon RDS for MySQL instance is deployed with Multi-AZ enabled. Under the AWS Shared Responsibility Model, which task is the customer responsible for?

- A) Patching the MySQL database engine to the latest version
- B) Replacing the underlying storage hardware if it fails
- C) Configuring IAM database authentication and managing the IAM policies that control access
- D) Replicating data synchronously to the standby instance in the secondary AZ

### Answer 8

Correct Answer: C

### Explanation 8

- A is incorrect: For Amazon RDS, AWS manages database engine patching. This is a key benefit of using a managed database service versus running MySQL on EC2.
- B is incorrect: Hardware replacement is always AWS's responsibility. Customers never interact with physical hardware in any AWS service.
- C is correct: IAM database authentication configuration and IAM policy management are customer responsibilities regardless of the managed service level.
- D is incorrect: Synchronous replication to the Multi-AZ standby is an AWS-managed feature of RDS Multi-AZ. The customer enables the option, but AWS performs the actual replication.

---

## Question 9

An AWS account has resources in us-east-1a and a business partner's AWS account also has resources in us-east-1a. A solutions architect discovers that the two accounts' us-east-1a resources are on physically different hardware. What is the most likely cause?

- A) The two accounts are in different AWS partitions and cannot share AZ resources
- B) AZ names are randomized per account; the accounts' us-east-1a maps to different physical AZs, and AZ IDs should be used for cross-account coordination
- C) us-east-1a is an opt-in AZ that must be enabled separately in each account
- D) Resources in different accounts are always isolated by separate VPCs and cannot use AZ-local routing

### Answer 9

Correct Answer: B

### Explanation 9

- A is incorrect: AWS partitions (aws, aws-cn, aws-us-gov) describe separate cloud environments, not AZ name mapping within the same partition.
- B is correct: AWS deliberately randomizes AZ name-to-physical-AZ mappings per account to distribute load. AZ IDs such as use1-az1 are consistent across accounts and must be used for cross-account coordination.
- C is incorrect: AZ availability is tied to the Region opt-in status, not individual AZ opt-in.
- D is incorrect: VPC isolation is a network boundary issue, not an AZ physical assignment issue.

---

## Question 10

An architect is evaluating whether AWS Outposts is appropriate for a client requirement. Which scenario best justifies deploying AWS Outposts rather than using a standard AWS Region?

- A) The client wants to reduce the cost of running EC2 workloads by using their own hardware
- B) The client needs to process data locally in their factory with single-digit millisecond latency to on-premises equipment, and data cannot leave the facility
- C) The client wants to deploy a web application serving users in a city that does not have an AWS Region
- D) The client needs to run machine learning training jobs that require more GPU capacity than a single Region can provide

### Answer 10

Correct Answer: B

### Explanation 10

- A is incorrect: AWS Outposts is more expensive than standard Region deployments because it involves dedicated hardware shipped to and managed at the customer's facility. Cost reduction is not a valid Outposts use case.
- B is correct: AWS Outposts is designed for scenarios requiring AWS-native APIs with physical on-premises presence — low latency to local equipment and strict data locality requirements that prohibit sending data to a Region.
- C is incorrect: This scenario describes the use case for AWS Local Zones, not Outposts. Outposts requires the customer to host the hardware at their own facility.
- D is incorrect: High GPU demand is addressed by selecting EC2 GPU instance families (P4d, G5) in a standard Region. Outposts does not solve compute capacity constraints.

---

## Question 11

A solutions architect is designing an architecture that must tolerate the simultaneous failure of two Availability Zones in the same AWS Region. What is the minimum number of Availability Zones required for the deployment to remain fully operational at normal capacity?

- A) 2
- B) 3
- C) 4
- D) 6

### Answer 11

Correct Answer: C

### Explanation 11

- A is incorrect: With only 2 AZs, a simultaneous dual-AZ failure would leave zero AZs operational.
- B is incorrect: With 3 AZs, losing 2 leaves only 1 AZ running. The application survives on reduced capacity rather than remaining fully operational under N+2 design.
- C is correct: To tolerate the simultaneous failure of any 2 AZs and remain fully operational at 100% capacity, you need N+2 AZs. Deploying across 4 AZs means losing 2 still leaves 2 AZs, which can carry the full load if each AZ is sized for 50% of total traffic. This is the N+2 high-availability design pattern.
- D is incorrect: 6 AZs satisfies the requirement but is excessive. Most AWS Regions do not offer 6 AZs, and 4 is the correct minimum for N+2 tolerance.

---

## Question 12

Which AWS service provides a globally distributed managed DNS service that can route users to the lowest-latency endpoint and automatically remove unhealthy endpoints from DNS responses?

- A) AWS Global Accelerator
- B) Amazon CloudFront
- C) Amazon Route 53
- D) AWS Transit Gateway

### Answer 12

Correct Answer: C

### Explanation 12

- A is incorrect: AWS Global Accelerator is a networking service that routes traffic over the AWS global backbone to the nearest healthy endpoint using static Anycast IP addresses. It is not a DNS service and does not perform DNS-based routing.
- B is incorrect: Amazon CloudFront is a content delivery network that caches content at edge locations. It does not perform general-purpose DNS resolution or health-check-based DNS failover for arbitrary application endpoints.
- C is correct: Amazon Route 53 is AWS's managed DNS service. It supports latency-based routing (directing users to the lowest-latency Region), health checks that monitor endpoint availability, and failover routing policies that automatically remove unhealthy endpoints from DNS responses.
- D is incorrect: AWS Transit Gateway connects VPCs and on-premises networks in a hub-and-spoke topology. It is a network routing service, not a DNS service.

---

## Question 13

A company needs to run a batch video processing job that can be interrupted and resumed from a checkpoint. The job takes approximately 8 hours to complete and runs weekly. The company wants to minimize EC2 costs. Which EC2 purchasing model is most appropriate?

- A) On-Demand Instances
- B) Reserved Instances with a 1-year commitment
- C) Spot Instances
- D) Dedicated Hosts

### Answer 13

Correct Answer: C

### Explanation 13

- A is incorrect: On-Demand pricing is the most expensive per-hour option and provides no discount for workloads that can tolerate interruption.
- B is incorrect: Reserved Instances are most cost-effective for steady-state continuously running workloads with predictable usage patterns. A weekly 8-hour batch job has very low utilization over a year, making an RI commitment economically unfavorable.
- C is correct: Spot Instances offer up to 90% discount versus On-Demand. Batch processing workloads that can checkpoint progress and resume after interruption are the canonical Spot Instance use case. The combination of interrupt-tolerance and large compute requirements makes Spot Instances the optimal choice.
- D is incorrect: Dedicated Hosts are designed for per-socket or per-core software licensing compliance. They are the most expensive EC2 option and provide no technical or cost benefit for a batch processing workload.

---

## Question 14

Which pillar of the AWS Well-Architected Framework focuses on the ability of a workload to perform its intended function correctly and consistently, including the ability to recover automatically from infrastructure failures?

- A) Cost Optimization
- B) Security
- C) Performance Efficiency
- D) Reliability

### Answer 14

Correct Answer: D

### Explanation 14

- A is incorrect: The Cost Optimization pillar focuses on running systems at the lowest price point while delivering the required business value, including right-sizing, eliminating waste, and using the right pricing model.
- B is incorrect: The Security pillar focuses on protecting information and systems through identity management, detection controls, infrastructure protection, data protection, and incident response.
- C is incorrect: The Performance Efficiency pillar focuses on using computing resources efficiently to meet system requirements and maintaining that efficiency as demand changes and technology evolves.
- D is correct: The Reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently throughout its lifecycle, recover from failures automatically, and dynamically acquire resources to meet demand. This directly maps to concepts like Multi-AZ, Auto Scaling, and disaster recovery patterns.

---

## Question 15

A new AWS account was created 13 months ago. A developer attempts to use the AWS Free Tier for launching an EC2 t2.micro instance and is surprised to see charges on the bill. What is the most likely explanation?

- A) The Free Tier requires a paid support plan to remain active
- B) The 12-month free tier offer for EC2 t2.micro hours expired after the first 12 months and standard On-Demand rates now apply
- C) The Free Tier was automatically converted to a Reserved Instance after 12 months
- D) EC2 t2.micro is not eligible for the AWS Free Tier in any Region

### Answer 15

Correct Answer: B

### Explanation 15

- A is incorrect: The AWS Free Tier is available to all new accounts regardless of support plan. No support plan purchase is required to activate or maintain free-tier eligibility.
- B is correct: The 12-month free tier for EC2 (750 hours/month of t2.micro or t3.micro) is available only during the first 12 months after account creation. After 12 months, standard On-Demand pricing applies to all usage. Always-free tiers for services like Lambda and DynamoDB do not expire, but the 12-month EC2 offer does.
- C is incorrect: The Free Tier does not automatically convert to Reserved Instances. Reserved Instances require an explicit purchase commitment and payment.
- D is incorrect: EC2 t2.micro (or t3.micro in regions where t2.micro is not available) is specifically included in the AWS Free Tier for new accounts.

---

## Question 16

A company with 15 AWS accounts wants centralized policy enforcement, consolidated billing, and the ability to restrict all accounts from launching EC2 instances outside the us-east-1 and us-west-2 Regions. Which combination of AWS services achieves all three goals?

- A) AWS Config with a remediation rule and AWS Cost Explorer for billing
- B) AWS Organizations with a Service Control Policy and consolidated billing enabled
- C) AWS IAM with permission boundaries applied to every role in every account
- D) AWS CloudFormation StackSets to deploy SCPs to every account

### Answer 16

Correct Answer: B

### Explanation 16

- A is incorrect: AWS Config can detect non-compliant resources but remediation is reactive rather than preventive. Config does not provide consolidated billing, and Cost Explorer is a cost visibility tool, not a billing consolidator.
- B is correct: AWS Organizations provides: (1) consolidated billing — all 15 accounts roll up to one payment; (2) organizational units where SCPs can be applied; and (3) SCPs that restrict what actions are allowed in member accounts, including denying EC2 launch actions where `aws:RequestedRegion` is not us-east-1 or us-west-2. This SCP is applied at the OU or root level and affects all member accounts.
- C is incorrect: IAM permission boundaries restrict individual IAM entities within a single account. Applying permission boundaries to every role in every account requires per-account, per-role management and provides no consolidated billing.
- D is incorrect: CloudFormation StackSets can deploy resources (including IAM policies) across accounts, but SCPs are applied within AWS Organizations, not deployed as CloudFormation resources. StackSets also do not provide consolidated billing.

---

## Question 17

Which of the following correctly describes how data transfer pricing works between two EC2 instances communicating using private IP addresses within the same VPC but in different Availability Zones?

- A) Data transfer is free because both instances are within the same VPC
- B) Data transfer incurs a per-GB charge in each direction because the traffic crosses AZ boundaries
- C) Data transfer is free because private IP communication never leaves the AWS network backbone
- D) Data transfer incurs charges only for traffic exceeding 1 TB per month

### Answer 17

Correct Answer: B

### Explanation 17

- A is incorrect: Same-VPC does not mean free cross-AZ data transfer. Data transfer charges apply per AZ boundary crossed, regardless of whether the same VPC is used.
- B is correct: EC2 data transfer between instances in different AZs within the same Region using private IP addresses incurs a charge of $0.01 per GB in each direction. This is a commonly misunderstood cost that can become significant for high-throughput inter-AZ applications. The charge applies even when using private IPs and even within the same VPC.
- C is incorrect: While private IP traffic stays on the AWS network and does not traverse the public internet, AWS still charges for cross-AZ data transfer. Staying on the AWS network is not the same as being free.
- D is incorrect: There is no free tier threshold of 1 TB for cross-AZ EC2 data transfer. Cross-AZ charges apply from the first byte transferred.

---

## Question 18

An architect wants to evaluate a new workload design against AWS best practices before development begins. The tool should generate a risk assessment report highlighting high-risk and medium-risk areas across all six Well-Architected Framework pillars. Which AWS tool provides this capability?

- A) AWS Trusted Advisor
- B) AWS Well-Architected Tool
- C) AWS Security Hub
- D) AWS Compute Optimizer

### Answer 18

Correct Answer: B

### Explanation 18

- A is incorrect: AWS Trusted Advisor analyzes deployed resources in an existing AWS account and provides recommendations across five categories. It reviews what has been built and deployed, not a planned workload described through a questionnaire.
- B is correct: The AWS Well-Architected Tool allows architects to define a workload, answer questions across all six pillars (Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability), and receive a risk report identifying high-risk issues (HRIs) and medium-risk issues before or after building. It is purpose-built for architecture review.
- C is incorrect: AWS Security Hub aggregates security findings from GuardDuty, Inspector, Macie, and other services for deployed resources. It is a security posture management tool, not an architectural review tool.
- D is incorrect: AWS Compute Optimizer analyzes the utilization metrics of existing EC2 instances, Auto Scaling groups, EBS volumes, and Lambda functions and recommends optimal resource configurations. It operates on deployed resources, not planned architectures.

---

## Question 19

A developer notices that creating an IAM policy change in the AWS Management Console immediately affects all AWS Regions without any manual replication. What explains this behavior?

- A) IAM replicates policy changes to all Regions within 60 seconds using an internal synchronization service
- B) IAM is a global service; changes are immediately available across all Regions because IAM is not scoped to any Region
- C) The AWS Management Console caches IAM data globally and applies changes to all Region views simultaneously
- D) IAM policies are stored in Amazon S3 with Cross-Region Replication enabled, distributing changes automatically

### Answer 19

Correct Answer: B

### Explanation 19

- A is incorrect: IAM does not replicate across Regions because it is not a regional service. There is no IAM replication process — IAM is globally scoped by design with no regional partitions.
- B is correct: IAM is a global AWS service. IAM users, groups, roles, and policies have global scope and are not tied to any specific Region. A policy change is immediately available in every Region because all Regions reference the same global IAM data plane — there is no per-Region copy to synchronize.
- C is incorrect: The Console's behavior reflects IAM's global architecture, not browser caching. The changes are truly global at the service level, not simulated globally by the front-end.
- D is incorrect: IAM does not store policies in customer-managed S3 buckets, and IAM does not use S3 CRR for distribution. IAM data persistence is internal to the AWS service layer.

---

## Question 20

A company currently uses a single AWS account shared by all development, testing, staging, and production workloads. A security architect recommends separating each environment into its own dedicated AWS account. Which security benefit most strongly justifies this recommendation?

- A) Separate accounts allow the company to use different instance types in each environment
- B) Separate accounts provide blast radius containment — a security event, IAM misconfiguration, or accidental resource deletion in one environment cannot directly affect another account's resources
- C) Separate accounts improve EC2 performance because compute resources are distributed across independent hardware pools per account
- D) Separate accounts eliminate the need for IAM policies because account boundaries inherently restrict all access

### Answer 20

Correct Answer: B

### Explanation 20

- A is incorrect: All EC2 instance types are available in any AWS account. Account separation does not change the availability of instance types.
- B is correct: The strongest security justification for environment account separation is blast radius containment. An IAM role compromised in the development account has no access to production resources in a separate account. An accidental `terraform destroy` in staging cannot destroy production resources. Account boundaries are the strongest isolation boundary in AWS, stronger than any IAM policy or VPC boundary within a single account.
- C is incorrect: Account separation has no effect on EC2 hardware assignment or performance. EC2 instance performance is determined by instance type, placement groups, and the underlying physical host — not the account.
- D is incorrect: IAM policies remain fully required within each account. Account boundaries prevent cross-account access by default, but all actions within an account still require appropriate IAM permissions. Account separation complements, not replaces, IAM.

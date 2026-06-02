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

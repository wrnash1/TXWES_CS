# Quiz: Module 01 - AWS Global Infrastructure and Core Services Overview
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which AWS infrastructure component consists of one or more discrete data centers with redundant power, networking, and connectivity, designed so that failures in one component are isolated from others?
*   A) AWS Region
*   B) Edge Location
*   C) Availability Zone
*   D) Local Zone
*   **Correct Answer:** C) An Availability Zone (AZ) is one or more discrete data centers within a Region, each with redundant infrastructure and physically separated from other AZs to isolate failures.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A Region is the broader geographic container that holds multiple AZs; it is not itself a discrete data center cluster.
    *   *Why B is incorrect:* Edge Locations are Points of Presence used by CloudFront and Route 53 for content caching and DNS, not general-purpose compute infrastructure.
    *   *Why C is correct:* An Availability Zone is the physical fault-isolation unit within a Region. Each AZ has independent power, cooling, and networking, and AZs are connected to each other by high-bandwidth, low-latency fiber.
    *   *Why D is incorrect:* A Local Zone is an AWS infrastructure extension to a metropolitan area for ultra-low latency, but it is not the standard HA unit described in the question.

---

**Question 2**
Which of the following is the most accurate definition of an **AWS Availability Zone (AZ)** in the context of cloud architecture?
*   A) A global content delivery network node that caches static assets closer to end users to reduce latency.
*   B) One or more physically separated, redundant data centers within a Region, connected by high-bandwidth fiber, designed to isolate faults and enable high-availability deployments.
*   C) A logical grouping of AWS accounts used to apply organizational policies and service control policies across an enterprise.
*   D) A dedicated physical server allocated to a single AWS customer to meet licensing or compliance requirements.
*   **Correct Answer:** B) An Availability Zone is one or more physically separated, redundant data centers within a Region connected by high-bandwidth fiber, designed to isolate faults and enable high-availability deployments.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes an Edge Location (CloudFront PoP), not an AZ.
    *   *Why B is correct:* This is the precise AWS definition of an AZ — the primary unit of physical fault isolation used for HA design on SAA-C03.
    *   *Why C is incorrect:* This describes AWS Organizations and organizational units (OUs), not infrastructure geography.
    *   *Why D is incorrect:* This describes a Dedicated Host, which is a billing/licensing construct, not an infrastructure topology concept.

---

**Question 3**
A solutions architect needs to design a web application that remains available if a single AWS data center loses power. Which deployment strategy directly addresses this requirement?
*   A) Deploy all EC2 instances in a single Availability Zone and enable detailed CloudWatch monitoring.
*   B) Deploy EC2 instances across at least two Availability Zones in the same Region behind an Application Load Balancer.
*   C) Store all application data in S3 Standard storage class and enable versioning on the bucket.
*   D) Purchase Reserved Instances to reduce cost and guarantee capacity in one AZ.
*   **Correct Answer:** B) Deploy EC2 instances across at least two Availability Zones in the same Region behind an Application Load Balancer.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A single AZ is a single fault domain — losing that data center takes down the entire application regardless of monitoring.
    *   *Why B is correct:* Multi-AZ deployment with an ALB distributes traffic and automatically routes away from an unhealthy AZ, directly satisfying the availability requirement.
    *   *Why C is incorrect:* S3 versioning protects against accidental deletion of objects but does nothing to keep a web application available during a data center outage.
    *   *Why D is incorrect:* Reserved Instances are a cost-optimization commitment, not an availability mechanism.

---

**Question 4**
Under the AWS Shared Responsibility Model, which of the following is the customer's responsibility when running an application on Amazon EC2?
*   A) Maintaining the physical security of the data center where the EC2 host server resides.
*   B) Patching and updating the hypervisor software running beneath the EC2 instance.
*   C) Patching the guest operating system and managing security group rules for the instance.
*   D) Replacing failed hardware components in the underlying EC2 host server.
*   **Correct Answer:** C) Patching the guest operating system and managing security group rules for the instance.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Physical data center security is AWS's responsibility — customers never have physical access to AWS facilities.
    *   *Why B is incorrect:* AWS owns and patches the hypervisor. Customers have no access to or responsibility for the virtualization layer.
    *   *Why C is correct:* The guest OS, application code, IAM configuration, firewall rules (security groups), and data encryption are all customer responsibilities under the Shared Responsibility Model.
    *   *Why D is incorrect:* Hardware maintenance and replacement is AWS's responsibility as part of their "security of the cloud" obligation.

---

**Question 5**
When designing a globally distributed application, a solutions architect wants to minimize the risk of a **full Region outage taking down all user-facing traffic**. Which of the following is the best architectural control to implement?
*   A) Deploy the application in a single Region with EC2 instances spread across all available AZs.
*   B) Enable automatic snapshots on all EBS volumes and store copies in the same Region.
*   C) Deploy the application in multiple AWS Regions and use Route 53 with failover or latency-based routing to direct traffic.
*   D) Enable AWS Shield Standard on the application to protect against regional infrastructure failures.
*   **Correct Answer:** C) Deploy the application in multiple AWS Regions and use Route 53 with failover or latency-based routing to direct traffic.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Multi-AZ within a single Region protects against individual AZ failures, not a full Region outage. All AZs in a Region share the same regional control plane dependencies.
    *   *Why B is incorrect:* EBS snapshots protect data durability but do not keep the application running during a Region outage — there is no compute to serve traffic.
    *   *Why C is correct:* Multi-Region deployments with Route 53 routing is the canonical SAA-C03 pattern for regional fault tolerance and global disaster recovery. Route 53 health checks detect a regional failure and reroute traffic to the secondary Region.
    *   *Why D is incorrect:* AWS Shield Standard protects against DDoS attacks, not infrastructure or Region-level outages.


# Quiz: Module 14 — AWS Cost Optimization

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Answer key and distractor analysis follow each question.

---

## Question 1

A company runs a web application on EC2 with steady, predictable traffic 24 hours a day, 7 days a week, for the foreseeable future. The finance team wants to reduce the EC2 cost by the maximum possible amount without changing the application architecture. Which purchasing option provides the greatest discount?

- A. Spot Instances with a persistent request
- B. On-Demand Instances with detailed monitoring disabled
- C. All Upfront, 3-year Standard Reserved Instances
- D. Compute Savings Plan with 1-year no-upfront commitment

### Q1 Answer: C

### Q1 Analysis

A is incorrect. Spot Instances can be interrupted with a 2-minute warning. A 24/7 web application cannot tolerate arbitrary interruptions. Additionally, a steady-state always-on workload is not the target use case for Spot.

B is incorrect. Disabling detailed monitoring reduces CloudWatch metric frequency but has no effect on EC2 instance pricing.

C is correct. All Upfront 3-year Standard Reserved Instances provide up to 72% discount — the maximum available for EC2. The workload is steady and predictable, making the 3-year commitment low risk.

D is incorrect. A 1-year Compute Savings Plan provides up to 66% discount, which is less than the 72% available from a 3-year Standard RI or EC2 Instance Savings Plan. The question asks for the maximum discount.

---

## Question 2

A data science team runs weekly batch ML training jobs that take 6–8 hours to complete. Jobs can be restarted from a checkpoint if interrupted. The team wants to minimize compute costs. Which EC2 purchasing model is MOST appropriate?

- A. Reserved Instances (1-year, All Upfront)
- B. On-Demand Instances
- C. Spot Instances
- D. Dedicated Hosts

### Q2 Answer: C

### Q2 Analysis

A is incorrect. Reserved Instances provide a discount on steady-state, continuous usage. Weekly 6–8 hour batch jobs represent sporadic usage — the RI capacity would sit idle most of the time, wasting the committed cost.

B is incorrect. On-Demand provides no discount. For this workload, Spot delivers up to 90% savings.

C is correct. Spot Instances are ideal for batch ML training jobs. The workload is fault-tolerant (restarts from checkpoint), runs periodically (not continuously), and can tolerate interruption. Spot delivers up to 90% discount.

D is incorrect. Dedicated Hosts are required for per-socket/per-core software licensing. This workload has no such licensing requirement. Dedicated Hosts are the most expensive option.

---

## Question 3

A company stores large volumes of log files in S3. Logs are queried intensively for the first 30 days after creation (daily analysis), then accessed approximately once per month for 6 months, then rarely accessed for the remaining retention period of 7 years. Which S3 configuration MOST cost-effectively serves this access pattern?

- A. S3 Standard for all objects throughout the 7-year retention period
- B. S3 Intelligent-Tiering applied to the entire bucket
- C. S3 Lifecycle policy: Standard → Standard-IA at 30 days → Glacier Flexible Retrieval at 180 days → expire at 7 years
- D. S3 One Zone-IA for all objects after initial creation

### Q3 Answer: C

### Q3 Analysis

A is incorrect. S3 Standard is the most expensive per-GB storage class. Keeping logs in Standard for 7 years when they are rarely accessed after 6 months is significantly over-cost.

B is incorrect. Intelligent-Tiering is appropriate when the access pattern is unknown. This scenario has a clearly defined access pattern — Intelligent-Tiering adds a per-object monitoring fee without providing additional cost savings over a lifecycle policy with known transitions.

C is correct. The access pattern perfectly maps to lifecycle transitions: Standard for the first 30 days (daily access), Standard-IA for months 1–6 (monthly access), Glacier Flexible Retrieval for years 1–7 (rare access). Each class is matched to the actual access frequency.

D is incorrect. S3 One Zone-IA stores data in a single AZ, eliminating Multi-AZ resilience. Log files are important audit data — losing them due to a single-AZ outage is unacceptable. Also, One Zone-IA does not cover the full access pattern progression.

---

## Question 4

An organization's AWS bill has increased 40% over the past quarter, but the number of deployed resources has increased only 10%. The finance team suspects untagged resources are driving unattributed costs. Which AWS tool provides the MOST granular view of spending broken down by team and project?

- A. AWS Trusted Advisor Cost Optimization checks
- B. AWS Cost Explorer grouped by cost allocation tags
- C. AWS Config configuration history for billing resources
- D. CloudWatch billing metric grouped by service

### Q4 Answer: B

### Q4 Analysis

A is incorrect. Trusted Advisor provides recommendations for specific optimization patterns (underutilized instances, unused Elastic IPs) but does not provide tag-based cost attribution.

B is correct. Cost Explorer can group spending by any activated cost allocation tag. Tags like `Team` and `Project` provide per-team, per-project breakdowns when resources are consistently tagged and tags are activated in the Billing console.

C is incorrect. AWS Config records resource configuration history and compliance, not billing data. It does not provide cost attribution.

D is incorrect. CloudWatch billing metrics provide total account spend by service but cannot break costs down by resource tag.

---

## Question 5

A company has purchased Compute Savings Plans covering 60% of their EC2 usage. The remaining 40% is covered by On-Demand pricing. A solutions architect recommends purchasing additional coverage to reach 80%. Which type of Savings Plan provides the MOST flexibility across EC2 instance families, regions, and also covers AWS Lambda and Fargate?

- A. EC2 Instance Savings Plan
- B. Standard Reserved Instance
- C. Compute Savings Plan
- D. Convertible Reserved Instance

### Q5 Answer: C

### Q5 Analysis

A is incorrect. EC2 Instance Savings Plans apply to a specific instance family in a specific region. They do not cover Lambda or Fargate usage.

B is incorrect. Standard Reserved Instances apply to a specific instance family, OS, and region. They do not cover Lambda or Fargate.

C is correct. Compute Savings Plans apply to any EC2 instance family, region, OS, and tenancy, and also cover Lambda and Fargate usage automatically. They provide the broadest coverage at up to 66% discount.

D is incorrect. Convertible RIs allow exchange for a different family, OS, or region, but they still do not cover Lambda or Fargate. They also require manual exchange requests, unlike Savings Plans which apply automatically.

---

## Question 6

A company's software requires a Windows Server license tied to physical CPU sockets for a legacy compliance scanning tool. The tool must run on AWS. Which EC2 purchasing model is REQUIRED for this licensing model?

- A. On-Demand Windows Instances
- B. Dedicated Instances
- C. Dedicated Hosts
- D. Spot Instances with Windows AMI

### Q6 Answer: C

### Q6 Analysis

A is incorrect. On-Demand instances run on shared physical hardware. Per-socket Windows Server licensing requires knowing which physical sockets are in use, which is not possible on shared hardware.

B is incorrect. Dedicated Instances run on hardware dedicated to your account but you do not control or see the underlying physical host. Per-socket licensing typically requires visibility into the specific physical hardware.

C is correct. Dedicated Hosts provide a physical server dedicated to your use with full visibility into the number of physical sockets and cores. This is required for Bring Your Own License (BYOL) software with per-socket or per-core licensing models.

D is incorrect. Spot Instances run on shared physical hardware and can be interrupted. Neither characteristic is compatible with per-socket licensing requirements.

---

## Question 7

AWS Compute Optimizer has flagged an EC2 instance as over-provisioned with a recommendation to downsize from m5.2xlarge to m5.xlarge. The instance currently runs a web application. Before applying the recommendation, a solutions architect should verify which THREE factors? (Select THREE.)

- A. The m5.xlarge has sufficient memory for peak application load
- B. The current instance's Reserved Instance term has expired
- C. Peak CPU utilization does not exceed the m5.xlarge's capacity during high-traffic periods
- D. The application can handle the 5-minute downtime required for instance type change
- E. Network throughput requirements are within the m5.xlarge's network bandwidth limit

### Q7 Answer: A, C, and E

### Q7 Analysis

A is correct. Compute Optimizer uses memory metrics from the CloudWatch Agent if available. If the Agent is not installed, memory data may be missing from the analysis. Verify peak memory usage fits within the smaller instance's capacity.

B is incorrect. Whether an RI term has expired is a billing consideration but does not affect whether the smaller instance will perform adequately. The technical suitability verification should come first.

C is correct. Compute Optimizer bases recommendations on average utilization metrics. A web application may have traffic spikes that push CPU beyond what the smaller instance can handle. Review p99 CPU, not just average CPU.

D is incorrect. Stopping and starting an instance to change the instance type does cause a brief downtime, but this is an operational concern separate from whether the smaller instance is technically sufficient. A properly designed application with load balancing handles this without impact.

E is correct. m5.2xlarge provides up to 10 Gbps network bandwidth; m5.xlarge provides up to 10 Gbps as well for this family, but network bandwidth scales with instance size. Verify the application's network throughput requirements are met.

---

## Question 8

A company activates cost allocation tags in the AWS Billing console but finds that resources created two months ago show no tag-based cost data in Cost Explorer. What is the MOST likely reason?

- A. Cost Explorer has a 90-day lag in processing tag activation requests
- B. Tags are not retroactive — tag-based cost data only appears from the activation date forward
- C. The resources must be stopped and restarted before tag data appears in billing
- D. Cost allocation tags only work with AWS Organizations management accounts

### Q8 Answer: B

### Q8 Analysis

A is incorrect. There is no 90-day lag. Tag activation takes effect promptly (within 24 hours), but only for future billing periods.

B is correct. Cost allocation tags are not retroactive. Once activated, the tags appear in Cost Explorer for billing data from that point forward. Past billing records do not retroactively include the tag attribution. This is a frequently missed nuance — organizations that adopt tagging late cannot recover historical per-tag cost data.

C is incorrect. Stopping and restarting resources is not related to tag processing in billing data.

D is incorrect. Cost allocation tags work in any AWS account, not only Organizations management accounts.

---

## Question 9

A company wants to automatically prevent engineers in a development account from spending more than $500 in a single month. When the $500 threshold is reached, all new EC2 instance launches should be denied automatically without manual intervention. Which feature implements this?

- A. AWS Budgets with a Budget Action that applies a deny-EC2 IAM policy
- B. CloudWatch billing alarm with an SNS email notification
- C. AWS Cost Anomaly Detection alert to an email address
- D. Service Control Policy pre-applied to all member accounts

### Q9 Answer: A

### Q9 Analysis

A is correct. AWS Budgets supports Budget Actions. When the $500 cost budget threshold is reached, a Budget Action can automatically apply an IAM policy that denies `ec2:RunInstances` to the account's IAM users. This requires no manual intervention.

B is incorrect. A CloudWatch billing alarm sends an SNS notification (email, SMS, Lambda) but does not automatically apply any IAM restriction. Manual intervention is still required to stop spending.

C is incorrect. Cost Anomaly Detection sends alerts about unusual spending patterns but does not take automated restricting actions.

D is incorrect. A pre-applied SCP could restrict EC2, but it would apply permanently regardless of spend level. The requirement is conditional — only apply the restriction when the $500 threshold is hit.

---

## Question 10

A company stores noncritical, reproducible thumbnail images in S3. These images are accessed frequently when first created but rarely after 60 days. The company wants to minimize storage costs while accepting reduced availability guarantees for these images. Which storage class is MOST cost-effective after 60 days?

- A. S3 Standard-IA
- B. S3 One Zone-IA
- C. S3 Glacier Instant Retrieval
- D. S3 Intelligent-Tiering

### Q10 Answer: B

### Q10 Analysis

A is incorrect. S3 Standard-IA provides Multi-AZ resilience, which is unnecessary for reproducible noncritical thumbnails. One Zone-IA is cheaper.

B is correct. S3 One Zone-IA stores data in a single Availability Zone at a lower cost than Standard-IA. The question explicitly states the images are noncritical and reproducible — losing them in a single-AZ failure is acceptable because they can be regenerated.

C is incorrect. Glacier Instant Retrieval has a lower per-GB storage cost than One Zone-IA but charges a per-GB retrieval fee. Images that are "rarely" — not "almost never" — accessed would accumulate retrieval charges that exceed the storage savings.

D is incorrect. Intelligent-Tiering adds a per-object monitoring fee. For objects with a known access pattern (frequently accessed initially, rarely after 60 days), a Lifecycle policy to One Zone-IA is more cost-effective than paying the monitoring fee for dynamic tiering.

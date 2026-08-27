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

---

### Question 11 (5 points)

A company runs a stateless web application on EC2 instances behind an Application Load Balancer. The application handles unpredictable traffic spikes and requires the lowest possible compute cost. Which EC2 purchasing option provides the greatest discount while keeping the application running during spikes?

A. On-Demand Instances exclusively — they scale quickly and have no commitment

B. Reserved Instances for 100% of the baseline load, with Spot Instances for additional capacity managed by an Auto Scaling group

C. Spot Instances exclusively — they offer up to 90% discount and Auto Scaling will replace interrupted instances

D. Dedicated Hosts for the baseline with On-Demand for spikes — Dedicated Hosts provide the best per-hour pricing

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. On-Demand Instances have no discount and are the most expensive option for sustained baseline traffic. They are appropriate for unpredictable short-term workloads, not steady-state production baselines.
- B is correct. Reserving capacity for the predictable baseline provides the largest sustained discount (up to 72% with 1-year Standard RIs). Spot Instances handle burst traffic at up to 90% discount. Auto Scaling manages Spot interruptions gracefully for a stateless application. This combination achieves the lowest blended cost.
- C is incorrect. Spot-only architectures risk availability when AWS reclaims capacity across all Spot pools during regional demand spikes. A stateless web application serving production traffic needs guaranteed baseline capacity — pure Spot is appropriate for batch or fault-tolerant workloads, not customer-facing applications requiring consistent availability.
- D is incorrect. Dedicated Hosts are the most expensive EC2 option — designed for software licensing requirements (Oracle, SQL Server per-socket licensing). They do not provide cost savings for general compute workloads.

---

### Question 12 (5 points)

A company's AWS bill shows $8,000/month in NAT Gateway data processing charges. Their architecture has EC2 instances in private subnets that primarily access Amazon S3 and DynamoDB. What is the most cost-effective architectural change?

A. Move the EC2 instances to public subnets to eliminate NAT Gateway traffic

B. Add VPC Gateway Endpoints for S3 and DynamoDB to route that traffic within the VPC without NAT charges

C. Replace the NAT Gateway with a NAT instance on a t3.micro to reduce hourly costs

D. Enable S3 Transfer Acceleration to bypass the NAT Gateway for S3 traffic

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Moving instances to public subnets creates significant security exposure — private subnets exist to prevent direct internet access to backend resources. This is an architectural regression, not a cost optimization.
- B is correct. VPC Gateway Endpoints for S3 and DynamoDB are free — they route traffic directly from the VPC to those services without traversing the NAT Gateway. If S3 and DynamoDB traffic represents the majority of NAT processing charges, this change can eliminate most of the $8,000 monthly cost with no downside.
- C is incorrect. Replacing a managed NAT Gateway with a NAT instance reduces hourly costs but still charges full data processing fees for all traffic. It also introduces operational overhead (patching, HA configuration) and does not address the root cause.
- D is incorrect. S3 Transfer Acceleration speeds up transfers between clients and S3 over long distances — it does not route traffic away from the NAT Gateway and actually adds additional per-GB charges on top of existing costs.

---

### Question 13 (5 points)

A startup uses AWS Cost Explorer to analyze their spending. They notice that EC2 costs vary significantly month to month and want to purchase Reserved Instances. They have 2 years of usage history showing consistent 24/7 use of `m5.large` instances in `us-east-1`. Which RI purchase provides the highest discount?

A. 1-year, No Upfront, Standard RI

B. 3-year, All Upfront, Standard RI

C. 1-year, All Upfront, Convertible RI

D. 3-year, No Upfront, Convertible RI

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. 1-year No Upfront provides the lowest discount of all RI options — roughly 36–40% for an m5.large. It has the highest effective hourly rate among Standard RIs.
- B is correct. 3-year All Upfront Standard RIs provide the maximum possible discount — up to 72% for an m5.large compared to On-Demand. Paying the full 3-year cost upfront eliminates the financing premium that No Upfront and Partial Upfront carry, maximizing total savings for a confirmed, stable workload.
- C is incorrect. Convertible RIs trade flexibility (ability to change instance family, OS, tenancy) for a lower discount compared to Standard RIs. For a stable, well-understood workload with 2 years of consistent usage history, the flexibility premium is unnecessary.
- D is incorrect. Convertible 3-year No Upfront provides a worse discount than Standard 3-year All Upfront on both dimensions — Convertible reduces discount, and No Upfront increases effective hourly rate.

---

### Question 14 (5 points)

A company wants to understand which AWS services are driving the most cost growth month-over-month across multiple linked accounts in their AWS Organization. They need line-item detail down to the resource level (individual EC2 instance IDs and S3 bucket names). Which AWS tool provides this granularity?

A. AWS Cost Explorer with "Group by: Service" filter

B. AWS Budgets with a cost budget and daily alert cadence

C. AWS Cost and Usage Report (CUR) delivered to S3 and queried with Amazon Athena

D. AWS Trusted Advisor Cost Optimization checks

**Correct Answer: C**

**Distractor Analysis:**

- A is incorrect. Cost Explorer provides service-level and account-level breakdowns with up to 12 months of history, but it does not drill down to individual resource IDs (instance IDs, bucket names). It is a visualization tool, not a raw billing data source.
- B is incorrect. Budgets alerts on threshold breaches for forecasted or actual spend — it does not provide resource-level cost attribution or trend analysis.
- C is correct. The AWS Cost and Usage Report is the most granular billing dataset AWS provides. It includes line items per resource ID (EC2 instance, S3 bucket, RDS instance), per hour, with usage type, tags, and blended/unblended costs. Delivered to S3 and queried with Athena, it enables any level of aggregation or drill-down needed for cost attribution.
- D is incorrect. Trusted Advisor Cost Optimization checks flag specific issues (underutilized EC2 instances, idle RDS) but do not provide month-over-month trend data or per-resource cost breakdowns.

---

### Question 15 (5 points)

A company runs hundreds of EC2 instances across multiple regions. They want to automatically identify underutilized instances and receive recommendations for downsizing without manually analyzing CloudWatch metrics. Which AWS service provides this?

A. AWS Cost Explorer RI recommendations

B. AWS Compute Optimizer

C. AWS Trusted Advisor low-utilization EC2 check (requires Business support)

D. Amazon CloudWatch automatic dashboards

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Cost Explorer RI recommendations identify opportunities to purchase Reserved Instances for current On-Demand usage — they do not analyze workload CPU/memory patterns to recommend instance size changes.
- B is correct. AWS Compute Optimizer uses machine learning to analyze 14 days of CloudWatch utilization metrics (CPU, memory via CloudWatch Agent, network, disk) and recommends optimal instance types and sizes. It identifies over-provisioned instances and suggests specific downsizing actions with estimated savings.
- C is incorrect. Trusted Advisor's low-utilization EC2 check flags instances with less than 10% average CPU utilization over 4 days — a useful signal, but far less sophisticated than Compute Optimizer's ML-based multi-metric analysis and specific rightsizing recommendations.
- D is incorrect. CloudWatch automatic dashboards display current metrics but do not perform utilization analysis or generate optimization recommendations.

---

### Question 16 (5 points)

A company purchases a 1-year EC2 Instance Savings Plan for 10 $/hour of compute spend. In a given hour, their actual EC2 spend is 14 $/hour. How does the Savings Plan apply?

A. The first 10 $/hour is covered at the Savings Plan discounted rate; the remaining 4 $/hour is charged at On-Demand rates

B. The entire 14 $/hour is covered at the Savings Plan discounted rate because the plan applies retroactively to all usage

C. The Savings Plan does not apply because actual spend exceeds the committed amount

D. The first 10 $/hour is free; the remaining 4 $/hour is charged at a 50% discount

**Correct Answer: A**

**Distractor Analysis:**

- A is correct. Savings Plans apply a discounted rate to compute usage up to the committed $/hour amount. Usage beyond the commitment continues at standard On-Demand rates. In this case, the first $10 of compute is discounted by the Savings Plan; the additional $4 is billed at On-Demand pricing.
- B is incorrect. Savings Plans do not retroactively cover all usage in an hour when the commitment is exceeded. The commitment is a ceiling, not a blanket discount on all spend in that hour.
- C is incorrect. Exceeding the committed amount does not invalidate the Savings Plan. The plan always applies its discount to usage up to the commitment level, regardless of total spend.
- D is incorrect. Savings Plans do not make committed usage free — they apply a discounted rate (e.g., 30–66% off On-Demand depending on plan type and term). The remaining usage above the commitment is On-Demand, not half-price.

---

### Question 17 (5 points)

A data engineering team runs Apache Spark jobs on EMR every night from midnight to 4 AM. The cluster is idle for the remaining 20 hours each day. Which cost optimization approach reduces the EMR cluster cost by the greatest amount?

A. Purchase Reserved Instances for all EMR core nodes

B. Terminate the cluster after each job completes and recreate it before the next job using a scheduled EventBridge rule and Step Functions

C. Move the EMR cluster to a smaller instance type to reduce the per-hour cost

D. Enable EMR Managed Scaling to reduce the number of core nodes during idle periods

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Reserving instances for nodes that are idle 20 hours per day would guarantee payment for unused capacity. RI discounts reduce hourly cost but do not eliminate cost during idle hours — making an idle cluster more expensive to reserve than to terminate.
- B is correct. Transient EMR clusters (terminate after job, recreate before next job) eliminate all EC2, EMR, and EBS costs during the 20 idle hours each day. For a batch workload with a predictable schedule, this reduces effective cost to approximately 17% of a continuously running cluster (4 active hours / 24 total hours).
- C is incorrect. A smaller instance type reduces per-hour cost but still charges for 20 idle hours. The cost reduction is proportional to the size reduction — far less than the ~83% savings from eliminating idle hours entirely.
- D is incorrect. EMR Managed Scaling adjusts the number of task nodes based on workload, but core nodes (minimum cluster size) remain running. It does not terminate the cluster or eliminate charges during the 20 idle hours.

---

### Question 18 (5 points)

A company activates cost allocation tags in the AWS Billing console and tags all resources with `Project` and `CostCenter` keys. After 30 days, the finance team reports that 40% of costs in Cost Explorer still show as untagged. What is the most likely reason?

A. Cost allocation tags only work for EC2 and S3 — other services are not supported

B. Some AWS service charges (data transfer, support fees, certain managed service costs) cannot be tagged at the resource level and appear as untagged

C. Tags must be applied retroactively to all historical usage for them to appear in Cost Explorer

D. The tags were activated after resources were created and AWS does not apply tags to running resources

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Cost allocation tags are supported across most AWS services — EC2, RDS, S3, Lambda, and many others. The limitation is not service coverage.
- B is correct. Certain AWS charges are not attributable to a specific tagged resource — data transfer charges, AWS Support fees, free tier credits, tax charges, and some managed service overhead costs appear without resource-level tags. Additionally, services like Route 53 hosted zones and some global features may not support resource tagging, contributing to untagged cost percentages in Cost Explorer.
- C is incorrect. Tags apply from the moment they are activated and resources are tagged going forward. Historical costs before tag activation remain untagged, but new charges from tagged resources show up correctly without retroactive application needed.
- D is incorrect. Cost allocation tags activated in Billing apply to all currently tagged resources going forward — AWS does not require re-tagging running resources after activation. The tags are read from current resource metadata, not at resource creation time.

---

### Question 19 (5 points)

A company is evaluating whether to commit to a 1-year Compute Savings Plan or continue with On-Demand pricing for their Lambda and Fargate workloads. Their Lambda invocation spend has been consistently $1,200/month for the past 6 months with minimal variation. Which analysis should drive the decision?

A. Purchase the Savings Plan only if the 1-year commitment cost is less than 12 months of On-Demand spend

B. Compare the effective hourly rate discount of the Savings Plan against the expected usage, then calculate the break-even point

C. Never purchase Savings Plans for Lambda — Reserved Concurrency is the cost control mechanism for Lambda

D. Purchase the Savings Plan only if the workload can be migrated to EC2 Instances within the commitment period

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. The 1-year commitment cost is always less than 12 months of On-Demand for the same usage level — that is the definition of a discount. The real analysis is whether the committed spend level matches expected actual usage, because unused commitment is wasted spend.
- B is correct. Compute Savings Plans apply a discount rate (e.g., 17% for Lambda, up to 52% for EC2) to eligible compute usage. The break-even analysis compares committed $/hour against expected actual $/hour usage. For $1,200/month of stable Lambda spend, a Compute Savings Plan commitment covering that usage level will save approximately 17% ($204/month) with minimal risk given the consistent usage history.
- C is incorrect. Compute Savings Plans explicitly cover Lambda compute costs (GB-seconds and request charges). Reserved Concurrency caps maximum concurrency but does not reduce Lambda per-invocation cost.
- D is incorrect. Compute Savings Plans cover Lambda, Fargate, and EC2 compute interchangeably — there is no requirement to migrate to EC2. The plan automatically applies the discount to whichever eligible compute service is used.

---

### Question 20 (5 points)

A company uses S3 Intelligent-Tiering for all objects in a large data lake. Objects range in size from 1 KB to 50 GB. A cost review shows the Intelligent-Tiering monitoring fee is unexpectedly high. What configuration change reduces the monitoring cost without losing the tiering benefit for large objects?

A. Switch all objects to S3 Standard-IA — it does not charge a monitoring fee

B. Configure an S3 Lifecycle policy to transition objects smaller than 128 KB to S3 Standard instead of Intelligent-Tiering

C. Disable Intelligent-Tiering and manually move objects between storage classes using a Lambda function

D. Enable S3 Batch Operations to consolidate small objects into large archive files before uploading

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. S3 Standard-IA charges a per-GB retrieval fee and has a 30-day minimum storage duration — for frequently accessed or short-lived objects, Standard-IA costs more than Standard. It also does not automatically tier objects.
- B is correct. S3 Intelligent-Tiering charges a per-object monitoring fee for every object regardless of size. For objects smaller than 128 KB, the monitoring fee typically exceeds any storage savings from tiering. Routing small objects to S3 Standard via Lifecycle policy eliminates their monitoring fees while preserving Intelligent-Tiering's benefit for the large objects where storage savings justify the monitoring cost.
- C is incorrect. Manual tiering via Lambda introduces operational complexity, requires custom code, and is prone to access pattern mismatches. It eliminates the Intelligent-Tiering monitoring fee but at significant operational cost.
- D is incorrect. S3 Batch Operations processes objects at scale (copying, tagging, restoring) but does not consolidate small objects into larger files — that would require application-level changes and would alter the data structure of the lake.

---

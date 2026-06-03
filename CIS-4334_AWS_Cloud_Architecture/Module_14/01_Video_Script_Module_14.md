# Video Script: Module 14 — AWS Cost Optimization

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Segment 1: The Cost Optimization Pillar

Welcome to Module 14. This module focuses on AWS cost optimization — the fifth pillar of the AWS Well-Architected Framework. Cloud economics is one of the defining advantages of AWS, but only if you actively manage your spending.

The Cost Optimization pillar has five design principles:

1. Implement cloud financial management — dedicate time and resources to cost management as a discipline
2. Adopt a consumption model — pay only for what you use; scale to zero when not needed
3. Measure overall efficiency — track business value delivered per dollar spent
4. Stop spending money on undifferentiated heavy lifting — use managed services so you pay for business logic, not infrastructure management
5. Analyze and attribute expenditures — use cost allocation tags and accounts to understand where money goes

For the SAA-C03 exam, cost optimization questions test your ability to select the right purchasing model, the right storage tier, and the right compute sizing for a given workload.

---

## Segment 2: EC2 Purchasing Options

Understanding EC2 purchasing options is critical for both the exam and real-world cost management.

**On-Demand Instances** — pay by the second (Linux) or by the hour (Windows). No commitment, no upfront cost. Highest per-unit price. Use for unpredictable workloads, new applications, and short-term spikes.

**Reserved Instances (RIs)** — commit to a 1-year or 3-year term for a specific instance family, OS, tenancy, and region. Discounts up to 72% compared to On-Demand. Three payment options:

- No Upfront — monthly payments, smallest discount
- Partial Upfront — pay some now, rest monthly, better discount
- All Upfront — pay the full term upfront, maximum discount

RI types:

- **Standard RIs** — locked to instance family, OS, and region. Greatest discount.
- **Convertible RIs** — can be exchanged for a different instance family, OS, or region. Smaller discount (~54%) but more flexibility.

**Savings Plans** — newer and more flexible than RIs. Two types:

- **Compute Savings Plans** — apply to any EC2 instance family, region, OS, or tenancy, plus Lambda and Fargate. Up to 66% discount.
- **EC2 Instance Savings Plans** — apply to a specific instance family in a specific region. Up to 72% discount (same as Standard RIs).

For new commitments, Savings Plans are generally preferred over RIs because they are simpler to manage and apply automatically.

**Spot Instances** — use spare EC2 capacity at up to 90% discount. AWS can reclaim Spot Instances with a 2-minute warning. Best for fault-tolerant, stateless, or interruptible workloads: batch processing, big data, CI/CD, and ML training.

**Dedicated Hosts** — physical servers dedicated to your use. Required for software licenses tied to physical cores or sockets (Windows Server, SQL Server per-core licensing). Most expensive option.

**Dedicated Instances** — instances that run on hardware dedicated to you but you do not manage the physical host.

---

## Segment 3: AWS Compute Optimizer and Rightsizing

**Rightsizing** is the process of matching instance size and type to actual workload requirements. Overprovisioning is the most common cost waste in AWS — organizations deploy large instances "just in case" and consistently use 10–20% of the available capacity.

**AWS Compute Optimizer** uses ML to analyze 14 days of CloudWatch metrics and recommends optimal instance types. It analyzes EC2 instances, Auto Scaling groups, Lambda functions (memory), EBS volumes (IOPS/throughput), ECS tasks on Fargate, and RDS DB instances.

Compute Optimizer provides three recommendation options for each resource:

- **Under-provisioned** — current instance is too small; performance is constrained
- **Optimized** — current instance is well-matched
- **Over-provisioned** — current instance is too large; reducing size saves money

Findings are available via console, API, or CloudWatch Recommendations dashboard. Export to S3 for bulk analysis.

**Rightsizing considerations:**

- Do not rightsize based on peak utilization alone. Look at average and p99 CPU, memory, and network.
- Account for burst capacity — some workloads spike briefly but need headroom.
- Test before production — validate the smaller instance type handles actual load.
- Use Auto Scaling as an alternative to manual rightsizing when workload is variable.

---

## Segment 4: S3 Storage Classes and Intelligent-Tiering

S3 offers multiple storage classes optimized for different access patterns. Choosing the wrong class is a significant source of unnecessary cost.

**S3 Standard** — general purpose, high durability (11 nines), low latency. Most expensive per GB. Use for frequently accessed data.

**S3 Standard-IA (Infrequent Access)** — same durability and availability as Standard, but lower storage cost and per-retrieval fee. Use for data accessed monthly, not daily. Minimum storage duration: 30 days.

**S3 One Zone-IA** — stored in a single AZ. Lower cost than Standard-IA. Use for reproducible data that does not need Multi-AZ resilience. Minimum 30-day duration.

**S3 Glacier Instant Retrieval** — millisecond retrieval for archive data accessed quarterly. Lower storage cost than Standard-IA. Minimum 90-day duration.

**S3 Glacier Flexible Retrieval** (formerly Glacier) — retrieval in minutes to hours. Very low storage cost. Use for backups and compliance archives. Minimum 90-day duration.

**S3 Glacier Deep Archive** — lowest storage cost in S3. Retrieval in 12–48 hours. Use for long-term compliance archives accessed once or twice per year. Minimum 180-day duration.

**S3 Intelligent-Tiering** — automatically moves objects between access tiers based on access patterns at no retrieval charge. Six tiers: Frequent, Infrequent (30 days no access), Archive Instant (90 days), Archive Access (90–730 days, configurable), Deep Archive Access (180–730 days, configurable). Small monthly monitoring and automation fee per object. Best for data with unknown or changing access patterns.

**S3 Lifecycle policies** move or expire objects on a schedule. Transition rules move objects to cheaper tiers after a specified number of days. Expiration rules delete objects after a specified period. Use lifecycle policies for predictable access patterns; use Intelligent-Tiering for unpredictable patterns.

---

## Segment 5: AWS Cost Management Tools

**AWS Cost Explorer** — visualize and analyze AWS spending over time. Built-in reports for daily and monthly spend by service, region, account, and tag. Forecast future spend based on historical trends. Identify Reserved Instance and Savings Plan coverage gaps.

**AWS Budgets** — set spending limits and receive alerts when actual or forecasted costs exceed thresholds. Four budget types:

- Cost budget — alert on total spend
- Usage budget — alert on service usage (e.g., EC2 hours)
- RI utilization budget — alert when RI utilization falls below a threshold
- Savings Plans coverage budget — alert when coverage drops

Budgets can trigger SNS notifications and AWS Budget Actions (automatically apply an IAM policy or SCP to restrict spending when a budget is exceeded).

**AWS Cost and Usage Report (CUR)** — the most granular cost and usage data available. Delivered to S3 as CSV or Parquet files. Integrates with Athena, Redshift, and QuickSight for custom analysis. The CUR is the source of truth for all billing data.

**Cost Allocation Tags** — key-value pairs applied to resources. Activate tags in the Billing console to enable per-tag cost breakdowns. Use consistent tags: `Project`, `Environment`, `Owner`, `CostCenter`. Untagged resources are invisible in tag-based cost reports.

**AWS Organizations and SCPs** — use Organizational Units and Service Control Policies to restrict which services teams can use and which regions they can deploy to. This prevents accidental cost overruns from unauthorized resource creation.

---

## Segment 6: Reserved Instances vs. Savings Plans Decision Guide

For the exam, use this framework:

If the question involves EC2 only in a specific region and instance family, and flexibility is NOT mentioned: **EC2 Instance Savings Plan** or **Standard RI** provide the maximum discount.

If the question involves Lambda or Fargate, or needs flexibility across instance families and regions: **Compute Savings Plans** are the right answer.

If the question involves workloads that run continuously 24/7 for 1–3 years: **Any RI or Savings Plan** is appropriate — On-Demand is never cost-optimal for steady-state workloads.

If the question mentions "batch," "interruptible," "fault-tolerant," or "can tolerate interruption": **Spot Instances** deliver the maximum possible discount.

If the question mentions "software license tied to physical hardware" or "per-core/per-socket licensing": **Dedicated Hosts** are required.

---

## Segment 7: Data Transfer and Network Cost Optimization

Data transfer costs are often overlooked and can surprise organizations with large bills.

Key data transfer pricing rules:

- Data transfer INTO AWS is free from the internet.
- Data transfer OUT of AWS to the internet is charged per GB.
- Data transfer between AWS services within the same AZ is free.
- Data transfer between AZs in the same region is charged ($0.01/GB each way).
- Data transfer between regions is charged at higher rates.

**Cost optimization strategies for data transfer:**

- Use CloudFront to serve content to end users. CloudFront origin fetches are cheaper than direct EC2-to-internet egress.
- Use VPC Endpoints (Gateway endpoints for S3 and DynamoDB) to keep traffic within the AWS network — no data transfer charges to the public internet.
- Colocate tightly coupled services in the same AZ when cross-AZ transfer costs matter.
- Use Compression to reduce data sizes before transfer.
- Use S3 Transfer Acceleration only when needed — it has a per-GB charge higher than standard S3 PUT.

---

## Segment 8: Well-Architected Framework Cost Pillar Best Practices

The SAA-C03 exam tests your understanding of cost best practices across these categories:

**Practice Cloud Financial Management** — assign cost ownership to teams, implement tagging standards, review Cost Explorer weekly, and conduct quarterly rightsizing reviews.

**Expenditure Awareness** — use AWS Budgets and alerts, enable Cost Anomaly Detection (ML-based unusual spend detection), and ensure all resources are tagged.

**Cost-Effective Resources** — match instance types to workload profiles, use managed services (RDS instead of self-managed databases, SQS instead of self-managed message brokers), choose the right storage class for each dataset.

**Manage Demand and Supply Resources** — use Auto Scaling to match compute supply to demand, use Lambda or Fargate to avoid paying for idle capacity.

**Optimize Over Time** — regularly review AWS new service launches; services often become cheaper over time or newer generations provide better price/performance.

---

## Closing Summary

Module 14 covered the full cost optimization toolkit. You can now select the right EC2 purchasing model for any workload, use Compute Optimizer and rightsizing to eliminate waste, choose the correct S3 storage class or configure Intelligent-Tiering for unknown access patterns, and use Cost Explorer, Budgets, and cost allocation tags to manage and attribute spending.

Your lab this week uses Cost Explorer to analyze a sample spending pattern, configures a Cost Budget with an SNS alert, and evaluates Compute Optimizer recommendations. See you in the lab.

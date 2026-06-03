# Reading Guide: Module 14 — AWS Cost Optimization

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Apply the five cost optimization design principles of the AWS Well-Architected Framework
2. Select the appropriate EC2 purchasing model for a given workload profile
3. Explain the difference between Reserved Instances and Savings Plans and choose between them
4. Configure S3 Lifecycle policies and select the correct storage class for a given access pattern
5. Use AWS Cost Explorer, Budgets, and Cost Allocation Tags to manage and attribute spending
6. Interpret AWS Compute Optimizer recommendations for EC2 rightsizing
7. Identify data transfer cost patterns and apply strategies to minimize egress charges

---

## Section 1: Well-Architected Cost Optimization Pillar

### 1.1 Five Design Principles

The Cost Optimization pillar defines five principles guiding cost-aware architecture decisions:

**Implement cloud financial management.** Treat cost management as a competency. Assign FinOps ownership, train engineers to understand the cost implications of their architectural choices, and build cost review into the development lifecycle.

**Adopt a consumption model.** Match resource provisioning to actual demand. Scale out during peak periods and scale in (or scale to zero) during off-peak. Serverless services naturally implement this principle.

**Measure overall efficiency.** Track business outcomes per dollar spent, not just total spend. Monitor metrics like revenue per EC2 instance or API calls processed per dollar.

**Stop spending on undifferentiated heavy lifting.** Use managed services (RDS, SQS, Lambda) instead of self-managed equivalents. The operational overhead of managing infrastructure is itself a cost.

**Analyze and attribute expenditures.** Use cost allocation tags, multiple AWS accounts, and Cost Explorer to attribute costs to teams, projects, and environments. Visible costs drive accountable behavior.

### 1.2 Cost Optimization vs. Other Pillars

Cost optimization does not mean "cheapest." It means maximizing value. A solution that saves money but introduces unacceptable downtime risk is not cost-optimized — it trades one type of cost (infrastructure) for another (lost revenue). Balance cost against the requirements of the other four pillars: reliability, security, performance efficiency, and operational excellence.

---

## Section 2: EC2 Purchasing Options Reference

### 2.1 Comparison Table

| Model | Discount vs. On-Demand | Commitment | Interruption Risk | Best For |
|---|---|---|---|---|
| On-Demand | 0% | None | None | Unpredictable, short-term |
| Spot | Up to 90% | None | Yes (2-min warning) | Fault-tolerant, batch |
| Compute Savings Plan | Up to 66% | 1 or 3 years | None | Lambda + Fargate + EC2 (flexible) |
| EC2 Instance Savings Plan | Up to 72% | 1 or 3 years | None | Specific family + region |
| Standard RI | Up to 72% | 1 or 3 years | None | Specific family + OS + region |
| Convertible RI | Up to 54% | 1 or 3 years | None | Specific region, flexible family |
| Dedicated Host | No discount | On-Demand or RI | None | Per-socket/core licensing |

### 2.2 Spot Instance Interruption Handling

When AWS needs the capacity back, Spot Instances receive a 2-minute interruption notice via the Instance Metadata Service (IMDS) at `http://169.254.169.254/latest/meta-data/spot/termination-time` and as an EventBridge event. Design Spot workloads to:

- Checkpoint state to S3 or EFS regularly
- Use Spot with Auto Scaling groups configured with multiple instance types and AZs (diversification)
- Use EC2 Fleet or Auto Scaling Group with `capacity-optimized` allocation strategy to select the pool with lowest interruption probability

### 2.3 Savings Plans vs. Reserved Instances

For new purchases, AWS recommends Savings Plans. They are simpler: no need to match specific instance attributes, they apply automatically across qualifying usage, and Compute Savings Plans extend to Lambda and Fargate. RIs remain available and may be advantageous when using third-party RI marketplaces.

---

## Section 3: AWS Compute Optimizer

### 3.1 Supported Resources

Compute Optimizer analyzes:

- EC2 instances (instance type, size, family recommendations)
- EC2 Auto Scaling groups (scaling configuration recommendations)
- Lambda functions (memory size recommendations)
- EBS volumes (IOPS and throughput configuration)
- ECS tasks on Fargate (CPU and memory configuration)
- RDS DB instances (instance class recommendations)

### 3.2 How It Works

Compute Optimizer collects 14 days of CloudWatch utilization metrics. It applies ML models trained on millions of workload profiles to project performance at other instance configurations. It normalizes CPU, memory (if CloudWatch Agent is installed), network, and disk metrics.

Recommendations include:

- Projected performance risk at the recommended configuration
- Estimated monthly savings
- Side-by-side comparison of current vs. recommended configuration

### 3.3 Enhanced Infrastructure Metrics

For an additional charge, Compute Optimizer can use up to 93 days of historical metrics (instead of 14) for more accurate recommendations on workloads with long-cycle seasonality (e.g., month-end batch processing).

### 3.4 Savings Estimation Accuracy

Compute Optimizer savings estimates assume On-Demand pricing. If you are already using Savings Plans or RIs, actual savings from rightsizing may differ. Always validate recommendations against your actual billing model.

---

## Section 4: S3 Storage Classes and Lifecycle Management

### 4.1 Storage Class Decision Framework

Use this framework to select the correct storage class:

| Access Pattern | Recommended Class |
|---|---|
| Accessed multiple times per day | S3 Standard |
| Accessed less than once per month, millisecond retrieval needed | S3 Standard-IA |
| Accessed less than once per month, single-AZ acceptable | S3 One Zone-IA |
| Accessed quarterly, millisecond retrieval needed | S3 Glacier Instant Retrieval |
| Accessed yearly, minutes/hours retrieval acceptable | S3 Glacier Flexible Retrieval |
| Accessed once or twice per year, 12–48 hour retrieval acceptable | S3 Glacier Deep Archive |
| Access pattern unknown or variable | S3 Intelligent-Tiering |

### 4.2 Minimum Storage Duration Charges

Some storage classes charge a minimum storage duration regardless of when you delete or transition the object:

- Standard-IA and One Zone-IA: 30 days
- Glacier Instant Retrieval and Glacier Flexible Retrieval: 90 days
- Glacier Deep Archive: 180 days

If you delete or transition an object before its minimum duration, you are charged for the remaining days. This makes short-lived objects in IA or Glacier classes more expensive than Standard.

### 4.3 S3 Intelligent-Tiering Architecture

Intelligent-Tiering monitors object access patterns and moves objects between internal tiers automatically:

- **Frequent Access tier** — default landing tier
- **Infrequent Access tier** — objects not accessed for 30 days are automatically moved here
- **Archive Instant Access tier** — objects not accessed for 90 days (optional activation)
- **Archive Access tier** — objects not accessed for 90–730 days (optional activation; retrieval in hours)
- **Deep Archive Access tier** — objects not accessed for 180–730 days (optional activation; retrieval in 12–48 hours)

There is no retrieval charge within Intelligent-Tiering for the Frequent and Infrequent tiers. A small per-object monitoring fee applies ($0.0025 per 1,000 objects/month). Not cost-effective for objects smaller than 128 KB — they are always stored in the Frequent Access tier.

### 4.4 Lifecycle Policy Rules

Lifecycle policies support two rule types:

- **Transition rules** — move objects to a specified storage class after N days
- **Expiration rules** — permanently delete objects (or delete non-current versions) after N days

Lifecycle rules can apply to all objects in a bucket or to a prefix/tag filter. Common patterns:

- Transition to Standard-IA at 30 days, Glacier Flexible Retrieval at 90 days, expire at 2,555 days (7 years)
- Delete incomplete multipart uploads after 7 days (prevents accumulation of partial uploads that incur storage charges)
- Expire noncurrent object versions after 30 days for versioned buckets

---

## Section 5: AWS Cost Management Tools

### 5.1 Cost Explorer

Cost Explorer provides interactive visualizations of AWS spending. Key features:

- Daily, monthly, and hourly granularity (hourly requires enabling)
- Group by service, region, account, usage type, tag, or API operation
- Filter to specific time ranges, services, or linked accounts
- RI and Savings Plan utilization and coverage reports
- Cost forecasting based on historical trends (up to 12-month forecast)
- Rightsizing recommendations (powered by Compute Optimizer data)

### 5.2 AWS Budgets

Four budget types with alerting:

| Budget Type | Alert Trigger |
|---|---|
| Cost | Actual or forecasted spend exceeds $ threshold |
| Usage | Actual or forecasted usage exceeds unit threshold |
| RI Utilization | RI utilization falls below % threshold |
| RI Coverage | RI coverage of usage falls below % threshold |

**Budget Actions** — when a budget threshold is reached, automatically:

- Apply an IAM policy (e.g., deny EC2 RunInstances)
- Apply an SCP to an OU (restrict service access organization-wide)
- Target specific EC2 or RDS instances for stop/terminate

Up to 5 actions per budget alert. Useful for protecting sandbox accounts from runaway costs.

### 5.3 Cost and Usage Report (CUR)

The CUR is the most detailed billing dataset available. It includes:

- Every resource used, every hour
- Blended and unblended costs
- On-Demand equivalent costs for reserved usage
- Savings Plan amortization
- Every cost allocation tag

Delivered to an S3 bucket as CSV or Apache Parquet. Query with Athena (set up via the CUR integration wizard). Visualize with QuickSight. Export to a Redshift data warehouse for multi-account reporting.

### 5.4 Cost Anomaly Detection

Cost Anomaly Detection uses ML to identify unusual spending patterns without requiring manual threshold configuration. It evaluates individual services, member accounts, cost categories, and cost allocation tags. Send alerts to SNS topics when anomalies are detected. Evaluate root-cause services automatically.

### 5.5 Cost Allocation Tags

Two types:

- **AWS-generated tags** — automatically applied by AWS (e.g., `aws:createdBy`, `aws:cloudformation:stack-name`)
- **User-defined tags** — applied by users and automation (e.g., `Project`, `Environment`, `Owner`)

Tags must be activated in the AWS Billing and Cost Management console before they appear in Cost Explorer. Tags are not retroactive — they appear in reports only from the activation date forward.

---

## Section 6: Data Transfer Cost Optimization

### 6.1 Pricing Model Summary

| Transfer Type | Cost |
|---|---|
| Internet → AWS (ingress) | Free |
| AWS → Internet (egress) | ~$0.09/GB (first 10 TB/month, US regions) |
| Between AZs in same region | ~$0.01/GB each direction |
| Between regions | ~$0.02–0.08/GB depending on regions |
| Within same AZ (same service) | Free |
| EC2 → S3 (Gateway VPC Endpoint) | Free |

### 6.2 Cost Reduction Strategies

**VPC Gateway Endpoints** for S3 and DynamoDB route traffic through the AWS private network. No internet gateway required, no NAT gateway charges for this traffic, and no data transfer charges.

**CloudFront** as a CDN reduces egress from origins. CloudFront pricing per GB is lower than EC2-to-internet pricing, and CloudFront caching eliminates repeat origin fetches.

**S3 regional co-location** — store S3 buckets in the same region as the EC2 instances or Lambda functions that access them. Cross-region S3 access incurs both S3 request charges and inter-region data transfer charges.

**Compress before transfer** — GZIP or Brotli compression reduces payload sizes for API responses and data exports.

---

## Key Terms

- **Reserved Instance (RI)** — 1 or 3-year EC2 capacity commitment for specific attributes in exchange for a discount
- **Savings Plan** — flexible commitment (compute or instance) applied automatically across qualifying usage
- **Spot Instance** — spare EC2 capacity at up to 90% discount; subject to 2-minute interruption notice
- **Rightsizing** — matching instance size to actual workload utilization to eliminate over-provisioning waste
- **Compute Optimizer** — ML-powered service recommending optimal instance and resource configurations
- **S3 Intelligent-Tiering** — automatic storage class management based on access patterns
- **S3 Lifecycle Policy** — rules to transition or expire objects after a specified number of days
- **Cost Allocation Tag** — key-value pair on a resource that enables per-tag cost breakdowns
- **Cost and Usage Report (CUR)** — most granular AWS billing dataset, delivered to S3
- **Budget Action** — automated response (IAM policy, SCP, resource stop) triggered when a budget threshold is breached

---

## SAA-C03 Exam Tips

- Spot Instances are always the right answer for "fault-tolerant batch workloads" needing maximum discount
- Compute Savings Plans are more flexible than RIs and cover Lambda + Fargate — prefer them for new purchases
- S3 Intelligent-Tiering is the right answer when the access pattern is unknown or unpredictable
- Minimum storage duration charges apply to IA and Glacier classes — do not use Glacier for short-lived objects
- Cost allocation tags must be activated in the Billing console before they appear in Cost Explorer
- VPC Gateway Endpoints for S3 and DynamoDB eliminate NAT gateway charges and data transfer fees
- Compute Optimizer requires 14 days of CloudWatch data; it does NOT analyze ECS EC2 tasks (only Fargate)
- AWS Budgets can take automated actions (apply IAM policy, stop instances) when thresholds are breached

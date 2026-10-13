# Video Script: Module 13 — AWS Monitoring, Logging, and Operations

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Segment 1: Why Observability Matters

Welcome to Module 13. This module covers the operational visibility layer of AWS — the tools that let you know what your systems are doing, what happened in the past, and whether your infrastructure is healthy and compliant.

The SAA-C03 exam tests your ability to design operationally excellent architectures. That means knowing which service answers which question:

- What is my system doing right now? → CloudWatch Metrics and Dashboards
- Did something go wrong? → CloudWatch Alarms
- What did my application log? → CloudWatch Logs
- Where is a request spending its time? → AWS X-Ray
- Who did what to my AWS account? → AWS CloudTrail
- Is my configuration compliant with policy? → AWS Config
- What operational tasks need automation? → AWS Systems Manager
- Am I following best practices? → AWS Trusted Advisor

Let's walk through each service in the depth the exam requires.

---

## Segment 2: Amazon CloudWatch — Metrics

CloudWatch is the central monitoring service for AWS. Every AWS service publishes metrics to CloudWatch automatically.

A **metric** is a time-series data point. Metrics have a namespace (e.g., `AWS/EC2`), a name (e.g., `CPUUtilization`), and dimensions (key-value pairs that identify specific resources, e.g., `InstanceId=i-0abc123`).

**Standard metrics** are published by AWS at no charge. EC2 publishes CPU utilization, network in/out, disk read/write operations, and status checks every 5 minutes. You cannot get memory utilization or disk space from EC2 standard metrics — those require the CloudWatch Agent.

**Detailed monitoring** for EC2 publishes metrics every 1 minute instead of 5. Costs extra but enables faster alarm response.

**Custom metrics** are published by your application using the `PutMetricData` API. Standard resolution is 1-minute granularity. High-resolution custom metrics use 1-second granularity (StorageResolution=1).

**Metric math** lets you query and transform multiple metrics into a new calculated metric without storing additional data. Example: divide `Errors` by `Invocations` to compute an error rate metric on a Lambda function.

**Metric retention.** CloudWatch retains metrics with different retention periods based on resolution:

- High-resolution (1 second): 3 hours
- 1-minute resolution: 15 days
- 5-minute resolution: 63 days
- 1-hour resolution: 455 days (15 months)

---

## Segment 3: CloudWatch Alarms

Alarms watch a metric and trigger actions when the metric crosses a threshold for a specified number of evaluation periods.

Alarm states:

- **OK** — metric is within the threshold
- **ALARM** — metric has crossed the threshold
- **INSUFFICIENT_DATA** — not enough data to evaluate (common at startup or if the resource was recently created)

Alarm actions include:

- Send a notification to an SNS topic (which can trigger email, SMS, Lambda, etc.)
- Execute an EC2 action (stop, terminate, reboot, recover)
- Trigger an Auto Scaling policy

**Composite Alarms** combine multiple alarms using AND/OR logic. Example: only page the on-call engineer when BOTH high CPU AND high error rate alarms are in ALARM state simultaneously. This reduces alert noise.

**Anomaly Detection** uses ML to establish a baseline band for a metric. Set an alarm when the metric falls outside the expected range. Useful for metrics with cyclical patterns (daily traffic peaks) where a static threshold would produce false positives.

---

## Segment 4: Amazon CloudWatch Logs

CloudWatch Logs stores, monitors, and searches log data from any source. Services like Lambda, API Gateway, and ECS can send logs automatically. EC2 requires the CloudWatch Agent.

**Log structure:**

- **Log Group** — logical container for logs from a related source. Retention policy applies at this level.
- **Log Stream** — sequence of log events from a single source instance (one Lambda execution environment, one EC2 instance, etc.)
- **Log Event** — individual timestamped log entry

**Log Insights** is an interactive query language for CloudWatch Logs. You can write queries using `fields`, `filter`, `stats`, `sort`, and `limit` commands. Results are returned in seconds to minutes depending on data volume. Use Log Insights to find error patterns, compute percentile latencies, and count event types.

**Metric Filters** extract metric data from log events. Define a filter pattern (e.g., `[ERROR]`) and a metric name/namespace/value. Every matching log event increments the metric. Use metric filters to build alarms on log-derived metrics (error counts, specific application events).

**Subscription Filters** route log events in real time to:

- Kinesis Data Streams (for real-time processing)
- Kinesis Data Firehose (for delivery to S3, Redshift, OpenSearch)
- Lambda (for real-time transformation or routing)

**Log retention** defaults to indefinite. Set retention periods (1 day to 10 years) to manage cost. Logs can be exported to S3 for long-term archival.

---

## Segment 5: CloudWatch Dashboards and Container Insights

**CloudWatch Dashboards** create custom operational views combining metrics from multiple services, accounts, and regions. Dashboards use widgets: line charts, number widgets, alarm status widgets, and text widgets. Cross-account and cross-region dashboards consolidate visibility for multi-account organizations.

**CloudWatch Container Insights** collects metrics and logs from ECS (EC2 and Fargate), EKS, and Kubernetes on EC2. Provides pod-level, task-level, and cluster-level performance data. Requires the CloudWatch Agent or Fluent Bit as a sidecar.

**CloudWatch Application Insights** automatically detects and monitors resource groups for common application patterns (.NET, SQL Server, Java). Identifies anomalies and correlates them with related logs and metrics.

**CloudWatch Synthetics** runs headless Chromium scripts (canaries) on a schedule to test API endpoints and web pages. Detects availability issues before real users encounter them.

---

## Segment 6: AWS X-Ray

X-Ray provides distributed tracing for applications. A **trace** represents the end-to-end journey of a single request through your system. A trace contains **segments** (one per service the request touches) and **subsegments** (subdivisions within a service — specific function calls, database queries, downstream HTTP calls).

**Service map.** X-Ray automatically generates a visual service map showing how services connect and the latency and error rate on each connection. This is the fastest way to identify bottlenecks and failure points in a microservices architecture.

**Sampling.** By default, X-Ray samples 1 request per second plus 5% of additional requests. You can configure custom sampling rules by service name, URL path, HTTP method, host, and request rate. Higher sampling = more visibility but higher cost.

**X-Ray integration.** Lambda, API Gateway, App Mesh, EC2 (via X-Ray daemon or SDK), ECS, EKS, Elastic Beanstalk, SNS, and SQS all integrate with X-Ray. Enable Active Tracing on Lambda and API Gateway with a checkbox — no code changes required for the trace header propagation.

**Annotations vs. Metadata.** Annotations are indexed key-value pairs — you can filter and group traces by annotation values. Metadata is unindexed rich data stored with a segment but not searchable. Use annotations for dimensions you want to query; use metadata for debug information.

---

## Segment 7: AWS CloudTrail

CloudTrail records API calls made to your AWS account — who did what, when, from where, and to which resource.

**Event types:**

- **Management events** — control-plane actions: creating/deleting resources, modifying IAM policies, changing security groups. Recorded by default. Read and write events can be separated.
- **Data events** — data-plane actions: S3 object reads/writes, Lambda invocations, DynamoDB item operations. Not recorded by default — you must explicitly enable them. High volume = higher cost.
- **Insights events** — CloudTrail Insights detects unusual patterns in write management event volume (e.g., a sudden spike in IAM policy changes or EC2 TerminateInstances calls). Requires explicit enablement.

**Trails.** A trail configures delivery of events to S3. You can create an organization trail that covers all accounts in an AWS Organization. Apply S3 Server-Side Encryption (SSE-KMS) and enable log file integrity validation (SHA-256 hash chain) to ensure logs have not been tampered with.

**CloudTrail Lake.** A managed audit and security lake that ingests CloudTrail events into an event data store. Supports SQL-based queries directly on the event data. Retention up to 7 years. Eliminates the need to manage Athena + S3 for CloudTrail queries.

For the exam: CloudTrail answers "who changed what?" It is the go-to service for security audits, compliance investigations, and detecting unauthorized API calls.

---

## Segment 8: AWS Config

AWS Config continuously records the configuration state of your AWS resources and evaluates them against rules.

**Configuration items** capture the state of a resource at a point in time — all attributes, relationships to other resources, and associated CloudTrail events.

**Configuration history** lets you view how a resource's configuration changed over time. Answer questions like: "What was the security group configuration last Tuesday at 3 PM?"

**Config Rules** evaluate resource configurations against desired policies:

- **AWS Managed Rules** — over 200 pre-built rules (e.g., `s3-bucket-public-read-prohibited`, `encrypted-volumes`, `multi-region-cloud-trail-enabled`)
- **Custom Rules** — Lambda-backed rules that evaluate any configuration condition your business requires

**Remediation.** Config rules can trigger automatic remediation via AWS Systems Manager Automation documents. Example: a rule detects a publicly accessible S3 bucket and automatically applies the `BlockPublicAccess` configuration.

**Conformance Packs** group multiple Config rules and remediation actions into a single deployable package. AWS provides sample packs for common compliance frameworks (PCI-DSS, HIPAA, CIS Benchmarks).

For the exam: Config answers "is my configuration compliant?" and "how did it change?" It is the compliance and governance service.

---

## Segment 9: AWS Systems Manager

Systems Manager (SSM) is the operational hub for managing AWS and on-premises resources at scale.

**Key SSM capabilities for SAA-C03:**

**Parameter Store** — hierarchical, versioned storage for configuration data and secrets. Supports plaintext (Standard tier, free) and SecureString (encrypted with KMS). Up to 10,000 parameters per account per region in the Standard tier. Advanced tier supports larger values and parameter policies (expiration, notifications). Integrate with Lambda, ECS, CloudFormation, and EC2 startup scripts.

**Session Manager** — browser-based or CLI shell access to EC2 instances and on-premises servers without opening SSH port 22. No bastion host required. All session activity is logged to CloudWatch Logs and S3.

**Run Command** — execute scripts or commands on a fleet of managed instances without SSH. Target by tag, resource group, or instance ID. Output sent to CloudWatch Logs or S3.

**Patch Manager** — automates OS and application patching across managed instances on a defined schedule with compliance reporting.

**Automation** — executes multi-step operational playbooks (runbooks) as SSM Automation documents. Used by Config remediation, incident response, and routine maintenance.

**Inventory** — collects software inventory, network configuration, and OS details from managed instances.

---

## Segment 10: Trusted Advisor and Operational Excellence

**AWS Trusted Advisor** analyzes your account and provides recommendations across five categories:

1. Cost Optimization — underutilized resources, unused Elastic IPs, Reserved Instance coverage gaps
2. Performance — high-utilization instances, CloudFront configuration, EBS throughput limits
3. Security — open security group ports, MFA on root account, S3 bucket public access, IAM password policy
4. Fault Tolerance — RDS Multi-AZ, EBS snapshots, EC2 Auto Scaling group configuration
5. Service Limits — warns when you approach account service limits

Free (Basic and Developer support) plans receive access to 7 core security and service limit checks. Business and Enterprise support plans unlock all checks and enable programmatic access via the Trusted Advisor API.

**Operational Excellence pillar summary.** For SAA-C03, the Operational Excellence pillar of the Well-Architected Framework emphasizes:

- Operations as code — use CloudFormation, SSM Automation, and Config remediation rather than manual processes
- Annotate documentation — keep runbooks and playbooks in SSM Automation documents
- Make small, reversible changes — deployments through CI/CD pipelines with rollback capabilities
- Anticipate failure — use CloudWatch Alarms, X-Ray tracing, and synthetic monitoring to detect issues proactively
- Learn from all operational events — conduct post-incident reviews and update runbooks

---

## Closing Summary

Module 13 gave you the full observability toolkit for AWS. CloudWatch provides metrics, alarms, logs, dashboards, and automated responses. X-Ray traces requests through distributed systems. CloudTrail records every API action for security audit. AWS Config enforces configuration compliance. Systems Manager automates operational tasks and provides secure instance access. Trusted Advisor identifies best-practice gaps across cost, security, performance, and fault tolerance.

Your lab this week configures a CloudWatch alarm that triggers an SNS notification, deploys a metric filter to count application errors from Lambda logs, and queries CloudTrail to identify recent changes to a security group. See you in the lab.

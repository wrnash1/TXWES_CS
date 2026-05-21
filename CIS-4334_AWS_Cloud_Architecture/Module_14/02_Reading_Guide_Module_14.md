# Reading Guide: Module 14 - Monitoring – CloudWatch, CloudTrail, AWS Config
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

### Introduction
Welcome to **Module 14 - Monitoring – CloudWatch, CloudTrail, and AWS Config**! Operational visibility is a core requirement of production cloud architectures. This module covers the three primary AWS monitoring and governance services: Amazon CloudWatch (metrics, logs, and alarms), AWS CloudTrail (API activity auditing), and AWS Config (resource configuration history and compliance). Understanding which service answers which type of operational question is directly tested on the SAA-C03 exam and is essential for architecting observable, auditable cloud systems.

---

### 1. High-Yield Glossary
Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

*   **Amazon CloudWatch Metrics**: Time-series data points emitted by AWS services (CPU utilization, NetworkIn, DiskReadOps, etc.) collected at 1-minute or 5-minute intervals (standard), or 1-second intervals with detailed monitoring. Custom metrics can be published via `PutMetricData` API for application-level measurements. CloudWatch Metrics are the foundation for Auto Scaling policies, dashboards, and alarm thresholds.

*   **Amazon CloudWatch Alarms**: Monitors a single CloudWatch metric and transitions between OK, ALARM, and INSUFFICIENT_DATA states based on configurable thresholds. Alarms trigger actions: SNS notifications, Auto Scaling policies, EC2 instance state changes (stop/terminate/recover), or Systems Manager OpsItems. Composite Alarms combine multiple alarms with AND/OR logic to reduce alert noise.

*   **Amazon CloudWatch Logs**: A managed log aggregation service. EC2 instances (via the CloudWatch Agent), Lambda functions (automatically), ECS containers, and other services stream log data to CloudWatch Log Groups. Log Groups contain Log Streams (per-source log sequences). Metric Filters extract metrics from log content (e.g., count ERROR occurrences per minute). Subscription Filters stream logs in real time to Lambda, Kinesis, or OpenSearch for processing and analysis.

*   **AWS CloudTrail**: Records every AWS API call made in an account — including who made the call (IAM principal), what resource was affected (ARN), when (timestamp), from where (source IP), and whether it succeeded or was denied. CloudTrail logs are stored in S3 and optionally streamed to CloudWatch Logs. CloudTrail is the primary service for security forensics, compliance audits, and answering "who changed what and when?" Trail events cover Management Events (control plane, enabled by default), Data Events (S3 object-level, Lambda invocations — paid), and Insights Events (unusual API activity patterns).

*   **AWS Config**: A configuration history and compliance service that continuously records the configuration state of AWS resources over time and evaluates those configurations against defined compliance rules (Config Rules). Config answers: "what was the configuration of this security group three weeks ago?" Config Rules can be AWS-managed (pre-built checks like `s3-bucket-public-read-prohibited`) or custom Lambda-based rules. Config can trigger automatic remediation via AWS Systems Manager Automation when non-compliant resources are detected.

---

### 2. Certification Exam Tips

*   **SAA-C03 Domain Relevance:** Monitoring content appears in all four domains but most heavily in Operational Excellence and Design Resilient Architectures (26%). "Who made this change?" → CloudTrail. "Is CPU high on my EC2?" → CloudWatch Metrics. "Is my S3 bucket publicly accessible?" → AWS Config.

*   **CloudWatch vs. CloudTrail vs. Config Exam Trap:** These three services are frequently confused. CloudWatch = performance metrics and logs (operational monitoring). CloudTrail = API call history (security auditing, "who did what?"). Config = resource configuration state over time (compliance, configuration change history). The exam presents a specific question type and expects the correct service.

*   **CloudWatch Agent:** By default, EC2 instances don't push memory utilization or disk usage metrics to CloudWatch — only hypervisor-level metrics (CPU, network, disk I/O) are available. Memory and disk metrics require the CloudWatch Agent installed on the instance. This is a common exam trap — "detailed monitoring" only increases the frequency of existing metrics, it does not add memory metrics.

*   **CloudTrail Multi-Region vs. Organization Trail:** By default, CloudTrail is enabled per-Region. Multi-Region trails capture all Regions into a single S3 bucket. For organizations with multiple AWS accounts, an Organization Trail in the management account captures all member account API activity — eliminating the need to configure trails in each account.

*   **Config vs. CloudTrail for Changes:** Config records "what the resource looks like" (configuration state) over time and shows configuration diffs between states. CloudTrail records "what API call was made" — who initiated the change. For compliance: Config. For accountability: CloudTrail. A complete audit uses both.

*   **Study Resource:** The CloudWatch and CloudTrail documentation covers all metrics, alarms, and log configuration: [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/cloudwatch/index.html) and [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/). The [AWS Config Developer Guide](https://docs.aws.amazon.com/config/latest/developerguide/) covers all managed Config Rules.

---

### Required Readings & Videos
To prepare for this module's topics, you must complete the following readings and videos:

*   **Required Reading:** Read the CloudWatch, CloudTrail, and AWS Config chapters in the AWS Solutions Architect study materials. Review the [CloudWatch Concepts documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html) for metrics, namespaces, and alarms. The [AWS Whitepapers & Guides](https://aws.amazon.com/whitepapers/) contains the "Operational Excellence Pillar" whitepaper, which covers monitoring architecture best practices.

*   **Required Video:** Watch the monitoring module in the official course playlist, focusing on the three-service distinction (CloudWatch/CloudTrail/Config), CloudWatch Agent configuration for memory metrics, and the AWS Config compliance rule evaluation cycle: [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).

---

### Lab & Command Integration
In this week's hands-on lab, you will perform the following steps to apply these concepts:

*   **Create a CloudWatch alarm on EC2 CPU utilization:** Create a CloudWatch Alarm triggering an SNS email notification when average CPU exceeds 70% for two consecutive 5-minute periods. Use the `aws cloudwatch put-metric-alarm` CLI command. Trigger the alarm using a CPU stress tool and verify the email is received.

*   **Query CloudTrail logs for specific API activity:** In the CloudTrail console, filter events by "Event name: TerminateInstances" and "User name" to identify who terminated a specific EC2 instance. Practice constructing CloudTrail Insights to detect unusual API call volumes.

*   **Enable an AWS Config Rule and test compliance:** Enable the `s3-bucket-public-read-prohibited` AWS managed Config Rule. Create an S3 bucket with public read access and observe Config marking it as NON_COMPLIANT within minutes. Enable auto-remediation to block public access automatically.

---

### 3. Study Checklist
- [ ] Read and be able to define all five glossary terms in your own words.
- [ ] Understand the CloudWatch metric types and alarm states at [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html).
- [ ] Review CloudTrail event types at [https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html).
- [ ] Watch the monitoring video lecture in [AWS Certified Solutions Architect Associate Course](https://www.youtube.com/watch?v=Ia-UEYYR44s).
- [ ] Complete the hands-on lab creating CloudWatch alarms, querying CloudTrail, and testing AWS Config Rules.
- [ ] Proceed to the weekly quiz.

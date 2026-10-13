# Reading Guide: Module 13 — AWS Monitoring, Logging, and Operations

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4334 &BULL; AMAZON WEB SERVICES (AWS) CLOUD ARCHITECTURE</text>
    
    <!-- Stage 1 -->
    <g transform="translate(40, 75)">
      <rect width="150" height="150" rx="8" fill="#ffffff" stroke="#1b365d" stroke-width="2"/>
      <rect width="150" height="32" rx="8" fill="#1b365d"/>
      <rect width="150" height="10" y="22" fill="#1b365d"/>
      <text x="75" y="20" fill="#d9a74a" font-size="12" font-weight="bold" text-anchor="middle">1. INPUT / SOURCE</text>
      <text x="75" y="65" fill="#1e293b" font-size="12" font-weight="600" text-anchor="middle">Raw Data / Code</text>
      <text x="75" y="90" fill="#64748b" font-size="11" text-anchor="middle">User Input</text>
      <text x="75" y="110" fill="#64748b" font-size="11" text-anchor="middle">Configurations</text>
      <text x="75" y="130" fill="#64748b" font-size="11" text-anchor="middle">Parameters</text>
      <rect x="25" y="145" width="100" height="20" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
      <text x="75" y="158" fill="#1b365d" font-size="10" font-weight="bold" text-anchor="middle">Validation</text>
    </g>

    <!-- Arrow 1 -->
    <path d="M 200 150 L 250 150" stroke="#d9a74a" stroke-width="3" fill="none" marker-end="url(#arrow)"/>
    <polygon points="250,150 240,144 240,156" fill="#d9a74a"/>

    <!-- Stage 2 -->
    <g transform="translate(260, 75)">
      <rect width="260" height="150" rx="8" fill="#ffffff" stroke="#16a34a" stroke-width="2"/>
      <rect width="260" height="32" rx="8" fill="#16a34a"/>
      <rect width="260" height="10" y="22" fill="#16a34a"/>
      <text x="130" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">2. CORE PROCESSING ENGINE</text>
      <text x="130" y="60" fill="#166534" font-size="13" font-weight="bold" text-anchor="middle">Logic &amp; Protocol Execution</text>
      <rect x="20" y="75" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="93" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">State Management &amp; Parsing</text>
      <rect x="20" y="110" width="220" height="28" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="130" y="128" fill="#166534" font-size="11" font-weight="600" text-anchor="middle">Security &amp; Exception Handling</text>
    </g>

    <!-- Arrow 2 -->
    <polygon points="580,150 570,144 570,156" fill="#d9a74a"/>
    <path d="M 530 150 L 580 150" stroke="#d9a74a" stroke-width="3" fill="none"/>

    <!-- Stage 3 -->
    <g transform="translate(590, 75)">
      <rect width="170" height="150" rx="8" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
      <rect width="170" height="32" rx="8" fill="#2563eb"/>
      <rect width="170" height="10" y="22" fill="#2563eb"/>
      <text x="85" y="20" fill="#ffffff" font-size="12" font-weight="bold" text-anchor="middle">3. OUTPUT / VERIFY</text>
      <text x="85" y="65" fill="#1e40af" font-size="12" font-weight="600" text-anchor="middle">Production Result</text>
      <text x="85" y="90" fill="#64748b" font-size="11" text-anchor="middle">Telemetry / Logs</text>
      <text x="85" y="110" fill="#64748b" font-size="11" text-anchor="middle">Automated Tests</text>
      <text x="85" y="130" fill="#64748b" font-size="11" text-anchor="middle">Verified Status</text>
      <rect x="25" y="145" width="120" height="20" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="85" y="158" fill="#1e40af" font-size="10" font-weight="bold" text-anchor="middle">Mastery Confirmed</text>
    </g>

    <!-- Footer -->
    <text x="400" y="260" fill="#64748b" font-size="11" font-style="italic" text-anchor="middle">Figure 1.1: Standard Enterprise Architectural Execution Workflow &bull; Texas Wesleyan University CIS Department</text>
  </svg>
</div>


## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Learning Objectives

By the end of this module, you will be able to:

1. Distinguish CloudWatch Metrics, Alarms, Logs, and Dashboards and configure each for operational visibility
2. Write CloudWatch Logs Insights queries to extract operational signals from log data
3. Explain how AWS X-Ray traces requests through distributed systems and identify bottlenecks
4. Use AWS CloudTrail to answer security audit and compliance questions
5. Configure AWS Config rules and remediation to enforce configuration compliance
6. Select Systems Manager capabilities for secure instance access, configuration management, and patching
7. Interpret AWS Trusted Advisor recommendations across all five categories

---

## Section 1: CloudWatch Metrics Deep Dive

### 1.1 Namespaces and Dimensions

Every CloudWatch metric belongs to a namespace. AWS service metrics use namespaces like `AWS/EC2`, `AWS/Lambda`, `AWS/RDS`, and `AWS/ELB`. Custom application metrics use custom namespaces you define.

Dimensions further identify the metric. For `AWS/EC2 CPUUtilization`, the dimension `InstanceId=i-0abc123` identifies a specific instance. You can aggregate metrics across dimensions — for example, get average CPU across an entire Auto Scaling group by omitting the InstanceId dimension.

### 1.2 Metric Math

Metric Math creates new time series from existing metrics. Supported functions include arithmetic operators, `SUM()`, `AVG()`, `MIN()`, `MAX()`, `PERIOD()`, `RATE()`, and `IF()`. Create an alarm on a metric math expression — for example, alarm when error rate `(errors / invocations * 100)` exceeds 1%.

### 1.3 CloudWatch Agent

The CloudWatch Agent runs on EC2 instances and on-premises servers to collect metrics not available from the hypervisor:

- Memory utilization
- Disk space utilization
- Open file handles, CPU steal time, swap usage
- Custom application log files

Store the agent configuration JSON in SSM Parameter Store and distribute it via SSM Run Command.

### 1.4 Metric Retention Periods

| Resolution | Retention |
|---|---|
| 1 second (high-resolution) | 3 hours |
| 1 minute | 15 days |
| 5 minutes | 63 days |
| 1 hour | 455 days |

---

## Section 2: CloudWatch Alarms Reference

### 2.1 Alarm States

- **OK** — metric is within the threshold
- **ALARM** — metric has breached the threshold for the configured number of periods
- **INSUFFICIENT_DATA** — not enough data points to evaluate

### 2.2 Alarm Configuration Parameters

| Parameter | Description |
|---|---|
| Period | Evaluation window length in seconds |
| Evaluation periods | Number of periods to consider |
| Datapoints to alarm | Breaching datapoints required within evaluation periods |
| Missing data treatment | breaching, notBreaching, ignore, or missing |

### 2.3 Missing Data Treatment

- **notBreaching** — missing data is treated as within threshold. Use for infrequently invoked resources.
- **breaching** — missing data is treated as crossing the threshold. Use for heartbeat-style health checks.
- **ignore** — current alarm state is maintained.
- **missing** — alarm transitions to INSUFFICIENT_DATA.

### 2.4 Composite Alarms

Composite Alarms evaluate the state of two or more child alarms using AND/OR/NOT logic. They do not evaluate metrics directly. Use composite alarms to require multiple signals before paging on-call — for example, only alert when both high CPU AND high error rate alarms are simultaneously in ALARM state.

---

## Section 3: CloudWatch Logs Operations

### 3.1 Log Structure

- **Log Group** — logical container for related log streams; retention policy is set at this level
- **Log Stream** — sequence of events from a single source (one EC2 instance, one Lambda execution environment)
- **Log Event** — individual timestamped entry

### 3.2 Log Insights Query Language

Key commands:

- `fields` — select fields to display
- `filter` — narrow results using comparisons and regex (`like`)
- `stats` — aggregate: `count()`, `sum()`, `avg()`, `min()`, `max()`, `percentile()`
- `sort` — order results
- `limit` — cap number of rows returned
- `parse` — extract fields from unstructured log text

Example — 95th percentile Lambda duration:

```text
fields @timestamp, @duration
| filter @type = "REPORT"
| stats pct(@duration, 95) as p95 by bin(5m)
| sort @timestamp desc
```

### 3.3 Metric Filters

A metric filter extracts a CloudWatch metric from log events. Define a filter pattern, a metric namespace, name, and value. Every matching log event increments the metric. Use metric filters to create alarms on application-level events (error counts, specific log strings) that are not tracked by default AWS metrics.

### 3.4 Subscription Filters

Subscription filters stream log events in real time to:

- Kinesis Data Streams — for real-time processing
- Kinesis Data Firehose — for delivery to S3, Redshift, or OpenSearch
- Lambda — for real-time transformation or alerting

Use a subscription filter with a central Kinesis stream to aggregate logs from multiple accounts and regions in an AWS Organizations environment.

---

## Section 4: AWS X-Ray Architecture

### 4.1 Trace Anatomy

A **trace** captures the end-to-end journey of one request. It consists of:

- **Segments** — one per service the request touches
- **Subsegments** — subdivisions within a segment (individual DB calls, downstream HTTP requests, custom code blocks)

The trace ID propagates through services via the `X-Amzn-Trace-Id` HTTP header.

### 4.2 Service Map

X-Ray automatically generates a visual service map. Each node represents a service; each edge shows the connection between services with latency percentiles and error rates. The service map is the primary tool for identifying bottlenecks and failure points in distributed architectures.

### 4.3 Sampling Rules

Default sampling: 1 request/second plus 5% of additional requests. Custom sampling rules can specify:

- Service name
- HTTP method and URL path
- Host
- Fixed rate and reservoir size

Higher sampling provides more visibility but increases cost. Configure lower sampling rates for high-volume, low-value paths (health checks) and higher rates for critical business transactions.

### 4.4 Annotations vs. Metadata

- **Annotations** — indexed key-value pairs. Filterable and groupable in the X-Ray console and API. Use for dimensions you want to query (customer tier, region, order type).
- **Metadata** — non-indexed rich data attached to a segment. Not searchable. Use for debug payloads you want preserved with the trace but do not need to query.

### 4.5 Integration Options

| Option | Effort | Notes |
|---|---|---|
| Active Tracing (Lambda/API GW) | Zero — one checkbox | Auto-instruments outbound AWS SDK calls |
| X-Ray SDK | Medium — code changes | Custom subsegments, annotations, metadata |
| AWS Distro for OpenTelemetry | Higher | Standards-based, multi-backend |

---

## Section 5: AWS CloudTrail Reference

### 5.1 Event Types

| Event Type | What It Captures | Default | Cost |
|---|---|---|---|
| Management events | Control-plane API calls (create, modify, delete) | On | Included |
| Data events | Data-plane operations (S3 Get/Put, Lambda Invoke, DynamoDB) | Off | Per event |
| Insights events | Unusual API activity patterns | Off | Per event |

### 5.2 Event History vs. Trails

- **Event History** — free, last 90 days, management events only, console/API access, no S3 delivery
- **Trail** — configures delivery to S3; enables retention beyond 90 days; required for data events and Insights

### 5.3 Log File Integrity Validation

CloudTrail creates a SHA-256 digest file that chains log file hashes. Use `aws cloudtrail validate-logs` to verify no log files were modified or deleted. Required by many compliance frameworks (PCI-DSS, SOC 2, HIPAA).

### 5.4 CloudTrail Lake

A managed event data store with SQL-based querying. Retention up to 7 years. Eliminates the need to manage Athena + S3 for ad-hoc CloudTrail queries. Supports cross-account queries via an organization event data store.

---

## Section 6: AWS Config Deep Dive

### 6.1 Configuration Items and History

A **configuration item** is a point-in-time snapshot of a resource's full configuration, relationships, and associated CloudTrail events. Config retains these items for the configured retention period (default 7 years). Use configuration history to answer: "What was the security group configuration on this instance last Tuesday?"

### 6.2 Rule Trigger Types

- **Configuration change** — evaluates when the resource's configuration changes
- **Periodic** — evaluates on a schedule (every 1, 3, 6, 12, or 24 hours)

### 6.3 Remediation Actions

Config rules can trigger automatic remediation using SSM Automation documents. AWS provides pre-built remediation actions for common rules:

- `AWS-DisablePublicAccessForSecurityGroup` — removes 0.0.0.0/0 inbound rules
- `AWS-EnableS3BucketEncryption` — enables default encryption on an S3 bucket
- `AWS-PublishSNSNotification` — sends a notification to an SNS topic

### 6.4 Conformance Packs

A Conformance Pack is a collection of Config rules and remediation actions deployable as a single unit. AWS provides sample packs for:

- CIS AWS Foundations Benchmark
- PCI DSS
- HIPAA Security Rule
- NIST 800-53

Deploy a Conformance Pack across all accounts in an organization using the Config aggregator and CloudFormation StackSets.

---

## Section 7: AWS Systems Manager Capabilities

### 7.1 Parameter Store Tiers

| Feature | Standard | Advanced |
|---|---|---|
| Max parameters | 10,000 | 100,000 |
| Max value size | 4 KB | 8 KB |
| Parameter policies | No | Yes (expiration, notification) |
| Cost | Free | $0.05/advanced parameter/month |

### 7.2 Secrets Manager vs. Parameter Store Decision Guide

Use Secrets Manager when:

- Automatic rotation is required (RDS, Redshift, DocumentDB, custom Lambda rotation)
- You need cross-service secret sharing with built-in versioning and rotation lifecycle
- The $0.40/secret/month cost is acceptable

Use Parameter Store when:

- Storing configuration values, feature flags, non-rotating API keys
- Cost sensitivity is high (free Standard tier)
- You need hierarchical organization by application/environment/parameter-name

### 7.3 Session Manager Architecture

Session Manager works through the SSM Agent installed on the instance. The agent maintains an outbound HTTPS (port 443) connection to the SSM service endpoints. No inbound ports need to be open. The instance needs:

- SSM Agent installed (pre-installed on Amazon Linux 2, Windows Server 2016+, Ubuntu 16.04+)
- `AmazonSSMManagedInstanceCore` IAM instance profile
- Outbound connectivity to SSM, EC2 Messages, and SSM Messages endpoints (VPC endpoints for private subnets)

---

## Section 8: Trusted Advisor Categories and Exam Relevance

### 8.1 Free Checks (All Support Plans)

- MFA on root account
- IAM use (at least one IAM user exists)
- Security groups with unrestricted access on specific high-risk ports
- S3 bucket public access
- EBS public snapshots
- RDS public snapshots
- Service limit warnings for EC2, ELB, EBS, VPC

### 8.2 Business/Enterprise-Only Checks

All 400+ checks are available, plus:

- Low-utilization EC2 and RDS instances (cost optimization)
- Unused Reserved Instances
- Amazon S3 storage cost optimization
- CloudFront SSL certificate expiration
- Route 53 health check configuration
- Full service limit checks across all services

### 8.3 Exam Pattern: Trusted Advisor Answers

When an exam question asks "Which service helps identify underutilized EC2 instances for cost savings?" — Trusted Advisor (Cost Optimization category).

When an exam question asks "Which service provides recommendations for improving fault tolerance?" — Trusted Advisor (Fault Tolerance category).

Trusted Advisor is advisory; it identifies issues and recommends actions but does not automatically remediate (unlike Config). The exception is that you can build automation around Trusted Advisor API results using EventBridge and Lambda.

---

## Key Terms

- **CloudWatch Metric** — time-series data point with namespace, name, and dimensions
- **Composite Alarm** — combines multiple child alarms with AND/OR logic to reduce noise
- **CloudWatch Logs Insights** — interactive SQL-like query language for log data
- **X-Ray Trace** — end-to-end record of a single request across all services
- **X-Ray Annotation** — indexed key-value pair on a segment; queryable and filterable
- **CloudTrail Trail** — configuration that delivers API event logs to an S3 bucket
- **Config Rule** — policy evaluating resource configurations for compliance
- **SSM Parameter Store** — hierarchical key-value store for configuration data and secrets
- **Session Manager** — shell access to instances without SSH, bastion hosts, or open ports
- **Conformance Pack** — bundle of Config rules for a compliance framework

---

## SAA-C03 Exam Tips

- CloudWatch Agent is required for EC2 memory utilization — it is NOT available as a default metric
- CloudTrail Event History is free for 90 days; trails are needed for longer retention or data events
- Config records configuration state; CloudTrail records API calls — both are needed for full compliance visibility
- Session Manager replaces bastion hosts — "no port 22 open" scenarios always point to Session Manager
- X-Ray Active Tracing on Lambda requires only enabling a checkbox — no SDK code changes needed
- Composite Alarms require AND/OR logic across multiple alarms — use them to reduce alert noise
- Secrets Manager is the answer when automatic rotation of database credentials is required
- Config Conformance Packs deploy compliance rule sets (PCI, HIPAA) as single deployable units

---

## 10. Supplemental Resources

**1. AWS Documentation — Amazon CloudWatch User Guide**
https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
Complete reference for CloudWatch metrics, alarms, composite alarms, Logs Insights query syntax, metric filters, and dashboards — the primary reference for the monitoring and alerting topics covered in Module 13 and tested on the SAA-C03 exam.

**2. AWS Skill Builder — Monitoring and Observability on AWS**
https://skillbuilder.aws/learn/course/external/view/elearning/1955/monitoring-and-observability-on-aws
Free course covering CloudWatch, X-Ray, CloudTrail, and AWS Config — supporting the full Module 13 observability curriculum and providing hands-on practice with the CLI commands and console workflows used in the lab.

**3. AWS Documentation — AWS CloudTrail User Guide**
https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
Authoritative guide to CloudTrail trail configuration, event types (management, data, Insights), log file integrity validation, and multi-region trail setup — the definitive reference for audit logging requirements and compliance scenarios in this module.

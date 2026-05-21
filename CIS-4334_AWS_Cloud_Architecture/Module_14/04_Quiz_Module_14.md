# Quiz: Module 14 - Monitoring – CloudWatch, CloudTrail, AWS Config
## Course: CIS-4334_AWS_Cloud_Architecture (AWS Certified Solutions Architect - Associate)

---

**Question 1**
Which AWS service should you check first to determine which IAM user or role executed an API call that terminated a production EC2 instance three days ago?
*   A) Amazon CloudWatch Metrics — review the EC2 instance state change metric history.
*   B) AWS CloudTrail — search the event history for `TerminateInstances` events with the instance ID to identify the caller's identity, source IP, and timestamp.
*   C) AWS Config — review the configuration history of the EC2 instance to identify who changed its state.
*   D) Amazon GuardDuty — check threat findings for unauthorized instance termination events.
*   **Correct Answer:** B) AWS CloudTrail records every API call including who made it (IAM ARN), from where (source IP), and when — making it the definitive source for answering "who did what?" in an AWS account.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudWatch Metrics track performance data (CPU, network, disk). Instance state changes are visible as metric data points, but CloudWatch does not record the identity of who initiated the state change — only that the state changed.
    *   *Why B is correct:* CloudTrail is the security audit trail for AWS API activity. The `TerminateInstances` EC2 API call creates a CloudTrail Management Event recording the `userIdentity` (IAM user/role ARN), `sourceIPAddress`, `eventTime`, and `requestParameters` (including the instance ID). This is the only native AWS service that records caller identity for API actions.
    *   *Why C is incorrect:* AWS Config records the configuration state of resources over time and can show when an EC2 instance's state changed from `running` to `terminated`. However, Config does not record the IAM identity that initiated the change — it records the state change outcome, not the caller. CloudTrail records the caller.
    *   *Why D is incorrect:* GuardDuty analyzes logs for threat patterns and generates security findings. It may generate a finding if the termination was from an anomalous source, but it is not the primary tool for answering accountability questions about specific API calls. GuardDuty findings are behavioral detections, not a complete API activity record.

---

**Question 2**
Which of the following is the most accurate description of **AWS Config** and its primary use case?
*   A) A real-time performance monitoring service that collects CPU, memory, and network metrics from AWS resources and triggers alarms when thresholds are exceeded.
*   B) A configuration history and compliance service that continuously records the state of AWS resource configurations, tracks changes over time, and evaluates resources against compliance rules.
*   C) A log aggregation service that collects application logs from EC2 instances, Lambda functions, and containers into centralized Log Groups for querying and alerting.
*   D) An API audit service that records every AWS API call made in an account, including the caller's identity, source IP, and timestamp.
*   **Correct Answer:** B) AWS Config records the configuration state of AWS resources continuously, maintains a history of changes, and evaluates configurations against compliance rules — answering "was this resource compliant at any point in time?"
*   **Distractor Analysis:**
    *   *Why A is incorrect:* This describes Amazon CloudWatch (metrics and alarms). CloudWatch collects time-series performance data; Config records resource configuration attributes (properties, relationships, and tags).
    *   *Why B is correct:* Config is the configuration history and compliance layer. It can answer questions like "what was the inbound rule set of this security group on March 15th?" and "have any S3 buckets been configured with public access in the last 30 days?" Config Rules provide automated compliance evaluation with optional auto-remediation.
    *   *Why C is incorrect:* This describes Amazon CloudWatch Logs. CloudWatch Logs aggregates log streams from various sources; Config tracks structured resource configuration attributes, not unstructured log text.
    *   *Why D is incorrect:* This describes AWS CloudTrail. CloudTrail records API call events (actions); Config records resource configuration states (current and historical property values).

---

**Question 3**
An operations team needs to receive an email alert whenever an EC2 instance's CPU utilization exceeds 80% for more than 10 consecutive minutes. Which combination of AWS services implements this with the least operational overhead?
*   A) Install a custom monitoring agent on each EC2 instance that sends emails via an SMTP server when CPU exceeds 80%.
*   B) Create a CloudWatch Alarm on the `CPUUtilization` metric with a threshold of 80% over two 5-minute periods; configure an SNS Topic as the alarm action, with an email subscription on the topic.
*   C) Enable AWS Config Rule `ec2-instance-cpu-alarm` to detect high CPU and trigger an SNS notification.
*   D) Configure CloudTrail to log CPU metrics and set a CloudTrail Insight to trigger an email when unusual CPU patterns are detected.
*   **Correct Answer:** B) CloudWatch Alarm → SNS → Email is the standard, fully managed AWS pattern for metric-based operational alerting with no infrastructure to manage.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A self-managed SMTP-based monitoring agent on every EC2 instance requires installation, maintenance, scaling, and SMTP configuration — significant operational overhead compared to the fully managed CloudWatch + SNS approach.
    *   *Why B is correct:* CloudWatch Alarms are designed exactly for this use case. The alarm monitors the `CPUUtilization` metric in the `AWS/EC2` namespace, evaluates it over the specified period and datapoint count (2 datapoints of 5 minutes each = 10 minutes), and triggers an SNS action when in ALARM state. SNS handles email delivery to all subscribed addresses — zero operational overhead.
    *   *Why C is incorrect:* AWS Config Rules evaluate resource configuration properties (e.g., security group rules, S3 bucket settings). CPU utilization is a performance metric, not a configuration property. There is no AWS Config managed rule for CPU performance.
    *   *Why D is incorrect:* CloudTrail records API calls (control plane events), not performance metrics. CloudTrail Insights detects unusual API activity patterns. CloudTrail cannot monitor EC2 CPU utilization — that is CloudWatch's domain.

---

**Question 4**
A security officer finds that an EC2 instance's security group was modified to allow inbound traffic from 0.0.0.0/0 on port 22 (SSH) at some point in the past two weeks. They need to determine both (a) what the security group looked like before the change and (b) which IAM user made the change. Which combination of services provides both answers?
*   A) Amazon CloudWatch Logs and Amazon Inspector
*   B) AWS Config (for configuration history showing the before/after state) and AWS CloudTrail (for the API event showing who made the change)
*   C) AWS CloudTrail only — CloudTrail records both the old and new configuration state in the event payload
*   D) AWS Config only — Config records both the configuration change and the identity of the principal who initiated it
*   **Correct Answer:** B) Config records the configuration history (showing the before and after security group rule states) and CloudTrail records the API event identifying who made the `AuthorizeSecurityGroupIngress` call.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CloudWatch Logs contains application and system logs, not resource configuration history. Amazon Inspector performs vulnerability scans, not configuration change tracking. Neither answers either of the two required questions.
    *   *Why B is correct:* This is the canonical AWS monitoring combination for compliance and accountability. Config maintains a timeline of resource configuration states — you can see exactly what the security group rules were at any point in time. CloudTrail provides the event record showing which IAM principal called `AuthorizeSecurityGroupIngress`, from which IP, and at what time. Together they provide complete forensic context.
    *   *Why C is incorrect:* CloudTrail records the API action and its parameters (the new rules being added), but it does not independently maintain the full configuration state of the resource before and after the change. You would need to reconstruct the before-state by examining all prior CloudTrail events, which is complex. Config's configuration history is far more straightforward for seeing historical resource state.
    *   *Why D is incorrect:* AWS Config records what the resource looks like (configuration state changes) and when the change occurred, but Config does not record the IAM identity that initiated the change. Config delegates accountability information to CloudTrail. Using Config alone, you know the configuration changed but not who changed it.

---

**Question 5**
A company wants to ensure that no EC2 instances in their AWS account are ever launched with the unrestricted inbound rule `0.0.0.0/0` on port 22. They want non-compliant resources detected automatically and the violation reported within minutes of the change. Which AWS service and configuration achieves this?
*   A) Create a CloudWatch Alarm on a custom metric that counts EC2 instances with open port 22.
*   B) Enable the AWS Config managed rule `restricted-ssh`, which evaluates security groups and marks those allowing unrestricted SSH as NON_COMPLIANT, triggering an SNS notification.
*   C) Enable AWS GuardDuty to detect open port 22 in security groups and generate a critical finding immediately.
*   D) Configure CloudTrail to send all events to a CloudWatch Logs group, then create a metric filter and alarm for `AuthorizeSecurityGroupIngress` API calls.
*   **Correct Answer:** B) The `restricted-ssh` AWS Config managed rule continuously evaluates security groups and immediately flags any group allowing 0.0.0.0/0 on port 22 as NON_COMPLIANT, with SNS notification support and optional auto-remediation.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* There is no built-in CloudWatch metric for "EC2 instances with open port 22." Building a custom metric would require a Lambda function scheduled to run periodically to evaluate all security groups, adding significant operational complexity. Config does this natively.
    *   *Why B is correct:* AWS Config managed rules evaluate resource configurations against defined policies. `restricted-ssh` is a purpose-built managed rule that detects security groups with unrestricted SSH access. Config evaluates the rule when the security group is created or changed (change-triggered), providing near-real-time detection. Auto-remediation via Systems Manager Automation can automatically remove the offending rule.
    *   *Why C is incorrect:* GuardDuty detects behavioral threats (active attacks, compromised credentials, cryptomining) by analyzing CloudTrail and Flow Logs. GuardDuty does not evaluate security group configurations for compliance policy violations. Detecting a configuration policy violation (open port 22) is AWS Config's role.
    *   *Why D is incorrect:* Monitoring `AuthorizeSecurityGroupIngress` CloudTrail events via CloudWatch metric filters detects when any security group rule is added, but requires additional filtering logic to determine if the new rule is specifically port 22 with 0.0.0.0/0 — a complex metric filter. This approach also triggers on any `AuthorizeSecurityGroupIngress` call, not just violations. Config's `restricted-ssh` rule evaluates the actual resource state directly, providing a cleaner and more accurate compliance check.


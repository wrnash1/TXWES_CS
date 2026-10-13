# Quiz: Module 13 — AWS Monitoring, Logging, and Operations

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Instructions

Select the best answer for each question. Each question is worth 10 points. Answer key and distractor analysis follow each question.

---

## Question 1

A company needs to monitor memory utilization on its EC2 instances and trigger an alarm when memory exceeds 85%. After enabling detailed monitoring, the operations team notices that memory metrics are still not appearing in CloudWatch. What is the MOST likely cause?

- A. Detailed monitoring only provides 1-minute resolution; memory metrics require 30-second resolution
- B. The CloudWatch Agent has not been installed and configured on the EC2 instances
- C. Memory metrics require a CloudWatch Logs subscription filter before appearing as metrics
- D. Memory utilization is available only for instances in a specific AWS Region

### Q1 Answer: B

### Q1 Analysis

A is incorrect. Detailed monitoring changes the frequency of standard hypervisor metrics from 5 minutes to 1 minute. It does not add new metric types such as memory.

B is correct. EC2 does not report memory or disk utilization to CloudWatch by default because the hypervisor cannot access guest OS memory statistics. The CloudWatch Agent must be installed on the instance and configured to publish these metrics.

C is incorrect. Subscription filters route log events to external destinations — they do not create infrastructure metrics.

D is incorrect. Memory metrics are not region-restricted. They simply require the CloudWatch Agent on every platform.

---

## Question 2

An operations team wants to receive a single PagerDuty alert only when BOTH a high CPU alarm AND a high error rate alarm are simultaneously in ALARM state. When only one alarm is triggered, no alert should be sent. Which CloudWatch feature satisfies this requirement?

- A. CloudWatch Anomaly Detection on a combined metric
- B. A Composite Alarm using AND logic on both child alarms
- C. A CloudWatch Dashboard widget combining both alarms
- D. An SNS filter policy filtering messages from both alarms

### Q2 Answer: B

### Q2 Analysis

A is incorrect. Anomaly Detection uses ML to establish a baseline band and alarm on deviations. It does not combine multiple alarms with logical conditions.

B is correct. A Composite Alarm evaluates the state of two or more child alarms using AND/OR/NOT logic. It fires only when the defined combination of child alarm states is met — in this case, both in ALARM simultaneously.

C is incorrect. Dashboards are visualization tools. They display alarm states but cannot suppress or combine alarm notifications.

D is incorrect. SNS filter policies filter messages based on message attributes. They cannot evaluate the state of multiple CloudWatch alarms.

---

## Question 3

A security team needs to investigate who deleted an S3 bucket in the production account yesterday. The account has CloudTrail enabled with a trail delivering to S3. Which CloudTrail event type must have been enabled to find this specific event?

- A. Data events for S3
- B. Management events (write)
- C. Insights events
- D. Network activity events

### Q3 Answer: B

### Q3 Analysis

A is incorrect. Data events capture object-level operations — GetObject, PutObject, DeleteObject — not bucket-level control plane operations. Deleting a bucket is a control-plane action.

B is correct. `DeleteBucket` is a management event (write category). Management events are recorded by default when a trail is created. Deleting a bucket is a control-plane action and is captured under management events.

C is incorrect. Insights events detect unusual API call patterns but do not record individual API calls. They cannot be used to identify the specific identity that deleted the bucket.

D is incorrect. Network activity events (a newer CloudTrail capability for VPC traffic) are not relevant to bucket deletion.

---

## Question 4

A company uses AWS Config to enforce that all EBS volumes must be encrypted. A new EBS volume is created without encryption. Config marks the volume as NON_COMPLIANT. The team wants Config to automatically encrypt the volume without manual intervention. Which feature enables this?

- A. CloudWatch Events rule targeting a Lambda function
- B. Config rule with an automatic remediation action using an SSM Automation document
- C. AWS Trusted Advisor automated fix for the Fault Tolerance category
- D. CloudTrail Insights triggering an SNS notification

### Q4 Answer: B

### Q4 Analysis

A is incorrect. While a CloudWatch Events (EventBridge) rule could trigger remediation, this is not the native Config remediation mechanism. The question asks about Config-native automation.

B is correct. AWS Config rules support automatic remediation via SSM Automation documents. The managed remediation action `AWS-EnableEbsEncryptionByDefault` or a custom SSM document can be attached to the rule to automatically remediate non-compliant resources.

C is incorrect. Trusted Advisor is advisory. It identifies issues and recommends actions but does not automatically remediate resources.

D is incorrect. CloudTrail Insights detects unusual API call patterns and publishes Insights events. It does not trigger resource remediation.

---

## Question 5

A developer needs to trace a slow API request through API Gateway, Lambda, and DynamoDB. The request is taking 4 seconds but the Lambda function itself executes in under 200 ms. Which AWS service and feature would MOST efficiently identify where the 4 seconds are being spent?

- A. CloudWatch Logs Insights query on the API Gateway access logs
- B. CloudTrail management event inspection for the API call
- C. AWS X-Ray service map and trace details with Active Tracing enabled
- D. CloudWatch Metric Math computing the sum of API Gateway and Lambda Duration metrics

### Q5 Answer: C

### Q5 Analysis

A is incorrect. CloudWatch Logs Insights can show per-request latency from access logs but does not break down latency into individual service segments within a request.

B is incorrect. CloudTrail records the API call event but does not measure per-segment latency within the request flow.

C is correct. X-Ray traces the end-to-end request across API Gateway, Lambda, and DynamoDB. The service map shows latency at each hop. Trace detail shows the exact subsegment durations — identifying whether the delay is in the API Gateway integration, Lambda initialization, the Lambda handler, or the DynamoDB call.

D is incorrect. Metric Math can combine metrics but these are aggregate metrics across all requests. It cannot isolate where latency occurs within a single specific slow request.

---

## Question 6

A company requires that all SSH access to EC2 instances be logged and that no inbound port 22 be open in any security group. The instances run Amazon Linux 2 and have the SSM Agent installed. Which AWS service enables this without opening port 22?

- A. EC2 Instance Connect with port 22 restricted to AWS IP ranges
- B. AWS Systems Manager Session Manager
- C. AWS Direct Connect with private VIF routing
- D. AWS VPN with an internal bastion host

### Q6 Answer: B

### Q6 Analysis

A is incorrect. EC2 Instance Connect still requires port 22 to be open to AWS IP ranges. The question specifies no port 22 open at all.

B is correct. Session Manager connects to instances through the SSM Agent over outbound HTTPS (port 443). No inbound ports are required. All session activity is logged to CloudWatch Logs and S3 for audit.

C is incorrect. Direct Connect is a dedicated network connection between on-premises and AWS. It does not provide shell access to instances or eliminate the need for port 22.

D is incorrect. A bastion host still requires port 22 to be open from the bastion to target instances. This does not satisfy the no-port-22 requirement.

---

## Question 7

A Lambda function processes financial transactions. The operations team wants to receive an alert whenever the application logs the string `TRANSACTION_FAILED` more than 5 times in a 1-minute window. The Lambda function writes structured logs to CloudWatch Logs. Which approach correctly implements this alerting?

- A. Enable detailed monitoring on the Lambda function and set a threshold alarm on the Errors metric
- B. Create a CloudWatch Logs metric filter matching `TRANSACTION_FAILED`, publish a custom metric, and create a CloudWatch Alarm on that metric
- C. Create a CloudWatch Logs subscription filter delivering logs to SNS
- D. Enable X-Ray Active Tracing and set an alarm on the X-Ray fault rate metric

### Q7 Answer: B

### Q7 Analysis

A is incorrect. The Lambda `Errors` metric counts unhandled exceptions that cause function execution failure. `TRANSACTION_FAILED` is a handled application log event — the function does not throw an exception, so the Errors metric does not increment.

B is correct. A metric filter extracts a CloudWatch metric from matching log events. Setting a filter pattern of `TRANSACTION_FAILED` publishes a count metric. A CloudWatch Alarm on this metric alerts when the count exceeds 5 within 1 minute.

C is incorrect. A subscription filter routes log events to a destination (Kinesis, Lambda, Firehose) for processing but does not directly create a CloudWatch metric or alarm.

D is incorrect. X-Ray fault rates reflect HTTP 5xx and Lambda execution errors, not application-level log strings. `TRANSACTION_FAILED` in a log line is not captured by X-Ray fault tracking.

---

## Question 8

A company's AWS account has CloudTrail enabled. The security team wants to ensure that CloudTrail log files have not been tampered with or deleted after delivery to S3. Which CloudTrail feature provides this assurance?

- A. CloudTrail Insights
- B. S3 Object Lock on the CloudTrail bucket
- C. CloudTrail log file integrity validation
- D. CloudWatch Logs subscription filter monitoring the CloudTrail log group

### Q8 Answer: C

### Q8 Analysis

A is incorrect. CloudTrail Insights detects unusual API call patterns. It does not validate whether log files have been tampered with.

B is incorrect. S3 Object Lock prevents deletion or overwriting of objects for a retention period. It protects against future tampering but does not provide cryptographic proof of integrity for files already delivered.

C is correct. CloudTrail log file integrity validation creates a SHA-256 hash digest file that chains all log file hashes. Using `aws cloudtrail validate-logs`, you can cryptographically verify that log files were not modified or deleted after delivery.

D is incorrect. Monitoring a CloudWatch Logs subscription filter can detect missing deliveries but cannot cryptographically verify the integrity of individual log file contents.

---

## Question 9

An AWS account has AWS Config enabled. A solutions architect wants to know which configuration state a specific EC2 security group was in last Tuesday at 2 PM — before a production incident. Which feature provides this information?

- A. CloudTrail Event History filtered by `AuthorizeSecurityGroupIngress`
- B. AWS Config resource timeline for the security group
- C. CloudWatch Logs Insights query on VPC Flow Logs
- D. EC2 console Security Groups change log

### Q9 Answer: B

### Q9 Analysis

A is incorrect. CloudTrail Event History shows the API call that made the change — the who and when — but does not show the complete configuration state of the security group at a specific point in time.

B is correct. AWS Config maintains a configuration timeline for each recorded resource. You can navigate the timeline to the exact date and time and view the complete configuration item — all inbound and outbound rules — as they existed at that moment.

C is incorrect. VPC Flow Logs capture network traffic flow records (source/destination IP, port, protocol, bytes, accept/reject). They do not record security group configuration state.

D is incorrect. The EC2 console does not maintain a change log of security group configuration history.

---

## Question 10

Which AWS Trusted Advisor check is available to ALL support plan levels (Basic and Developer) at no charge?

- A. Low-utilization Amazon EC2 instances
- B. Underutilized Amazon EBS volumes
- C. Security groups with unrestricted access (0.0.0.0/0) on specific high-risk ports
- D. Amazon RDS idle DB instances

### Q10 Answer: C

### Q10 Analysis

A is incorrect. The low-utilization EC2 instances check (Cost Optimization category) requires Business or Enterprise support.

B is incorrect. The underutilized EBS volumes check requires Business or Enterprise support.

C is correct. Core security checks — including the security groups with unrestricted access check — are available to all support plans including free Basic and Developer support. Other free checks include MFA on root account, S3 bucket permissions, and service limit warnings.

D is incorrect. The RDS idle DB instances check (Cost Optimization) requires Business or Enterprise support.

---

### Question 11 (5 points)

A company wants to receive an alert whenever more than 5 failed SSH login attempts occur on any EC2 instance within a 10-minute window. The instances run Amazon Linux 2 and write auth logs to `/var/log/secure`. Which combination of services implements this?

A. VPC Flow Logs → CloudWatch alarm on Rejected packets

B. CloudWatch Agent → CloudWatch Logs → Metric Filter → CloudWatch Alarm → SNS

C. AWS Config → Config Rule → EventBridge → SNS

D. CloudTrail → CloudWatch Logs → Metric Filter → CloudWatch Alarm → SNS

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. VPC Flow Logs record network-level ACCEPT/REJECT decisions based on security group and NACL rules — they do not parse application-level log content such as SSH authentication failures recorded in `/var/log/secure`.
- B is correct. The CloudWatch Agent streams `/var/log/secure` to CloudWatch Logs. A metric filter pattern matching SSH failure messages (e.g., `"Failed password"`) creates a custom metric. A CloudWatch alarm triggers on that metric when the count exceeds 5 in 10 minutes, then notifies via SNS. This is the correct end-to-end pipeline for application log alerting.
- C is incorrect. AWS Config records resource configuration state — it does not process OS-level log content or detect authentication events inside instances.
- D is incorrect. CloudTrail records AWS API calls (control plane events). SSH authentication failures are OS-level events that never appear in CloudTrail — CloudTrail has no visibility into what happens inside an instance's operating system.

---

### Question 12 (5 points)

A CloudWatch alarm monitors the `CPUUtilization` metric for an Auto Scaling group. The alarm is in `INSUFFICIENT_DATA` state. What is the most likely explanation?

A. The EC2 instances in the group have been terminated and no data has been reported recently

B. The alarm threshold is set too high and has never been crossed

C. The alarm is currently in a period where CPU utilization is exactly at the threshold

D. Auto Scaling groups do not support CloudWatch alarms

**Correct Answer: A**

**Distractor Analysis:**

- A is correct. `INSUFFICIENT_DATA` means CloudWatch has not received enough data points to evaluate the alarm condition. This happens when no metric data has been reported recently — for example, when all instances in the Auto Scaling group have been terminated, or immediately after creating an alarm before data arrives.
- B is incorrect. If the threshold has never been crossed, the alarm would be in `OK` state (assuming data is being received). `INSUFFICIENT_DATA` is specifically about missing data, not about the threshold level.
- C is incorrect. An alarm evaluating data at exactly the threshold would transition to `ALARM` or `OK` depending on the comparison operator — not `INSUFFICIENT_DATA`. That state reflects missing data, not borderline data.
- D is incorrect. CloudWatch alarms are frequently used with Auto Scaling groups as the trigger mechanism for scaling policies. This is a core AWS architectural pattern.

---

### Question 13 (5 points)

An operations team wants to use CloudWatch Logs Insights to find the top 10 Lambda functions by error count over the last 24 hours across all Lambda log groups. Which Logs Insights feature makes this possible without querying each log group separately?

A. CloudWatch cross-account observability with a linked source account

B. CloudWatch Logs Insights query with a log group pattern or log group prefix covering all Lambda log groups

C. AWS X-Ray service map filtered by error rate

D. CloudWatch Container Insights with Lambda function dimension

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Cross-account observability links accounts so a monitoring account can query multiple source accounts — it addresses multi-account scenarios, not multi-log-group queries within a single account.
- B is correct. CloudWatch Logs Insights supports querying multiple log groups simultaneously by specifying a log group prefix (e.g., `/aws/lambda/`) or a list of log group names. A single query can scan all Lambda log groups matching the prefix and aggregate results, including `stats count(*) by @logStream` to identify the top error-generating functions.
- C is incorrect. AWS X-Ray service maps visualize service dependencies and latency/error rates for traced requests, but they require X-Ray instrumentation on each function and do not provide log-level error count aggregation across all functions.
- D is incorrect. CloudWatch Container Insights is designed for containerized workloads (ECS, EKS) — it does not apply to Lambda functions.

---

### Question 14 (5 points)

A developer enables AWS X-Ray on a Lambda function. The X-Ray service map shows a high percentage of `Fault` (5xx) errors on a downstream DynamoDB call. Which X-Ray feature would help the developer identify the exact DynamoDB table, operation type, and error message for the failing requests?

A. X-Ray sampling rules — increase the sampling rate to capture more traces

B. X-Ray groups — create a group filtering on `fault = true` and review the traces within it

C. X-Ray annotations — add custom annotations to the DynamoDB subsegment

D. X-Ray trace segments — drill into individual trace details showing the DynamoDB subsegment attributes

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect. Sampling rules control what percentage of requests generate traces — increasing sampling captures more data volume but does not by itself reveal the error details. The error details are already in the existing traces.
- B is incorrect. X-Ray groups filter the service map and trace list to a subset matching a filter expression — they help locate the affected traces but do not themselves reveal the DynamoDB operation details.
- C is incorrect. X-Ray annotations are custom key-value pairs added by the developer to segments for indexing and filtering. They would need to be added before the problem is captured — they are not retroactively available in existing traces.
- D is correct. X-Ray trace details show the full segment and subsegment tree for a single request. The DynamoDB subsegment includes the table name, operation (e.g., `PutItem`), HTTP status code, and error cause. Drilling into an individual fault trace's DynamoDB subsegment directly reveals the information needed to diagnose the error.

---

### Question 15 (5 points)

A security auditor requires proof that no IAM policies were modified in the production account over the past 6 months. CloudTrail was enabled but no trail was configured to deliver logs to S3. Where can the auditor find IAM API call records going back 6 months?

A. CloudTrail Event History in the console — it retains 90 days of management events

B. CloudWatch Logs — CloudTrail automatically streams all events to CloudWatch Logs for 6 months

C. AWS Config configuration timeline — it records all IAM policy changes with timestamps

D. There is no AWS-managed record beyond 90 days without a configured trail delivering to S3

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect. CloudTrail Event History retains the last 90 days of management events — not 6 months (180 days). The auditor cannot retrieve records beyond 90 days from Event History alone.
- B is incorrect. CloudTrail does not automatically stream to CloudWatch Logs. A trail must be explicitly configured to deliver to CloudWatch Logs, and that configuration was not in place here.
- C is incorrect. AWS Config records configuration state changes for supported resources — including IAM policies — but only if Config was enabled and recording. The question states only CloudTrail was enabled; Config is not mentioned. Even if Config were enabled, it records what changed, not who called the API with full request context.
- D is correct. Without a configured CloudTrail trail delivering to S3 or CloudWatch Logs, records beyond the 90-day Event History window are not retained by AWS. The auditor cannot retrieve 6-month-old IAM API records. This is why AWS recommends enabling a multi-region trail with S3 delivery from account inception.

---

### Question 16 (5 points)

A company wants to use AWS Systems Manager Session Manager to replace SSH bastion hosts for EC2 access. Which prerequisite must be met on the EC2 instances?

A. Instances must have port 22 open in their security group to the Systems Manager service endpoints

B. Instances must have the SSM Agent installed and an IAM instance profile with the `AmazonSSMManagedInstanceCore` policy attached

C. Instances must be in a public subnet with a public IP address so Session Manager can reach them

D. Instances must have the CloudWatch Agent installed and streaming logs before Session Manager can be enabled

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Session Manager operates over HTTPS (port 443) to the SSM service endpoints — it does not require port 22. In fact, the primary benefit of Session Manager is eliminating the need for any inbound ports, including SSH.
- B is correct. Session Manager requires two things: the SSM Agent (pre-installed on Amazon Linux 2, Windows Server 2019+, and Ubuntu 20.04+) and an IAM instance profile granting the instance permission to communicate with the SSM service. The `AmazonSSMManagedInstanceCore` managed policy provides the minimum required permissions.
- C is incorrect. Session Manager works with instances in private subnets — the SSM Agent initiates outbound HTTPS connections to the SSM regional endpoint. No inbound connectivity or public IP is required (though VPC endpoints for SSM improve reliability in fully private environments).
- D is incorrect. The CloudWatch Agent and Session Manager are independent features. Installing the CloudWatch Agent is not a prerequisite for Session Manager access.

---

### Question 17 (5 points)

An architect designs a monitoring solution for a multi-tier application. The requirement states: "Alert only when BOTH the application error rate exceeds 5% AND the database connection pool is exhausted simultaneously — not when either condition occurs alone." Which CloudWatch feature implements this exact logic?

A. A single CloudWatch alarm with two metric conditions joined by AND in the threshold expression

B. A CloudWatch Composite Alarm combining two child alarms with an AND condition

C. Two separate CloudWatch alarms each connected to the same SNS topic

D. A CloudWatch Metric Math expression that multiplies the two metric values together

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Standard CloudWatch alarms evaluate a single metric against a threshold — they do not support AND/OR logic across multiple metrics natively within a single alarm.
- B is correct. CloudWatch Composite Alarms evaluate the alarm states of multiple child alarms using Boolean logic (AND, OR, NOT). Configuring `ALARM("error-rate-alarm") AND ALARM("db-pool-alarm")` triggers the composite alarm only when both child alarms are simultaneously in ALARM state — exactly matching the requirement.
- C is incorrect. Two alarms connected to the same SNS topic will each fire notifications independently when their individual conditions are met. This implements OR logic (either one triggers), not AND logic.
- D is incorrect. Metric Math creates calculated metrics (e.g., error rate percentage from raw counts) but does not implement alarm state logic. A Metric Math result still requires a standard alarm that can only evaluate one threshold at a time.

---

### Question 18 (5 points)

A company needs to automatically rotate their RDS database password every 30 days and update all applications that use it without any downtime. Which AWS service handles this with built-in RDS integration?

A. AWS Systems Manager Parameter Store with an EventBridge scheduled rule triggering a Lambda rotation function

B. AWS Secrets Manager with automatic rotation enabled and the RDS rotation Lambda function

C. AWS KMS with automatic key rotation set to 30 days for the RDS master password

D. AWS Config with a Config rule that detects passwords older than 30 days and triggers an SSM Automation runbook

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. Parameter Store does not have built-in automatic rotation capability. While you could build a rotation solution using EventBridge and Lambda, this requires custom code and does not have native RDS integration.
- B is correct. AWS Secrets Manager has native integration with Amazon RDS. When automatic rotation is enabled, Secrets Manager uses an AWS-provided Lambda rotation function that creates a new password, updates it in RDS, and updates the secret — all without application downtime. Applications retrieve the current password from Secrets Manager at runtime, so they automatically use the new password after rotation.
- C is incorrect. AWS KMS key rotation rotates the encryption key material for KMS Customer Managed Keys — it has nothing to do with RDS database user passwords or application credentials.
- D is incorrect. AWS Config evaluates resource compliance state — it does not have the capability to change database passwords or orchestrate credential rotation workflows.

---

### Question 19 (5 points)

A DevOps team needs to run a patching script on 500 EC2 instances in a maintenance window without SSH access. The instances are in private subnets. Which AWS service and feature handles this?

A. AWS OpsWorks with Chef or Puppet recipes executed during the maintenance window

B. AWS Systems Manager Run Command with the `AWS-RunShellScript` document targeting the instance fleet

C. AWS Lambda invoked by EventBridge Scheduler, deploying to EC2 instances via the EC2 user data mechanism

D. AWS CodeDeploy deployment group targeting the instance fleet with an in-place deployment

**Correct Answer: B**

**Distractor Analysis:**

- A is incorrect. OpsWorks is a configuration management service for Chef and Puppet. While it can run scripts, it requires OpsWorks agent installation and stack configuration — adding significant setup complexity for a patching use case that SSM Run Command handles natively.
- B is correct. Systems Manager Run Command executes scripts on managed instances (those with SSM Agent and the required IAM profile) without requiring SSH or open inbound ports. Targeting all 500 instances is straightforward using tags or instance IDs. The `AWS-RunShellScript` document runs arbitrary shell commands, and the results stream back to the SSM console and CloudWatch Logs.
- C is incorrect. EC2 user data runs only at instance launch — it cannot be triggered for already-running instances during a maintenance window. Lambda also cannot directly execute code on EC2 instances.
- D is incorrect. CodeDeploy is an application deployment service that requires a deployment package (appspec.yml and application artifacts). It is not designed for arbitrary patch scripts and requires the CodeDeploy agent, adding overhead beyond what Run Command needs.

---

### Question 20 (5 points)

A company wants to ensure their AWS environment continuously complies with the CIS AWS Foundations Benchmark. They need automated detection when a resource drifts from the benchmark — for example, when S3 bucket logging is disabled or an IAM password policy does not meet minimum length requirements. Which AWS service provides this continuous automated evaluation?

A. AWS Trusted Advisor with Business support — it checks CIS benchmark controls continuously

B. Amazon Inspector — it scans EC2 instances against the CIS benchmark on a schedule

C. AWS Config Conformance Pack with the CIS AWS Foundations Benchmark conformance pack

D. AWS Security Hub with the CIS AWS Foundations Benchmark standard enabled

**Correct Answer: D**

**Distractor Analysis:**

- A is incorrect. Trusted Advisor provides best-practice checks in cost, performance, security, and fault tolerance categories, but it does not evaluate against the full CIS AWS Foundations Benchmark or provide continuous compliance tracking against a named standard.
- B is incorrect. Amazon Inspector scans EC2 instances and container images for software vulnerabilities (CVEs) and network reachability issues. It does not evaluate AWS resource configurations against CIS benchmark controls such as S3 logging settings or IAM password policies.
- C is partially correct — AWS Config Conformance Packs can deploy CIS benchmark rules. However, Security Hub is more appropriate because it aggregates findings from Config, GuardDuty, Inspector, and others into a unified compliance score with a CIS standard dashboard, providing a more complete continuous compliance view.
- D is correct. AWS Security Hub with the CIS AWS Foundations Benchmark standard enabled continuously evaluates AWS account and resource configurations against all CIS controls, generates findings for non-compliant resources, and provides an overall compliance score — directly meeting the requirement for automated continuous benchmark compliance tracking.

---

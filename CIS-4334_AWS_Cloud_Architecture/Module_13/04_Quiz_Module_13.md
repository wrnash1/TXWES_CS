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

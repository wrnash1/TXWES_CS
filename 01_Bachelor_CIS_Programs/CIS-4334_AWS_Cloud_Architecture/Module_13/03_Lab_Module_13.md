# Lab: Module 13 — CloudWatch Alarms, Logs Insights, and CloudTrail Audit

## Course: CIS-4334 AWS Cloud Architecture

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** AWS Solutions Architect — Associate (SAA-C03)

---

## Lab Overview

In this lab you configure operational visibility for a Lambda function. You create a CloudWatch Alarm on the Lambda error metric linked to an SNS email notification, write a metric filter to count application errors from Lambda logs, run a Logs Insights query to analyze latency distribution, and query CloudTrail Event History to investigate a simulated security group change. You also verify that AWS Config has recorded the security group configuration history.

**Estimated Time:** 75 minutes

**AWS Services Used:** Lambda, CloudWatch (Metrics, Alarms, Logs, Logs Insights), SNS, CloudTrail, AWS Config, IAM

**Cost Estimate:** Under $0.50. All services used fall within Free Tier limits for this lab scope.

---

## Prerequisites

- AWS account with console access
- Module 12 lab completed (reuse `order-intake-fn`) or create a new test Lambda function
- An email address you can access to confirm SNS subscription

---

## Part 1: Create a Test Lambda Function

If you did not complete Module 12, create a simple Lambda function for this lab.

### Step 1.1

1. Open the Lambda console → **Create function**.
2. Name: `monitoring-test-fn`
3. Runtime: Python 3.12
4. Role: Create a new role with basic Lambda permissions.
5. Replace the code with:

```python
import json
import random
import time

def lambda_handler(event, context):
    action = event.get('action', 'success')

    if action == 'error':
        raise ValueError("Simulated application error")

    if action == 'slow':
        time.sleep(2)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'success', 'action': action})
    }
```

1. Deploy.

### Step 1.2 — Generate Test Invocations

Create a test event named `ErrorEvent` with this payload:

```json
{ "action": "error" }
```

Run the test 5 times to generate error records in CloudWatch Logs and Metrics.

Create a second test event named `SuccessEvent`:

```json
{ "action": "success" }
```

Run the success event 10 times.

---

## Part 2: CloudWatch Alarm on Lambda Errors

### Step 2.1 — Create SNS Topic

1. Open SNS → **Create topic → Standard**.
2. Name: `lab13-alerts`
3. Create. Copy the **Topic ARN**.

### Step 2.2 — Email Subscription

1. Open `lab13-alerts` → **Create subscription**.
2. Protocol: Email, your address.
3. Create and confirm via the confirmation email.

### Step 2.3 — Create the CloudWatch Alarm

1. Open CloudWatch → **Alarms → Create alarm**.
2. Choose **Select metric → Lambda → By Function Name**.
3. Find your function and select the **Errors** metric.
4. Choose **Select metric**.
5. Configure the alarm:

   - Period: 1 minute
   - Threshold type: Static
   - Condition: Greater than or equal to 2
   - Datapoints to alarm: 1 out of 1

6. Under **Notification**, select **In alarm → Send notification to: lab13-alerts**.
7. Name the alarm: `Lambda-ErrorRate-Alarm`
8. Create the alarm.

### Step 2.4 — Trigger the Alarm

Run the `ErrorEvent` test 3 more times in rapid succession. Wait up to 2 minutes. Verify:

- The alarm transitions to ALARM state in the CloudWatch console
- You receive an email notification from SNS

Record the time the alarm entered ALARM state.

---

## Part 3: Metric Filter on Application Logs

### Step 3.1 — Locate the Log Group

1. Open CloudWatch → **Log groups**.
2. Find `/aws/lambda/monitoring-test-fn` (or your function's log group).

### Step 3.2 — Create a Metric Filter

1. Open the log group → **Metric filters → Create metric filter**.
2. Filter pattern: `[ERROR]`
3. Choose **Test pattern** and verify it matches your error log lines.
4. Choose **Next** and configure:

   - Filter name: `ApplicationErrors`
   - Metric namespace: `LabMetrics`
   - Metric name: `ApplicationErrorCount`
   - Metric value: `1`
   - Default value: `0`

5. Create the filter.

### Step 3.3 — Verify the Metric

1. Open CloudWatch → **Metrics → All metrics → Custom namespaces → LabMetrics**.
2. Confirm `ApplicationErrorCount` is present.
3. Select the metric and view the graph. Confirm it reflects the number of error invocations you triggered.

---

## Part 4: CloudWatch Logs Insights

### Step 4.1 — Latency Distribution Query

1. Open CloudWatch → **Logs Insights**.
2. Select the log group `/aws/lambda/monitoring-test-fn`.
3. Set the time range to the last 1 hour.
4. Paste this query:

```text
fields @timestamp, @duration, @billedDuration, @memorySize
| filter @type = "REPORT"
| stats
    count() as invocations,
    avg(@duration) as avg_ms,
    max(@duration) as max_ms,
    pct(@duration, 95) as p95_ms,
    pct(@duration, 99) as p99_ms
  by bin(5m)
| sort @timestamp desc
```

1. Run. Note the p95 and p99 values.

### Step 4.2 — Error Isolation Query

Run a second query to list only the error invocations:

```text
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20
```

Note the exact error messages and timestamps from your simulated errors.

### Step 4.3 — Cold Start Detection Query

```text
fields @timestamp, @initDuration, @duration
| filter @type = "REPORT" and ispresent(@initDuration)
| sort @initDuration desc
| limit 10
```

If you see results, a cold start occurred. Note the `@initDuration` values. If no results appear, trigger another invocation after waiting 15 minutes for the execution environment to expire.

---

## Part 5: CloudTrail Security Group Audit

### Step 5.1 — Make a Security Group Change

1. Open the EC2 console → **Security Groups**.
2. Select the default VPC security group (or any security group).
3. Choose **Edit inbound rules → Add rule**.
4. Add: Type = All traffic, Source = 0.0.0.0/0 (intentionally insecure for simulation only).
5. Save the rule.

### Step 5.2 — Query CloudTrail Event History

1. Open CloudTrail → **Event History**.
2. Filter by **Event name**: `AuthorizeSecurityGroupIngress`.
3. Find the event corresponding to your change.
4. Open the event and examine:

   - `userIdentity.arn` — which IAM identity made the change
   - `sourceIPAddress` — the IP address of the API caller
   - `eventTime` — when the change was made
   - `requestParameters` — the specific security group rule that was added

Record all four fields in your lab document.

### Step 5.3 — Revert the Change

Return to the security group and remove the 0.0.0.0/0 inbound rule you added.

---

## Part 6: AWS Config Configuration History

### Step 6.1 — Verify Config is Enabled

1. Open AWS Config → **Dashboard**.
2. If Config is not enabled, choose **Get started** and enable recording for all resource types (use the default IAM role).

Note: Config may take up to 10 minutes to record the security group change.

### Step 6.2 — View Security Group History

1. Open AWS Config → **Resources → EC2 SecurityGroup**.
2. Locate the security group you modified.
3. Choose **Resource timeline**.
4. Identify the two configuration items — before and after your change.
5. Click the AFTER configuration item and expand the `ipPermissions` field.
6. Confirm the 0.0.0.0/0 rule appears in the recorded configuration state.
7. Click the BEFORE item and confirm the rule is absent.

Record in your lab document: what is the difference between what CloudTrail recorded and what AWS Config recorded for the same change?

---

## Part 7: Composite Alarm (Stretch Goal)

If time permits, create a second alarm on the Lambda `Duration` metric (threshold: p95 duration > 1,500 ms). Then create a Composite Alarm combining your `Lambda-ErrorRate-Alarm` AND the Duration alarm with an AND condition. Observe that the composite alarm only enters ALARM state when both child alarms are in ALARM state simultaneously.

---

## Reflection Questions

Answer these questions in your lab submission document:

1. What is the difference between a CloudWatch Alarm on the Lambda `Errors` metric and the metric filter you created on the log group? Under what circumstances would you need the metric filter approach in addition to the native Lambda metric?

2. Your CloudTrail query showed `sourceIPAddress` for the security group change. Why is this field important from a security investigation perspective, and what IAM service would you check next if the IP address was unexpected?

3. AWS Config recorded the security group's configuration state. CloudTrail recorded the API call that caused the change. Describe a compliance investigation where you would need BOTH services — what question does each answer that the other cannot?

4. You triggered a CloudWatch Alarm that sent an SNS email. In a production environment, what would be a more operationally useful action to trigger from this alarm in addition to email notification?

---

## Cleanup

1. Delete the CloudWatch alarm: `Lambda-ErrorRate-Alarm`
2. Delete the metric filter `ApplicationErrors` from the log group
3. Delete the SNS topic `lab13-alerts`
4. Delete the Lambda function `monitoring-test-fn`
5. Remove the CloudWatch log group `/aws/lambda/monitoring-test-fn`
6. Optionally disable AWS Config recording to avoid ongoing charges (Config charges per configuration item recorded)

---

## Submission Checklist

- Screenshot of `Lambda-ErrorRate-Alarm` in ALARM state
- Screenshot of the SNS confirmation email received
- Screenshot of the Logs Insights latency query results showing p95 and p99
- Screenshot of the CloudTrail event for `AuthorizeSecurityGroupIngress` with userIdentity, sourceIPAddress, eventTime, and requestParameters visible
- Screenshot of the AWS Config resource timeline showing before/after states for the security group
- Written answers to all four reflection questions

---

## Part 9 — Challenge Exercise

### Challenge 1: CloudWatch Logs Insights Advanced Querying
Practice writing multi-step Logs Insights queries to extract operational intelligence from Lambda and application logs.
1. Navigate to CloudWatch Logs Insights and select the `/aws/lambda/` log group prefix (or a specific Lambda log group from the lab). Run a query that counts errors by error type over the last 24 hours: `filter @message like /ERROR/ | parse @message "* ERROR *: *" as timestamp, level, errorMsg | stats count(*) as errorCount by errorMsg | sort errorCount desc | limit 10`.
2. Write a query that calculates p50, p90, p99 latency percentiles from Lambda `REPORT` lines: `filter @type = "REPORT" | parse @message "Duration: * ms" as duration | stats pct(duration, 50) as p50, pct(duration, 90) as p90, pct(duration, 99) as p99 by bin(5m)`. Run it and screenshot the results table.
3. Create a saved query from one of the above queries using the "Save" button in Logs Insights. Confirm the saved query appears in the "Saved queries" panel. Document the query name and the log group it targets.
4. Export the query results to CloudWatch dashboard: choose "Add to dashboard" from the Logs Insights results and create a new widget on an existing or new dashboard. Screenshot the dashboard widget displaying the query results.

### Challenge 2: CloudWatch Anomaly Detection
Configure CloudWatch anomaly detection on a metric to alert on unusual patterns rather than fixed thresholds.
1. Choose a metric that has at least a few hours of data — Lambda `Duration`, EC2 `CPUUtilization`, or SQS `NumberOfMessagesSent`. Create an anomaly detection band on it: in the CloudWatch console, select the metric, choose "Add anomaly detection" and set the standard deviation band to 2. Allow 15 minutes for the model to train.
2. Create a CloudWatch alarm based on the anomaly detection band: the alarm fires when the metric is outside the predicted band. Configure the alarm to notify the SNS topic from the lab (`lab13-alerts`). Document the alarm ARN: `aws cloudwatch describe-alarms --alarm-names <alarm-name> --query "MetricAlarms[0].AlarmArn"`.
3. Examine the anomaly detection model configuration via CLI: `aws cloudwatch describe-anomaly-detectors --metric-name <metric-name> --namespace <namespace>`. Record the `Stat`, `Dimensions`, and `ExcludedTimeRanges` fields.
4. Explain one scenario where anomaly detection-based alerting is superior to a fixed threshold alarm, and one scenario where a fixed threshold alarm is more appropriate. Reference a specific AWS workload type for each.

### Reflection Questions
1. After completing Challenge 1, explain how CloudWatch Logs Insights query-based dashboards differ from metric-based dashboards in terms of data freshness, cost, and use cases. When would you choose a Logs Insights widget over a CloudWatch metric widget for an operations dashboard, and what is the trade-off in query execution cost at high dashboard refresh rates?
2. Based on Challenge 2, explain how CloudWatch anomaly detection addresses the challenge of setting meaningful alert thresholds for metrics with natural seasonality (e.g., traffic that peaks every weekday morning and drops on weekends). How does this relate to the AWS Well-Architected Framework Operational Excellence pillar principle of "anticipating failure" rather than simply reacting to it?

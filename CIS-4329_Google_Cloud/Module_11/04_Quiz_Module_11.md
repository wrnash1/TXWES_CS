# Quiz: Module 11 – Cloud Monitoring, Logging, and Alerting
## Course: CIS-4329 – Google Cloud Administration (Google Cloud Associate Cloud Engineer)

---

**Question 1**
Your company's compliance policy requires that all Cloud Audit Logs (Admin Activity and Data Access logs) be retained for 7 years. Cloud Logging's default retention is 30 days. What is the correct way to implement the 7-year retention requirement with minimal operational overhead?

A) Increase the Cloud Logging bucket retention period for the `_Default` bucket to 2,555 days in the Logs Storage settings.
B) Create a log sink that exports audit logs to a Cloud Storage bucket, then configure an Object Lifecycle rule on the bucket to delete objects after 7 years.
C) Write a daily Cloud Scheduler job that copies logs from Cloud Logging to BigQuery for long-term storage.
D) Enable Cloud Monitoring log-based metrics on audit log entries, which automatically archives the underlying log data for 7 years.

*   **Correct Answer:** B) Create a log sink that exports audit logs to a Cloud Storage bucket, then configure an Object Lifecycle rule on the bucket to delete objects after 7 years.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* The `_Default` log bucket maximum retention period is 3,650 days (10 years), so technically this could work — however, extending the default bucket retention does not give you cost-efficient long-term storage. Cloud Storage Archive class is far cheaper for logs that are rarely accessed, making a Cloud Storage sink the recommended pattern for compliance archival.
    *   *Why C is incorrect:* A Cloud Scheduler job that copies logs adds operational complexity (a script to maintain, error handling, IAM permissions for copying) and introduces a 24-hour gap in coverage for any logs written between runs. A log sink streams logs continuously in near real-time without any scheduled job to maintain.
    *   *Why D is incorrect:* Log-based metrics are counters derived from log entry patterns — they do not archive the underlying log data. Creating a log-based metric does not cause Cloud Logging to retain the source log entries for any longer than the bucket's retention policy specifies.

---

**Question 2**
You have deployed a web application on Compute Engine. You want to receive an email alert whenever the average CPU utilization across all VMs in the instance group exceeds 85% for more than 5 consecutive minutes. Which sequence of steps correctly configures this alerting?

A) Create a Cloud Logging log sink filtered on CPU metrics, then create a Pub/Sub topic that emails subscribers when messages arrive.
B) Create an email notification channel in Cloud Monitoring, then create an alerting policy with a metric condition on `compute.googleapis.com/instance/cpu/utilization` with a threshold of 0.85 and a duration of 5 minutes, referencing the notification channel.
C) Enable a Cloud Monitoring uptime check on the instance group's load balancer endpoint, and configure the uptime check to send an email if the response time exceeds a threshold.
D) Create a Cloud Function triggered by a Pub/Sub message that checks CPU metrics via the Cloud Monitoring API every 5 minutes and sends an email if the threshold is exceeded.

*   **Correct Answer:** B) Create an email notification channel in Cloud Monitoring, then create an alerting policy with a metric condition on `compute.googleapis.com/instance/cpu/utilization` with a threshold of 0.85 and a duration of 5 minutes, referencing the notification channel.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* CPU utilization is a Cloud Monitoring metric, not a log entry — it does not appear in Cloud Logging and cannot be captured by a log sink. Log sinks export log data, not time-series metrics. Alerting policies are the correct mechanism for metric-based alerts.
    *   *Why C is incorrect:* Uptime checks verify that an HTTP/HTTPS endpoint returns a successful response — they test external availability, not CPU utilization. An uptime check cannot measure or threshold internal VM CPU metrics.
    *   *Why D is incorrect:* Polling the Cloud Monitoring API from a Cloud Function every 5 minutes adds unnecessary complexity compared to the native alerting policy, introduces latency in detection (up to 5 minutes between polls), and requires maintaining a Cloud Function. Native alerting policies evaluate conditions continuously against the metric time series.

---

**Question 3**
A developer on your team is troubleshooting a Cloud Run service that is returning intermittent 500 errors. They need to find all log entries from the service in the last hour that have a severity of ERROR or higher. Which tool and query syntax should they use?

A) Cloud Monitoring Metrics Explorer — filter by `run.googleapis.com/request_count` and segment by response code.
B) Cloud Logging Logs Explorer — use the filter `resource.type="cloud_run_revision" AND severity>=ERROR` with the time range set to the last 1 hour.
C) Cloud Trace — search for traces with a latency above 500ms, which identifies requests that encountered errors.
D) BigQuery — run `SELECT * FROM cloudlogging.run_logs WHERE severity = 'ERROR'` to query the error logs table.

*   **Correct Answer:** B) Cloud Logging Logs Explorer — use the filter `resource.type="cloud_run_revision" AND severity>=ERROR` with the time range set to the last 1 hour.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* Metrics Explorer shows aggregated numeric metrics (like request count by response code) — it does not show individual log entries with their message text. To read the actual error messages and stack traces needed for debugging, the developer must use Logs Explorer.
    *   *Why C is incorrect:* Cloud Trace shows latency data and the call graph for individual requests. While a 500 error may correlate with high latency, Cloud Trace does not provide the error log messages, exception text, or stack traces needed to diagnose the root cause of the errors.
    *   *Why D is incorrect:* BigQuery can query logs if a log sink has been configured to export to BigQuery, but this requires advance setup and the log data is only available there if the sink was created before the errors occurred. Logs Explorer provides direct access to all Cloud Logging data without any prior export configuration.

---

**Question 4**
You are setting up monitoring for a multi-tier application. You want to be notified if the `/health` endpoint of your public-facing load balancer returns a non-200 response from any of Google's global probe locations. Which Cloud Monitoring feature implements this?

A) Create a log-based metric that counts HTTP 200 responses in the load balancer access logs and alert when the count drops to zero.
B) Configure an alerting policy on the `loadbalancing.googleapis.com/https/request_count` metric filtered by response code 200.
C) Create an uptime check targeting the load balancer's external IP address on the `/health` path, and attach an alerting policy that fires when the check fails.
D) Deploy a Cloud Function that sends an HTTP GET to `/health` every minute and publishes a Pub/Sub message if the response code is not 200.

*   **Correct Answer:** C) Create an uptime check targeting the load balancer's external IP address on the `/health` path, and attach an alerting policy that fires when the check fails.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A log-based metric counting 200 responses would alert when the count drops to zero — but this only fires after a sustained period with no successful requests, not immediately when the health endpoint starts failing. Uptime checks probe from multiple global locations every minute and alert within minutes of a failure.
    *   *Why B is incorrect:* Alerting on the `request_count` metric filtered to 200 responses measures actual user traffic — it will alert when user 200 responses drop, but only if users are actively sending requests. Uptime checks send their own synthetic probes regardless of user traffic volume, providing coverage even during off-peak hours with no real traffic.
    *   *Why D is incorrect:* A self-managed polling Cloud Function achieves the same goal but adds infrastructure to maintain (a Cloud Function, a Pub/Sub topic, a subscriber, retry logic). Cloud Monitoring uptime checks provide this capability natively with global probe locations and built-in alerting integration.

---

**Question 5**
Your security team wants to receive real-time alerts whenever any project administrator grants the `roles/owner` or `roles/editor` IAM role to any user in the production project. Cloud Audit Logs capture all IAM policy changes. Which combination of Cloud Logging and Cloud Monitoring features implements this with the least custom code?

A) Create a log sink to Pub/Sub filtered on `protoPayload.methodName="SetIamPolicy"`, then write a Cloud Function that parses the Pub/Sub message and sends an email if an Owner or Editor role is detected.
B) Create a log-based metric with a filter for `protoPayload.methodName="SetIamPolicy" AND (protoPayload.request.policy.bindings.role="roles/owner" OR protoPayload.request.policy.bindings.role="roles/editor")`, then create a Cloud Monitoring alerting policy on that metric with an email notification channel.
C) Enable Security Command Center and configure a finding notification for IAM misconfigurations, which automatically emails administrators when broad roles are granted.
D) Schedule a daily Cloud Scheduler job that runs `gcloud projects get-iam-policy` and sends a diff report by email if Owner or Editor bindings are present.

*   **Correct Answer:** B) Create a log-based metric with a filter for `protoPayload.methodName="SetIamPolicy"` and role conditions, then create a Cloud Monitoring alerting policy on that metric with an email notification channel.
*   **Distractor Analysis:**
    *   *Why A is incorrect:* A log sink to Pub/Sub combined with a Cloud Function is a valid approach but requires writing, deploying, and maintaining custom function code for message parsing and email delivery. The log-based metric plus native alerting policy achieves the same result entirely within Cloud Monitoring and Cloud Logging with no custom code.
    *   *Why C is incorrect:* Security Command Center's IAM finding notifications flag configurations that violate security best practices on a periodic scan basis — they are not real-time streaming alerts triggered by individual IAM change events. Response time can be hours rather than minutes.
    *   *Why D is incorrect:* A daily scheduled diff report introduces up to a 24-hour delay between when a privilege escalation occurs and when the team is notified. Real-time alerting via log-based metrics fires within minutes of the IAM change event being written to Cloud Audit Logs.

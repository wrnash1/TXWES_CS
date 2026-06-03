# Quiz: Module 13 - Azure Monitoring and Diagnostics

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)
**Questions:** 10 | **Points:** 10 (1 point each)

---

## Question 1

A DevOps team wants to receive an SMS notification when the CPU utilization of their production virtual machine exceeds 85% for more than 10 minutes. Which Azure Monitor components are required to implement this?

- A) An Application Insights instance and a Log Analytics workspace
- B) A metric alert rule with a condition and an action group configured with SMS notification
- C) A Log Analytics workspace with a KQL scheduled query and an email action
- D) Azure Service Health with a health advisory subscription

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* A metric alert rule monitors a specific metric (CPU utilization) against a threshold condition (> 85%) over a time window (10 minutes). When the condition is met, it triggers an action group. Action groups can be configured with SMS notifications. This is the purpose-built solution for threshold-based metric alerting with phone/SMS notification.
- *Why A is incorrect:* Application Insights is for application-level performance monitoring (requests, dependencies, exceptions), not for VM infrastructure metrics like CPU. A Log Analytics workspace is needed for log-based queries, not for real-time metric threshold alerts.
- *Why C is incorrect:* Log-based KQL queries are used for detecting patterns in log data (security events, application errors). CPU utilization is a metric, not a log event. Metric alerts are faster and more appropriate for real-time threshold conditions. Also, the scenario specifies SMS, not email.
- *Why D is incorrect:* Azure Service Health provides notifications about Azure infrastructure incidents (Azure's problems, not your application's problems). It does not monitor your VM's CPU utilization.

---

## Question 2

What is the difference between Azure Monitor Metrics and Azure Monitor Logs?

- A) Metrics are collected from applications only; Logs are collected from infrastructure only
- B) Metrics are numerical time-series data points collected frequently for real-time monitoring; Logs are event records with richer content queried using KQL for investigation and analysis
- C) Metrics require diagnostic settings to be configured; Logs are collected automatically from all resources
- D) Metrics are stored for 7 years by default; Logs are stored for only 24 hours

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Metrics are lightweight numerical time-series values (CPU %, bytes/sec, request count) collected frequently (typically every minute) and stored in a fast time-series database. Logs are richer event records (authentication events, resource changes, application traces) with more context but larger size, stored in Log Analytics workspaces and queried with KQL. They serve different operational purposes.
- *Why A is incorrect:* Both metrics and logs can come from applications or infrastructure. Application Insights collects both application metrics (request rate, response time) and application logs (traces, exceptions). Azure Monitor collects infrastructure metrics and infrastructure logs.
- *Why C is incorrect:* This is backwards. Platform metrics are collected automatically from Azure resources without configuration. Resource-level logs (like storage access logs or SQL audit logs) require diagnostic settings to be configured to route them to a destination.
- *Why D is incorrect:* The default retention for metrics is 93 days, not 7 years. Log Analytics workspace default retention is 30 days (configurable up to 2 years for an additional cost). Neither is 24 hours.

---

## Question 3

A security operations team needs to investigate a potential data exfiltration incident. They want to query the last 60 days of Azure Blob Storage access logs to identify all read operations performed by a specific service principal. Which service provides this capability?

- A) Azure Monitor Metrics with the Transactions metric filtered by identity
- B) Azure Service Health with compliance log access
- C) Log Analytics workspace with a KQL query on the StorageBlobLogs table
- D) Application Insights with dependency tracking filtered by caller identity

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Storage access logs (StorageBlobLogs) are written to a Log Analytics workspace when diagnostic settings are configured. KQL queries against this table can filter by identity, operation type, and time range to identify specific access patterns. This is exactly the investigation use case for Log Analytics — rich structured log data queried with KQL.
- *Why A is incorrect:* Azure Monitor Metrics track aggregate counts (total transactions, total ingress bytes) but do not store per-request details including which identity made the request. Metrics cannot answer "which service principal performed this read."
- *Why B is incorrect:* Azure Service Health provides notifications about Azure infrastructure incidents. It does not provide access to your storage account's access logs.
- *Why D is incorrect:* Application Insights dependency tracking monitors outbound calls FROM your application TO external services. It tracks your application's calls to storage, not all calls made to your storage account from any identity.

---

## Question 4

A company deploys Application Insights in their web application. A production incident is reported where users are experiencing slow page loads. Which Application Insights feature would most directly help identify which specific operation or dependency is causing the slowness?

- A) Live Metrics Stream — shows real-time request rate and failure count
- B) Application Map — shows the component topology with response time and failure indicators per component
- C) Availability tests — show synthetic probe results from multiple Azure regions
- D) Smart Detection — automatically alerts on unusual failure rates

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* The Application Map is a visual representation of how application components connect — web front end, database calls, calls to external APIs, background workers. Each component shows its request rate, average response time, and failure rate. During a slowness incident, the Application Map immediately reveals which component has elevated response times, pointing directly at the bottleneck (for example: the database dependency is taking 2 seconds when it normally takes 50ms).
- *Why A is incorrect:* Live Metrics shows real-time aggregate metrics (overall request rate, server resources). It confirms the problem is occurring but does not break down by component to show which operation is slow.
- *Why C is incorrect:* Availability tests are synthetic probes that detect whether the application is reachable and measures overall response time. They detect the symptom (slow pages) but do not show which internal component is causing the slowness.
- *Why D is incorrect:* Smart Detection fires alerts when anomalies are detected but is diagnostic in the sense of alerting, not investigating root cause. Once alerted, you would use the Application Map to investigate.

---

## Question 5

An organization has 15 Azure subscriptions. They want to be automatically notified when Azure publishes an incident that affects Azure SQL Database in the East US region — specifically for incidents that affect their resources, not general global incidents. Which service provides this capability?

- A) Azure Monitor metric alerts on SQL Database error rate
- B) Microsoft Sentinel with an analytics rule for SQL incidents
- C) Azure Service Health with a service health alert
- D) Log Analytics with a KQL query on the AzureActivity table

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Service Health provides personalized, subscription-specific notifications about Azure service incidents. You can create a Service Health alert that filters to specific services (Azure SQL Database), specific regions (East US), and specific event types (Service issues) — and triggers an action group to notify your team when a matching incident is published. This is the purpose-built service for "notify me when Azure has a problem affecting my resources."
- *Why A is incorrect:* A metric alert on SQL Database error rate monitors YOUR application's error rate, not Azure's service health. If Azure SQL itself has an outage, the error rate metric might increase, but the root cause is an Azure infrastructure event, not your configuration. Service Health provides the authoritative notification.
- *Why B is incorrect:* Microsoft Sentinel is a SIEM for security threat detection. It does not provide Azure infrastructure health event monitoring. Azure incidents are not security threats in the Sentinel context.
- *Why D is incorrect:* The AzureActivity table in Log Analytics captures control-plane events (who created/deleted/changed Azure resources). It does not capture Azure service health incidents published by Microsoft.

---

## Question 6

A Log Analytics workspace has the following KQL query:

```kql
AzureActivity
| where OperationName contains "delete"
| where ActivityStatusValue == "Failure"
| summarize count() by Caller, bin(TimeGenerated, 1h)
| order by count_ desc
```

What does this query do?

- A) Lists all Azure resources that were deleted in the last hour
- B) Shows the number of failed delete operations per user per hour, ordered from most to least failures
- C) Deletes all Azure Activity log entries older than one hour
- D) Counts the total number of Azure resources and groups them by creation time

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Reading the query pipe by pipe: (1) query the AzureActivity table; (2) filter to operations containing "delete"; (3) filter to failed operations (ActivityStatusValue == "Failure"); (4) count the results grouped by Caller (the user/identity) and binned into 1-hour time buckets; (5) order the results with the most failures at the top. This shows which users had the most failed delete attempts, which could indicate permission issues or an investigation target.
- *Why A is incorrect:* The query filters to ActivityStatusValue == "Failure" — it only shows FAILED delete attempts, not successful ones. Also, it does not list the resource names; it summarizes counts by Caller.
- *Why C is incorrect:* KQL is a read-only query language. It cannot delete or modify data. "Delete" in the query refers to Azure operations containing the word "delete" in the OperationName field — it is filtering log data about deletion operations, not deleting log entries.
- *Why D is incorrect:* This query has nothing to do with resource counts or creation times. It queries the Activity log for delete operations, filters by failure status, and counts by user.

---

## Question 7

An action group is created and attached to an Azure Alerts rule. The alert fires at 2:00 AM when a VM's disk reaches 95% full. The action group contains: an email to ops@company.com, an SMS to the on-call engineer's phone, and a webhook to PagerDuty. What happens when the alert fires?

- A) Azure randomly selects one of the three actions to execute
- B) Azure executes all three actions simultaneously
- C) Azure executes the actions in sequence — email first, then SMS, then webhook — and stops if any action fails
- D) Azure executes only the highest-priority action (webhook) because it is the most sophisticated notification type

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure action groups execute all configured actions simultaneously when triggered. All three notifications (email, SMS, PagerDuty webhook) fire at the same time when the alert condition is met. There is no priority ordering or sequential execution — the intent is that all designated parties receive notification immediately.
- *Why A is incorrect:* Azure does not randomly select actions. All actions in the action group execute when the alert fires.
- *Why C is incorrect:* Actions are not sequential and do not stop on failure. If the email action fails, the SMS and webhook still execute independently. Azure action groups are designed for reliability — one failing action should not prevent other notifications from being sent.
- *Why D is incorrect:* There is no priority ordering among action types in Azure action groups. Webhook, email, and SMS are all treated as equal notification channels that all execute.

---

## Question 8

A company wants to monitor the performance of a Python web application deployed on Azure App Service. They want to capture request response times, failed request counts, and track which external API calls are causing latency. Which service and configuration option is most appropriate?

- A) Azure Monitor Metrics with custom metric emission from the application
- B) Application Insights with the Python SDK or auto-instrumentation for App Service
- C) Log Analytics with a KQL alert rule querying App Service logs
- D) Azure Service Health monitoring of the App Service platform

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Application Insights is designed exactly for this scenario — request response times, failed request counts, and dependency (outbound API call) tracking are all built-in capabilities. For Python on Azure App Service, Application Insights supports auto-instrumentation (enable without code changes) and a Python SDK for custom telemetry. Dependency tracking automatically measures duration and success of outbound HTTP calls.
- *Why A is incorrect:* Azure Monitor custom metrics allow applications to emit numeric metric values (like a counter or gauge). While this can capture some data, it requires explicit code for every metric, does not automatically capture request/dependency details, and lacks the Application Insights analysis features (Application Map, transaction search, Smart Detection).
- *Why C is incorrect:* App Service logs can be sent to Log Analytics, but the raw logs require significant KQL work to produce the request/dependency performance analysis that Application Insights provides natively. This is a manual reimplementation of what Application Insights does out of the box.
- *Why D is incorrect:* Azure Service Health monitors the App Service platform infrastructure health (Azure's availability, not your application's performance). It tells you if Azure App Service itself has an outage, not whether your application's external API calls are slow.

---

## Question 9

Azure Monitor collects data from Azure resources automatically. However, a team notices that Azure SQL Database query performance data (slow query logs) is NOT appearing in their Log Analytics workspace. What is the most likely reason?

- A) Azure SQL Database does not support monitoring
- B) SQL Database query logs require a P2 Entra ID license to collect
- C) The team has not configured diagnostic settings on the SQL Database resource to route logs to the Log Analytics workspace
- D) Log Analytics workspaces cannot store SQL Database logs — they require Azure Storage

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Platform metrics are collected automatically, but resource-level diagnostic logs (including SQL Database query performance logs, slow query logs, audit logs, and deadlock logs) require the team to explicitly configure diagnostic settings on the resource. Without diagnostic settings routing these logs to a Log Analytics workspace, they are not collected. This is a common operational oversight.
- *Why A is incorrect:* Azure SQL Database fully supports monitoring through Azure Monitor, including metrics and multiple log categories (SQLInsights, QueryStoreRuntimeStatistics, Errors, Deadlocks, etc.). Monitoring is well-supported.
- *Why B is incorrect:* Azure Monitor data collection and Log Analytics have no dependency on Entra ID license tier. Diagnostic settings are a resource management configuration, not an identity feature.
- *Why D is incorrect:* Log Analytics workspaces can absolutely store SQL Database diagnostic logs. SQL logs sent via diagnostic settings to a Log Analytics workspace are queryable using KQL like any other log type.

---

## Question 10

A company runs a large-scale e-commerce application. During the holiday season, they want to proactively know about any Azure infrastructure issues — power outages, network disruptions, or service degradations in East US — that could affect their customer-facing services before their monitoring systems detect application impact. Which Azure service provides this proactive awareness?

- A) Azure Monitor with infrastructure metric alerts
- B) Application Insights availability tests from multiple Azure regions
- C) Azure Service Health service issue notifications
- D) Log Analytics with Azure Activity log queries

**Correct Answer:** C

**Distractor Analysis:**

- *Why C is correct:* Azure Service Health service issue notifications are published by Microsoft when Azure infrastructure experiences problems. These notifications are available before the issues manifest as application failures, giving the team awareness and context about what is happening at the platform level. Service Health alerts can be configured to notify the team via email/SMS/webhook when a service issue is published affecting their subscriptions in East US.
- *Why A is incorrect:* Azure Monitor infrastructure metric alerts detect when your application's metrics cross thresholds — they detect the symptoms of an Azure issue (increased errors, increased latency) but not the Azure infrastructure cause. They alert AFTER the application is already impacted.
- *Why B is incorrect:* Application Insights availability tests detect when your application becomes unreachable or slow from external probes — again, they detect the symptom after the fact. They do not provide advance awareness of Azure infrastructure incidents.
- *Why D is incorrect:* Azure Activity log in Log Analytics captures control-plane changes (resource creation, role assignment changes). It does not contain Azure service health events or infrastructure incident information.

---

Quiz 13 | CIS-4331 Azure Cloud | Texas Wesleyan University

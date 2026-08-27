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

---

### Question 11 (5 points)

A team wants to monitor the CPU utilization of their Azure Virtual Machines and receive a page when any VM's CPU stays above 85% for more than 10 minutes. Which Azure Monitor components do they need to configure to achieve this?

- A) A Log Analytics workspace query and an Action Group with an email receiver
- B) A Metric Alert rule with a condition on "Percentage CPU > 85", a 10-minute evaluation window, and an Action Group with a notification action
- C) An Application Insights availability test and an Action Group
- D) Azure Service Health alert and an Action Group with SMS notification

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* VM CPU utilization is a platform metric collected automatically by Azure Monitor. A Metric Alert rule evaluates the signal (Percentage CPU) against the threshold (>85%) over the specified time window (10 minutes). When the condition is met, the alert fires and triggers the linked Action Group, which can send email, SMS, voice call, webhook, or other notifications. This is the standard Azure Monitor alerting pattern for metric-based conditions.
  - *Why A is incorrect:* Log Analytics KQL queries can detect conditions, but scheduled log query alerts have higher latency (typically minutes) compared to metric alerts and require logs to be configured and flowing. Platform metrics like CPU are better monitored with metric alerts, which evaluate faster. A log query alert is appropriate for log-based conditions, not VM CPU.
  - *Why C is incorrect:* Application Insights availability tests monitor external application endpoints (HTTP URLs) for uptime and response time. They are not used for VM infrastructure metrics like CPU utilization.
  - *Why D is incorrect:* Azure Service Health alerts notify about Azure platform incidents that Microsoft publishes. They do not evaluate customer workload metrics like individual VM CPU utilization.

---

### Question 12 (5 points)

An operations team needs to query log data asking: "How many HTTP 500 errors occurred on our web application per hour over the last 7 days?" The logs are stored in a Log Analytics workspace. What query language do they use?

- A) SQL (Structured Query Language)
- B) KQL (Kusto Query Language)
- C) Splunk Processing Language (SPL)
- D) ANSI standard log query syntax

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Log Analytics workspaces use KQL (Kusto Query Language) as their query language. KQL is also used in Application Insights, Microsoft Sentinel, and Azure Resource Graph. KQL uses a pipe operator syntax (table | where | summarize | project) and supports time-series analysis, aggregation, and cross-workspace queries.
  - *Why A is incorrect:* SQL is the query language for relational databases like Azure SQL Database. Log Analytics workspaces do not use SQL syntax, though Azure Data Explorer (which also uses KQL) supports some SQL-like syntax as an alternative.
  - *Why C is incorrect:* Splunk Processing Language is the query language for Splunk, a competing log management platform. Azure Monitor uses KQL. While both serve similar analytical purposes, they are different products with different query syntaxes.
  - *Why D is incorrect:* There is no ANSI standard for log query syntax. Log analytics tools each define their own query language. Azure Monitor's Log Analytics specifically requires KQL.

---

### Question 13 (5 points)

A developer deploys a web application to Azure App Service. They want to track the number of users who visit the homepage each day, the average server response time, and any JavaScript errors that occur in the browser. Which Azure service is most appropriate for collecting all three of these data points?

- A) Azure Monitor platform metrics
- B) Azure Log Analytics with Activity Log diagnostics
- C) Application Insights
- D) Azure Service Health custom alerts

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Application Insights is Azure's application performance monitoring service. It collects server-side telemetry (response times, request rates, dependency calls, exceptions) and client-side telemetry (page views, browser performance, JavaScript errors) through a browser JavaScript SDK. It also tracks user sessions and custom events. All three data points (user visits, response time, browser errors) are native Application Insights capabilities.
  - *Why A is incorrect:* Azure Monitor platform metrics collect infrastructure-level data about the App Service resource (CPU, memory, HTTP server errors at the infrastructure level). They do not track individual user page views, user sessions, or client-side JavaScript errors.
  - *Why B is incorrect:* Log Analytics with Activity Log diagnostics captures Azure control-plane events (resource deployments, configuration changes, RBAC assignments). It does not collect application-level telemetry like user visits, response times, or browser JavaScript errors.
  - *Why D is incorrect:* Azure Service Health tracks Microsoft's Azure platform status. It has no awareness of individual application behavior, user visits, or application errors.

---

### Question 14 (5 points)

A company has 12 different alert rules monitoring various services. When any alert fires, they want to notify the on-call engineer via SMS, create a ticket in their IT service management system via webhook, and post a message to a Teams channel. How should they configure this to minimize management overhead?

- A) Add SMS, webhook, and Teams notification actions individually to each of the 12 alert rules
- B) Create one Action Group containing all three notification actions, and link all 12 alert rules to the same Action Group
- C) Create 12 separate Action Groups (one per alert rule) each containing the three notification actions
- D) Configure Azure Service Health to route all alert notifications to the ticketing system

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Action Groups are reusable notification configurations. By creating one Action Group with all three actions (SMS, webhook, Teams message) and linking all 12 alert rules to that single Action Group, any change to notification recipients or methods only requires updating one Action Group. This is the designed purpose of Action Groups — decouple the notification configuration from the alert rules for reuse.
  - *Why A is incorrect:* Adding notification actions individually to each of the 12 alert rules creates 36 action configurations (3 × 12). When the on-call engineer changes or the webhook URL changes, the team must update all 12 rules individually. This is the maintenance overhead that Action Groups are designed to prevent.
  - *Why C is incorrect:* Creating 12 separate Action Groups (one per alert rule) defeats the purpose of reusable Action Groups. This approach has the same maintenance overhead as option A — changes require updating 12 separate objects.
  - *Why D is incorrect:* Azure Service Health alerts notify about Azure platform incidents. They cannot aggregate or route application-level metric and log alerts to ticketing systems. The routing described requires alert rules with Action Groups.

---

### Question 15 (5 points)

An Azure Log Analytics workspace is configured to collect diagnostic logs from an Azure SQL Database. A security analyst runs a KQL query to find all failed login attempts in the last 24 hours but the results show no data even though failed logins are occurring. What is the most likely cause?

- A) KQL queries cannot access SQL Database security event logs
- B) The diagnostic settings on the SQL Database are not configured to send the SQLSecurityAuditEvents log category to the workspace
- C) Log Analytics workspaces require a 48-hour delay before logs are queryable
- D) SQL Database failed login logs are stored in the Activity Log, not in Log Analytics

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Diagnostic settings on Azure resources allow you to select which log categories to route to Log Analytics. SQL Database has multiple log categories (SQLInsights, QueryStoreRuntimeStatistics, SQLSecurityAuditEvents, Errors, Deadlocks, etc.). If the diagnostic settings were configured but the SQLSecurityAuditEvents category was not selected, security audit logs will not flow to the workspace and the query returns no data.
  - *Why A is incorrect:* KQL can query any log type in a Log Analytics workspace, including SQL security audit logs. SQL Database supports the SQLSecurityAuditEvents log category which includes failed login events.
  - *Why C is incorrect:* Log Analytics typically makes logs available for querying within 2-5 minutes of ingestion. There is no 48-hour delay; this is not an Azure Monitor characteristic.
  - *Why D is incorrect:* The Azure Activity Log captures control-plane operations (creating or deleting SQL servers, changing firewall rules). Data-plane events like failed login attempts are captured in SQL Database diagnostic logs (specifically SQLSecurityAuditEvents), not in the Activity Log.

---

### Question 16 (5 points)

An organization's Azure subscription experienced a regional outage in East US on a Tuesday afternoon. The operations team was alerted by their customers before they saw any internal alerts. Management wants to ensure the team is notified directly by Microsoft as soon as Azure service issues affecting East US are published. Which configuration achieves this?

- A) Create an Azure Monitor metric alert on the East US region's availability metric
- B) Configure an Azure Service Health alert for Service Issues affecting East US for all subscriptions
- C) Enable Application Insights availability tests in all Azure regions
- D) Create a Log Analytics query alert that scans the Activity Log for outage events

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Service Health allows creating alert rules for Service Issues (active incidents), Planned Maintenance, and Health Advisories. Filtering by the East US region and the relevant subscription ensures the team receives a notification the moment Microsoft publishes a service issue affecting that region — before it necessarily manifests as application failures. The alert can trigger an Action Group sending email, SMS, or webhook notifications.
  - *Why A is incorrect:* Azure Monitor metric alerts evaluate customer workload metrics (VM CPU, App Service response time, etc.). There is no "region availability metric" that reflects Azure infrastructure health. Metric alerts detect the application symptoms, not the platform cause.
  - *Why C is incorrect:* Application Insights availability tests probe an application from outside to detect outages. They detect that the application is down (the symptom) but do not provide Microsoft's service issue notifications, root cause context, or estimated time to resolution that Service Health provides.
  - *Why D is incorrect:* The Activity Log does not contain Azure service health incident records. Service Health events are published through a separate channel. Azure Service Health alert rules are the correct mechanism for receiving service issue notifications.

---

### Question 17 (5 points)

A company pins four Azure Monitor charts to an Azure Dashboard: VM CPU over 24 hours, storage account transaction count over 7 days, App Service HTTP request rate over 1 hour, and a KQL query result showing error counts by hour. Which statement best describes the purpose and limitations of this Azure Dashboard?

- A) The dashboard provides a real-time operations center view, but charts do not auto-refresh and must be manually refreshed
- B) The dashboard provides a customizable shared view of metrics and log query results that auto-refreshes on the configured interval and can be shared with the team via Azure RBAC
- C) The dashboard replaces Azure Monitor alert rules — active alerts are shown directly on the dashboard charts
- D) The dashboard can only display metrics from a single Azure subscription

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Dashboards are customizable views in the Azure Portal that can display pinned metrics charts, log query results, resource status tiles, and other widgets. They support auto-refresh intervals (from 5 minutes to 1 hour). Dashboards can be shared with other Azure users by granting them Reader access to the dashboard, making them useful for team situational awareness. They are the primary Azure Portal tool for building shared operational views.
  - *Why A is incorrect:* Azure Dashboards do support auto-refresh. The auto-refresh interval can be configured (5m, 15m, 30m, 1h) or set to manual. Saying they "do not auto-refresh" is incorrect.
  - *Why C is incorrect:* Dashboards can display an Alerts tile showing the count of fired alerts, but the dashboard charts themselves are metric/log visualizations. Dashboards do not replace alert rules. Alert rules evaluate conditions and trigger notifications; dashboards are visualizations only.
  - *Why D is incorrect:* Azure Dashboards can display data from multiple subscriptions. Metric charts and log query tiles can be scoped to resources across subscriptions within the same Azure AD tenant.

---

### Question 18 (5 points)

A company's Application Insights resource shows a spike in "Server response time" from 200ms average to 4 seconds, and simultaneously a spike in "Failed requests." A developer investigates by reviewing the Application Insights dependency tracking feature. What type of information does dependency tracking provide that helps diagnose this issue?

- A) The list of users who made requests during the spike
- B) The response times and success/failure status of calls the application made to external services (databases, APIs, storage) during the requests
- C) The CPU and memory utilization of the App Service plan during the spike
- D) The geographic distribution of requests during the spike

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Application Insights dependency tracking automatically instruments outbound calls the application makes to external dependencies — Azure SQL Database, Cosmos DB, Redis Cache, HTTP APIs, Azure Storage, and others. For each dependency call, it records the response time, success/failure status, and target endpoint. When the server response time spikes, dependency tracking shows whether a downstream service (such as the database) is responding slowly, isolating the root cause.
  - *Why A is incorrect:* User information (authenticated user IDs) is captured in Application Insights through user tracking telemetry, but the dependency tracking feature specifically focuses on outbound service calls, not inbound user identity.
  - *Why C is incorrect:* CPU and memory utilization of the App Service plan are Azure Monitor platform metrics available from the App Service resource. Application Insights dependency tracking focuses on application-level outbound calls, not infrastructure metrics.
  - *Why D is incorrect:* Geographic distribution of requests is shown in the Application Insights map view and can be analyzed by location. Dependency tracking specifically shows outbound service call performance, which is the relevant feature for diagnosing slow response times caused by downstream service issues.

---

### Question 19 (5 points)

A security team wants to retain Azure Activity Log data for 2 years to meet regulatory compliance requirements. By default, the Activity Log is retained for how long, and what configuration is needed to meet the 2-year requirement?

- A) Default retention is 90 days; configure a diagnostic setting to send Activity Log data to a Log Analytics workspace with a 730-day retention setting or to Azure Storage
- B) Default retention is 30 days; upgrade to an Azure Monitor Premium tier to extend retention to 2 years
- C) Default retention is 1 year; no configuration is needed as the Activity Log automatically retains data for 2 years in enterprise subscriptions
- D) Default retention is 7 days; configure Log Analytics with a Sentinel license to extend retention

- **Correct Answer:** A

- **Distractor Analysis:**
  - *Why A is correct:* The Azure Activity Log has a default retention of 90 days in the Activity Log experience. To retain data beyond 90 days, the team must configure a diagnostic setting to export Activity Log data to a Log Analytics workspace (where retention can be set from 30 days to 730 days, or longer with archive tier) or to Azure Storage (where retention is governed by blob lifecycle management rules and is effectively unlimited). Both options can achieve the 2-year requirement.
  - *Why B is incorrect:* The default Activity Log retention is 90 days, not 30 days. There is no "Azure Monitor Premium tier" — Azure Monitor is not tiered by license. Extending retention requires a diagnostic setting export, not a license upgrade.
  - *Why C is incorrect:* The default retention is 90 days, not 1 year. Enterprise subscriptions do not automatically receive extended retention; retention extension requires explicit configuration of diagnostic settings.
  - *Why D is incorrect:* The default retention is 90 days, not 7 days. Microsoft Sentinel does provide long-term retention capabilities, but a Sentinel license is not required to extend Activity Log retention. A Log Analytics workspace with the retention setting configured, or Azure Storage, achieves this without Sentinel.

---

### Question 20 (5 points)

A company uses Azure Monitor to track the health of a critical order processing application. The team lead asks: "What is the difference between Azure Monitor Metrics and Azure Monitor Logs, and when should we use each?" Which answer best captures the distinction?

- A) Metrics are stored in Log Analytics workspaces; Logs are stored in the Azure Metrics database. Both use KQL for queries
- B) Metrics are numerical time-series values collected at regular intervals, optimized for fast threshold-based alerting and charting; Logs are structured event records with richer context, queried using KQL, best for investigation and trend analysis
- C) Metrics can only be collected from Azure VMs; Logs can be collected from any Azure resource type
- D) Metrics are retained for 90 days by default; Logs are retained for 30 days by default

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Metrics are lightweight numerical values (CPU %, transaction count, response time in ms) sampled at regular intervals (typically 1 minute). They are stored in the Azure Monitor metrics database, are fast to query, support near-real-time alerting, and are ideal for dashboards and threshold alerts. Logs are structured records (events, errors, audit entries) with rich contextual fields, stored in Log Analytics workspaces, queried with KQL, and better suited for investigation, correlation, and complex analysis requiring text fields and variable schemas.
  - *Why A is incorrect:* The storage is reversed. Metrics are stored in the Azure Monitor metrics time-series database (not Log Analytics). Logs are stored in Log Analytics workspaces. Only Logs use KQL for queries; Metrics use a separate query interface (though metrics can also be sent to Log Analytics).
  - *Why C is incorrect:* Both Metrics and Logs can be collected from many Azure resource types. Platform metrics are available for VMs, storage accounts, SQL databases, App Services, and many others. The statement that Metrics are only for VMs is incorrect.
  - *Why D is incorrect:* The retention values are reversed. Platform metrics are retained for 93 days by default in the Azure Monitor metrics database. Log Analytics workspace logs have a configurable default retention of 30 days (free tier) to 730 days (paid tier). The specific numbers and the direction of the comparison in the distractor are incorrect.

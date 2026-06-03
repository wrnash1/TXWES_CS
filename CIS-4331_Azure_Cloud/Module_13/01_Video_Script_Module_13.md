# Video Script: Module 13 - Azure Monitoring and Diagnostics

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)
**Estimated Duration:** 20-24 minutes

---

## Learning Objectives

By the end of this video you will be able to:

- Describe what Azure Monitor does and what data it collects
- Explain the difference between metrics and logs
- Describe the role of Log Analytics workspaces and KQL queries
- Explain what Application Insights provides for application monitoring
- Describe Azure Alerts and how they notify on threshold breaches
- Match monitoring scenarios to the correct Azure monitoring service

---

## Section 1: Introduction — Why Monitoring Matters (0:00-2:00)

[INSTRUCTOR ON CAMERA]

You've deployed an application to Azure. Congratulations. Now the question is: how do you know it's working?

Is it responding quickly? Are requests failing? Is the database running out of connections? Is a VM running out of disk space? Is there an unusual spike in traffic that might indicate an attack?

Without monitoring, you find out about these problems when users call you — or when the application is already down. With monitoring, you detect problems before users notice them, diagnose issues faster when they do occur, and build a historical baseline that helps you understand what "normal" looks like.

[SLIDE: "Azure's Monitoring Stack"]

Azure provides a comprehensive monitoring stack. Today we cover four services in that stack.

Azure Monitor is the umbrella service — the central platform that collects, stores, and routes telemetry data from across your Azure environment. Everything else plugs into it.

Log Analytics is the data store and query engine within Azure Monitor. It stores log data and lets you query it using the Kusto Query Language, or KQL.

Application Insights is an application performance monitoring tool that sits within Azure Monitor. It gives you deep visibility into your application's behavior — request rates, response times, failures, dependencies, user behavior.

Azure Alerts is the notification system. It watches your metrics and logs and sends alerts when something crosses a threshold.

Let's go through each one.

---

## Section 2: Azure Monitor — The Monitoring Platform (2:00-7:00)

[SLIDE: "Azure Monitor Overview"]

[INSTRUCTOR ON CAMERA]

Azure Monitor is the centralized monitoring platform for Azure. It collects telemetry data from two main categories: metrics and logs.

Let me explain the difference between these two.

[SLIDE: "Metrics vs. Logs"]

Metrics are numerical, time-series data points. CPU percentage at a given time. Memory available at a given time. Number of HTTP requests per second. Network bytes in. Storage IOPS. Metrics are lightweight, collected frequently (every minute by default), and stored in a specialized time-series database. They are ideal for real-time dashboards and alerting because the data is always recent and fast to query.

Logs are structured or unstructured records of events. A log entry might say: "At 10:23:47 AM, user john at company dot com signed in from IP 192.168.1.1 and accessed the /api/orders endpoint. Response code: 200. Duration: 147ms." Logs contain much richer information than metrics but are also larger and more expensive to query at scale. Logs are ideal for investigation, root cause analysis, and compliance auditing.

[SLIDE: "What Azure Monitor Collects"]

Azure Monitor can collect telemetry from:

Azure resources — VMs, storage accounts, databases, app services, and virtually every Azure service sends metrics to Azure Monitor automatically. Some logs require explicit configuration.

Guest operating systems — If you install the Azure Monitor Agent on a VM, it collects logs and metrics from the operating system inside the VM, including event logs, performance counters, and custom application logs.

Applications — Using Application Insights (covered in a moment), Monitor can collect request traces, exceptions, and performance data from your application code.

Custom sources — Using the Monitor APIs or agents, you can send telemetry from on-premises systems and other clouds.

[SLIDE: "Azure Monitor Data Paths"]

Once collected, Azure Monitor data can flow to several destinations.

Log Analytics workspace — Stores log data for querying and analysis.

Azure Storage — Long-term archival of logs.

Azure Event Hubs — Streaming logs to external SIEM systems like Microsoft Sentinel or third-party tools.

Alerts — Triggers notifications based on metric thresholds or log query results.

Workbooks — Visual dashboards built from Monitor data.

[SHOW PORTAL: Azure Monitor > Overview — show the main Monitor hub with Metrics, Logs, Alerts, and Service Health tiles]

In the portal, Azure Monitor is the hub from which you access all monitoring capabilities. The Metrics Explorer lets you chart any metric from any resource over any time window. The Logs section opens the Log Analytics query interface.

---

## Section 3: Log Analytics (7:00-11:00)

[SLIDE: "Log Analytics Workspace"]

[INSTRUCTOR ON CAMERA]

A Log Analytics workspace is the Azure Monitor data store for log data. When resources send logs to Azure Monitor, those logs land in a Log Analytics workspace where they can be queried.

Think of it as a managed log database. Azure resources, VMs with the Monitor Agent, Application Insights, and Sentinel all write to Log Analytics workspaces. You query the data using KQL.

[SLIDE: "What Is KQL?"]

KQL — the Kusto Query Language — is the query language for Log Analytics. It is a read-only query language designed for working with large volumes of time-series log data.

A basic KQL query looks like this:

Heartbeat
| where TimeGenerated > ago(24h)
| summarize count() by Computer, bin(TimeGenerated, 1h)
| order by TimeGenerated desc

That query reads the Heartbeat table — which VMs with the Monitor Agent send data to every minute — filters to the last 24 hours, counts heartbeats per computer per hour, and sorts by time.

You don't need to memorize KQL syntax for AZ-900. You do need to know that Log Analytics uses KQL to query log data, and that KQL is available in the Log Analytics query interface in the portal.

[SLIDE: "Log Analytics Use Cases"]

Log Analytics is used for:

Security log analysis — Querying security events to investigate incidents.

Performance analysis — Querying performance counters to identify resource bottlenecks.

Compliance auditing — Querying activity logs to verify who made what changes.

Alert creation — Writing KQL queries that trigger alerts when specific log patterns are detected.

Microsoft Sentinel — Sentinel's entire detection and investigation capability is built on Log Analytics.

[SHOW PORTAL: Azure Monitor > Logs — show the query editor with a sample KQL query and result table]

In the portal, the Logs blade shows the query editor. You can select tables from the left panel, write queries in the editor, and see results in a table or chart below.

---

## Section 4: Application Insights (11:00-15:00)

[SLIDE: "What Is Application Insights?"]

[INSTRUCTOR ON CAMERA]

Application Insights is an application performance monitoring (APM) service within Azure Monitor. While Azure Monitor watches your Azure infrastructure — VMs, databases, networks — Application Insights watches your application itself.

It answers questions like:

How many requests is my application receiving per second? What percentage of those requests fail? How long does it take to respond? Which specific requests are slowest? Are there database queries causing latency? What exceptions are users triggering? What countries are my users coming from?

[SLIDE: "How Application Insights Works"]

Application Insights works by adding an SDK to your application or by enabling agent-based monitoring for Azure App Service, AKS, Azure Functions, and Azure VMs.

The SDK instruments your application code. As your application runs, it automatically captures:

Request data — Every HTTP request: URL, method, response code, duration, and whether it succeeded.

Dependency tracking — Calls your application makes to other services: database queries, HTTP calls to external APIs, Azure Service Bus messages. It measures the duration and success of each call.

Exceptions — Unhandled exceptions are automatically captured with full stack traces.

Page views and user behavior — For web applications, client-side JavaScript instrumentation captures browser page loads, user sessions, and custom events.

Performance counters — CPU, memory, and other VM-level performance counters.

Custom telemetry — Your application code can emit custom events and metrics using the Application Insights API. For example: "Payment processed," "User signed up," "Search query returned 0 results."

[SLIDE: "Application Map"]

One of the most powerful features of Application Insights is the Application Map. This is a visual diagram showing how your application components connect — your web front end, its database calls, its calls to external APIs, its background processing workers. Each component shows its request rate, response time, and failure rate. You can immediately see which component is causing problems.

[SLIDE: "Live Metrics Stream"]

Application Insights also provides Live Metrics — a real-time dashboard updating every second showing incoming requests, outgoing dependencies, server CPU and memory, and failure rate. This is invaluable during deployments, incident response, or load testing.

[SHOW PORTAL: Application Insights > Overview — show request count, response time, failure rate. Show Application Map]

In the portal, the Application Insights Overview shows four key metrics front and center: server requests, server response time, server exceptions, and browser page load time. The Application Map shows your dependency topology.

[SLIDE: "Application Insights — AZ-900 Key Points"]

For the exam: Application Insights is within Azure Monitor and provides application-level performance monitoring. It requires instrumentation — adding an SDK or enabling an agent. It collects requests, dependencies, exceptions, and custom telemetry. The Application Map visualizes component relationships. Live Metrics provides real-time visibility.

---

## Section 5: Azure Alerts (15:00-19:00)

[SLIDE: "What Are Azure Alerts?"]

[INSTRUCTOR ON CAMERA]

Azure Alerts is the notification system for Azure Monitor. You define conditions — alert rules — and when those conditions are met, Alerts notifies you.

The alert rule has three parts.

One: The condition. What are you watching? This could be: a metric exceeds a threshold (CPU > 90% for 5 minutes), a log query returns results (any failed login attempts in the last hour), or a service health event (an Azure region has an outage).

Two: The action group. What do you do when the alert fires? An action group defines one or more actions: send an email, send an SMS, call a webhook, run an Azure Automation runbook, create an ITSM incident in ServiceNow. One action group can be shared across many alert rules.

Three: The severity. Alerts have severity levels from 0 (Critical) to 4 (Verbose). Severity helps teams prioritize — a Severity 0 alert wakes someone up at 3 AM; a Severity 4 alert just adds to a daily digest.

[SLIDE: "Alert Rule Types"]

There are several types of alert rules.

Metric alerts — Fire when a metric value crosses a threshold. Example: "Alert me when the average CPU of my VM cluster exceeds 85% for more than 5 minutes." These are fast because metrics are near real-time.

Log alert rules — Fire when a KQL query against a Log Analytics workspace returns results. Example: "Alert me when there are more than 10 failed login attempts in 5 minutes."

Activity log alerts — Fire when specific control-plane events occur. Example: "Alert me when any resource is deleted in this subscription." Great for change management.

Service health alerts — Fire when Azure publishes a service incident that affects your subscription and regions. This keeps your team informed when Azure itself has a problem.

Smart detection — Application Insights includes automatic anomaly detection that fires alerts without you having to set explicit thresholds. It learns your application's normal behavior and alerts when something deviates significantly.

[SLIDE: "Action Groups"]

Action groups define what happens when an alert fires. Multiple notifications and actions can be in one group:

- Email, SMS, voice call — Notify specific people
- Azure app push notification — Mobile alert to the Azure mobile app
- Webhook — Call an external system's API
- Azure Automation runbook — Run automated remediation scripts
- Azure Functions — Run serverless code in response to the alert
- ITSM connector — Create a ticket in ServiceNow, Jira, or similar tools

[SHOW PORTAL: Azure Monitor > Alerts > show the Alerts summary dashboard and an alert rule's configuration]

In the portal, the Alerts dashboard shows all fired alerts with their severity, state (fired/resolved), and time. The Alert rules blade shows all configured rules and their last evaluation status.

---

## Section 6: Azure Service Health (19:00-21:00)

[SLIDE: "Azure Service Health"]

[INSTRUCTOR ON CAMERA]

Azure Service Health is a monitoring service that provides personalized notifications about Azure service outages, planned maintenance, and health advisories that affect your specific subscriptions and regions.

This is different from the Azure Status page — which shows global Azure status — because Service Health is filtered to show only incidents that affect your resources. If you have VMs in East US and Azure has a storage issue in West Europe, your Service Health page will not show that issue. You only see what affects you.

Service Health has three types of communications.

Service issues — Active outages or degradations affecting Azure services in your region.

Planned maintenance — Microsoft's schedule for maintenance activities that might affect your resources. Usually low-impact but important to track.

Health advisories — Notifications about Azure features being deprecated, requiring action on your part, or best practice recommendations.

For AZ-900: Know that Service Health provides personalized, subscription-specific Azure incident notifications. Combine Service Health with Azure Alerts to automatically notify your team when an Azure incident affects your resources.

---

## Section 7: Monitoring Service Selection Summary (21:00-23:00)

[SLIDE: "Monitoring Service Selection Framework"]

[INSTRUCTOR ON CAMERA]

Let's nail down the service selection for AZ-900.

When the scenario is about collecting and centralizing telemetry from Azure resources — the answer is Azure Monitor. It's the platform everything else builds on.

When the scenario is about storing and querying log data, especially using KQL — the answer is Log Analytics workspace.

When the scenario is about understanding how your application behaves — request rates, response times, failures, user behavior — the answer is Application Insights.

When the scenario is about getting notified when something goes wrong — a metric threshold is crossed, a log pattern is detected — the answer is Azure Alerts with action groups.

When the scenario is about knowing when Azure itself has a problem affecting your resources — the answer is Azure Service Health.

[SLIDE: "Quick Scenario Practice"]

Scenario: "A team wants to receive an SMS when the CPU utilization of their production VMs exceeds 90% for more than 5 minutes." That's Azure Alerts — specifically a metric alert on the CPU metric, with an action group that sends an SMS.

Scenario: "A security team wants to query the last 90 days of authentication logs to identify which users logged in from foreign IP addresses." That's Log Analytics — querying sign-in logs stored in a Log Analytics workspace using KQL.

Scenario: "A product manager wants to know which page in their web application has the highest load time, and which country most users are coming from." That's Application Insights — it tracks page views and browser timing data.

---

## Section 8: Closing (23:00-24:00)

[INSTRUCTOR ON CAMERA]

Let's wrap up. Azure Monitor is the central telemetry collection and routing platform — it collects metrics and logs from Azure resources, OS guests, and applications. Log Analytics is the log data store and query engine using KQL. Application Insights provides deep application performance monitoring — requests, dependencies, exceptions, user behavior. Azure Alerts notifies you when conditions are met, using action groups to send emails, SMS, run automation. Azure Service Health keeps you informed when Azure itself affects your resources.

Monitoring is not optional in production cloud environments. The teams that detect and diagnose problems fastest are the ones that have set up comprehensive monitoring before problems occur. In the lab, you will explore Azure Monitor metrics and create an alert rule. See you in the reading guide.

---

Module 13 Video Script | CIS-4331 Azure Cloud | Texas Wesleyan University

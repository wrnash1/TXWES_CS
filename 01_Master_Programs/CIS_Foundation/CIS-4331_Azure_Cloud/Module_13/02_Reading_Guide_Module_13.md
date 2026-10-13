# Reading Guide: Module 13 - Azure Monitoring and Diagnostics

<div style="text-align: center; margin: 24px 0;">
  <svg viewBox="0 0 800 280" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 800px; background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <rect width="100%" height="45" fill="#1b365d" rx="8" ry="8"/>
    <rect width="100%" height="20" y="30" fill="#1b365d"/>
    <text x="400" y="28" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif" font-size="15" font-weight="bold" text-anchor="middle">🏛️ TEXAS WESLEYAN UNIVERSITY &bull; CIS-4331 &BULL; MICROSOFT AZURE CLOUD ARCHITECTURE</text>
    
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


**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**AZ-900 Domain:** Describe Azure management and governance (30-35% of exam)

---

## Overview

Monitoring is the foundation of operational visibility in cloud environments. Without it, problems go undetected until users report failures. With comprehensive monitoring, teams detect anomalies proactively, diagnose root causes quickly, and build performance baselines that inform capacity planning. This module covers Azure's monitoring stack: Azure Monitor, Log Analytics, Application Insights, Azure Alerts, and Azure Service Health.

---

## Section 1: Azure Monitor

### What Azure Monitor Does

Azure Monitor is the unified monitoring platform for Azure. It collects, stores, analyzes, and acts on telemetry data from Azure resources, guest operating systems, and applications. Almost every other Azure monitoring capability is built on or integrated with Azure Monitor.

### Two Data Types: Metrics and Logs

| Dimension | Metrics | Logs |
|---|---|---|
| Format | Numerical time-series values | Structured or unstructured event records |
| Examples | CPU %, available memory bytes, requests/sec | Sign-in events, error messages, audit records |
| Frequency | Collected every minute (default) | Collected when events occur |
| Storage | Azure Monitor Metrics (time-series store) | Log Analytics workspace |
| Query method | Metrics Explorer charts | KQL (Kusto Query Language) |
| Best for | Real-time dashboards, threshold alerts | Investigation, root cause analysis, compliance |
| Retention (default) | 93 days | 30 days (configurable to 2 years) |

### What Azure Monitor Collects

| Source | What Is Collected | Configuration Required? |
|---|---|---|
| Azure platform resources | Resource metrics (CPU, memory, I/O, requests) | No — sent automatically |
| Azure platform logs | Activity log (control-plane events), resource logs | Activity log: auto; resource logs: diagnostic settings needed |
| Guest OS (VMs) | OS metrics, event logs, performance counters, custom app logs | Yes — requires Azure Monitor Agent |
| Applications | Request traces, exceptions, dependencies, user behavior | Yes — requires Application Insights SDK or agent |
| Custom sources | Any data via Monitor REST API, custom logs | Yes — requires configuration |

### Azure Monitor Data Destinations

Collected telemetry can be routed to multiple destinations simultaneously:

| Destination | Use Case |
|---|---|
| Log Analytics workspace | Query log data with KQL; alerts; Sentinel integration |
| Azure Storage | Long-term archival (compliance, cost optimization) |
| Azure Event Hubs | Stream to external SIEM or analytics platforms |
| Azure Monitor Metrics | Near-real-time metric dashboards and alerts |
| Partner solutions | Splunk, Elastic, Datadog via built-in integrations |

### Diagnostic Settings

Diagnostic settings configure where a resource's logs and metrics are sent. Each resource can have diagnostic settings that send data to Log Analytics, Storage, Event Hubs, or a partner solution. Without configuring diagnostic settings, resource-level logs are not collected (though platform metrics are).

---

## Section 2: Log Analytics

### Log Analytics Workspace

A Log Analytics workspace is the managed database for log data within Azure Monitor. It is where:

- Resource logs from Azure services land (when configured via diagnostic settings)
- VM operating system logs arrive (when collected by the Azure Monitor Agent)
- Application Insights data is stored (optionally, in workspace-based mode)
- Microsoft Sentinel stores all security data

Multiple resources across multiple subscriptions can send data to a single Log Analytics workspace, centralizing log data for unified analysis.

### Kusto Query Language (KQL)

KQL is the query language used to query Log Analytics workspaces. Key characteristics:

- Read-only (cannot modify data)
- Pipe-based syntax — each operation feeds into the next using the `|` character
- Designed for large-scale time-series log data
- Used by Log Analytics, Sentinel, Application Insights, Azure Resource Graph, and others

Sample KQL queries (for context — AZ-900 does not require writing KQL):

```kql
// Count VM heartbeats by computer over the last 24 hours
Heartbeat
| where TimeGenerated > ago(24h)
| summarize count() by Computer

// Find failed sign-ins in Entra ID logs
SigninLogs
| where ResultType != "0"
| project TimeGenerated, UserPrincipalName, ResultDescription, IPAddress
| order by TimeGenerated desc

// Average CPU usage per VM over the last hour
Perf
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| where TimeGenerated > ago(1h)
| summarize avg(CounterValue) by Computer
```

### Common Log Analytics Tables

| Table Name | Contains |
|---|---|
| Heartbeat | Periodic signals from VMs with Azure Monitor Agent (proves VM is alive) |
| Perf | Performance counters from VMs (CPU, memory, disk) |
| Event | Windows event log entries |
| Syslog | Linux syslog entries |
| AzureActivity | Azure control-plane activity (who created/deleted/changed what) |
| SigninLogs | Entra ID user sign-in events |
| SecurityEvent | Windows Security event log (login attempts, privilege escalations) |
| AppRequests | Application Insights — HTTP requests |
| AppExceptions | Application Insights — unhandled exceptions |

---

## Section 3: Application Insights

### What Application Insights Monitors

Application Insights is the application performance monitoring (APM) capability within Azure Monitor. Where Azure Monitor monitors infrastructure (VMs, networks, storage), Application Insights monitors the application running on that infrastructure.

### Data Collected by Application Insights

| Data Type | Description | Example |
|---|---|---|
| Requests | Every inbound HTTP request to the application | GET /api/orders, 200 OK, 145ms |
| Dependencies | Outbound calls the app makes | SQL query to database, 23ms; HTTP call to payment API, 340ms |
| Exceptions | Unhandled errors with full stack traces | NullReferenceException in OrderController.cs line 47 |
| Page views | Browser-side page load events (JavaScript SDK) | User loaded /checkout page, 2.3s load time |
| Custom events | Application-defined business events | PaymentProcessed, UserRegistered, SearchPerformed |
| Performance counters | Server CPU, memory, request queue depth | Server CPU 42%, available memory 1.2 GB |
| Availability tests | Synthetic HTTP probes from multiple Azure regions | HTTP GET to homepage from 5 global locations every 5 min |

### Key Application Insights Features

| Feature | Description |
|---|---|
| Application Map | Visual topology of application components with health indicators |
| Live Metrics | Real-time (sub-second latency) dashboard of requests, failures, server resources |
| Transaction search | Find individual request traces by ID, URL, user, or time |
| Failures blade | Aggregate view of exceptions and failed requests by operation |
| Performance blade | Response time analysis by operation with dependency breakdown |
| Availability tests | Proactive synthetic monitoring from global Azure regions |
| Smart detection | Automatic anomaly detection with alerts — no threshold configuration required |
| User analytics | User sessions, retention, funnel analysis, user flows |

### Instrumentation Options

| Method | Best For | Languages / Platforms |
|---|---|---|
| SDK (code-level) | Maximum telemetry control; custom events | .NET, Java, Node.js, Python, JavaScript |
| Auto-instrumentation | Zero-code change for supported platforms | Azure App Service (.NET, Java, Node), Azure Functions, AKS |
| Azure Monitor Agent | VM-based applications | Any application writing to OS logs |
| OpenTelemetry | Standards-based instrumentation | Multi-language, multi-cloud |

### Application Insights vs. Azure Monitor Metrics

Application Insights data is stored in a Log Analytics workspace and queried with KQL — it is part of the Azure Monitor ecosystem. The distinction is that Application Insights provides application-layer telemetry (requests, dependencies, exceptions) while Azure Monitor infrastructure metrics provide resource-layer telemetry (CPU, memory, disk). Both are needed for comprehensive end-to-end observability.

---

## Section 4: Azure Alerts

### Alert Rule Components

Every Azure alert rule has three components:

| Component | Description |
|---|---|
| Signal (condition) | What to monitor: metric threshold, log query result, activity log event, service health event |
| Action group | What to do when the alert fires: send email/SMS, call webhook, run automation |
| Severity | Priority level from 0 (Critical) to 4 (Verbose) |

### Alert Rule Types

| Type | Signal Source | Use Case | Latency |
|---|---|---|---|
| Metric alert | Azure Monitor Metrics | CPU > 90% for 5 min, memory < 1 GB | Near real-time (1 min) |
| Log alert | Log Analytics KQL query | > 10 failed logins in 5 min, error count spike | 5+ minutes |
| Activity log alert | Azure Activity log | Resource deleted, role assignment changed | Minutes |
| Service health alert | Azure Service Health | Azure outage in your region | Minutes |
| Smart detection (App Insights) | Application Insights ML | Unusual failure rate, dependency degradation | Automatic |

### Action Groups

An action group is a reusable collection of notification and automation actions. One action group can be attached to many alert rules.

| Action Type | Description |
|---|---|
| Email | Send to specified email addresses |
| SMS | Send text message to phone number |
| Voice call | Automated phone call |
| Azure app push notification | Notify via Azure mobile app |
| Webhook | HTTP POST to external URL (Slack, PagerDuty, custom API) |
| Azure Automation runbook | Execute automated remediation script |
| Azure Functions | Run serverless function (custom response logic) |
| ITSM | Create ticket in ServiceNow, Jira, or other tools |
| Event Hub | Stream alert to Event Hub for external processing |

### Alert States

| State | Meaning |
|---|---|
| Fired | Alert condition was met; notification sent |
| Resolved | Alert condition is no longer met (for stateful alerts) |
| Acknowledged | Team member marked it as being investigated |

### Dynamic Thresholds

For metric alerts, Azure Monitor can use machine learning to automatically set alert thresholds based on historical data rather than requiring you to specify a fixed number. This is useful when "normal" varies by day of week or time of day — for example, a web application that naturally has higher traffic on weekday mornings.

---

## Section 5: Azure Service Health

### What Service Health Provides

Azure Service Health provides personalized monitoring of Azure service incidents that affect your specific subscriptions and regions. Unlike the public Azure Status page (which shows global Azure status), Service Health filters to show only incidents that impact your resources.

### Three Types of Service Health Notifications

| Type | Description | Example |
|---|---|---|
| Service issues | Active outages or degradations in Azure services | "Azure SQL Database experiencing connectivity issues in East US" |
| Planned maintenance | Scheduled maintenance activities by Microsoft | "VM host maintenance window: March 15, 2:00-4:00 AM UTC in West US 2" |
| Health advisories | Actions you may need to take; deprecation notices | "Azure AD Graph API is being retired — migrate to Microsoft Graph by June 2024" |

### Service Health + Azure Alerts

You can create Azure Alerts that trigger on Service Health events. This means when Azure publishes an incident that affects your subscription, your team can receive automatic notifications via email, SMS, or webhook — without anyone having to monitor the Azure Status page manually.

---

## Section 6: Monitoring Service Selection Summary

| Scenario | Correct Service |
|---|---|
| Collect CPU and memory metrics from all Azure VMs | Azure Monitor (metrics are collected automatically) |
| Query 90 days of authentication logs to investigate an incident | Log Analytics workspace (KQL query on SigninLogs table) |
| Get notified when a VM's CPU exceeds 90% for 5 minutes | Azure Alerts (metric alert + action group with email/SMS) |
| Monitor request response times and exception rates in a web app | Application Insights |
| Automatically notify the team when Azure has an outage in East US | Azure Service Health alert |
| View application dependency topology to diagnose slow requests | Application Insights Application Map |
| Stream security logs to an external SIEM | Azure Monitor with Event Hub destination |
| Store 2 years of compliance audit logs cost-effectively | Azure Monitor logs to Azure Storage (long-term archival) |
| Detect unusual failure rate spikes without setting explicit thresholds | Application Insights Smart Detection |

---

## Section 7: Azure CLI — Monitoring Commands

```bash
# List available metrics for a resource
az monitor metrics list-definitions \
  --resource "/subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Compute/virtualMachines/<vm-name>" \
  --output table

# Query recent metric values (last hour CPU average)
az monitor metrics list \
  --resource "/subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Compute/virtualMachines/<vm-name>" \
  --metric "Percentage CPU" \
  --interval PT1H \
  --output table

# Create an action group (email notification)
az monitor action-group create \
  --name "ops-team-alerts" \
  --resource-group my-rg \
  --short-name "OpsAlerts" \
  --email-receiver name=ops-email email=ops@company.com

# Create a metric alert rule (CPU > 90%)
az monitor metrics alert create \
  --name "high-cpu-alert" \
  --resource-group my-rg \
  --scopes "/subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.Compute/virtualMachines/<vm-name>" \
  --condition "avg Percentage CPU > 90" \
  --window-size 5m \
  --evaluation-frequency 1m \
  --action "/subscriptions/<sub-id>/resourceGroups/<rg>/providers/microsoft.insights/actionGroups/ops-team-alerts"

# List all alert rules
az monitor metrics alert list \
  --resource-group my-rg \
  --output table
```

---

## Section 8: AZ-900 Exam Tips

1. **Azure Monitor is the platform, everything else builds on it.** Log Analytics, Application Insights, and Alerts are all part of or integrate with Azure Monitor. Azure Monitor is the umbrella.

2. **Metrics vs. Logs — know the difference.** Metrics are numbers over time, fast to query, good for alerts. Logs are event records, richer content, queried with KQL, good for investigation.

3. **Log Analytics uses KQL.** You do not need to write KQL for AZ-900, but you need to know that KQL is the query language for Log Analytics workspaces and that it is used in Sentinel, Application Insights, and Azure Resource Graph.

4. **Application Insights is for applications.** When the scenario mentions request rates, response times, exceptions, dependency tracking, or user behavior — Application Insights is the answer.

5. **Alerts = signal + action group.** An alert rule needs a signal (condition) and an action group (what to do). Action groups are reusable — one group can be shared by many alert rules.

6. **Service Health is subscription-filtered.** The public Azure Status page shows all Azure issues globally. Service Health shows only the issues affecting your subscriptions and regions.

7. **Diagnostic settings required for resource logs.** Platform metrics are automatically collected, but resource-level logs (SQL diagnostics, storage logs, etc.) require you to configure diagnostic settings to route them to a destination.

8. **Application Insights availability tests** are synthetic probes — they test your application from outside by sending HTTP requests from multiple Azure regions on a schedule. Use them to detect outages before users do.

---

Module 13 Reading Guide | CIS-4331 Azure Cloud | Texas Wesleyan University

---

## 9. Supplemental Resources

1. Azure Monitor overview — platform architecture, Metrics vs. Logs, and the relationship between Azure Monitor and its sub-services: https://learn.microsoft.com/en-us/azure/azure-monitor/overview

2. Application Insights overview — application performance monitoring, telemetry types, dependency tracking, and availability tests: https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview

3. Azure Service Health documentation — service issue notifications, planned maintenance alerts, health history, and health advisories: https://learn.microsoft.com/en-us/azure/service-health/overview

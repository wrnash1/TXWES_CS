# Lab Activity: Module 13 - Azure Monitoring and Diagnostics

**Course:** CIS-4331 Azure Cloud | Texas Wesleyan University
**Instructor:** Professor Nash
**Points:** 100
**Estimated Time:** 60-75 minutes
**Submission:** Canvas LMS — Module 13 Lab Assignment
**Prerequisite:** Azure for Students subscription, Azure CLI authenticated

---

## Learning Objectives

By completing this lab you will be able to:

- Explore Azure Monitor metrics for deployed Azure resources
- Create a Log Analytics workspace and configure diagnostic settings
- Run basic KQL queries against collected log data
- Create an alert rule with an action group
- Explain the difference between metrics and logs in operational contexts
- Describe what Application Insights provides beyond infrastructure monitoring

---

## Part A: Azure Monitor — Explore Metrics (25 Points)

### Step 1: Create a Resource Group and Storage Account (5 Points)

Open Azure Cloud Shell (Bash) and run:

```bash
az group create \
  --name lab13-rg \
  --location eastus

az storage account create \
  --name lab13storage[your-initials] \
  --resource-group lab13-rg \
  --location eastus \
  --sku Standard_LRS \
  --kind StorageV2
```

Generate some activity on the storage account by creating a container and uploading a file:

```bash
STORAGE_KEY=$(az storage account keys list \
  --resource-group lab13-rg \
  --account-name lab13storage[your-initials] \
  --query "[0].value" \
  --output tsv)

az storage container create \
  --account-name lab13storage[your-initials] \
  --account-key $STORAGE_KEY \
  --name lab13-container

echo "Lab 13 monitoring test file" > testfile.txt

az storage blob upload \
  --account-name lab13storage[your-initials] \
  --account-key $STORAGE_KEY \
  --container-name lab13-container \
  --name testfile.txt \
  --file testfile.txt
```

Include the output showing the storage account was created and the blob was uploaded.

### Step 2: Explore Metrics in Azure Monitor (10 Points)

Navigate to the Azure Portal: Monitor > Metrics (or navigate directly to your storage account > Monitoring > Metrics).

[PORTAL STEPS: Azure Monitor > Metrics > select storage account as scope]

Configure a chart with these settings:

1. Scope: Select your storage account (lab13storage[your-initials])
2. Metric namespace: Blob
3. Metric: Transactions
4. Aggregation: Count
5. Set the time range to the last 1 hour

Take a screenshot of the Metrics chart showing transaction data.

Now add a second metric to the same chart:

1. Click "Add metric"
2. Metric: Ingress
3. Aggregation: Sum

Take a screenshot showing both metrics on the chart.

Answer:

1. The Metrics chart shows Azure Monitor collected transaction data for your storage account automatically — you did not configure anything to enable this. What does this tell you about how Azure Monitor collects platform metrics? How is this different from how guest OS logs are collected?

2. The Transactions metric counts the number of API calls to the storage account. The Ingress metric measures bytes received. In an operational context, what would it mean if you saw a spike in Ingress but no corresponding spike in Transactions? Give a specific scenario where this pattern might occur.

3. The time-range selector lets you view metrics from the last hour to the last 30 days. Metrics data is retained for 93 days by default. If you need to retain this data for compliance purposes beyond 93 days, what Azure Monitor configuration would you use?

### Step 3: Pin to Dashboard (10 Points)

On the Metrics chart showing both metrics:

1. Click "Save to dashboard" or "Pin to dashboard"
2. Select "Create new" dashboard
3. Name it "Lab13-Monitoring-Dashboard"
4. Click "Pin"

Navigate to the Dashboard to verify the chart was pinned.

[PORTAL STEPS: Azure Portal home > Dashboards > Lab13-Monitoring-Dashboard]

Take a screenshot of the dashboard with the pinned metrics chart.

Answer:

1. Dashboards consolidate monitoring views from multiple resources and services. In a production environment, what types of metrics from different resources would a cloud operations team want to see on a single dashboard? Give at least three examples of resource types and the metric that would be most important for each.

2. Azure Monitor Workbooks provide more advanced dashboard capabilities than the basic pin-to-dashboard approach. Based on what you know about monitoring, what is one scenario where a Workbook would be more appropriate than a simple pinned metrics chart?

---

## Part B: Log Analytics Workspace and KQL Queries (35 Points)

### Step 1: Create a Log Analytics Workspace (5 Points)

```bash
az monitor log-analytics workspace create \
  --resource-group lab13-rg \
  --workspace-name lab13-workspace \
  --location eastus
```

Get the workspace ID for later use:

```bash
WORKSPACE_ID=$(az monitor log-analytics workspace show \
  --resource-group lab13-rg \
  --workspace-name lab13-workspace \
  --query customerId \
  --output tsv)

echo "Workspace ID: $WORKSPACE_ID"
```

Include both command outputs.

### Step 2: Configure Diagnostic Settings for the Storage Account (10 Points)

Configure the storage account to send logs to the Log Analytics workspace:

```bash
STORAGE_RESOURCE_ID=$(az storage account show \
  --name lab13storage[your-initials] \
  --resource-group lab13-rg \
  --query id \
  --output tsv)

WORKSPACE_RESOURCE_ID=$(az monitor log-analytics workspace show \
  --resource-group lab13-rg \
  --workspace-name lab13-workspace \
  --query id \
  --output tsv)

az monitor diagnostic-settings create \
  --name "lab13-diag" \
  --resource $STORAGE_RESOURCE_ID/blobServices/default \
  --workspace $WORKSPACE_RESOURCE_ID \
  --logs '[{"category": "StorageRead", "enabled": true}, {"category": "StorageWrite", "enabled": true}]' \
  --metrics '[{"category": "Transaction", "enabled": true}]'
```

Verify the diagnostic settings were created:

```bash
az monitor diagnostic-settings list \
  --resource $STORAGE_RESOURCE_ID/blobServices/default \
  --output table
```

Include both outputs and answer:

1. Before you configured diagnostic settings, was Azure Monitor collecting any data from the storage account? After configuring diagnostic settings, what additional data will flow to the Log Analytics workspace that was not being collected before?

2. Diagnostic settings can route logs to three destinations: Log Analytics workspace, Azure Storage, and Azure Event Hubs. For a company that needs to retain storage access logs for 7 years for regulatory compliance, which destination would be most cost-effective and why? (Consider that Log Analytics default retention is 30 days.)

### Step 3: Generate Log Data and Run KQL Queries (20 Points)

Generate some blob storage activity to create log data:

```bash
# Upload several files to create storage read/write log entries
for i in 1 2 3 4 5; do
  echo "Log data test file $i" > "testfile$i.txt"
  az storage blob upload \
    --account-name lab13storage[your-initials] \
    --account-key $STORAGE_KEY \
    --container-name lab13-container \
    --name "testfile$i.txt" \
    --file "testfile$i.txt"
done

# Download a file to generate a read event
az storage blob download \
  --account-name lab13storage[your-initials] \
  --account-key $STORAGE_KEY \
  --container-name lab13-container \
  --name testfile.txt \
  --file downloaded.txt
```

Wait 10-15 minutes for the logs to appear in the Log Analytics workspace, then navigate to the portal:

[PORTAL STEPS: Azure Monitor > Logs > select lab13-workspace scope]

Run the following KQL queries and capture screenshots of the results:

#### Query 1: List available tables in the workspace

```kql
search *
| distinct $table
| sort by $table asc
```

#### Query 2: Query storage blob operations (once data appears)

```kql
StorageBlobLogs
| where TimeGenerated > ago(1h)
| project TimeGenerated, OperationName, StatusCode, DurationMs, CallerIpAddress
| order by TimeGenerated desc
| take 20
```

#### Query 3: Summarize operations by type

```kql
StorageBlobLogs
| where TimeGenerated > ago(1h)
| summarize count() by OperationName
| order by count_ desc
```

Note: If StorageBlobLogs table is empty (logs have not yet arrived), take a screenshot of the empty query result and document that you submitted the query. Logs can take up to 15 minutes to appear after the first diagnostic setting configuration.

Include all query screenshots and answer:

1. KQL uses a pipe (`|`) operator to chain operations — each operation takes the output of the previous one as input. Looking at Query 3, explain in plain English what each line does: what does the `where` clause do, what does `summarize count() by OperationName` do, and what does `order by count_ desc` do?

2. The `StorageBlobLogs` table captures every blob operation including the caller's IP address and the operation duration. What security and operational questions could a security team answer by querying this table that they could not answer from metrics alone?

3. Log Analytics workspace data has a configurable retention period. The default is 30 days. Name two specific business or compliance scenarios where you would need longer retention, and explain how you would achieve it cost-effectively in Azure Monitor.

---

## Part C: Create an Alert Rule (25 Points)

### Step 1: Create an Action Group (10 Points)

Create an action group that sends an email notification:

```bash
az monitor action-group create \
  --resource-group lab13-rg \
  --name "lab13-alerts" \
  --short-name "Lab13" \
  --email-receiver \
    name="Lab Email" \
    email-address="[your-email@txwes.edu]"
```

Verify it was created:

```bash
az monitor action-group list \
  --resource-group lab13-rg \
  --output table
```

Include both outputs.

Answer:

1. The action group currently has only one action (email). In a production environment supporting a 24/7 application, what additional actions would you add to the action group beyond email? For each action you name, explain what operational purpose it serves (for example: who receives it, when it is appropriate, and what they do with it).

### Step 2: Create a Metric Alert Rule (15 Points)

Create an alert rule that fires when the storage account has more than 5 transactions per minute:

```bash
STORAGE_RESOURCE_ID=$(az storage account show \
  --name lab13storage[your-initials] \
  --resource-group lab13-rg \
  --query id \
  --output tsv)

ACTION_GROUP_ID=$(az monitor action-group show \
  --resource-group lab13-rg \
  --name "lab13-alerts" \
  --query id \
  --output tsv)

az monitor metrics alert create \
  --name "lab13-transaction-alert" \
  --resource-group lab13-rg \
  --scopes $STORAGE_RESOURCE_ID \
  --condition "count Transactions > 5" \
  --window-size 1m \
  --evaluation-frequency 1m \
  --action $ACTION_GROUP_ID \
  --severity 3 \
  --description "Alert when storage transactions exceed 5 per minute"
```

Verify the alert rule was created:

```bash
az monitor metrics alert list \
  --resource-group lab13-rg \
  --output table
```

Trigger the alert by generating transactions:

```bash
for i in $(seq 1 10); do
  az storage blob list \
    --account-name lab13storage[your-initials] \
    --account-key $STORAGE_KEY \
    --container-name lab13-container \
    --output none
done
```

Navigate to Azure Monitor > Alerts in the portal and wait 2-3 minutes for the alert to evaluate.

[PORTAL STEPS: Azure Monitor > Alerts — show fired or evaluated alerts]

Take a screenshot of the Azure Monitor Alerts dashboard (even if the alert has not fired yet — show the alert rule exists in the rules list).

Include all command outputs and the screenshot. Answer:

1. The alert rule uses a 1-minute window and 1-minute evaluation frequency. What is the trade-off between very short evaluation windows (like 1 minute) and longer windows (like 15 minutes) for a threshold-based alert? When would you choose a longer window, and what problem does a longer window help avoid?

2. The alert severity was set to 3 (Informational). Azure alert severity levels range from 0 (Critical) to 4 (Verbose). Design a severity assignment scheme for three different alert scenarios: (a) production database CPU at 95% for 10 minutes, (b) a single failed deployment in a dev environment, and (c) a production web application returning 500 errors for 100% of requests. Assign a severity and justify each.

3. After an alert fires and is resolved, the alert state changes to "Resolved." Why is automatic alert resolution important for operations teams? What problem occurs if alert systems only send "fired" notifications and never send "resolved" notifications?

---

## Resource Cleanup

```bash
az group delete \
  --name lab13-rg \
  --yes \
  --no-wait
```

Note: Log Analytics workspaces have a 14-day soft-delete retention after the resource group is deleted. This is expected behavior.

---

## Grading Rubric

| Component | Points | Criteria |
|---|---|---|
| Part A Step 1: Storage account creation and activity | 5 | Commands executed, outputs included |
| Part A Step 2: Metrics chart with two metrics | 10 | Screenshots captured, platform vs. guest collection explained, operational pattern analysis |
| Part A Step 3: Dashboard pin | 10 | Dashboard screenshot captured, production dashboard design described |
| Part B Step 1: Workspace creation | 5 | Commands executed, workspace ID captured |
| Part B Step 2: Diagnostic settings configuration | 10 | Diagnostic settings configured, difference from default collection explained, retention destination analysis |
| Part B Step 3: KQL queries and analysis | 20 | Query screenshots included (or empty results documented), KQL pipe explained, security use cases described, retention scenarios answered |
| Part C Step 1: Action group | 10 | Created successfully, production action group design described |
| Part C Step 2: Alert rule creation and analysis | 15 | Alert rule created, window trade-off explained, severity scheme designed, resolution importance explained |
| **Total** | **100** | |

---

## Troubleshooting

**Metrics not showing data:** Platform metrics are collected automatically but may show "No data" immediately after resource creation. Wait 5 minutes and refresh. Use the time range selector and verify you have selected the correct resource scope.

**StorageBlobLogs table empty:** Log data from diagnostic settings takes 5-15 minutes to appear in Log Analytics after the first configuration. If the table remains empty after 20 minutes, verify the diagnostic settings were applied: `az monitor diagnostic-settings list --resource $STORAGE_RESOURCE_ID/blobServices/default`.

**Action group email not received:** Check spam/junk folders. The email comes from the azure-noreply address at microsoft.com. Also verify the alert fired (check Monitor > Alerts > Alert history).

**Alert rule condition syntax error:** The condition syntax for the CLI is `"count Transactions > 5"` where `count` is the aggregation and `Transactions` is the metric name. Metric names are case-sensitive. Run `az monitor metrics list-definitions --resource $STORAGE_RESOURCE_ID` to see exact metric names.

**Log Analytics workspace query returns "Query could not be completed":** The workspace may be in a different region than expected. Verify with `az monitor log-analytics workspace show --resource-group lab13-rg --workspace-name lab13-workspace`.

---

Lab 13 | CIS-4331 Azure Cloud | Texas Wesleyan University

---

## Part 9 — Challenge Exercise

### Challenge 1: Application Insights Live Metrics and Custom Events
Create an Application Insights resource in your lab resource group. Using the Application Insights JavaScript snippet, instrument a static HTML page hosted on Azure Blob Storage (static website enabled). Add a `trackEvent()` call that fires when a button on the page is clicked, naming the event "LabButtonClicked". Open the Application Insights Live Metrics stream, click the button several times, and capture a screenshot showing the custom event appearing in the Live Metrics stream. Then navigate to Application Insights > Events and run a KQL query against the `customEvents` table to count occurrences grouped by name. Document the instrumentation key setup, the JavaScript snippet, the Live Metrics screenshot, and the KQL query with results. Explain in 2–3 sentences how custom events in Application Insights differ from automatically collected telemetry (requests, dependencies, exceptions) and what business scenarios benefit from custom event tracking.

### Challenge 2: Multi-Resource Dashboard with Alert Integration
Create an Azure Dashboard that displays: (1) a Metrics chart showing CPU utilization for at least one VM or App Service over the past 24 hours, (2) a Log Analytics query tile showing the count of storage transactions per hour for the past 6 hours using KQL, and (3) an Alerts summary tile showing the current fired alert count. Configure the dashboard to auto-refresh every 5 minutes. Share the dashboard with Reader access to a second user in your Azure tenant (or document the sharing steps if a second user is unavailable). Export the dashboard JSON definition using the portal Download button. Document the dashboard JSON, a screenshot of the completed dashboard, and the sharing configuration. Explain in 2–3 sentences how a shared Azure Dashboard supports NOC (Network Operations Center) or on-call rotation practices compared to each engineer having a personal dashboard.

### Reflection Questions
1. The lab configured both a metric alert (storage transaction count) and a Log Analytics diagnostic settings pipeline for the same storage account. Describe a monitoring scenario where a metric alert alone is insufficient and a Log Analytics log query is required to diagnose the root cause — specifically: what does the metric alert tell the operations team, what does it NOT tell them, and what KQL query would they run against the StorageBlobLogs table to get the missing information?
2. Azure Monitor supports four alert signal types: Metric, Log query, Activity Log, and Service Health. For each of the following production scenarios, identify the most appropriate signal type and justify your choice: (a) alert when any user deletes a Key Vault in the subscription; (b) alert when the East US region has a service issue affecting Azure SQL Database; (c) alert when the 95th percentile response time for an App Service exceeds 2 seconds over a 5-minute window; (d) alert when more than 10 authentication failures occur in a 15-minute window, detected from Azure AD sign-in logs.

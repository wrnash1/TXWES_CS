# Quiz: Module 13 - Azure Monitoring and Diagnostics

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service provides personalized recommendations to optimize resource performance, security, and cost?

* A) Azure Monitor
* B) Azure Log Analytics
* C) Azure Advisor
* D) Microsoft Sentinel
* **Correct Answer:** C) Azure Advisor scans your deployment configuration and recommends improvements across five pillars: Cost, Security, Reliability, Performance, and Operational Excellence.
* **Distractor Analysis:**
  * *Why correct:* Azure Advisor analyzes your Azure resources and provides actionable optimization recommendations — it is the proactive advisory service, not a monitoring or alerting tool.
  * *Why A is incorrect:* Azure Monitor collects telemetry metrics and generates alerts but does not provide prioritized optimization recommendations.

---

**Question 2**
Which of the following most accurately describes **Azure Advisor recommendations**?

* A) A free, personalized recommendation engine that analyzes Azure deployments and provides actionable guidance across five pillars — Cost, Security, Reliability, Performance, and Operational Excellence — to help optimize Azure environments.
* B) A telemetry collection platform that ingests metrics and logs from Azure resources and triggers automated alerts when thresholds are crossed.
* C) A query-based log analytics service that stores diagnostic data from Azure resources and allows analysis using the Kusto Query Language (KQL).
* D) A platform health service that provides personalized notifications when Azure regional incidents or planned maintenance affects services you use.
* **Correct Answer:** A) Azure Advisor is a free recommendation engine providing actionable guidance across Cost, Security, Reliability, Performance, and Operational Excellence.
* **Distractor Analysis:**
  * *Why A is correct:* Advisor's defining characteristics are its five pillars of recommendations, its personalization to your specific deployment, and its advisory (non-enforcing) nature.
  * *Why B is incorrect:* That describes Azure Monitor, which collects telemetry and generates alerts.
  * *Why C is incorrect:* That describes Log Analytics (a component of Azure Monitor) with its KQL-based querying capability.
  * *Why D is incorrect:* That describes Azure Service Health, which communicates Azure platform incidents affecting your services.

---

**Question 3**
A web application team wants to receive an email notification whenever the average CPU utilization of their Azure VM exceeds 85% for more than 10 minutes. Which Azure service is used to configure this?

* A) Azure Service Health with a service alert
* B) Azure Advisor with a cost threshold
* C) Azure Monitor with a metric alert rule and action group
* D) Microsoft Defender for Cloud with a security alert
* **Correct Answer:** C) Azure Monitor metric alert rules evaluate resource metrics against defined thresholds and trigger action groups (which can send email) when conditions are met.
* **Distractor Analysis:**
  * *Why C is correct:* Azure Monitor is the platform for metric-based alerting on Azure resources. Action groups define the notification channel (email, SMS, webhook, runbook).
  * *Why A is incorrect:* Service Health alerts notify about Azure platform incidents — they cannot alert on individual VM CPU metrics.
  * *Why B is incorrect:* Azure Advisor provides recommendations but cannot set threshold-based metric alerts.
  * *Why D is incorrect:* Defender for Cloud generates security threat alerts — it does not monitor performance metrics like CPU utilization.

---

**Question 4**
An Azure administrator receives a notification that Azure SQL Database in East US is experiencing degraded performance due to an Azure platform issue. Which Azure service sent this notification?

* A) Azure Monitor metric alert
* B) Azure Advisor security recommendation
* C) Azure Service Health
* D) Microsoft Sentinel incident alert
* **Correct Answer:** C) Azure Service Health provides personalized alerts when Azure platform issues — including service degradation, regional outages, and planned maintenance — affect the services and regions you use.
* **Distractor Analysis:**
  * *Why C is correct:* Service Health is specifically designed to communicate Azure platform-side incidents to affected customers. The admin configured a Service Health alert for their services and regions.
  * *Why A is incorrect:* Azure Monitor alerts are based on your resource's own metrics — not on Azure platform health events.
  * *Why B is incorrect:* Azure Advisor provides optimization recommendations — it does not send real-time platform incident notifications.
  * *Why D is incorrect:* Sentinel alerts are generated from security event analysis — not from Azure platform infrastructure health.

---

**Question 5**
Which Azure monitoring service is the correct choice for querying historical log data from multiple Azure resources using the Kusto Query Language (KQL)?

* A) Azure Service Health
* B) Azure Advisor
* C) Azure Application Insights only
* D) Azure Monitor Log Analytics
* **Correct Answer:** D) Azure Monitor Log Analytics collects and stores log and performance data from Azure resources, enabling querying and analysis using KQL.
* **Distractor Analysis:**
  * *Why D is correct:* Log Analytics Workspaces are the storage and query layer within Azure Monitor for log data. KQL is the query language used to analyze this data.
  * *Why A is incorrect:* Service Health provides Azure platform incident information — it does not store or query resource diagnostic logs.
  * *Why B is incorrect:* Azure Advisor analyzes configurations for recommendations — it does not provide a query interface for historical log data.
  * *Why C is incorrect:* Application Insights is a specialized component of Azure Monitor focused on application performance telemetry — Log Analytics (which Application Insights uses as its backend) is the broader log querying platform.

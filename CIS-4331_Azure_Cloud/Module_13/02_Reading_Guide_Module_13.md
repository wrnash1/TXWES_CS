# Reading Guide: Module 13 - Azure Monitoring and Diagnostics

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

### Introduction

Welcome to **Module 13 - Azure Monitoring and Diagnostics**! This module covers Azure's observability and monitoring services as tested on the **Microsoft Azure Fundamentals (AZ-900)** exam. You cannot manage what you cannot measure — Azure's monitoring tools provide visibility into the health, performance, and security of your cloud resources.

You will learn how Azure Monitor collects and acts on telemetry data, how Log Analytics enables querying of diagnostic logs, how Azure Service Health communicates platform-level incidents, and how Azure Advisor provides proactive optimization recommendations. AZ-900 tests your ability to match a monitoring need to the correct service. Complete the checklist and glossary before beginning the lab.

---

### 1. High-Yield Glossary

Review these essential definitions carefully. The certification exam expects you to know these concepts inside and out:

* **Azure Monitor**: The unified monitoring platform for Azure that collects, analyzes, and acts on telemetry data from Azure resources, applications, and on-premises systems. Azure Monitor ingests metrics (numerical time-series data like CPU%) and logs (structured event data). It can trigger alerts, scale actions, and feed data to dashboards. Azure Monitor is the umbrella service that includes Log Analytics and Application Insights.

* **Log Analytics**: A service within Azure Monitor that collects and stores log and performance data, allowing you to query it using the Kusto Query Language (KQL). Log Analytics Workspaces are the storage containers for this data. AZ-900 tests that Log Analytics is used for querying diagnostic and activity logs from Azure resources.

* **Azure Service Health**: A service that provides personalized alerts and guidance when Azure platform issues — such as planned maintenance, service incidents, or regional outages — affect the services and regions you use. Unlike Azure Monitor (which monitors your resources), Service Health monitors the Azure platform itself on your behalf.

* **Azure Advisor**: A free, personalized recommendation engine that analyzes your Azure deployments and suggests improvements across five pillars: Cost (reduce spending), Security (improve security posture), Reliability (improve resilience), Performance (improve speed), and Operational Excellence (best practices). Advisor does not enforce anything — it advises.

---

### 2. Certification Exam Tips

* **Monitor vs. Advisor vs. Service Health**: AZ-900 frequently tests which monitoring service applies to which scenario. Azure Monitor = telemetry collection and alerting for your resources. Azure Advisor = proactive recommendations for optimization. Azure Service Health = Azure platform incident communication. Know all three and their distinct purposes.
* **Alerts in Azure Monitor**: Azure Monitor can generate alerts when metrics cross thresholds (e.g., CPU > 90% for 5 minutes). Alerts can trigger notifications (email, SMS) or automated actions (VMSS scale-out, Azure Automation runbook). AZ-900 may ask which service creates alerts based on metric thresholds.
* **Application Insights**: A feature of Azure Monitor for application performance monitoring (APM). It tracks request rates, response times, failure rates, and user behavior for web applications. AZ-900 may reference Application Insights as a subcomponent of Azure Monitor for application-level telemetry.
* **Service Health vs. Resource Health**: Service Health reports on platform-wide Azure incidents. Resource Health reports on the health of your specific resource (e.g., is this VM currently impacted by a platform issue). Both are under the Service Health blade in the portal — know the distinction.
* **Study Resource**: The Microsoft Learn monitoring module covers Azure Monitor, Log Analytics, Advisor, and Service Health with interactive exercises. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).

---

### Required Readings & Videos

To prepare for this module's topics, you must complete the following readings and videos:

* **Required Reading:** The Microsoft Learn path for AZ-900 covers Azure monitoring tools including Monitor, Log Analytics, Advisor, and Service Health. Access it at [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* **Required Video:** This free freeCodeCamp course covers Azure monitoring for AZ-900 — watch the monitoring and management section: [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).

---

### Lab & Command Integration

In this week's hands-on lab, you will perform the following steps to apply these concepts:

* **Examine Azure Advisor suggestions for cost and security**: In the Azure portal, navigate to Azure Advisor and review the current recommendations in the Cost and Security categories. Note the estimated monthly savings from cost recommendations.
* **Configure an Azure Monitor metric alert**: Create a metric alert rule on a VM that triggers when CPU percentage exceeds 80% for 5 minutes. Configure an action group to send an email notification when the alert fires.
* **Verify Service Health dashboard status**: Navigate to Azure Service Health and review the current health of Azure services in your region. Explore the Health History and Planned Maintenance sections to understand the types of platform events communicated here.

---

### 3. Study Checklist

* [ ] Read the glossary terms and memorize their definitions.
* [ ] Complete the Azure monitoring unit in [Microsoft Learn – AZ-900 Azure Management and Governance](https://learn.microsoft.com/en-us/training/paths/describe-azure-management-governance/).
* [ ] Watch the monitoring section of [Microsoft Azure Fundamentals Full Course by freeCodeCamp](https://www.youtube.com/watch?v=NPEsD6n9A_I).
* [ ] Review the lab instructions for Advisor review, alert creation, and Service Health exploration.
* [ ] Proceed to the weekly hands-on lab activity.

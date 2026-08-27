# Quiz: Module 16 - Final Exam Prep & AZ-900 Certification

## Course: CIS-4331_Azure_Cloud (Microsoft Azure Fundamentals (AZ-900))

---

**Question 1**
Which Azure service should you use when you need to enforce that all Azure VMs deployed across your organization must use only approved VM SKU sizes, automatically blocking non-compliant deployments?

* A) Azure Advisor
* B) Azure Policy with a "Deny" effect
* C) Azure Resource Manager tags
* D) Microsoft Defender for Cloud Secure Score
* **Correct Answer:** B) Azure Policy with a "Deny" effect evaluates resource deployments against defined rules and blocks any that do not conform to the approved SKU list.
* **Distractor Analysis:**
  * *Why B is correct:* Azure Policy with Deny effect is the only mechanism that actively blocks non-compliant deployments at submission time.
  * *Why A is incorrect:* Azure Advisor provides recommendations — it cannot block deployments.
  * *Why C is incorrect:* Tags are metadata labels — they have no enforcement capability and cannot block deployments.
  * *Why D is incorrect:* Defender for Cloud's Secure Score measures overall security posture — it does not enforce deployment restrictions.

---

**Question 2**
A VM deployed in a single Azure datacenter fails due to a power outage in that datacenter. Which architecture change would most cost-effectively meet a 99.99% SLA for this VM workload going forward?

* A) Add a second VM in the same datacenter within the same Availability Set
* B) Deploy two identical VMs across two different Availability Zones in the same Azure region
* C) Enable auto-shutdown on the VM to reduce operational costs
* D) Move the VM to a Spot Instance to improve resilience
* **Correct Answer:** B) Two VMs deployed across separate Availability Zones within the same region achieve 99.99% SLA by ensuring no single datacenter failure can take down both instances.
* **Distractor Analysis:**
  * *Why B is correct:* Availability Zones are physically separate datacenters within a region. Two instances across zones gives 99.99% SLA per Microsoft's published guarantees.
  * *Why A is incorrect:* An Availability Set distributes VMs across fault/update domains within one datacenter or cluster area — it achieves 99.95% SLA but does not protect against full datacenter failure.
  * *Why C is incorrect:* Auto-shutdown reduces costs but has no effect on availability or SLA.
  * *Why D is incorrect:* Spot Instances are the least reliable option — they can be evicted with 30-second notice and are explicitly not suitable for high-availability workloads.

---

**Question 3**
A developer accidentally committed the Azure storage account access key to a public GitHub repository. Using Azure best practices, which immediate remediation steps are correct?

* A) Delete the GitHub repository and hope the key was not seen before deletion
* B) Rotate the storage account access key immediately to invalidate the exposed key, then store the new key in Azure Key Vault and update the application to retrieve it via Managed Identity
* C) Apply a CanNotDelete lock to the storage account to prevent unauthorized deletion
* D) Enable Azure DDoS Protection on the storage account's VNet
* **Correct Answer:** B) Rotating the key immediately invalidates the exposed credential. Storing the replacement key in Key Vault and using Managed Identity prevents future hardcoding.
* **Distractor Analysis:**
  * *Why B is correct:* This is the complete Microsoft-recommended response: rotate immediately (revoke exposure), then adopt Key Vault + Managed Identity (prevent recurrence).
  * *Why A is incorrect:* The key was already exposed publicly — simply deleting the repository does not invalidate the key. Anyone who saw it can still use it.
  * *Why C is incorrect:* A CanNotDelete lock prevents accidental resource deletion — it does not revoke an exposed access key or protect against unauthorized API calls using that key.
  * *Why D is incorrect:* DDoS Protection defends against volumetric network attacks — it does not protect storage accounts from API-level access using a valid (though stolen) key.

---

**Question 4**
Which combination of Azure cost management features best supports an organization that wants to (1) estimate costs before migrating to Azure, (2) monitor ongoing cloud spending, and (3) reduce costs on stable, predictable workloads?

* A) TCO Calculator + Azure Cost Management budgets + Azure Spot Instances
* B) Azure Pricing Calculator + Azure Cost Management budgets + Azure Reservations
* C) Azure Advisor + Azure Monitor + Azure Blueprints
* D) TCO Calculator + Azure Cost Management budgets + Azure Reservations
* **Correct Answer:** D) The TCO Calculator builds the pre-migration business case; Cost Management monitors ongoing spending; Reservations reduce costs for stable workloads.
* **Distractor Analysis:**
  * *Why D is correct:* TCO Calculator = pre-migration comparison. Cost Management budgets = ongoing monitoring and alerts. Reservations = commitment-based savings for predictable workloads.
  * *Why B is incorrect:* The Pricing Calculator estimates individual Azure service costs — for comparing total on-premises vs. Azure costs before migration, the TCO Calculator is the correct choice.
  * *Why A is incorrect:* Spot Instances are for interruptible workloads with no reliability guarantee — they are not appropriate for stable, predictable production workloads.
  * *Why C is incorrect:* Advisor, Monitor, and Blueprints are governance and observability tools — none of them address pre-migration cost estimation or commitment-based discounts.

---

**Question 5**
Looking across all AZ-900 domains, which statement correctly pairs each Azure service with its primary purpose?

* A) Azure Policy = proactive cost saving recommendations; Azure Advisor = blocking non-compliant deployments; Azure Monitor = managing identity and access.
* B) Azure Key Vault = storing secrets and certificates securely; Azure Bastion = browser-based RDP/SSH without VM public IPs; Azure ExpressRoute = private dedicated connectivity bypassing the public internet.
* C) Azure Availability Zones = disaster recovery across regions 300 miles apart; Azure Region Pairs = datacenter-level fault isolation within one region; ARM Templates = real-time cost monitoring.
* D) Microsoft Sentinel = proactive VM security posture scoring; Defender for Cloud = enterprise SIEM for multi-source log analysis; Azure Service Health = managing user identities.
* **Correct Answer:** B) Key Vault stores secrets; Bastion provides secure VM access without public IPs; ExpressRoute provides private dedicated connectivity — all three descriptions are accurate.
* **Distractor Analysis:**
  * *Why B is correct:* All three service-to-purpose mappings in option B are factually accurate and align with AZ-900 exam definitions.
  * *Why A is incorrect:* The services are swapped — Azure Advisor provides recommendations; Azure Policy blocks non-compliant deployments; Azure Monitor handles telemetry, not identity.
  * *Why C is incorrect:* The definitions are reversed — Availability Zones are datacenter-level isolation within one region; Region Pairs span geographic distances for regional disaster recovery.
  * *Why D is incorrect:* The services are swapped — Sentinel is the enterprise SIEM; Defender for Cloud provides security posture and Secure Score; Service Health reports Azure platform incidents, not identity management.

---

### Question 6 (5 points)

A company is migrating a legacy web application to Azure. The application must scale up to handle traffic spikes during business hours but needs minimal cost during off-hours. The operations team does not want to manage the underlying operating system. Which Azure compute service best fits these requirements?

- A) Azure Virtual Machine Scale Sets with manual scaling rules
- B) Azure App Service with auto-scaling configured at the Standard tier or above
- C) Azure Container Instances with a custom container image
- D) Azure Virtual Machines with an auto-shutdown schedule

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure App Service is a PaaS compute service — the underlying OS, patching, and infrastructure are managed by Microsoft. Auto-scaling is available at the Standard tier and above, allowing the application to scale out during traffic spikes and scale in during off-hours automatically. This combination directly meets both requirements: no OS management and automatic scaling.
  - *Why A is incorrect:* VM Scale Sets scale VMs automatically but the team is still responsible for OS patching, updates, and configuration management. The requirement to not manage the OS eliminates IaaS-based options.
  - *Why C is incorrect:* Azure Container Instances runs individual containers on-demand but does not provide built-in auto-scaling based on HTTP traffic patterns. It is suited for short-lived, event-driven workloads rather than persistent web applications with traffic-based scaling.
  - *Why D is incorrect:* A single VM with an auto-shutdown schedule reduces cost by stopping the VM at scheduled times, but this makes the application unavailable during off-hours rather than simply reducing resource allocation. This does not support continuous availability at lower cost.

---

### Question 7 (5 points)

A company wants to connect their on-premises headquarters network to their Azure virtual network with a dedicated private connection that does not traverse the public internet, provides consistent bandwidth, and supports latency-sensitive financial applications. Which Azure networking service meets these requirements?

- A) Azure VPN Gateway with Site-to-Site connection
- B) Azure Virtual Network Peering
- C) Azure ExpressRoute
- D) Azure Traffic Manager

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Azure ExpressRoute provides a dedicated private connection between on-premises infrastructure and Azure through a connectivity provider. Traffic does not traverse the public internet, providing consistent latency, reliable bandwidth, and the security posture required for latency-sensitive financial workloads. ExpressRoute supports bandwidths from 50 Mbps to 100 Gbps.
  - *Why A is incorrect:* Azure VPN Gateway Site-to-Site creates an encrypted tunnel over the public internet. While it provides security through encryption, it still traverses the public internet, meaning latency is variable and bandwidth is limited (up to 10 Gbps for VpnGw5 SKU). For latency-sensitive financial applications, internet variability is unacceptable.
  - *Why B is incorrect:* Azure VNet Peering connects two Azure virtual networks to each other within the Azure backbone. It does not connect on-premises infrastructure to Azure. VNet Peering has no on-premises component.
  - *Why D is incorrect:* Azure Traffic Manager is a DNS-based global load balancing service that routes user requests to the best endpoint. It operates at the DNS layer and does not provide physical network connectivity between on-premises locations and Azure.

---

### Question 8 (5 points)

An organization has deployed Azure resources across 12 subscriptions organized under 4 management groups. They want a single view showing the security posture and security recommendations for all 12 subscriptions together. Which Azure service provides this unified multi-subscription security view?

- A) Azure Monitor with a Log Analytics workspace collecting logs from all subscriptions
- B) Microsoft Defender for Cloud at the management group scope
- C) Azure Policy compliance dashboard at the root management group
- D) Azure Service Health for all subscriptions

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Microsoft Defender for Cloud can be enabled at the management group scope, which automatically covers all subscriptions under that management group. The Defender for Cloud Overview and Recommendations pages provide a unified view of the Secure Score and security recommendations across all subscriptions in scope. This is the designed use case for multi-subscription security posture management.
  - *Why A is incorrect:* Azure Monitor with Log Analytics can collect and correlate log data across subscriptions for monitoring and investigation. However, it does not provide a security posture score, categorized security recommendations, or the Secure Score concept. Log Analytics is for log analysis, not security posture scoring.
  - *Why C is incorrect:* The Azure Policy compliance dashboard shows configuration compliance against assigned policies. It does not provide security recommendations, vulnerability assessments, or the Secure Score that Defender for Cloud provides. Policy compliance and security posture are related but different views.
  - *Why D is incorrect:* Azure Service Health reports on Azure platform incidents, planned maintenance, and health advisories for the customer's subscriptions. It does not assess or score the security posture of deployed resources or provide security recommendations.

---

### Question 9 (5 points)

An architect is designing an Azure solution for a startup. The startup processes customer orders through a web application backed by an Azure SQL Database. They want the highest availability for the database with automatic failover to a secondary region if the primary region becomes unavailable. Which Azure SQL Database feature provides this capability?

- A) Azure SQL Database Elastic Pools
- B) Azure SQL Database Auto-failover groups
- C) Azure SQL Database point-in-time restore
- D) Azure SQL Database Active Geo-Replication with manual failover only

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Auto-failover groups in Azure SQL Database create a continuous replication relationship between a primary database and a secondary in a different region. When a regional outage is detected, automatic failover promotes the secondary to primary without requiring manual intervention, and the connection string endpoint remains the same so the application reconnects automatically. This is the correct solution for automatic cross-region failover.
  - *Why A is incorrect:* Elastic Pools allow multiple databases to share a pool of resources (DTUs or vCores) for cost efficiency. They address resource sharing and cost optimization, not cross-region high availability or automatic failover.
  - *Why C is incorrect:* Point-in-time restore allows recovery of a database to a previous state within the backup retention window (up to 35 days). It is a data recovery mechanism for logical data corruption, not a high-availability solution for regional outages. Restore operations take time and require manual initiation.
  - *Why D is incorrect:* Active Geo-Replication creates a readable secondary in another region, but failover with Active Geo-Replication is manual — the DBA must explicitly initiate the failover. The question requires automatic failover, which is the distinguishing characteristic of Auto-failover groups over Active Geo-Replication.

---

### Question 10 (5 points)

A company stores sensitive employee data in Azure Blob Storage. The security team requires that the data be encrypted using encryption keys that the company fully controls and can rotate on their own schedule, rather than using Microsoft-managed keys. Which Azure storage configuration meets this requirement?

- A) Enable Azure Storage service-side encryption with Microsoft-managed keys (the default)
- B) Configure Customer-Managed Keys (CMK) in Azure Key Vault for the storage account
- C) Encrypt the data in the application before uploading it and store the key in an on-premises HSM
- D) Enable blob versioning on the storage account to maintain encrypted copies of all versions

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Storage supports Customer-Managed Keys (CMK) where the encryption keys are stored in an Azure Key Vault that the customer controls. The company manages key creation, rotation schedule, and revocation. If the key is revoked or the Key Vault is made inaccessible, the encrypted data becomes unreadable, giving the company full control. CMK meets the requirement while maintaining Azure-native integration.
  - *Why A is incorrect:* Microsoft-managed keys are the default and are controlled by Microsoft, not the customer. Microsoft rotates these keys on its own schedule. This is the opposite of what the requirement specifies.
  - *Why C is incorrect:* Client-side encryption with on-premises key storage is technically a valid security approach, but it requires the application to manage all encryption and decryption operations and introduces operational complexity for an on-premises HSM. The question asks for Azure configuration, and using Azure Key Vault CMK is the standard Azure-native approach that meets the requirement without on-premises dependencies.
  - *Why D is incorrect:* Blob versioning automatically maintains copies of blobs as they are modified or deleted — it is a data protection and audit feature. It does not affect the encryption key management model. Versioning has no relationship to who controls the encryption keys.

---

### Question 11 (5 points)

A team is evaluating Azure compute services for a new microservices architecture consisting of 8 independent services that need to communicate with each other, scale independently, and be deployed using container images. Which Azure service is most appropriate?

- A) Azure App Service with eight deployment slots
- B) Azure Kubernetes Service (AKS)
- C) Azure Container Instances with eight separate container groups
- D) Azure Virtual Machine Scale Sets with Docker installed on each VM

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Kubernetes Service (AKS) is designed for orchestrating multi-container microservices architectures. It manages container scheduling, inter-service networking, independent scaling per service (using Kubernetes Deployments and Horizontal Pod Autoscaler), rolling updates, and service discovery. For 8 independent services that scale independently and communicate with each other, AKS is the purpose-built solution.
  - *Why A is incorrect:* Azure App Service deployment slots are used for blue/green deployments of a single web application — swapping between staging and production versions. Deployment slots are not independent microservices; each App Service plan runs one application with multiple deployment versions, not eight independently-scaling services.
  - *Why C is incorrect:* Azure Container Instances runs individual containers (or small groups) on-demand without persistent orchestration. Running eight separate container groups provides no built-in service discovery, load balancing between instances, or coordinated scaling. ACI is suited for short-lived isolated workloads, not persistent interconnected microservices.
  - *Why D is incorrect:* Installing Docker on VM Scale Sets is an IaaS approach that requires the team to manage OS patching, Docker installation, container networking, and orchestration manually. This is the approach AKS was designed to replace. The overhead of managing the full stack on VMs defeats the purpose of containers for this use case.

---

### Question 12 (5 points)

A data analyst at a retail company wants to run complex analytical queries across 10 years of transaction data stored in Azure Blob Storage (Data Lake). The queries involve aggregating billions of rows and joining multiple large tables. Which Azure analytics service is most appropriate for this workload?

- A) Azure SQL Database General Purpose tier with increased vCores
- B) Azure Cosmos DB with a SQL API container
- C) Azure Synapse Analytics with a Dedicated SQL Pool
- D) Azure Database for PostgreSQL Flexible Server

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* Azure Synapse Analytics Dedicated SQL Pool is purpose-built for large-scale analytical workloads using Massively Parallel Processing (MPP) architecture. It can query petabytes of data stored in Azure Data Lake Storage through external tables or direct PolyBase queries, distribute complex aggregations and joins across hundreds of compute nodes, and scale independently from storage. This is the designed solution for multi-billion-row analytical queries on data lake data.
  - *Why A is incorrect:* Azure SQL Database is an OLTP (Online Transaction Processing) database optimized for concurrent transactional workloads with many small reads and writes. Even with increased vCores, a single-node SQL Database is not architected for MPP analytical queries over billions of rows and does not natively query data from Blob Storage.
  - *Why B is incorrect:* Azure Cosmos DB is a NoSQL document, key-value, graph, and column-family database optimized for globally distributed applications requiring low-latency reads and writes. It does not perform well for complex multi-table JOIN and aggregation queries across historical datasets, and is not designed for analytical warehouse workloads.
  - *Why D is incorrect:* Azure Database for PostgreSQL Flexible Server is a fully managed OLTP relational database. While PostgreSQL has analytical capabilities, it is a single-node service that cannot match the MPP scale needed for billions of rows of transaction data. It does not natively integrate with Azure Data Lake Storage for external table queries.

---

### Question 13 (5 points)

A company uses Azure Active Directory (Microsoft Entra ID) to manage employee identities. They want to ensure that employees can use their corporate credentials to sign in to both Azure resources and their on-premises applications without maintaining two separate passwords. Which scenario describes this capability?

- A) Azure AD B2C for external user identity federation
- B) Hybrid identity with Microsoft Entra Connect synchronizing on-premises Active Directory identities to Entra ID
- C) Azure AD Privileged Identity Management enabling just-in-time access
- D) Azure AD Conditional Access requiring MFA for all cloud app sign-ins

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Microsoft Entra Connect (formerly Azure AD Connect) synchronizes on-premises Active Directory user accounts and password hashes to Microsoft Entra ID. Once synchronized, employees use the same username and password (or seamless SSO token) for both on-premises applications and Azure/Microsoft 365 services. This hybrid identity model eliminates the need for separate cloud and on-premises credentials.
  - *Why A is incorrect:* Azure AD B2C (Business to Consumer) is a separate identity service for managing external customer identities for public-facing applications. It is designed for consumer-facing apps, not for synchronizing corporate employee identities between on-premises AD and Azure.
  - *Why C is incorrect:* Privileged Identity Management (PIM) provides just-in-time activation of privileged roles to reduce standing administrative access. It manages role activation, not password synchronization or single sign-on between on-premises and cloud environments.
  - *Why D is incorrect:* Conditional Access policies enforce additional authentication requirements (like MFA) under certain conditions. While Conditional Access can be used alongside hybrid identity, it does not itself synchronize identities or eliminate the need for separate passwords.

---

### Question 14 (5 points)

Across all AZ-900 service domains, which of the following statements about the Azure shared responsibility model is correct?

- A) In an IaaS model, Microsoft is responsible for securing the guest operating system, application data, and identity management
- B) In a SaaS model, the customer retains responsibility for managing network controls and the physical datacenter
- C) Regardless of cloud service model (IaaS, PaaS, SaaS), the customer always retains responsibility for their own data and identity/access management
- D) In a PaaS model, Microsoft assumes responsibility for the customer's application code and database schema design

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* The Azure shared responsibility model consistently places data protection and identity/access management on the customer regardless of service model. In IaaS, PaaS, and SaaS, the customer owns their data and is responsible for who has access to it. Microsoft's responsibility grows as you move from IaaS to SaaS (taking on OS, runtime, platform), but customer data ownership and identity management always remain with the customer.
  - *Why A is incorrect:* In IaaS, Microsoft is responsible for the physical infrastructure, network, and hypervisor. The guest OS, applications, data, and identity management are the customer's responsibility. Customers patch the OS, manage applications, and control identity in an IaaS model.
  - *Why B is incorrect:* In SaaS, Microsoft takes responsibility for nearly the entire stack — infrastructure, networking, OS, runtime, application, and data storage infrastructure. The customer is not responsible for network controls or physical datacenter management in a SaaS model. Customer responsibilities in SaaS are primarily limited to data, access management, and device security.
  - *Why D is incorrect:* In PaaS, Microsoft manages the underlying platform (OS, runtime, middleware) but the customer is still responsible for the application code, data, and schema design. Microsoft does not design or secure customer application logic or database structures — these are always customer responsibilities.

---

### Question 15 (5 points)

A company is preparing for the AZ-900 exam and encounters this question: "Which service provides a way to run event-driven code without managing servers, charging only for execution time with no idle cost?" The answer options include Azure Functions, Azure Logic Apps, Azure App Service, and Azure Container Apps. Which answer is correct, and why do the other options not fit?

- A) Azure Logic Apps — it provides serverless workflow automation with per-execution billing
- B) Azure Functions with the Consumption plan — it runs event-triggered code with per-execution billing (per invocation and per GB-second of memory) and zero cost when idle
- C) Azure App Service Free tier — it provides serverless hosting with no idle charges
- D) Azure Container Apps — it provides serverless containers that scale to zero with per-request billing

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Azure Functions on the Consumption plan is the canonical Azure serverless compute service for event-driven code. Billing is based on the number of executions and execution duration (GB-seconds of memory consumed). When there are no invocations, there is zero cost. This matches the description: event-driven, no server management, pay-per-execution, no idle cost.
  - *Why A is incorrect:* Azure Logic Apps is a serverless workflow orchestration service using a visual designer with connectors. It is billed per action execution (connector calls). While it shares the serverless billing model, it is designed for integrating services and automating workflows, not for running arbitrary code. The question specifically asks about running code, making Functions the better answer.
  - *Why C is incorrect:* Azure App Service Free tier provides a small amount of shared compute for lightweight apps. It is not serverless — the app service plan is always allocated (even if the app is idle). There is no per-execution billing model. Free tier is a fixed allocation with usage caps, not a true serverless model.
  - *Why D is incorrect:* Azure Container Apps can scale to zero and provides serverless-style billing for containerized workloads. However, the question asks specifically about running event-driven code without server management, which more precisely describes Azure Functions. Container Apps are primarily for microservices and containerized applications, while Functions are the AZ-900 canonical answer for event-driven serverless code execution.

---

### Question 16 (5 points)

A company's security team wants to ensure that no Azure resource group in their environment can ever be accidentally deleted by a developer with Contributor access. They also want this protection to apply automatically to all new resource groups created in the future without requiring a manual step each time. Which combination of Azure governance features accomplishes both requirements?

- A) Assign a "ReadOnly" lock directly on each resource group after it is created
- B) Use Azure Policy with a "DeployIfNotExists" effect to automatically apply a "CanNotDelete" resource lock to every resource group upon creation
- C) Assign the Contributor role to a security group and instruct developers not to delete resource groups
- D) Enable Microsoft Defender for Cloud on all subscriptions to monitor for deletion activities

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Policy with the "DeployIfNotExists" (DINE) effect can automatically deploy a child resource — including a resource lock — when a parent resource (such as a resource group) is created or updated. By assigning a policy that deploys a "CanNotDelete" lock on all resource groups, the protection is applied automatically to new resource groups without manual intervention. This satisfies both requirements: prevention of deletion and automatic enforcement going forward.
- *Why A is incorrect:* Manually applying a "ReadOnly" lock to each resource group after creation addresses the deletion prevention requirement but fails the automation requirement. A developer creating a new resource group would not have the lock automatically applied — someone would need to add it manually each time.
- *Why C is incorrect:* Relying on developers to self-enforce a policy is not a governance control. RBAC Contributor access includes delete permissions; without a resource lock, any developer with Contributor rights can delete a resource group regardless of informal instructions.
- *Why D is incorrect:* Microsoft Defender for Cloud monitors and alerts on security posture and suspicious activity. It can detect deletion events after the fact, but it does not prevent deletions. Monitoring and alerting is a detective control, not a preventive control.

---

### Question 17 (5 points)

An organization wants to grant a third-party auditing firm temporary read-only access to their Azure resources for a 30-day compliance review. The auditing firm's staff do not have corporate Azure AD accounts. Which Microsoft Entra ID feature is most appropriate for providing this access?

- A) Create local Azure AD user accounts for each auditor and assign the Reader role at the subscription scope
- B) Use Microsoft Entra ID B2B (External Identities) to invite the auditors as guest users, then assign the Reader role with a Conditional Access policy enforcing MFA
- C) Share the subscription's root account credentials with the auditing firm for the 30-day period
- D) Enable Azure AD Privileged Identity Management (PIM) and create time-limited Owner role assignments for each auditor

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Microsoft Entra External Identities (B2B collaboration) allows organizations to invite external users — using their own existing identity provider (Microsoft, Google, or any SAML-compliant IdP) — as guest users without creating new managed accounts. Assigning Reader role limits access to read-only, and a Conditional Access policy enforcing MFA ensures the external access is secured. When the 30-day review ends, the guest accounts can be removed or expire automatically. This is the purpose-built Microsoft pattern for external partner/auditor access.
- *Why A is incorrect:* Creating local Azure AD accounts for external auditors requires the organization to manage credentials for accounts it does not own. When the engagement ends, the accounts must be manually deleted. This approach creates unnecessary administrative overhead and security risk compared to B2B guest access where the auditors authenticate with their own credentials.
- *Why C is incorrect:* Sharing root account or global admin credentials violates the principle of least privilege and creates a severe security risk. There is no audit trail of individual actions, credentials cannot be scoped to read-only, and the credentials must be changed after the engagement — creating operational disruption.
- *Why D is incorrect:* PIM with Owner role assignments grants privileged administrative access — Owner is the highest Azure RBAC role, allowing full resource management including deletion. An auditor requires read-only access. Assigning Owner via PIM is both excessive (wrong role) and creates an elevated-privilege risk even with time limits.

---

### Question 18 (5 points)

A company needs to deploy an identical set of Azure resources — including a virtual network, an Azure Key Vault with specific access policies, an Azure Policy assignment, and RBAC role assignments — across 15 new project subscriptions. The deployment must be repeatable, version-controlled, and include governance controls from day one. Which Azure service is most appropriate for this requirement?

- A) Azure Resource Manager (ARM) templates deployed individually to each of the 15 subscriptions
- B) Azure Blueprints to package the ARM templates, Policy assignments, and RBAC assignments into a single versioned blueprint definition and assign it to each subscription
- C) Azure Advisor to recommend the correct resource configuration for each subscription
- D) Azure Cost Management budgets applied to each subscription to enforce spending limits

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Blueprints is designed specifically for deploying a governed, repeatable package of Azure resources across multiple subscriptions. A blueprint definition can contain ARM templates (for infrastructure), Azure Policy assignments (for governance rules), and RBAC role assignments (for access control) in a single versioned artifact. When assigned to a subscription, all components deploy together. Blueprint assignments can also lock deployed resources to prevent drift, and the relationship between the blueprint and the assigned subscription is tracked for compliance. This addresses all requirements: repeatability, versioning, and day-one governance.
- *Why A is incorrect:* ARM templates can deploy the infrastructure components but cannot natively include Policy assignments or RBAC role assignments in the same versioned, tracked artifact. Deploying ARM templates individually to 15 subscriptions requires scripting the RBAC and Policy assignments separately, has no built-in assignment tracking, and cannot lock resources to prevent post-deployment drift.
- *Why C is incorrect:* Azure Advisor analyzes deployed resources and provides recommendations for cost, security, reliability, and performance. It is an advisory tool — it does not deploy resources or enforce governance configurations.
- *Why D is incorrect:* Azure Cost Management budgets set spending thresholds and trigger alerts or actions when spending approaches or exceeds the budget. Budgets address cost governance but do not deploy infrastructure, assign policies, or configure RBAC.

---

### Question 19 (5 points)

A company runs a business-critical web application on Azure. The operations team wants a single service that can: (1) collect performance metrics from the web application's App Service and Azure SQL Database, (2) alert the team when response time exceeds 2 seconds, and (3) visualize 30-day performance trends on a shared dashboard. Which Azure service provides all three capabilities natively?

- A) Azure Service Health — tracks Azure platform health and planned maintenance events
- B) Azure Monitor — collects metrics and logs, supports alert rules with action groups, and provides workbooks and dashboards for visualization
- C) Microsoft Sentinel — provides SIEM capabilities for security event analysis and threat detection
- D) Azure Network Watcher — provides network performance monitoring and packet capture capabilities

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* Azure Monitor is the unified observability platform for Azure resources. It collects metrics (CPU, response time, DTU consumption) from App Service and Azure SQL Database natively through Azure Monitor metrics. Alert rules can be configured on any metric — including response time — with action groups that send emails, SMS, or trigger Logic Apps when thresholds are breached. Azure Monitor Workbooks and the shared Azure dashboard feature enable visualization of historical metric trends across any configured time range. All three requirements are met within a single service.
- *Why A is incorrect:* Azure Service Health reports on the health of the Azure platform itself — incidents affecting Azure regions or services, planned maintenance windows, and health advisories. It does not collect application-level performance metrics, support custom alert rules on application response times, or visualize application performance trends.
- *Why C is incorrect:* Microsoft Sentinel is a cloud-native SIEM (Security Information and Event Management) and SOAR platform for security event collection, threat detection, and incident response. While Sentinel can ingest logs, its purpose is security analytics, not application performance monitoring or metric-based alerting.
- *Why D is incorrect:* Azure Network Watcher provides network-level diagnostics — including packet capture, connection troubleshooting, flow logs, and topology visualization — for Azure virtual network resources. It monitors network infrastructure performance and connectivity, not application-layer performance metrics from App Service or SQL Database.

---

### Question 20 (5 points)

Looking across all AZ-900 exam domains, a candidate encounters a comprehensive review question: "Which statement correctly describes how Azure's geographic infrastructure — regions, region pairs, Availability Zones, and the global network — work together to support high availability and disaster recovery?" Which answer is accurate?

- A) An Azure region is a single datacenter; Availability Zones are groups of multiple regions; region pairs connect continents; and the Azure global network is a public internet path between regions
- B) An Azure region is a geographic area containing one or more datacenters; Availability Zones are physically separate datacenters within a single region connected by high-speed private network links; region pairs are two regions within the same geography separated by at least 300 miles; and the Azure global network is a private fiber backbone connecting all Azure regions without traversing the public internet
- C) Availability Zones are the same as Availability Sets; region pairs provide millisecond latency between continents; and the Azure global network routes traffic through public internet exchange points
- D) An Azure region always contains exactly three datacenters; region pairs are located on different continents to maximize distance; Availability Zones are virtual constructs with no physical separation; and the Azure global network is managed by third-party ISPs

**Correct Answer:** B

**Distractor Analysis:**

- *Why B is correct:* All four infrastructure concepts in option B are accurately described per Microsoft's AZ-900 documentation. An Azure region is a geographic area with one or more datacenters (some regions have many). Availability Zones are physically separate buildings within a region, each with independent power, cooling, and networking, connected by dedicated high-speed private fiber. Region pairs are two Azure regions in the same geopolitical boundary (e.g., East US / West US) separated by at least 300 miles to protect against regional disasters; Azure serializes updates to region pairs to prevent simultaneous maintenance outages. The Azure global network is Microsoft's owned private fiber backbone — traffic between Azure regions travels over Microsoft's private network, not the public internet, providing lower latency and higher reliability.
- *Why A is incorrect:* Multiple definitions are wrong. A region is not a single datacenter — it is a collection of datacenters. Availability Zones are not groups of regions — they are isolated locations within one region. The Azure global network is not public internet — it is Microsoft's private fiber backbone.
- *Why C is incorrect:* Availability Zones and Availability Sets are different constructs. Availability Sets distribute VMs across fault/update domains within a datacenter and achieve 99.95% SLA; Availability Zones are separate physical buildings within a region and achieve 99.99% SLA. Region pairs do not provide millisecond inter-continental latency — they are geographically separated for DR purposes, not low-latency connectivity. The Azure global network does not route through public internet exchange points.
- *Why D is incorrect:* Azure regions do not always contain exactly three datacenters — the number varies by region. Region pairs are within the same geography (e.g., same country or continent) to comply with data residency regulations, not on different continents. Availability Zones have genuine physical separation — they are not virtual constructs. The Azure global network is owned and operated by Microsoft, not third-party ISPs.

---

Module 16 Quiz (extended) | CIS-4331 Azure Cloud | Texas Wesleyan University

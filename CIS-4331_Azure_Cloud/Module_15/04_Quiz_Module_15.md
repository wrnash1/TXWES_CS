# Quiz: Module 15 — Azure Compliance, Privacy, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Instructions

Select the single best answer for each question. Each question is worth 10 points. This quiz is aligned to AZ-900 exam objectives in the Management and Governance domain.

---

## Question 1

A compliance officer at a financial services company needs to download the most recent SOC 2 Type II audit report for Azure to share with an external auditor. Where should they go to obtain this document?

A. Microsoft Trust Center — public overview page
B. Azure Cost Management + Billing
C. Service Trust Portal
D. Azure Advisor

**Correct Answer: C**

### Distractor Analysis — Q1

**A — Incorrect.** The Microsoft Trust Center is a public-facing transparency website that describes Microsoft's compliance posture in general terms. It does not provide downloadable audit reports or certification evidence documents.

**B — Incorrect.** Azure Cost Management + Billing is a financial management tool for monitoring and optimizing Azure spending. It has no function related to compliance documentation or audit reports.

**C — Correct.** The Service Trust Portal at servicetrust.microsoft.com is the authenticated portal where Microsoft publishes detailed compliance documentation including SOC 1, SOC 2, ISO 27001, FedRAMP, and other third-party audit reports. This is where auditors and compliance teams go to download formal evidence.

**D — Incorrect.** Azure Advisor provides recommendations to optimize cost, security, reliability, performance, and operational excellence. It does not contain or link to compliance audit reports.

---

## Question 2

A healthcare organization is deploying an electronic health records application in Azure that will store and process protected health information. Before going live, their compliance team requires that a specific contractual agreement be in place with Microsoft. What is this agreement called?

A. Service Level Agreement (SLA)
B. Business Associate Agreement (BAA)
C. Data Processing Addendum (DPA)
D. Master Services Agreement (MSA)

**Correct Answer: B**

### Distractor Analysis — Q2

**A — Incorrect.** A Service Level Agreement defines uptime and performance commitments for Azure services. It addresses availability, not the handling of protected health information or HIPAA compliance obligations.

**B — Correct.** Under HIPAA, any organization (business associate) that processes protected health information on behalf of a covered entity must have a signed Business Associate Agreement with the service provider. Microsoft provides a HIPAA BAA to Azure customers through the Microsoft Online Services Terms. Without it, using Azure for PHI is a HIPAA violation.

**C — Incorrect.** The Data Processing Addendum governs GDPR obligations between Microsoft and Azure customers for EU personal data. It is the relevant contractual instrument for GDPR, not HIPAA.

**D — Incorrect.** A Master Services Agreement is a general commercial contract framework. It is not specific to HIPAA or health data processing requirements.

---

## Question 3

An Azure administrator creates a policy definition with a Deny effect and assigns it at the subscription scope with the following rule: if a storage account's "supportsHttpsTrafficOnly" property is false, deny the deployment. A developer attempts to create a storage account with HTTP access enabled. What happens?

A. The storage account is created and flagged as noncompliant in the compliance dashboard.
B. The storage account is created and Azure automatically enables HTTPS afterward.
C. The deployment is blocked and the developer receives an error message.
D. The developer receives an email alert but the storage account is still created.

**Correct Answer: C**

### Distractor Analysis — Q3

**A — Incorrect.** This describes the Audit effect, not Deny. The Audit effect allows the resource to be created but marks it noncompliant. The Deny effect blocks creation entirely.

**B — Incorrect.** This describes the DeployIfNotExists or Modify effect, which automatically remediates a missing or incorrect configuration. Deny does not create the resource and then modify it — it prevents creation entirely.

**C — Correct.** The Deny effect blocks the resource deployment at the point of the ARM API call. The storage account is not created, and the developer receives an error response indicating that the resource violates an assigned policy.

**D — Incorrect.** Email alerts are associated with Azure Monitor alerts and budget alerts in Cost Management. Policy Deny effects do not send emails — they block the operation immediately and return an error to the requester.

---

## Question 4

A large enterprise wants to ensure that every new Azure subscription provisioned for a business unit arrives pre-configured with a specific set of policies, role assignments, resource groups, and networking resources — and that these configurations are tracked for drift over time. Which Azure service best meets this requirement?

A. Azure Resource Manager templates
B. Azure Policy initiatives
C. Azure Blueprints
D. Azure Advisor

**Correct Answer: C**

### Distractor Analysis — Q4

**A — Incorrect.** ARM templates deploy resources but do not maintain a live tracking relationship between the template and the deployed resources. There is no built-in mechanism to detect if someone later removes a policy assignment or role assignment that was included in the template.

**B — Incorrect.** Azure Policy initiatives group multiple policy definitions for assignment, but they address only the policy enforcement dimension. They cannot deploy resource groups, apply role assignments, or deploy networking resources as part of the same operation.

**C — Correct.** Azure Blueprints is specifically designed for this scenario. It packages policy assignments, role assignments, resource groups, and ARM templates into a single unit. It maintains a live assignment relationship with the deployed subscription, enabling drift detection and remediation. Versioning supports controlled updates.

**D — Incorrect.** Azure Advisor provides recommendations for optimizing existing resources. It does not provision environments or enforce consistent subscription configurations.

---

## Question 5

Which statement correctly describes the difference between ISO 27001 and FedRAMP?

A. ISO 27001 is specific to US government cloud services; FedRAMP is an international standard.
B. ISO 27001 is an international information security management standard; FedRAMP is a US government framework for authorizing cloud services for federal agency use.
C. Both ISO 27001 and FedRAMP are administered by the American Institute of Certified Public Accountants.
D. FedRAMP replaces ISO 27001 for organizations that work with US federal data.

**Correct Answer: B**

### Distractor Analysis — Q5

**A — Incorrect.** This reverses the correct description. ISO 27001 is the international standard published by the International Organization for Standardization. FedRAMP is a US government program, not an international standard.

**B — Correct.** ISO 27001 is an internationally recognized standard for information security management systems (ISMS), applicable to any organization globally. FedRAMP is a US government-specific program that standardizes security assessment and authorization for cloud services used by federal agencies.

**C — Incorrect.** ISO 27001 is published by the International Organization for Standardization and administered through ISO-accredited certification bodies. FedRAMP is administered by the US General Services Administration and the Joint Authorization Board. Neither is administered by the AICPA, which governs SOC reports.

**D — Incorrect.** FedRAMP and ISO 27001 serve different purposes and different audiences. They are complementary rather than substitutes. An organization might hold both certifications — ISO 27001 for general enterprise compliance and FedRAMP authorization for US federal contracts.

---

## Question 6

An Azure Policy initiative is assigned to a management group with the FedRAMP High built-in initiative. A new virtual machine is deployed in a child subscription without a required diagnostic extension. The policy definition for this scenario uses the AuditIfNotExists effect. What is the outcome?

A. The VM deployment is blocked.
B. The diagnostic extension is automatically deployed on the VM.
C. The VM is deployed and marked as noncompliant in the policy compliance dashboard.
D. The VM is deployed and an automatic remediation task runs immediately.

**Correct Answer: C**

### Distractor Analysis — Q6

**A — Incorrect.** AuditIfNotExists does not block deployments. The Deny effect blocks deployments. AuditIfNotExists allows the resource to be created and then evaluates whether a dependent related resource exists.

**B — Incorrect.** Automatically deploying the missing diagnostic extension is the behavior of the DeployIfNotExists effect, not AuditIfNotExists. DeployIfNotExists creates a missing related resource; AuditIfNotExists only detects and reports its absence.

**C — Correct.** AuditIfNotExists allows the VM to be deployed, then checks whether the required related resource (the diagnostic extension) exists. If the extension is absent, the VM is marked noncompliant in the Policy compliance dashboard. No blocking or auto-remediation occurs.

**D — Incorrect.** Automatic remediation tasks are associated with DeployIfNotExists and Modify policy effects. AuditIfNotExists only reports noncompliance — it does not trigger remediation.

---

## Question 7

A European Union-based company stores customer personal data in an Azure SQL Database in the West Europe region. The company's legal team receives a request from a customer in Germany to have all their personal data permanently deleted from the company's systems. What is this type of request called under GDPR?

A. Data portability request
B. Right to erasure (right to be forgotten)
C. Subject access request
D. Lawful basis objection

**Correct Answer: B**

### Distractor Analysis — Q7

**A — Incorrect.** Data portability is a separate GDPR right (Article 20) that allows individuals to receive their personal data in a structured, machine-readable format and transmit it to another controller. It is about obtaining and moving data, not deleting it.

**B — Correct.** The right to erasure, also known as the right to be forgotten under GDPR Article 17, gives individuals the right to request that their personal data be deleted when it is no longer necessary for the original purpose, consent is withdrawn, or there is no overriding legitimate interest in retaining it.

**C — Incorrect.** A Subject Access Request (SAR) is a request under GDPR Article 15 for an individual to obtain a copy of all personal data a controller holds about them. It is about accessing data, not deleting it.

**D — Incorrect.** Objection to processing is a right under GDPR Article 21 that allows individuals to object to certain types of processing, particularly for direct marketing or processing based on legitimate interests. It is not a deletion request.

---

## Question 8

A company is planning to deploy a new workload that will process data for US federal government customers. The workload must comply with FedRAMP High requirements. The company wants to use Azure infrastructure that is pre-authorized at FedRAMP High. Which Azure cloud environment should they use?

A. Azure public cloud (commercial) in East US region
B. Azure Government cloud
C. Azure China operated by 21Vianet
D. Azure public cloud (commercial) with FedRAMP initiative assigned via Azure Policy

**Correct Answer: B**

### Distractor Analysis — Q8

**A — Incorrect.** While many Azure commercial services have FedRAMP Moderate authorization, the FedRAMP High P-ATO covers the Azure Government cloud environment. For strict FedRAMP High workloads requiring the full isolation and compliance posture, Azure Government is the correct choice.

**B — Correct.** Azure Government is specifically designed for US federal, state, and local government workloads. It holds FedRAMP High Provisional Authority to Operate (P-ATO) issued by the Joint Authorization Board, is physically separated from Azure commercial infrastructure, and is accessible only to vetted US government customers and partners.

**C — Incorrect.** Azure China is operated by 21Vianet as an independent cloud under Chinese data sovereignty requirements. It is designed for compliance with Chinese regulations, not US federal FedRAMP requirements.

**D — Incorrect.** Assigning a FedRAMP Azure Policy initiative to a commercial subscription enforces policy checks but does not confer FedRAMP authorization. Authorization requires a formal assessment and approval by the FedRAMP Joint Authorization Board or an individual agency, not a self-imposed policy assignment.

---

## Question 9

Microsoft Purview scans an organization's Azure Data Lake Storage account and identifies files that contain patterns matching Social Security Numbers and credit card numbers. What Purview capability performed this identification?

A. Data lineage tracking
B. Business glossary mapping
C. Automated data classification
D. Compliance Manager scoring

**Correct Answer: C**

### Distractor Analysis — Q9

**A — Incorrect.** Data lineage tracking maps how data flows from source systems through transformation pipelines to downstream consumers. It shows data movement and dependencies, not the content or sensitivity of individual files.

**B — Incorrect.** Business glossary mapping links technical data assets to business-meaningful terms and definitions. It supports data discoverability and stewardship but does not scan files for sensitive data patterns.

**C — Correct.** Automated data classification in Microsoft Purview uses built-in system classifiers that scan data assets and identify sensitive data patterns including Social Security Numbers, credit card numbers, passport numbers, and other regulated data types. This is a core capability of the Purview Data Map.

**D — Incorrect.** Compliance Manager produces a Compliance Score by assessing your Microsoft 365 and Azure environment configurations against regulatory frameworks. It evaluates configuration controls, not the content of individual data files.

---

## Question 10

An organization assigns an Azure Policy at the management group level that restricts deployments to the West Europe and North Europe regions. A developer in a child subscription tries to deploy a virtual machine to East US. The policy uses the Deny effect. Which of the following accurately describes what happens?

A. The VM is deployed to East US and flagged noncompliant for 24 hours, then automatically moved to West Europe.
B. The VM deployment to East US is blocked at the time of the deployment request.
C. The policy has no effect on child subscriptions — it only applies at the management group level.
D. The VM is deployed and a remediation task deletes it within one hour.

**Correct Answer: B**

### Distractor Analysis — Q10

**A — Incorrect.** Azure Policy Deny does not allow the deployment and then move it. The Deny effect intercepts the ARM API call at the moment of the request and prevents the resource from being created. There is no post-deployment relocation capability in Azure Policy.

**B — Correct.** When a policy with the Deny effect is assigned at the management group level, it applies to all child subscriptions, resource groups, and resources in that management group. When the developer attempts to deploy to East US, the ARM API call is evaluated against the policy, the condition is met (East US is not in the allowed list), and the deployment is blocked immediately with a policy violation error.

**C — Incorrect.** Management group is the broadest scope for policy assignments, and assignments inherit downward. A policy assigned at the management group level applies to all subscriptions, resource groups, and resources beneath it unless explicitly excluded.

**D — Incorrect.** Automatic deletion is not a behavior of any Azure Policy effect. The DeployIfNotExists and Modify effects can add or change resources, but no policy effect retroactively deletes a deployed resource. The Deny effect prevents creation before it happens.

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 15 Quiz*

---

### Question 11 (5 points)

A healthcare company is deploying a patient data management application to Azure. Their legal team requires proof that Microsoft has signed a Business Associate Agreement (BAA) covering Azure services before any Protected Health Information (PHI) can be processed in Azure. Where can the company access the Microsoft BAA for Azure?

- A) The company must negotiate and sign a custom BAA directly with their Microsoft account representative
- B) The Microsoft BAA for Azure is available online through the Microsoft Service Trust Portal and is accepted as part of the Microsoft Online Services Terms
- C) The BAA is only available to Enterprise Agreement customers with a minimum $1 million annual commitment
- D) Microsoft does not offer a BAA for Azure; HIPAA compliance requires on-premises infrastructure for PHI

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Microsoft offers a standard BAA for Azure (and other covered Microsoft services) that is incorporated into the Microsoft Online Services Terms (OST) / Microsoft Products and Services Agreement. Organizations can access and review the BAA through the Service Trust Portal. For enterprise customers, the BAA is accepted at scale — organizations do not need to individually negotiate custom agreements for standard Azure services.
  - *Why A is incorrect:* While enterprise organizations may have custom agreement terms, the standard Microsoft BAA for Azure is a standardized document available to all customers. Custom negotiation is not required to obtain HIPAA BAA coverage for Azure. The BAA terms are published and accepted through the online service terms.
  - *Why C is incorrect:* The Microsoft BAA is available to all Azure customers, not only large Enterprise Agreement customers. Healthcare organizations of any size can use Azure for HIPAA-covered workloads under the standard BAA terms.
  - *Why D is incorrect:* Microsoft Azure does support HIPAA-compliant workloads and provides a BAA. Many healthcare organizations run PHI workloads in Azure. The claim that HIPAA requires on-premises infrastructure is false — cloud environments are permissible under HIPAA when appropriate administrative, physical, and technical safeguards are in place and a BAA is executed.

---

### Question 12 (5 points)

A company's security team downloads a SOC 2 Type II report for Azure from the Service Trust Portal. The report covers the period from January 1 to December 31 of the previous year. What does the "Type II" designation specifically indicate about this report?

- A) The report was issued by a Type II auditing firm with government certification
- B) The report covers two data centers rather than a single facility
- C) The report describes the design AND effectiveness of controls over an extended audit period, not just a point-in-time design assessment
- D) The report covers two trust service criteria categories (Availability and Security)

- **Correct Answer:** C

- **Distractor Analysis:**
  - *Why C is correct:* SOC 2 Type I reports assess whether controls are suitably designed at a specific point in time. SOC 2 Type II reports assess both the design and operating effectiveness of controls over a sustained period (typically 6–12 months). A Type II report demonstrates that controls actually functioned as intended throughout the audit period, not merely that they were designed correctly on the audit date. For compliance purposes, Type II reports are more valuable because they prove sustained effectiveness.
  - *Why A is incorrect:* The Type I / Type II designation refers to the scope and duration of the audit, not the certification level of the auditing firm. SOC 2 audits are performed by CPA firms licensed to conduct attest engagements — there is no "Type II auditing firm" classification.
  - *Why B is incorrect:* SOC 2 reports cover a service organization's controls across its entire service scope, which may include multiple data centers. The Type I / Type II designation has nothing to do with the number of facilities covered.
  - *Why D is incorrect:* SOC 2 reports can cover one or more of the five Trust Service Criteria (Security, Availability, Processing Integrity, Confidentiality, Confidential Information). The Type I / Type II designation refers to point-in-time vs. period-of-time assessment, not to how many criteria are covered.

---

### Question 13 (5 points)

An organization is subject to GDPR and stores Azure Blob Storage data containing EU customer personal data in the West Europe region. A GDPR compliance officer asks whether the data can be replicated to East US for disaster recovery purposes. What GDPR consideration governs this scenario?

- A) GDPR prohibits all replication of personal data outside the European Union regardless of security measures
- B) GDPR restricts transfers of personal data outside the EU/EEA to countries without adequate data protection unless appropriate safeguards are in place, such as Standard Contractual Clauses
- C) GDPR has no jurisdiction over data stored in Azure because Azure is a US company
- D) GDPR allows free transfer of personal data to any Azure region because Microsoft holds ISO 27001 certification

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* GDPR Chapter V restricts transfers of personal data to third countries (outside the EU/EEA) unless the destination country has an adequacy decision from the European Commission, or appropriate safeguards are in place (such as Standard Contractual Clauses, Binding Corporate Rules, or approved codes of conduct). The US does not have a blanket adequacy decision, but Microsoft provides Standard Contractual Clauses and Data Processing Addendums that enable lawful transfers from EU to US Azure regions for GDPR compliance.
  - *Why A is incorrect:* GDPR does not absolutely prohibit all cross-border transfers of personal data. It requires appropriate safeguards when transferring to countries without adequate protection, but transfers are possible with proper legal mechanisms in place.
  - *Why C is incorrect:* GDPR's territorial scope (Article 3) applies to any organization processing personal data of EU data subjects, regardless of where the organization is based. Azure being a US company does not exempt it or its customers from GDPR requirements.
  - *Why D is incorrect:* ISO 27001 is an information security management standard, not a GDPR adequacy mechanism. Holding ISO 27001 certification does not authorize free data transfer to any country. GDPR transfer restrictions are legal requirements separate from security certifications.

---

### Question 14 (5 points)

A financial services company needs to demonstrate compliance with PCI DSS for their Azure-hosted cardholder data environment. They want to understand which PCI DSS controls Microsoft is responsible for (platform-level) versus which controls the company itself must implement (customer-level). Which resource provides this shared responsibility breakdown specifically for PCI DSS?

- A) Azure Security Center (Defender for Cloud) Secure Score
- B) The PCI DSS Shared Responsibility Matrix available on the Microsoft Service Trust Portal
- C) Azure Policy regulatory compliance dashboard with PCI DSS initiative assigned
- D) The Azure Trust Center's general shared responsibility model overview

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The Microsoft Service Trust Portal hosts detailed compliance documentation including Shared Responsibility Matrices for specific regulatory frameworks like PCI DSS. These documents explicitly map each PCI DSS requirement to either Microsoft responsibility (infrastructure), customer responsibility (application and data), or shared responsibility. This is the authoritative source for understanding the compliance division for PCI DSS on Azure.
  - *Why A is incorrect:* Defender for Cloud Secure Score measures the security posture of the customer's Azure resource configurations. It does not provide a PCI DSS-specific shared responsibility matrix explaining which controls Microsoft versus the customer owns.
  - *Why C is incorrect:* The Azure Policy PCI DSS regulatory compliance dashboard shows whether customer-managed Azure resources comply with PCI DSS policy controls. It assesses the customer's configuration compliance, but does not document the full framework of which requirements are Microsoft-managed versus customer-managed at the contractual level.
  - *Why D is incorrect:* The Azure Trust Center provides a general overview of the shared responsibility model (IaaS/PaaS/SaaS layers) but does not provide PCI DSS-specific control mapping. The Service Trust Portal has the framework-specific documentation needed for PCI DSS compliance planning.

---

### Question 15 (5 points)

An organization wants to verify that their Azure environment meets the requirements of the NIST SP 800-53 framework. They have enabled the NIST SP 800-53 regulatory compliance initiative in Microsoft Defender for Cloud. The dashboard shows 67% compliance. Which action would most directly improve this score?

- A) Purchase Microsoft Entra ID P2 licenses to enable advanced identity protection features
- B) Review the non-compliant controls, identify customer-managed controls with failing resources, and remediate the specific Azure resource configurations those controls require
- C) Contact Microsoft support to request that Microsoft implement the remaining 33% of controls
- D) Enable Azure Blueprints and deploy the NIST SP 800-53 blueprint assignment to the subscription

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* The regulatory compliance dashboard in Defender for Cloud distinguishes between Microsoft-managed controls (platform-level, already implemented) and customer-managed controls (configuration-level, requiring action). The 33% non-compliant controls are specific Azure resource configuration requirements the organization has not implemented. Reviewing each failing control, identifying which Azure resources are non-compliant, and remediating those configurations (enabling encryption, applying network restrictions, enabling logging, etc.) directly improves the compliance score.
  - *Why A is incorrect:* Purchasing Entra ID P2 licenses may satisfy some identity-related NIST controls (like multi-factor authentication or privileged identity management), but it alone does not address all non-compliant controls. The correct approach is to identify which specific controls are failing and remediate them systematically.
  - *Why C is incorrect:* Microsoft is responsible for platform-level controls, which are already implemented (these appear as compliant in the Microsoft-managed section of the dashboard). The remaining non-compliant controls in the customer section require the organization to configure their own Azure resources — Microsoft cannot implement customer-managed controls.
  - *Why D is incorrect:* Azure Blueprints is deprecated. Even when available, it deployed resource configurations but would not automatically bring an existing environment into NIST compliance. The organization already has deployed resources; they need to remediate existing resource configurations, not deploy new ones via Blueprints.

---

### Question 16 (5 points)

A company stores all Azure resource audit logs (Activity Log) in a Log Analytics workspace for compliance purposes. Their legal team says they need to retain these logs for 7 years to meet financial industry regulatory requirements. The default Log Analytics workspace retention is 30 days (free tier) or up to 730 days (paid tier). What is the correct approach to meet the 7-year retention requirement?

- A) Switch the Log Analytics workspace to the Premium SKU which supports 7-year retention
- B) Configure the Log Analytics workspace to archive data to Azure Blob Storage (Cool or Archive tier) after the active retention period, where data can be retained for years at low cost
- C) Enable Azure Site Recovery on the Log Analytics workspace to replicate logs to a secondary region for long-term retention
- D) Export logs to an on-premises server each month using Azure Data Factory, as Azure does not support log retention beyond 2 years

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Log Analytics workspaces support a two-tier retention model: active retention (up to 730 days for paid tiers, queryable via KQL) and archive retention (up to 12 years total, using the workspace's archive tier backed by Azure Blob Storage at reduced cost). After the active retention period expires, data moves to the archive tier where it can be restored for investigation when needed. This approach meets the 7-year retention requirement without exporting logs off Azure.
  - *Why A is incorrect:* There is no "Premium SKU" for Log Analytics workspaces that extends retention to 7 years as a single active tier. Log Analytics has the archive feature to address long-term retention needs at reduced cost, regardless of workspace tier.
  - *Why C is incorrect:* Azure Site Recovery replicates VMs and workloads for disaster recovery purposes. It has no function related to Log Analytics data retention and cannot extend the retention of log data.
  - *Why D is incorrect:* Azure does support log retention beyond 2 years through the Log Analytics archive tier (up to 12 years total). Exporting logs to on-premises monthly is a valid approach but is unnecessary given Azure's native long-term retention capabilities, and the statement that Azure does not support retention beyond 2 years is factually incorrect.

---

### Question 17 (5 points)

An organization subject to GDPR receives a data subject access request (DSAR) — an EU customer is requesting a copy of all personal data the company holds about them. The company stores customer data across Azure SQL Database, Azure Blob Storage, and Azure Cosmos DB. Which Microsoft Purview capability most directly helps the organization locate all instances of this customer's personal data across these data stores?

- A) Microsoft Purview Compliance Manager
- B) Microsoft Purview Data Map with automated scanning and classification
- C) Azure Active Directory (Entra ID) user activity logs
- D) Azure Policy with a GDPR regulatory compliance initiative

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Microsoft Purview's Data Map can register Azure SQL Database, Blob Storage, and Cosmos DB as data sources and scan them to discover and classify data assets. After scanning, the data catalog shows where personal data (including customer-identifying information) is stored across all registered sources. This discovery capability directly supports DSAR fulfillment by identifying which data stores contain the subject's personal data, enabling the compliance team to extract and compile the required information.
  - *Why A is incorrect:* Purview Compliance Manager is a Microsoft 365-focused tool that scores compliance posture against regulatory frameworks. It does not scan Azure data stores to locate specific customer personal data.
  - *Why C is incorrect:* Entra ID user activity logs capture authentication and sign-in events — they show when users logged in, not what personal data the organization holds about a customer. Activity logs cannot fulfill a data subject access request for stored personal data.
  - *Why D is incorrect:* Azure Policy with a GDPR initiative assesses Azure resource configuration compliance (encryption enabled, access controls configured, etc.). It evaluates how data is protected but does not scan data content to locate a specific customer's personal data across multiple data stores.

---

### Question 18 (5 points)

A US government agency requires cloud services to meet FedRAMP High authorization. They are evaluating two options: (a) Azure Commercial (public cloud) with the FedRAMP High Azure Policy initiative assigned, and (b) Azure Government (sovereign cloud). Which option meets the FedRAMP High requirement and why?

- A) Option (a) meets FedRAMP High because assigning the policy initiative certifies the environment
- B) Option (b) — Azure Government — meets FedRAMP High because it holds a formal Joint Authorization Board Provisional Authority to Operate (JAB P-ATO) at the FedRAMP High impact level
- C) Both options equally meet FedRAMP High when the policy initiative is assigned
- D) Neither option meets FedRAMP High; agencies must use on-premises air-gapped infrastructure for High impact workloads

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* FedRAMP High authorization is a formal accreditation issued by the FedRAMP Joint Authorization Board (JAB) after an independent security assessment by a Third Party Assessment Organization (3PAO). Azure Government holds this JAB Provisional Authority to Operate (P-ATO) at the High impact level, making it the authorized environment for sensitive federal workloads. The physical separation of Azure Government from commercial infrastructure and its US-persons-only operations model contribute to this authorization.
  - *Why A is incorrect:* Assigning an Azure Policy initiative is a governance tool that checks whether resource configurations meet policy requirements. It does not grant FedRAMP authorization. FedRAMP authorization requires a formal security assessment and approval by the JAB or an individual agency, not a self-certification via policy assignment.
  - *Why C is incorrect:* Azure Commercial and Azure Government are not equivalent for FedRAMP High. While some Azure Commercial services have FedRAMP Moderate authorization, the full FedRAMP High JAB P-ATO for the complete cloud environment is specific to Azure Government. Policy initiatives do not make Azure Commercial equivalent to Azure Government for FedRAMP High purposes.
  - *Why D is incorrect:* FedRAMP is the US federal government's program specifically designed to authorize cloud services for government use. Air-gapped on-premises infrastructure is not required. FedRAMP High is the authorization level for cloud-hosted government systems with the most sensitive (but not classified) data.

---

### Question 19 (5 points)

A company's compliance officer says: "We need to ensure our Azure environment is compliant with ISO 27001." Which combination of Azure tools and Microsoft resources best supports demonstrating and maintaining ISO 27001 compliance?

- A) Azure Security Center vulnerability scans + Azure Backup + Azure Monitor alerts
- B) Microsoft Defender for Cloud Regulatory Compliance dashboard (with ISO 27001 initiative) + ISO 27001 audit reports from the Service Trust Portal
- C) Azure Policy Audit initiative + Azure Blueprints ISO 27001 template deployment
- D) Azure Advisor Security pillar recommendations + Microsoft Trust Center security overview

- **Correct Answer:** B

- **Distractor Analysis:**
  - *Why B is correct:* Demonstrating ISO 27001 compliance on Azure involves two components: (1) assessing the organization's Azure resource configurations against ISO 27001 controls using the Defender for Cloud Regulatory Compliance dashboard with the ISO 27001 initiative assigned — this shows which controls are compliant and which need remediation; and (2) obtaining Microsoft's ISO 27001 certificate and audit reports from the Service Trust Portal to show auditors that the underlying Azure platform has been certified. Together, these cover both the platform certification and the organization's configuration compliance.
  - *Why A is incorrect:* While security scanning, backups, and alerting are good security practices, they do not provide ISO 27001 framework mapping, compliance scoring, or downloadable audit reports. These tools address specific security capabilities but not the structured compliance assessment framework that ISO 27001 requires.
  - *Why C is incorrect:* Azure Blueprints is deprecated. An Azure Policy Audit initiative can check some ISO 27001-related configurations, but without the Regulatory Compliance dashboard's framework mapping it lacks the control-level compliance view. Additionally, this combination does not provide access to Microsoft's platform-level ISO 27001 certificate documentation.
  - *Why D is incorrect:* Azure Advisor Security recommendations suggest specific security improvements but are not mapped to ISO 27001 control numbers. The Microsoft Trust Center provides general security information and links to compliance documentation, but does not provide the operational compliance assessment of the organization's specific Azure resource configurations.

---

### Question 20 (5 points)

A company with operations in the EU, US, and Singapore is architecting a new Azure deployment. Their legal team has three requirements: (1) EU customer data must remain in EU Azure regions, (2) Singapore customer data must remain in Singapore, and (3) US data can be replicated anywhere. Which Azure capability primarily supports requirements 1 and 2?

- A) Azure Policy "Allowed locations" definition with region restrictions per deployment scope
- B) Azure Traffic Manager with geographic routing profiles
- C) Azure Content Delivery Network with regional endpoint restrictions
- D) Azure ExpressRoute with private peering to prevent data from traversing the public internet

- **Correct Answer:** A

- **Distractor Analysis:**
  - *Why A is correct:* Data residency requirements — ensuring data is stored only in specific geographic regions — are enforced at the resource deployment level using Azure Policy's "Allowed locations" definition. By assigning region-restricted policies to the EU and Singapore deployments (for example, restricting EU subscriptions to West Europe and North Europe, and Singapore subscriptions to Southeast Asia), the company prevents resources from being accidentally deployed in non-compliant regions. This is the standard Azure mechanism for enforcing data residency at the governance layer.
  - *Why B is incorrect:* Azure Traffic Manager routes network traffic (DNS-based) to endpoints in different regions based on routing policies. It controls where user requests are directed, not where Azure resources (and their stored data) are deployed. Traffic Manager does not prevent data from being stored in a non-compliant region.
  - *Why C is incorrect:* Azure CDN replicates content to edge nodes globally for performance. By default it distributes data widely, which would violate data residency requirements rather than enforce them. CDN has geographic restriction features that block content delivery to certain regions, but these are access restrictions, not data storage residency controls.
  - *Why D is incorrect:* Azure ExpressRoute provides private network connectivity between on-premises infrastructure and Azure, bypassing the public internet. It does not control which Azure regions data is stored in. ExpressRoute addresses network privacy and latency, not data residency or geographic storage restrictions.

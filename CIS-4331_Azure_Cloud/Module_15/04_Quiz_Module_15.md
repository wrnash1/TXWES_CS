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

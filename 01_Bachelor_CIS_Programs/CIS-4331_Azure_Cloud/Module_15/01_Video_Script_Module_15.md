# Video Script: Module 15 — Azure Compliance, Privacy, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Production Notes

**Estimated Runtime:** 28–32 minutes
**Slide Deck:** Module_15_Slides.pptx
**Visual Aids:** Microsoft Trust Center screenshot, Azure Policy definition editor, Blueprints workflow diagram, Purview data map, compliance dashboard

---

## SEGMENT 1 — Introduction: Why Compliance and Governance Matter (3 minutes)

[SLIDE: Module 15 Title Card]

Welcome back to CIS-4331. I'm Professor Nash, and this is Module 15: Azure Compliance, Privacy, and Governance.

In the previous module we focused on cost — understanding where your money goes and how to control it. This module focuses on something equally important and in many industries even more consequential: whether your use of Azure meets legal, regulatory, and organizational requirements.

[SLIDE: The Compliance Stakes]

Consider three scenarios. A healthcare company stores patient records in Azure. A government contractor processes federal data. A financial services firm handles consumer credit information. In each case, how Azure manages and protects that data is not just a technical question — it is a legal and contractual obligation. Violations carry fines in the millions, loss of contracts, and reputational damage that takes years to recover from.

[SLIDE: Governance in the Enterprise]

Beyond legal compliance there is the internal governance question: how does a company ensure that its own teams follow standards for how Azure resources are deployed? Left unchecked, different teams will deploy resources in inconsistent configurations, skip required security settings, and create technical debt that is expensive to untangle later. Azure's governance tools provide the guardrails.

[SLIDE: Module Learning Objectives]

By the end of this module you will be able to describe the Microsoft Trust Center and its role in communicating Microsoft's compliance posture, identify key compliance certifications including ISO 27001, SOC 1 and 2, FedRAMP, and HIPAA, explain how Azure Policy enforces rules on resource deployments, describe the purpose and workflow of Azure Blueprints, explain what Microsoft Purview does for data governance, and define data residency and its importance for GDPR compliance.

---

## SEGMENT 2 — Microsoft Trust Center (4 minutes)

[SLIDE: What is the Microsoft Trust Center?]

The Microsoft Trust Center is a public website at microsoft.com/en-us/trust-center that provides transparency into how Microsoft handles security, privacy, and compliance across its cloud services including Azure, Microsoft 365, and Dynamics 365.

Think of the Trust Center as Microsoft's public commitment to responsible cloud operation. It is the starting point for compliance research — where a compliance officer or auditor goes to understand what certifications Azure holds, how Microsoft responds to government data requests, and what contractual commitments are available.

[SLIDE: What the Trust Center Contains]

The Trust Center is organized into several areas. The Security section describes how Microsoft secures the physical data centers, the network infrastructure, and the software supply chain. The Privacy section explains Microsoft's data processing practices — what data Microsoft collects, how it is used, and what controls customers have. The Compliance section lists all the compliance frameworks and certifications that Azure has achieved.

[SLIDE: Compliance Offerings Database]

One of the most useful resources on the Trust Center is the Compliance Offerings database. It is searchable by industry, region, and regulation. If you need to know whether Azure is compliant with Australia's Privacy Act, the EU General Data Protection Regulation, or the US Department of Defense IL4 requirements, you look it up in this database.

[SLIDE: Service Trust Portal]

Closely related to the Trust Center is the Service Trust Portal at servicetrust.microsoft.com. The Service Trust Portal is where you download audit reports, penetration test results, compliance guides, and whitepapers that you can share with your own auditors. While the Trust Center is public-facing and informational, the Service Trust Portal requires a Microsoft account and contains more detailed technical documentation.

---

## SEGMENT 3 — Key Compliance Certifications (6 minutes)

[SLIDE: Why Certifications Matter]

Azure achieves compliance certifications by submitting to independent third-party audits of its controls, processes, and infrastructure. When Azure holds a certification, it means an independent auditor has verified that Azure's operations meet the requirements of that framework.

When you build on Azure, you can inherit these certifications for your own compliance programs — a concept called shared compliance responsibility. Azure does the work to maintain the certification; you focus on building your application correctly within the certified environment.

[SLIDE: ISO 27001]

ISO 27001 is the international standard for information security management systems, published by the International Organization for Standardization. It specifies requirements for establishing, implementing, maintaining, and continually improving an information security management system.

Azure holds ISO 27001 certification across its global infrastructure. This certification is broadly recognized and is often required by enterprise customers as a baseline before they will consider a cloud provider. Many organizations in Europe, Asia-Pacific, and Latin America treat ISO 27001 certification as a prerequisite for cloud adoption.

[SLIDE: SOC 1 and SOC 2]

SOC stands for System and Organization Controls, a framework developed by the American Institute of Certified Public Accountants. SOC 1 focuses on controls relevant to financial reporting. SOC 2 focuses on controls related to security, availability, processing integrity, confidentiality, and privacy — the five Trust Services Criteria.

Azure undergoes annual SOC 1 and SOC 2 audits conducted by independent CPA firms. The SOC 2 Type II report — which covers the operating effectiveness of controls over a period of time, not just at a point in time — is particularly important for enterprise customers who need evidence that Azure's security controls work consistently throughout the year.

[SLIDE: FedRAMP]

FedRAMP stands for the Federal Risk and Authorization Management Program. It is the US government's standardized approach to security assessment, authorization, and continuous monitoring for cloud services used by federal agencies.

Azure has FedRAMP High authorization, which is the highest level and covers the most sensitive federal data categories. This authorization means that US federal agencies can use Azure for workloads up to and including data classified at the High impact level without needing to conduct their own full security assessment of Azure's infrastructure.

[SLIDE: HIPAA]

HIPAA is the Health Insurance Portability and Accountability Act, the US law governing the privacy and security of protected health information. While HIPAA does not offer a formal certification — it is a law, not an audit framework — Microsoft provides a HIPAA Business Associate Agreement to Azure customers.

The Business Associate Agreement, or BAA, is a contractual commitment in which Microsoft agrees to handle protected health information in accordance with HIPAA requirements. Any healthcare organization using Azure to process, store, or transmit patient data must have a signed BAA with Microsoft. Without it, using Azure for PHI would be a HIPAA violation regardless of how securely the data is stored.

[SLIDE: Other Notable Certifications]

Beyond these four, Azure holds dozens of additional certifications: PCI DSS for payment card data, GDPR compliance under European data protection law, HITRUST CSF for healthcare, CSA STAR for cloud security, and country-specific certifications like Germany's C5 and Australia's IRAP. The full list is available on the Trust Center compliance offerings page.

---

## SEGMENT 4 — Azure Policy (5 minutes)

[SLIDE: What is Azure Policy?]

Azure Policy is a governance service that lets you create, assign, and manage rules — called policies — that enforce specific configurations on your Azure resources. When a resource is deployed or modified, Azure Policy evaluates it against the assigned policies and either prevents the noncompliant action or flags the resource for remediation.

[SLIDE: Policy Definitions]

A policy definition describes the condition to check and the effect to apply when the condition is true. For example: if a virtual machine is deployed in a region other than East US or West US, deny the deployment. Or: if a storage account does not have encryption enabled, audit it and flag it as noncompliant.

Azure provides hundreds of built-in policy definitions covering security best practices, naming conventions, resource types, regions, and more. You can also write custom policy definitions using JSON if the built-in policies do not meet your requirements.

[SLIDE: Policy Effects]

Every policy definition includes an effect that determines what happens when a resource violates the policy. The most important effects are:

Deny — blocks the deployment or modification. The resource is not created if it violates the policy.

Audit — allows the deployment but flags the resource as noncompliant in the compliance dashboard.

AuditIfNotExists — checks for the existence of a related resource. For example, audit a VM that does not have the diagnostic extension installed.

DeployIfNotExists — automatically deploys a required resource if it is missing. For example, automatically enable Azure Monitor on a newly deployed VM.

Modify — automatically changes resource properties to bring them into compliance.

[SLIDE: Policy Assignments and Scope]

A policy definition becomes active by being assigned to a scope — a management group, subscription, or resource group. Resources within that scope are evaluated against the policy. You can exclude specific child scopes from an assignment when needed, for example excluding a sandbox resource group from a strict production policy.

[SLIDE: Initiative Definitions]

An initiative definition is a collection of related policy definitions grouped together to achieve a broader goal. Rather than assigning dozens of individual policies one by one, you assign the initiative and all its member policies apply at once.

Azure provides built-in initiatives for major compliance frameworks — the Azure Security Benchmark initiative, the HIPAA/HITRUST initiative, the FedRAMP High initiative. Each initiative contains the policies necessary to assess compliance with that framework. You assign the initiative to your subscription and immediately see a compliance percentage across all covered controls.

[SLIDE: Compliance Dashboard]

The Policy compliance dashboard in the Azure portal shows the overall compliance state of your subscriptions and resource groups. You can see what percentage of resources are compliant, which policies have the most violations, and drill into specific non-compliant resources to understand what needs to change.

---

## SEGMENT 5 — Azure Blueprints (4 minutes)

[SLIDE: What is Azure Blueprints?]

Azure Blueprints is a service that lets you define a repeatable set of Azure resources, policies, and role assignments that can be deployed together as a single unit. Think of a blueprint as a deployment template for an entire governed environment.

[SLIDE: Blueprint Artifacts]

A blueprint is composed of artifacts. Each artifact is one of four types:

Role assignments — which Azure AD identities get which roles on the deployed resources.

Policy assignments — which Azure Policy definitions or initiatives apply to the deployed resources.

Resource groups — the resource group structure within the subscription.

ARM templates — the actual resources to deploy (VMs, networks, storage accounts, etc.).

[SLIDE: Blueprint Lifecycle]

The blueprint lifecycle has three stages. First, you define the blueprint — specify the artifacts and their configuration parameters. Second, you publish the blueprint — assign it a version number. Versioning is important because it allows you to track changes and roll back to a previous version. Third, you assign the blueprint to a subscription — this triggers the deployment of all artifacts in sequence.

[SLIDE: Blueprint vs ARM Template]

Students often ask: how is a Blueprint different from an ARM template? The key difference is tracking and governance. ARM templates are deployment documents — they create resources and their job is done. Blueprints maintain a live relationship between the blueprint definition and the deployed resources. If a policy assignment or role assignment in the blueprint is changed or removed, Azure tracks the drift and can alert or remediate.

[SLIDE: Blueprint Use Cases]

Blueprints are most valuable in large organizations that need to provision new Azure environments consistently — for example, spinning up a new subscription for a new business unit and ensuring it arrives pre-configured with all required policies, the correct network topology, the correct role assignments for the security team, and the required audit logging. Without Blueprints this process might take weeks and vary between teams. With Blueprints it takes minutes and is identical every time.

---

## SEGMENT 6 — Microsoft Purview (4 minutes)

[SLIDE: What is Microsoft Purview?]

Microsoft Purview is a unified data governance and compliance service. Where Azure Policy governs how infrastructure is deployed, Purview governs how data is discovered, classified, and managed across your organization.

[SLIDE: Purview Data Map]

The core of Purview is the Data Map, which automatically scans your data sources — Azure Storage, Azure SQL Database, Azure Data Lake, Power BI, and even on-premises SQL Server — and builds a catalog of all the data assets it finds. Each asset is classified automatically using built-in classifiers that detect patterns like social security numbers, credit card numbers, email addresses, and health record identifiers.

[SLIDE: Data Catalog and Glossary]

Once the Data Map is built, the Data Catalog makes it searchable. Data stewards and analysts can search for data assets by name, type, classification, or business glossary term. The business glossary links technical data assets to business-meaningful terms — "Customer PII" as a glossary term points to the actual database tables and columns that contain personally identifiable information.

[SLIDE: Data Lineage]

Purview also tracks data lineage — the path data travels from its source through transformation pipelines to its final destination. If a compliance auditor asks where your customer email addresses came from and which downstream reports use them, Purview can show the complete lineage diagram.

[SLIDE: Purview Compliance Manager]

Within the compliance capabilities, Purview includes Compliance Manager — a tool that assesses your Microsoft 365 and Azure environment against regulatory frameworks and generates a compliance score. It provides a prioritized list of improvement actions that, when completed, increase your score. This is particularly useful for organizations working toward certifications like ISO 27001 or FedRAMP who need a roadmap of gaps to close.

---

## SEGMENT 7 — Data Residency, Sovereignty, and GDPR (4 minutes)

[SLIDE: Data Residency]

Data residency refers to the physical location where your data is stored and processed. For many organizations — particularly in healthcare, financial services, government, and any industry operating in the European Union — data residency is a legal requirement. Data may not leave a specific country or region.

[SLIDE: Azure Regions and Data Residency]

Azure's global region architecture is designed to support data residency requirements. When you deploy a resource in the Australia East region, your data stays in New South Wales. When you deploy in Germany West Central, your data stays in Germany. Azure also offers sovereign cloud environments — Azure Government for US federal and state agencies, Azure China operated by 21Vianet, and Azure Germany operated under special data trustee arrangements.

[SLIDE: Data Sovereignty]

Data sovereignty goes beyond residency. It means that the laws of the jurisdiction where data is stored apply to that data. Data stored in Azure Germany under the German data trustee model is subject to German law, and Microsoft cannot hand it to a third party without the trustee's approval — even in response to a US government request.

[SLIDE: GDPR and Azure]

The General Data Protection Regulation, or GDPR, is the European Union's comprehensive data privacy law. It applies to any organization that processes personal data of EU residents, regardless of where the organization is located. GDPR requirements include obtaining lawful basis for processing personal data, enabling individuals to exercise their rights (access, erasure, portability), notifying authorities within 72 hours of a data breach, and conducting data protection impact assessments for high-risk processing.

Azure supports GDPR compliance in several ways. The GDPR-compliant terms are embedded in Microsoft's Data Processing Addendum, which all Azure customers accept. Azure provides tools for data subject request fulfillment, privacy controls for limiting data collection, and data residency configurations that keep EU personal data in EU regions.

---

## SEGMENT 8 — Exam Tips and Module Summary (2 minutes)

[SLIDE: AZ-900 Exam Focus — Compliance and Governance]

Here are the key exam-ready distinctions for Module 15.

Microsoft Trust Center is the public-facing transparency portal for Microsoft's security, privacy, and compliance posture. The Service Trust Portal is where you download audit reports.

Azure Policy enforces rules on resource deployments — it can deny, audit, or auto-remediate noncompliant resources. Initiatives group multiple policies together.

Azure Blueprints packages policies, role assignments, resource groups, and ARM templates for consistent environment deployment. It maintains a live tracking relationship with deployed resources.

Microsoft Purview provides data governance — discovery, classification, cataloging, and lineage. Compliance Manager within Purview provides a compliance score and improvement roadmap.

GDPR applies to EU personal data regardless of where the processing organization is located. Azure provides GDPR-supportive contractual terms, data residency controls, and tooling.

[SLIDE: Module Summary]

In this module we covered the Microsoft Trust Center and Service Trust Portal, key compliance certifications including ISO 27001, SOC 1 and 2, FedRAMP, and HIPAA, Azure Policy for infrastructure governance, Azure Blueprints for consistent environment deployment, Microsoft Purview for data governance, and data residency and GDPR considerations.

Our next and final module is Module 16 — AZ-900 Exam Preparation and Capstone. We will review all three exam domains, work through exam strategy, and complete a set of practice questions that mirror the real exam format.

I will see you there.

---

## End of Script — Module 15

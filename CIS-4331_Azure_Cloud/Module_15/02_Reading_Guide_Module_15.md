# Reading Guide: Module 15 — Azure Compliance, Privacy, and Governance

## Course: CIS-4331 Azure Cloud Computing

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** Microsoft Azure Fundamentals (AZ-900)

---

## Overview

As organizations move workloads to Azure they take on a shared responsibility for compliance with legal, regulatory, and contractual requirements. Microsoft fulfills its portion through physical security, certified operational processes, contractual commitments, and governance tooling. Customers fulfill their portion by using Azure's governance services to enforce standards on their own deployments and by properly configuring Azure to meet regulatory obligations. This module covers both sides of that shared responsibility.

---

## Section 1 — Microsoft Trust Center and Service Trust Portal

### 1.1 Microsoft Trust Center

The Microsoft Trust Center at microsoft.com/en-us/trust-center is the primary public resource for understanding Microsoft's approach to security, privacy, and compliance across its cloud services. It serves as a reference for compliance officers, auditors, legal teams, and enterprise customers evaluating Azure.

The Trust Center is organized around four main themes.

**Security** covers physical data center security, network security, software development lifecycle, and vulnerability management.

**Privacy** covers data collection practices, customer data ownership, government request handling, and privacy controls.

**Compliance** covers the full list of certifications, audit reports, and regulatory compliance documentation.

**Transparency** covers Microsoft's policies on how it accesses customer data, law enforcement requests, and subprocessor lists.

### 1.2 Service Trust Portal

The Service Trust Portal at servicetrust.microsoft.com provides deeper technical compliance documentation for customers and auditors who need verifiable evidence of Microsoft's controls. Resources available include third-party audit reports (SOC 1, SOC 2, ISO 27001, FedRAMP packages), penetration testing reports, compliance implementation guides, and regional compliance documentation.

Access requires a Microsoft organizational account. Documents are updated following annual audits.

### 1.3 Compliance Manager

Compliance Manager is integrated into the Microsoft Purview compliance portal. It provides an automated assessment of your Microsoft 365 and Azure environment against a chosen regulatory framework and generates a Compliance Score (0–100%). Each assessment includes a list of improvement actions ranked by impact, allowing organizations to prioritize their compliance work systematically.

---

## Section 2 — Key Compliance Certifications

### 2.1 ISO 27001

ISO 27001 is the globally recognized standard for Information Security Management Systems (ISMS), published by the International Organization for Standardization. It specifies requirements for establishing, implementing, maintaining, and continually improving an ISMS.

Azure holds ISO 27001 certification across its global infrastructure, renewed annually through third-party audits. This certification is required by many enterprise procurement processes — particularly in Europe, Asia-Pacific, and Latin America — as a baseline for cloud vendor selection.

Key focus areas include risk management, asset management, access control, cryptography, physical security, incident management, and business continuity.

### 2.2 SOC 1 and SOC 2

System and Organization Controls (SOC) reports are produced under standards from the American Institute of Certified Public Accountants (AICPA).

SOC 1 addresses internal controls relevant to financial reporting. It is important for organizations whose Azure usage directly impacts financial statement processing.

SOC 2 addresses controls across five Trust Services Criteria: Security, Availability, Processing Integrity, Confidentiality, and Privacy.

Both report types come in two forms. Type I is a point-in-time assessment of whether controls are suitably designed. Type II assesses whether controls operated effectively over a period, typically 6–12 months.

Azure undergoes annual SOC 1 Type II and SOC 2 Type II audits. The Type II designation is more valuable because it demonstrates that controls work consistently over time, not just at one moment.

### 2.3 FedRAMP

The Federal Risk and Authorization Management Program (FedRAMP) is the US government's standardized approach to security assessment, authorization, and continuous monitoring for cloud services used by federal agencies.

FedRAMP has three impact levels.

| Level | Description | Data Sensitivity |
|---|---|---|
| Low | Limited adverse effect if compromised | Public data |
| Moderate | Serious adverse effect | Most federal data |
| High | Severe or catastrophic effect | Most sensitive federal data |

Azure holds FedRAMP High Provisional Authority to Operate (P-ATO), the highest level, covering the full Azure Government cloud environment and many Azure commercial services. This authorization is issued by the FedRAMP Joint Authorization Board and accepted by federal agencies.

### 2.4 HIPAA and the Business Associate Agreement

HIPAA (Health Insurance Portability and Accountability Act) governs the privacy and security of Protected Health Information (PHI) in the United States. HIPAA applies to covered entities (healthcare providers, payers, clearinghouses) and their business associates (service providers who handle PHI on their behalf).

Because HIPAA is a law rather than an auditable standard, there is no formal HIPAA certification. Instead, cloud providers demonstrate HIPAA readiness through a signed Business Associate Agreement (BAA) — a contractual commitment to handle PHI per HIPAA requirements — and technical safeguards aligned with the HIPAA Security Rule.

Microsoft provides a HIPAA BAA to all Azure customers through the Microsoft Online Services Terms. Any Azure customer processing PHI must ensure the BAA is executed. The BAA does not transfer all HIPAA responsibility to Microsoft — the customer remains responsible for correct application configuration.

### 2.5 Additional Notable Certifications

| Certification | Scope | Relevance |
|---|---|---|
| PCI DSS | Payment card data processing | Retail, financial services |
| GDPR | EU personal data | Any organization serving EU residents |
| HITRUST CSF | Healthcare information | US healthcare organizations |
| CSA STAR | Cloud security | General cloud security assurance |
| DoD IL2/IL4/IL5 | US Department of Defense | Defense contractors |
| IRAP | Australian government data | Australian public sector |
| C5 | German federal data | German public sector |

---

## Section 3 — Azure Policy

### 3.1 Overview and Purpose

Azure Policy is a governance service that evaluates resources against organizational rules and enforces compliance. It operates at the control plane — it acts when resources are created, modified, or evaluated on a recurring schedule.

Azure Policy answers the question: are our Azure resources deployed and configured in the way we have defined as correct?

### 3.2 Policy Definitions

A policy definition is a JSON document specifying a mode (which resource types to evaluate), parameters (variables for reuse), and a policy rule (an if-then condition).

Example use cases include requiring all storage accounts to use HTTPS only, restricting VM deployments to approved regions, requiring a specific tag on all resource groups, mandating that VMs use managed disks, and enforcing that SQL databases have Transparent Data Encryption enabled.

### 3.3 Policy Effects

The effect determines what Azure does when a resource violates the policy condition.

| Effect | Behavior | Common Use Case |
|---|---|---|
| Deny | Blocks the noncompliant create or update | Enforce required configurations |
| Audit | Allows the action, marks resource noncompliant | Visibility without blocking |
| AuditIfNotExists | Audits if a related resource is missing | Detect missing dependent resources |
| DeployIfNotExists | Auto-deploys a missing related resource | Ensure required agents or extensions exist |
| Modify | Changes resource properties automatically | Add required tags automatically |
| Disabled | Policy defined but not enforced | Testing or temporary suspension |

### 3.4 Policy Assignments

A policy definition becomes active only when assigned to a scope. Scope levels from broadest to narrowest are Management Group, Subscription, Resource Group, and individual Resource.

Assignments inherit downward — a policy assigned to a Management Group applies to all subscriptions, resource groups, and resources beneath it unless explicitly excluded.

Exclusions allow specific child scopes to be exempt from an assignment. For example, a sandbox resource group can be excluded from a policy that blocks noncompliant configurations in production.

### 3.5 Initiative Definitions

An initiative definition (also called a policy set) groups multiple policy definitions into a single assignable package, simplifying management when a compliance framework requires dozens of individual policies.

Microsoft provides built-in initiatives for major frameworks including the Azure Security Benchmark, NIST SP 800-53, HIPAA/HITRUST, FedRAMP High, and ISO 27001:2013. Assigning an initiative produces a compliance report showing what percentage of resources meet each included policy.

### 3.6 Compliance Dashboard

The Azure Policy compliance dashboard provides an at-a-glance view of compliance state including overall compliance percentage (compliant resources divided by total resources), per-policy compliance breakdown, per-resource compliance status, and non-compliant resource lists with remediation links.

Compliance state is recalculated every 24 hours or when resources are created or modified.

### 3.7 Remediation Tasks

For policies with DeployIfNotExists or Modify effects, Azure Policy can create remediation tasks that apply the policy effect retroactively to already-deployed noncompliant resources. Remediation tasks require a managed identity with sufficient permissions to modify target resources.

---

## Section 4 — Azure Blueprints

### 4.1 Overview

Azure Blueprints is a service for defining, publishing, and deploying a repeatable, governed Azure environment. A blueprint packages together all the components needed to stand up a compliant subscription: policies, role assignments, resource groups, and ARM templates.

### 4.2 Blueprint Artifacts

A blueprint is composed of one or more artifacts, each of which is one of four types.

| Artifact Type | Purpose |
|---|---|
| Role Assignment | Assigns Azure AD identities to RBAC roles on deployed resources |
| Policy Assignment | Applies a policy definition or initiative to the blueprint scope |
| Resource Group | Creates resource groups within the subscription |
| ARM Template | Deploys specific Azure resources such as VMs, VNets, and storage accounts |

### 4.3 Blueprint Lifecycle

The blueprint lifecycle has three distinct phases.

**Define** — Create the blueprint, add artifacts, and configure parameters. The blueprint exists as a draft.

**Publish** — Assign a version number and lock the blueprint definition. Published blueprints can be assigned to subscriptions. Versioning enables rollback to a previous version.

**Assign** — Link the published blueprint to one or more subscriptions. This triggers deployment of all artifacts in dependency order.

### 4.4 Blueprint Locking

Blueprint assignment supports a locking mode that prevents resources deployed by the blueprint from being modified or deleted outside an authorized blueprint update.

Do Not Lock allows resources to be modified freely after deployment. Do Not Delete prevents resources from being deleted but allows modification. Read Only prevents any modification or deletion.

### 4.5 Blueprints vs ARM Templates vs Azure Policy

| Tool | Primary Purpose | Tracks Deployed Resources? |
|---|---|---|
| ARM Template | Deploy Azure resources | No |
| Azure Policy | Enforce rules on resources | No |
| Azure Blueprints | Package and deploy a governed environment | Yes — maintains assignment relationship |

---

## Section 5 — Microsoft Purview

### 5.1 Overview

Microsoft Purview is a unified data governance and compliance platform. It addresses the challenge of knowing where your data is, what it contains, and whether it is being handled appropriately. It brings together capabilities previously split across Azure Purview and the Microsoft 365 Compliance Center.

### 5.2 Data Map

The Purview Data Map automatically scans registered data sources and builds a metadata catalog of discovered assets. Supported sources include Azure Data Lake Storage, Azure SQL Database, Azure Synapse Analytics, Azure Blob Storage, on-premises SQL Server, Power BI, and third-party sources.

### 5.3 Automated Classification

Purview applies automated classification using built-in system classifiers that detect sensitive data patterns including Social Security Numbers, credit card numbers, passport numbers, medical record identifiers, email addresses, phone numbers, and GDPR-relevant personal data fields. Custom classifiers can be created using regular expressions or dictionary-based matching for organization-specific patterns.

### 5.4 Data Catalog

The Data Catalog is the searchable interface built on the Data Map. Users can search for data assets by name, business glossary term, classification, or data source. Each asset has a profile page showing its schema, classifications, lineage, and stewardship contacts.

### 5.5 Data Lineage

Data lineage tracks how data flows from source systems through transformation processes to downstream consumers. Purview captures lineage from Azure Data Factory pipelines, Synapse Analytics, and Azure Machine Learning. Lineage diagrams support both impact analysis and compliance evidence showing where personal data travels through an organization.

### 5.6 Information Protection and Data Loss Prevention

Within the compliance scope, Purview provides sensitivity labels (Confidential, Highly Confidential, etc.) that trigger protection policies, Data Loss Prevention policies that detect and prevent sharing of sensitive information through email and collaboration tools, and records management with retention and disposition policies for regulated records.

### 5.7 Compliance Manager

Compliance Manager within Purview assesses your environment against regulatory frameworks and produces a Compliance Score. It provides pre-built assessments for 300+ regulations including GDPR, ISO 27001, HIPAA, and NIST; automated checks against Microsoft 365 and Azure configurations; manual improvement actions with step-by-step guidance; and progress tracking toward certification targets.

---

## Section 6 — Data Residency, Sovereignty, and GDPR

### 6.1 Data Residency

Data residency refers to the physical or geographic location where data is stored. Many regulations require that specific categories of data remain within a defined geographic boundary. Examples include EU personal data under GDPR, German financial data under BAIT, and Australian government data under the ISM.

Azure addresses data residency through its global region architecture. Data stored in a region stays in that region unless the customer explicitly configures replication to another region.

### 6.2 Paired Regions

Azure regions are organized into regional pairs. Business continuity replication stays within the region pair — East US pairs with West US, UK South pairs with UK West. This ensures that even during geo-redundant replication, data stays within the same geographic boundary, which is important for data residency requirements.

### 6.3 Sovereign Clouds

Azure operates separate cloud environments for jurisdictions with strict data sovereignty requirements.

| Cloud | Jurisdiction | Operator |
|---|---|---|
| Azure Government | US federal, state, local | Microsoft (US persons only) |
| Azure China | China | 21Vianet (independent operator) |

### 6.4 GDPR Overview

The General Data Protection Regulation (GDPR), effective May 2018, is the EU's comprehensive data protection law. Key principles include lawfulness and transparency (processing must have a legal basis and be communicated clearly), purpose limitation (data collected for one purpose cannot be used for another), data minimization (collect only what is necessary), accuracy (keep data correct), storage limitation (do not retain data longer than needed), integrity and confidentiality (protect data with appropriate security), and accountability (demonstrate compliance).

GDPR applies to any organization that processes personal data of EU residents, regardless of where the organization is located.

### 6.5 GDPR and Azure

Azure supports GDPR compliance through the Data Processing Addendum (contractual GDPR obligations between Microsoft and customers), tools for data subject request fulfillment (locate, export, and delete personal data), Azure region selection that keeps EU personal data in EU geography, breach notification to customers within 72 hours of discovering a breach, and a Privacy Dashboard for reviewing and managing personal data Microsoft holds about accounts.

---

## Key Terms Glossary

**Microsoft Trust Center** — Public portal for Microsoft's security, privacy, and compliance documentation.

**Service Trust Portal** — Authenticated portal for downloading audit reports and compliance evidence.

**ISO 27001** — International standard for information security management systems.

**SOC 2 Type II** — Third-party audit assessing the operating effectiveness of controls over a period of time.

**FedRAMP** — US government framework for authorizing cloud services for federal agency use.

**HIPAA BAA** — Business Associate Agreement required when a cloud provider handles protected health information.

**Azure Policy** — Service that enforces rules on Azure resource configurations through effects such as Deny, Audit, and DeployIfNotExists.

**Initiative Definition** — A collection of Azure policy definitions grouped to achieve a compliance goal.

**Azure Blueprints** — Service for packaging and deploying governed Azure environments with versioning and assignment tracking.

**Microsoft Purview** — Unified data governance and compliance platform for data discovery, classification, lineage, and information protection.

**Data Residency** — The geographic location where data is physically stored.

**GDPR** — EU regulation governing the privacy and security of personal data of EU residents.

**Data Processing Addendum** — Contractual document in which Microsoft commits to GDPR obligations for Azure customers.

---

## AZ-900 Exam Key Distinctions

- Trust Center is public transparency. Service Trust Portal requires sign-in for downloadable audit reports.
- Azure Policy enforces configurations (deny, audit, remediate). Azure Blueprints packages policies plus resources plus roles for consistent environment deployment.
- Blueprints track deployed resources and maintain an assignment relationship; ARM templates do not.
- HIPAA has no formal certification — compliance is demonstrated through a signed BAA and correct configuration.
- FedRAMP High is the highest US federal authorization level for cloud services.
- GDPR applies to EU personal data regardless of where the processing organization is located.
- Data residency = where data is stored. Data sovereignty = which laws govern data in that location.

---

## Review Questions

1. What is the difference between the Microsoft Trust Center and the Service Trust Portal?
2. What is a Business Associate Agreement and why is it required for HIPAA compliance?
3. Describe the difference between a SOC 2 Type I and SOC 2 Type II report.
4. What are the five most important policy effects in Azure Policy and what does each one do?
5. What is an initiative definition in Azure Policy?
6. How does Azure Blueprints differ from an ARM template in terms of post-deployment governance?
7. What are the four artifact types that can be included in an Azure Blueprint?
8. What does Microsoft Purview's Data Map do?
9. What is data residency and how does Azure's region architecture support it?
10. Name four key GDPR principles and describe each in one sentence.

---

*Texas Wesleyan University — CIS-4331 Azure Cloud Computing — Module 15 Reading Guide*

---

## 9. Supplemental Resources

1. Microsoft Service Trust Portal — downloadable audit reports, compliance guides, and shared responsibility matrices for ISO 27001, SOC 2, PCI DSS, FedRAMP, HIPAA, and other frameworks: https://servicetrust.microsoft.com

2. Azure compliance documentation — overview of compliance offerings, regulatory frameworks supported, and compliance resources by industry and region: https://learn.microsoft.com/en-us/azure/compliance/

3. Microsoft Purview compliance portal documentation — data classification, sensitivity labels, compliance score, and regulatory compliance assessment tools: https://learn.microsoft.com/en-us/purview/purview-compliance-portal

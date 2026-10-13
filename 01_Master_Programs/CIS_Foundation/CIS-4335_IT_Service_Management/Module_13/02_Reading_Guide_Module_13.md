# Reading Guide: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Overview

IT Asset Management (ITAM) is the ITIL 4 practice responsible for planning and managing the full lifecycle of all IT assets to help the organization maximize value, control costs, manage risks, support decision-making, and meet regulatory and contractual requirements. It is a foundational practice — without accurate knowledge of what assets the organization owns, how they are configured, and what their license terms require, every other management practice operates on incomplete information.

Use this guide alongside the Module 13 video lecture and ITIL 4 Foundation study resources.

---

## Purpose of IT Asset Management

ITIL 4 defines the purpose of IT Asset Management as:

> To plan and manage the full lifecycle of all IT assets to help the organization maximize value, control costs, manage risks, support decision-making about purchase, reuse, retirement, and disposal, and meet regulatory and contractual requirements.

This purpose statement contains four distinct objectives that are each worth examining.

**Maximize value** — Assets should be acquired when needed and fully utilized before being replaced. Assets that sit unused represent purchased value that is not being realized. Assets that are used beyond their useful life create reliability and security risk.

**Control costs** — IT assets represent significant capital and operational expenditure. Over-licensed software, underutilized hardware, and missed maintenance renewals all represent controllable cost failures. Accurate asset data enables informed purchasing decisions.

**Manage risks** — Assets that are untracked cannot be secured. Assets whose license terms are not understood create compliance exposure. Assets that are disposed of without data sanitization create data breach risk.

**Meet regulatory and contractual requirements** — Many regulatory frameworks — including SOX, HIPAA, PCI-DSS, and ISO 27001 — require organizations to maintain accurate inventories of assets that process or store regulated data. License agreements are contracts — violating them through unauthorized use creates legal liability.

---

## The IT Asset Lifecycle

Every IT asset passes through a defined lifecycle. The purpose of lifecycle management is to apply the right management attention at each stage and to ensure smooth, documented transitions between stages.

### Stage 1: Planning

Planning establishes that an asset is needed before it is acquired. This stage connects to financial planning, technology roadmaps, and capacity planning. Planning questions include: Is this asset already owned in a different location? Does an existing license cover this use? Is this the right time to buy, or should procurement wait for a contract renewal?

### Stage 2: Procurement

Procurement is the acquisition of the asset. At procurement, the asset receives its initial identity record: asset tag, description, vendor, cost, license terms, warranty period, and assigned owner. This record is the foundation of all subsequent lifecycle management.

### Stage 3: Deployment

The asset is configured and put into active use. Deployment triggers registration in the Configuration Management Database (CMDB) with attributes and relationships recorded. An asset that is deployed without being recorded in the CMDB is invisible to asset management and every other practice that depends on asset data.

### Stage 4: Maintenance and Operation

The asset is in active service. This stage is typically the longest stage in the lifecycle. Management activities include patch and update management, hardware maintenance contracts, license compliance monitoring, and periodic asset audits. The asset record in the CMDB should be kept current throughout this stage — changes in configuration, location, assignment, or license status should trigger record updates.

### Stage 5: Retirement

The asset is removed from active service. Retirement may be triggered by end of vendor support (hardware or software reaching end-of-life), technology obsolescence, or organizational change. Retirement decisions should consider whether the asset can be redeployed elsewhere, sold, donated, or must be disposed of.

### Stage 6: Disposal

The asset is permanently removed from the organization's inventory. Disposal must include data sanitization for any asset that has stored data. The CMDB record is closed. License entitlements associated with the asset are decommissioned or reallocated. A certificate of destruction or disposal is retained for audit purposes.

---

## The Configuration Management Database

### What Is the CMDB?

The Configuration Management Database (CMDB) is the authoritative repository of information about configuration items (CIs) and their relationships. A configuration item is any component that must be managed in order to deliver an IT service. The CMDB stores:

- Individual CI records with attributes (type, model, serial number, owner, location, status)
- Relationships between CIs (Server A hosts Application B; Application B supports Service C)
- History of changes made to each CI

The CMDB is the foundation for several critical ITSM practices:

| Practice | How It Uses the CMDB |
|---|---|
| Change Management | Impact analysis — which services are affected by a proposed change |
| Incident Management | Asset identification — which CI is involved in a reported failure |
| Problem Management | Root cause investigation — which CI is the source of recurring incidents |
| IT Asset Management | Asset tracking — what is owned, where it is, and what its status is |
| Information Security | Asset inventory — ensuring all assets are within security control scope |

### CMDB Accuracy

The CMDB is only valuable when accurate. An inaccurate CMDB generates incorrect impact assessments, misleads incident response, and gives false confidence to compliance audits. Common CMDB accuracy problems include:

- Assets deployed without being recorded
- Decommissioned assets not removed from the CMDB
- Relationships not maintained when configurations change
- Manual records drifting from actual state over time

### Asset Discovery Tools

Discovery tools address CMDB accuracy by automatically scanning the network and identifying hardware and software present in the environment. Discovery feeds supplement and validate manually maintained records. Key capabilities include:

- Network scanning to identify all connected devices
- Software inventory scanning to identify installed applications and versions
- Cloud asset discovery to enumerate virtual machines, storage, and services
- Comparison with CMDB records to identify discrepancies (assets in CMDB not found in scan; assets found in scan not in CMDB)

Discovery tools should be run on a regular schedule — typically daily or weekly — to maintain CMDB currency. Newly discovered assets that are not in the CMDB trigger an investigation and record creation. Assets in the CMDB that are no longer discovered trigger a verification and potential retirement.

---

## Software Asset Management

Software Asset Management (SAM) is the discipline within ITAM focused on managing software licenses throughout their lifecycle. SAM operates at the intersection of financial management, legal compliance, and operational control.

### The Two SAM Risks

**Under-licensing** occurs when an organization uses more software than it has licensed. This creates legal liability — the organization is in breach of its license agreement and is exposed to audit penalties, retroactive license fees, and reputational harm.

**Over-licensing** occurs when an organization has purchased more licenses than it uses. This wastes money — budget is allocated to software that provides no value. Over-licensing is often the result of bulk purchasing without tracking actual usage, or of failing to decommission licenses when users leave the organization.

Effective SAM reduces both risks simultaneously by maintaining accurate records of what is licensed and what is actually installed and used.

### Software License Models

| License Model | Description | Compliance Measurement |
|---|---|---|
| Per-device | One license per installation | Count of installations |
| Per-user (named user) | One license per authorized user | Count of authorized users |
| Concurrent (floating) | Licensed for N simultaneous users | Peak concurrent usage |
| Subscription | Time-limited right to use | Renewal tracking; lapse = non-compliance |
| Site license | Unlimited use within defined scope | Scope boundary adherence |
| OEM | Tied to specific hardware | Retirement tracks with hardware |

### Software License Audits

Software vendors have the contractual right to audit their customers' software usage. Major vendors — including Microsoft, Oracle, IBM, and Adobe — conduct periodic audits. Audit preparation requires:

- An accurate, current software inventory with installation counts
- License entitlement records (purchase orders, license certificates, subscription confirmations)
- A reconciliation showing that entitlements cover actual usage
- Records of decommissioned licenses from retired systems

Organizations with mature SAM programs can respond to an audit request with a complete, accurate reconciliation. Organizations without SAM programs typically discover their under-licensing problem during the audit — at which point the vendor has significant negotiating leverage.

---

## Secure Asset Disposal

Secure disposal is the final stage of the asset lifecycle. Its importance is often underestimated because by the time an asset is being disposed of, it is no longer producing value — the operational focus has moved on. But the risk of improper disposal is significant.

### Data Sanitization Methods

**Physical destruction** destroys the storage media itself — shredding, degaussing, or incineration. Physical destruction is the most certain method. It is appropriate for media containing highly sensitive data (classified information, healthcare records, financial data) where the risk of any recovery is unacceptable. Hardware destroyed by this method has no residual value.

**Cryptographic erasure** destroys the encryption key for a self-encrypting drive. All data on the drive is rendered unreadable because the key required to decrypt it no longer exists. This method is fast and preserves the hardware for reuse or resale. It is only applicable to self-encrypting drives.

**Software-based overwriting** uses approved algorithms to overwrite storage media with random data, following standards such as NIST SP 800-88. Multiple overwrite passes are required for spinning disk media. SSD overwriting requires manufacturer-specific tools because of how flash memory manages data blocks.

### Certificates of Destruction

For every asset disposed of, the organization should retain a record that documents: the asset identifier, the disposal date, the sanitization method used, and the name of the party that performed sanitization (internal or vendor). This certificate serves as evidence in compliance audits and demonstrates that the organization met its data protection obligations.

### Regulatory Requirements

Several regulatory frameworks impose specific requirements on asset disposal:

- **HIPAA** requires that electronic protected health information (ePHI) be rendered unreadable and indecipherable prior to disposal of hardware
- **PCI-DSS** requires that media containing cardholder data be destroyed when no longer needed for business or legal reasons
- **GDPR** requires that personal data be erased in a manner that renders it permanently unrecoverable when the lawful basis for processing no longer exists

---

## Key Terms for the ITIL 4 Foundation Exam

| Term | Definition |
|---|---|
| IT asset | Any financially valuable component that can contribute to the delivery of an IT product or service |
| Asset lifecycle | The stages an asset passes through from planning and procurement to disposal |
| Configuration item (CI) | Any component that needs to be managed in order to deliver a service |
| CMDB | Configuration Management Database — authoritative record of CIs and their relationships |
| Software Asset Management (SAM) | Discipline managing software licenses throughout their lifecycle |
| Under-licensing | Using more software than licensed — creates legal and compliance risk |
| Over-licensing | Purchasing more licenses than needed — creates financial waste |
| Discovery tool | Automated scanning tool that identifies hardware and software in an environment |
| Secure disposal | Removal of assets with data sanitization to prevent unauthorized data recovery |
| Certificate of destruction | Documentation proving secure sanitization of disposed hardware |

---

## Study Questions

1. What are the four objectives in the ITIL 4 definition of IT Asset Management's purpose?

2. What is the difference between a configuration item and an IT asset?

3. Why does CMDB inaccuracy create risk rather than just inconvenience?

4. What are the two risks that Software Asset Management is designed to control, and which one creates legal exposure?

5. A laptop assigned to a departing employee is being returned to the IT department. It contains customer records. Which data sanitization method is most appropriate if the laptop will be refurbished and reissued to a new employee?

6. What is a software license audit and why should organizations with mature SAM programs have less to fear from one?

7. How does the CMDB support Change Management's impact analysis function?

---

## Supplemental Resources

**1. AXELOS — ITIL 4 IT Asset Management Practice**
<https://www.axelos.com/resource-hub/blog/it-asset-management-practice>
Official AXELOS overview of the IT Asset Management practice in ITIL 4, covering the purpose, key activities, CMDB integration, and relationship to Service Configuration Management. Essential reference for understanding how ITAM fits within the broader ITIL 4 framework.

**2. NIST SP 800-88 — Guidelines for Media Sanitization**
<https://csrc.nist.gov/publications/detail/sp/800-88/rev-1/final>
The authoritative U.S. government standard for data sanitization methods — clear, purge, and destroy — with specific guidance on cryptographic erasure for encrypted media. Directly relevant to the secure disposal section of this module and referenced in HIPAA compliance guidance.

**3. ITAM Forum — Software Asset Management Best Practices**
<https://www.itassetmanagement.net/best-practices/>
Practitioner-focused resource from the IT Asset Management Forum covering SAM program maturity, license reconciliation workflows, vendor audit preparation, and over/under-licensing risk management. Provides real-world context for the SAM concepts covered in this module.

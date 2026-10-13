# Video Script: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation

---

## Slide 1: Introduction (0:00–0:45)

Welcome to Module 13 of CIS-4335. I'm Professor Nash. This module covers IT Asset Management — one of the most foundational and often underestimated practices in IT Service Management.

When organizations cannot answer basic questions like "How many laptops do we own?", "Are all our software licenses in compliance?", or "What servers are running in our data center?", they face financial waste, security vulnerabilities, and regulatory risk. IT Asset Management exists to answer those questions systematically.

By the end of this video you will understand the asset lifecycle, the role of the Configuration Management Database, asset discovery, software asset management, license compliance, and responsible disposal.

---

## Slide 2: What Is IT Asset Management? (0:45–2:00)

ITIL 4 defines IT Asset Management as the practice responsible for planning and managing the full lifecycle of all IT assets, to help the organization maximize value, control costs, manage risks, support decision-making about purchase, re-use, retirement, and disposal, and meet regulatory and contractual requirements.

Notice several things in this definition:

- It is explicitly **lifecycle** focused — from acquisition to disposal.
- It is about **value and cost** — not just inventory.
- It explicitly includes **regulatory and contractual** requirements — particularly relevant for software licensing.

An **IT asset** is any financially valuable component that can contribute to the delivery of an IT product or service. This includes hardware (laptops, servers, networking equipment), software (operating systems, applications, SaaS subscriptions), cloud resources, and even intellectual property such as code licenses.

---

## Slide 3: The IT Asset Lifecycle (2:00–4:15)

Every IT asset passes through six lifecycle stages. Understanding these stages is critical for both ITAM practitioners and the ITIL 4 Foundation exam.

### Stage 1: Request and Acquisition

The lifecycle begins before ownership. During this stage:

- A business need is identified and justified.
- A purchase request is submitted and approved.
- Procurement selects a vendor and negotiates terms.
- The asset is purchased, leased, or provisioned (in the case of cloud or SaaS).

At acquisition, the asset should be immediately registered in the asset management system. Too many organizations skip this step and spend enormous effort later trying to reconcile physical hardware with incomplete records.

### Stage 2: Deployment

The asset is prepared for use: hardware is imaged and configured, software is installed and licensed, network connectivity is established. The CMDB is updated to reflect the new asset's existence, attributes, and relationships.

### Stage 3: Operation and Maintenance

This is the longest phase. The asset is in active use. During operation:

- Regular maintenance, patching, and upgrades occur.
- License compliance is monitored.
- Asset utilization is tracked (are resources being used or wasted?).
- Physical location and user assignment are kept current.

### Stage 4: Refresh or Replacement Decision

Assets age. Hardware performance degrades; software reaches end-of-support. At this stage, the organization evaluates whether to refresh (upgrade/extend life) or replace (retire and procure new). This decision should be data-driven — pulling from maintenance cost trends and utilization metrics.

### Stage 5: Retirement

When an asset is no longer needed, it is formally decommissioned. This includes removing software licenses from the asset, returning cloud resources, and removing the asset from active configuration records.

### Stage 6: Disposal

Physical assets require secure disposal. Data must be sanitized or destroyed before hardware leaves the organization's control. Regulatory requirements (HIPAA, GDPR, PCI-DSS) often mandate documented evidence of secure data destruction.

---

## Slide 4: The Configuration Management Database (4:15–6:30)

The CMDB is one of the most important concepts in ITIL — and one of the most misunderstood.

A **Configuration Management Database** is a repository that stores information about **configuration items (CIs)** — the components that make up the IT environment. A CI can be a server, an application, a network device, a database, a service, or even a document.

The CMDB does not just list assets. It captures **relationships** between CIs:

- This server **runs** this application.
- This application **depends on** this database.
- This service **is composed of** these infrastructure components.

These relationships are what make the CMDB powerful. When an incident occurs, CMDB relationship maps help analysts understand which services are affected by a failing component. When a change is planned, the CMDB reveals downstream dependencies that must be considered.

### CMDB vs. Asset Register

Students often confuse these two. An **asset register** is a financial and inventory record — it tracks ownership, cost, depreciation, and lifecycle stage. A **CMDB** is an operational record — it tracks attributes, relationships, and current state of CIs used to deliver services.

Many organizations maintain both. Some CIs are also assets (a server is both financially tracked and operationally tracked). Some assets are not CIs (a spare laptop in storage has financial value but is not actively delivering services). Some CIs are not financial assets in the traditional sense (a running database instance may be part of a licensed product tracked elsewhere).

### CMDB Data Quality

A CMDB is only as valuable as its data quality. Stale or inaccurate CMDB records are often worse than no CMDB — they create false confidence and lead engineers to make decisions based on wrong information. CMDB data quality must be actively maintained through discovery tools, process discipline, and periodic audits.

---

## Slide 5: Asset Discovery Tools (6:30–8:15)

Manual asset inventory processes are unsustainable at scale. Organizations use automated discovery tools to find and catalog assets across their environments.

### Network-Based Discovery

Tools like **Lansweeper**, **Nmap**, and **SolarWinds Network Topology Mapper** scan IP address ranges and identify connected devices. They can enumerate open ports, running services, and basic hardware characteristics.

### Agent-Based Discovery

Agent software deployed on endpoints collects detailed hardware and software inventory: CPU, RAM, disk, installed applications, running processes, and license keys. **Microsoft Endpoint Configuration Manager (MECM)**, **Tanium**, and **Flexera** use this approach.

### Cloud Asset Discovery

For cloud environments, native services like **AWS Config**, **Azure Policy**, and **Google Cloud Asset Inventory** continuously monitor resource provisioning and attribute changes. These integrate with ITSM platforms to automatically create and update CIs.

### Reconciliation

Discovery tools generate raw data. Asset managers must reconcile discovered assets against the asset register:

- **Known and found** — in the register and in the environment. No action needed.
- **Known but not found** — in the register but not discovered. Investigate: decommissioned but not recorded? Stolen? Network-isolated?
- **Found but not known** — discovered but not in the register. Register immediately; investigate origin.

The "found but not known" category — sometimes called **shadow IT** — is a significant security and compliance risk.

---

## Slide 6: Software Asset Management and License Compliance (8:15–10:45)

Software asset management (SAM) is a subset of IT Asset Management focused specifically on software — the licenses, installations, and usage rights.

### Why SAM Matters

Software licensing is complex and expensive. Large organizations can spend millions of dollars annually on software licenses. Without SAM:

- Organizations risk **under-licensing** — using more copies than they paid for. This exposes them to vendor audits and significant financial penalties.
- Organizations risk **over-licensing** — paying for more licenses than they use. This is pure waste.
- End-of-life software runs without support contracts, creating security vulnerabilities.

### License Types

Understanding license types is foundational to SAM:

- **Per-seat (per user):** One license per named user, regardless of device count.
- **Per device:** One license per device; users may share devices.
- **Concurrent (floating):** A pool of licenses; only users actively using the software at a given moment consume a license.
- **Subscription:** Periodic payment for time-limited access (most SaaS).
- **OEM:** License tied to the hardware it shipped with; not transferable.
- **Enterprise Agreement (EA):** Negotiated contract covering a defined quantity across the organization.

### License Compliance Process

Maintaining compliance requires three steps:

1. **Entitlement management:** Know exactly what licenses you own — purchase orders, agreements, certificates of authenticity.
2. **Usage tracking:** Know exactly what is installed and being used — from discovery tools.
3. **Reconciliation:** Compare entitlements to usage. If usage exceeds entitlements, purchase additional licenses. If entitlements exceed usage, evaluate whether licenses can be reduced at next renewal.

---

## Slide 7: Asset Disposal (10:45–12:30)

Disposal is the most risk-laden phase of the asset lifecycle from a security and regulatory perspective.

### Data Sanitization Methods

Before any hardware leaves organizational control, data must be removed beyond recovery:

- **Overwriting:** Software tools write random data patterns over all storage sectors multiple times. Suitable for spinning hard drives.
- **Degaussing:** A strong magnetic field disrupts magnetic media, erasing data. Renders drives inoperable.
- **Physical destruction:** Shredding, crushing, or incinerating storage media. Required for classified or highly sensitive data and for solid-state storage where overwriting may not reach all cells.

### Chain of Custody Documentation

Responsible disposal requires a documented chain of custody:

- Identification of asset (serial number, asset tag).
- Data destruction method and date.
- Witness or technician signature.
- Certificate of destruction from a qualified disposal vendor (if outsourced).

This documentation is audit evidence. Regulatory frameworks including HIPAA, PCI-DSS, and GDPR require organizations to demonstrate that data was destroyed securely.

### Environmental Responsibility

IT equipment contains hazardous materials — lead, mercury, cadmium. Disposal must comply with local environmental regulations. Certified e-waste recyclers (R2 or e-Stewards certified) provide environmentally responsible processing and typically provide certificates of recycling.

---

## Slide 8: IT Asset Management in the ITIL 4 SVS (12:30–14:00)

IT Asset Management is categorized in the **General Management** practice group within ITIL 4 — reflecting that it spans IT and business domains.

Key integrations:

- **Service Configuration Management** shares the CMDB as a common tool. ITAM populates financial and lifecycle data; SCM populates operational relationships.
- **Change Enablement** relies on ITAM data to assess the financial and regulatory impact of proposed changes.
- **Supplier Management** tracks vendor contracts and license agreements that ITAM monitors for compliance.
- **Information Security Management** depends on ITAM's hardware and software inventory to identify unpatched, end-of-life, or unauthorized assets.

The **SVS guiding principle** most relevant to ITAM is **"Start where you are"** — many organizations already have asset data in spreadsheets, procurement systems, and help desk tools. A mature ITAM program consolidates and enriches these existing data sources rather than starting from scratch.

---

## Slide 9: Key Terms Summary (14:00–15:15)

Key vocabulary:

- **IT asset** — financially valuable component contributing to service delivery.
- **Asset lifecycle** — request/acquisition, deployment, operation, refresh/replace, retirement, disposal.
- **CMDB** — repository of configuration items and their relationships.
- **Configuration item (CI)** — any component managed to deliver a service.
- **Asset register** — financial and inventory record of owned assets.
- **Asset discovery** — automated tools that find and catalog assets in the environment.
- **Shadow IT** — assets found but not in the official register.
- **Software Asset Management (SAM)** — management of software licenses, installations, and usage rights.
- **License compliance** — matching entitlements owned to installations in use.
- **Data sanitization** — overwriting, degaussing, or physical destruction of data before disposal.
- **Certificate of destruction** — documented evidence of secure data removal.

---

## Slide 10: Closing and Preview (15:15–16:00)

That's Module 13. You can now describe the full IT asset lifecycle, explain the CMDB and its relationship to the asset register, understand how discovery tools find and reconcile assets, manage software license compliance, and handle disposal responsibly.

In Module 14 we move to Risk and Compliance in IT Service Management — including risk registers, regulatory frameworks like ISO 27001 and SOC 2, and how ITIL integrates with audit preparation.

Complete the reading guide, lab, and quiz. See you in Module 14.

---

*End of Module 13 Video Script — approximately 235 lines*

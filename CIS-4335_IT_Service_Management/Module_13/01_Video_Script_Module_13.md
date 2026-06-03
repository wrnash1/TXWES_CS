# Video Script: Module 13 — IT Asset Management

## Course: CIS-4335 IT Service Management

## Texas Wesleyan University | Professor Nash

**Certification Alignment:** ITIL 4 Foundation
**Estimated Duration:** 22–25 minutes
**Recorded by:** Professor Nash

---

## Production Notes

- Slides advance on each bracketed cue.
- [SHOW DIAGRAM] cues indicate points where a visual must appear on screen.
- [PAUSE] cues indicate natural break points for student note-taking.

---

## Section 1: Welcome and Module Overview [00:00 - 02:30]

Welcome to Module 13. I am Professor Nash. Today we are covering IT Asset Management — a practice that sounds administrative on the surface but is absolutely foundational to how an organization controls its costs, manages its risk, and maintains regulatory compliance.

[SHOW DIAGRAM: Title slide — "Module 13: IT Asset Management" with ITIL 4 SVS label and ITIL 4 Foundation certification badge]

Every organization owns or licenses technology assets — servers, laptops, switches, software licenses, cloud subscriptions, mobile devices, virtual machines. IT Asset Management is the practice that ensures those assets are tracked, managed, and disposed of in a way that maximizes value and minimizes risk throughout the asset lifecycle. ITIL 4 defines this practice as ensuring that the value of IT assets is maximized, costs are controlled, risks are managed, and decisions about purchasing, reuse, retirement, and disposal are made based on accurate, complete asset information.

By the end of this module you will be able to: define the purpose of IT Asset Management, describe the asset lifecycle, explain the role of the Configuration Management Database, identify software license compliance risks, and describe secure asset disposal requirements.

---

## Section 2: The IT Asset Lifecycle [02:30 - 07:30]

[SHOW DIAGRAM: Asset lifecycle wheel — six stages: Planning, Procurement, Deployment, Maintenance/Operation, Retirement, Disposal — arranged in a cycle with brief description of each stage]

An IT asset goes through a defined lifecycle from the moment it is considered for acquisition to the moment it is securely destroyed or transferred. Managing each stage of this lifecycle is what IT Asset Management is about.

**Stage 1: Planning.** Before an asset is purchased, the organization must establish that it is needed. Asset planning identifies requirements, aligns with technology roadmaps, and ensures that procurement is budgeted and approved. Without planning, organizations accumulate redundant assets — duplicate software licenses for the same function, servers that were bought for projects that never launched.

**Stage 2: Procurement.** Assets are acquired — purchased, leased, or licensed. Procurement records establish the asset's identity: what it is, how much it cost, what the license terms are, and who the vendor is. These records are the foundation of all subsequent asset tracking.

[PAUSE]

**Stage 3: Deployment.** The asset is configured, assigned to a user or system, and put into active use. At this stage the asset is registered in the CMDB — the Configuration Management Database — with its attributes, relationships, and ownership recorded.

**Stage 4: Maintenance and Operation.** The asset is in active service. During this stage it requires updates, patches, repairs, and periodic review. License compliance monitoring happens here — ensuring that software use stays within licensed limits.

**Stage 5: Retirement.** The asset reaches end of useful life or end of vendor support. It is removed from active service. Retirement triggers decisions about whether the asset will be redeployed, sold, donated, or disposed of.

**Stage 6: Disposal.** The asset is permanently removed from the organization's inventory. Secure disposal is critical — hardware that contains data must be sanitized before disposal. Software licenses must be decommissioned or transferred to avoid paying for unused entitlements.

---

## Section 3: The Configuration Management Database [07:30 - 12:30]

[SHOW DIAGRAM: CMDB architecture — central CMDB repository connected to: CI records (hardware, software, services, locations), relationships graph, discovery tool feeds, and consuming practices (Change Management, Incident Management, Problem Management, Asset Management)]

The Configuration Management Database — CMDB — is the authoritative repository of information about configuration items and their relationships. A configuration item (CI) is any component that needs to be managed in order to deliver a service. Hardware assets, software installations, cloud instances, network devices, and even documentation can be CIs.

The CMDB does not just store individual records — it stores the relationships between them. It knows that Server A hosts Application B, which is used by Service C, which is covered by SLA D. This relationship data is what makes the CMDB powerful for impact analysis. When a CI is about to change, impact analysis traces the relationships to understand what services and users will be affected.

[PAUSE]

The CMDB is only as valuable as its accuracy. An inaccurate CMDB is often worse than no CMDB — it creates false confidence. Organizations that rely on a CMDB with stale or incomplete data make change and incident decisions based on wrong information.

### Asset Discovery Tools

Keeping the CMDB accurate requires ongoing discovery. Asset discovery tools scan the network and automatically identify hardware and software present in the environment. Common tools include ServiceNow Discovery, Lansweeper, Microsoft Endpoint Configuration Manager, and open-source tools like OCS Inventory. Discovery tools feed the CMDB with current data — identifying new assets, flagging decommissioned assets that are still in the database, and detecting unauthorized software.

The integration between discovery tools and the CMDB is what enables continuous accuracy rather than point-in-time snapshots.

---

## Section 4: Software License Compliance and SAM [12:30 - 17:30]

[SHOW DIAGRAM: Software license compliance gap analysis — left column: licenses purchased (100), right column: installations detected (127), gap: 27 unlicensed installations → compliance risk + financial exposure]

Software asset management — SAM — is the subset of IT Asset Management focused specifically on managing software licenses throughout their lifecycle. SAM has two primary goals: ensuring the organization is not using software it has not licensed (under-licensing, which creates legal and compliance risk) and ensuring the organization is not paying for licenses it is not using (over-licensing, which wastes money).

### License Types

Software licensing is complex. Different license models create different compliance obligations.

Per-device licensing: each installation must be covered by a license. If you install the software on 50 machines, you need 50 licenses.

Per-user licensing: each named user accessing the software must be licensed. If the software is installed on 10 machines but accessed by 30 users, you need 30 licenses — not 10.

Concurrent or floating licensing: a defined number of simultaneous users can access the software at any one time. 20 concurrent licenses means 20 people can be logged in simultaneously — more people can be authorized, but only 20 at once.

Subscription licensing: the right to use the software is purchased for a period of time, not permanently. When the subscription expires, use must cease or be renewed.

[PAUSE]

### License Compliance Audits

Software vendors conduct audits — often without advance notice — to verify that customers are using their software within license terms. The consequences of non-compliance can include retroactive license fees, penalties, and reputational damage. SAM programs that maintain accurate entitlement records and regular compliance checks are the primary defense against audit exposure.

---

## Section 5: Secure Asset Disposal [17:30 - 20:30]

[SHOW DIAGRAM: Data sanitization methods — three boxes: Physical Destruction (shredding/degaussing — 100% unrecoverable), Cryptographic Wipe (software-based overwrite — recoverable with forensic tools if improperly done), Certificate of Destruction (vendor-provided documentation for audit trail)]

Secure disposal is one of the most overlooked risk areas in IT Asset Management. When hardware reaches end of life, it may contain sensitive data — customer records, employee information, financial data, intellectual property. If that hardware is disposed of without proper data sanitization, the data can be recovered.

ITIL 4 and information security frameworks including ISO 27001 require that hardware containing data undergo approved sanitization before disposal. The three main approaches are:

**Physical destruction** — the storage media is physically shredded, degaussed, or incinerated. This is the most certain method and is appropriate for highly sensitive data. Physical destruction is irreversible — the hardware has no resale value after destruction.

**Cryptographic erasure** — for self-encrypting drives, destroying the encryption key renders all data on the drive unreadable. This is fast and allows hardware to be resold or donated.

**Software-based overwriting** — data is overwritten multiple times using a recognized standard such as NIST SP 800-88. This is appropriate for standard hard drives and SSDs when the hardware will be reused or donated.

Documentation matters. Organizations should retain certificates of destruction or sanitization for every disposed asset — both for internal audit purposes and to demonstrate compliance to regulators.

---

## Section 6: Asset Management and the ITIL 4 SVS [20:30 - 22:30]

IT Asset Management connects to multiple other ITIL 4 practices. Change Management consults the CMDB to assess the impact of proposed changes on existing assets. Incident Management uses asset relationships to rapidly identify the source of failures. Financial Management relies on asset records for budgeting and cost allocation. Information Security Management depends on accurate asset inventories to ensure all assets are included in security controls.

The ITIL 4 guiding principle "Start with What You Exist" applies directly here. Asset Management builds on existing asset records, discovery data, and procurement systems — it does not require a blank-slate rebuild of every record.

---

## Section 7: Exam Reminders and Lab Preview [22:30 - End]

Three exam reminders. First: the CMDB tracks configuration items and their relationships — not just individual asset records. Second: SAM's two risks are under-licensing (compliance exposure) and over-licensing (financial waste). Third: secure disposal requires data sanitization with documentation — not just decommissioning the asset in the CMDB.

This week's lab places you in the role of an IT Asset Manager at a mid-sized organization. You will classify assets by lifecycle stage, identify license compliance gaps, and design a disposal procedure for retiring hardware.

---

## Module 13 Complete

Next: Module 14 — Risk and Compliance in ITSM

### Additional Resources

- axelos.com — ITIL 4 Foundation study materials
- itam.org — IT Asset Management Forum resources
- nist.gov — NIST SP 800-88 Guidelines for Media Sanitization
